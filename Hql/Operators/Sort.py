from Hql.Operators import Operator
from Hql.Context import register_op, Context
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import OrderedExpression


# @register_op('Sort')
# @register_op('Order')
class Sort(Operator):
    def __init__(self, exprs:list['OrderedExpression']):
        Operator.__init__(self)
        self.exprs = exprs

    def decompile(self, ctx: 'Context') -> str:
        out = 'sort by '

        exprs = []
        for i in self.exprs:
            exprs.append(i.decompile(ctx))
        out += ', '.join(exprs)
        
        return out

    def eval(self, ctx:'Context', **kwargs):
        exprs = []
        orders = []
        nulls = []
        for expr in self.exprs:
            assert expr.expr
            exprs.append(expr.expr.eval(ctx, as_pl=True))
            orders.append(expr.order == 'desc')
            nulls.append(expr.nulls == 'last')

        for table in ctx.data:
            table.sort(exprs, orders, nulls)
        
        return ctx.data
