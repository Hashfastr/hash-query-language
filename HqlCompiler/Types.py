import polars as pl
import logging

class HqlTypes():
    def type_by_name(name:str):
        types = {
            'multivalue': HqlTypes.multivalue,
            'string': HqlTypes.string,
            'float': HqlTypes.float,
            'int': HqlTypes.int,
            'bool': HqlTypes.bool,
            'null': HqlTypes.null
        }

        return types[name]

    def priority_by_name(name:str):
        priorities = {
            'multivalue': {
                'name': 'multivalue',
                'priority': 5,
                'super': set(),
            },
            'string': {
                'name': 'string',
                'priority': 4,
                'super': {'list'}
            },
            'float': {
                'name': 'float',
                'priority': 3,
                'super': {'str', 'list'}
            },
            'int': {
                'name': 'int',
                'priority': 2,
                'super': {'float', 'str', 'list'}
            },
            'bool': {
                'name': 'bool',
                'priority': 1,
                'super': {'str', 'list'}
            },
            'null': {
                'name': 'null',
                'priority': 0,
                'super': {'bool', 'int', 'float', 'string', 'multivalue'}
            }
        }

        return priorities[name]
    
    def resolve_conflict(ts:list):
        # Check to see if there's a multivalue we need to handle
        mv = False
        for i in ts:
            if isinstance(i, HqlTypes.multivalue):
                mv = True
                break
        
        # Handle multivalue
        if mv:
            inner_set = set()
            for i in ts:
                if isinstance(i, HqlTypes.multivalue):
                    inner_set.add(i.inner)
                else:
                    inner_set.add(i)
            inner = HqlTypes.resolve_conflict(list(inner_set))
            return HqlTypes.multivalue(inner)

        l = HqlTypes.priority_by_name('null')
        for i in [str(x) for x in ts]:
            r = HqlTypes.priority_by_name(i)
            if l['priority'] > r['priority']:
                continue

            if r['name'] in l['super']:
                l = r
                continue

        return HqlTypes.type_by_name(l['name'])

    # Gets the appropriate Hql type for a particular piece of data
    def to_hql_type(proto):
        prototype = type(proto)

        if prototype == dict:
            return prototype
        elif prototype in (list, tuple):
            inner = HqlTypes.resolve_conflict([HqlTypes.to_hql_type(x) for x in proto])
            return HqlTypes.multivalue(inner)
        elif prototype == str:
            return HqlTypes.string()
        elif prototype == int:
            return HqlTypes.int()
        elif prototype == float:
            return HqlTypes.float()
        elif prototype == bool:
            return HqlTypes.bool()
        elif prototype == type(None):
            return HqlTypes.null()
        else:
            logging.error(f'Unhandled conversion type {prototype}')

    def cast(src:pl.Series, target:type):
        pass

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
        
    class object(pl.Struct):
        def pl_schema(self):
            return pl.Struct
        
    class null(pl.Null):
        def pl_schema(self):
            return pl.Null()
        
    class unknown(pl.Unknown):
        def pl_schema(self):
            return pl.Unknown()
        
    class multivalue(pl.List):
        def pl_schema(self):
            if isinstance(self.inner, type(self)):
                return pl.List(self.inner.pl_schema())
            else:
                return pl.List(self.inner().pl_schema())