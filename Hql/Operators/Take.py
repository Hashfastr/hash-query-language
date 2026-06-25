from Hql.Expressions.References import NamedReference
from Hql.Operators.Operator import Operator
from Hql.Data import Data
from Hql.Expressions.Literals import Integer
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context

# Take, limits the number of results given an integer
# Ensures that only integers are given, if not then errors
# The implementation algorithm is just grab the first n rows.
#
# https://learn.microsoft.com/en-us/kusto/query/take-operator
# @register_op('Take')
class Take(Operator):
    def __init__(self, limit:Integer, tables:list[NamedReference]):
        Operator.__init__(self)
        self._expr:Integer = limit
        self.tables = tables

    @property
    def expr(self) -> Integer:
        expr = self._expr
        assert expr
        return expr

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
        tables = [x.str() for x in self.tables]

        return {
            'limit': limit,
            'tables': tables
        }

    def deparse(self) -> str:
        out = 'take ' + self.expr.deparse()

        if self.tables:
            out += ' from '
            exprs = []
            for i in self.tables:
                exprs.append(i.deparse())
            out += ', '.join(exprs)

        return out
    
    '''
    Takes only so many results for each table.

    If given the parameter global=True then it will limit results such that
    the sum of all tables is less than or equal to the take amount.
    Unimplemented.
    '''
    def eval(self, ctx:'Context'):        
        limit = self.expr.value

        table_names = []
        for i in self.tables:
            table_names.append(i.str())
            
        if not table_names:
            table_names.append('*')

        for i in table_names:
            tables = ctx.data.get_tables(i)
            for j in tables:
                j.truncate(limit)

        return ctx
