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
        data = self.by_expr.eval(ctx)
        for table in data.tables:
            df = data.tables[table].df
            print(df)
        
        return Data()