from HqlCompiler.Data import Data
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.PolarsTools import pltools
from HqlCompiler.Functions import Function
from HqlCompiler.Operators import Operator
import polars as pl
from HqlCompiler.Context import register_op, Context

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