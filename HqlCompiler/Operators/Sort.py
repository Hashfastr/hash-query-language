from HqlCompiler.Data import Data, Table
from HqlCompiler.Expression import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op, Context

@register_op('Sort')
@register_op('Order')
class Sort(Operator):
    def __init__(self, exprs:list[Expression]):
        Operator.__init__(self)
        self.exprs = exprs

    def eval(self, ctx:Context, **kwargs):
        exprs = []
        orders = []
        nulls = []
        for expr in self.exprs:
            exprs.append(expr.expr.eval(ctx, as_pl=True))
            
            if expr.order == 'desc':
                orders.append(True)
            else:
                orders.append(False)
                
            if expr.nulls == 'last':
                nulls.append(True)
            else:
                nulls.append(False)

        for table in ctx.data:
            table.sort(exprs, orders, nulls)
        
        return ctx.data
