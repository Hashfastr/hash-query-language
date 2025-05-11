from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op

# Count simply returns the number of rows given by a record set.
#
# https://learn.microsoft.com/en-us/kusto/query/count-operator
@register_op('Count')
class Count(Operator):
    def __init__(self, expr:Expression=None):
        super().__init__()
        self.expr = expr
        
    def eval(self, data:Results):
        count = [{'Count': len(data)}]

        return pl.from_dicts(count)