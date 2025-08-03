from typing import Union
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_type, get_type
from Hql.Types.Hql import HqlTypes as hqlt
from Hql.Types.Compiler import CompilerType

class PythonTypes():
    class PythonType(CompilerType):
        def __init__(self, base:type, inner:Union[None, type]=None):
            CompilerType.__init__(self, base, inner=inner)

            self.priority = 0
            self.super = ()
        
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
    class int(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self, hqlt.int)
                        
            self.priority = 2
            self.super = (PythonTypes.float, PythonTypes.str, PythonTypes.list) 

    @register_type('python_float')
    class float(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self, hqlt.float)
            
            self.priority = 3
            self.super = (PythonTypes.str, PythonTypes.list)

    @register_type('python_complex') 
    class complex(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self, hqlt.string)
        
    @register_type('python_str')
    class str(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self, hqlt.string)
 
            self.priority = 4
            self.super = (PythonTypes.list)

    @register_type('python_bytes')
    class bytes(PythonType, hqlt.binary):
        ...
    
    @register_type('python_bool') 
    class bool(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self, hqlt.bool)
                        
            self.priority = 1
            self.super = (PythonTypes.int, PythonTypes.str, PythonTypes.list)
        
    @register_type('python_NoneType')
    class NoneType(PythonType):
        def __init__(self):
            PythonTypes.PythonType.__init__(self, hqlt.null)
                        
            self.priority = 0
            self.super = (PythonTypes.bool, PythonTypes.int, PythonTypes.float, PythonTypes.str, PythonTypes.list)

    @register_type('python_list')
    class list(PythonType):
        def __init__(self, inner):
            PythonTypes.PythonType.__init__(self, hqlt.multivalue, inner=inner)

            self.HqlType = hqlt.multivalue
            
            self.priority = 5
            self.super = ()

    @register_type('python_dict')
    class dict(PythonType):
        def __init__(self, keys:list[str]):
            raise hqle.CompilerException('Unimplemented python type object')

            PythonTypes.PythonType.__init__(self, hqlt.object)
            self.keys = keys
            
        #def hql_schema(self):
        #    return self.hql_schema()(self.keys)
