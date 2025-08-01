import importlib, pkgutil
from .Function import Function

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")
