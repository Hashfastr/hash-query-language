from typing import TYPE_CHECKING, Union
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
from Hql.Types.Compiler import CompilerType

import polars as pl

from Hql.Types.Hql import HqlTypes as hqlt

class PolarsTypes():
    
    class PolarsType(CompilerType):
        def __init__(self, base:type, inner:Union[None, type]=None):
            CompilerType.__init__(self, base, inner=inner)
            
            if self.HqlType == None:
                raise hqle.CompilerException(f'{self.name} is missing a parent polars datatype')

            self.pltype = pl.String

        def pl_schema(self):
            return self.pltype
        
    @staticmethod
    def from_name(name:str):
        return get_type(f'polars_{name}')
    
    @staticmethod
    def from_pure_polars(pltype):
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
    class Decimal(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.decimal)
            self.pltype = pl.Decimal

    @register_type('polars_Float32')
    class Float32(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.float)
            self.pltype = pl.Float32
    
    @register_type('polars_Float64') 
    class Float64(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.double)
            self.pltype = pl.Float64
        
    @register_type('polars_Int8')
    class Int8(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.byte)
            self.pltype = pl.Int8
    
    @register_type('polars_Int16') 
    class Int16(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.short)
            self.pltype = pl.Int16
    
    @register_type('polars_Int32') 
    class Int32(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.int)
            self.pltype = pl.Int32
    
    @register_type('polars_Int64') 
    class Int64(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.long)
            self.pltype = pl.Int64
    
    @register_type('polars_Int128') 
    class Int128(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.xlong)
            self.pltype = pl.UInt128
    
    @register_type('polars_UInt8') 
    class UInt8(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.ubyte)
            self.pltype = pl.UInt8
    
    @register_type('polars_UInt16') 
    class UInt16(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.ushort)
            self.pltype = pl.UInt16
        
    @register_type('polars_UInt32')
    class UInt32(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.uint)
            self.pltype = pl.UInt32
    
    @register_type('polars_UInt64') 
    class UInt64(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.ulong)
            self.pltype = pl.UInt64
    
    @register_type('polars_Date') 
    class Date(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.datetime)
            self.pltype = pl.Date
    
    @register_type('polars_Duration') 
    class Duration(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.duration)
            self.pltype = pl.Duration
    
    @register_type('polars_Time') 
    class Time(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.time)
            self.pltype = pl.Time
    
    @register_type('polars_Array') 
    class Array(PolarsType):
        def __init__(self, inner:type):
            PolarsTypes.PolarsType.__init__(self, hqlt.matrix, inner=inner)

            if hasattr(inner, 'pl_schema'):
                inner = inner.pl_schema()

            self.pltype = pl.Array(inner)
    
    @register_type('polars_List') 
    class List(PolarsType):
        def __init__(self, inner:type):
            PolarsTypes.PolarsType.__init__(self, hqlt.multivalue, inner=inner)

            if hasattr(inner, 'pl_schema'):
                inner = inner.pl_schema()

            self.pltype = pl.List(inner)
    
    @register_type('polars_String') 
    class String(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.string)
            self.pltype = pl.String
        
    @register_type('polars_Enum')
    class Enum(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.enum)
            self.pltype = pl.Enum
    
    @register_type('polars_Utf8') 
    class Utf8(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.string)
            self.pltype = pl.Utf8
        
    @register_type('polars_Binary')
    class Binary(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.binary)
            self.pltype = pl.Binary
        
    @register_type('polars_Boolean')
    class Boolean(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.bool)
            self.pltype = pl.Boolean
        
    @register_type('polars_Null') 
    class Null(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.null)
            self.pltype = pl.Null
        
    @register_type('polars_Object')   
    class Object(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.object)
            self.pltype = pl.Object

    @register_type('polars_Struct')   
    class Struct(PolarsType):
        def __init__(self, fields:list[str]):
            self.fields = fields
            PolarsTypes.PolarsType.__init__(self, hqlt.object)
            self.pltype = pl.Struct
        
    @register_type('polars_Unknown')
    class Unknown(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self, hqlt.unknown)
            self.pltype = pl.Unknown
