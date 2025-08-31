from os import stat
from typing import Union, TYPE_CHECKING
import logging
import time
import json

from Hql.Compiler import Compiler, BranchDescriptor, InstructionSet
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
from Hql.Query import LetStatement, QueryStatement

if TYPE_CHECKING:
    from Hql.Query import Query
    from Hql.Config import Config
    from Hql.Operators import Database, Operator
    from Hql.Expressions import Expression
    import Hql

'''
Hql preprocessor
'compiles' out a set of pure-Hql expressions and operators
Works out preprocessor functions
'''
class HqlCompiler(Compiler):
    def __init__(self, config:'Config', query:Union[None, 'Query']=None):
        Compiler.__init__(self)
        self.config = config
        self.root = None

        if query:
            self.Query(query)

    def compile(self, src:Union['Operator', 'Expression']) -> BranchDescriptor:
        return self.from_name(src.type)(src)

    # def is_breaking(self, op:'Operator') -> bool:
    #     breaking = self.compile(op).attrs.get('aggregate', False)
    #     return breaking

    def Query(self, query: 'Hql.Query.Query'):
        for i in query.statements:
            self.root = self.Statement(i)

    def Statement(self, statement: 'Hql.Query.Statement'):
        if isinstance(statement, QueryStatement):
            self.QueryStatement(statement)

        elif isinstance(statement, LetStatement):
            self.LetStatement(statement)

        else:
            raise hqle.CompilerException('')

    def QueryStatement(self, statement: 'Hql.Query.QueryStatement'):
        handler = self.from_name(statement.root.type)
        self.root = handler(statement.root)

    def LetStatement(self, statement: 'Hql.Query.LetStatement'):
        name = statement.name.eval(self.ctx, as_str=True)
        res = self.compile(statement.root)
        handler = self.from_name(statement.root.type)
        expr = handler(statement.root)

        self.ctx.symbol_table[name] = expr

    def Tabular(self, expr:Union['Hql.Operators.Range', 'Hql.Expressions.Expression']) -> 'Database':
        from Hql.Operators.Database import Database, Static
        from Hql.Expressions import DotCompositeFunction, NamedReference
        from Hql.Operators import Range

        db = None

        if isinstance(expr, DotCompositeFunction):
            res = self.DotCompositeFunction(expr)
            db = res.db

        elif isinstance(expr, NamedReference):
            db = self.ctx.symbol_table[expr.name]

            if not isinstance(db, Database):
                db = self.config.get_default_db()
                db = db.get_variable(expr.name)

        elif isinstance(expr, Range):
            op = self.Range(expr).op
            if not op:
                raise hqle.CompilerException('Range precompile did not set op')
            db = Static(op.eval(self.ctx))

        if not isinstance(db, Database):
            logging.critical(json.dumps(expr.to_dict(), indent=2))
            raise hqle.CompilerException(f'Tabular reference returns non-tabular expression {type(db)}')

        return db

    def PrePipe(self, op: 'Hql.Operators.PrePipe'):
        return self.Tabular(op.expr)

    def PipeExpression(self, expr: 'Hql.Expressions.PipeExpression'):
        from Hql.Operators import PrePipe
        from Hql.Expressions import Expression

        if expr.prepipe:
            if isinstance(expr.prepipe, PrePipe):
                prepipe = self.PrePipe(expr.prepipe)

            elif isinstance(expr.prepipe, Expression):
                prepipe = self.Tabular(expr.prepipe)

            else:
                logging.critical(json.dumps(expr.prepipe.to_dict(), indent=2))
                raise hqle.CompilerException(f'Invalid prepipe expression type {type(expr.prepipe)}')

        else:
            logging.warning('Preprocessing PipeExpression had None prepipe')
            prepipe = []

        if not isinstance(prepipe, list):
            prepipe = [prepipe]

        # Preprocess all pipes
        pipes = []
        for i in expr.pipes:
            method = self.from_name(i.type)
            p = method(i)
            pipes.append(p)

        # Do basic optimization
        pipes = self.optimize(pipes)

        # Create groups where data needs to be sync'd
        groups:list[list[BranchDescriptor]] = []
        top = 0
        idx = 0
        for idx, i in enumerate(pipes):
            if i.get_attr('requires_sync'):
                groups.append(pipes[top:idx])
                top = idx
        groups.append(pipes[top:idx])

        # Compile first group
        sets = []
        for i in prepipe:
            comp = i
            for idx, j in enumerate(groups[0]):
                rej = comp.add_op(j)

                if rej:
                    comp = InstructionSet(comp)
                    comp.add_op(rej)

            if not isinstance(comp, InstructionSet):
                comp = InstructionSet(comp)

            sets.append(comp)

        comp = InstructionSet(sets)
        # If needed I can compile the other groups separate in the future
        for i in groups[1:]:
            comp.ops += [x.get_op() for x in i]

        return comp

    def optimize(self, ops: list[BranchDescriptor]):
        from Hql.Operators import Take

        optimized = [ops[0]]
        
        logging.debug(f'Optimizing the following operators:')
        for op in ops:
            assert op.op
            logging.debug(f'    {op.op.id}: {op.op.type}')

        for op in ops[1:]:
            assert op.op
            i = -1
            while i >= -len(optimized):
                if not (optimized[i].get_attr('row_dependent') or optimized[i].get_attr('row_mutable')) and op.get_attr('row_reducing'):
                    if isinstance(optimized[i].op, Take):
                        logging.debug(f'Maintaining Take as a priority operator')
                        continue

                    logging.debug(f'Can optimize {op.op.id} passing {optimized[i].op.id}')
                    i -= 1
                    continue

                else:
                    break
                
            optimized.insert(i, op)
        
        logging.debug('Final optimized set:')
        for op in optimized:
            assert op.op
            logging.debug(f'    {op.op.id}: {op.op.type}')

        return optimized


    def Where(self, op: 'Hql.Operators.Where') -> BranchDescriptor:
        from Hql.Operators import Where

        res = self.compile(op.expr)
        op = Where(res.get_expr(), op.parameters)

        desc = BranchDescriptor()
        desc.op = op
        desc.merge_attrs(res.attrs)

        return desc

    def Project(self, op: 'Hql.Operators.Project') -> BranchDescriptor:
        from Hql.Operators import Project

        parts:list[BranchDescriptor] = []
        for i in op.exprs:
            method = self.from_name(i.type)
            parts.append(method(i))

        res = BranchDescriptor()
        exprs = []
        for i in parts:
            exprs.append(i.get_expr())
            res.merge_attrs(i.attrs)

        op = Project(op.optok, exprs)
        res.op = op

        return res

    def ProjectAway(self, op: 'Hql.Operators.Project') -> BranchDescriptor:
        return self.Project(op)

    def ProjectKeep(self, op: 'Hql.Operators.Project') -> BranchDescriptor:
        return self.Project(op)

    def ProjectReorder(self, op: 'Hql.Operators.Project') -> BranchDescriptor:
        return self.Project(op)

    def ProjectRename(self, op: 'Hql.Operators.ProjectRename') -> BranchDescriptor:
        return self.Project(op)

    def Take(self, op: 'Hql.Operators.Take') -> BranchDescriptor:
        from Hql.Operators import Take
        desc = BranchDescriptor()
        desc.set_attr('row_mutable', True)

        res = self.compile(op.expr)
        desc.merge_attrs(res.attrs)
        expr = res.get_expr()

        tables = []
        for i in op.tables:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            tables.append(res.get_expr())

        desc.op = Take(expr, tables)
        return desc

    def Count(self, op: 'Hql.Operators.Count') -> BranchDescriptor:
        from Hql.Operators import Count
        desc = BranchDescriptor()
        desc.set_attr('row_dependent', True)
        desc.set_attr('row_mutable', True)

        if op.name:
            expr = self.compile(op.name)
            desc.merge_attrs(expr.attrs)
            expr = expr.get_expr()
        else:
            expr = None

        desc.op = Count(expr)
        return desc

    def Extend(self, op: 'Hql.Operators.Extend') -> BranchDescriptor:
        from Hql.Operators import Extend

        parts = []
        for i in op.exprs:
            handler = self.from_name(i.type)
            parts.append(handler(i))

        desc = BranchDescriptor()
        exprs = []
        for i in parts:
            desc.merge_attrs(i.attrs)
            exprs.append(i.get_expr())

        desc.op = Extend(exprs)
        return desc

    def Range(self, op: 'Hql.Operators.Range') -> BranchDescriptor:
        from Hql.Operators import Range
        desc = BranchDescriptor()

        res = self.compile(op.name)
        desc.merge_attrs(res.attrs)
        name = res.get_expr()
        
        res = self.compile(op.start)
        desc.merge_attrs(res.attrs)
        start = res.get_expr()
        
        res = self.compile(op.end)
        desc.merge_attrs(res.attrs)
        end = res.get_expr()

        res = self.compile(op.step)
        desc.merge_attrs(res.attrs)
        step = res.get_expr()
        
        desc.op = Range(name, start, end, step)
        return desc

    def Top(self, op: 'Hql.Operators.Top') -> BranchDescriptor:
        from Hql.Operators import Top
        from Hql.Expressions import ByExpression
        desc = BranchDescriptor()

        res = self.compile(op.expr)
        desc.merge_attrs(res.attrs)
        expr = res.get_expr()

        res = self.compile(op.by)
        desc.merge_attrs(res.attrs)
        by = res.get_expr()
        assert isinstance(by, ByExpression)

        desc.op = Top(expr, by)
        return desc

    def Unnest(self, op: 'Hql.Operators.Unnest') -> BranchDescriptor:
        from Hql.Operators import Unnest
        desc = BranchDescriptor()

        res = self.compile(op.field)
        desc.merge_attrs(res.attrs)
        field = res.get_expr()

        tables = []
        for i in op.tables:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            tables.append(res.get_expr())

        desc.op = Unnest(field, tables)
        return desc

    def Summarize(self, op: 'Hql.Operators.Summarize') -> BranchDescriptor:
        from Hql.Operators import Summarize
        from Hql.Expressions import ByExpression
        desc = BranchDescriptor()

        exprs = []
        for i in op.aggregate_exprs:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            exprs.append(res.get_expr())

        res = self.ByExpression(op.by_expr)
        desc.merge_attrs(res.attrs)
        by_expr = res.get_expr()

        # Mostly done to shut my linter up
        if not isinstance(by_expr, ByExpression):
            raise hqle.CompilerException(f'ByExpression returned non-ByExpression expr type {type(by_expr)}')

        desc.op = Summarize(exprs, by_expr)
        return desc

    def Datatable(self, op: 'Hql.Operators.Datatable') -> BranchDescriptor:
        from Hql.Operators import Datatable
        desc = BranchDescriptor()

        schema = []
        for i in op.schema:
            res = self.compile(i[0])
            desc.merge_attrs(res.attrs)
            name = res.get_expr()

            res = self.compile(i[1])
            desc.merge_attrs(res.attrs)
            t = res.get_expr()
            
            schema.append([name, t])

        values = []
        for i in op.values:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            values.append(res.get_expr())

        desc.op = Datatable(schema, values)
        return desc

    def Join(self, op: 'Hql.Operators.Join') -> BranchDescriptor:
        from Hql.Operators import Join
        desc = BranchDescriptor()

        res = self.compile(op.rh)
        desc.join_attrs = res.attrs
        rh = res.get_expr()
        assert isinstance(rh, InstructionSet)

        params = []
        for i in op.params:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            params.append(res.get_expr())
        
        on = []
        for i in op.on:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            on.append(res.get_expr())

        where = None
        if op.where:
            res = self.compile(op.where)
            desc.merge_attrs(res.attrs)
            where = res.get_expr()

        desc.op = Join(rh, params=params, on=on, where=where)
        return desc

    def MvExpand(self, op: 'Hql.Operators.MvExpand') -> BranchDescriptor:
        from Hql.Operators import MvExpand
        from Hql.Expressions import Integer
        desc = BranchDescriptor()
        desc.set_attr('row_mutable', True)

        exprs = []
        for i in op.exprs:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            exprs.append(res.get_expr())
        
        limit = None
        if op.limit:
            res = self.compile(op.limit)
            desc.merge_attrs(res.attrs)
            limit = res.get_expr()
            assert isinstance(limit, Integer)

        desc.op = MvExpand(exprs, limit)

    def Sort(self, op: 'Hql.Operators.Sort') -> BranchDescriptor:
        from Hql.Operators import Sort
        desc = BranchDescriptor()
        desc.set_attr('row_dependent', True)

        exprs = []
        for i in op.exprs:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            exprs.append(res.get_expr())

        desc.op = Sort(exprs)
        return desc
    
    def OpParameter(self, expr: 'Hql.Expressions.OpParameter') -> BranchDescriptor:
        from Hql.Expressions import OpParameter
        desc = BranchDescriptor()

        res = self.compile(expr.value)
        desc.merge_attrs(res.attrs)

        desc.expr = OpParameter(expr.name, res.get_expr())
        return desc

    def ToClause(self, expr: 'Hql.Expressions.ToClause') -> BranchDescriptor:
        from Hql.Expressions import ToClause
        desc = BranchDescriptor()

        if expr.to:
            desc.set_attr('type_casting', True)
            desc.set_attr('types', expr.to)

        res = self.compile(expr.expr)
        desc.merge_attrs(res.attrs)
    
        desc.expr = ToClause(res.get_expr(), to=expr.to)
        return desc

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression') -> BranchDescriptor:
        from Hql.Expressions import OrderedExpression
        desc = BranchDescriptor()
        desc.set_attr('null_ordering', True)
        desc.set_attr('ordering', True)

        ordered_expr = None
        if expr.expr:
            res = self.compile(expr.expr)
            desc.merge_attrs(res.attrs)

        desc.expr = OrderedExpression(expr=ordered_expr, order=expr.order, nulls=expr.nulls)
        return desc

    def ByExpression(self, expr:'Hql.Expressions.ByExpression') -> BranchDescriptor:
        from Hql.Expressions import ByExpression
        desc = BranchDescriptor()
        desc.set_attr('aggregation', True)

        by_exprs = []
        for i in expr.exprs:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            by_exprs.append(res.get_expr())

        desc.expr = ByExpression(by_exprs)
        return desc

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr') -> BranchDescriptor:
        from Hql.Expressions import FuncExpr, NamedReference
        desc = BranchDescriptor()

        res = self.compile(expr.name)
        desc.merge_attrs(res.attrs)
        name = res.get_expr()
        assert isinstance(name, NamedReference)

        args = []
        for i in expr.args:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            args.append(res.get_expr())

        desc.set_attr('functions', name.value)
        desc.expr = FuncExpr(name, args)
        return desc

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction') -> BranchDescriptor:
        from Hql.Expressions import DotCompositeFunction
        desc = BranchDescriptor()

        funcs = []
        for i in expr.funcs:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            funcs.append(res.get_expr())

        if len(funcs) > 1:
            desc.set_attr('dot_functions', True)
            desc.expr = DotCompositeFunction(funcs)
        else:
            # Breakdown a dot function to a normal function
            desc.expr = funcs[0]

        return desc

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression') -> BranchDescriptor:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.from_name(expr.type))
        desc.expr = expr
        
        return desc

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral') -> BranchDescriptor:
        from Hql.Types.Hql import HqlTypes as hqlt

        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.string())
        desc.expr = expr

        return desc

    def Integer(self, expr:'Hql.Expressions.Integer') -> BranchDescriptor:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.int())
        desc.expr = expr

        return desc

    def IP4(self, expr:'Hql.Expressions.IP4') -> BranchDescriptor:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.ip4())
        desc.expr = expr

        return desc

    def Float(self, expr:'Hql.Expressions.Float') -> BranchDescriptor:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.float())
        desc.expr = expr

        return desc

    def Bool(self, expr:'Hql.Expressions.Bool') -> BranchDescriptor:
        from Hql.Types.Hql import HqlTypes as hqlt
        
        desc = BranchDescriptor()
        desc.set_attr('types', hqlt.bool())
        desc.expr = expr

        return desc
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference') -> BranchDescriptor:
        desc = BranchDescriptor()
        desc.expr = expr
        return desc

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference') -> BranchDescriptor:
        desc = BranchDescriptor()
        desc.set_attr('complex_names', True)
        desc.expr = expr
        return desc

    def Keyword(self, expr:'Hql.Expressions.Keyword') -> BranchDescriptor:
        return self.NamedReference(expr)

    def Identifier(self, expr:'Hql.Expressions.Identifier') -> BranchDescriptor:
        return self.NamedReference(expr)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard') -> BranchDescriptor:
        desc = self.NamedReference(expr)
        desc.set_attr('wildcards', True)
        return desc

    def Path(self, expr:'Hql.Expressions.Path') -> BranchDescriptor:
        from Hql.Expressions import Path
        desc = BranchDescriptor()
        desc.set_attr('nested_objects', True)
        
        path = []
        for i in expr.path:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            path.append(res.get_expr())

        desc.expr = Path(path)
        return desc

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression') -> BranchDescriptor:
        from Hql.Expressions import NamedExpression
        desc = BranchDescriptor()
        desc.set_attr('assignment', True)

        paths = []
        for i in expr.paths:
            res = self.compile(i)
            desc.merge_attrs(res.attrs)
            paths.append(res.get_expr())

        res = self.compile(expr.value)
        desc.merge_attrs(res.attrs)
        value = res.get_expr()

        desc.expr = NamedExpression(paths, value)
        return desc
