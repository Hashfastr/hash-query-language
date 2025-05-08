import logging
import json
from .Operators import Operator

# An expression is any grouping of other expressions
# Typically children of an operation, an expression can also contain operators itself
# Such as a subsearch, which is an expression, and contains operators
# All other expressions are children of this one
class Expression():
    def __init__(self):
        self.type = self.__class__.__name__
    
    def to_dict(self):
        return {}
    
    def get_name(self):
        return self.name
    
    def get_value(self):
        return self.value
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class PipeExpression(Expression):
    def __init__(self, prepipe:Expression=None, pipes:list[Operator]=None):
        super().__init__()
        self.prepipe = prepipe
        self.pipes = pipes if pipes else []
        
    def to_dict(self):
        return {
            'type': self.type,
            'prepipe': self.prepipe.to_dict(),
            'pipes': [x.to_dict() for x in self.pipes]
        }

# Expression expressing anything with ==, >, <, <=, >=, !=, etc
# has a left and right hand expression along with it's type.
class Equality(Expression):
    def __init__(self, type:str, lh:Expression, rh:Expression):
        super().__init__()
        self.eqtype = type
        self.lh = lh
        self.rh = rh
    
    def to_dict(self):
        return {
            'type': self.type,
            'eqtype': self.eqtype,
            'lh': self.lh.to_dict(),
            'rh': self.rh.to_dict()
        }

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
    def __init__(self, lh:Expression, rh:list[Expression]):
        super().__init__()
        self.lh = lh
        self.rh = rh
    
    def to_dict(self):
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }


# Data range functionality
# Left hand side is the expression to evaluate in being between two values.
# The right hand has a start and end expression showing the range of the values.
#
# | where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
# 
# Here lh is the '@timestamp' escaped string literal, and the right hand has
# the start and end values for the time range.
class BetweenEquality(Expression):
    def __init__(self, lh:Expression, start:Expression, end:Expression, negate:str="BETWEEN"):
        super().__init__()
        self.lh = lh
        self.start = start
        self.end = end
        self.negate = True if negate == "NOT_BETWEEN" else False
    
    def to_dict(self):
        return {
            'type': self.type,
            'negate': self.negate,
            'lh': self.lh.to_dict(),
            'rh': {
                'start': self.start.to_dict(),
                'end': self.end.to_dict()
            }
        }

# A named reference, can be scoped
# Scopes are not implemented yet.
class NamedReference(Expression):
    def __init__(self, name:Expression, scope:str=""):
        super().__init__()
        self.name = name
        self.scope = scope
        
    def get_name(self):
        if hasattr(self.name, 'name'):
            return self.name.name
        else:
            return self.name
        
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'scope': self.scope,
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
    def __init__(self, name:str):
        super().__init__(name)
        self.name = name
        self.escaped = True
        
    def to_dict(self):
        dict = super().to_dict()
        dict['escaped'] = self.escaped
        return dict

# An identifier is like a variable that is not unique across everything
# A keyword is unique across the compiler
# database('test').index('test')
# Here database is unique while index is not, multiple things can have a index child
class Identifier(Expression):
    def __init__(self, name:str, keyword:bool=False):
        super().__init__()
        self.name = name
        self.keyword = keyword
        
    def to_dict(self):
        return {
            'type': self.type,
            'keyword': self.keyword,
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

class Bool(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = value.lower() == 'true'
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }

class FuncExpr(Expression):
    def __init__(self, name:Expression, args:list=None):
        super().__init__()
        self.name = name
        self.args = args if args else []

    def get_name(self):
        return self.name.get_name()
    
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'args': [x.to_dict() for x in self.args]
        }
        
    def resolve(self):
        from HqlCompiler.Registry import get_func
        
        func = get_func(self.get_name())
        logging.debug(f'Resolved func {func}')

        return func(self.args)
        
class DotCompositeFunction(Expression):
    def __init__(self, funcs:list[FuncExpr]):
        super().__init__()
        self.funcs = funcs
    
    def to_dict(self):
        return {
            'type': self.type,
            'funcs': [x.to_dict() for x in self.funcs]
        } 

class Path(Expression):
    def __init__(self, path:list=None):
        super().__init__()
        self.path = path if path else []

    def get_name(self):
        return '.'.join([x.get_name() for x in self.path])
                
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'path': [x.to_dict() for x in self.path]
            }
        except Exception as e:
            logging.debug(self.path)
            logging.debug(e)
    
class BinaryLogic(Expression):
    def __init__(self, lh:Expression, rh:list[Expression], type:str):
        super().__init__()
        self.bitype = type.lower()
        self.lh = lh
        self.rh = rh
        
    def to_dict(self):
        return {
            'type': self.type,
            'bitype': self.bitype,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }

class OpParameter(Expression):
    def __init__(self, name:str, value:Expression):
        super().__init__()
        self.name = name
        self.value = value
        
    def to_dict(self):        
        return {
            'name': self.name,
            'value': self.value.to_dict()
        }