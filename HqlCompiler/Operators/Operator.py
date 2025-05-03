import json
from ..Results import Results
import logging

# The proto for an operator.
# An operator is simply a operation denoted by a pipe (|).
# 
# so-beats-2022.10.*
# | where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
# | where event.code == 1
# | where host.name == "asarea.vxnwua.net"
# | project ['@timestamp'], event.code, host.name
# 
# For example, here we have four operators, a index, three wheres, and a project.
# Each operator is a subclass of the base Operator, they are slightly different by the same idea.
# Each operator has expressions and a type.
# The type is typically just the name of the operator such as where.
# In the case of index, it is nameless, so I used an unused name.
# Additionally, the top operator doesn't have to be an index, could be the saved
# value of another statement.
class Operator():
    def __init__(self):
        self.type = self.__class__.__name__
        self.expressions = []
        self.compatible = []
        self.non_conseq = []
    
    def to_dict(self):
        return {
            'type': self.type,
            'expressions': [x.to_dict() for x in self.expressions]
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return self.__str__()

    # default execution passthrough unless implemented
    def execute(self, data:Results):
        return data

    def can_integrate(self, type:str):
        return type in self.compatible
    
    def non_consequential(self, type:str):
        return type in self.non_conseq