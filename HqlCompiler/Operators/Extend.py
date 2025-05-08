from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        
    def execute(self, data:Results):

        
        return data