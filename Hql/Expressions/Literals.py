from typing import TYPE_CHECKING, Union, Optional
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
    def __init__(self, hql_type:str):
        Literal.__init__(self)
        self.hql_type = hql_type

    def decompile(self, ctx: 'Context') -> str:
        return self.hql_type
        
    def eval(self, ctx:'Context', **kwargs):
        return hqlt.from_name(self.hql_type)()

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Literal):
    def __init__(self, value:str, lquote:str="'", rquote:str="'", sanitized=False):
        Literal.__init__(self)

        if not sanitized and '@' not in lquote and value != value.encode('unicode_escape').decode('utf-8'):
            lquote = '@' + lquote

        self.lquote = lquote
        self.rquote = rquote
        self.value = value
        self.sanitized = sanitized
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }

    def decompile(self, ctx: 'Context') -> str:
        if len(self.rquote) == 3:
            return self.lquote + self.value + self.rquote

        if '@' in self.lquote:
            return self.lquote + self.value + self.rquote

        value = self.value
        if not self.sanitized:
            value = value.encode('unicode_escape').decode('utf-8')
        return self.lquote + value + self.rquote
        
    def eval(self, ctx:'Context', **kwargs):
        value = self.value
        if '@' not in self.lquote:
            value = value.encode('utf-8').decode('unicode_escape')

        if 'h' in self.lquote.lower():
            value = bytes.fromhex(value).decode('utf-8')

        if kwargs.get('as_pl', False):
            return pl.lit(value)
        return value

class MultiString(Literal):
    def __init__(self, strlits:Optional[list[StringLiteral]]=None):
        self.strlits = strlits if strlits else []
    
    def to_dict(self) -> Union[None, dict]:
        return {
            'type': self.type,
            'value': [x.to_dict() for x in self.strlits]
        }

    def decompile(self, ctx: 'Context') -> str:
        return ' '.join([x.decompile(ctx) for x in self.strlits])

    def eval(self, ctx:'Context', **kwargs):
        running = ''
        for i in self.strlits:
            running += i.eval(ctx)

        if kwargs.get('as_pl', False):
            return pl.lit(self.value)
        return running


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

    def decompile(self, ctx: 'Context') -> str:
        return str(self.value)
        
    def eval(self, ctx:'Context', **kwargs):
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

    def decompile(self, ctx: 'Context') -> str:
        return str(self.value)
        
    def eval(self, ctx:'Context', **kwargs):
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

    def decompile(self, ctx: 'Context') -> str:
        return str(self.value)
        
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('as_pl', False):
            return pl.lit(self.value)

        return self.value

class Multivalue(Literal):
    def __init__(self, value:list[Literal]) -> None:
        Literal.__init__(self)
        self.value = value

    def decompile(self, ctx: 'Context') -> str:
        dec = [x.decompile(ctx) for x in self.value]
        return 'make_mv(' + ', '.join(dec) + ')'
