from .Operator import Operator
from ..Expression import Expression
import polars as pl
from ..PolarsTools import PolarsTools as pltools
from ..Results import Results
from HqlCompiler.Registry import register_op
from HqlCompiler.Functions import Function

import logging
from HqlCompiler.Exceptions import *

# Super meta operator, 
@register_op('PrePipe')
class PrePipe(Operator):
    def __init__(self, expr:Expression):
        super().__init__()
        self.expr = expr
        self.non_conseq = []
        
    def execute(self, data:Results):        
        funcs = []
        out = None
        
        if self.expr.type == "DotCompositeFunction":
            funcs = self.expr.resolve_func_chain()
            out = funcs.eval_chain()

        if self.expr.type == "Path":
            out = self.expr.eval_path()
            
        return out