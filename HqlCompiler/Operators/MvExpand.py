from HqlCompiler.Data import Data, Table
from HqlCompiler.Expressions import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Types.Hql import HqlTypes as hqlt

@register_op('MvExpand')
class MvExpand(Operator):
    def __init__(self, to_exprs:list[Expression], limit:Expression):
        Operator.__init__(self)
        self.to_exprs = to_exprs
        self.limit = limit
        
    def explode_table(self, ctx:Context, table:Table):
        schema = table.schema
        df = table.df

        for to in self.to_exprs:
            path = to.expr.eval(ctx, as_list=True)
            pl_expr = to.expr.eval(ctx, as_pl=True)

            # Short circuit case
            if not isinstance(schema.get_type(path).schema, hqlt.multivalue):
                continue
            
            new_type = schema.get_type(path).schema.inner
            df = df.with_columns(
                pl_expr.list.slice(0, self.limit)
            ).explode(pl_expr)

            if to.to:
                new_type = to.to
                        
            schema.set(path, new_type)
            
        return Table(df=df, schema=schema, name=table.name)

    def eval(self, ctx:Context, **kwargs):
        # Long literal, just get us the number
        self.limit = self.limit.eval(ctx)

        new = []
        for table in ctx.data:
            new.append(self.explode_table(ctx, table))
        
        return Data(tables=new)