from HqlCompiler.Operators import Operator
from HqlCompiler.Data import Data
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context
import polars as pl
import numpy as np

'''
Give the top, or bottom, x values for a given field in a dataframe

range x from 1 to 100 step 2
| top 5 by x desc

99
97
95
93
91

Preserves the other fields as well

https://learn.microsoft.com/en-us/kusto/query/top-operator
'''
@register_op('Top')
class Top(Operator):
    def __init__(self, quota:Expression, by:Expression):
        super().__init__()
        self.quota = quota
        self.by = by
        
    def to_dict(self):
        return {
            'type': self.type,
            'quota': self.quota.to_dict(),
            'by': self.order.to_dict()
        }
        
    def eval(self, ctx:Context, **kwargs):
        name = self.by.name.eval(ctx, as_str=True, as_list=True)
        if isinstance(name, str):
            name = [name]
            
        quota = self.quota.eval(ctx)
        order = self.by.order
        nulls = self.by.nulls
        
        
         
        return pl.DataFrame({name: series})