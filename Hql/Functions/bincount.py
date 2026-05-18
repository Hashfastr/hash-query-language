from . import Function
from Hql.Context import register_func
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from Hql.Context import Context

@register_func('bincount')
class bincount(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        # allows 1 to infinity args
        super().__init__(args, 1, 1)

    def eval(self, ctx: 'Context', receiver=None) -> object:
        from Hql.Data import Data
        return Data()
