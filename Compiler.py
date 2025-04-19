import logging
import json
import Container
import Guid

class Compiler():
    def __init__(self, conf_file:str, top:dict):
        self.top = top
        self.conf_file = conf_file
        self.statements = []
        self.composes = []
        
        # load conf file
        with open(self.conf_file, mode='r') as f:
            self.conf = json.loads(f.read())
        
    def to_dict(self):
        return self.statements
    
    def get_compose(self):
        return self.composes
        
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']
    
    def compile(self, ruleset:dict):
        self.ruleset = ruleset
        
        # compile the containers for each statement
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
                containers.append(Container.IndexContainer(self.conf, index))
                
            if op == 'where':
                if containers[-1].get_type() == 'index':
                    for exp in operation['expressions']:
                        containers[-1].add_filter(exp)       
                                
        return [ x.to_dict() for x in containers ]
    
    def gen_compose(self):
        self.composes = []
        
        for statement in self.statements:
            top_guid = statement['guid']
            
            compose = {
                'guid': top_guid,
                'services': {
                    
                },
                'networks': {
                    f'net-{top_guid}': {
                        'driver': 'bridge'
                    }
                }
            }
            
            for container in statement['containers']:
                con_type = container['type']
                guid = container['guid']
                
                compose['services'][f'{con_type}-{guid}'] = self.gen_yaml(container)
                compose['services'][f'{con_type}-{guid}']['networks'] = [
                    f'net-{top_guid}'
                ]
        
            self.composes.append(compose)
        
    def gen_yaml(self, container):
        con_type = container['type']
        guid = container['guid']
        mnt_flags = self.conf['MNT_FLAGS']
        
        yaml = {
            'container_name': f'{con_type}-{guid}',
            'image': self.conf['IMAGES'][con_type],
            'restart': self.conf['RESTART_POLICY'],
            'volumes': [
                f'./{con_type}-{guid}.json:/opt/hql/conf.json:{mnt_flags}'
            ],
            'userns': 'auto',
            'group-add': [
                'keep-groups'
            ],
            'cap_add': [
                'NET_RAW'
            ]
        }
        
        return yaml