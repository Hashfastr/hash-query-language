import polars as pl
import logging

from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_type, get_type
# from HqlCompiler.Types.Compiler import CompilerType

class HqlTypes():
    class HqlType():
        def __init__(self):
            # Only init if it's a subclass
            if len(type(self).__bases__):
                self.proto = type(self).__bases__[-1]
            else:
                self.proto = None
                
            self.complex = False
            self.priority = 0
            self.super = (HqlTypes.string, HqlTypes.multivalue)

        def pl_schema(self):
            return self.proto()

        def cast(self, data:pl.Series):
            return data.cast(self.proto)
        
        def hql_schema(self):
            return self
        
    def from_name(name:str):
        return get_type(f'hql_{name}')
    
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
    class decimal(HqlType, pl.Decimal):
        ...
    
    @register_type('hql_float') 
    class float(HqlType, pl.Float32):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            pl.Float32.__init__(self)
            
            self.priority = 3
            self.super = (HqlTypes.string, HqlTypes.multivalue)

    @register_type('hql_double')
    class double(HqlType, pl.Float64):
        ...
    
    @register_type('hql_byte') 
    class byte(HqlType, pl.Int8):
        ...

    @register_type('hql_short')
    class short(HqlType, pl.Int16):
        ...

    @register_type('hql_int')
    class int(HqlType, pl.Int32):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            pl.Int32.__init__(self)
            
            self.priority = 2
            self.super = (HqlTypes.float, HqlTypes.string, HqlTypes.multivalue)
    
    @register_type('hql_long') 
    class long(HqlType, pl.Int64):
        ...

    @register_type('hql_xlong')
    class xlong(HqlType, pl.Int128):
        ...

    @register_type('hql_guid')
    class guid(HqlType, pl.Int128):
        ...
    
    @register_type('hql_ubyte') 
    class ubyte(HqlType, pl.UInt8):
        ...
        
    @register_type('hql_ushort')
    class ushort(HqlType, pl.UInt16):
        ...
    
    @register_type('hql_uint') 
    class uint(HqlType, pl.UInt32):
        ...
    
    @register_type('hql_ulong') 
    class ulong(HqlType, pl.UInt64):
        ...

    @register_type('hql_ip')
    class ip(HqlType, pl.String):
        ...

    @register_type('hql_ip4')
    class ip4(HqlType, pl.UInt32):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            pl.UInt32.__init__(self)

            self.complex = True

        def cast(self, data:pl.Series):
            # lazy if not string
            if data.dtype != pl.String:
                return data.cast(self.proto)

            ips = []
            for i in data:
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
        
        def human(self, data:pl.Series):
            if data.dtype != self.proto:
                raise CompilerException('Attempting to human a non-converted ip4 field')

            ips = []
            for i in data:
                ...
                

    @register_type('hql_ip6')
    class ip6(HqlType, pl.Int128):
        ...
    
    @register_type('hql_datetime')     
    class datetime(HqlType, pl.Datetime):
        ...
        
    @register_type('hql_duration')
    class duration(HqlType, pl.Duration):
        ...
        
    @register_type('hql_time')  
    class time(HqlType, pl.Time):
        ...

    @register_type('hql_range')
    class range(HqlType, pl.Struct):
        def __init__(self, type=None, start=None, end=None):
            pl.Struct.__init__(self, fields=['start', 'end'])

            self.start = start
            # self.start_clusivity = 'gt' if start_clusivity == 'gt' else 'gte'
            self.end = end
            # self.end_clusivity = 'lt' if end_clusivity == 'lt' else 'lte'
            self.type = type

        def pl_schema(self):
            return self.__class__.__bases__[0].__init__({
                'start': self.start, 'end': self.end, 'type': self.type
            })
            
    @register_type('hql_matrix')
    class matrix(HqlType, pl.Array):
        ...
    
    @register_type('hql_string') 
    class string(HqlType, pl.String):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            pl.String.__init__(self)
            
            self.priority = 4
            self.super = (HqlTypes.multivalue)
        
    @register_type('hql_enum') 
    class enum(HqlType, pl.Enum):
        ...
        
    @register_type('hql_binar') 
    class binary(HqlType, pl.Binary):
        ...
    
    @register_type('hql_bool') 
    class bool(HqlType, pl.Boolean):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            pl.Boolean.__init__(self)
            
            self.priority = 1
            self.super = (HqlTypes.int, HqlTypes.string, HqlTypes.multivalue)

    '''
    This is a generic object, unspecified the contents
    '''
    @register_type('hql_object')
    class object(HqlType, pl.Struct):
        def __init__(self, fields:list[str]=None):
            if not fields:
                fields = []
                
            HqlTypes.HqlType.__init__(self)
            pl.Struct.__init__(self, fields)
            
        def cast(self, data: pl.Struct):
            return data
        
        def pl_schema(self):
            return self.proto(self.fields)

        def hql_schema(self):
            return self

    @register_type('hql_null')
    class null(HqlType, pl.Null):
        def __init__(self):
            HqlTypes.HqlType.__init__(self)
            pl.Null.__init__(self)
            
            self.priority = 0
            self.super = (HqlTypes.bool, HqlTypes.int, HqlTypes.float, HqlTypes.string, HqlTypes.multivalue)
        
    @register_type('hql_unknown')
    class unknown(HqlType, pl.Unknown):
        ...
        
    @register_type('hql_multivalue')
    class multivalue(HqlType, pl.List):
        def __init__(self, inner:"HqlTypes.HqlType"):
            HqlTypes.HqlType.__init__(self)
            
            self.priority = 5
            self.super = ()
            
            if isinstance(inner, type):
                inner = inner()
                        
            self.inner = inner
        
        def pl_schema(self):
            return pl.List(self.inner.pl_schema())
        
        # Casts a polars series to List
        def cast(self, data: pl.Series):
            if not self.inner:
                logging.critical('Cannot cast to empty multivalue!')
                raise TypeError('Attempted to cast to empty multivalue')
            
            return data.cast(self.pl_schema())