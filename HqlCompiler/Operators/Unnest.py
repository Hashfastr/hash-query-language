from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
import polars as pl
from HqlCompiler.Context import register_op, Context

from HqlCompiler.Data import Data, Table, Schema

import logging

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
@register_op('Unnest')
class Unnest(Operator):
    def __init__(self, field:Expression, tables:list[Expression]):
        super().__init__()
        self.field = field
        self.tables = tables
            
    def eval(self, ctx:Context, **kwargs):
        self.ctx = ctx

        field = self.field.eval(ctx, as_list=True, as_str=True)
        for i in self.tables:
            table = i.eval(ctx, as_str=True)
            if table not in ctx.data.tables:
                raise QueryException(f'Attempting to unnest unknown table {table}')
            
            new_df = ctx.data.tables[table].get_value(field)
            if not isinstance(new_df, pl.DataFrame):
                raise QueryException(f'{field} in {table} is not a nested object')
                        
            new_schema = Schema(schema=ctx.data.tables[table].schema.get_type(field))
            if not new_schema:
                logging.warning(f'No schema defined for field {field} in table {table}')
                
            ctx.data.replace_table(Table(df=new_df, schema=new_schema, name=table))
        
        return ctx.data