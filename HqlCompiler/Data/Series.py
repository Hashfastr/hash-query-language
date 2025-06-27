import polars as pl
from HqlCompiler.Types.Hql import HqlTypes as hqlt
from HqlCompiler.Types.Polars import PolarsTypes as plt

'''
Series for individual values, mimics a pl.Series
'''
class Series():
    def __init__(self, series:pl.Series=None, stype:hqlt.HqlType=None):
        if stype == None and not isinstance(series, type(None)):
            ptype = series.dtype
            stype = plt.from_pure_polars(ptype)
        
        self.series = series
        self.type = stype

    def __bool__(self)-> bool:
        if isinstance(self.series, type(None)):
            return False
        return True
