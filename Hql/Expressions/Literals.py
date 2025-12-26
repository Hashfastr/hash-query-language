from typing import TYPE_CHECKING, Union, Optional
import polars as pl
import datetime

from .__proto__ import Expression
from Hql.Types.Hql import HqlTypes as hqlt

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Data import Series

class Literal(Expression):
    def __init__(self, hql_type:hqlt.HqlType) -> None:
        Expression.__init__(self)
        self.literal = True
        self.hql_type = hql_type

    def series(self) -> 'Series':
        from Hql.Data import Series
        series = Series(pl.Series([self.value]), self.hql_type)
        return series.cast()

    def polars(self) -> Union[pl.Expr, pl.DataTypeExpr]:
        return pl.lit(self.value)

    def polars_value(self) -> 'pl.Expr':
        return self.polars()

    def str(self) -> str:
        return str(self.value)
    
    def dtype(self) -> hqlt.HqlType:
        return self.hql_type

    def deparse(self) -> str:
        return self.str()

    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }

class TypeExpression(Literal):
    def __init__(self, hql_type:Union[str, hqlt.HqlType]):
        Literal.__init__(self, hqlt.type())
        self.hql_type:hqlt.HqlType = hqlt.from_name(hql_type) if isinstance(hql_type, str) else hql_type

    def polars(self) -> pl.DataTypeExpr:
        return pl.Decimal().to_dtype_expr()

    def polars_value(self) -> pl.Expr:
        return NotImplemented

    def deparse(self) -> str:
        return self.hql_type.name

    def dtype(self) -> hqlt.HqlType:
        return self.hql_type

class StringLiteral(Literal):
    def __init__(self, value:Union[str, bytes], verbatim:bool=False, obfuscated:bool=False):
        Literal.__init__(self, hqlt.string())

        if isinstance(value, str):
            value = value.encode('utf-8')

        self.value:bytes = value
        self.verbatim = verbatim
        self.obfuscated = obfuscated

    def quote(self, quote:str) -> str:
        import re

        if quote:
            new = ''.join([fr'\{x}' for x in quote])
            cur = re.sub(quote, new, self.value.decode('utf-8'))
        else:
            cur = self.value.decode('utf-8')

        if not self.verbatim:
            cur = cur.encode('unicode_escape').decode('utf-8')

        return quote + cur + quote

    def polars(self) -> 'pl.Expr':
        return pl.lit(self.str())

    def str(self) -> str:
        return self.quote('')
    
    def dtype(self) -> hqlt.HqlType:
        return hqlt.string()

    def deparse(self) -> str:
        if self.verbatim:
            if '\n' in self.value.decode('utf-8'):
                quoted = self.quote("'''")
            else:
                quoted = '@' + self.quote("'")
        else:
            quoted = self.quote("'")

        if self.obfuscated:
            quoted = 'h' + quoted
        return quoted
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.quote('')
        }

class MultiString(StringLiteral):
    def __init__(self, strlits:Optional[list[StringLiteral]]=None):
        Literal.__init__(self, hqlt.string())
        self.strlits:list[StringLiteral] = strlits if strlits else []

    def str(self) -> str:
        running = ''
        for i in self.strlits:
            running += i.str()
        return running
         
    def deparse(self) -> str:
        return ' '.join([x.deparse() for x in self.strlits])

    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'value': [x.to_dict() for x in self.strlits]
        }

class Integer(Literal):
    def __init__(self, value:Union[str, int]):
        Literal.__init__(self, hqlt.int())
        self.value = int(value)
        
class IP4(Literal):
    def __init__(self, value:Union[Integer, StringLiteral]):
        Literal.__init__(self, hqlt.ip4())
        
        if isinstance(value, StringLiteral):
            self.value = hqlt.ip4().cast_single(value)
        else:
            self.value = value

    def str(self):
        return hqlt.ip4().human_single(self.value)

    def deparse(self) -> str:
        return f"ip4('{self.str()}')"
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.str()
        }

class Float(Literal):
    def __init__(self, value:Union[str, float]):
        Literal.__init__(self, hqlt.float())
        self.value = float(value)

class Bool(Literal):
    def __init__(self, value:bool):
        Literal.__init__(self, hqlt.bool())
        self.value = value

class Multivalue(Literal):
    def __init__(self, value:list[Literal]) -> None:
        super_type = hqlt.resolve_conflict([x.hql_type for x in value])
        Literal.__init__(self, hqlt.multivalue(super_type))

        series = pl.Series([x.value for x in value])
        self.value = self.hql_type.cast(series)

    def deparse(self) -> str:
        return NotImplemented
        self.hql_type.inner()
        dec = [ for x in self.value]
        return 'make_mv(' + ', '.join(dec) + ')'

class Datetime(Literal):
    def __init__(self, value:Union[StringLiteral, datetime.datetime]) -> None:
        from dateutil import parser
        Literal.__init__(self, hqlt.datetime())

        if isinstance(value, StringLiteral):
            self.value:datetime.datetime = parser.parse(value.value)
        else:
            self.value = value

    def render(self, time_format:str="%Y-%m-%dT%H:%M:%S.%f%z", timezone:datetime.timezone=datetime.timezone.utc) -> str:
        dt = self.value.astimezone(timezone)
        return dt.strftime(time_format)

    def deparse(self) -> str:
        inner = StringLiteral(self.value.isoformat())
        return 'datetime(' + inner.str() + ')'

class Null(Literal):
    def __init__(self) -> None:
        Literal.__init__(self, hqlt.null())
