from typing import TYPE_CHECKING, Union
import polars as pl

from .__proto__ import Expression
from Hql.Types.Hql import HqlTypes as hqlt

if TYPE_CHECKING:
    from Hql.Context import Context

class Literal(Expression):
    def __init__(self) -> None:
        Expression.__init__(self)
        self.literal = True

    def decompile(self, ctx: 'Context') -> str:
        return str(self.value)

class TypeExpression(Literal):
    def __init__(self, type:str):
        Literal.__init__(self)
        self.type = type

    def decompile(self, ctx: 'Context') -> str:
        return self.type
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decompile', False):
            return self.decompile(ctx)

        return hqlt.from_name(self.type)

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Literal):
    def __init__(self, value:str):
        Literal.__init__(self)

        if value[0] == '"':
            self.quote = '"'
        else:
            self.quote = "'"

        self.value = value.strip(self.quote)
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def decompile(self, ctx: 'Context') -> str:
        return self.quote + self.value + self.quote
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decompile', False):
            return self.decompile(ctx)

        if kwargs.get('as_pl', False):
            return pl.lit(self.value)

        return self.value

# Integer
# An integer
# Z
# unreal, not real
class Integer(Literal):
    def __init__(self, value:Union[str, int]):
        Literal.__init__(self)
        self.value = int(value)
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decompile', False):
            return self.decompile(ctx)

        if kwargs.get('as_pl', False):
            return pl.lit(self.value)

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

    def decompile(self, ctx: 'Context') -> str:
        # just stealing how I did this for the ip4 type
        d = 0xFF
        c = d << 8
        b = c << 8
        a = b << 8
        i = self.value

        return f'{(i & a) >> 24}.{(i & b) >> 16}.{(i & c) >> 8}.{i & d}'
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decompile', False):
            return self.decompile(ctx)
        
        return self.value

class Float(Literal):
    def __init__(self, value:Union[str, float]):
        Literal.__init__(self)
        self.value = float(value)
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decompile', False):
            return self.decompile(ctx)
        
        if kwargs.get('as_pl', False):
            return pl.lit(self.value)

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
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decompile', False):
            return self.decompile(ctx)
        
        if kwargs.get('as_pl', False):
            return pl.lit(self.value)

        return self.value
