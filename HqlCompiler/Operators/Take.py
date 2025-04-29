from .Operator import Operator
from ..Expression import Expression
import polars as pl
from ..PolarsTools import PolarsTools as pltools
from ..Results import Results

# Take, limits the number of results given an integer
# Ensures that only integers are given, if not then errors
# The implementation algorithm is just grab the first n rows.
#
# https://learn.microsoft.com/en-us/kusto/query/take-operator?view=microsoft-fabric
class Take(Operator):
    def __init__(self):
        super().__init__()
        
    def execute(self, data:Results):
        limit = self.expressions[0].value
        orig_type = type(limit)
        
        if not isinstance(limit, int):
            try:
                limit = int(limit)
            except Exception as e:
                raise Exception(f"Invalid argument given to take, expected int got {orig_type}")
        
        return data[:limit]