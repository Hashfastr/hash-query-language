index_registry = {}

def regsiter_index(name):
    def decorator(cls):
        index_registry[name] = cls
        return cls
    return decorator
    
func_registry = {}

def register_func(name):
    def decorator(cls):
        func_registry[name] = cls
        return cls
    return decorator