from HqlCompiler.Operators import Operator
from HqlCompiler.Data import Data
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
    
    '''
    Takes only so many results for each table.

    If given the parameter global=True then it will limit results such that
    the sum of all tables is less than or equal to the take amount.
    Unimplemented.
    '''
    def eval(self, ctx:Context, **kwargs):        
        limit = self.expr.eval(ctx)

        if not isinstance(limit, int):
            raise QueryException(f'Take operator passed non-int type {self.n_rows}')

        for table in ctx.data.tables:
            ctx.data.tables[table].truncate(limit)
                
        return ctx.data