from .Operator import Operator
from ..Expression import Expression
from HqlCompiler.Exceptions import *

# Where operator
# Essentially just a field filter, can hold a number of expressions, even nested ones.
# Can also take a number of parameters, although I'm not sure what they are
# but they can exist.
# https://learn.microsoft.com/en-us/kusto/query/where-operator
class Where(Operator):
    def __init__(self, expr:Expression, params:list=None):
        super().__init__()
        if expr == None:
            raise ParseException('Where instanciated with None type predicate')
        
        self.parameters = params if params else []
        self.expr = expr
            
    def to_dict(self):        
        return {
            'type': self.type,
            'parameters': [x.to_dict() for x in self.parameters],
            'expression': self.expr.to_dict()
        }