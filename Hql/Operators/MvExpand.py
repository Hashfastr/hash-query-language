from Hql.Data import Data, Table
from Hql.Operators import Operator
from Hql.Context import register_op, Context
from Hql.Types.Hql import HqlTypes as hqlt
from typing import Union, TYPE_CHECKING
from Hql.Exceptions import HqlExceptions as hqle
import polars as pl

if TYPE_CHECKING:
    from Hql.Expressions import ToClause, Integer

# @register_op('MvExpand')
class MvExpand(Operator):
    def __init__(self, exprs:list['ToClause'], limit:Union[None, 'Integer']=None):
        Operator.__init__(self)
        self.exprs = exprs
        self.limit = limit
        
    def explode_table(self, ctx:'Context', table:Table, limit:int):
        schema = table.schema
        df = table.df

        for to in self.exprs:
            path = to.expr.eval(ctx, as_list=True)
            if not isinstance(path, list):
                raise hqle.CompilerException(f'To expression return non-list type {type(path)}')

            pl_expr = to.expr.eval(ctx, as_pl=True)
            if not isinstance(path, pl.Expr):
                raise hqle.CompilerException(f'To expression return non-list type {type(path)}')

            to_schema = schema.get_type(path).schema

            # Short circuit case
            if not isinstance(to_schema, hqlt.multivalue):
                continue
            
            new_type = to_schema.inner
            df = df.with_columns(
                pl_expr.list.slice(0, limit)
            ).explode(pl_expr)

            if to.to:
                new_type = to.to
                        
            schema.set(path, new_type)
            
        return Table(df=df, schema=schema, name=table.name)

    def decompile(self, ctx: 'Context') -> str:
        out = 'mvexpand '

        exprs = []
        for i in self.exprs:
            exprs.append(i.decompile(ctx))
        out += ', '.join(exprs)
        
        if self.limit:
            out += ' '
            out += self.limit.decompile(ctx)

        return out

    def eval(self, ctx:'Context', **kwargs):
        # Long literal, just get us the number
        limit = -1
        if self.limit:
            limit = self.limit.eval(ctx)
            assert isinstance(limit, int)

        new = []
        for table in ctx.data:
            new.append(self.explode_table(ctx, table, limit))
        
        return Data(tables=new)
