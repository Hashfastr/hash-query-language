import time
from Hql.Context import Context
from Hql.Exceptions import HqlExceptions as hqle
import logging
from typing import Callable, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Expressions import Expression
    import Hql

class Compiler():
    def __init__(self):
        from Hql.Data import Data
        self.type = self.__class__.__name__
        self.ctx = Context(Data())

        self.ops:list['Operator'] = []
        self.parents = []

    def from_name(self, name:str) -> Callable:
        if hasattr(self, name):
            return getattr(self, name)
        raise hqle.CompilerException(f'Attempting to get non-existant compiler function for {name}')

    def run(self, ctx:Union[Context, None]=None) -> Context:
        ctx = ctx if ctx else self.ctx
        return self.ctx

    def add_op(self, op:'Operator'):
        self.ops.append(op)
    
    def add_ops(self, ops:list['Operator']):
        self.ops += ops

    def add_parent(self, parent):
        self.parents.append(parent)

    def optimize(self, ops:list['Operator']):
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
    def compile(self) -> Union[str, list['Operator']]:
        return self.optimize(self.ops)

    def decompile(self) -> str:
        from Expressions import PipeExpression
        return PipeExpression(pipes=self.ops).decompile(self.ctx)

    '''
    By default, all of these return themselves as they are being
    'rejected' back to the compiler
    '''

    '''
    Statements
    '''

    def Query(self, query:'Hql.Query.Query'):
        return query

    def Statement(self, statement:'Hql.Query.Statement'):
        return statement

    def QueryStatement(self, statement:'Hql.Query.QueryStatement'):
        return statement

    def LetStatement(self, statement:'Hql.Query.LetStatement'):
        return statement

    '''
    Operators
    '''

    def PrePipe(self, op:'Hql.Operators.PrePipe'):
        return op

    def Where(self, op:'Hql.Operators.Where'):
        return op

    def Project(self, op:'Hql.Operators.Project'):
        return op

    def ProjectAway(self, op:'Hql.Operators.ProjectAway'):
        return op

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep'):
        return op

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder'):
        return op

    def ProjectRename(self, op:'Hql.Operators.ProjectRename'):
        return op

    def Take(self, op:'Hql.Operators.Take'):
        return op

    def Count(self, op:'Hql.Operators.Count'):
        return op

    def Extend(self, op:'Hql.Operators.Extend'):
        return op

    def Range(self, op:'Hql.Operators.Range'):
        return op

    def Top(self, op:'Hql.Operators.Top'):
        return op

    def Unnest(self, op:'Hql.Operators.Unnest'):
        return op

    def Summarize(self, op:'Hql.Operators.Summarize'):
        return op

    def Datatable(self, op:'Hql.Operators.Datatable'):
        return op

    def Join(self, op:'Hql.Operators.Join'):
        return op

    def MvExpand(self, op:'Hql.Operators.MvExpand'):
        return op

    def Sort(self, op:'Hql.Operators.Sort'):
        return op

    '''
    Expressions
    '''

    def Tabular(self, expr:'Hql.Expressions.Expression'):
        return expr

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression'):
        return expr

    def OpParameter(self, expr:'Hql.Expressions.OpParameter'):
        return expr

    def ToClause(self, expr:'Hql.Expressions.ToClause'):
        return expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression'):
        return expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression'):
        return expr

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr'):
        return expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction'):
        return expr

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression'):
        return expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral'):
        return expr

    def Integer(self, expr:'Hql.Expressions.Integer'):
        return expr

    def IP4(self, expr:'Hql.Expressions.IP4'):
        return expr

    def Float(self, expr:'Hql.Expressions.Float'):
        return expr

    def Bool(self, expr:'Hql.Expressions.Bool'):
        return expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference'):
        return expr

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference'):
        return self.NamedReference(expr)

    def Keyword(self, expr:'Hql.Expressions.Keyword'):
        return self.NamedReference(expr)

    def Identifier(self, expr:'Hql.Expressions.Identifier'):
        return self.NamedReference(expr)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard'):
        return self.NamedReference(expr)

    def Path(self, expr:'Hql.Expressions.Path'):
        return expr

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression'):
        return expr
