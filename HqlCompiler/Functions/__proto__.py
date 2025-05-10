import json
from HqlCompiler.Exceptions import *
import polars as pl

class Function():
    def __init__(self, args:list, min:int, max:int):
        self.name = self.__class__.__name__
        self.args = args
        self.min = min
        self.max = max
        self.chain = []
        
        if len(args) < min:
            raise ArgumentException(f'Function {self.name} got {len(args)} args, expected at least {self.min}')
        if len(args) > max:
            raise ArgumentException(f'Function {self.name} got {len(args)} args, expected at most {self.max}')
        
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
        
    def eval(self, *data):
        if len(self.chain) != 0:
            return self.eval_chain(data)
        
        return pl.DataFrame()
        
    def eval_chain(self, *data):
        out = self.eval(data)
                
        for i in self.chain:
            if out.has_method(i.name):
                out = i.eval(out)
            else:
                raise CompilerException(f'{out.name} has no method {i.name}')
        
        return out