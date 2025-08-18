from pathlib import Path
import Hql.Operators as Ops
import time
import Hql.Config as Config
from Hql.Query import Query
from Hql.Context import Context
from Hql.Exceptions import HqlExceptions as hqle
import logging
from typing import Union

class CompilerSet():
    def __init__(self, ops:list[Union[Ops.Operator, "CompilerSet"]]):
        self.type = self.__class__.__name__
        self.ops = self.adjust_set(ops)

    def adjust_set(self, ops:list[Union[Ops.Operator, "CompilerSet"]]) -> list[Ops.Operator]:
        new_ops = []
        for i in ops:
            if isinstance(i, type(self)):
                new_ops += i.ops

            elif isinstance(i, Ops.Operator):
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
    
    def add_ops(self, ops:list[Ops.Operator]):
        self.ops += ops
        self.compile()
        
    def add_op(self, op:Ops.Operator):
        self.add_ops([op])
    
    def eval(self, ctx:'Context', **kwargs):
        ctx = Context(None, ctx.symbol_table)
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
    def __init__(self, conf_file:Path, query:Query):
        from Hql.Data import Data

        self.query = query
        self.ctx = Context(Data())

    def run(self, ctx:Union[Context,None]=None, **kwargs):
        ctx = ctx if ctx else self.ctx
        preview = kwargs.get('preview', False)
        
        if not ctx.root:
            logging.critical('No root statement compiled!')
            raise hqle.CompilerException('No root statement compiled before runtime!')
        
        return ctx.root.eval(ctx, preview=preview)

    def decompile(self):
        return self.query.decompile(self.ctx)
 
    def compile(self):
        from Hql.Query import Statement, LetStatement, QueryStatement
        from Hql.Data import Data

        self.compiled = []
        self.op_sets = []
        ctx = Context(Data())
                
        statement = self.query.statements
        
        for statement in self.query.statements:
            if isinstance(statement, Statement):
                logging.debug(f'Handling {statement.type}')
                root = statement.root

            else:
                raise hqle.CompilerException(f'Unhandled statement type {statement.type}')

            cs = root.eval(ctx, no_exec=True)
                                
            if isinstance(statement, LetStatement):
                name = statement.name.eval(ctx, as_str=True)
                ctx.symbol_table[name] = cs
                
            elif isinstance(statement, QueryStatement):
                if ctx.root:
                    logging.warning('Overwriting root compiler set, bug?')
                    
                ctx.root = cs

            else:
                raise hqle.CompilerException(f'Unhandled statement type {statement.type}')
                
        self.ctx = ctx
