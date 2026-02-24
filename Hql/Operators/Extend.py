from typing import TYPE_CHECKING, Union
from Hql.Expressions import Expression, NamedExpression, NamedReference, Path, Reference
from Hql.Operators import Operator
from Hql.Context import Context
import logging
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Data import Data

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        Operator.__init__(self)
        self.exprs = exprs

    def deparse(self) -> str:
        return 'extend ' + ', '.join(x.deparse() for x in self.exprs)

    def eval(self, ctx:'Context'):
        ctx = ctx.copy()
        orig:'Data' = ctx.data
        data:list['Data'] = []

        for i in self.exprs:
            if isinstance(i, NamedExpression):
                datum = i.eval(ctx).data
                data.append(datum)

                for j in i.paths:
                    orig = orig.drop(j)
        
        # orig is now a subset of the original with all assignments replaced
        data.append(orig)
        ctx.data = Data.merge(data)

        return ctx
