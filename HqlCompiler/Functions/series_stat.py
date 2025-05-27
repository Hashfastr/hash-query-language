from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from typing import Tuple
from .__proto__ import Function

import polars as pl
from HqlCompiler.PolarsTools import pltools

# This is a meta function resolved while parsing
@register_func('series_stats')
class series_stats(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 2)
        self.ignore_nonfinite = False
        self.series_name = args[0]

        if len(self.args) > 1:
            if self.args[1].type != "Bool":
                raise ArgumentException(f'{self.name} expected argument type Bool, got {self.args[1].type} for nonfinite')
            self.ignore_nonfinite = self.args[1].eval()
            
    def cal_min(self, s:pl.Series) -> Tuple[int, int]:
        min = s.min()
                
        # got to be a better way
        for idx, i in enumerate(s):
            if i == min:
                min_idx = idx
                break
        
        return (min, min_idx)

    def cal_max(self, s:pl.Series) -> Tuple[int, int]:
        max = s.max()
                
        # got to be a better way
        for idx, i in enumerate(s):
            if i == max:
                max_idx = idx
                break
        
        return (max, max_idx)
    
    def cal_avg(self, s:pl.Series) -> float:
        return s.mean()
    
    def cal_stdev(self, s:pl.Series) -> float:
        return s.std()
    
    def cal_vari(self, s:pl.Series) -> float:
        return s.var()
    
    def eval(self, ctx:Context, **kwargs):
        s = self.series_name.eval(ctx)
        name = self.series_name.eval(ctx, as_str=True, as_list=True)
        
        if not isinstance(name, list):
            name = [name]
        
        min, min_idx = self.cal_min(s)
        max, max_idx = self.cal_max(s)
        avg = self.cal_avg(s)
        stdev = self.cal_stdev(s)
        vari = self.cal_vari(s)
       
        prefix = f"series_stats_{'_'.join(name)}"
        
        df = pl.DataFrame(
            {
                f'{prefix}_min': min,
                f'{prefix}_min_idx': min_idx,
                f'{prefix}_max': max,
                f'{prefix}_max_idx': max_idx,
                f'{prefix}_avg': avg,
                f'{prefix}_stdev': stdev,
                f'{prefix}_variance': vari
            }
        )
        
        return df