from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema
from Hql.Expressions import Expression, Not
from typing import Optional

@register_func('not')
class hqlnot(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        Function.__init__(self, args, 1, 1)
        self.expr:Expression = args[0]
        self.preprocess = True
        
    def eval(self, ctx:'Context', **kwargs):
        return Not(self.expr)
