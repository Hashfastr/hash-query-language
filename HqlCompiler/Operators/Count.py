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
    def __init__(self, expr:Expression=None):
        super().__init__()
        self.expr = expr
    
    '''
    Counts each table and replaces the contents of that table with the count.
    Adds an additional meta * table for the total count of all tables.
    '''
    def eval(self, ctx:Context, **kwargs):
        counts = [Table(name='*', init_data=[{'Count': len(ctx.data)}])]
        for table in ctx.data.tables:
            count = [{'Count': len(ctx.data.tables[table])}]
            counts.append(Table(name=table, init_data=count))

        return Data(tables_list=counts)