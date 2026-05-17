from typing import TYPE_CHECKING, Union, Optional
import datetime

from .__proto__ import Expression
from Hql.Types.Hql import HqlTypes as hqlt

from Hql.Expressions.Logic import Logic

if TYPE_CHECKING:
    from Hql.Data import Series
    from Hql.Context import Context
    import polars as pl

class Literal(Expression):
    def __init__(self, hql_type:hqlt.HqlType, value:object) -> None:
        Expression.__init__(self)
        self.literal = True
        self.hql_type = hql_type
        self.value = value

    def series(self) -> 'Series':
        from Hql.Data import Series
        import polars as pl
        series = Series(pl.Series([self.value]), self.hql_type)
        return series.cast()

    def polars(self) -> 'pl.Expr':
        import polars as pl
        return pl.lit(self.value).cast(self.hql_type.pl_schema())

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
        self.hql_type:hqlt.HqlType = hqlt.from_name(hql_type) if isinstance(hql_type, str) else hql_type
        Literal.__init__(self, self.hql_type, None)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, TypeExpression):
            return False
        return self.hql_type == value.hql_type
    
    def polars(self) -> 'pl.Expr':
        import polars as pl
        return pl.lit(self.hql_type.pl_schema())

    def deparse(self) -> str:
        return self.hql_type.str()

    def dtype(self) -> hqlt.HqlType:
        return self.hql_type

class StringLiteral(Literal):
    def __init__(self, value:Union[str, bytes], verbatim:bool=False, obfuscated:bool=False):
        if isinstance(value, str):
            value = value.encode('utf-8')

        self.value:bytes = value
        self.verbatim = verbatim
        self.obfuscated = obfuscated
        
        Literal.__init__(self, hqlt.string(), self.value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, StringLiteral):
            return False
        return value.value == self.value

    def cmp(self, value:Expression, cs:bool=True):
        from Hql.Expressions.Literals import StringLiteral

        if cs or not isinstance(value, StringLiteral):
            return self == value
        else:
            return self.str().lower() == value.str().lower()

    def startswith(self, value:StringLiteral, cs:bool=True) -> bool:
        if cs:
            return self.value.startswith(value.value)
        else:
            return self.str().lower().startswith(value.str().lower())

    def endswith(self, value:StringLiteral, cs:bool=True) -> bool:
        if cs:
            return self.value.endswith(value.value)
        else:
            return self.str().lower().endswith(value.str().lower())

    def contains(self, value:StringLiteral, cs:bool=True) -> bool:
        if cs:
            return value.value in self.value
        else:
            return value.str().lower() in self.str().lower()

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
        import polars as pl
        return pl.lit(self.str())

    def str(self) -> str:
        return self.quote('')

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
        self.strlits:list[StringLiteral] = strlits if strlits else []
        Literal.__init__(self, hqlt.string(), None)

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

    def preprocess(self, ctx:'Context') -> object:
        return StringLiteral(self.str())

class Integer(Literal):
    def __init__(self, value:Union[str, int]):
        self.value = int(value)
        Literal.__init__(self, hqlt.int(), self.value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Integer):
            return False
        return value.value == self.value
        
class IP4(Literal):
    def __init__(self, value:Union[Integer, StringLiteral]):
        if isinstance(value, StringLiteral):
            self.value = hqlt.ip4().cast_single(value)
        else:
            self.value = value

        Literal.__init__(self, hqlt.ip4(), self.value)

    def str(self):
        return hqlt.ip4().human_single(self.value)

    def deparse(self) -> str:
        return f"ip4('{self.str()}')"

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, IP4):
            return False
        return value.value == self.value
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.str()
        }

class Float(Literal):
    def __init__(self, value:Union[str, float]):
        self.value = float(value)
        Literal.__init__(self, hqlt.float(), self.value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Float):
            return False
        return value.value == self.value

class Bool(Logic, Literal):
    def __init__(self, value:bool):
        self.value = value
        Literal.__init__(self, hqlt.bool(), self.value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Bool):
            return False
        return value.value == self.value

class Multivalue(Literal):
    def __init__(self, value:list[Literal]) -> None:
        import polars as pl
        super_type = hqlt.resolve_conflict([x.hql_type for x in value])

        series = pl.Series([x.value for x in value])
        self.value = self.hql_type.cast(series)
        
        Literal.__init__(self, hqlt.multivalue(super_type), self.value)

    def __len__(self):
        return len(self.value)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Multivalue):
            return False

        '''
        # for later if we want to consider a single multivalue as a comparison
        if not isinstance(value, Literal):
            return False
        value = Multivalue([value])
        '''
        
        if len(self) != len(value):
            return False

        for idx, _ in enumerate(self.value):
            if self.value[idx] != value.value[idx]:
                return False

        return True

    def deparse(self) -> str:
        return NotImplemented
        # self.hql_type.inner()
        # dec = [ for x in self.value]
        # return 'make_mv(' + ', '.join(dec) + ')'

class Datetime(Literal):
    def __init__(self, value:Union[StringLiteral, datetime.datetime]) -> None:
        from dateutil import parser
        if isinstance(value, StringLiteral):
            self.value:datetime.datetime = parser.parse(value.value)
        else:
            self.value = value
        
        Literal.__init__(self, hqlt.datetime(), self.value)

    def render(self, time_format:str="%Y-%m-%dT%H:%M:%S.%f%z", timezone:datetime.timezone=datetime.timezone.utc) -> str:
        dt = self.value.astimezone(timezone)
        return dt.strftime(time_format)

    def deparse(self) -> str:
        inner = StringLiteral(self.value.isoformat())
        return 'datetime(' + inner.str() + ')'

class Null(Literal):
    def __init__(self) -> None:
        Literal.__init__(self, hqlt.null(), None)
