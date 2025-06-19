from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from .__proto__ import Function
from HqlCompiler.Data import Data, Series, Table, Schema

@register_func('count')
class count(Function):
    def __init__(self, args:list):
        super().__init__(args, 0, 0)
        self.aggregate = True
        self.count_name = 'count_'
        
    def get_count_name(self, agg):
        name = self.count_name
        
        # Unsure if this is a performant solution
        # Does .agg compute? or does it just output what already has?
        i = 0
        while name in agg.agg():
            i += 1
            
        if i > 0:
            name = f'{name}{i}'
            
        return name
        
    def eval(self, ctx:Context, **kwargs):
        tables = []
        for name in ctx.data.tables:
            table = ctx.data.tables[name]
            if not table.agg:
                tables.append(table)
                
            cname = self.get_count_name(table.agg)

            df = table.agg.len(name=cname)
            df = df.drop(table.agg_cols)
            
            new = Table(df=df, name=table.name)
            tables.append(new)
        
        return Data(tables_list=tables)