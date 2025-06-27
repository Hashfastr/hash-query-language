import polars as pl
from HqlCompiler.Types.Hql import HqlTypes as hqlt

'''
Series for individual values, mimics a pl.Series
'''
class Series():
    def __init__(self, series:pl.Series, stype:hqlt.HqlType):
        self.series = series
        self.type = stype