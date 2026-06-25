from typing import TYPE_CHECKING
from Hql.Expressions.Literals import Integer
from Hql.Operators.Operator import Operator
from Hql.Data import Data
from Hql.Expressions import Expression
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context
import polars as pl

if TYPE_CHECKING:
    from Hql.Expressions.Aggregation import ByExpression

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
    def __init__(self, expr:Integer, by:'ByExpression'):
        Operator.__init__(self)
        self._expr:Integer = expr
        self.by = by
        
    def to_dict(self):
        assert self.expr
        return {
            'type': self.type,
            'quota': self.expr.to_dict(),
            'by': self.by.to_dict()
        }

    def deparse(self) -> str:
        out = 'top '
        assert self.expr
        out += self.expr.deparse()
        out += ' by '
        out += self.by.deparse()

        return out
        
    def eval(self, ctx:'Context'):
        assert self.expr
        limit = self.expr.value
        assert isinstance(limit, int)
        
        ctx = self.by.eval(ctx)
        [x.truncate(limit) for x in ctx.data]
        return ctx
