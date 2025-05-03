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
        self.type = self.__class__.__name__
        self.expressions = []
    
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
        self.eqtype = type
    
    def to_dict(self):
        try:
            {
                'type': self.type,
                'eqtype': self.eqtype,
                'lh': self.expressions[0].to_dict(),
                'rh': self.expressions[1].to_dict()
            }
        except:
            for expression in self.expressions:
                print(expression)
            raise Exception("Failure to dict an equality")

# List equality
# Essenitally a filter stating that a field should have any value in a tuple.
# 
# | where event.code in (10, 11, 13, 3)
#
# is semantically identical to
#
# | where event.code == 10 or event.code == 11 or event.code == 13 or event.code == 3
#
# But is much easier to write and read
class ListEquality(Expression):
    def __init__(self):
        super().__init__()
    
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'lh': self.expressions[0].to_dict(),
                'rh': [x.to_dict() for x in self.expressions[1:]]
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
    def __init__(self, name:str, escaped:bool=False, scope:str=""):
        super().__init__()
        self.name = name
        self.escaped = escaped
        self.scope = scope
        
    def to_dict(self):
        return {
            'name': self.name,
            'scope': self.scope,
            'escaped': self.escaped
        }

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = value.strip('"').strip("'")
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
class EscapedName(StringLiteral):
    def __init__(self, value:str):
        super().__init__(value)
        self.escaped = True
        
    def to_dict(self):
        dict = super().to_dict()
        dict['escaped'] = self.escaped
        return dict

class Keyword(Expression):
    def __init__(self, name):
        super().__init__()
        self.value = name
        
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name
        }

# Integer
# An integer
# Z
# unreal, not real
class Integer(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = int(value)
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }

class Function(Expression):
    def __init__(self, name:str, args:list=[]):
        super().__init__()
        self.name = name
        self.args = args
    
    def __str__(self):
        return super().__str__()
    
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name,
            'args': [x.to_dict() for x in self.args]
        }

class PathExpression(Expression):
    def __init__(self, path:list=[]):
        super().__init__()
        self.path = path
                
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'path': [x.to_dict() for x in self.path]
            }
        except Exception as e:
            logging.debug(self.path)
            logging.debug(e)
        
class PathReference(Expression):
    def __init__(self, ref):
        super().__init__()
        self.ref = ref

    def to_dict(self):
        return {
            'type': self.type,
            'ref': self.ref
        }

class DotCompositeFunctionCall(Expression):
    def __init__(self):
        super().__init__()
        
    def to_dict(self):
        return {
            'type': self.type,
            'funcs': [x.to_dict() for x in self.expressions]
        }
    
class BinaryLogic(Expression):
    def __init__(self, type=""):
        super().__init__()
        self.bitype = type
        
    def to_dict(self):
        try:
            out = {
                'type': self.type,
                'bitype': self.bitype,
                'expressions': []
            }
            
            for i in self.expressions:
                if issubclass(type(i), Expression):
                    out['expressions'].append(i.to_dict())
                else:
                    out['expressions'].append(i)
                    
            return out
        except IndexError as e:
            logging.critical(self.bitype)
            logging.critical(f'{len(self.expressions)} expressions found')
            logging.critical(e)
        except Exception as e:
            logging.debug(f'{self.type} {self.bitype}')
            for i in self.expressions:
                logging.debug(i)
            logging.critical(e)