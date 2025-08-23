from Hql.Operators import Operator
from Hql.Context import register_op, Context

# @register_op('Template')
class Template(Operator):
    def __init__(self):
        Operator.__init__(self)

    def decompile(self, ctx: 'Context', split: bool = False) -> str:
        return ''

    def eval(self, ctx:'Context', **kwargs):
        return ctx.data
