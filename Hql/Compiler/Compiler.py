from typing import Union, TYPE_CHECKING, Callable
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
import logging

if TYPE_CHECKING:
    from . import BranchDescriptor
    from Hql.Operators import Operator, Database
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

    def add_op(self, op:'BranchDescriptor'):
        self.ops.append(op.get_op())
    
    def add_ops(self, ops:list['Operator']):
        self.ops += ops

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
    def compile(self, src:Union['Expression', 'Operator']) -> object:
        return ''

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

    def Query(self, query:'Hql.Query.Query') -> object:
        return query

    def Statement(self, statement:'Hql.Query.Statement') -> object:
        return statement

    def QueryStatement(self, statement:'Hql.Query.QueryStatement') -> object:
        return statement

    def LetStatement(self, statement:'Hql.Query.LetStatement') -> object:
        return statement

    '''
    Operators
    '''

    def PrePipe(self, op:'Hql.Operators.PrePipe') -> object:
        return op

    def Where(self, op:'Hql.Operators.Where') -> object:
        return op

    def Project(self, op:'Hql.Operators.Project') -> object:
        return op

    def ProjectAway(self, op:'Hql.Operators.ProjectAway') -> object:
        return op

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep') -> object:
        return op

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder') -> object:
        return op

    def ProjectRename(self, op:'Hql.Operators.ProjectRename') -> object:
        return op

    def Take(self, op:'Hql.Operators.Take') -> object:
        return op

    def Count(self, op:'Hql.Operators.Count') -> object:
        return op

    def Extend(self, op:'Hql.Operators.Extend') -> object:
        return op

    def Range(self, op:'Hql.Operators.Range') -> object:
        return op

    def Top(self, op:'Hql.Operators.Top') -> object:
        return op

    def Unnest(self, op:'Hql.Operators.Unnest') -> object:
        return op

    def Summarize(self, op:'Hql.Operators.Summarize') -> object:
        return op

    def Datatable(self, op:'Hql.Operators.Datatable') -> object:
        return op

    def Join(self, op:'Hql.Operators.Join') -> object:
        return op

    def MvExpand(self, op:'Hql.Operators.MvExpand') -> object:
        return op

    def Sort(self, op:'Hql.Operators.Sort') -> object:
        return op

    '''
    Expressions
    '''

    def Tabular(self, expr:'Hql.Expressions.Expression') -> Union['Hql.Expressions.Expression', 'Hql.Operators.Database', 'Hql.Compiler.InstructionSet']:
        return expr

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression') -> object:
        return expr

    def OpParameter(self, expr:'Hql.Expressions.OpParameter') -> object:
        return expr

    def ToClause(self, expr:'Hql.Expressions.ToClause') -> object:
        return expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression') -> object:
        return expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression') -> object:
        return expr

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr') -> object:
        return expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction') -> object:
        return expr

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression') -> object:
        return expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral') -> object:
        return expr

    def Integer(self, expr:'Hql.Expressions.Integer') -> object:
        return expr

    def IP4(self, expr:'Hql.Expressions.IP4') -> object:
        return expr

    def Float(self, expr:'Hql.Expressions.Float') -> object:
        return expr

    def Bool(self, expr:'Hql.Expressions.Bool') -> object:
        return expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference') -> object:
        return expr

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference') -> object:
        return self.NamedReference(expr)

    def Keyword(self, expr:'Hql.Expressions.Keyword') -> object:
        return self.NamedReference(expr)

    def Identifier(self, expr:'Hql.Expressions.Identifier') -> object:
        return self.NamedReference(expr)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard') -> object:
        return self.NamedReference(expr)

    def Path(self, expr:'Hql.Expressions.Path') -> object:
        return expr

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression') -> object:
        return expr
