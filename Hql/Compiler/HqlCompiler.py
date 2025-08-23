from typing import Union, TYPE_CHECKING
import logging
import time
import json

from Hql.Compiler import Compiler, BranchDescriptor
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
from Hql.Query import LetStatement, QueryStatement

if TYPE_CHECKING:
    from Hql.Query import Query
    from Hql.Config import Config
    from Hql.Operators import Database
    import Hql

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

    def Query(self, query: 'Hql.Query.Query'):
        for i in query.statements:
            self.Statement(i)

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
        handler = self.from_name(statement.root.type)
        expr = handler(statement.root)

        self.ctx.symbol_table[name] = expr

    def Tabular(self, expr: 'Hql.Expressions.Expression') -> 'Database':
        from Hql.Operators.Database import Database

        db = None

        if isinstance(expr, 'Hql.Expressions.DotCompositeFunction'):
            db = self.DotCompositeFunction(expr)

        elif isinstance(expr, 'Hql.Expressions.NamedReference'):
            db = self.ctx.symbol_table[expr.name]

            if not isinstance(db, Database):
                db = self.config.get_default_db()
                db = db.get_variable(expr.name)

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

        # Compile operators into DBs
        parents = []
        for i in prepipe:
            comp = i
            for idx, j in enumerate(pipes):
                rej = comp.add_op(j)

                if rej:
                    new = HqlCompiler(self.config)
                    new.add_parent(comp)
                    new.add_op(rej)
                    comp = new

            parents.append(comp)

        comp = HqlCompiler(self.config)
        comp.parents = parents

        return comp

    def Where(self, op: 'Hql.Operators.Where') -> BranchDescriptor:
        from Hql.Operators import Where

        method = self.from_name(op.expr.type)
        res:BranchDescriptor = method(op.expr)
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

        res = BranchDescriptor()

        if op.name:
            handler = self.from_name(op.name.type)
            expr = handler(op.name)
            res.merge_attrs(expr.attrs)
            expr = expr.get_expr()
        else:
            expr = None

        op = Count(expr)
        res.op = op

        return res

    def Extend(self, op: 'Hql.Operators.Extend') -> object:
        from Hql.Operators import Extend

        parts = []
        for i in op.exprs:
            handler = self.from_name(i.type)
            parts.append(handler(i))

        res = BranchDescriptor()
        exprs = []
        for i in parts:
            res.merge_attrs(i.attrs)
            exprs.append(i.get_expr())

        op = Extend(exprs)
        res.op = op

        return res
