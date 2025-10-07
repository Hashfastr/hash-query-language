from numpy import isin
import polars as pl
import logging
from typing import TYPE_CHECKING, Union

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
from Hql.Types.Compiler import CompilerType

if TYPE_CHECKING:
    from Hql.Data import Series

class HqlTypes():
    class HqlType(CompilerType):
        def __init__(self, proto:pl.DataType, inner:Union[None, type]=None):
            CompilerType.__init__(self, type(self), inner=inner)
            
            self.proto:pl.DataType = proto
                
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
    def from_name(name:str):
        return get_type(f'hql_{name}')
    
    @staticmethod
    def resolve_conflict(types:list[HqlType]):
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

    @register_type('hql_decimal')
    class decimal(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Decimal())
    
    @register_type('hql_float') 
    class float(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Float32())
            self.priority = 3
            self.super = [HqlTypes.string, HqlTypes.multivalue]

    @register_type('hql_double')
    class double(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Float64())
    
    @register_type('hql_byte') 
    class byte(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int8())

    @register_type('hql_short')
    class short(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int16())

    @register_type('hql_int')
    class int(HqlType, pl.Int32):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int32())
            
            self.priority = 2
            self.super = [HqlTypes.float, HqlTypes.string, HqlTypes.multivalue]
    
    @register_type('hql_long') 
    class long(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int64())

    @register_type('hql_xlong')
    class xlong(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int128())

    @register_type('hql_guid')
    class guid(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int128())
    
    @register_type('hql_ubyte') 
    class ubyte(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.UInt8())
        
    @register_type('hql_ushort')
    class ushort(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.UInt16())
    
    @register_type('hql_uint') 
    class uint(HqlType, pl.UInt32):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.UInt32())
    
    @register_type('hql_ulong') 
    class ulong(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.UInt64())

    @register_type('hql_ip')
    class ip(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.String())

    @register_type('hql_ip4')
    class ip4(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.UInt32())

            self.complex = True

        def pl_schema(self) -> pl.DataType:
            schema = super().pl_schema()

            if isinstance(schema, dict):
                raise hqle.CompilerException('Returned a dict schema where ')

            return super().pl_schema()

        def cast(self, series:pl.Series):
            # lazy if not string
            if series.dtype != pl.String:
                return series.cast(self.pl_schema())

            ips = []
            for i in series:
                if not i:
                    ips.append(None)
                    continue

                split = i.split('.')
                num = 0
                for idx, j in enumerate(split):
                    try:
                        # magnitude scales with the index
                        num += int(split[idx]) << (8 * (3 - idx))
                    
                    # Likely IPv6 if we hit this
                    # Or trash garbo data
                    except ValueError:
                        continue

                ips.append(num)
                
            return pl.Series(ips, dtype=self.proto)
        
        def human(self, series:pl.Series):
            if series.dtype != self.proto:
                raise hqle.CompilerException('Attempting to human a non-converted ip4 field')

            d = 0xFF
            c = d << 8
            b = c << 8
            a = b << 8
            
            ips = []
            for i in series:
                if i == None:
                    ips.append(None)
                    continue
                
                ips.append(f'{(i & a) >> 24}.{(i & b) >> 16}.{(i & c) >> 8}.{i & d}')

            return pl.Series(ips, dtype=pl.String)                

    @register_type('hql_ip6')
    class ip6(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Int128())
    
    @register_type('hql_datetime')     
    class datetime(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Datetime())
        
    @register_type('hql_duration')
    class duration(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Duration())
        
    @register_type('hql_time')  
    class time(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Time())

    # Need to figure this out properly
    @register_type('hql_range')
    class range(HqlType, pl.Struct):
        def __init__(self, inner:type):
            self.inner = inner
            HqlTypes.HqlType.__init__(self, self.pl_schema())

        def pl_schema(self) -> pl.DataType:
            return pl.Struct(fields=[pl.Field('start', self.inner), pl.Field('end', self.inner)])

    @register_type('hql_matrix')
    class matrix(HqlType):
        def __init__(self, dtype:"HqlTypes.HqlType"):
            HqlTypes.HqlType.__init__(self, self.pl_schema())
            self.dtype = dtype
            
            raise hqle.CompilerException('Unimplemented hql type matrix')

        def pl_schema(self) -> pl.DataType:
            return pl.Array(self.dtype.pl_schema())
    
    @register_type('hql_string') 
    class string(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.String())
            
            self.priority = 4
            self.super = [HqlTypes.multivalue]
        
    @register_type('hql_enum') 
    class enum(HqlType):
        def __init__(self):
            raise hqle.CompilerException('Unimplemented type enum')
            HqlTypes.HqlType.__init__(self, pl.Null())
        
    @register_type('hql_binary') 
    class binary(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Binary())
    
    @register_type('hql_bool') 
    class bool(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Boolean())
            
            self.priority = 1
            self.super = [HqlTypes.int, HqlTypes.string, HqlTypes.multivalue]

    '''
    This is a generic object, unspecified the contents
    '''
    @register_type('hql_object')
    class object(HqlType):
        def __init__(self, schema:Union[dict, None]=None):
            self.schema = schema if schema else dict()
            HqlTypes.HqlType.__init__(self, self.pl_schema())

        def pl_schema(self) -> pl.DataType:
            return pl.Struct(self.schema)
            
    @register_type('hql_null')
    class null(HqlType):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Null())
            
            self.priority = 0
            self.super = [HqlTypes.bool, HqlTypes.int, HqlTypes.float, HqlTypes.string, HqlTypes.multivalue]
        
    @register_type('hql_unknown')
    class unknown(HqlType, pl.Unknown):
        def __init__(self):
            HqlTypes.HqlType.__init__(self, pl.Unknown())
            raise hqle.CompilerException('Unknown type Unimplemented')
        
    @register_type('hql_multivalue')
    class multivalue(HqlType):
        def __init__(self, inner:type):
            self.inner = inner
            HqlTypes.HqlType.__init__(self, self.pl_schema(), inner=inner)
            
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
