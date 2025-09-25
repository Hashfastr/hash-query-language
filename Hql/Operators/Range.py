from Hql.Operators import Operator
from Hql.Data import Data, Table, Schema
from Hql.PolarsTools import pltools
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op
import polars as pl
import numpy as np
from Hql.Operators import Operator

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Context import Context

'''
Generates a single-column table of values

range x from 1 to 5 step 1

https://learn.microsoft.com/en-us/kusto/query/range-operator
'''
# @register_op('Range')
class Range(Operator):
    def __init__(self, name:'Expression', start:'Expression', end:'Expression', step:'Expression'):
        Operator.__init__(self)
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

    def decompile(self, ctx: 'Context') -> str:
        name = self.name.decompile(ctx)
        start = self.start.decompile(ctx)
        end = self.end.decompile(ctx)
        step = self.step.decompile(ctx)

        return f'range {name} from {start} to {end} step {step}'
        
    def eval(self, ctx:'Context', **kwargs):
        name = self.name.eval(ctx, as_list=True)
        start = self.start.eval(ctx)
        end = self.end.eval(ctx)
        step = self.step.eval(ctx)
        
        if type(start) not in (int, float):
            raise hqle.CompilerException(f'Range given invalid start value type {type(start)}')
        
        if type(end) not in (int, float):
            raise hqle.CompilerException(f'Range given invalid end value type {type(end)}')
        
        if type(step) not in (int, float):
            raise hqle.CompilerException(f'Range given invalid step value type {type(step)}')
                
        series = pl.Series(np.arange(start, end, step))
        # This handles the inclusive case as arange does not
        if (end - start) % step == 0:
            series = pl.concat([series, pl.Series([end])])
        
        df = pltools.build_element(name, series)
        table = Table(df=df, name='range')
         
        return Data(tables=[table])
