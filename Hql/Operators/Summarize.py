from __future__ import annotations
from typing import TYPE_CHECKING, Sequence
from Hql.Operators.Operator import Operator

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Expressions.Aggregation import ByExpression
    from Hql.Context import Context

class Summarize(Operator):
    def __init__(self, aggregate_exprs:Sequence[Expression], by_expr:ByExpression):
        Operator.__init__(self)
        self.aggregate_exprs = aggregate_exprs
        self.by_expr = by_expr

    def deparse(self) -> str:
        out = 'summarize'

        if self.aggregate_exprs:
            out += ' ' + ', '.join(i.deparse() for i in self.aggregate_exprs)

        if self.by_expr:
            out += ' ' + self.by_expr.deparse()

        return out

    def eval(self, ctx:Context) -> Context:
        from Hql.Data import Data, Table

        ctx = self.by_expr.eval(ctx)

        agg_data = []
        for expr in self.aggregate_exprs:
            agg_data.append(expr.eval(ctx, insert=False))

        new = []
        for table in ctx.data:
            table = Table(table.agg.agg(), schema=table.agg_schema, name=table.name)
            new.append(table)

        ctx.data = Data.merge([Data(tables=new)] + agg_data)
        return ctx
