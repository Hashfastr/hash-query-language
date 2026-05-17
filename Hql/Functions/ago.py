from typing import Optional, TYPE_CHECKING
from . import Function
from Hql.Context import register_func

if TYPE_CHECKING:
    from Hql.Context import Context

'''
Static function, can be precomputed
Generates a time delta
'''
@register_func('ago')
class template(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        Function.__init__(self, args, 1, 1)

    def eval(self, ctx: 'Context', receiver=None) -> object:
        from datetime import timedelta
        return timedelta()
