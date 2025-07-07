from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from .__proto__ import Function
from HqlCompiler.Data import Data, Series, Table, Schema
from HqlCompiler.Types.Hql import HqlTypes as hqlt
import polars.dataframe.group_by as group_by
from HqlCompiler.Operators import Project
import polars as pl

@register_func('make_list')
@register_func('make_mv')
class make_mv(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, -1)
        self.args = args
    
    def gen_schema(self, schema:Schema, paths:list[str]):
        schema = schema.select_many(paths)
        
        new = Schema()
        for path in paths:
            t = schema.select(path).strip()
            t = hqlt.multivalue(t)
            new.set(path, t)

        return new
    
    def aggregate(self, ctx:Context, table:Table):
        cols = []
        paths = []
        for arg in self.args:
            cols.append(arg.eval(ctx, as_pl=True))
            paths.append(arg.eval(ctx, as_list=True))
        
        df = table.agg.agg(cols)
                    
        # Drop the aggregation fields as they can be added back later
        # Such as with a summarize
        df = df.drop(table.agg_cols)
        schema = self.gen_schema(table.schema, paths)
        
        return Table(df=df, schema=schema, name=table.name)
    
    def get_series(self, df:pl.DataFrame, schema:dict):
        cur = []
                
        for key in schema:
            if isinstance(schema[key], dict):
                cur += self.get_series(df.select(key).unnest(key), schema[key])
                continue
            
            series = df.select(key).to_series().rename('')
            stype = schema[key]
            cur.append(Series(series, stype))
            
        return cur
    
    def normal(self, ctx:Context, table:Table):
        # Only operate on the single table
        ctx.data = Data(tables=[table])

        # Create the data subset and grab the table
        data = Project(self.args).eval(ctx)
        table = data.table_by_index(0)
        series = self.get_series(table.df, table.schema.schema)
        
        # Cast to our agreed upon type
        mv_type = hqlt.resolve_conflict([x.type for x in series])
        series = [mv_type.cast(x.series) for x in series]
        series = pl.Series(pl.DataFrame(series).rows())
        mv_type = hqlt.multivalue(mv_type)
        
        return Series(series, mv_type)
        
    def eval(self, ctx:Context, **kwargs):
        as_value = kwargs.get('as_value', False)
        
        new = []
        for table in ctx.data:
            if isinstance(table.agg, group_by.GroupBy):
                new.append(self.aggregate(ctx, table))
                continue
            
            series = self.normal(ctx, table)
            
            if as_value:
                new.append(Table(series=series, name=table.name))
                continue
            
            df = pl.DataFrame({'mv': series.series})
            schema = {'mv': series.type}

            new.append(Table(df=df, schema=Schema(schema=schema), name=table.name))
        
        return Data(tables=new)