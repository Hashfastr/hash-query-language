from Hql.Operators import Operator
from Hql.Context import Context
from Hql.Expressions import Expression
from typing import Sequence, TYPE_CHECKING
import logging

if TYPE_CHECKING:
    from Hql.Operators import Database

class Push(Operator):
    """Push the current data to configured database targets."""

    def __init__(self, exprs:Sequence[Expression]):
        Operator.__init__(self)
        self.exprs = exprs
        self.dbs:list[Database] = []

    def decompile(self, ctx: 'Context', split: bool = False) -> str:
        out = 'push'

        out += ' '
        exprs = []
        for i in self.exprs:
            exprs.append(i.decompile(ctx))
        out += ', '.join(exprs)

        return out

    def eval(self, ctx:'Context', **kwargs):
        for i in self.dbs:
            if not i.can_push:
                logging.error(f'Cannot push to DB {i.name}')
                continue

            i.push(ctx)

        return ctx.data
