import time
from Hql.Context import Context
from Hql.Exceptions import HqlExceptions as hqle
import logging
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Expressions import Expression

class CompilerSet():
    def __init__(self, ops:list[Union['Operator', "CompilerSet"]]):
        self.type = self.__class__.__name__
        self.ops = self.adjust_set(ops)

    def adjust_set(self, ops:list[Union['Operator', "CompilerSet"]]) -> list['Operator']:
        from Hql.Operators import Operator

        new_ops = []
        for i in ops:
            if isinstance(i, type(self)):
                new_ops += i.ops

            elif isinstance(i, Operator):
                new_ops.append(i)

            else:
                raise hqle.CompilerException(f'Passed invalid type to {type(i)} to compilerset')

        return new_ops
        
    def compile(self):
        compiled = [self.ops[0]]
        
        logging.debug('Optimizing the following operators in a compilerset:')
        for op in self.ops:
            logging.debug(f'    {op.id}: {op.type}')
        
        for op in self.ops[1:]:
            # This is an attempt at optimizing cases where a take can be placed higher
            i = -1
            while i >= -len(compiled):
                nonconseq = compiled[i].non_consequential(op.type)

                res = compiled[i].integrate(op)

                if res == None:
                    logging.debug(f'Integrated {op.id} into {compiled[i].id}')
                    break

                elif res != op:
                    logging.debug(f'Partially integrated {op.id} into {compiled[i].id}')
                    break
                
                if nonconseq:
                    logging.debug(f'Can optimize {op.id} passing {compiled[i].id}')
                    i -= 1

                else:
                    logging.debug(f'As high as we can go for {op.id}')
                    compiled.append(op)
                    break
                
        logging.debug('Final compiled set:')
        for op in compiled:
            logging.debug(f'    {op.id}: {op.type}')
            
        self.ops = compiled

        return self
    
    def add_ops(self, ops:list['Operator']):
        self.ops += ops
        self.compile()
        
    def add_op(self, op:'Operator'):
        self.add_ops([op])
    
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Data import Data

        ctx = Context(Data(), ctx.symbol_table)
        preview = kwargs.get('preview', False)
        pdict = []
        
        for i in self.ops:
            start = time.perf_counter()
            logging.debug(f'Executing {i.type}: {i.id}')
            
            data = i.eval(ctx, preview=preview)

            if preview:
                pdict.append(data)
            else:
                ctx.data = data
                        
            end = time.perf_counter()
            logging.debug(f"{i.id} - {end - start}")
            
        if preview:
            return pdict

        return ctx.data

class Compiler():
    def __init__(self):
        from Hql.Data import Data
        self.ctx = Context(Data())
        self.ops:list['Operator'] = []
        self.root:Union[None, 'Expression', 'Operator'] = None

    def run(self, ctx:Union[Context, None]=None):
        ctx = ctx if ctx else self.ctx
        raise hqle.QueryException('Running an empty compiler has no effect!')

    def add_op(self, op:'Operator'):
        self.ops.append(op)

    def compile(self):
        return ''

    def decompile(self):
        if not self.root:
            return ''
        return self.root.decompile(self.ctx)

    '''
    By default, all of these return themselves as they are being
    'rejected' back to the compiler
    '''

    def Where(self, op:'Operator'):
        return op

    def Project(self, op:'Operator'):
        return op

    def ProjectAway(self, op:'Operator'):
        return op

    def ProjectKeep(self, op:'Operator'):
        return op

    def ProjectReorder(self, op:'Operator'):
        return op

    def ProjectRename(self, op:'Operator'):
        return op

    def Take(self, op:'Operator'):
        return op

    def Count(self, op:'Operator'):
        return op

    def Extend(self, op:'Operator'):
        return op

    def PrePipe(self, op:'Operator'):
        return op

    def Range(self, op:'Operator'):
        return op

    def Top(self, op:'Operator'):
        return op

    def Unnest(self, op:'Operator'):
        return op

    def Summarize(self, op:'Operator'):
        return op

    def Datatable(self, op:'Operator'):
        return op

    def Join(self, op:'Operator'):
        return op

    def MvExpand(self, op:'Operator'):
        return op

    def Sort(self, op:'Operator'):
        return op

    def PipeExpression(self, expr:'Expression'):
        return expr

    def OpParameter(self, expr:'Expression'):
        return expr

    def ToClause(self, expr:'Expression'):
        return expr

    def OrderedExpression(self, expr:'Expression'):
        return expr

    def ByExpression(self, expr:'Expression'):
        return expr

    def FuncExpr(self, expr:'Expression'):
        return expr

    def DotCompositeFunction(self, expr:'Expression'):
        return expr

    def TypeExpression(self, expr:'Expression'):
        return expr

    def StringLiteral(self, expr:'Expression'):
        return expr

    def Integer(self, expr:'Expression'):
        return expr

    def IP4(self, expr:'Expression'):
        return expr

    def Float(self, expr:'Expression'):
        return expr

    def Bool(self, expr:'Expression'):
        return expr
