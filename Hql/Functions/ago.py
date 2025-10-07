from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema

import logging

'''
Static function, can be precomputed
Generates a time delta
'''
@register_func('ago')
class template(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, 1)
        
    def eval(self, ctx:'Context', **kwargs):
        from datetime import timedelta
        return timedelta()
