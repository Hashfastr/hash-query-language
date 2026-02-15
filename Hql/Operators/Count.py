from . import Operator
from Hql.Data import Data, Table
from Hql.Expressions import NamedReference
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context

from typing import Optional

from Hql.Exceptions import HqlExceptions as hqle

# Count simply returns the number of rows given by a record set.
#
# https://learn.microsoft.com/en-us/kusto/query/count-operator
# @register_op('Count')
class Count(Operator):
    def __init__(self, name:Optional[NamedReference]=None):
        Operator.__init__(self)
        self.name:Optional[NamedReference] = name

    def deparse(self) -> str:
        return f'count as {self.name.deparse()}' if self.name else 'count'

    def to_dict(self) -> dict:
        d = super().to_dict()
        if self.name:
            d['name'] = self.name.str()
        return d

    def eval(self, ctx: Context) -> Context:
        counts = dict()
        for table in ctx.data:
            counts[table.name] = len(table)
            
        # cast count to a field
        if self.name:
            new_data = []
            for count in counts:
                new_data.append({'Table': count, 'Count': counts[count]})
            
            new_table = Table(init_data=new_data, name=self.name.str())
            ctx.data.add_table(new_table)
            
            return ctx
                                
        # Replace tables with counts
        else:
            ctx = ctx.copy()

            new_tables = []
            for count in counts:
                new = [{'Count': counts[count]}]
                new_tables.append(Table(name=count, init_data=new))
            ctx.data = Data(tables=new_tables)

            return ctx
