from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context
import logging

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Expressions import OpParameter

# Where operator
# Essentially just a field filter, can hold a number of expressions, even nested ones.
# Can also take a number of parameters, although I'm not sure what they are
# but they can exist.
# https://learn.microsoft.com/en-us/kusto/query/where-operator
# @register_op('Where')
class Where(Operator):
    # Pass in the parser context here for helpful debugging
    def __init__(self, expr:'Expression', params:Union[None, list['OpParameter']]=None):
        Operator.__init__(self)
        self.parameters = params if params else []
        self.expr = expr

    def decompile(self, ctx: 'Context') -> Union[str, list[str]]:
        from Hql.Expressions import BinaryLogic

        out = 'where '

        if self.parameters:
            exprs = []
            for i in self.parameters:
                exprs.append(i.decompile(ctx))
            out += ' '.join(exprs)
            out += ' '

        # Attempt to split up ands
        if isinstance(self.expr, BinaryLogic) and self.expr.bitype == 'and':
            splits = []
            exprs = [] 
            for i in [self.expr.lh] + self.expr.rh:
                exprs.append(i.decompile(ctx))

            splits = []
            for i in exprs:
                if not splits or len(splits[0]) + len(i) > 60:
                    splits.append(i)

                else:
                    splits[0] += f' and {i}'

            outs = []
            for i in splits:
                outs.append(out + i)

            return outs

        else:
            out += self.expr.decompile(ctx)

        return out

    '''
    Counts each table and replaces the contents of that table with the count.
    Adds an additional meta * table for the total count of all tables.
    '''
    def eval(self, ctx:'Context', **kwargs):
        pl_filter = self.expr.eval(ctx, as_pl=True)

        for table in ctx.data:
            try:
                table.filter(pl_filter)
            except hqle.QueryException as e:
                logging.warning(e)

        return ctx.data
