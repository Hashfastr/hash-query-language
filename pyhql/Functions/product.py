from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context

@register_func('product')
class product(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 1, -1)
        self.preprocess = True
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Hac import Source

        src = Source(ctx)
        for i in self.args:
            arg = i.eval(ctx, as_str=True)
            if not isinstance(arg, str):
                raise hqle.QueryException(f"Invalid argument type passed to function product {type(i)} eval'd to {type(arg)}")
            src.product(arg)

        return src
