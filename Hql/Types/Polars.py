from typing import TYPE_CHECKING, Optional, Union
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
from Hql.Types.Compiler import CompilerType

import polars as pl

from Hql.Types.Hql import HqlTypes as hqlt

class PolarsTypes():
    class PolarsType(CompilerType):
        def __init__(self, inner:Optional['PolarsTypes.PolarsType']=None):
            CompilerType.__init__(self, inner=inner)
            self.inner:Optional[PolarsTypes.PolarsType] = inner
            self.pltype:Optional[pl.DataType] = None

        def pl_schema(self) -> pl.DataType:
            if isinstance(self.pltype, type(None)):
                raise hqle.CompilerException(f'Polars type {self.name} has no defined pl_schema')
            return self.pltype
        
    @staticmethod
    def from_name(name:str):
        return get_type(f'polars_{name}')
    
    @staticmethod
    def from_pure_polars(pltype) -> PolarsType:
        if hasattr(pltype, '__name__'):
            name = pltype.__name__
        else:
            name = type(pltype).__name__

        resolved = PolarsTypes.from_name(name)

        if hasattr(pltype, 'inner'):
            inner = PolarsTypes.from_pure_polars(pltype.inner)
            return resolved(inner=inner)
        else:
            return resolved()
            
    @register_type('polars_Decimal')
    class Decimal(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.decimal()
            self.pltype = pl.Decimal()

    @register_type('polars_Float32')
    class Float32(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.float()
            self.pltype = pl.Float32()
    
    @register_type('polars_Float64') 
    class Float64(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.double()
            self.pltype = pl.Float64()
        
    @register_type('polars_Int8')
    class Int8(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.byte()
            self.pltype = pl.Int8()
    
    @register_type('polars_Int16') 
    class Int16(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.short()
            self.pltype = pl.Int16()
    
    @register_type('polars_Int32') 
    class Int32(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.int()
            self.pltype = pl.Int32()
    
    @register_type('polars_Int64') 
    class Int64(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.long()
            self.pltype = pl.Int64()
    
    @register_type('polars_Int128') 
    class Int128(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.xlong()
            self.pltype = pl.UInt128()
    
    @register_type('polars_UInt8') 
    class UInt8(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.ubyte()
            self.pltype = pl.UInt8()
    
    @register_type('polars_UInt16') 
    class UInt16(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.ushort()
            self.pltype = pl.UInt16()
        
    @register_type('polars_UInt32')
    class UInt32(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.uint()
            self.pltype = pl.UInt32()
    
    @register_type('polars_UInt64') 
    class UInt64(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.ulong()
            self.pltype = pl.UInt64()
    
    @register_type('polars_Date') 
    class Date(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.datetime()
            self.pltype = pl.Date()
    
    @register_type('polars_Duration') 
    class Duration(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.duration()
            self.pltype = pl.Duration()
    
    @register_type('polars_Time') 
    class Time(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.time()
            self.pltype = pl.Time()
    
    @register_type('polars_Array') 
    class Array(PolarsType):
        def __init__(self, inner:'PolarsTypes.PolarsType'):
            PolarsTypes.PolarsType.__init__(self, inner=inner)
            self.HqlType = hqlt.matrix(inner.hql_schema())
            self.pltype = pl.Array(inner.pl_schema())
    
    @register_type('polars_List') 
    class List(PolarsType):
        def __init__(self, inner:'PolarsTypes.PolarsType'):
            PolarsTypes.PolarsType.__init__(self, inner=inner)
            self.HqlType = hqlt.multivalue(inner.hql_schema())
            self.pltype = pl.List(inner.pl_schema())
    
    @register_type('polars_String') 
    class String(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.string()
            self.pltype = pl.String()
        
    @register_type('polars_Enum')
    class Enum(PolarsType):
        def __init__(self, values:list[str]):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.enum(values)
            self.pltype = pl.Enum(values)
    
    @register_type('polars_Utf8') 
    class Utf8(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.string()
            self.pltype = pl.Utf8()
        
    @register_type('polars_Binary')
    class Binary(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.binary()
            self.pltype = pl.Binary()
        
    @register_type('polars_Boolean')
    class Boolean(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.bool()
            self.pltype = pl.Boolean()
        
    @register_type('polars_Null') 
    class Null(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.null()
            self.pltype = pl.Null()
        
    @register_type('polars_Object')   
    class Object(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.object()
            self.pltype = pl.Object()

    @register_type('polars_Struct')   
    class Struct(PolarsType):
        def __init__(self, schema:dict):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.object()

            self.schema = schema
            self.pltype = pl.Struct(schema)
        
    @register_type('polars_Unknown')
    class Unknown(PolarsType):
        def __init__(self):
            PolarsTypes.PolarsType.__init__(self)
            self.HqlType = hqlt.unknown()
            self.pltype = pl.Unknown()
