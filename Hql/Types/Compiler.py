from typing import Union, Optional, TYPE_CHECKING
import polars as pl
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Types.Hql import HqlTypes as hqlt

class CompilerType():
    def __init__(self, inner:Optional['CompilerType']=None):
        bases = type(self).__bases__

        self.type = bases[0]
        self.HqlType:Optional['hqlt.HqlType'] = None
        self.inner = inner
        self.name = self.__class__.__name__
    
    def hql_schema(self) -> 'hqlt.HqlType':
        if self.HqlType == None:
            raise hqle.CompilerException(f"{self.type}.{self.name} defined without an Hql proto")

        if self.inner:
            self.HqlType.inner = self.inner.hql_schema()

        return self.HqlType

    def pl_schema(self):
        return self.hql_schema().pl_schema()

    def cast(self, series:pl.Series):
        if self.HqlType == None:
            raise hqle.CompilerException('Attempting to cast data to type without a prototype')

        return series.cast(self.pl_schema())

    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name
        }

    def deparse(self):
        return self.name

    def str(self):
        return self.name

    def __len__(self) -> int:
        return 1
