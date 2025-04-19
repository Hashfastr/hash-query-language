import logging
import json
import Container
import Guid

class Compiler():
    def __init__(self, conf_file:str, top:dict):
        self.top = top
        self.conf_file = conf_file
        
    def to_dict(self):
        return self.statements
        
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']
    
    def compile(self, ruleset:dict):
        self.ruleset = ruleset
        
        # compile the containers for each statement
        self.statements = []
        for statement in self.top['statements']:
            compiled = {
                'guid': Guid.gen_guid()
            }
            
            compiled['containers'] = self.compile_statement(statement)
                        
            self.statements.append(compiled)
                                
    def compile_statement(self, statement:dict):
        containers = []
        
        for operation in statement['operations']:
            op = operation['type']
                        
            if op == 'index':
                if len(containers) != 0:
                    logging.error("Compiler error, attempting to add an index not at top level.")
                    logging.error(json.dumps(statement))
                    raise Exception("Compiler Exception")
                
                index = operation['expressions'][0]['name']
                containers.append(Container.IndexContainer(self.conf_file, index))
                
            if op == 'where':
                if containers[-1].get_type() == 'index':
                    for exp in operation['expressions']:
                        containers[-1].add_filter(exp)       
                                
        return [ x.to_dict() for x in containers ]