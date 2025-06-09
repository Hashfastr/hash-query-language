from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
import polars as pl
from HqlCompiler.Context import register_op, Context

from HqlCompiler.Data import Data, Table, Schema

import logging
import json

@register_op('Unnest')
class Unnest(Operator):
    def __init__(self, field:Expression, tables:list[Expression]):
        super().__init__()
        self.field = field
        self.tables = tables
        
    def to_dict(self):
        return {
            'type': self.type,
            'field': self.field.to_dict(),
            'tables': [x.to_dict() for x in self.tables]
        }
            
    def eval(self, ctx:Context, **kwargs):
        self.ctx = ctx

        field = self.field.eval(ctx, as_list=True)
        
        # loop through tables defined by 'on'
        for i in self.tables:
            table = i.eval(ctx, as_list=True)
            
            # match tables matching the pattern
            tables = ctx.data.get_tables(table[0])
            
            # loop through matching tables
            for j in tables:
                new_table = j.unnest(field)
                ctx.data.replace_table(new_table)
        
        return ctx.data