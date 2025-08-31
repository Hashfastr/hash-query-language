import time
from Hql.Context import Context
from Hql.Exceptions import HqlExceptions as hqle
import logging
from typing import Callable, Union, TYPE_CHECKING
import time

if TYPE_CHECKING:
    from Hql.Operators import Operator, Database
    from Hql.Data import Data
    from Hql.Expressions import Expression
    from .HqlCompiler import HqlCompiler
    import Hql

class InstructionSet():
    def __init__(self, upstream:Union['Database', list['Database'], 'InstructionSet', list['InstructionSet']], operators:Union[None, list['Operator']]=None) -> None:
        import random

        if isinstance(upstream, list):
            self.upstream = upstream
        else:
            self.upstream = [upstream]

        self.ops:list['Operator'] = operators if operators else []
        self.id = '%08x' % random.getrandbits(32)

    def add_op(self, op:Union['BranchDescriptor', 'Operator']):
        if isinstance(op, BranchDescriptor):
            self.ops.append(op.get_op())

        else:
            self.ops.append(op)

        return None

    def exec(self, inst:Union['Database', 'Operator'], ctx:Context) -> Context:
        logging.debug(f'Executing {inst.type} - {inst.id}')
        start = time.perf_counter()

        ctx.data = inst.eval(ctx)

        end = time.perf_counter()
        logging.debug(f'{inst.id} - {end - start}')

        return ctx

    def eval(self, ctx:Context, **kwargs) -> Context:
        logging.debug(f'Starting InstructionSet {self.id}')
        start = time.perf_counter()

        sets = []
        for i in self.upstream:
            sets.append(i.eval(Context(Data())))

        ctx = Context.merge(sets)

        for i in self.ops:
            ctx = self.exec(i, ctx)

        end = time.perf_counter()
        logging.debug(f'InstructionSet {self.id} - {end - start}')

        return ctx

'''
Wraps an Expression or Operator with some tagged metadata
Helpful for finding out if we can compile something
'''
class BranchDescriptor():
    def __init__(self):
        # contains a timeseries element
        self.attrs:dict = dict()

        self.expr:Union[None, 'Expression'] = None
        self.op:Union[None, 'Operator'] = None
        self.db:Union[None, 'Database'] = None
        self.str:str = ''
        self.join_attrs:dict = dict()
        self.list_attrs:list[str] = [
            'types',
            'functions'
        ]

    def set_attr(self, name:str, value):
        self.attrs[name] = value

    def get_attr(self, name:str):
        return self.attrs.get(name, None)

    def merge_attrs(self, attrs:dict):
        for i in attrs:
            cur = self.attrs.get(i, None)
            val = attrs[i]

            if i in self.list_attrs:
                if not isinstance(val, list):
                    val = [val]

                if cur:
                    cur += val
                else:
                    self.attrs[i] = val

            elif isinstance(cur, type(None)):
                self.attrs[i] = attrs[i]

            elif isinstance(cur, type(bool)) and isinstance(val, type(bool)):
                if not cur:
                    self.attrs[i] = attrs[i]

            # Default catchall for now
            else:
                self.attrs[i] = attrs[i]

    def get_expr(self) -> 'Expression':
        if isinstance(self.expr, type(None)):
            raise hqle.CompilerException('Attempting to access NoneType BranchDescriptor Expr')
        return self.expr

    def get_op(self) -> 'Operator':
        if isinstance(self.op, type(None)):
            raise hqle.CompilerException('Attempting to access NoneType BranchDescriptor Op')
        return self.op

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

    def add_parent(self, parent):
        self.parents.append(parent)

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
        from Expressions import PipeExpression
        return PipeExpression(pipes=self.ops).decompile(self.ctx)

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

    def Tabular(self, expr:'Hql.Expressions.Expression') -> Union['Hql.Expressions.Expression', 'Hql.Operators.Database']:
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
