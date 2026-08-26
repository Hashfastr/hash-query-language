from __future__ import annotations
from . import Function
from Hql.Context import register_func, Context
from Hql.Data import Data, Table
from Hql.Types.Hql import HqlTypes as hqlt
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Hql.Expressions.References import Reference

@register_func('count')
class count(Function):
    """Count rows within each active aggregation group."""

    def __init__(self, args:list, name:str='count_', conf:Optional[dict]=None):
        super().__init__(args, 0, 0)
        self.count_name = name
        self.count_type = hqlt.uint()
        
    def get_count_name(self, agg) -> Reference:
        from Hql.Expressions.References import NamedReference
        name = self.count_name
        
        # Unsure if this is a performant solution
        # Does .agg compute? or does it just output what already has?
        i = 0
        while name in agg.agg():
            i += 1
            name = f'{name}{i}'
            
        return NamedReference(name)
        
    def eval(self, ctx: Context, receiver=None) -> object:
        tables = []
        for table in ctx.data:
            if not table.agg:
                tables.append(table)
                continue
            
            cname = self.get_count_name(table.agg)
            
            df = table.agg.len(name=cname.str())
            schema = table.agg_schema.copy().set(cname, self.count_type)
            new = Table(df=df, schema=schema, name=table.name)
            new = new.drop_many(table.agg_paths)
                        
            tables.append(new)
        
        return Data(tables=tables)
