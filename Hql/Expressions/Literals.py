from .__proto__ import Expression
from Hql.Context import Context
from Hql.Types.Hql import HqlTypes as hqlt

import polars as pl

class Literal(Expression):
    def __init__(self) -> None:
        Expression.__init__(self)
        self.literal = True

class TypeExpression(Literal):
    def __init__(self, type:str):
        Literal.__init__(self)
        self.type = type
        
    def eval(self, ctx:Context, **kwargs):
        return hqlt.from_name(self.type)

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Literal):
    def __init__(self, value:str):
        Literal.__init__(self)
        self.value = value.strip('"').strip("'")
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

# Integer
# An integer
# Z
# unreal, not real
class Integer(Literal):
    def __init__(self, value:str):
        Literal.__init__(self)
        self.value = int(value)
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class IP4(Literal):
    def __init__(self, value:int):
        Literal.__init__(self)
        self.value = value
        
    def to_dict(self):
        s = pl.Series([self.value])
        human = hqlt.ip4().human(s)
        
        return {
            'type': self.type,
            'value': human
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class Float(Literal):
    def __init__(self, value:str):
        Literal.__init__(self)
        self.value = float(value)
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class Bool(Literal):
    def __init__(self, value:str):
        Literal.__init__(self)
        self.value = value.lower() == 'true'
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value
