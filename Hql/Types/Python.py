from typing import Optional
from Hql.Context import register_type, get_type
from Hql.Types.Compiler import CompilerType

class PythonTypes():
    from Hql.Types.Hql import HqlTypes as hqlt

    class PythonType(CompilerType):
        def __init__(self, inner:Optional['PythonTypes.PythonType']=None):
            CompilerType.__init__(self, inner=inner)

            self.priority = 0
            self.super = []

        def __len__(self):
            return 1
        
    @staticmethod
    def from_name(name:str):
        return get_type(f'python_{name}')

    @staticmethod
    def from_value(value) -> 'PythonTypes.PythonType':
        if isinstance(value, dict):
            new = dict()
            for i in value:
                new[i] = PythonTypes.from_value(value[i])
            return PythonTypes.dict(new)
        else:
            return PythonTypes.from_name(type(value).__name__)

    @staticmethod
    def resolve_conflict(types:list[PythonType]):
        if len(types) == 1:
            return types[0]
        
        # Check to see if there's a multivalue we need to handle
        mv = False
        for i in types:
            if isinstance(i, PythonTypes.list):
                mv = True
                break
        
        # Handle multivalue
        if mv:
            inner_set = set()
            for i in types:
                if isinstance(i, PythonTypes.list):
                    inner_set.add(i.inner)
                else:
                    inner_set.add(i)
            types = list(inner_set)

        # set to default basecase
        l = PythonTypes.NoneType()
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
            return PythonTypes.list(l)
        else:
            return l

    @staticmethod
    def resolve_mv(mv:list[type]):
        mvset = set()
        for i in mv:
            mvset.add(PythonTypes.from_name(i.__name__))
        return PythonTypes.resolve_conflict(list(mvset))
            
    @register_type('python_int')
    class int(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            self.HqlType = PythonTypes.hqlt.int()
            
            self.priority = 2
            self.super = (PythonTypes.float, PythonTypes.str, PythonTypes.list) 

    @register_type('python_float')
    class float(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            self.HqlType = PythonTypes.hqlt.float()
            
            self.priority = 3
            self.super = (PythonTypes.str, PythonTypes.list)

    @register_type('python_complex') 
    class complex(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            self.HqlType = PythonTypes.hqlt.string()
        
    @register_type('python_str')
    class str(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            self.HqlType = PythonTypes.hqlt.string()
 
            self.priority = 4
            self.super = [PythonTypes.list]

    @register_type('python_bytes')
    class bytes(PythonType, hqlt.binary):
        ...
    
    @register_type('python_bool') 
    class bool(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            self.HqlType = PythonTypes.hqlt.bool()
                        
            self.priority = 1
            self.super = (PythonTypes.int, PythonTypes.str, PythonTypes.list)
        
    @register_type('python_NoneType')
    class NoneType(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            self.HqlType = PythonTypes.hqlt.null()
                        
            self.priority = 0
            self.super = (PythonTypes.bool, PythonTypes.int, PythonTypes.float, PythonTypes.str, PythonTypes.list)

    @register_type('python_list')
    class list(PythonType):
        def __init__(self, inner:'PythonTypes.PythonType'):
            PythonTypes.PythonType.__init__(self, inner=inner)
            self.inner = inner
            self.HqlType = PythonTypes.hqlt.multivalue(inner.hql_schema())
            
            self.priority = 5
            self.super = []

    @register_type('python_dict')
    class dict(PythonType):
        def __init__(self, schema:dict):
            PythonTypes.PythonType.__init__(self)
            self.schema = schema
            self.HqlType = PythonTypes.hqlt.object(schema)

        def __getitem__(self, key:str):
            if isinstance(self.schema[key], dict):
                return PythonTypes.dict(self.schema[key])
            else:
                return self.schema[key]

        def __eq__(self, value: object, /) -> bool:
            if not isinstance(value, PythonTypes.dict):
                return False
            return PythonTypes.hqlt.object.eq(self.schema, value.schema)

        def hql_schema(self) -> 'PythonTypes.hqlt.HqlType':
            new = dict()
            for i in self.schema:
                new[i] = self[i].hql_schema()
            return PythonTypes.hqlt.object(new)

        def pl_schema(self):
            return self.hql_schema().pl_schema()
