from .Operator import Operator
from HqlCompiler.Data import Data, Table
from HqlCompiler.Expression import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op, Context

# Count simply returns the number of rows given by a record set.
#
# https://learn.microsoft.com/en-us/kusto/query/count-operator
@register_op('Count')
class Count(Operator):
    def __init__(self, name:Expression=None):
        super().__init__()
        self.name = name
    
    '''
    Counts each table and replaces the contents of that table with the count.
    Adds an additional meta * table for the total count of all tables.
    '''
    def eval(self, ctx:Context, **kwargs):
        name = self.name.eval(ctx, as_str=True) if self.name else None
        
        counts = dict()
        for table in ctx.data:
            counts[table.name] = len(table)
            
        # cast count to a field
        if name:
            new_data = []
            for count in counts:
                new_data.append({'Table': count, 'Count': counts[count]})
            
            new_table = Table(init_data=new_data, name=name)
            ctx.data.add_table(new_table)
            
            return ctx.data
                                
        # Replace tables with counts
        else:
            new_tables = []
            for count in counts:
                new = [{'Count': counts[count]}]
                new_tables.append(Table(name=count, init_data=new))
                
            return Data(tables_list=new_tables)