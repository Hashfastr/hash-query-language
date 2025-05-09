from polars import DataFrame
from HqlCompiler.Exceptions import *
from HqlCompiler.Registry import register_func
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
                
    def eval(self, data:pl.DataFrame):
        if self.src.type == 'Path':
            self.series_name = [x.get_name() for x in self.src.path]
        elif self.src.type == "NamedReference":
            self.series_name = [self.src.get_name()]
        else:
            raise ArgumentException(f'{self.name} got invalid argument type {self.src.type} as argument')
                
        series = PolarsTools.get_element_series(data, self.series_name)
        return series.cast(pl.Int32)