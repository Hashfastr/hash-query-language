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
        
        self.runtimes = [
            'podman',
            'docker',
        ]
        
        # load conf file
        with open(self.conf_file, mode='r') as f:
            self.conf = json.loads(f.read())
            
        self.out_dir = self.conf.get('OUTPUT_DIR', './out')
        
        self.ext_mnt_flags = 'z'
        self.conf_mnt_flags = 'ro'
        
        self.mnt_flags = [self.conf_mnt_flags, self.ext_mnt_flags]
        
        if 'container_runtime' in self.conf:
            self.runtime = self.conf['container_runtime']            
        else:
            self.runtime = self.get_exec()
        
        
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
        
    def to_dict(self):
        return self.statements

    def working_dir(self):
        return self.out_dir + os.sep + self.query_guid
    
    # Not used yet, will probably make sense eventually
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']
    
    def get_exec(self):
        path = os.environ.get('PATH', '')
        
        if path == '':
            raise Exception("Empty shell $PATH detected!")
        
        for directory in path.split(':'):
            for runtime in self.runtimes:
                full = directory + os.sep + runtime
                if os.path.isfile(full):
                    return full
                
        raise Exception('No runtime available on the system!')
    
    # Go through each statement in the query and compile it
    def compile(self):        
        # compile the containers for each statement
        for statement in self.top['statements']:
            compiled = {
                # generate the statement guid
                'guid': Guid.gen_guid(),
            }
            
            # Compile the containers for the statement
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
                                
        return containers

    def network_create(self, guid:str):
        return 
    
    def gen_mnt_flags(self):
        if len(self.mnt_flags) == 0:
            return ""
        else:
            return f":{','.join(self.mnt_flags)}"
    
    def gen_commands(self):
        cmds = {
            'capture': [],
            'entry': [],
            'exit': [],
            'kill': []
        }
        flags = self.gen_mnt_flags()
        
        for statement in self.statements:
            guid = statement['guid']
            
            network = f"{guid}-net"
            net_cmd = [
                self.runtime,
                'network',
                'create',
                network
            ]
            cmds['entry'].append(net_cmd)
            
            for container in statement['containers']:
                cmds['entry'].append(container.gen_entry_cmd(self.runtime, network, flags))
                cmds['exit'].append(container.gen_exit_cmd(self.runtime))
                cmds['kill'].append(container.gen_exit_cmd(self.runtime))
                capture = container.con_name
                
            net_cmd = [
                self.runtime,
                'network',
                'rm',
                network
            ]
            cmds['exit'].append(net_cmd)
            
            cmds['wait'] = [
                self.runtime,
                'wait',
                capture
            ]
            
            cmds['capture'] = [
                self.runtime,
                'logs',
                capture
            ]
            
        self.cmds = cmds                
    
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
        
        for statement in self.statements:
            # Write out each container config
            for container in statement['containers']:
                filename = f"{wd}/{container.con_name}.json"
                with open(filename, 'w+') as f:
                    f.write(json.dumps(container.to_dict(), indent=2))
                    
                # Make the config file 644 so that the non-root user
                # in the container can read it.
                os.chmod(
                    filename,
                    stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH
                )