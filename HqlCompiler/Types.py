import polars as pl

class decimal(pl.Decimal):
    def pl_type(self):
        return self.__super__()
    
class float(pl.Float32):
    def pl_type(self):
        return self.__super__()

class double(pl.Float64):
    def pl_type(self):
        return self.__super__()
    
class byte(pl.Int8):
    def pl_type(self):
        return self.__super__()

class short(pl.Int16):
    def pl_type(self):
        return self.__super__()

class int(pl.Int32):
    def pl_type(self):
        return self.__super__()
    
class long(pl.Int64):
    def pl_type(self):
        return self.__super__()

class xlong(pl.Int128):
    def pl_type(self):
        return self.__super__()

class guid(pl.Int128):
    def pl_type(self):
        return self.__super__()
    
class ubyte(pl.UInt8):
    def pl_type(self):
        return self.__super__()
    
class ushort(pl.UInt16):
    def pl_type(self):
        return self.__super__()
    
class uint(pl.UInt32):
    def pl_type(self):
        return self.__super__()
    
class ulong(pl.UInt64):
    def pl_type(self):
        return self.__super__()

class ip(pl.String):
    def pl_type(self):
        return self.__super__()

class ip4(pl.UInt32):
    def pl_type(self):
        return self.__super__()

class ip6(pl.Int128):
    def pl_type(self):
        return self.__super__()

    def display(self, value:pl.Int128):
        return self.__super__()
        
class datetime(pl.Datetime):
    def pl_type(self):
        return super
    
class duration(pl.Duration):
    def pl_type(self):
        return self.__super__()
        
class time(pl.Time):
    def pl_type(self):
        return self.__super__()
    
class range(pl.Struct):
    def __init__(self, start, end):
        return super().__init__({'start': start, 'end': end})

    def pl_type(self):
        return self.__super__()
        
class matrix(pl.Array):
    def pl_type(self):
        return self.__super__()
    
class multivalue(pl.List):
    def pl_type(self):
        return self.__super__()
    
class string(pl.String):
    def pl_type(self):
        return self.__super__()
        
class enum(pl.Enum):
    def pl_type(self):
        return self.__super__()
        
class binary(pl.Binary):
    def pl_type(self):
        return self.__super__()
    
class bool(pl.Boolean):
    def pl_type(self):
        return self.__super__()
    
class null(pl.Null):
    def pl_type(self):
        return self.__super__()
    
class unknown(pl.Unknown):
    def pl_type(self):
        return self.__super__()