from .__proto__ import Expression
from Hql.Context import Context
from Hql.Data import Data, Table, Schema
from Hql.PolarsTools import pltools
from Hql.Exceptions import HqlExceptions as hqle

from typing import Union

class OrderedExpression(Expression):
    def __init__(self, expr:Union[Expression, None]=None, order:str='desc', nulls:str=''):
        super().__init__()
        self.expr = expr
        self.order = order
        
        if nulls == '':
            if order == 'asc':
                self.nulls = 'first'
            if order == 'desc':
                self.nulls = 'last'
        else:
            self.nulls = nulls
        
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
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        
    def build_table_agg(self, ctx:Context, table:Table):
        if table.schema == None:
           raise hqle.CompilerException(f'Table passed to by expression is not fully initialized, schema == None')

        paths = []
        schema = []
        for expr in self.exprs:
            path = expr.eval(ctx, as_list=True)
            
            if not isinstance(path, list):
                raise hqle.CompilerException(f'By path expression returned non-list[str] {type(path)}')

            ptype = table.get_type(path)

            # failed get_type returns a empty schema
            # Might reference a field that exists in another table but not this one.
            if not ptype:
                continue

            paths.append(path)
            schema.append(table.schema.select(path))
        
        pl_exprs = []
        for path in paths:
            pl_expr = pltools.path_to_expr(path)
            pl_exprs.append(pl_expr)
        
        # Groups and coelesces the schemas together for each field
        # Probably need to rework and change maintain_order here in the future
        # Without it, it fucks up the aggregation functions but is much faster
        table.agg = table.df.group_by(pl_exprs, maintain_order=True)
        table.agg_paths = paths
        table.agg_schema = Schema.merge(schema)
        
        return table
    
    def eval(self, ctx:Context, **kwargs):
        new = []
        
        for table in ctx.data:
            new.append(self.build_table_agg(ctx, table))
            
        return Data(tables=new)
