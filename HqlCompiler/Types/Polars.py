import logging
import polars as pl

from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_type, get_type
# from HqlCompiler.Types.Compiler import CompilerType

class PolarsTypes():
    from .Hql import HqlTypes as hqlt
    
    class PolarsType():
        def __init__(self):
            if len(type(self).__bases__):
                super().__init__()
                self.HqlType = type(self).__bases__[-1]
            else:
                self.HqlType = None
        
        def hql_schema(self):
            if self.HqlType:
                return self.HqlType()
            return None
        
        def pl_schema(self):
            return self

        def __len__(self):
            return 1
        
    @staticmethod
    def from_name(name:str):
        return get_type(f'polars_{name}')
    
    @staticmethod
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
    class Decimal(PolarsType, hqlt.decimal):
        ...

    @register_type('polars_Float32')
    class Float32(PolarsType, hqlt.float):
        ...
    
    @register_type('polars_Float64') 
    class Float64(PolarsType, hqlt.double):
        ...
        
    @register_type('polars_Int8')
    class Int8(PolarsType, hqlt.byte):
        ...
    
    @register_type('polars_Int16') 
    class Int16(PolarsType, hqlt.short):
        ...
    
    @register_type('polars_Int32') 
    class Int32(PolarsType, hqlt.int):
        ...
    
    @register_type('polars_Int64') 
    class Int64(PolarsType, hqlt.long):
        ...
    
    @register_type('polars_Int128') 
    class Int128(PolarsType, hqlt.xlong):
        ...
    
    @register_type('polars_UInt8') 
    class UInt8(PolarsType, hqlt.ubyte):
        ...
    
    @register_type('polars_UInt16') 
    class UInt16(PolarsType, hqlt.ushort):
        ...
        
    @register_type('polars_UInt32')
    class UInt32(PolarsType, hqlt.uint):
        ...
    
    @register_type('polars_UInt64') 
    class UInt64(PolarsType, hqlt.ulong):
        ...
    
    @register_type('polars_Date') 
    class Date(PolarsType, hqlt.datetime):
        ...
    
    @register_type('polars_Duration') 
    class Duration(PolarsType, hqlt.duration):
        ...
    
    @register_type('polars_Time') 
    class Time(PolarsType, hqlt.time):
        ...
    
    @register_type('polars_Array') 
    class Array(PolarsType, hqlt.matrix):
        ...
    
    @register_type('polars_List') 
    class List(PolarsType, hqlt.multivalue):
        ...
    
    @register_type('polars_String') 
    class String(PolarsType, hqlt.string):
        ...
        
    @register_type('polars_Enum')
    class Enum(PolarsType, hqlt.enum):
        ...
    
    @register_type('polars_Utf8') 
    class Utf8(PolarsType, hqlt.string):
        ...
        
    @register_type('polars_Binary')
    class Binary(PolarsType, hqlt.binary):
        ...
        
    @register_type('polars_Boolean')
    class Boolean(PolarsType, hqlt.bool):
        ...
        
    @register_type('polars_Null') 
    class Null(PolarsType, hqlt.null):
        ...
        
    @register_type('polars_Object')   
    class Object(PolarsType, hqlt.object):
        ...

    @register_type('polars_Struct')   
    class Struct(PolarsType, hqlt.object):
        def __init__(self, fields:list[str]):
            super().__init__()
        
    @register_type('polars_Unknown')
    class Unknown(PolarsType, hqlt.unknown):
        ...
