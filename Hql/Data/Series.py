import polars as pl
from Hql.Types.Hql import HqlTypes as hqlt
from Hql.Types.Polars import PolarsTypes as plt
from typing import Union

'''
Series for individual values, mimics a pl.Series
'''
class Series():
    def __init__(self, series:pl.Series, stype:Union[hqlt.HqlType, None]=None):
        if stype == None:
            ptype = series.dtype
            stype = plt.from_pure_polars(ptype)
        
        self.series = series
        self.type = stype

    def __bool__(self)-> bool:
        if isinstance(self.series, type(None)):
            return False
        return True
