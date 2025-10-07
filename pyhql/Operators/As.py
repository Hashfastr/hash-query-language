from Hql.Operators import Operator
from Hql.Expressions import Expression
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context

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
    def __init__(self, expr:Expression):
        Operator.__init__(self)
        self.expr = expr

    def decompile(self, ctx: 'Context') -> str:
        expr = self.expr.decompile(ctx)
        return f'as {expr}'
        
    def eval(self, ctx:'Context', **kwargs):
        return ctx.data
