from Hql.Operators import Operator
from Hql.Data import Data
from Hql.Expressions import Expression
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context

# Take, limits the number of results given an integer
# Ensures that only integers are given, if not then errors
# The implementation algorithm is just grab the first n rows.
#
# https://learn.microsoft.com/en-us/kusto/query/take-operator
# @register_op('Take')
class Take(Operator):
    def __init__(self, limit:Expression, tables:list[Expression]):
        Operator.__init__(self)
        self.expr = limit
        self.tables = tables

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'limit': self.expr.to_dict(),
            'tables': [x.to_dict() for x in self.tables]
        }

    def get_limits(self):
        ctx = Context(Data())
        limit = self.expr.eval(ctx)
        tables = [x.eval(ctx, as_str=True) for x in self.tables]

        return {
            'limit': limit,
            'tables': tables
        }

    def decompile(self, ctx: 'Context') -> str:
        out = 'take '
        expr = self.expr.decompile(ctx)
        if not isinstance(expr, str):
            raise hqle.DecompileStringException(type(self.expr), type(expr))

        out += expr

        if self.tables:
            out += ' from '
            exprs = []
            for i in self.tables:
                exprs.append(i.decompile(ctx))
            out += ', '.join(exprs)

        return out
    
    '''
    Takes only so many results for each table.

    If given the parameter global=True then it will limit results such that
    the sum of all tables is less than or equal to the take amount.
    Unimplemented.
    '''
    def eval(self, ctx:'Context', **kwargs):        
        limit = self.expr.eval(ctx)

        if not isinstance(limit, int):
            raise hqle.QueryException(f'Take operator passed non-int type {type(self.expr)}')
        
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
