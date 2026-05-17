from typing import Optional, Union, TYPE_CHECKING

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context

from . import Compiler

if TYPE_CHECKING:
    from Hql.Compiler import BranchDescriptor, InstructionSet
    from Hql.Operators.Operator import Operator
    from Hql.Expressions import Expression
    from Hql.Query import Statement
    import Hql

class KustoCompiler(Compiler):
    def __init__(self):
        from Hql.Data import Data
        self.type = self.__class__.__name__
        self.ctx = Context(Data())

        self.stmts:list['Statement'] = []

    def optimize(self, ops: list['BranchDescriptor']) -> list['BranchDescriptor']:
        return ops

    def compile(self, preprocess:bool=True) -> tuple[Union[str, list['Statement']], None]:
        stmts = []
        for i in self.stmts:
            acc, _ = self.compile_stmt(i, preprocess=preprocess)
            stmts.append(acc)

        if preprocess:
            return stmts, None
        return '\n;\n'.join(stmts), None

    def compile_op(self, src:'Operator', preprocess:bool=True) -> tuple[Union['Operator', str, None], Optional['Operator']]:
        return self.from_name(src.type)(src, preprocess=preprocess)

    def compile_expr(self, src:'Expression', preprocess:bool=True) -> tuple[Union['Expression', str, None], Optional['Expression']]:
        return self.from_name(src.type)(src, preprocess=preprocess)

    def compile_stmt(self, src:'Statement', preprocess:bool=True) -> tuple[Union['Statement', str, None], Optional['Statement']]:
        from Hql.Query import QueryStatement
        from Hql.Expressions import Expression, PipeExpression

        if isinstance(src, QueryStatement):
            acc, rej = self.compile_expr(src.root, preprocess=preprocess)
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

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Expression, PipeExpression

        if isinstance(expr.prepipe, Expression):
            acc, rej = self.compile_expr(expr.prepipe, preprocess=preprocess)
            if rej:
                return None, expr
            prepipe = acc
        else:
            prepipe = None

        for i in expr.pipes:
            i.



        return None, expr

    '''
    Operators
    '''

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Operators.Where import Where
        from Hql.Expressions.Logic import Logic

        if preprocess:
            expr, _ = self.compile_expr(op.expr)
            assert isinstance(expr, Logic)
            return Where(expr), None

        out = 'where '
        expr, _ = self.compile_expr(op.expr, preprocess=False)
        assert isinstance(expr, str)
        return out + expr, None

    def Project(self, op:'Hql.Operators.Project', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            exprs = []
            for i in op.exprs:
                expr, rej = self.compile(i)
                if rej:
                    return None, op
                assert isinstance(expr, 'Expression')
                exprs.append(expr)
            op.exprs = exprs
            return op, None

        out = f'| {op.optok} '
        exprs = []
        for i in op.exprs:
            expr, _ = self.compile(op.expr, preprocess=False)
            assert isinstance(expr, str)
            exprs.append(expr)
        out += ', '.join(exprs)
        return out, None

    def ProjectAway(self, op:'Hql.Operators.ProjectAway', preprocess:bool=True) -> tuple[object, object]:
        return self.Project(op, preprocess=preprocess)

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep', preprocess:bool=True) -> tuple[object, object]:
        return self.Project(op, preprocess=preprocess)

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder', preprocess:bool=True) -> tuple[object, object]:
        return self.Project(op, preprocess=preprocess)

    def ProjectRename(self, op:'Hql.Operators.ProjectRename', preprocess:bool=True) -> tuple[object, object]:
        return self.Project(op, preprocess=preprocess)

    def Take(self, op:'Hql.Operators.Take', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            if op.tables:
                return None, op
            return op, None
        out = '| take '
        val, _ = self.compile(op.expr, False)
        assert isinstance(val, str)
        return out + val, None

    def Count(self, op:'Hql.Operators.Count', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            if op.name:
                return None, op
            return op, None
        out = '| count'
        return out, None

    def Extend(self, op:'Hql.Operators.Extend', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            exprs = []
            for i in op.exprs:
                expr, rej = self.compile(i)
                if rej:
                    return None, op
                assert isinstance(expr, 'Expression')
                exprs.append(expr)
            op.exprs = exprs
            return op, None

        out = f'| extend '
        exprs = []
        for i in op.exprs:
            expr, _ = self.compile(op.expr, preprocess=False)
            assert isinstance(expr, str)
            exprs.append(expr)
        out += ', '.join(exprs)
        return out, None

    def Range(self, op:'Hql.Operators.Range', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Context import Context
        from Hql.Data import Data
        
        if preprocess:
            return op, None
        out = op.decompile(Context(Data(None)))
        return out, None

    def Top(self, op:'Hql.Operators.Top', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Context import Context
        from Hql.Data import Data
        
        if preprocess:
            return op, None
        out = op.decompile(Context(Data(None)))
        return out, None

    def Unnest(self, op:'Hql.Operators.Unnest', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Union(self, op:'Hql.Operators.Union', preprocess:bool=True) -> tuple[object, object]:
        return None, op

        from Hql.Context import Context
        from Hql.Data import Data
        
        if preprocess:
            return op, None
        out = op.decompile(Context(Data(None)))
        return out, None

    def Summarize(self, op:'Hql.Operators.Summarize', preprocess:bool=True) -> tuple[object, object]:

        return None, op

    def Datatable(self, op:'Hql.Operators.Datatable', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Join(self, op:'Hql.Operators.Join', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def MvExpand(self, op:'Hql.Operators.MvExpand', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Sort(self, op:'Hql.Operators.Sort', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Rename(self, op:'Hql.Operators.Rename', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    '''
    Expressions
    '''

    def OpParameter(self, expr:'Hql.Expressions.OpParameter', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def ToClause(self, expr:'Hql.Expressions.ToClause', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Function(self, expr:'Hql.Functions.Function', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Equality(self, expr:'Hql.Expressions.Equality', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Substring(self, expr:'Hql.Expressions.Substring', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Relational(self, expr:'Hql.Expressions.Relational', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Not(self, expr:'Hql.Expressions.Not', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BasicRange(self, expr:'Hql.Expressions.BasicRange', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Regex(self, expr:'Hql.Expressions.Regex', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral', preprocess:bool=True) -> tuple[object, object]:
        return None, expr
    
    def MultiString(self, expr:'Hql.Expressions.MultiString', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Integer(self, expr:'Hql.Expressions.Integer', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def IP4(self, expr:'Hql.Expressions.IP4', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Float(self, expr:'Hql.Expressions.Float', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Bool(self, expr:'Hql.Expressions.Bool', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Multivalue(self, expr:'Hql.Expressions.Multivalue', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Datetime(self, expr:'Hql.Expressions.Datetime', preprocess:bool=True) -> tuple[object, object]:
        return None, expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Keyword(self, expr:'Hql.Expressions.Keyword', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Identifier(self, expr:'Hql.Expressions.Identifier', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Path(self, expr:'Hql.Expressions.Path', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr
