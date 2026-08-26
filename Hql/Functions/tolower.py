from __future__ import annotations
from . import Function
from Hql.Context import register_func

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Hql.Context import Context

@register_func('tolower')
class tolower(Function):
    """Convert string literals or field values to lowercase."""

    def __init__(self, args:list, conf:Optional[dict]=None):
        import polars as pl
        Function.__init__(self, args, 1, 1, conf)
        self.src = args[0]

        if self.src.literal:
            self.src = pl.Series([self.src.value]).str.to_lowercase()
        
    def eval(self, ctx: Context, receiver=None) -> object:
        import polars as pl
        from Hql.Data import Data, Table
        from Hql.Expressions.Literals import StringLiteral
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
