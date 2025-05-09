from HqlCompiler.Exceptions import *
from HqlCompiler.Registry import register_func
import logging
from typing import Tuple
from .__proto__ import Function

import polars as pl
from HqlCompiler.PolarsTools import PolarsTools

# This is a meta function resolved while parsing
@register_func('series_stat')
class series_stat(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 2)
        self.ignore_nonfinite = False
        
        narg = self.args[0]
        if narg.type == "Path":
            self.series_name = [x.get_name() for x in narg.path]
        elif narg.type == "NamedReference":
            self.series_name = [narg.get_name()]
        else:
            raise CompilerException(f'Invalid argument type {narg.type} given to {self.name}')

        if len(self.args) > 1:
            if self.args[1].type != "Bool":
                raise ArgumentException(f'{self.name} expected argument type Bool, got {self.args[1].type} for nonfinite')
            self.ignore_nonfinite = self.args[1].get_value()
            
    def cal_min(self, series:pl.Series) -> Tuple[int, int]:
        pass
        
    def eval(self, data:pl.DataFrame):
        series = PolarsTools.get_element_series(data, self.series_name)
        
        