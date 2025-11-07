from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema
import polars as pl

import logging
from typing import Optional

@register_func('tolower')
class tolower(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        Function.__init__(self, args, 1, 1, conf)
        self.src = args[0]

        if self.src.literal:
            self.src = pl.Series([self.src.value]).str.to_lowercase()
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Expressions import StringLiteral
        from Hql.Types.Hql import HqlTypes as hqlt
        
        if isinstance(self.src, pl.Series):
            new = self.src.str.to_lowercase()
            return StringLiteral(new[0])

        path = self.src.eval(ctx, as_list=True)
        data = ctx.data.select(path).strip()
        
        tables = []
        for table in data:
            if not table.series:
                continue

            series = table.series.series.str.to_lowercase()

            new = Table(name=table.name)
            new.insert(path, series, hqlt.string())
            tables.append(new)

        return Data(tables=tables)
