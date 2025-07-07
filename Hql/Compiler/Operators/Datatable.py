from .Operator import Operator
from HqlCompiler.Data import Data, Table, Schema
from HqlCompiler.PolarsTools import pltools
from HqlCompiler.Expressions import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context
import polars as pl
import numpy as np
from HqlCompiler.Operators import Operator

'''
Creates a simple datatable, essentially an inline dataframe/table
'''
@register_op('Datatable')
class Datatable(Operator):
    def __init__(self, schema:list[list[Expression]], values:list[Expression]):
        super().__init__()
        self.schema = schema
        self.values = values
        self.tabular = True
        
    def to_dict(self):
        return {
            'type': self.type,
            # 'schema': 
        }
        
    def eval(self, ctx:Context, **kwargs):
        width = len(self.schema)
        nvalues = len(self.values)
        
        schema = dict()
        for i in self.schema:
            name = i[0].eval(ctx, as_str=True)
            t = i[1]
            schema[name] = t

        keys = list(schema.keys())
        data = dict()
        for i in range(width):
            rows = []
            for j in range(0, nvalues, width):
                rows.append(self.values[j + i].eval(ctx))
            data[keys[i]] = rows
            
        schema = Schema(schema=schema)
        df = pl.DataFrame(data)
        table = Table(df=df, schema=schema, name='datatable')
        
        return Data(tables=[table])