import logging
import json

class Compiler():
    def __init__(self, conf_file:str, top:dict):
        self.top = top
        self.conf_file = conf_file
    
    def isblocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']
    
    def compile(self, ruleset:dict):
        self.ruleset = ruleset
        
        statements = []
        for statement in self.top['statements']:
            compiled = self.compile_statement(statement)
            statements.append(compiled)
                    
    def compile_containers(self, statement:dict):
        containers = []
        
        for operation in statement['operations']:
            op = operation['type']
            
            if op == 'index':
                if len(containers) != 0:
                    logging.error("Compiler error, attempting to add an index not at top level.")
                    logging.error(json.dumps(statement))
                    raise Exception("Compiler Exception")
                
                containers.append[]
                
                compiled['INDEX'] = operation['expressions'][0]['name']