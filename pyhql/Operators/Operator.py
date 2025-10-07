import json
from typing import TYPE_CHECKING, Union
from Hql.Context import Context

if TYPE_CHECKING:
    from Hql.Data import Data

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
# @register_op('Operator')
class Operator():
    def __init__(self):
        import random
        
        self.type:str = self.__class__.__name__
        self.expr = None
        self.exprs = []
        self.compatible = []
        self.non_conseq = []
        self.methods = []
        self.variables:dict = {}
        self.tabular = False
        self.id = '%08x' % random.getrandbits(32)
    
    def to_dict(self):
        if self.expr:
            return {
                'id': self.id,
                'type': self.type,
                'expression': self.expr.to_dict()
            }
        if self.exprs:
            return {
                'id': self.id,
                'type': self.type,
                'expressions': [x.to_dict() for x in self.exprs]
            }
        else:
            return {
                'id': self.id,
                'type': self.type,
                'expression': None
            }

    def decompile(self, ctx: 'Context') -> Union[str, list[str]]:
        return ''
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return self.__str__()

    # default execution passthrough unless implemented
    def eval(self, ctx:'Context', **kwargs) -> 'Data':
        return ctx.data
    
    def non_consequential(self, type:str):
        return type in self.non_conseq
    
    def has_method(self, name:str):
        return name in self.methods

    def get_variable(self, name:str):
        return self.variables[name]

    def can_integrate(self, type:str):
        return type in self.compatible

    '''
    Where you take in operators you can merge together

    Idea is that you return what you couldn't integrate
    - Full integration means you return None
    - Impossible integration means you return the original op
    - Partial mean you return an op with what you couldn't integrate

    A partial integration must still result in a semantically congruent operator
    when combined with the integrating operator.

    So for example, elasticsearch has no functions, so the database here would do a partial
    integration leaving behind a semantically congruent operator

    Elasticsearch
    | where foo == 10 and bar == toint('11')

    Elasticsearch (has foo == 10 integrated)
    | where bar == toint('11')

    Since an 'and' in this case can be represented by a pipe, the reduced where operator is returned.
    If it were a 'or' on the other hand then there would be no ability to integrate
    Alternatively if the expression were:

    | where foo == 10 and (bar == toint('11') or zoo == 'wee')

    Then again you can only integrate foo, although if the or were an and you could say

    Elasticsearch
    | where foo == 10 and (bar == toint('11') and zoo == 'wee')

    Elasticsearch (has foo == 10 and zoo == 'wee' integrated)
    | where bar == toint('11')
    '''
    def integrate(self, op:'Operator'):
        if self.can_integrate(op.type):
            # You would then integrate a consuming integration here
            return None

        else:
            # otherwise reject the operator back to the compiler
            return op
