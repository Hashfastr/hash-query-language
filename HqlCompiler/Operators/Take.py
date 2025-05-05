from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *

# Take, limits the number of results given an integer
# Ensures that only integers are given, if not then errors
# The implementation algorithm is just grab the first n rows.
#
# https://learn.microsoft.com/en-us/kusto/query/take-operator?view=microsoft-fabric
class Take(Operator):
    def __init__(self, expr:Expression):
        super().__init__()
        self.expr = expr
        
    def execute(self, data:Results):
        if self.expr.type != 'Integer':
            raise CompilerException(f'Invalid type {self.expr.type} given to take operator')
        
        limit = self.expr.value
        orig_type = type(limit)
        
        if not isinstance(limit, int):
            try:
                limit = int(limit)
            except Exception as e:
                raise Exception(f"Invalid argument given to take, expected int got {orig_type}")
        
        return data[:limit]