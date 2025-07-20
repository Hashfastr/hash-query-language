import importlib, pkgutil
from ..Exceptions import *
from .__proto__ import Function

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")
