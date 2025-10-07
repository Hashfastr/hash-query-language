from . import Operator
from Hql.Data import Data, Table
from Hql.Expressions import Expression
from Hql.Exceptions import HqlExceptions as hqle
import polars as pl
from Hql.Context import register_op, Context

from typing import Union

from Hql.Exceptions import HqlExceptions as hqle

# Count simply returns the number of rows given by a record set.
#
# https://learn.microsoft.com/en-us/kusto/query/count-operator
# @register_op('Count')
class Count(Operator):
    def __init__(self, name:Union[Expression, None]=None):
        Operator.__init__(self)
        self.name = name

    def decompile(self, ctx: 'Context') -> str:
        name = self.name.decompile(ctx) if self.name else ''
        return f'count as {name}' if name else 'count'
    
    '''
    Counts each table and replaces the contents of that table with the count.
    Adds an additional meta * table for the total count of all tables.
    '''
    def eval(self, ctx:'Context', **kwargs):
        name = self.name.eval(ctx, as_str=True) if self.name else None

        if not isinstance(name, (str, type(None))):
            raise hqle.CompilerException(f'Name given to count operator is not of [str, None], is {type(name)}')
        
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
                
            return Data(tables=new_tables)
