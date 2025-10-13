from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Context import Context

import logging
import polars as pl

@register_func('isnotempty')
class isnotempty(Function):
    def __init__(self, args:list):
        # allows 1 to infinity args
        Function.__init__(self, args, 1, -1)

    def gen_filter(self, ctx:'Context') -> pl.Expr:
        expr:Optional[pl.Expr] = None

        for i in self.args:
            cur = i.eval(ctx, as_pl=True)
            assert isinstance(cur, pl.Expr)
            cur = cur.is_null().not_()

            if isinstance(expr, type(None)):
                expr = cur
            else:
                expr = expr.and_(cur)

        assert isinstance(expr, pl.Expr)
        return expr
        
    def eval(self, ctx:'Context', **kwargs):
        return self.gen_filter(ctx)
