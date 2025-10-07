from typing import TYPE_CHECKING
from Hql.Expressions import Expression
from Hql.Data import Schema, Data, Table
from Hql.Context import register_op, Context
from Hql.Operators import Operator

if TYPE_CHECKING:
    from Hql.Expressions import ByExpression

# @register_op('Summarize')
class Summarize(Operator):
    def __init__(self, aggregate_exprs:list[Expression], by_expr:'ByExpression'):
        Operator.__init__(self)
        self.aggregate_exprs = aggregate_exprs
        self.by_expr = by_expr

    def decompile(self, ctx: 'Context') -> str:
        out = 'summarize'

        if self.aggregate_exprs:
            out += ' '
            exprs = []
            for i in self.aggregate_exprs:
                exprs.append(i.decompile(ctx))
            out += ', '.join(exprs)

        if self.by_expr:
            out += ' '
            out += self.by_expr.decompile(ctx)

        return out

    def eval(self, ctx:'Context', **kwargs):
        ctx.data = self.by_expr.eval(ctx)
        
        agg_data = []
        for expr in self.aggregate_exprs:
            agg_data.append(expr.eval(ctx, insert=False))
        
        new = []
        for table in ctx.data:
            table = Table(table.agg.agg(), schema=table.agg_schema, name=table.name)
            new.append(table)
            
        new = Data(tables=new)
        
        return Data.merge([new] + agg_data)
