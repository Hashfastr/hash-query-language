import logging

from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_type, get_type
from HqlCompiler.Types.Hql import HqlTypes as Hql
# from HqlCompiler.Types.Compiler import CompilerType


class PythonTypes():
    class PythonType():
        def __init__(self):
            if len(type(self).__bases__):
                self.HqlType = type(self).__bases__[-1]
            else:
                self.HqlType = None
        
        def hql_schema(self):
            return self.HqlType()
        
        def pl_schema(self):
            return self.hql_schema().pl_schema()
    
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
    
    def resolve_mv(mv:list):
        mvset = set()
        for i in mv:
            if isinstance(i, list):
                mvset.add(PythonTypes.list(PythonTypes.resolve_mv(i)))
                
            else:
                mvset.add(PythonTypes.from_name(type(i).__name__))
                
        return PythonTypes.resolve_conflict(list(mvset))
    
    def from_name(name:str):
        return get_type(f'python_{name}')
            
    @register_type('python_int')
    class int(PythonType, Hql.int):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            Hql.int.__init__(self)
            
            self.priority = 2
            self.super = (PythonTypes.float, PythonTypes.str, PythonTypes.list) 

    @register_type('python_float')
    class float(PythonType, Hql.float):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            Hql.float.__init__(self)
            
            self.priority = 3
            self.super = (PythonTypes.str, PythonTypes.list)
    @register_type('python_complex') 
    class complex(PythonType, Hql.string):
        ...
        
    @register_type('python_str')
    class str(PythonType, Hql.string):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            Hql.string.__init__(self)
            
            self.priority = 4
            self.super = (PythonTypes.list)

    @register_type('python_bytes')
    class bytes(PythonType, Hql.binary):
        ...
    
    @register_type('python_bool') 
    class bool(PythonType, Hql.bool):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            Hql.bool.__init__(self)
            
            self.priority = 1
            self.super = (PythonTypes.int, PythonTypes.str, PythonTypes.list)
        
    @register_type('python_NoneType')
    class NoneType(PythonType, Hql.null):
        def __init__(self):
            PythonTypes.PythonType.__init__(self)
            Hql.null.__init__(self)
            
            self.priority = 0
            self.super = (PythonTypes.bool, PythonTypes.int, PythonTypes.float, PythonTypes.str, PythonTypes.list)

    @register_type('python_list')
    class list(PythonType, Hql.multivalue):
        def __init__(self, inner):
            PythonTypes.PythonType.__init__(self)
            Hql.multivalue.__init__(self, inner)
            
            self.priority = 5
            self.super = ()
        
        def hql_schema(self):
            return self.HqlType(self.inner)

    @register_type('dict')
    class dict(PythonType, Hql.object):
        def __init__(self, keys:list[str]):
            PythonTypes.PythonType.__init__(self)
            Hql.object.__init__(self, keys)
            self.keys = keys
            
        def hql_schema(self):
            return self.HqlType(self.keys)