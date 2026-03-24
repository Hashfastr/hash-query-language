import importlib, pkgutil

import json
from typing import TYPE_CHECKING, Optional

from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Context import Context

class Function():
    def __init__(self, args:list, min:int, max:int, conf:Optional[dict]=None):
        self.name = self.__class__.__name__
        self.type = 'Function'
        self.args = args
        self.min = min
        # Can disable by passing -1
        self.can_preprocess = False
        self.max = max
        self.static = False
        self.conf = conf if conf else dict()
        
        if len(args) < min:
            raise hqle.ArgumentException(f'Function {self.name} got {len(args)} args, expected at least {self.min}')
        if max != -1 and len(args) > max:
            raise hqle.ArgumentException(f'Function {self.name} got {len(args)} args, expected at most {self.max}')
    
    def __hash__(self):
        return hash((self.name))

    def deparse(self):
        args = ', '.join([x.deparse() for x in self.args])
        return f'{self.name}({args})'
        
    def to_dict(self):
        return {
            'type': 'function',
            'name': self.name,
            'args': self.args
        }
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()

    def preprocess(self, ctx:'Context', receiver=None) -> object:
        raise hqle.FunctionException(f'Attempting to preprocess non-preprocess function {self.name}')
        
    def eval(self, ctx:'Context', receiver=None) -> object:
        return NotImplemented

class DotCompositeFunction():
    def __init__(self, funcs:list[Function]):
        self.type = self.__class__.__name__
        self.funcs = funcs

    def __new__(cls, funcs:list[Function]):
        if len(funcs) == 1:
            return funcs[0]
        return super().__new__(cls)

    def __bool__(self):
        return bool(self.funcs)
    
    def to_dict(self):
        return {
            'type': self.type,
            'funcs': [x.to_dict() for x in self.funcs]
        }

    def deparse(self) -> str:
        funcs = []
        for i in self.funcs:
            funcs.append(i.deparse())
        return '.'.join(funcs)

    def preprocess(self, ctx:'Context') -> object:
        ctx = ctx.copy()
            
        rec = None
        for i in self.funcs:
            try:
                rec = i.preprocess(ctx, receiver=rec)
            except hqle.FunctionException as e:
                # catching for handling for if a function can't preprocess within the chain
                e.add_note(f'Occured in {self.deparse()}')
                raise

        return rec

    def eval(self, ctx:'Context') -> object:
        ctx = ctx.copy()

        rec = None
        for func in self.funcs:
            rec = func.eval(ctx, receiver=rec)
        
        return rec

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")
