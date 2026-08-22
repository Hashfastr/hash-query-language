from __future__ import annotations
from . import Function
from Hql.Context import register_func
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Hql.Context import Context
    from polars import Expr as plExpr

@register_func('not')
class hqlnot(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions import Expression
        Function.__init__(self, args, 1, 1)
        self.expr:Expression = args[0]
        self.logic = True
        
    def preprocess(self, ctx: Context, receiver=None) -> object:
        from Hql.Expressions.Logic import Not, Logic
        from Hql.Expressions.References import Reference

        expr = self.expr.preprocess(ctx)

        if isinstance(expr, Function) and expr.can_preprocess:
            expr = self.expr.preprocess(ctx)
        assert isinstance(expr, (Logic, Reference, Function))

        return Not(expr)
