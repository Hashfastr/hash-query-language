from . import Function

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Table
from typing import Union

import polars as pl
from Hql.PolarsTools import pltools

# This is a meta function resolved while parsing
@register_func('series_stats')
class series_stats(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, 3)
        self.ignore_nonfinite = False
        self.src = args[0]

        if len(self.args) > 1:
            if self.args[1].type != "Bool":
                raise hqle.ArgumentException(f'{self.name} expected argument type Bool, got {self.args[1].type} for nonfinite')
            self.ignore_nonfinite = self.args[1].eval()
            
    def cal_min(self, s:Union[pl.Series, list]):
        if isinstance(s, list):
            s = pl.concat(s)
            # return like this as it's a union pattern
            return (s.min(), None)
        
        min = s.min()
        min_idx = None
                
        # got to be a better way
        for idx, i in enumerate(s):
            if i == min:
                min_idx = idx
                break
        
        return (min, min_idx)

    def cal_max(self, s:Union[pl.Series, list]):
        if isinstance(s, list):
            s = pl.concat(s)
            # return like this as it's a union pattern
            return (s.max(), None)

        max = s.max()
        max_idx = None
                
        # got to be a better way
        for idx, i in enumerate(s):
            if i == max:
                max_idx = idx
                break
        
        return (max, max_idx)
    
    def cal_avg(self, s:Union[pl.Series, list]):
        if isinstance(s, list):
            s = pl.concat(s)

        return s.mean()
    
    def cal_stdev(self, s:Union[pl.Series, list]):
        if isinstance(s, list):
            s = pl.concat(s)

        return s.std()
    
    def cal_vari(self, s:Union[pl.Series, list]):
        if isinstance(s, list):
            s = pl.concat(s)
    
        return s.var()
    
    def eval(self, ctx:'Context', **kwargs):
        # Returns tables of series
        data = self.src.eval(ctx)
        name = self.src.eval(ctx, as_list=True)
        prefix = f"series_stats_{'_'.join(name)}"

        overall = {
            'min': None, 'min_idx': None,
            'max': None, 'max_idx': None,
            'avg': None,
            'stdev': None,
            'vari': None
        }

        serieses = []
        tables = []
        for table in data:
            s = table.series.series
            stype = table.series.type.pl_schema()
            serieses.append(s)

            min, min_idx = self.cal_min(s)
            max, max_idx = self.cal_max(s)
            avg = self.cal_avg(s)
            stdev = self.cal_stdev(s)
            vari = self.cal_vari(s)

            df = pl.DataFrame(
                {
                    f'{prefix}_min': min,
                    f'{prefix}_min_idx': min_idx,
                    f'{prefix}_max': max,
                    f'{prefix}_max_idx': max_idx,
                    f'{prefix}_avg': avg,
                    f'{prefix}_stdev': stdev,
                    f'{prefix}_variance': vari
                },
                schema_overrides={
                    f'{prefix}_min': stype,
                    f'{prefix}_max': stype
                }
            )
            
            # Explode out the rows so the number of rows of the source
            # Reasoning is that if we don't do this, all of the data extra data
            # will be marked as null and would suck
            df = df.select(pl.all().repeat_by(len(s))).explode(pl.all())

            tables.append(Table(df=df, name=table.name))
       
        min, min_idx = self.cal_min(serieses)
        max, max_idx = self.cal_max(serieses)
        avg = self.cal_avg(serieses)
        stdev = self.cal_stdev(serieses)
        vari = self.cal_vari(serieses)
        
        df = pl.DataFrame(
            {
                f'{prefix}_min': min,
                f'{prefix}_max': max,
                f'{prefix}_avg': avg,
                f'{prefix}_stdev': stdev,
                f'{prefix}_variance': vari
            }
        )

        tables.append(Table(df=df, name='*'))
        
        return Data(tables=tables)
