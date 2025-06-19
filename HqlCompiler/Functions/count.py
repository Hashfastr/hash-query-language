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
        
    def eval(self, ctx:Context, **kwargs):
        tables = []
        for i in ctx.data.tables:
            table = ctx.data.tables[i]
            if not table.aggregation:
                tables.append(table)
                
            agg = table.aggregation
            
            # Unsure if this is a performant solution
            # Does .agg compute? or does it just output what already has?
            i = 0
            while self.count_name in agg.agg():
                i += 1
            if i > 0:
                self.count_name = f'{self.count_name}{i}'
            
            df = agg.len(name=self.count_name)
            
            new = Table(df=df, schema=table.agg_schema, name=table.name)
            tables.append(new)
        
        return Data(tables_list=tables)