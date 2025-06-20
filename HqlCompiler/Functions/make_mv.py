from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from .__proto__ import Function
from HqlCompiler.Data import Data, Series, Table, Schema
from HqlCompiler.Types.Hql import HqlTypes as hqlt

@register_func('make_list')
@register_func('make_mv')
class make_mv(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, -1)
        self.args = args
    
    def gen_schema(self, schema:Schema, paths:list[str]):
        schema = schema.select_many(paths)
        
        new = Schema()
        for path in paths:
            t = schema.select(path).strip()
            t = hqlt.multivalue(t)
            new.set(path, t)

        return new
        
    def eval(self, ctx:Context, **kwargs):
        cols = []
        paths = []
        for arg in self.args:
            cols.append(arg.eval(ctx, as_pl=True))
            paths.append(arg.eval(ctx, as_list=True))
            
        new = []
        for name in ctx.data.tables:
            table = ctx.data.tables[name]
                        
            df = table.agg.agg(cols)
                        
            # Drop the aggregation fields as they can be added back later
            # Such as with a summarize
            df = df.drop(table.agg_cols)
            schema = self.gen_schema(table.schema, paths)
            
            new.append(Table(df=df, schema=schema, name=table.name))
        
        return Data(tables_list=new)