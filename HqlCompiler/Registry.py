from HqlCompiler.Exceptions import *

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