from Hql.Operators.Operator import Operator

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Hql.Expressions.References import NamedReference
    from Hql.Context import Context

# Count simply returns the number of rows given by a record set.
#
# https://learn.microsoft.com/en-us/kusto/query/count-operator
class Count(Operator):
    def __init__(self, name:Optional['NamedReference']=None):
        Operator.__init__(self)
        self.name:Optional['NamedReference'] = name

    def deparse(self) -> str:
        return f'count as {self.name.deparse()}' if self.name else 'count'

    def to_dict(self) -> dict:
        d = super().to_dict()
        if self.name:
            d['name'] = self.name.str()
        return d

    def eval(self, ctx:'Context') -> 'Context':
        from Hql.Data import Data, Table

        counts = dict()
        for table in ctx.data:
            counts[table.name] = len(table)
            
        # if sending to a table name, make a new table with counts
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
            for name in counts:
                new = [{'Count': counts[name]}]
                new_tables.append(Table(name=name, init_data=new))
            ctx.data = Data(tables=new_tables)

            return ctx
