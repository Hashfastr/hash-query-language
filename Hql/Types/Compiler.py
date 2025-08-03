from typing import Union
from Hql.Exceptions import HqlExceptions as hqle

class CompilerType():
    def __init__(self, base:type, inner:Union[None, type]=None):
        bases = type(self).__bases__

        self.type = bases[0]
        self.HqlType = base
        self.inner = inner
        self.name = self.__class__.__name__
    
    def hql_schema(self):
        if self.HqlType == None:
            raise hqle.CompilerException(f"{self.type}.{self.name} defined without an Hql proto")

        if self.inner:
            return self.HqlType(self.inner)

        return self.HqlType()

    def __len__(self):
        return 1

