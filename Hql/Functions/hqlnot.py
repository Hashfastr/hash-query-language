from . import Function
from Hql.Context import register_func
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Hql.Context import Context

@register_func('not')
class hqlnot(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions import Expression
        Function.__init__(self, args, 1, 1)
        self.expr:Expression = args[0]
        
    def preprocess(self, ctx: 'Context', receiver=None) -> object:
        from Hql.Expressions.Logic import Not
        return Not(self.expr)
