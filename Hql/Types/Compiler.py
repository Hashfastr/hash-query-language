from typing import Union
import polars as pl
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

    def pl_schema(self):
        return self.hql_schema().pl_schema()

    def cast(self, series:pl.Series):
        if self.HqlType == None:
            raise hqle.CompilerException('Attempting to cast data to type without a prototype')

        return series.cast(self.pl_schema())

    def __len__(self):
        return 1

