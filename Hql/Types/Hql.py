import polars as pl
import logging
from typing import TYPE_CHECKING, Union, Optional

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
from Hql.Types.Compiler import CompilerType

if TYPE_CHECKING:
    from Hql.Data import Series
    from Hql.Expressions.Literals import Integer, StringLiteral

class HqlTypes():
    class HqlType(CompilerType):
        def __init__(self, inner:Optional['HqlTypes.HqlType']=None):
            CompilerType.__init__(self, inner=inner)
            self.proto:Optional[pl.DataType] = None
                
            self.complex:bool = False
            self.priority:int = 0
            self.super:list[type] = [HqlTypes.string, HqlTypes.multivalue]

        def pl_schema(self) -> pl.DataType:
            if self.proto == None:
                raise hqle.CompilerException(f'{self.name}')
            else:
                return self.proto

        def cast(self, series:pl.Series):
            if self.proto == None:
                raise hqle.CompilerException('Attempting to cast data to type without a prototype')

            return series.cast(self.pl_schema())

        def __len__(self):
            return 1

        def hql_schema(self):
            return self
    
    @staticmethod
    def from_name(name:str) -> HqlTypes.HqlType:
        return get_type(f'hql_{name}')
    
    @staticmethod
    def resolve_conflict(types:list[HqlType]) -> HqlType:
        if len(types) == 1:
            return types[0]
        
        # Check to see if there's a multivalue we need to handle
        mv = False
        for i in types:
            if isinstance(i, HqlTypes.multivalue):
                mv = True
                break
        
        # Handle multivalue
        if mv:
            inner_set = set()
            for i in types:
                if isinstance(i, HqlTypes.multivalue):
                    inner_set.add(i.inner)
                else:
                    inner_set.add(i)
            types = list(inner_set)

        # set to default basecase
        l = HqlTypes.null()
        for r in types:
            # Check to see if we need to instanciate
            if isinstance(r, type):
                r = r()
            
            if l.priority > r.priority:
                continue

            if type(r) in l.super:
                l = r
                continue

        if mv:
            return HqlTypes.multivalue(l)
        else:
            return l

    @register_type('hql_type')
    class type(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.DataType()

    @register_type('hql_decimal')
    class decimal(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Decimal()
    
    @register_type('hql_float') 
    class float(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Float32()

            self.priority = 3
            self.super = [HqlTypes.string, HqlTypes.multivalue]

    @register_type('hql_double')
    class double(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Float64()
    
    @register_type('hql_byte') 
    class byte(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Int8()

    @register_type('hql_short')
    class short(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Int16()

    @register_type('hql_int')
    class int(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Int32()
            
            self.priority = 2
            self.super = [HqlTypes.float, HqlTypes.string, HqlTypes.multivalue]
    
    @register_type('hql_long') 
    class long(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)

    @register_type('hql_xlong')
    class xlong(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Int128()

    @register_type('hql_guid')
    class guid(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Int128()
    
    @register_type('hql_ubyte') 
    class ubyte(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.UInt8()
        
    @register_type('hql_ushort')
    class ushort(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.UInt16()
    
    @register_type('hql_uint') 
    class uint(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.UInt32()
    
    @register_type('hql_ulong') 
    class ulong(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.UInt64()

    @register_type('hql_ip')
    class ip(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.String()

    @register_type('hql_ip4')
    class ip4(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.UInt32()

            self.complex = True

        def cast_single(self, ip:Union['StringLiteral', str]) -> int:
            from Hql.Expressions.Literals import StringLiteral

            if isinstance(ip, StringLiteral):
                ip = ip.str()

            split = ip.split('.')
            num = 0
            for idx, j in enumerate(split):
                try:
                    # magnitude scales with the index
                    num += int(split[idx]) << (8 * (3 - idx))
                
                # Likely IPv6 if we hit this
                # Or trash garbo data
                except ValueError:
                    continue
            return num

        def cast(self, series:pl.Series):
            # lazy if not string
            if series.dtype != pl.String:
                return series.cast(self.pl_schema())

            ips = []
            for i in series:
                ips.append(self.cast_single(i)) if i != None else ips.append(None)
                
            return pl.Series(ips, dtype=self.proto)
        
        def human_single(self, ip:Union['Integer', int]) -> str:
            from Hql.Expressions.Literals import Integer

            if isinstance(ip, Integer):
                ip = ip.value

            d = 0xFF
            c = d << 8
            b = c << 8
            a = b << 8

            return f'{(ip & a) >> 24}.{(ip & b) >> 16}.{(ip & c) >> 8}.{ip & d}'
        
        def human(self, series:pl.Series):
            if series.dtype != self.proto:
                raise hqle.CompilerException('Attempting to human a non-converted ip4 field')
            
            ips = []
            for i in series:
                ips.append(self.human_single(i)) if i != None else ips.append(None)

            return pl.Series(ips, dtype=pl.String)                

    @register_type('hql_ip6')
    class ip6(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Int128()
    
    @register_type('hql_datetime')     
    class datetime(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Datetime()

            self.complex = True

        def human(self, series:pl.Series):
            dates = []
            for i in series:
                if i == None:
                    dates.append(None)
                    continue
                dates.append(i.isoformat())
            return pl.Series(dates, dtype=pl.String)
        
    @register_type('hql_duration')
    class duration(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Duration()
        
    @register_type('hql_time')  
    class time(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Time()

    # Need to figure this out properly
    @register_type('hql_range')
    class range(HqlType, pl.Struct):
        def __init__(self, inner:'HqlTypes.HqlType'):
            HqlTypes.HqlType.__init__(self, inner=inner)
            self.proto = self.pl_schema()

        def pl_schema(self) -> pl.DataType:
            assert self.inner != None
            pl_schema = self.inner.pl_schema()
            return pl.Struct(fields=[pl.Field('start', pl_schema), pl.Field('end', pl_schema)])

    @register_type('hql_matrix')
    class matrix(HqlType):
        def __init__(self, inner:'HqlTypes.HqlType'):
            HqlTypes.HqlType.__init__(self, inner=inner)
            raise hqle.CompilerException('Unimplemented hql type matrix')

        def pl_schema(self) -> pl.DataType:
            assert self.inner != None
            return pl.Array(self.inner.pl_schema())
    
    @register_type('hql_string') 
    class string(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.String()
            
            self.priority = 4
            self.super = [HqlTypes.multivalue]
        
    @register_type('hql_enum') 
    class enum(HqlType):
        def __init__(self, values:list[str]):
            raise hqle.CompilerException('Unimplemented type enum')
            HqlTypes.HqlType.__init__(self, pl.Null())
        
    @register_type('hql_binary') 
    class binary(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Binary()
    
    @register_type('hql_bool') 
    class bool(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Boolean()
            
            self.priority = 1
            self.super = [HqlTypes.int, HqlTypes.string, HqlTypes.multivalue]

    '''
    This is a generic object, unspecified the contents
    '''
    @register_type('hql_object')
    class object(HqlType):
        def __init__(self, schema:dict):
            HqlTypes.HqlType.__init__(self)
            self.schema = self.convert_dict(schema)
            self.proto = self.pl_schema()

        def convert_dict(self, d:dict, t:str='hql') -> dict:
            new = {}
            for i in d:
                if isinstance(d[i], dict):
                    new[i] = self.convert_dict(d[i], t=t)
                elif t == 'hql':
                    new[i] = d[i].hql_schema()
                else:
                    new[i] = d[i].pl_schema()
            return new

        def pl_schema(self) -> pl.DataType:
            return pl.Struct(self.convert_dict(self.schema, t='pl'))
            
    @register_type('hql_null')
    class null(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Null()
            
            self.priority = 0
            self.super = [HqlTypes.bool, HqlTypes.int, HqlTypes.float, HqlTypes.string, HqlTypes.multivalue]
        
    @register_type('hql_unknown')
    class unknown(HqlType, pl.Unknown):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            self.proto = pl.Unknown()
            raise hqle.CompilerException('Unknown type Unimplemented')
        
    @register_type('hql_multivalue')
    class multivalue(HqlType):
        def __init__(self, inner:'HqlTypes.HqlType'):
            self.inner = inner
            assert inner.proto
            self.proto = pl.List(inner.proto)

            HqlTypes.HqlType.__init__(self, inner=inner)
            
            self.priority = 5
            self.super = []
        
        def pl_schema(self):
            if isinstance(self.inner, type):
                return pl.List(self.inner().pl_schema())

            return pl.List(self.inner.pl_schema())
        
        # Casts a polars series to List
        def cast(self, series:pl.Series):
            if not self.inner:
                logging.critical('Cannot cast to empty multivalue!')
                raise TypeError('Attempted to cast to empty multivalue')
            
            return series.cast(self.pl_schema())
