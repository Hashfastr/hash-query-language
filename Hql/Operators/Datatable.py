from typing import Optional
from .Operator import Operator
from Hql.Data import Data, Table, Schema
from Hql.PolarsTools import pltools
from Hql.Expressions import Expression, NamedReference
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context
import polars as pl
import numpy as np
from Hql.Operators import Operator

'''
Creates a simple datatable, essentially an inline dataframe/table
'''
# @register_op('Datatable')
class Datatable(Operator):
    def __init__(self, schema:list[list[Expression]], values:list[Expression], name:Optional[Expression]=None):
        Operator.__init__(self)
        self.values = values
        self.schema = schema
        self.name = name
        self.tabular = True
        
    def to_dict(self):
        return {
            'type': self.type,
            # 'schema': 
        }

    def decompile(self, ctx: 'Context') -> str:
        width = len(self.schema)
        nvalues = len(self.values)

        schema = []
        for i in self.schema:
            schema.append(f'{i[0].decompile(ctx)}: {i[1].decompile(ctx)}')
        schema = ', '.join(schema)
        
        values = []
        for i in range(0, nvalues, width):
            row = [x.decompile(ctx) for x in self.values[i:i+width]]
            values.append(', '.join(row))

        table = '    '
        table += ',\n    '.join(values)
        table += '\n'

        total  = f'datatable ({schema})\n'
        total += '[\n'
        total += table
        total += ']'
        
        if self.name:
            total += f' as {self.name.decompile(ctx)}'

        return total

    def eval(self, ctx:'Context', **kwargs):
        width = len(self.schema)
        nvalues = len(self.values)
        
        schema = dict()
        for i in self.schema:
            name = i[0].eval(ctx, as_str=True)
            t = i[1].eval(ctx)
            schema[name] = t

        keys = list(schema.keys())
        data = dict()
        for i in range(width):
            rows = []
            for j in range(0, nvalues, width):
                rows.append(self.values[j + i].eval(ctx))
            data[keys[i]] = rows

        name = 'datatable'
        if self.name:
            name = self.name.eval(ctx, as_str=True)
            assert isinstance(name, str)
            
        schema = Schema(schema=schema)
        df = pl.DataFrame(data)
        table = Table(df=df, schema=schema, name=name)
        
        return Data(tables=[table])
