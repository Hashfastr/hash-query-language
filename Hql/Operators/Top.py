from typing import TYPE_CHECKING
from Hql.Operators import Operator
from Hql.Data import Data
from Hql.Expressions import Expression
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context
import polars as pl

if TYPE_CHECKING:
    from Hql.Expressions import ByExpression

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
# @register_op('Top')
class Top(Operator):
    def __init__(self, expr:Expression, by:'ByExpression'):
        Operator.__init__(self)
        self.expr = expr
        self.by = by
        
    def to_dict(self):
        return {
            'type': self.type,
            'quota': self.expr.to_dict(),
            'by': self.by.to_dict()
        }

    def decompile(self, ctx: 'Context') -> str:
        out = 'top '
        out += self.expr.decompile(ctx)
        out += ' by '
        out += self.by.decompile(ctx)

        return out
        
    def eval(self, ctx:'Context', **kwargs):
        name = self.by.name.eval(ctx, as_str=True, as_list=True)
        if isinstance(name, str):
            name = [name]
            
        quota = self.expr.eval(ctx)
        order = self.by.order
        nulls = self.by.nulls
        
        return pl.DataFrame({name: series})
