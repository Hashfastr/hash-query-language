import os
import subprocess
import logging

class Compose():
    def __init__(self, target:str, compose_override:str=''):
        self.composes = [
            'podman-compose',
            'docker-compose',
        ]
        
        self.override = compose_override
        self.exec = self.get_exec()
        self.target = target
        
        self.logger = logging.getLogger()
        
    def get_exec(self):
        if self.override:
            return self.override
        
        path = os.environ.get('PATH', '')
        
        if path == '':
            raise Exception("Empty shell $PATH detected!")
        
        for directory in path.split(':'):
            for compose in self.composes:
                full = directory + os.sep + compose
                if os.path.isfile(full):
                    return full
                
        raise Exception('No compose available in the system!')

    # runs a compose file in a given target dir    
    def up(self) -> subprocess.CompletedProcess:
        self.logger.debug(f"Running compose {self.target}")
        
        out = subprocess.run(
            [self.exec, 'up'],
            check=True,
            capture_output=True,
            cwd=self.target
        )
        
        self.logger.debug(f'Finished running')
        
        return out

    # Brings down a compose file in a given dir
    # No timeout, fast, kill it
    def down(self):
        self.logger.debug(f"Composing down {self.target}")
        
        subprocess.run(
            [self.exec, 'down', '-t', '0'],
            cwd=self.target
        )
        
        self.logger.debug(f"Containers composed down")