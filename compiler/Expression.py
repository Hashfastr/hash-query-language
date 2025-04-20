import logging
import json

# An expression proto
# An expression is the data to be handled in a given operator
# 
# | where a == 'b'
# 
# Here the 'where' operator has a single expression, Equality.
# Equality comprises of two expressions and it's type.
# Here the two expressions are a ScopedNameReference and a StringLiteral
# This allows for nested expressions that are resolved and built at the end of
# compilation.
class Expression():
    def __init__(self):
        pass
    
    def to_dict(self):
        return {}
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()

# Expression expressing anything with ==, >, <, <=, >=, !=, etc
# has a left and right hand expression along with it's type.
class Equality(Expression):
    def __init__(self, type:str=""):
        super().__init__()
        self.type = type
        self.expressions = []
    
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'lh': self.expressions[0].to_dict(),
                'rh': self.expressions[1].to_dict()
            }
        except:
            for expression in self.expressions:
                print(expression)
            raise Exception("Failure to dict an equality")

# Data range functionality
# Left hand side is the expression to evaluate in being between two values.
# The right hand has a start and end expression showing the range of the values.
#
# | where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
# 
# Here lh is the '@timestamp' escaped string literal, and the right hand has
# the start and end values for the time range.
class BetweenEquality(Expression):
    def __init__(self):
        super().__init__()
        self.expressions = []
        self.type = 'between'
    
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'lh': self.expressions[0].to_dict(),
                'rh': {
                    'start': self.expressions[1].to_dict(),
                    'end': self.expressions[2].to_dict()
                }
            }
        except:
            for expression in self.expressions:
                print(expression)
            raise Exception("Failure to dict a between")

# A scoped name reference.
# Simply a name for now, scopes are not implemented yet.
class ScopedNameReference(Expression):
    def __init__(self, name:str, scope:str=""):
        super().__init__()
        self.name = name
        self.scope = scope
        
    def to_dict(self):
        return {
            'name': self.name,
            'scope': self.scope
        }

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = value.strip('"').strip("'")
        self.type = 'stringliteral'
        
    def get_name(self):
        return self.value
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }

# Integer
# An integer
# Z
# unreal, not real
class Integer(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = int(value)
        self.type = 'integer'
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }