from HqlCompiler.Expression import Expression
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator

@register_op('Summarize')
class Summarize(Operator):
    def __init__(self, aggregate_exprs:list[Expression], by_expr:Expression):
        super().__init__()
        self.aggregate_exprs = aggregate_exprs
        self.by_expr = by_expr

    def eval(self, ctx:Context, **kwargs):
        ctx.data = self.by_expr.eval(ctx)
        
        agg_data = []
        for expr in self.aggregate_exprs:
            agg_data.append(expr.eval(ctx, insert=False))
        
        new = []
        for table in ctx.data:
            table = Table(table.agg.agg(), schema=table.agg_schema, name=table.name)
            new.append(table)
            
        new = Data(tables_list=new)
        
        return Data.merge([new] + agg_data)