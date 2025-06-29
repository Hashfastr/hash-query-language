from .__proto__ import Expression
from HqlCompiler.Context import Context
from HqlCompiler.Types.Hql import HqlTypes as hqlt

import polars as pl

class TypeExpression(Expression):
    def __init__(self, type:str):
        Expression.__init__(self)
        self.type = type
        
    def eval(self):
        return hqlt.from_name(self.type)

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Expression):
    def __init__(self, value:str):
        Expression.__init__(self)
        self.literal = True
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
class Integer(Expression):
    def __init__(self, value:str):
        Expression.__init__(self)
        self.literal = True
        self.value = int(value)
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class IP4(Expression):
    def __init__(self, value:int):
        Expression.__init__(self)
        self.literal = True
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

class Float(Expression):
    def __init__(self, value:str):
        Expression.__init__(self)
        self.literal = True
        self.value = float(value)
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class Bool(Expression):
    def __init__(self, value:str):
        Expression.__init__(self)
        self.literal = True
        self.value = value.lower() == 'true'
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value
