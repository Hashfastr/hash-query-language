from HqlCompiler.Operators import Operator
from HqlCompiler.Expressions import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Data import Data, Table, Schema
from HqlCompiler.PolarsTools import pltools
import logging

# Where operator
# Essentially just a field filter, can hold a number of expressions, even nested ones.
# Can also take a number of parameters, although I'm not sure what they are
# but they can exist.
# https://learn.microsoft.com/en-us/kusto/query/where-operator
@register_op('Where')
class Where(Operator):
    # Pass in the parser context here for helpful debugging
    def __init__(self, expr:Expression, params:list=None):
        Operator.__init__(self)
        self.parameters = params if params else []
        self.expr = expr

    '''
    Counts each table and replaces the contents of that table with the count.
    Adds an additional meta * table for the total count of all tables.
    '''
    def eval(self, ctx:Context, **kwargs):
        pl_filter = self.expr.eval(ctx, as_pl=True)

        for table in ctx.data:
            try:
                table.filter(pl_filter)
            except QueryException as e:
                logging.warning(e)

        return ctx.data
