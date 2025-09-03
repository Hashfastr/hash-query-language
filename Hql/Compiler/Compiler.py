from typing import Union, TYPE_CHECKING, Callable
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
import logging

if TYPE_CHECKING:
    from . import BranchDescriptor
    from Hql.Operators import Operator
    from Hql.Expressions import Expression
    import Hql

class Compiler():
    def __init__(self):
        from Hql.Data import Data
        self.type = self.__class__.__name__
        self.ctx = Context(Data())

        self.ops:list['Operator'] = []

    def from_name(self, name:str) -> Callable:
        if hasattr(self, name):
            return getattr(self, name)
        raise hqle.CompilerException(f'Attempting to get non-existant compiler function for {name}')

    def run(self, ctx:Union[Context, None]=None) -> Context:
        ctx = ctx if ctx else self.ctx
        return self.ctx

    def add_op(self, op:'BranchDescriptor') -> Union['BranchDescriptor', None]:
        return op
    
    def add_ops(self, ops:list['BranchDescriptor']) -> Union[list['BranchDescriptor'], None]:
        for idx, op in enumerate(ops):
            res = self.add_op(op)
            if res:
                return [res] + ops[idx+1:]
        return None

    def optimize(self, ops):
        optimized = [ops[0]]
        
        logging.debug(f'Optimizing the following operators in for {self.type}:')
        for op in ops:
            logging.debug(f'    {op.id}: {op.type}')
        
        for op in ops[1:]:
            # This is an attempt at optimizing cases where a take can be placed higher
            i = -1
            while i >= -len(optimized):
                nonconseq = optimized[i].non_consequential(op.type)

                res = optimized[i].integrate(op)

                if res == None:
                    logging.debug(f'Integrated {op.id} into {optimized[i].id}')
                    break

                elif res != op:
                    logging.debug(f'Partially integrated {op.id} into {optimized[i].id}')
                    break
                
                if nonconseq:
                    logging.debug(f'Can optimize {op.id} passing {optimized[i].id}')
                    i -= 1

                else:
                    logging.debug(f'As high as we can go for {op.id}')
                    optimized.append(op)
                    break

        logging.debug('Final optimized set:')
        for op in optimized:
            logging.debug(f'    {op.id}: {op.type}')
            
        return optimized

    '''
    You'll want to replace this with something like a string that you'll query your database with.
    Default returns optimized operators for running in Hql-land
    '''
    def compile(self, src:Union['Expression', 'Operator'], preprocess:bool=True) -> object:
        return self.from_name(src.type)(src, preprocess=preprocess)

    def decompile(self) -> str:
        from Hql.Expressions import PipeExpression
        logging.critical("Decompilationg doesn't actually work right now, sorry")
        # return PipeExpression(pipes=self.ops).decompile(self.ctx)
        return ''

    '''
    By default, all of these return themselves as they are being
    'rejected' back to the compiler
    '''

    '''
    Statements
    '''

    def Query(self, query:'Hql.Query.Query', preprocess:bool=True) -> object:
        return query

    def Statement(self, statement:'Hql.Query.Statement', preprocess:bool=True) -> object:
        return statement

    def QueryStatement(self, statement:'Hql.Query.QueryStatement', preprocess:bool=True) -> object:
        return statement

    def LetStatement(self, statement:'Hql.Query.LetStatement', preprocess:bool=True) -> object:
        return statement

    '''
    Operators
    '''

    def PrePipe(self, op:'Hql.Operators.PrePipe', preprocess:bool=True) -> object:
        return op

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> object:
        return op

    def Project(self, op:'Hql.Operators.Project', preprocess:bool=True) -> object:
        return op

    def ProjectAway(self, op:'Hql.Operators.ProjectAway', preprocess:bool=True) -> object:
        return op

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep', preprocess:bool=True) -> object:
        return op

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder', preprocess:bool=True) -> object:
        return op

    def ProjectRename(self, op:'Hql.Operators.ProjectRename', preprocess:bool=True) -> object:
        return op

    def Take(self, op:'Hql.Operators.Take', preprocess:bool=True) -> object:
        return op

    def Count(self, op:'Hql.Operators.Count', preprocess:bool=True) -> object:
        return op

    def Extend(self, op:'Hql.Operators.Extend', preprocess:bool=True) -> object:
        return op

    def Range(self, op:'Hql.Operators.Range', preprocess:bool=True) -> object:
        return op

    def Top(self, op:'Hql.Operators.Top', preprocess:bool=True) -> object:
        return op

    def Unnest(self, op:'Hql.Operators.Unnest', preprocess:bool=True) -> object:
        return op

    def Summarize(self, op:'Hql.Operators.Summarize', preprocess:bool=True) -> object:
        return op

    def Datatable(self, op:'Hql.Operators.Datatable', preprocess:bool=True) -> object:
        return op

    def Join(self, op:'Hql.Operators.Join', preprocess:bool=True) -> object:
        return op

    def MvExpand(self, op:'Hql.Operators.MvExpand', preprocess:bool=True) -> object:
        return op

    def Sort(self, op:'Hql.Operators.Sort', preprocess:bool=True) -> object:
        return op

    '''
    Expressions
    '''

    def Tabular(self, expr:'Hql.Expressions.Expression') -> Union['Hql.Expressions.Expression', 'Hql.Operators.Database', 'Hql.Compiler.InstructionSet']:
        return expr

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression', preprocess:bool=True) -> object:
        return expr

    def OpParameter(self, expr:'Hql.Expressions.OpParameter', preprocess:bool=True) -> object:
        return expr

    def ToClause(self, expr:'Hql.Expressions.ToClause', preprocess:bool=True) -> object:
        return expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression', preprocess:bool=True) -> object:
        return expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression', preprocess:bool=True) -> object:
        return expr

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr', preprocess:bool=True) -> object:
        return expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', preprocess:bool=True) -> object:
        return expr

    def Equality(self, expr:'Hql.Expressions.Equality', preprocess:bool=True) -> object:
        return expr

    def Substring(self, expr:'Hql.Expressions.Substring', preprocess:bool=True) -> object:
        return expr

    def Relational(self, expr:'Hql.Expressions.Relational', preprocess:bool=True) -> object:
        return expr

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', preprocess:bool=True) -> object:
        return expr

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', preprocess:bool=True) -> object:
        return expr

    def BasicRange(self, expr:'Hql.Expressions.BasicRange', preprocess:bool=True) -> object:
        return expr

    def Regex(self, expr:'Hql.Expressions.Regex', preprocess:bool=True) -> object:
        return expr

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression', preprocess:bool=True) -> object:
        return expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral', preprocess:bool=True) -> object:
        return expr

    def Integer(self, expr:'Hql.Expressions.Integer', preprocess:bool=True) -> object:
        return expr

    def IP4(self, expr:'Hql.Expressions.IP4', preprocess:bool=True) -> object:
        return expr

    def Float(self, expr:'Hql.Expressions.Float', preprocess:bool=True) -> object:
        return expr

    def Bool(self, expr:'Hql.Expressions.Bool', preprocess:bool=True) -> object:
        return expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference', preprocess:bool=True) -> object:
        return expr

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference', preprocess:bool=True) -> object:
        return self.NamedReference(expr)

    def Keyword(self, expr:'Hql.Expressions.Keyword', preprocess:bool=True) -> object:
        return self.NamedReference(expr)

    def Identifier(self, expr:'Hql.Expressions.Identifier', preprocess:bool=True) -> object:
        return self.NamedReference(expr)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard', preprocess:bool=True) -> object:
        return self.NamedReference(expr)

    def Path(self, expr:'Hql.Expressions.Path', preprocess:bool=True) -> object:
        return expr

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression', preprocess:bool=True) -> object:
        return expr
