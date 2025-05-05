import json
from ..Registry import get_func
import importlib, pkgutil
from HqlCompiler.Exceptions import *
from .__proto__ import Function

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")