from polars import DataFrame
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from typing import Tuple
from .__proto__ import Function

import polars as pl
from HqlCompiler.PolarsTools import PolarsTools

# This is a meta function resolved while parsing
@register_func('toint')
class toint(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1, )
        self.src = args[0]
                
    def eval(self, ctx:Context, **kwargs):
        series = self.src.eval(ctx)
        df = PolarsTools.build_element(self.series_name, series.cast(pl.Int32))
        return df