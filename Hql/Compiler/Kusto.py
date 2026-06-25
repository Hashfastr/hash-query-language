from typing import Optional, Union, TYPE_CHECKING

from Hql.Exceptions import HqlExceptions as hqle
import logging

from . import Compiler

if TYPE_CHECKING:
    from Hql.Compiler import BranchDescriptor, InstructionSet
    from Hql.Expressions import Expression
    from Hql.Expressions.Logic import Logic
    from Hql.Query import Statement
    import Hql.Operators as Ops

class KustoCompiler(Compiler):
    def __init__(self):
        from Hql.Context import Context
        from Hql.Data import Data
        self.type = self.__class__.__name__
        self.ctx = Context(Data())

        self.stmts:list['Statement'] = []

    def optimize(self, ops: list['BranchDescriptor']) -> list['BranchDescriptor']:
        return ops

    def compile(self, prep:bool=True) -> tuple[Union[str, list['Statement']], None]:
        stmts = []
        for i in self.stmts:
            acc, _ = self.compile_stmt(i, prep=prep)
            stmts.append(acc)

        if prep:
            return stmts, None
        return '\n;\n'.join(stmts), None

    def compile_op(self, src:'Ops.Operator', prep:bool=True) -> tuple[Union['Ops.Operator', str, None], Optional['Ops.Operator']]:
        return self.from_name(src.type)(src, prep=prep)

    def compile_expr(self, src:'Expression', prep:bool=True) -> tuple[Union['Expression', str, None], Optional['Expression']]:
        return self.from_name(src.type)(src, prep=prep)

    def compile_logic(self, src:'Logic', prep:bool=True) -> tuple[Union['Logic', str, None], Optional['Logic']]:
        return self.from_name(src.type)(src, prep=prep)

    def compile_stmt(self, src:'Statement', prep:bool=True) -> tuple[Union['Statement', str, None], Optional['Statement']]:
        from Hql.Query import QueryStatement
        from Hql.Expressions import Expression, PipeExpression

        if isinstance(src, QueryStatement):
            acc, rej = self.compile_expr(src.root, prep=prep)
        else:
            return None, src

        if rej:
            return None, src

        if isinstance(acc, Expression):
            assert isinstance(acc, PipeExpression)
            return QueryStatement(acc), None
        
        return acc, None

    '''
    By default, all of these return themselves as they are being
    'rejected' back to the compiler
    '''

    def Tabular(self, expr:'Hql.Expressions.Expression') -> tuple[Optional['InstructionSet'], Optional['Hql.Expressions.Expression']]:
        return None, expr

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression', prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Expression, PipeExpression

        def preprocess(prepipe:Optional[Expression], pipes:list[Ops.Operator]) -> tuple[object, object]:
            processed = []
            for j, i in enumerate(pipes):
                acc, rej = self.compile_op(i)

                if acc:
                    assert not isinstance(acc, str)
                    pipes.append(acc)

                if rej:
                    return PipeExpression(processed, prepipe=prepipe), PipeExpression([rej] + expr.pipes[j+1:])

            return PipeExpression(processed, prepipe=prepipe), None

        def compile(prepipe:Optional[str], pipes:list[Ops.Operator]) -> tuple[object, object]:
            cpipes:list[str] = []
            for i in pipes:
                acc, rej = self.compile_op(i, prep=False)
                if rej or not isinstance(acc, str):
                    logging.error(acc)
                    logging.error(rej)
                    raise hqle.CompilerException('Attempt to compile without proper preprocess!')
                cpipes.append(acc)

            out = prepipe if prepipe else ''
            out += '\n' + '\n| '.join(cpipes)

            return out, None

        if isinstance(expr.prepipe, Expression):
            acc, rej = self.compile_expr(expr.prepipe, prep=prep)
            if rej:
                return None, expr
            prepipe = acc
        else:
            prepipe = None

        if prep:
            assert not isinstance(prepipe, str)
            return preprocess(prepipe, expr.pipes)
        else:
            assert not isinstance(prepipe, Expression)
            return compile(prepipe, expr.pipes)

    '''
    Operators
    '''

    def Where(self, op:'Ops.Where', prep:bool=True) -> tuple[object, object]:
        from Hql.Operators import Where
        from Hql.Expressions.Logic import Logic

        if prep:
            acc, rej = self.compile_logic(op.expr)
            
            if rej:
                rej = Where(rej)

            assert isinstance(acc, Logic)
            return Where(acc), rej

        out = 'where '
        expr, _ = self.compile_logic(op.expr, prep=False)
        assert isinstance(expr, str)
        return out + expr, None

    def Project(self, op:'Ops.Project', prep:bool=True) -> tuple[object, object]:
        if prep:
            exprs = []
            for i in op.exprs:
                expr, rej = self.compile_expr(i)
                if rej:
                    return None, op
                assert isinstance(expr, 'Expression')
                exprs.append(expr)
            op.exprs = exprs
            return op, None

        out = f'{op.optok} '
        exprs = []
        for i in op.exprs:
            expr, _ = self.compile_expr(i, prep=False)
            exprs.append(expr)
        out += ', '.join(exprs)
        return out, None

    def ProjectAway(self, op:'Ops.ProjectAway', prep:bool=True) -> tuple[object, object]:
        return self.Project(op, prep=prep)

    def ProjectKeep(self, op:'Ops.ProjectKeep', prep:bool=True) -> tuple[object, object]:
        return self.Project(op, prep=prep)

    def ProjectReorder(self, op:'Ops.ProjectReorder', prep:bool=True) -> tuple[object, object]:
        return self.Project(op, prep=prep)

    def ProjectRename(self, op:'Ops.ProjectRename', prep:bool=True) -> tuple[object, object]:
        return self.Project(op, prep=prep)

    def Take(self, op:'Ops.Take', prep:bool=True) -> tuple[object, object]:
        if prep:
            if op.tables:
                return None, op
            return op, None

        out = 'take '
        val, _ = self.compile_expr(op.expr, prep=False)
        assert isinstance(val, str)
        return out + val, None

    def Count(self, op:'Ops.Count', prep:bool=True) -> tuple[object, object]:
        if prep:
            if op.name:
                return None, op
            return op, None
        out = 'count'
        return out, None

    def Extend(self, op:'Ops.Extend', prep:bool=True) -> tuple[object, object]:
        if prep:
            exprs = []
            for i in op.exprs:
                expr, rej = self.compile_expr(i)
                if rej:
                    return None, op
                exprs.append(expr)
            op.exprs = exprs
            return op, None

        out = f'extend '
        exprs = []
        for i in op.exprs:
            expr, _ = self.compile_expr(i, prep=False)
            exprs.append(expr)
        out += ', '.join(exprs)
        return out, None

    def Range(self, op:'Ops.Range', prep:bool=True) -> tuple[object, object]:
        return None, op
        
        if prep:
            return op, None
        out = op.decompile(Context(Data(None)))
        return out, None

    def Top(self, op:'Ops.Top', prep:bool=True) -> tuple[object, object]:
        if prep:
            return op, None

        out = 'top ' + 
        return out, None

    def Unnest(self, op:'Ops.Unnest', prep:bool=True) -> tuple[object, object]:
        return None, op

    def Union(self, op:'Ops.Union', prep:bool=True) -> tuple[object, object]:
        return None, op

        from Hql.Context import Context
        from Hql.Data import Data
        
        if prep:
            return op, None
        out = op.decompile(Context(Data(None)))
        return out, None

    def Summarize(self, op:'Ops.Summarize', prep:bool=True) -> tuple[object, object]:

        return None, op

    def Datatable(self, op:'Ops.Datatable', prep:bool=True) -> tuple[object, object]:
        return None, op

    def Join(self, op:'Ops.Join', prep:bool=True) -> tuple[object, object]:
        return None, op

    def MvExpand(self, op:'Ops.MvExpand', prep:bool=True) -> tuple[object, object]:
        return None, op

    def Sort(self, op:'Ops.Sort', prep:bool=True) -> tuple[object, object]:
        return None, op

    def Rename(self, op:'Ops.Rename', prep:bool=True) -> tuple[object, object]:
        return None, op

    '''
    Expressions
    '''

    def OpParameter(self, expr:'Hql.Expressions.OpParameter', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def ToClause(self, expr:'Hql.Expressions.ToClause', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Function(self, expr:'Hql.Functions.Function', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Equality(self, expr:'Hql.Expressions.Equality', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Substring(self, expr:'Hql.Expressions.Substring', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Relational(self, expr:'Hql.Expressions.Relational', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Not(self, expr:'Hql.Expressions.Not', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def BasicRange(self, expr:'Hql.Expressions.BasicRange', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Regex(self, expr:'Hql.Expressions.Regex', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral', prep:bool=True) -> tuple[object, object]:
        return None, expr
    
    def MultiString(self, expr:'Hql.Expressions.MultiString', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Integer(self, expr:'Hql.Expressions.Integer', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def IP4(self, expr:'Hql.Expressions.IP4', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Float(self, expr:'Hql.Expressions.Float', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Bool(self, expr:'Hql.Expressions.Bool', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Multivalue(self, expr:'Hql.Expressions.Multivalue', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def Datetime(self, expr:'Hql.Expressions.Datetime', prep:bool=True) -> tuple[object, object]:
        return None, expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference', prep:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, prep=prep)

    def Keyword(self, expr:'Hql.Expressions.Keyword', prep:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, prep=prep)

    def Identifier(self, expr:'Hql.Expressions.Identifier', prep:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, prep=prep)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard', prep:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, prep=prep)

    def Path(self, expr:'Hql.Expressions.Path', prep:bool=True) -> tuple[object, object]:
        return None, expr

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression', prep:bool=True) -> tuple[object, object]:
        return None, expr
