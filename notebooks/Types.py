import polars as pl

class decimal(pl.Decimal):
    def pl_schema(self):
        return pl.Decimal()
    
class float(pl.Float32):
    def pl_schema(self):
        return pl.Float32()

class double(pl.Float64):
    def pl_schema(self):
        return pl.Float64()
    
class byte(pl.Int8):
    def pl_schema(self):
        return pl.Int8()

class short(pl.Int16):
    def pl_schema(self):
        return pl.Int16()

class int(pl.Int32):
    def pl_schema(self):
        return pl.Int32()
    
class long(pl.Int64):
    def pl_schema(self):
        return pl.Int64()

class xlong(pl.Int128):
    def pl_schema(self):
        return pl.Int128()

class guid(pl.Int128):
    def pl_schema(self):
        return pl.Int128()
    
class ubyte(pl.UInt8):
    def pl_schema(self):
        return pl.UInt8()
    
class ushort(pl.UInt16):
    def pl_schema(self):
        return pl.UInt16()
    
class uint(pl.UInt32):
    def pl_schema(self):
        return pl.UInt32()
    
class ulong(pl.UInt64):
    def pl_schema(self):
        return pl.UInt64()

class ip(pl.String):
    def pl_schema(self):
        return pl.String()

class ip4(pl.UInt32):
    def pl_schema(self):
        return pl.UInt32()

class ip6(pl.Int128):
    def pl_schema(self):
        return pl.Int128()
        
class datetime(pl.Datetime):
    def pl_schema(self):
        return pl.Datetime()
    
class duration(pl.Duration):
    def pl_schema(self):
        return pl.Duration()
        
class time(pl.Time):
    def pl_schema(self):
        return pl.Time()

class range(pl.Struct):
    def __init__(self, start, end):
        self.start = start
        # self.start_clusivity = 'gt' if start_clusivity == 'gt' else 'gte'
        self.end = end
        # self.end_clusivity = 'lt' if end_clusivity == 'lt' else 'lte'

    def pl_schema(self):
        return self.__class__.__bases__[0].__init__({'start': self.start, 'end': self.end})
        
class matrix(pl.Array):
    def pl_schema(self):
        return pl.Array()
    
class multivalue(pl.List):
    def pl_schema(self):
        if isinstance(self.inner, type(self)):
            return pl.List(self.inner.pl_schema())
        else:
            return pl.List(self.inner().pl_schema())
    
class string(pl.String):
    def pl_schema(self):
        return pl.String()
        
class enum(pl.Enum):
    def pl_schema(self):
        return pl.Enum()
        
class binary(pl.Binary):
    def pl_schema(self):
        return pl.Binary()
    
class bool(pl.Boolean):
    def pl_schema(self):
        return pl.Boolean()
    
class null(pl.Null):
    def pl_schema(self):
        return pl.Null()
    
class unknown(pl.Unknown):
    def pl_schema(self):
        return pl.Unknown()