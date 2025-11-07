from typing import Optional, Sequence, Union, TYPE_CHECKING
import logging
import json

from Hql.Compiler import Compiler, BranchDescriptor, InstructionSet
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions.References import NamedReference
from Hql.Types.Hql import HqlTypes as hqlt

if TYPE_CHECKING:
    from Hql.Query import Query
    from Hql.Config import Config
    from Hql.Context import Context
    from Hql.Hac import Hac
    import Hql

'''
Hql preprocessor
'compiles' out a set of pure-Hql expressions and operators
Works out preprocessor functions
'''
class HqlCompiler(Compiler):
    def __init__(self, config:'Config', query:Optional['Query']=None, hac:Optional['Hac']=None):
        Compiler.__init__(self)
        self.ctx.config = config
        self.root:Optional[InstructionSet] = None
        self.hac:Optional['Hac'] = hac

        if query:
            self.Query(query)

    def compile(self, src:Union['Hql.Operators.Operator', 'Hql.Expressions.Expression', 'Hql.Query.Statement', None], preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        if not src:
            logging.error('Access Hql root via HqlCompiler.root not default compiler')
            raise hqle.CompilerException('Hql compiler with default parameter')
        return self.from_name(src.type)(src)

    def run(self, ctx: Optional['Context'] = None) -> 'Context':
        ctx = ctx if ctx else self.ctx
        if not self.root:
            raise hqle.CompilerException('Attempting to run compiler with None-root')
        return self.root.eval(ctx, hac=self.hac)

    def Query(self, query: 'Hql.Query.Query', preprocess:bool=True):
        res = None
        for i in query.statements:
            res = self.compile(i)
            if res:
                break
        return res

    def Statement(self, statement: 'Hql.Query.Statement', preprocess:bool=True) -> Optional[InstructionSet]:
        logging.error("This shouldn't trigger? Compiling Statement directly")
        acc, _ = self.compile(statement.root)
        assert isinstance(acc, InstructionSet)
        return acc

    def QueryStatement(self, statement: 'Hql.Query.QueryStatement', preprocess:bool=True) -> InstructionSet:
        from Hql.Hac import Source
        from Hql.Operators import Database
        acc, _ = self.compile(statement.root)

        if isinstance(acc, InstructionSet):
            self.root = acc
        elif isinstance(acc, Source):
            self.root = acc.assemble()
        elif isinstance(acc, Database):
            self.root = InstructionSet(acc)
        else:
            raise hqle.CompilerException(f'QueryStatement compiled to {type(acc)} not InstructionSet, mistake?')
        
        return self.root

    def LetStatement(self, statement: 'Hql.Query.LetStatement', preprocess:bool=True) -> None:
        acc, _ = self.compile(statement.root)

        if not isinstance(acc, InstructionSet):
            acc = acc.get_expr()

        self.ctx.symbol_table[statement.name] = acc
        return None

    def Tabular(self, expr:Union['Hql.Operators.Range', 'Hql.Expressions.Expression', InstructionSet]) -> tuple[Optional[InstructionSet], Optional['Hql.Expressions.Expression']]:
        from Hql.Operators.Database import Database, Static
        from Hql.Expressions import DotCompositeFunction, NamedReference
        from Hql.Operators import Range, Datatable, Union
        from Hql.Hac import Source

        if isinstance(expr, InstructionSet):
            return expr, None

        elif isinstance(expr, Source):
            acc = expr.assemble()
        
        elif isinstance(expr, DotCompositeFunction):
            acc, _ = self.DotCompositeFunction(expr)

        elif isinstance(expr, NamedReference):
            acc = self.ctx.symbol_table[expr]

            if not isinstance(acc, (Database, InstructionSet)):
                acc = self.ctx.get_func('database')([]).eval(self.ctx)
                acc = acc.get_variable(expr)

        elif isinstance(expr, Range):
            acc, _ = self.Range(expr)
            op = acc.get_op()
            acc = Static(op.eval(self.ctx))

        elif isinstance(expr, Datatable):
            acc, _ = self.Datatable(expr)
            op = acc.get_op()
            acc = Static(op.eval(self.ctx))

        elif isinstance(expr, Union):
            upstream = []
            for i in expr.exprs:
                acc, rej = self.Tabular(i)
                if rej:
                    return None, expr
                assert acc
                
                if not acc.ops:
                    upstream += acc.upstream
                else:
                    upstream.append(acc)
            
            acc = InstructionSet(upstream=upstream)

        elif isinstance(expr, Database):
            acc = expr

        else:
            return None, expr

        if isinstance(acc, Source):
            acc = acc.assemble()

        if isinstance(acc, Database):
            acc = InstructionSet(acc)

        if not isinstance(acc, InstructionSet):
            assert not isinstance(expr, Range)
            return None, expr

        # Add hac timebound
        if self.hac:
            from Hql.Operators import Where
            from Hql.Expressions import BetweenEquality, Datetime, NamedReference

            start, end = self.hac.get_timerange()

            acc.add_op(
                Where(
                    BetweenEquality(
                        NamedReference('_hqltimestamp'),
                        Datetime(start),
                        Datetime(end),
                        'between'
                    )
                )
            )

        return acc, None

    def PipeExpression(self, expr: 'Hql.Expressions.PipeExpression', preprocess:bool=True) -> tuple[Union[InstructionSet, BranchDescriptor], None]:
        from Hql.Expressions import PipeExpression
        if expr.prepipe:
            acc, rej = self.Tabular(expr.prepipe)
            if rej:
                return self.compile(rej)
            elif not acc:
                prepipe = []
            else:
                prepipe = acc
        else:
            prepipe = []
            
        if not isinstance(prepipe, list):
            prepipe = [prepipe]

        new:list[InstructionSet] = []
        for i in prepipe:
            if isinstance(i, PipeExpression):
                acc, _ = self.PipeExpression(i)
                assert not isinstance(acc, BranchDescriptor)
                new.append(acc)
            else:
                new.append(i)
        prepipe = new
        
        if len(prepipe) == 0:
            logging.warning('Preprocessing with empty prepipe')

        instr = InstructionSet(prepipe, expr.pipes)
        return self.InstructionSet(instr), None

    def InstructionSet(self, instr: InstructionSet, preprocess:bool=True) -> InstructionSet:
        # Preprocess all pipes
        pipes = []
        for i in instr.ops:
            acc, _ = self.compile(i)
            pipes.append(acc)

        # Do basic optimization
        if pipes:
            pipes = self.optimize(pipes)

        # Create groups where data needs to be sync'd
        groups:list[list[BranchDescriptor]] = []
        top = 0
        idx = 0
        for idx, i in enumerate(pipes):
            if i.get_attr('requires_sync'):
                groups.append(pipes[top:idx])
                top = idx
        groups.append(pipes[top:idx+1])

        # Compile first group
        sets = []
        for i in instr.upstream:
            comp = i
            for idx, j in enumerate(groups[0]):
                acc, rej = comp.add_op(j)

                if rej:
                    comp = InstructionSet(comp)
                    comp.add_op(rej)

            if not isinstance(comp, InstructionSet):
                comp = InstructionSet(comp)

            sets.append(comp)

        comp = sets
        for i in groups[1:]:
            comp = InstructionSet(comp)
            for j in i:
                comp.add_op(j.get_op())

        if isinstance(comp, list):
            comp = InstructionSet(comp)

        if len(comp.upstream) == 1 and isinstance(comp.upstream[0], InstructionSet):
            comp.upstream[0].ops += comp.ops
            comp = comp.upstream[0]

        return comp

    def optimize(self, ops: Sequence[Union['Hql.Operators.Operator', BranchDescriptor]]) -> list[BranchDescriptor]:
        from Hql.Operators import Take, Unnest, Operator

        new = []
        for i in ops:
            if isinstance(i, Operator):
                acc, _ = self.compile(i)
                assert isinstance(acc, BranchDescriptor)
                new.append(acc)
            else:
                new.append(i)
        ops = new
        
        logging.debug(f'Optimizing the following operators:')
        for op in ops:
            logging.debug(f'    {op.get_op().id}: {op.get_op().type}')
        
        optimized = [ops[0]]
        for op in ops[1:]:
            i = -1
            while i >= -len(optimized):
                if not (optimized[i].get_attr('row_dependent') or optimized[i].get_attr('row_mutable')) and op.get_attr('row_reducing'):
                    if isinstance(optimized[i].get_op(), Take) or isinstance(op.get_op(), Take):
                        logging.debug("Holding take's location")
                        break

                    if type(optimized[i].get_op()) == type(op.get_op()):
                        break

                    if optimized[i].get_attr('requires_sync') and isinstance(op.get_op(), Take):
                        break

                    if optimized[i].get_attr('type_casting'):
                        break

                    can_map, mapped = self.apply_map(optimized[i], op)
                    if can_map == 1:
                        op = mapped
                        logging.debug(f'{op.get_op().id} is remapped by {optimized[i].get_op().id}')
                        i -= 1
                        continue

                    if can_map == 2:
                        logging.debug(f'{op.get_op().id} references names provided by {optimized[i].get_op().id}')
                        break

                    logging.debug(f'Can optimize {op.get_op().id} passing {optimized[i].get_op().id}')
                    i -= 1
                    continue

                else:
                    logging.debug(f'As high as we can go for {op.get_op().id}')
                    break
            
            if i == -1:
                optimized.append(op)
            else:
                optimized.insert(i+1, op)
        
        logging.debug('Final optimized set:')
        for op in optimized:
            logging.debug(f'    {op.get_op().id}: {op.get_op().type}')

        return optimized

    def apply_map(self, upstream:BranchDescriptor, integrating:BranchDescriptor) -> tuple[int, BranchDescriptor]:
        from Hql.Operators import Project, ProjectRename, Extend
        from copy import deepcopy

        if not upstream.mapping:
            return 0, integrating

        # Should use this to do allow for more more error checking here
        if type(upstream.op) == Project:
            for i in integrating.references:
                if i not in upstream.mapping and i not in upstream.symmetric and i not in self.ctx.symbol_table:
                    return 2, integrating

        elif type(upstream.op) in (Extend, ProjectRename):
            ...
            
        else:
            return 0, integrating
        
        new = deepcopy(self)
        for i in upstream.mapping:
            new.ctx.symbol_table[i] = upstream.mapping[i]

        acc, _ = new.compile(integrating.get_op())
        return 1, acc

    def Where(self, op: 'Hql.Operators.Where', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Where
        desc = BranchDescriptor()
        desc.set_attr('row_reducing')

        acc, _ = self.compile(op.expr)
        op = Where(acc.get_expr(), op.parameters)

        desc.op = op
        desc.merge(acc)
        return desc, None

    def Project(self, op: 'Hql.Operators.Project', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Project
        desc = BranchDescriptor()

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i)
            if isinstance(acc.get_expr(), NamedReference):
                desc.provides.append(acc.get_expr())
                desc.symmetric.append(acc.get_expr())
            desc.merge(acc)
            exprs.append(acc.get_expr())

        op = Project(op.optok, exprs)
        desc.op = op
        return desc, None

    def ProjectAway(self, op: 'Hql.Operators.ProjectAway', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import ProjectAway
        
        acc, _ = self.Project(op)
        new = ProjectAway('project-away', acc.get_op().exprs)
        acc.op = new

        return acc, _

    def ProjectKeep(self, op: 'Hql.Operators.Project', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import ProjectKeep
        
        acc, _ = self.Project(op)
        new = ProjectKeep('project-keep', acc.get_op().exprs)
        acc.op = new

        return acc, _

    def ProjectReorder(self, op: 'Hql.Operators.Project', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import ProjectReorder
        
        acc, _ = self.Project(op)
        new = ProjectReorder('project-reorder', acc.get_op().exprs)
        acc.op = new

        return acc, _

    def ProjectRename(self, op: 'Hql.Operators.ProjectRename', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import ProjectRename
        
        acc, _ = self.Project(op)
        new = ProjectRename('project-rename', acc.get_op().exprs)
        acc.op = new

        return acc, _

    def Take(self, op: 'Hql.Operators.Take', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Take
        desc = BranchDescriptor()
        desc.set_attr('row_dependent') # take a subset of the above rows
        desc.set_attr('row_reducing')

        acc, _ = self.compile(op.expr)
        desc.merge(acc)
        expr = acc.get_expr()

        tables = []
        for i in op.tables:
            acc, _ = self.compile(i)
            desc.merge(acc)
            tables.append(acc.get_expr())

        desc.op = Take(expr, tables)
        return desc, None

    def Count(self, op: 'Hql.Operators.Count', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Count
        desc = BranchDescriptor()
        desc.set_attr('row_dependent')
        desc.set_attr('row_mutable')

        if op.name:
            acc, _ = self.compile(op.name)
            desc.merge(acc)
            expr = acc.get_expr()
        else:
            expr = None

        desc.op = Count(expr)
        return desc, None

    def Extend(self, op: 'Hql.Operators.Extend', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Extend
        desc = BranchDescriptor()

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            exprs.append(acc.get_expr())

        desc.op = Extend(exprs)
        return desc, None

    def Range(self, op: 'Hql.Operators.Range', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Range
        desc = BranchDescriptor()

        acc, _ = self.compile(op.name)
        desc.merge(acc)
        name = acc.get_expr()
        
        acc, _ = self.compile(op.start)
        desc.merge(acc)
        start = acc.get_expr()
        
        acc, _ = self.compile(op.end)
        desc.merge(acc)
        end = acc.get_expr()

        acc, _ = self.compile(op.step)
        desc.merge(acc)
        step = acc.get_expr()
        
        desc.op = Range(name, start, end, step)
        return desc, None

    def Top(self, op: 'Hql.Operators.Top', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Top
        from Hql.Expressions import ByExpression
        desc = BranchDescriptor()

        acc, _ = self.compile(op.expr)
        desc.merge(acc)
        expr = acc.get_expr()

        acc, _ = self.compile(op.by)
        desc.merge(acc)
        by = acc.get_expr()
        assert isinstance(by, ByExpression)

        desc.op = Top(expr, by)
        return desc, None

    def Unnest(self, op: 'Hql.Operators.Unnest', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Unnest
        desc = BranchDescriptor()
        desc.set_attr('row_mutable')

        acc, _ = self.compile(op.field)
        desc.merge(acc)
        field = acc.get_expr()

        tables = []
        for i in op.tables:
            acc, _ = self.compile(i)
            desc.merge(acc)
            tables.append(acc.get_expr())

        desc.op = Unnest(field, tables)
        return desc, None

    def Union(self, op: 'Hql.Operators.Union', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Operators import Union
        desc = BranchDescriptor()
        desc.set_attr('requires_sync')

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            exprs.append(acc.get_expr())

        name = None
        if op.name:
            acc, _ = self.compile(op.name)
            acc.provides = acc.references
            acc.references = []
            desc.merge(acc)
            name = acc.get_expr()
        
        desc.op = Union(exprs, name=name)
        return desc, None

    def Summarize(self, op: 'Hql.Operators.Summarize', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Summarize
        from Hql.Expressions import ByExpression
        desc = BranchDescriptor()
        desc.set_attr('row_dependent')
        desc.set_attr('requires_sync')

        exprs = []
        for i in op.aggregate_exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            exprs.append(acc.get_expr())

        acc, _ = self.ByExpression(op.by_expr)
        desc.merge(acc)
        by_expr = acc.get_expr()

        # Mostly done to shut my linter up
        if not isinstance(by_expr, ByExpression):
            raise hqle.CompilerException(f'ByExpression returned non-ByExpression expr type {type(by_expr)}')

        desc.op = Summarize(exprs, by_expr)
        return desc, None

    def Datatable(self, op: 'Hql.Operators.Datatable', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Datatable
        desc = BranchDescriptor()

        schema = []
        for i in op.schema:
            acc, _ = self.compile(i[0])
            desc.merge(acc)
            name = acc.get_expr()

            acc, _ = self.compile(i[1])
            desc.merge(acc)
            t = acc.get_expr()
            
            schema.append([name, t])

        values = []
        for i in op.values:
            acc, _ = self.compile(i)
            desc.merge(acc)
            values.append(acc.get_expr())

        name = None
        if op.name:
            acc, _ = self.compile(op.name)
            desc.merge(acc)
            name = acc.get_expr()

        desc.op = Datatable(schema, values, name=name)
        return desc, None

    def Join(self, op: 'Hql.Operators.Join', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Join
        from Hql.Expressions import PipeExpression
        desc = BranchDescriptor()

        # The case of recompiling a compiled join
        if isinstance(op.rh, InstructionSet):
            rh = op.rh
            desc.join_attrs = rh.attrs

        elif isinstance(op.rh, PipeExpression):
            acc, _ = self.compile(op.rh)
            desc.join_attrs = acc.attrs
            rh = acc

        else:
            acc, _ = self.Tabular(op.rh)
            assert acc != None
            desc.join_attrs = acc.attrs
            rh = acc
        assert isinstance(rh, InstructionSet)

        params = []
        for i in op.params:
            acc, _ = self.compile(i)
            desc.merge(acc)
            params.append(acc.get_expr())
        
        on = []
        for i in op.on:
            acc, _ = self.compile(i)
            desc.merge(acc)
            on.append(acc.get_expr())

        where = None
        if op.where:
            acc, _ = self.compile(op.where)
            desc.merge(acc)
            where = acc.get_expr()

        desc.op = Join(rh, params=params, on=on, where=where)
        return desc, None

    def MvExpand(self, op: 'Hql.Operators.MvExpand', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import MvExpand
        from Hql.Expressions import Integer
        desc = BranchDescriptor()
        desc.set_attr('row_mutable')

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            exprs.append(acc.get_expr())
        
        limit = None
        if op.limit:
            acc, _ = self.compile(op.limit)
            desc.merge(acc)
            limit = acc.get_expr()
            assert isinstance(limit, Integer)

        desc.op = MvExpand(exprs, limit)
        return desc, None

    def Sort(self, op: 'Hql.Operators.Sort', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Operators import Sort
        desc = BranchDescriptor()
        desc.set_attr('row_dependent')

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            exprs.append(acc.get_expr())

        desc.op = Sort(exprs)
        return desc, None

    def Rename(self, op: 'Hql.Operators.Rename', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Operators import Rename
        desc = BranchDescriptor()
        desc.set_attr('table_mutable')

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            exprs.append(acc.get_expr())

        desc.op = Rename(exprs)
        return desc, None
    
    def OpParameter(self, expr: 'Hql.Expressions.OpParameter', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import OpParameter
        desc = BranchDescriptor()

        acc, _ = self.compile(expr.value)
        desc.merge(acc)

        desc.expr = OpParameter(expr.name, acc.get_expr())
        return desc, None

    def ToClause(self, expr: 'Hql.Expressions.ToClause', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import ToClause
        from Hql.Types.Hql import HqlTypes as hqlt
        desc = BranchDescriptor()

        if isinstance(expr.to, hqlt.HqlType):
            desc.set_attr('type_casting')
            desc.set_attr('types', expr.to)
            to = expr.to
        
        elif expr.to:
            acc, _ = self.compile(expr.to)
            desc.merge(acc)
            to = acc.get_expr()

        else:
            to = None

        acc, _ = self.compile(expr.expr)
        desc.merge(acc)
    
        desc.expr = ToClause(acc.get_expr(), to=to)
        return desc, None

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import OrderedExpression
        desc = BranchDescriptor()
        desc.set_attr('null_ordering')
        desc.set_attr('ordering')

        ordered_expr = None
        if expr.expr:
            acc, _ = self.compile(expr.expr)
            desc.merge(acc)
            ordered_expr = acc.get_expr()

        desc.expr = OrderedExpression(expr=ordered_expr, order=expr.order, nulls=expr.nulls)
        return desc, None

    def ByExpression(self, expr:'Hql.Expressions.ByExpression', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import ByExpression
        desc = BranchDescriptor()
        desc.set_attr('aggregation')

        by_exprs = []
        for i in expr.exprs:
            acc, _ = self.compile(i)
            desc.merge(acc)
            by_exprs.append(acc.get_expr())

        desc.expr = ByExpression(by_exprs)
        return desc, None

    def Function(self, expr: 'Hql.Functions.Function', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import FuncExpr
        return self.compile(FuncExpr(expr.name, expr.args))

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr', preprocess:bool=True, dotcomp:bool=False) -> tuple[object, None]:
        from Hql.Expressions import FuncExpr, NamedReference, Expression
        from Hql.Functions import Function, typecasting
        from Hql.Operators import Operator, Database
        desc = BranchDescriptor()

        acc, _ = self.compile(expr.name)
        desc.merge(acc)
        desc.references = []
        name = acc.get_expr()
        assert isinstance(name, NamedReference)

        args = []
        for i in expr.args:
            acc, _ = self.compile(i)
            desc.merge(acc)
            args.append(acc.get_expr())

        desc.set_attr('functions', name.value)
        desc.expr = FuncExpr(name, args).eval(self.ctx)
        assert isinstance(desc.expr, Function)

        if isinstance(desc.expr, typecasting.Typecast):
            desc.set_attr('type_casting')

        if desc.expr.preprocess and preprocess and not dotcomp:
            res = desc.expr.eval(self.ctx, preprocess=True)
            if isinstance(res, (Expression, Operator)) and not isinstance(res, Database):
                return self.compile(res)
            return res, None

        return desc, None

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import DotCompositeFunction, Expression, FuncExpr
        from Hql.Functions import Function
        from Hql.Operators import Operator, Database
        desc = BranchDescriptor()
        func_preprocess = True

        funcs:list[Function] = []
        for i in expr.funcs:
            if isinstance(i, Function):
                funcs.append(i)
                continue

            assert isinstance(i, FuncExpr)
            acc, _ = self.FuncExpr(i, dotcomp=True)
            assert isinstance(acc, BranchDescriptor)
            desc.merge(acc)
            acc = acc.get_expr()
            assert isinstance(acc, Function)
            funcs.append(acc)

        for i in funcs:
            if not i.preprocess:
                func_preprocess = False

        if func_preprocess:
            res = DotCompositeFunction(funcs).eval(self.ctx, preprocess=True)
            if isinstance(res, (Expression, Operator)) and not isinstance(res, Database):
                return self.compile(res)
            return res, None

        if len(funcs) > 1:
            desc.set_attr('dot_functions')
            desc.expr = DotCompositeFunction(funcs)
        else:
            # Breakdown a dot function to a normal function
            desc.expr = funcs[0]

        return desc, None

    def Equality(self, expr:'Hql.Expressions.Equality', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import Equality
        desc = BranchDescriptor()
        desc.set_attr('case_insensitive_compare', not expr.cs)
        desc.set_attr('case_sensitive_compare', expr.cs)

        acc, _ = self.compile(expr.lh)
        desc.merge(acc)
        lh = acc.get_expr()

        rh = []
        for i in expr.rh:
            acc, _ = self.compile(i)
            desc.merge(acc)
            rh.append(acc.get_expr())

        desc.expr = Equality(lh, expr.op, rh)
        return desc, None

    def Substring(self, expr:'Hql.Expressions.Substring', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import Substring
        desc = BranchDescriptor()
        desc.set_attr('case_insensitive_compare', not expr.cs)
        desc.set_attr('case_sensitive_compare', expr.cs)
        desc.set_attr('term_matching', expr.term)
        desc.set_attr('substring_matching')

        acc, _ = self.compile(expr.lh)
        desc.merge(acc)
        lh = acc.get_expr()

        rh = []
        for i in expr.rh:
            acc, _ = self.compile(i)
            desc.merge(acc)
            rh.append(acc.get_expr())

        desc.expr = Substring(lh, expr.op, rh)
        return desc, None

    def Relational(self, expr:'Hql.Expressions.Relational', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import Relational
        desc = BranchDescriptor()

        acc, _ = self.compile(expr.lh)
        desc.merge(acc)
        lh = acc.get_expr()

        rh = []
        for i in expr.rh:
            acc, _ = self.compile(i)
            desc.merge(acc)
            rh.append(acc.get_expr())

        desc.expr = Relational(lh, expr.op, rh)
        return desc, None

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import BetweenEquality
        desc = BranchDescriptor()
        desc.set_attr('range_compare')

        acc, _ = self.compile(expr.lh)
        desc.merge(acc)
        lh = acc.get_expr()

        acc, _ = self.compile(expr.start)
        desc.merge(acc)
        start = acc.get_expr()
        
        acc, _ = self.compile(expr.end)
        desc.merge(acc)
        end = acc.get_expr()

        desc.expr = BetweenEquality(lh, start, end, expr.op)
        return desc, None

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import BinaryLogic
        desc = BranchDescriptor()

        acc, _ = self.compile(expr.lh)
        desc.merge(acc)
        lh = acc.get_expr()

        rh = []
        for i in expr.rh:
            acc, _ = self.compile(i)
            desc.merge(acc)
            rh.append(acc.get_expr())

        desc.expr = BinaryLogic(lh, rh, expr.bitype)
        return desc, None

    def Not(self, expr: 'Hql.Expressions.Not', preprocess: bool = True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import Not
        desc = BranchDescriptor()

        acc, _ = self.compile(expr.expr)
        desc.merge(acc)
        inner = acc.get_expr()
        
        desc.expr = Not(inner)
        return desc, None

    def BasicRange(self, expr:'Hql.Expressions.BasicRange', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import BasicRange
        desc = BranchDescriptor()
        desc.set_attr('range_compare')

        acc, _ = self.compile(expr.start)
        desc.merge(acc)
        start = acc.get_expr()
        
        acc, _ = self.compile(expr.end)
        desc.merge(acc)
        end = acc.get_expr()

        desc.expr = BasicRange(start, end)
        return desc, None

    def Regex(self, expr:'Hql.Expressions.Regex', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import Regex
        desc = BranchDescriptor()
        desc.set_attr('regex_matching')
        desc.set_attr('regex_insensitive', expr.i)
        desc.set_attr('regex_multiline', expr.m)
        desc.set_attr('regex_dotall', expr.s)
        desc.set_attr('regex_global', expr.g)

        acc, _ = self.compile(expr.lh)
        desc.merge(acc)
        lh = acc.get_expr()
        
        acc, _ = self.compile(expr.rh)
        desc.merge(acc)
        rh = acc.get_expr()

        desc.expr = Regex(lh, rh, expr.i, expr.m, expr.s, expr.g)
        return desc, None
    
    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', expr.eval(self.ctx))
        desc.expr = expr
        
        return desc, None

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Types.Hql import HqlTypes as hqlt

        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.string())
        desc.expr = expr

        return desc, None
    
    def MultiString(self, expr:'Hql.Expressions.MultiString', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import StringLiteral
        desc = BranchDescriptor()

        val = ''
        for i in expr.strlits:
            val += i.quote('')

        desc.set_attr('types', hqlt.string())
        desc.expr = StringLiteral(val)
        return desc, None

    def Integer(self, expr:'Hql.Expressions.Integer', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.int())
        desc.expr = expr

        return desc, None

    def IP4(self, expr:'Hql.Expressions.IP4', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.ip4())
        desc.expr = expr

        return desc, None

    def Float(self, expr:'Hql.Expressions.Float', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.float())
        desc.expr = expr

        return desc, None

    def Bool(self, expr:'Hql.Expressions.Bool', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.bool())
        desc.expr = expr

        return desc, None

    def Datetime(self, expr: 'Hql.Expressions.Datetime', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Types.Hql import HqlTypes as hqlt

        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.datetime())
        desc.expr = expr

        return desc, None
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import PipeExpression
        from Hql.Operators.Database import Database

        desc = BranchDescriptor()

        if expr in self.ctx.symbol_table and expr != self.ctx.symbol_table[expr]:
            res = self.ctx.symbol_table[expr]

            if not isinstance(res, (PipeExpression, Database, InstructionSet)):
                acc, _ = self.compile(res)
                desc.expr = acc.get_expr()
                desc.merge(desc)
                return desc, None

        desc.expr = expr
        desc.references = [expr]
        return desc, None

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        acc, _ = self.NamedReference(expr)
        acc.set_attr('complex_names')
        return acc, None

    def Keyword(self, expr:'Hql.Expressions.Keyword', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        return self.NamedReference(expr)

    def Identifier(self, expr:'Hql.Expressions.Identifier', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        return self.NamedReference(expr)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        acc, _ = self.NamedReference(expr)
        acc.set_attr('wildcards')
        return acc, None

    def Path(self, expr:'Hql.Expressions.Path', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import Path, EscapedNamedReference, Wildcard
        from Hql.Expressions import PipeExpression
        from Hql.Operators.Database import Database
        
        desc = BranchDescriptor()
        desc.set_attr('nested_objects')

        if expr in self.ctx.symbol_table:
            res = self.ctx.symbol_table[expr]
            if not isinstance(res, (PipeExpression, Database, InstructionSet)):
                acc, _ = self.compile(res)
                desc.expr = acc.get_expr()
                desc.merge(desc)
                return desc, None
        
        path = []
        for i in expr.path:
            if isinstance(i, EscapedNamedReference):
                desc.set_attr('complex_names')
            
            if isinstance(i, Wildcard):
                desc.set_attr('wildcards')

            path.append(i)

        desc.expr = Path(path)
        desc.references = [desc.expr]
        return desc, None

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression', preprocess:bool=True) -> tuple[BranchDescriptor, None]:
        from Hql.Expressions import NamedExpression, NamedReference, Path
        desc = BranchDescriptor()
        desc.set_attr('assignment')

        acc, _ = self.compile(expr.value)
        desc.merge(acc)
        value = acc.get_expr()

        paths = []
        assignments = []
        for i in expr.paths:
            acc, _ = self.compile(i)
            desc.merge(acc)
            dest = acc.get_expr()

            if isinstance(value, (NamedReference, Path)):
                assert isinstance(dest, (NamedReference, Path))
                desc.add_mapping(dest, value)
                desc.references.append(value)

            desc.provides.append(dest)
            paths.append(dest)

        desc.expr = NamedExpression(paths, value)
        return desc, None
