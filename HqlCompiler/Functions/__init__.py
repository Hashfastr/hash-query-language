import json
from ..Registry import func_registry
import importlib, pkgutil

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")

def get_func(name:str):
    if name in func_registry:
        return func_registry[name]
    
    raise Exception(f"Function referenced but not found: {name}")

class Function():
    def __init__(self, args:list):
        self.args = args
        self.name = ''
        
    def to_dict(self):
        return {
            'type': 'function',
            'name': self.name,
            'args': self.args
        }
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def eval(self):
        return {
            "results": []
        }