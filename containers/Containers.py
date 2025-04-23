import os
import subprocess

# priority list of container runtimes to use
composes = [
    'podman-compose',
    'docker-compose',
]

# find the best compose around
def get_compose():
    path = os.environ.get('PATH', '')
    
    if path == '':
        raise Exception("Empty shell $PATH detected!")
    
    for directory in path.split(':'):
        for compose in composes:
            full = directory + os.sep + compose
            if os.path.isfile(full):
                return full
            
    return ''

def compose_up(target:str, compose_override:str=''):
    if compose_override:
        exec = compose_override
    else:
        exec = get_compose()
        
    if exec == '':
        raise Exception('No compose available in the system!')
        
    out = subprocess.run(
        [exec, 'up'],
        check=True,
        capture_output=True,
        cwd=target
    )
    
    subprocess.run(
        [exec, 'down'],
        cwd=target
    )
    
    return out