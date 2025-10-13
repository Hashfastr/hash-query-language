from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema

import logging

@register_func('null')
class null(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 0, 0)
        self.preprocess = True
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Expressions import Null
        return Null()

@register_func('isnull')
class isnull(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, 1)
        self.preprocess = True
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Expressions import Null, Equality
        return Equality(self.args[0], '==', [Null()])
