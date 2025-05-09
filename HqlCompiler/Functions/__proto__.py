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
        
    def eval(self, data:pl.DataFrame=None):
        if len(self.chain) != 0:
            return self.eval_chain(data)
        
        return pl.DataFrame({"results": []})
        
    def eval_chain(self, data:pl.DataFrame=None, next:list=None):
        if not next:
            next = self.chain
        
        out = self.eval()
        
        if len(next) == 1:
            return next[0].exec_func(out)
        else:
            return cur.exec_func_chain(next)