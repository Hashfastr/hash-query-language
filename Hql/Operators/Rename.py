from Hql.Operators import Operator
from Hql.Context import register_op, Context
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import ToClause

class Rename(Operator):
    def __init__(self, exprs:list['ToClause']):
        Operator.__init__(self)
        self.exprs = exprs

    def decompile(self, ctx: 'Context', split: bool = False) -> str:
        return 'rename ' + ', '.join([x.decompile(ctx) for x in self.exprs])

    def eval(self, ctx:'Context', **kwargs):
        from Hql.Expressions import Expression

        for i in self.exprs:
            assert isinstance(i.to, Expression)
            src = i.expr.eval(ctx, as_str=True)
            assert isinstance(src, str)
            dst = i.to.eval(ctx, as_str=True)
            assert isinstance(dst, str)

            if src in ctx.data:
                ctx.data[dst] = ctx.data.tables.pop(src)
                ctx.data[dst].name = dst

        return ctx.data
