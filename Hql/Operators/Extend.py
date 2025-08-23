from Hql.Expressions import Expression
from Hql.Operators import Operator
from Hql.Context import register_op, Context

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
# @register_op('Extend')
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        Operator.__init__(self)
        self.exprs = exprs

    def decompile(self, ctx: 'Context') -> str:
        return ', '.join(x.decompile(ctx) for x in self.exprs)
            
    def eval(self, ctx:'Context', **kwargs):
        for i in self.exprs:
            i.eval(ctx)
        
        return ctx.data
