from HqlCompiler.Operators import Operator
from HqlCompiler.Data import Data
from HqlCompiler.Expressions import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context

'''
Binds a name to the operator's input tabular expression

database("tf11-elastic").index("so-beats-2022.10.*")
| where winlog.computer_name == "asarea.vxnwua.net"
| take 10
| as asarea_events
| ...

https://learn.microsoft.com/en-us/kusto/query/as-operator
'''
@register_op('As')
class As(Operator):
    def __init__(self, expr:Expression):
        super().__init__()
        self.expr = expr
        
    def eval(self, ctx:Context, **kwargs):
        if self.expr.type != 'Integer':
            raise CompilerException(f'Invalid type {self.expr.type} given to take operator')
        
        limit = self.expr.eval(ctx)
        
        return ctx.data[:limit]