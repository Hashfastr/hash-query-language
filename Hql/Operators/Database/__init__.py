# import importlib,pkgutil
from .Database import Database
from .Static import Static
from .CSV import CSV
from .JSON import JSON
from .Opensearch import Opensearch
from .Elasticsearch import Elasticsearch

# for loader, name, is_pkg in pkgutil.iter_modules(__path__):
#     importlib.import_module(f"{__name__}.{name}")
