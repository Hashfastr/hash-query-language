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

    # src defined here but not implemented, yet....
    # Target and src should be HqlType, can't definite it in the params for
    # some reason, hate python scoping sometimes.
    def cast(data:pl.Series, target, src=None):
        if not isinstance(data, pl.Series):
            raise CompilerException(f'Attempting to cast data of type {type(data)} to {target}')

    class HqlType():
        def __init__(self):
            # Only init if it's a subclass
            if len(type(self).__bases__):
                super().__init__()
                self.proto = type(self).__bases__[-1]
            else:
                self.proto = None

        def pl_schema(self):
            return self.proto

        def cast(self, data:pl.Series):
            return data.cast(self.proto)

    class decimal(HqlType, pl.Decimal):
        ...
        
    class float(HqlType, pl.Float32):
        ...

    class double(HqlType, pl.Float64):
        ...
        
    class byte(HqlType, pl.Int8):
        ...

    class short(HqlType, pl.Int16):
        ...

    class int(HqlType, pl.Int32):
        ...
        
    class long(HqlType, pl.Int64):
        ...

    class xlong(HqlType, pl.Int128):
        ...

    class guid(HqlType, pl.Int128):
        ...
        
    class ubyte(HqlType, pl.UInt8):
        ...
        
    class ushort(HqlType, pl.UInt16):
        ...
        
    class uint(HqlType, pl.UInt32):
        ...
        
    class ulong(HqlType, pl.UInt64):
        ...

    class ip(HqlType, pl.String):
        ...

    class ip4(HqlType, pl.UInt32):
        ...

    class ip6(HqlType, pl.Int128):
        ...
            
    class datetime(HqlType, pl.Datetime):
        ...
        
    class duration(HqlType, pl.Duration):
        ...
            
    class time(HqlType, pl.Time):
        ...

    class range(HqlType, pl.Struct):
        def __init__(self, start, end):
            super().__init__()

            self.start = start
            # self.start_clusivity = 'gt' if start_clusivity == 'gt' else 'gte'
            self.end = end
            # self.end_clusivity = 'lt' if end_clusivity == 'lt' else 'lte'

        def pl_schema(self):
            return self.__class__.__bases__[0].__init__({'start': self.start, 'end': self.end})
            
    class matrix(HqlType, pl.Array):
        ...
        
    class string(HqlType, pl.String):
        ...
            
    class enum(HqlType, pl.Enum):
        ...
            
    class binary(HqlType, pl.Binary):
        ...
        
    class bool(HqlType, pl.Boolean):
        ...
    
    '''
    This is a generic object, unspecified the contents
    '''
    class object(HqlType, pl.Struct):
        def __init__(self, fields:list[str]):
            pl.Struct.__init__(self, fields)
            self.proto = pl.Struct

    class null(HqlType, pl.Null):
        ...
        
    class unknown(HqlType, pl.Unknown):
        ...
        
    class multivalue(pl.List):
        def pl_schema(self):
            if isinstance(self.inner, type(self)):
                return pl.List(self.inner.pl_schema())
            else:
                return pl.List(self.inner().pl_schema())