from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
from HqlCompiler.Data import Data, Table, Series, Schema
from .__proto__ import Function
from HqlCompiler.Types.Hql import HqlTypes as hqlt
import polars as pl
import HqlCompiler.Expressions as Expr

class Typecast(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, 1)
        self.src = args[0]
        
        if self.src.literal:
            self.src = pl.Series([self.src.value])
        
        # default cast type
        self.cast_type = hqlt.string()
        
    def eval(self, ctx:Context, **kwargs):        
        path = self.src.eval(ctx, as_list=True)
        data = ctx.data.select(path)

        return data.cast_in_place(path, self.cast_type)
    
@register_func('toint')
class toint(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.int()

@register_func('tofloat')
class tofloat(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.float()
        
@register_func('todouble')
class todouble(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.double()
        
@register_func('tostring')
class tostring(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.string()

@register_func('toip4')
class toip4(Typecast):
    def __init__(self, args:list):
        Typecast.__init__(self, args)
        self.cast_type = hqlt.ip4()

    def eval(self, ctx:Context, **kwargs):
        # Just the literal example
        if isinstance(self.src, pl.Series):
            new = self.cast_type.cast(self.src)
            return Expr.IP4(new[0])
        
        path = self.src.eval(ctx, as_list=True)
        data = ctx.data.select(path).strip()

        tables = []
        for table in data:
            series = self.cast_type.cast(table.df)

            new = Table(name=table.name)
            new.insert(path, series, self.cast_type)
            tables.append(new)

        return Data(tables=tables)