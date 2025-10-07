from . import Function
from Hql.Context import register_func, Context
from Hql.Data import Data, Table
from Hql.Types.Hql import HqlTypes as hqlt

@register_func('count')
class count(Function):
    def __init__(self, args:list, name:str='count_'):
        super().__init__(args, 0, 0)
        self.count_name = name
        self.count_type = hqlt.uint()
        
    def get_count_name(self, agg):
        name = self.count_name
        
        # Unsure if this is a performant solution
        # Does .agg compute? or does it just output what already has?
        i = 0
        while name in agg.agg():
            i += 1
            name = f'{name}{i}'
            
        return name
        
    def eval(self, ctx:'Context', **kwargs):
        tables = []
        for table in ctx.data:
            if not table.agg:
                tables.append(table)
                continue
            
            cname = self.get_count_name(table.agg)
            
            df = table.agg.len(name=cname)
            schema = table.agg_schema.copy().set([cname], self.count_type)
            new = Table(df=df, schema=schema, name=table.name)
            new = new.drop_many(table.agg_paths)
                        
            tables.append(new)
        
        return Data(tables=tables)
