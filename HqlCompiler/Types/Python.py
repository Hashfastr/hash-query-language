import logging

from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_type, get_type
from HqlCompiler.Types.Hql import HqlTypes as Hql
# from HqlCompiler.Types.Compiler import CompilerType


class PythonTypes():
    class PythonType():
        def __init__(self):
            if len(type(self).__bases__):
                super().__init__()
                self.HqlType = type(self).__bases__[-1]
            else:
                self.HqlType = None
        
        def hql_schema(self):
            return self.HqlType
        
    def from_name(name:str):
        return get_type(f'python_{name}')
            
    @register_type('python_int')
    class int(int, PythonType, Hql.int):
        ...

    @register_type('python_float')
    class float(float, PythonType, Hql.float):
        ...
    
    @register_type('python_complex') 
    class complex(complex, PythonType, Hql.string):
        ...
        
    @register_type('python_str')
    class str(str, PythonType, Hql.string):
        ...

    @register_type('python_bytes')
    class bytes(bytes, PythonType, Hql.binary):
        ...
    
    @register_type('python_bool') 
    class bool(PythonType, Hql.bool):
        ...
        
    @register_type('python_None')
    class NoneType(PythonType, Hql.null):
        ...