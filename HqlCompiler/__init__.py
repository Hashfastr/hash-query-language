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
from HqlCompiler.Context import Context
import logging

class CompilerException(Exception):
    ...

class CompilerSet():
    def __init__(self, exprs:list[Expr.Expression], op_sets:list[str]):
        self.type = self.__class__.__name__
        self.exprs = exprs
        self.op_sets = op_sets
    
    def eval(self, ctx:Context, **kwargs):
        seti = 0
        ctx = Context(None)
        
        for i in self.exprs:
            start = time.perf_counter()
            
            logging.debug(f'Executing opset {self.op_sets[seti]}')
            
            data = i.eval(ctx)
            ctx.data = data
                        
            end = time.perf_counter()
            logging.debug(f"{self.op_sets[seti]} - {end - start}")
            
            seti += 1
            
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
            compiled = []
            op_sets = []
            
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
            compiled.append(op)
            op_sets.append([op.type])
            
            for op in pipes:
                # This is an attempt at optimizing cases where a take can be placed higher
                i = -1
                while i >= -len(self.compiled):
                    nonconseq = self.compiled[i].non_consequential(op.type)
                    integrate = self.compiled[i].can_integrate(op.type)
                    
                    if nonconseq and not integrate:
                        logging.debug(f'Can optimize {op.type} passing {self.compiled[i].type}')
                        i -= 1
                    if integrate:
                        logging.debug(f'Integrating {op.type} into {self.compiled[i].type}')
                        self.compiled[i].add_op(op)
                        self.op_sets[i].append(op.type)
                        break
                    elif not nonconseq and not integrate:
                        logging.debug(f'As high as we can go for type {op.type}')
                        self.compiled.append(op)
                        self.op_sets.append([op.type])
                        break
                    
            cs = CompilerSet(compiled, op_sets)
            
            if statement.type == "LetExpression":
                name = statement.name.eval(ctx, as_str=True)
                ctx.symbol_table[name] = cs
                
            else:
                if ctx.root:
                    logging.warning('Overwriting root compiler set, bug?')
                    
                ctx.root = cs
                
        self.ctx = ctx