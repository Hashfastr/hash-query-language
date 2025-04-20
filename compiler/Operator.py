from compiler.Expression import Expression
import json

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
        self.type = ''
        self.expressions = []
    
    def to_dict(self):
        return {
            'type': self.type,
            'expressions': [x.to_dict() for x in self.expressions]
        }
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return self.__str__()

# Index in a database to grab data from, extremely simple.
class Index(Operator):
    def __init__(self, expression:Expression):
        super().__init__()
        self.type = 'index'
        self.expressions.append(expression)

# Where operator
# Essentially just a field filter, can hold a number of expressions, even nested ones.
# Can also take a number of parameters, although I'm not sure what they are
# but they can exist.
# https://learn.microsoft.com/en-us/kusto/query/where-operator
class Where(Operator):
    def __init__(self):
        super().__init__()
        self.type = 'where'
        self.parameters = []
    
    def to_dict(self):
        return {
            'type': self.type,
            'parameters': self.parameters,
            'expressions': [x.to_dict() for x in self.expressions]
        }

# Project my beloved
# Defines a number of fields to be kept in the output following this operator.
#
# {"test1":"val","test2":"val","test3":"val","test4":"val","test5":"val"}
# | project test1, test3, test5
# 
# Would result in
#
# {"test1":"val","test3":"val","test5":"val"}
# https://learn.microsoft.com/en-us/kusto/query/project-operator
class Project(Operator):
    def __init__(self):
        super().__init__()
        self.type = 'project'