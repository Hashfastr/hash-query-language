from .Operator import Operator
from HqlCompiler.Data import Data
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context
import polars as pl
import numpy as np
from HqlCompiler.Operators import Operator

'''
Generates a single-column table of values

range x from 1 to 5 step 1

https://learn.microsoft.com/en-us/kusto/query/range-operator
'''
@register_op('Range')
class Range(Operator):
    def __init__(self, name:Expression, start:Expression, end:Expression, step:Expression):
        super().__init__()
        self.name = name
        self.start = start
        self.end = end
        self.step = step
        self.tabular = True
        
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'start': self.start.to_dict(),
            'end': self.end.to_dict(),
            'step': self.step.to_dict(),
        }
        
    def eval(self, ctx:Context, **kwargs):
        name = self.name.eval(ctx, as_str=True)
        start = self.start.eval(ctx)
        end = self.end.eval(ctx)
        step = self.step.eval(ctx)
        
        if type(start) not in (int, float):
            raise CompilerException(f'Range given invalid start value type {type(start)}')
        
        if type(end) not in (int, float):
            raise CompilerException(f'Range given invalid end value type {type(end)}')
        
        if type(step) not in (int, float):
            raise CompilerException(f'Range given invalid step value type {type(step)}')
        
        series = pl.Series(name, np.arange(start, end, step))
        # This handles the inclusive case as arange does not
        if (end - start) % step == 0:
            pl.concat([series, pl.Series([end])])
         
        return pl.DataFrame({name: series})