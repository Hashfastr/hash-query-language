from __future__ import annotations

from . import Function
from Hql.Context import register_func
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Context import Context
    import polars as pl

@register_func('isnotempty')
class isnotempty(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        # allows 1 to infinity args
        Function.__init__(self, args, 1, -1)

    def gen_filter(self, ctx:Context) -> pl.Expr:
        expr:pl.Expr = pl.lit(True)

        for i in self.args:
            cur = i.polars().is_null().not_()
            expr = expr.and_(cur)

        return expr
        
    def eval(self, ctx: Context, receiver=None) -> object:
        return self.gen_filter(ctx)
