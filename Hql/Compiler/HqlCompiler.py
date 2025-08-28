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
        
    def run(self, ctx: Union[Context, None] = None) -> Context:
        ctx = ctx if ctx else self.ctx

        if not self.ops:
            raise hqle.QueryException('Running an empty compiler has no effect!')

        for i in self.ops:
            start = time.perf_counter()
            logging.debug(f'Executing {i.type}: {i.id}')
            
            ctx.data = i.eval(ctx)
            
            end = time.perf_counter()
            logging.debug(f"{i.id} - {end - start}")

        return ctx

    def compile(self, src:Union['Operator', 'Expression']) -> BranchDescriptor:
        return self.from_name(src.type)(src)

    def is_breaking(self, op:'Operator') -> bool:
        breaking = self.from_name(op.type)(op).attrs.get('aggregate', False)
        return breaking

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

        idx = 0
        for idx, i in enumerate(pipes):
            if self.is_breaking(i):
                break

        viable = pipes[:idx]
        breaking = pipes[idx:]

        # Compile operators into DBs
        sets = []
        for i in prepipe:
            comp = i
            for idx, j in enumerate(viable):
                rej = comp.add_op(j)

                if rej:
                    comp = InstructionSet(comp)
                    comp.add_op(rej)

            if not isinstance(comp, InstructionSet):
                comp = InstructionSet(comp)

            sets.append(comp)

        comp = InstructionSet()

        comp = HqlCompiler(self.config)
        comp.parents = parents

        return comp

    def Where(self, op: 'Hql.Operators.Where') -> BranchDescriptor:
        from Hql.Operators import Where
        desc = BranchDescriptor()

        res = self.compile(op.expr)

        op = Where(res.get_expr(), op.parameters)

        res.op = op
        res.expr = None

        return res

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

        handler = self.from_name(op.expr.type)
        expr = handler(op.expr)

        parts = []
        for i in op.tables:
            handler = self.from_name(i.type)
            parts.append(handler(i))

        res = BranchDescriptor()
        res.merge_attrs(expr.attrs)
        for i in parts:
            res.merge_attrs(i.attrs)

        op = Take(expr.get_expr(), [x.get_expr() for x in parts])
        res.op = op

        return res

    def Count(self, op: 'Hql.Operators.Count') -> BranchDescriptor:
        from Hql.Operators import Count
        desc = BranchDescriptor()

        if op.name:
            expr = self.from_name(op.name.type)(op.name)
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

        res = self.from_name(op.name.type)(op.name)
        desc.merge_attrs(res.attrs)
        name = res.get_expr()
        
        res = self.from_name(op.start.type)(op.start)
        desc.merge_attrs(res.attrs)
        start = res.get_expr()
        
        res = self.from_name(op.end.type)(op.end)
        desc.merge_attrs(res.attrs)
        end = res.get_expr()

        res = self.from_name(op.step.type)(op.step)
        desc.merge_attrs(res.attrs)
        step = res.get_expr()
        
        desc.op = Range(name, start, end, step)
        return desc

    def Top(self, op: 'Hql.Operators.Top') -> BranchDescriptor:
        from Hql.Operators import Top
        desc = BranchDescriptor()

        res = self.from_name(op.expr.type)(op.expr)
        desc.merge_attrs(res.attrs)
        expr = res.get_expr()

        res = self.from_name(op.by.type)(op.by)
        desc.merge_attrs(res.attrs)
        by = res.get_expr()

        desc.op = Top(expr, by)
        return desc

    def Unnest(self, op: 'Hql.Operators.Unnest') -> BranchDescriptor:
        from Hql.Operators import Unnest
        desc = BranchDescriptor()

        res = self.from_name(op.field.type)(op.field)
        desc.merge_attrs(res.attrs)
        field = res.get_expr()

        tables = []
        for i in op.tables:
            res = self.from_name(i.type)(i)
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
            res = self.from_name(i.type)(i)
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
        rh = res.expr

        res = self.compile()

        return desc

    def ByExpression(self, expr: 'Hql.Expressions.ByExpression') -> BranchDescriptor:
        return BranchDescriptor(expr=expr)

    def DotCompositeFunction(self, expr: 'Hql.Expressions.DotCompositeFunction') -> BranchDescriptor:
        return BranchDescriptor(expr=expr)
