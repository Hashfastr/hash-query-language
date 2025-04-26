__all__ = [
    "Operators",
    "Exceptions",
    "Expression",
    "HqlVisitor",
    "Query",
    "Compiler"
]

import json
from .Config import Config
from .Query import *
from .Functions import *
from .Operators.Index import Index as Index
from .Operators.Index import get_indexer

class CompilerException(Exception): ...

# THE compiler which turns the assembly into containers and container configs.
# Builds networks and containers using GUIDs and linking them on who to talk to.
# At the end writes out the compose file, along with the configs for each container.
# In the compose each container is configured to reference their own configs.
class Compiler():
    def __init__(self, conf_file:str, query:Query):
        self.query = query
        self.conf_file = conf_file
        
        self.conf = Config(conf_file)
            
        self.stages = []
    
    # Not used yet, will probably make sense eventually
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']

    def compile(self):        
        compiled = []
        statement = self.query.statements[0]
        
        for op in statement.operations:
            if op.type == 'index':
                compiled.append(self.resolve_index(op))
                
        print(len(compiled))

    def resolve_index(self, op):
        expr = op.expressions[0]
        
        if expr.type == 'PathExpression':
            path = expr.path
            if path[0].type == 'Function':
                if path[0].name == 'database':
                    db = Functions.get_func('database')(path[0].args)
                    conf = db.eval(self.conf)['results'][0]
                else:
                    raise CompilerException(f"Invalid function for index {path[0].name}")
            else:
                raise CompilerException(f"Invalid index reference type {path[0].type}")
        else:
            raise CompilerException(f"Invalid index reference type {expr.type}")
        
        indexer = get_indexer(conf)
        
        return indexer