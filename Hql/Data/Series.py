import polars as pl
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from Hql.Types.Hql import HqlTypes as hqlt

'''
Series for individual values, mimics a pl.Series
'''
class Series():
    def __init__(self, series:pl.Series, stype:Union['hqlt.HqlType', None]=None):
        from Hql.Types.Polars import PolarsTypes as plt

        if stype == None:
            ptype = series.dtype
            stype = plt.from_pure_polars(ptype).HqlType
        
        self.series = series
        self.type = stype

    def __bool__(self)-> bool:
        if isinstance(self.series, type(None)):
            return False
        return True

    def cast(self, target:"hqlt.HqlType"):
        self.series = target.cast(self.series)
        self.type = target
        return self
