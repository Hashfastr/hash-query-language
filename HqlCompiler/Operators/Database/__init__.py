from HqlCompiler.Operators.Operator import Operator
from HqlCompiler.Registry import *
from HqlCompiler.Exceptions import *
import importlib,pkgutil

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")

class Database(Operator):
    def __init__(self):
        super().__init__()
        self.dbtype = self.type
        self.type = "Database"