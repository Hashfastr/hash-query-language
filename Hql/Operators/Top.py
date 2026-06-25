from typing import TYPE_CHECKING, Optional
from Hql.Expressions.Literals import Integer
from Hql.Operators.Operator import Operator
from Hql.Context import Context
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Expressions import Expression
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
class Top(Operator):
    def __init__(self, expr:Integer, by:'ByExpression'):
        Operator.__init__(self)
        self._expr:Integer = expr
        self.by = by

    @property
    def expr(self) -> Integer:
        expr = self._expr
        assert expr
        return expr

    @expr.setter
    def expr(self, value:Optional['Expression']) -> None:
        if value is None or not isinstance(value, Integer):
            raise hqle.CompilerException('Setting Top expression to non-Integer')
        self._expr = value

    def to_dict(self):
        return {
            'type': self.type,
            'quota': self.expr.to_dict(),
            'by': self.by.to_dict()
        }

    def deparse(self) -> str:
        return f'top {self.expr.deparse()} by {self.by.deparse()}'

    def eval(self, ctx:'Context'):
        limit = self.expr.value

        ctx = self.by.eval(ctx)
        for table in ctx.data:
            table.truncate(limit)
        return ctx
