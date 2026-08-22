from __future__ import annotations
from typing import TYPE_CHECKING
from Hql.Operators.Operator import Operator

if TYPE_CHECKING:
    from Hql.Context import Context

class Template(Operator):
    def __init__(self):
        Operator.__init__(self)

    def deparse(self) -> str:
        return ''

    def eval(self, ctx:Context):
        return ctx
