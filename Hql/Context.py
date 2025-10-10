from Hql.Exceptions import HqlExceptions as hqle
from typing import TYPE_CHECKING, Union
from Hql.Config import Config

if TYPE_CHECKING:
    from Hql.Data import Data

database_registry = {}

def register_database(name:str):
    def decorator(cls):
        from Hql.Operators.Database import Database

        if not issubclass(cls, Database):
            raise hqle.CompilerException(f'Attempting to register non-database class {name} as a database')

        database_registry[name] = cls
        return cls
    return decorator

def get_database(name:str):
    if name in database_registry:
        return database_registry[name]
    else:
        raise hqle.CompilerException(f"Unknown database type {name}")
    
func_registry = {}

def register_func(name):
    def decorator(cls):
        from Hql.Functions import Function

        if not issubclass(cls, Function):
            raise hqle.CompilerException(f'Attempting to register non-function class {name} as a function')

        func_registry[name] = cls
        return cls

    return decorator

def get_func(name):
    if name in func_registry:
        return func_registry[name]
    else:
        raise hqle.CompilerException(f"Unknown function {name} referenced")
    
op_registry = {}

def register_op(name):
    def decorator(cls):
        from Hql.Operators import Operator
        from Hql.Operators.Database import Database

        if not issubclass(cls, Operator):
            raise hqle.CompilerException(f'Attempting to register non-operator class {name} as an operator')

        if issubclass(cls, Database):
            raise hqle.CompilerException(f'Attempting to register database class {name} as an operator, use @register_database')

        op_registry[name] = cls
        return cls
    return decorator

def get_op(name):
    if name in op_registry:
        return op_registry[name]
    else:
        raise hqle.CompilerException(f"Unknown operator {name} referenced")

'''
The naming scheme here is 

{db_type}_{typename}

So for Elasticsearch it would be

elasticsearch_scaled_float

Since the schema provided by elasticsearch calls that type scaled_float.
It can be helpful for you to provide a from_name function in your base type for looking up:

def from_name(name:str):
    return get_type(f'elasticsearch_{name}')
'''
type_registry = {}

def register_type(name):
    def decorator(cls):
        type_registry[name] = cls
        return cls
    return decorator

def get_type(name):
    if name in type_registry:
        return type_registry[name]
    else:
        raise hqle.CompilerException(f"Unknown type {name} referenced")

# Essentially a scoped context
class Context():
    def __init__(self, data:'Data', symbol_table:Union[dict, None]=None, macros:Union[dict, None]=None, config:Union[Config, None]=None) -> None:
        from copy import copy

        self.dbs = copy(database_registry)
        self.ops = copy(op_registry)
        self.funcs = copy(func_registry)
        self.data = data
        self.symbol_table = symbol_table if symbol_table else dict()
        self.macros = macros if macros else dict()
        self.config = config if config else Config()
        # self.root = None

    def __bool__(self):
        return self.data.__bool__()

    @staticmethod
    def merge(ctxs:list['Context'], merge_rows=True):
        from Hql.Data import Data
        
        if len(ctxs) == 1:
            return ctxs[0]

        data = Data.merge([x.data for x in ctxs], merge_rows=merge_rows)

        syms = dict()
        macros = dict()
        for i in ctxs:
            for j in i.symbol_table:
                syms[j] = i.symbol_table[j]
            
            for j in i.macros:
                macros[j] = i.macros[j]

        return Context(data, symbol_table=syms, macros=macros)

    def get_db(self, name:str):
        if name in self.dbs:
            return self.dbs[name]
        else:
            raise hqle.CompilerException(f"Unknown database {name} referenced")

    def get_db_types(self):
        return list(self.dbs.keys())

    def get_func(self, name:str):
        if name in self.funcs:
            return self.funcs[name]
        else:
            raise hqle.CompilerException(f"Unknown function {name} referenced")

    def get_op(self, name:str):
        if name in self.ops:
            return self.ops[name]
        else:
            raise hqle.CompilerException(f"Unknown operator {name} referenced")
