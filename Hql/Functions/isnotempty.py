from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema

import logging

# @register_func('template')
class template(Function):
    def __init__(self, args:list):
        # allows 1 to infinity args
        Function.__init__(self, args, 1, -1)
        
    def eval(self, ctx:'Context', **kwargs):
        return Data()
