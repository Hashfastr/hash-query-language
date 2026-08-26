from __future__ import annotations
from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func

import polars as pl
from typing import Optional

@register_func('isnull')
class isnull(Function):
    """Build a predicate that tests a referenced field for null."""

    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions.References import Reference
        Function.__init__(self, args, 1, 1)

        expr = args[0]
        if not isinstance(expr, Reference):
            hqle.ArgumentException(f'Invalid argument type to isnull: {type(expr)}')
        self.expr:Reference = expr

        self.logic = True

    def polars(self) -> pl.Expr:
        expr = self.expr.polars()
        return expr.is_null()
