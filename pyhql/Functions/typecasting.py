from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Table, Series, Schema
from Hql.Types.Hql import HqlTypes as hqlt
import polars as pl
from Hql import Expressions as Expr

class Typecast(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, 1)
        self.src = args[0]
        
        if self.src.literal:
            self.src = pl.Series([self.src.value])
        
        # default cast type
        self.cast_type = hqlt.string()
        self.expr = Expr.StringLiteral
        
    def eval(self, ctx:'Context', **kwargs):
        # represents a single value literal 
        if isinstance(self.src, pl.Series):
            new = self.cast_type.cast(self.src)
            return self.expr(new[0])

        path = self.src.eval(ctx, as_list=True)
        data = ctx.data.select(path).strip()

        tables = []
        for table in data:
            series = table.series.cast(self.cast_type).series

            new = Table(name=table.name)
            new.insert(path, series, self.cast_type)
            tables.append(new)

        return Data(tables=tables)
    
@register_func('toint')
class toint(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.int()
        self.expr = Expr.Integer

@register_func('tofloat')
class tofloat(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.float()
        self.expr = Expr.Float
        
@register_func('todouble')
class todouble(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.double()
        self.expr = Expr.Float
        
@register_func('tostring')
class tostring(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.string()
        self.expr = Expr.StringLiteral

@register_func('toip4')
class toip4(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.ip4()
        self.expr = Expr.IP4
