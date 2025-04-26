from ..Operator import Operator
from HqlCompiler.Expression import Expression
from HqlCompiler.Registry import *
import importlib,pkgutil

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")

def get_indexer(conf:dict):
    if conf['TYPE'] in index_registry:
        return index_registry[conf['TYPE']]
    
    raise Exception(f"Indexer of type {conf['TYPE']} not implemented")

class Index(Operator):
    def __init__(self, expression:Expression):
        super().__init__()
        self.type = 'index'
        self.expressions = [expression]