import compiler.Container as Container
import compiler.Guid as Guid
import json, oyaml
import os, stat
import logging

# THE compiler which turns the assembly into containers and container configs.
# Builds networks and containers using GUIDs and linking them on who to talk to.
# At the end writes out the compose file, along with the configs for each container.
# In the compose each container is configured to reference their own configs.
class Compiler():
    def __init__(self, conf_file:str, top:dict):
        self.top = top
        self.conf_file = conf_file
        self.query_guid = Guid.gen_guid()
        self.statements = []
        self.compose = {}
        
        # load conf file
        with open(self.conf_file, mode='r') as f:
            self.conf = json.loads(f.read())
            
        self.out_dir = self.conf.get('OUTPUT_DIR', './out')
        
    def to_dict(self):
        return self.statements

    def working_dir(self):
        return self.out_dir + os.sep + self.query_guid

    #def output_service(self):
    #    return self.composes[]
        
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']
    
    def compile(self, ruleset:dict={}):
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
        self.compose = {
            'guid': self.query_guid,
            'services': {
                
            },
            'networks': {}
        }
        
        for statement in self.statements:
            statement_guid = statement['guid']
            
            self.compose['networks'][f'net-{statement_guid}'] = {
                'driver': 'bridge'
            }
            
            for container in statement['containers']:
                con_type = container['type']
                guid = container['guid']
                
                self.compose['services'][f'{con_type}-{guid}'] = self.gen_yaml(container)
                self.compose['services'][f'{con_type}-{guid}']['networks'] = [
                    f'net-{statement_guid}'
                ]

    # Generate the yaml for a particular container/service
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
    
    # Write compiled results to disk
    def write_to_disk(self):
        # make the out dir if it doesn't already exist
        try:
            os.mkdir(self.out_dir)
        except:
            logging.debug(f'Dir {self.out_dir} already exists')
        
        wd = self.working_dir()

        try:
            os.mkdir(wd)
        except:
            raise Exception('Query already exists')
        
        # Dump out the compose file
        with open(f'{wd}/compose.yml', 'w+') as f:
            oyaml.dump(self.compose, f)
        
        for statement in self.statements:
            # Write out each container config
            for container in statement['containers']:
                filename = f"{wd}/{container['type']}-{container['guid']}.json"
                with open(filename, 'w+') as f:
                    f.write(json.dumps(container, indent=2))
                    
                # Make the config file 644 so that the non-root user
                # in the container can read it.
                os.chmod(
                    filename,
                    stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH
                )