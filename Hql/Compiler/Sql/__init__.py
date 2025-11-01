from typing import Optional, Union, TYPE_CHECKING, Callable

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
import logging

if TYPE_CHECKING:
    from Hql.Compiler import BranchDescriptor, InstructionSet
    from Hql.Operators import Operator
    # from Hql.Expressions import Expression
    from Hql.Query import Statement
    import Hql

'''
Generic SQL compiler
'''
class SqlCompiler():
    def __init__(self):
        from Hql.Data import Data
        from Hql.Compiler import HqlCompiler
        from Hql.Config import Config
        self.type = self.__class__.__name__
        self.ctx = Context(Data())
        self.vestigial_compiler = HqlCompiler(Config())

        self.where:Optional['Hql.Operators.Where'] = None

    def from_name(self, name:str) -> Callable:
        if hasattr(self, name):
            return getattr(self, name)
        raise hqle.CompilerException(f'Attempting to get non-existant compiler function for {name}')

    def run(self, ctx:Union[Context, None]=None) -> Context:
        ctx = ctx if ctx else self.ctx
        return self.ctx

    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Optional['Operator'], Optional['Operator']]:
        from Hql.Compiler import BranchDescriptor
        if isinstance(op, BranchDescriptor):
            op = op.get_op()
        return None, op
    
    def add_ops(self, ops:list['BranchDescriptor']) -> Optional[list['Operator']]:
        for idx, op in enumerate(ops):
            acc, rej = self.add_op(op)
            if rej:
                return [rej] + [x.get_op() for x in ops[idx+1:]]
        return None

    def optimize(self, ops: list['BranchDescriptor']) -> list['BranchDescriptor']:
        return ops

    '''
    You'll want to replace this with something like a string that you'll query your database with.
    Default returns optimized operators for running in Hql-land
    '''
    def compile(self, src:Union['Hql.Expressions.Expression', 'Operator', 'Statement', None], preprocess:bool=True) -> tuple[Optional[object], Optional[object]]:
        if src == None:
            raise hqle.CompilerException('Unimplemented root compile')
        return self.from_name(src.type)(src, preprocess=preprocess)

    def decompile(self) -> str:
        from Hql.Expressions import PipeExpression
        logging.critical("Decompilation doesn't actually work right now, sorry")
        # return PipeExpression(pipes=self.ops).decompile(self.ctx)
        return ''

    '''
    By default, all of these return themselves as they are being
    'rejected' back to the compiler
    '''

    '''
    Operators
    '''

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Project(self, op:'Hql.Operators.Project', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectAway(self, op:'Hql.Operators.ProjectAway', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectRename(self, op:'Hql.Operators.ProjectRename', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Take(self, op:'Hql.Operators.Take', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Count(self, op:'Hql.Operators.Count', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Extend(self, op:'Hql.Operators.Extend', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Range(self, op:'Hql.Operators.Range', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Top(self, op:'Hql.Operators.Top', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Unnest(self, op:'Hql.Operators.Unnest', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Union(self, op:'Hql.Operators.Union', preprocess:bool=True) -> tuple[object, object]:
        return None, op

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

    def Tabular(self, expr:'Hql.Expressions.Expression') -> tuple[Optional['InstructionSet'], Optional['Hql.Expressions.Expression']]:
        return None, expr

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def OpParameter(self, expr:'Hql.Expressions.OpParameter', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def ToClause(self, expr:'Hql.Expressions.ToClause', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Function(self, expr:'Hql.Functions.Function', preprocess:bool=True, negate:bool=False) -> tuple[object, object]:
        if expr.name == 'isnull':
            if preprocess:
                acc, rej = self.compile(expr.args[0])
                if rej:
                    return None, expr
                expr.args[0] = acc
                return expr, None
            lh, _ = self.compile(expr.args[0], preprocess=False)
            if negate:
                return f'{lh} NOTNULL', None
            else:
                return f'{lh} ISNULL', None

        return None, expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Equality(self, expr:'Hql.Expressions.Equality', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Equality, Expression

        if preprocess:
            if expr.cs:
                logging.warning('Case sensitive comparison in Lucene has inconsistent results')
                logging.warning('For compatibility, assuming agnostic')

            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            assert isinstance(acc, Expression)
            lh = acc

            rh = []
            for i in expr.rh:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                rh.append(acc)

            return Equality(lh, expr.op, rh), None

        lh, rej = self.compile(expr.lh, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')

        rh = []
        for i in expr.rh:
            acc, rej = self.compile(i, preprocess=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            if isinstance(acc, list):
                rh += acc
            else:
                rh.append(acc)
        
        eqs = [f'{lh}:{x}' for x in rh]
        ret = ' OR '.join(eqs)
        if len(eqs) > 1:
            ret = f'({ret})'

        return f'(NOT {ret})' if expr.neq else ret, None

    def Substring(self, expr:'Hql.Expressions.Substring', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Relational(self, expr:'Hql.Expressions.Relational', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Not(self, expr:'Hql.Expressions.Not', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Functions import Function
        from Hql.Expressions import Expression
        if preprocess:
            acc, rej = self.compile(expr.expr)
            if rej:
                return None, expr
            assert isinstance(acc, Expression)
            expr.expr = acc
            return expr, None

        val, _ = self.compile(expr.expr, preprocess=False)
        assert isinstance(val, str)
        
        # quick optimization
        if isinstance(expr.expr, Function) and expr.expr.name == 'isnull':
            val, _ = self.Function(expr.expr, preprocess=False, negate=True)

        else:
            val = f'NOT {val}'

        return val, None

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
        if preprocess:
            return expr, None
        return str(expr.value), None

    def IP4(self, expr:'Hql.Expressions.IP4', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Float(self, expr:'Hql.Expressions.Float', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return str(expr.value), None

    def Bool(self, expr:'Hql.Expressions.Bool', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        val = 'TRUE' if expr.value else 'FALSE'
        return val, None

    def Multivalue(self, expr:'Hql.Expressions.Multivalue', preprocess:bool=True) -> tuple[object, object]:
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
