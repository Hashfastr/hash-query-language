from .Operator import Operator
from ..Expression import Expression

# Where operator
# Essentially just a field filter, can hold a number of expressions, even nested ones.
# Can also take a number of parameters, although I'm not sure what they are
# but they can exist.
# https://learn.microsoft.com/en-us/kusto/query/where-operator
class Where(Operator):
    def __init__(self):
        super().__init__()
        self.parameters = []
    
    def to_dict(self):
        return {
            'type': self.type,
            'parameters': self.parameters,
            'expressions': [x.to_dict() for x in self.expressions]
        }