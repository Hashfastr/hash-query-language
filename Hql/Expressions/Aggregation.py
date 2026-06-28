from __future__ import annotations

from .__proto__ import Expression

from typing import TYPE_CHECKING, Optional, Sequence

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Data import Table
    from Hql.Expressions.References import Reference

class OrderedExpression(Expression):
    def __init__(self, expr:Expression, order:str='desc', nulls:str=''):
        Expression.__init__(self)
        self.expr = expr
        self.order = order
        self.nulls = nulls
        self.implicit_nulls = True
        
        if nulls == '':
            if order == 'asc':
                self.nulls = 'first'
            if order == 'desc':
                self.nulls = 'last'
        else:
            self.implicit_nulls = False

    def deparse(self) -> str:
        expr = self.expr.deparse()
        out = f'{expr} {self.order}'
        if not self.implicit_nulls:
            out += f' nulls {self.nulls}'
        return out
        
    def to_dict(self):
        if self.expr == None:
            expr_dict = {}
        else:
            expr_dict = self.expr.to_dict()

        return {
            'name': expr_dict,
            'order': self.order,
            'nulls': self.nulls
        }

class ByExpression(Expression):
    def __init__(self, exprs:Sequence[Reference]):
        Expression.__init__(self)
        self.exprs = exprs
        
    def build_table_agg(self, table:Table) -> Optional[Table]:
        from Hql.Data import Schema
        from Hql.PolarsTools import pltools

        paths = []
        schema = []
        for expr in self.exprs:
            ptype = table.get_type(expr)

            # failed get_type returns a empty schema
            # Might reference a field that exists in another table but not this one.
            if not ptype:
                continue

            paths.append(expr)
            schema.append(table.schema.select(expr))
        
        pl_exprs = []
        for path in paths:
            pl_expr = pltools.path_to_expr(path)
            pl_exprs.append(pl_expr)

        if not pl_exprs:
            return None
        
        # Groups and coelesces the schemas together for each field
        # Probably need to rework and change maintain_order here in the future
        # Without it, it ####s up the aggregation functions but is much faster
        table.agg = table.df.group_by(pl_exprs, maintain_order=True)
        table.agg_paths = paths
        table.agg_schema = Schema.merge(schema)
        
        return table

    def deparse(self) -> str:
        exprs = []
        for i in self.exprs:
            exprs.append(i.deparse())
        out = 'by '
        out += ', '.join(exprs)
        return out
    
    def eval(self, ctx:Context):
        from Hql.Data import Data
        ctx = ctx.copy()

        new = []
        for table in ctx.data:
            agg = self.build_table_agg(table)
            if agg:
                new.append(agg)

        ctx.data = Data(tables=new)
        return ctx
