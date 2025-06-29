import json
from HqlCompiler.Context import Context

# An expression is any grouping of other expressions
# Typically children of an operation, an expression can also contain operators itself
# Such as a subsearch, which is an expression, and contains operators
# All other expressions are children of this one
class Expression():
    def __init__(self)-> None:
        self.type = self.__class__.__name__
        self.escaped = False
        self.literal = False
    
    def to_dict(self):
        return {
            'type': self.type
        }
    
    def eval(self, ctx:Context, **kwargs):
        return None
    
    def is_escaped(self)-> bool:
        return self.escaped
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()

    def features(self):
        return []
