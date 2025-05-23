from .Operator import Operator
from HqlCompiler.Data import Data
from HqlCompiler.Expression import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op, Context

# Count simply returns the number of rows given by a record set.
#
# https://learn.microsoft.com/en-us/kusto/query/count-operator
@register_op('Count')
class Count(Operator):
    def __init__(self, expr:Expression=None):
        super().__init__()
        self.expr = expr
        
    def eval(self, ctx:Context, **kwargs):
        count = [{'Count': len(ctx.data)}]

        return pl.from_dicts(count)