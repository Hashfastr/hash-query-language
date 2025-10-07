from Hql.Expressions import Expression
from Hql.Operators import Operator
from Hql.Context import register_op, Context

# @register_op('Unnest')
class Unnest(Operator):
    def __init__(self, field:Expression, tables:list[Expression]):
        Operator.__init__(self)
        self.field = field
        self.tables = tables
        
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'field': self.field.to_dict(),
            'tables': [x.to_dict() for x in self.tables]
        }

    def decompile(self, ctx: 'Context') -> str:
        out = 'unnest '
        out += self.field.decompile(ctx)

        if self.tables:
            out += ' on '
            exprs = []
            for i in self.tables:
                exprs.append(i.decompile(ctx))
            out += ', '.join(exprs)

        return out
            
    def eval(self, ctx:'Context', **kwargs):
        self.ctx = ctx

        field = self.field.eval(ctx, as_list=True)
        
        # loop through tables defined by 'on'
        for i in self.tables:
            table = i.eval(ctx, as_list=True)
            
            # match tables matching the pattern
            tables = ctx.data.get_tables(table[0])
            
            # loop through matching tables
            for j in tables:
                new_table = j.unnest(field)
                ctx.data.replace_table(new_table)
        
        return ctx.data
