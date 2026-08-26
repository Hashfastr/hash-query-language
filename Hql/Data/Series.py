from __future__ import annotations
from typing import TYPE_CHECKING, Union, Optional

if TYPE_CHECKING:
    from Hql.Types.Hql import HqlTypes as hqlt
    import polars as pl

'''
Series for individual values, mimics a pl.Series
'''
class Series():
    """Pair a Polars series with its corresponding HQL type."""

    def __init__(self, series:pl.Series, stype:Union[hqlt.HqlType, None]=None):
        from Hql.Types.Polars import PolarsTypes as plt

        if stype == None:
            ptype = series.dtype
            stype = plt.from_pure_polars(ptype).HqlType
        
        self.series = series
        assert stype
        self.type = stype

    def __bool__(self)-> bool:
        if isinstance(self.series, type(None)):
            return False
        return True

    def cast(self, target:Optional[hqlt.HqlType]=None):
        if not target:
            target = self.type
        self.series = target.cast(self.series)
        self.type = target
        return self
