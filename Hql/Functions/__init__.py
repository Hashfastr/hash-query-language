import importlib, pkgutil

import json
import polars as pl
from typing import TYPE_CHECKING, Union

from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Data import Data, Series
    from Hql.Context import Context
    from Hql.Expressions import Expression as Expression
    from Hql.Compiler import InstructionSet
    from Hql.Hac import Source

class Function():
    def __init__(self, args:list, min:int, max:int):
        self.name = self.__class__.__name__
        self.args = args
        self.min = min
        # Can disable by passing -1
        self.max = max
        self.preprocess = False
        self.type = 'Function'
        self.static = False
        
        if len(args) < min:
            raise hqle.ArgumentException(f'Function {self.name} got {len(args)} args, expected at least {self.min}')
        if max != -1 and len(args) > max:
            raise hqle.ArgumentException(f'Function {self.name} got {len(args)} args, expected at most {self.max}')

    def decompile(self, ctx:'Context'):
        args = ', '.join([x.decompile(ctx) for x in self.args])
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
        
    def eval(self, ctx:'Context', **kwargs) -> Union['Data', 'Series', 'Expression', 'InstructionSet', 'Source', pl.Expr]:
        from Hql.Data import Data
        return Data()

for loader, name, is_pkg in pkgutil.iter_modules(__path__):
    importlib.import_module(f"{__name__}.{name}")
