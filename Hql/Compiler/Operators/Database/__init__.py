from HqlCompiler.Context import *
from HqlCompiler.Exceptions import *
import importlib,pkgutil
from .__proto__ import Database

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")