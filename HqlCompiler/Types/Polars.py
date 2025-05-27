import logging
import polars as pl

from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_type, get_type
# from HqlCompiler.Types.Compiler import CompilerType

class PolarsTypes():
    from .Hql import HqlTypes as Hql
    
    class PolarsType():
        def __init__(self):
            if len(type(self).__bases__):
                super().__init__()
                self.HqlType = type(self).__bases__[-1]
            else:
                self.HqlType = None
        
        def hql_schema(self):
            return self.HqlType
        
        def pl_schema(self):
            return self
        
    def from_name(name:str):
        return get_type(f'polars_{name}')
    
    def from_pure_polars(pltype:pl.DataType):
        if hasattr(pltype, '__name__'):
            name = pltype.__name__
        else:
            name = type(pltype).__name__

        resolved = PolarsTypes.from_name(name)

        if hasattr(pltype, 'inner'):
            inner = PolarsTypes.from_pure_polars(pltype.inner)
            return resolved(inner)
        else:
            return resolved()
            
    @register_type('polars_Decimal')
    class Decimal(PolarsType, Hql.decimal):
        ...

    @register_type('polars_Float32')
    class Float32(PolarsType, Hql.float):
        ...
    
    @register_type('polars_Float64') 
    class Float64(PolarsType, Hql.double):
        ...
        
    @register_type('polars_Int8')
    class Int8(PolarsType, Hql.byte):
        ...
    
    @register_type('polars_Int16') 
    class Int16(PolarsType, Hql.short):
        ...
    
    @register_type('polars_Int32') 
    class Int32(PolarsType, Hql.int):
        ...
    
    @register_type('polars_Int64') 
    class Int64(PolarsType, Hql.long):
        ...
    
    @register_type('polars_Int128') 
    class Int128(PolarsType, Hql.xlong):
        ...
    
    @register_type('polars_UInt8') 
    class UInt8(PolarsType, Hql.ubyte):
        ...
    
    @register_type('polars_UInt16') 
    class UInt16(PolarsType, Hql.ushort):
        ...
        
    @register_type('polars_UInt32')
    class UInt32(PolarsType, Hql.uint):
        ...
    
    @register_type('polars_UInt64') 
    class UInt64(PolarsType, Hql.ulong):
        ...
    
    @register_type('polars_Date') 
    class Date(PolarsType, Hql.datetime):
        ...
    
    @register_type('polars_Duration') 
    class Duration(PolarsType, Hql.duration):
        ...
    
    @register_type('polars_Time') 
    class Time(PolarsType, Hql.time):
        ...
    
    @register_type('polars_Array') 
    class Array(PolarsType, Hql.matrix):
        ...
    
    @register_type('polars_List') 
    class List(PolarsType, Hql.multivalue):
        ...
    
    @register_type('polars_String') 
    class String(PolarsType, Hql.string):
        ...
        
    @register_type('polars_Enum')
    class Enum(PolarsType, Hql.enum):
        ...
    
    @register_type('polars_Utf8') 
    class Utf8(PolarsType, Hql.string):
        ...
        
    @register_type('polars_Binary')
    class Binary(PolarsType, Hql.binary):
        ...
        
    @register_type('polars_Boolean')
    class Boolean(PolarsType, Hql.bool):
        ...
        
    @register_type('polars_Null') 
    class Null(PolarsType, Hql.null):
        ...
        
    @register_type('polars_Object')   
    class Object(PolarsType, Hql.object):
        ...
        
    @register_type('polars_Unknown')
    class Unknown(PolarsType, Hql.unknown):
        ...