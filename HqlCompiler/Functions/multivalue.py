from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
from HqlCompiler.Data import Data, Table, Series, Schema
from .__proto__ import Function
from HqlCompiler.Types.Hql import HqlTypes as hqlt
from HqlCompiler.Types.Polars import PolarsTypes
import polars as pl
import logging

'''
@register_func('make_mv')
class make_mv(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, -1)
        self.args = args

    def eval(self, ctx:Context, **kwargs):
        names = [x.eval(ctx, as_list=True) for x in self.args]
        # A list of Data objects, containing tables containing a single value
        cols = [x.eval(ctx) for x in self.args]
        tables = []
        
        # Build tables
        for name in ctx.data.tables:
            top_dtype = None
            table_series = []
            for idx, col in enumerate(cols):
                if name not in col.tables:
                    continue
                
                table = col.tables[name]
                                
                if table.schema != None:
                    dtype = table.schema.strip()
                    series = table.strip()                        
                else:
                    series = table.series.series
                    dtype = table.series.type
                
                if isinstance(dtype, dict):
                    logging.warning('Attempting to multi-value an object, setting to null')
                    logging.warning(f"At path {'.'.join(names[idx])} in table {name}")
                    dtype = hqlt.null()
                    
                if top_dtype == None or isinstance(top_dtype, hqlt.null):
                    top_dtype = dtype
                
                # Cast to the top dtype
                table_series.append(series.rename(''))
                
            cast_series = []
            for series in table_series:
                cast_series.append(top_dtype.cast(series))
        
            series = pl.Series(pl.DataFrame(cast_series).rows())
        
            df = pl.DataFrame(
                {
                    f'{name}-mv': series
                }
            )
            
            schema = Schema(
                schema={
                    f'{name}-mv': hqlt.multivalue(top_dtype)
                }
            )
            
            table = Table(df=df, name=name, schema=schema)
            tables.append(table)

        return Data(tables_list=tables)
'''