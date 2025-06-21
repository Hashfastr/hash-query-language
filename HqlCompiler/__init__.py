__all__ = [
    "Operators",
    "Exceptions",
    "Expr",
    "HqlVisitor",
    "Query",
    "Compiler"
]

import time
import HqlCompiler.Config as Config
from HqlCompiler.Query import *
from HqlCompiler.Functions import *
from HqlCompiler.Operators.Database import Database as Database
from HqlCompiler.Operators.Database import get_database
import HqlCompiler.Expression as Expr
import HqlCompiler.Operators as Ops
from HqlCompiler.Context import Context
import logging

class CompilerException(Exception):
    ...

class CompilerSet():
    def __init__(self, ops:list[Ops.Operator]):
        self.type = self.__class__.__name__
        self.ops = ops
        
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
                integrate = compiled[i].can_integrate(op.type)
                
                if nonconseq and not integrate:
                    logging.debug(f'Can optimize {op.id} passing {compiled[i].id}')
                    i -= 1
                if integrate:
                    logging.debug(f'Integrating {op.id} into {compiled[i].id}')
                    compiled[i].add_op(op)
                    break
                elif not nonconseq and not integrate:
                    logging.debug(f'As high as we can go for {op.id}')
                    compiled.append(op)
                    break
                
        logging.debug('Final compiled set:')
        for op in compiled:
            logging.debug(f'    {op.id}: {op.type}')
            
        self.ops = compiled
    

    def add_ops(self, ops:list[Ops.Operator]):
        self.ops += ops
        self.compile()
        
    
    def add_op(self, op:Ops.Operator):
        self.add_ops([op])
        
    
    def eval(self, ctx:Context, **kwargs):
        ctx = Context(None, ctx.symbol_table)
        
        for i in self.ops:
            start = time.perf_counter()
            logging.debug(f'Executing {i.type}: {i.id}')
            
            data = i.eval(ctx)
            ctx.data = data
                        
            end = time.perf_counter()
            logging.debug(f"{i.id} - {end - start}")
            
        return ctx.data

# THE compiler which turns the assembly into containers and container configs.
# Builds networks and containers using GUIDs and linking them on who to talk to.
# At the end writes out the compose file, along with the configs for each container.
# In the compose each container is configured to reference their own configs.
class Compiler():
    def __init__(self, conf_file:str, query:Query):
        self.query = query
        Config.HqlConfig = Config.Config(conf_file)
        self.ctx = Context(None)
    
    # Not used yet, will probably make sense eventually
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']

    def run(self, ctx:Context=None):
        ctx = ctx if ctx else self.ctx
        
        if not ctx.root:
            logging.critical('No root statement compiled!')
            raise CompilerException('No root statement compiled before runtime!')
        
        return ctx.root.eval(ctx)
 
    def compile(self):        
        self.compiled = []
        self.op_sets = []
        ctx = Context(None)
                
        statement = self.query.statements
        
        for statement in self.query.statements:
            if statement.type == "LetExpression":
                logging.debug('Letting let expression')
                root = statement.value
                
            if statement.type == "QueryStatement":
                logging.debug('Handling QueryStatement')
                root = statement.root
            
            if root.type == "PrePipe":
                prepipe = root
                pipes = []
            else:
                prepipe = root.prepipe
                pipes = root.pipes
                
            op = prepipe.eval(ctx, tabular=True)
            
            if isinstance(op, CompilerSet):
                cs = op
                cs.add_ops(pipes) # This recompiles automatically
                
            else:
                cs = CompilerSet([op] + pipes)
                cs.compile()
                                
            if statement.type == "LetExpression":
                name = statement.name.eval(ctx, as_str=True)
                ctx.symbol_table[name] = cs
                
            else:
                if ctx.root:
                    logging.warning('Overwriting root compiler set, bug?')
                    
                ctx.root = cs
                
        self.ctx = ctx