from ..Exceptions import *
from ..Context import register_type, get_type
from .Hql import HqlTypes as hqlt

class PythonTypes():
    class PythonType():
        def __init__(self):
            if len(type(self).__bases__):
                self.HqlType = type(self).__bases__[-1]
            else:
                self.HqlType = hqlt.null

            self.priority = 0
            self.super = ()
        
        def hql_schema(self):
            return self.HqlType()
        
        def pl_schema(self):
            return self.hql_schema().pl_schema()

        def __len__(self):
            return 1
        
    @staticmethod
    def from_name(name:str):
        return get_type(f'python_{name}')

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
    def resolve_mv(mv:list):
        mvset = set()
        for i in mv:
            if isinstance(i, list):
                mvset.add(PythonTypes.list(PythonTypes.resolve_mv(i)))
                
            else:
                mvset.add(PythonTypes.from_name(type(i).__name__))
                
        return PythonTypes.resolve_conflict(list(mvset))
            
    @register_type('python_int')
    class int(PythonType, hqlt.int):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            hqlt.int.__init__(self)
            
            self.priority = 2
            self.super = (PythonTypes.float, PythonTypes.str, PythonTypes.list) 

    @register_type('python_float')
    class float(PythonType, hqlt.float):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            hqlt.float.__init__(self)
            
            self.priority = 3
            self.super = (PythonTypes.str, PythonTypes.list)

    @register_type('python_complex') 
    class complex(PythonType, hqlt.string):
        ...
        
    @register_type('python_str')
    class str(PythonType, hqlt.string):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            hqlt.string.__init__(self)
            
            self.priority = 4
            self.super = (PythonTypes.list)

    @register_type('python_bytes')
    class bytes(PythonType, hqlt.binary):
        ...
    
    @register_type('python_bool') 
    class bool(PythonType, hqlt.bool):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            hqlt.bool.__init__(self)
            
            self.priority = 1
            self.super = (PythonTypes.int, PythonTypes.str, PythonTypes.list)
        
    @register_type('python_NoneType')
    class NoneType(PythonType, hqlt.null):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            hqlt.null.__init__(self)
            
            self.priority = 0
            self.super = (PythonTypes.bool, PythonTypes.int, PythonTypes.float, PythonTypes.str, PythonTypes.list)

    @register_type('python_list')
    class list(PythonType, hqlt.multivalue):
        def __init__(self, inner):
            PythonTypes.PythonType.__init__(self)
            hqlt.multivalue.__init__(self, inner)

            self.HqlType = hqlt.multivalue
            
            self.priority = 5
            self.super = ()
        
        def hql_schema(self):
            return self.HqlType(self.inner)

    @register_type('python_dict')
    class dict(PythonType, hqlt.object):
        def __init__(self, keys:list[str]):
            PythonTypes.PythonType.__init__(self)
            hqlt.object.__init__(self, keys)
            
            self.HqlType = hqlt.object
            self.keys = keys
            
        def hql_schema(self):
            return self.HqlType(self.keys)
