from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
import logging
from .__proto__ import Function
from HqlCompiler.Data import Data, Series, Table, Schema

@register_func('bincount')
class bincount(Function):
    def __init__(self, args:list):
        # allows 1 to infinity args
        super().__init__(args, 1, 1)
        
    def eval(self, ctx:Context, **kwargs):
        return Data()