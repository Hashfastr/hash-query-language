from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from Hql.Operators.Operator import Operator

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Expressions import Expression

'''
Binds a name to the operator's input tabular expression

database("tf11-elastic").index("so-beats-2022.10.*")
| where winlog.computer_name == "asarea.vxnwua.net"
| take 10
| as asarea_events
| ...

https://learn.microsoft.com/en-us/kusto/query/as-operator
'''
# Disabled until implementation is decided
class As(Operator):
    def __init__(self, expr:Expression):
        Operator.__init__(self)
        self._expr:Expression = expr

    @property
    def expr(self) -> Expression:
        expr = self._expr
        assert expr
        return expr

    @expr.setter
    def expr(self, value:Optional[Expression]) -> None:
        from Hql.Exceptions import HqlExceptions as hqle

        if value is None:
            raise hqle.CompilerException('Setting As expression to None')
        self._expr = value

    def deparse(self) -> str:
        return f'as {self.expr.deparse()}'

    def eval(self, ctx: Context) -> Context:
        return ctx
