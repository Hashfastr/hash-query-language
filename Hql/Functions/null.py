from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Expressions import Expression

import logging
import polars as pl
from typing import Optional

@register_func('isnull')
class isnull(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        Function.__init__(self, args, 1, 1)
        self.expr:Expression = args[0]
        
    def eval(self, ctx:'Context', **kwargs):
        expr = self.expr.eval(ctx, as_pl=True)
        assert isinstance(expr, pl.Expr)
        return expr.is_null()
