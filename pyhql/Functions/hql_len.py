from . import Function
from Hql.Context import register_func, Context
from Hql.Data import Data, Table, Schema
from Hql.Types.Hql import HqlTypes as hqlt

import logging

@register_func('len')
@register_func('array_length')
class hql_len(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1)
        self.args = args
        self.count_type = hqlt.ulong()
        
    def eval(self, ctx:'Context', **kwargs):
        path = self.args[0].eval(ctx, as_list=True)
        filter = self.args[0].eval(ctx, as_pl=True)
        
        new = []
        for table in ctx.data:            
            if not table.assert_field(path):
                new.append(Table(name=table.name))
                continue
            
            if not isinstance(table.schema.get_type(path).schema, hqlt.multivalue):
                logging.warning(f"Skipping over evaluating length of {'.'.join(path)} in {table.name}")
                new.append(Table(name=table.name))
                continue
            
            count = table.df.with_columns(filter.list.len())
            schema = Schema().set(path, self.count_type)
            
            new.append(Table(df=count, schema=Schema(schema=schema), name=table.name))
            
        return Data(tables=new)
