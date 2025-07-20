from ..Data import Data
from ..Expressions import Expression
from ..Exceptions import *
from ..PolarsTools import pltools
from ..Functions import Function
from ..Operators import Operator
import polars as pl
from ..Context import register_op, Context

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
@register_op('Extend')
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
            
    def eval(self, ctx:Context, **kwargs):
        for i in self.exprs:
            i.eval(ctx)
        
        return ctx.data