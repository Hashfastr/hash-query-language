from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
from HqlCompiler.Data import Data
from .__proto__ import Function
from HqlCompiler.Types.Hql import HqlTypes as hqlt

# This is a meta function resolved while parsing
@register_func('toint')
class toint(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1,)
        self.src = args[0]
                
    def eval(self, ctx:Context, **kwargs):        
        path = self.src.eval(ctx, as_list=True)
        data = ctx.data.select(path)

        return data.cast_in_place(path, hqlt.int())