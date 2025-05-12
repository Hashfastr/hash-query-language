from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context

# Take, limits the number of results given an integer
# Ensures that only integers are given, if not then errors
# The implementation algorithm is just grab the first n rows.
#
# https://learn.microsoft.com/en-us/kusto/query/take-operator
@register_op('Take')
class Take(Operator):
    def __init__(self, expr:Expression):
        super().__init__()
        self.expr = expr
        
    def eval(self, ctx:Context, **kwargs):
        if self.expr.type != 'Integer':
            raise CompilerException(f'Invalid type {self.expr.type} given to take operator')
        
        limit = self.expr.eval(ctx)
        
        return ctx.data[:limit]