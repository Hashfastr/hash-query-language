__all__ = [
    "Operators",
    "Compiler",
]

import json

# THE compiler which turns the assembly into containers and container configs.
# Builds networks and containers using GUIDs and linking them on who to talk to.
# At the end writes out the compose file, along with the configs for each container.
# In the compose each container is configured to reference their own configs.
class Compiler():
    def __init__(self, conf_file:str, top:dict):
        self.top = top
        self.conf_file = conf_file
        self.statements = []
        
        # load conf file
        with open(self.conf_file, mode='r') as f:
            self.conf = json.loads(f.read())
        
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
        
    def to_dict(self):
        return self.statements
    
    # Not used yet, will probably make sense eventually
    def is_blocking(self, type:str) -> bool:
        return self.ruleset['operations'][type]['blocking']
