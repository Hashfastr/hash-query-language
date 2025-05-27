from HqlCompiler.Exceptions import *
import copy

database_registry = {}

def register_database(name:str):
    def decorator(cls):
        database_registry[name] = cls
        return cls
    return decorator

def get_database(name:str):
    if name in database_registry:
        return database_registry[name]
    else:
        raise CompilerException(f"Unknown database type {name}")
    
func_registry = {}

def register_func(name):
    def decorator(cls):
        func_registry[name] = cls
        return cls
    return decorator

def get_func(name):
    if name in func_registry:
        return func_registry[name]
    else:
        raise CompilerException(f"Unknown function {name} referenced")
    
op_registry = {}

def register_op(name):
    def decorator(cls):
        op_registry[name] = cls
        return cls
    return decorator

def get_op(name):
    if name in op_registry:
        return op_registry[name]
    else:
        raise CompilerException(f"Unknown operator {name} referenced")

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
        raise CompilerException(f"Unknown type {name} referenced")

# Essentially a scoped context
class Context():
    def __init__(self, data:"Data.Data") -> None:
        self.dbs = copy.copy(database_registry)
        self.ops = copy.copy(op_registry)
        self.funcs = copy.copy(func_registry)
        self.data = data

    def get_db(self, name:str):
        if name in self.dbs:
            return self.dbs[name]
        else:
            raise CompilerException(f"Unknown database {name} referenced")

    def get_db_types(self):
        return list(self.dbs.keys())

    def get_func(self, name:str):
        if name in self.funcs:
            return self.funcs[name]
        else:
            raise CompilerException(f"Unknown function {name} referenced")

    def get_op(self, name:str):
        if name in self.ops:
            return self.ops[name]
        else:
            raise CompilerException(f"Unknown operator {name} referenced")