from polars import DataFrame
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from typing import Tuple
from .__proto__ import Function

import polars as pl
from HqlCompiler.PolarsTools import plt

# This is a meta function resolved while parsing
@register_func('toint')
class toint(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1, )
        self.src = args[0]
                
    def eval(self, ctx:Context, **kwargs):
        series = self.src.eval(ctx)
        
        series_name = self.src.eval(ctx, as_str=True, as_list=True)
        if not isinstance(series_name, list):
            series_name = [series_name]
        
        df = plt.build_element(series_name, series.cast(pl.Int32))
        return df