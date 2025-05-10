__all__ = [
    "Operators",
    "Exceptions",
    "Expression",
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
import HqlCompiler.Expression as Expression
import logging

class CompilerException(Exception): ...

# THE compiler which turns the assembly into containers and container configs.
# Builds networks and containers using GUIDs and linking them on who to talk to.
# At the end writes out the compose file, along with the configs for each container.
# In the compose each container is configured to reference their own configs.
class Compiler():
    def __init__(self, conf_file:str, query:Query):
        self.query = query
                
        Config.HqlConfig = Config.Config(conf_file)
        
        self.stages = []
    
    # Not used yet, will probably make sense eventually
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']

    def run(self):
        results = None
        seti = 0
        for i in self.compiled:
            start = time.perf_counter()
            
            logging.debug(f'Executing opset {self.op_sets[seti]}')
            
            results = i.execute(results)
            
            end = time.perf_counter()
            logging.debug(f"{self.op_sets[seti]} - {end - start}")
            
            seti += 1
            
        return results
 
    def compile(self):        
        self.compiled = []
        self.op_sets = []
        
        statement = self.query.statements[0]
        
        if statement.type == "QueryStatement":
            logging.debug('Handling QueryStatement')

            root = statement.root
            
            if root.type == "PrePipe":
                prepipe = root.execute(None)
                self.compiled.append(prepipe)
                self.op_sets.append([prepipe.type])
                return
            
            prepipe = root.prepipe.execute(None)
            self.compiled.append(prepipe)
            self.op_sets.append([prepipe.type]) 
                         
            for op in root.pipes:
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