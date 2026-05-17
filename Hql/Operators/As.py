from Hql.Operators.Operator import Operator
from typing import Optional, TYPE_CHECKING

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
# Disabling this for now until I decide how to implement
## @register_op('As')
class As(Operator):
    def __init__(self, expr:'Expression'):
        Operator.__init__(self)
        self.expr = expr

    @property
    def expr(self) -> 'Expression':
        e = super().expr
        assert e is not None
        return e

    @expr.setter
    def expr(self, value:Optional['Expression']):
        assert value is not None
        super().expr = value

    def deparse(self) -> str:
        expr = self.expr.deparse()
        return f'as {expr}'
        
    def eval(self, ctx: 'Context') -> 'Context':
        return ctx
