from ..Exceptions import *
from ..Context import register_func, Context
import logging
from .__proto__ import Function
from ..Data import Data, Series, Table, Schema

# @register_func('template')
class template(Function):
    def __init__(self, args:list):
        # allows 1 to infinity args
        super().__init__(args, 1, -1)
        
    def eval(self, ctx:Context, **kwargs):
        return Data()
