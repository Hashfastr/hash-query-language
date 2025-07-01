from HqlCompiler.Operators import Operator
from HqlCompiler.Data import Data
from HqlCompiler.Expressions import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context

# Take, limits the number of results given an integer
# Ensures that only integers are given, if not then errors
# The implementation algorithm is just grab the first n rows.
#
# https://learn.microsoft.com/en-us/kusto/query/take-operator
@register_op('Take')
class Take(Operator):
    def __init__(self, limit:Expression, tables:list[Expression]):
        super().__init__()
        self.limit = limit
        self.tables = tables

    def to_dict(self):
        return {
            'type': self.type,
            'limit': self.limit.to_dict(),
            'tables': [x.to_dict() for x in self.tables]
        }

    def get_limits(self):
        ctx = Context(Data())
        limit = self.limit.eval(ctx)
        tables = [x.eval(ctx, as_str=True) for x in self.tables]

        return {
            'limit': limit,
            'tables': tables
        }

    
    '''
    Takes only so many results for each table.

    If given the parameter global=True then it will limit results such that
    the sum of all tables is less than or equal to the take amount.
    Unimplemented.
    '''
    def eval(self, ctx:Context, **kwargs):        
        limit = self.limit.eval(ctx)

        if not isinstance(limit, int):
            raise QueryException(f'Take operator passed non-int type {self.n_rows}')
        
        table_names = []
        for i in self.tables:
            table_names.append(i.eval(ctx, as_str=True))
            
        if not table_names:
            table_names.append('*')

        for i in table_names:
            tables = ctx.data.get_tables(i)
            for j in tables:
                j.truncate(limit)

        return ctx.data
