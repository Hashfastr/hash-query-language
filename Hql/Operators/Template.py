from typing import TYPE_CHECKING
from Hql.Operators.Operator import Operator

if TYPE_CHECKING:
    from Hql.Context import Context

class Template(Operator):
    def __init__(self):
        Operator.__init__(self)

    def decompile(self, ctx: 'Context', split: bool = False) -> str:
        return ''

    def eval(self, ctx:'Context', **kwargs):
        return ctx.data
