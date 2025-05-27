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
        field = self.src.eval(ctx, as_str=True, as_list=True)
        if not isinstance(field, list):
            field = [field]
        
        # df = plt.build_element(series_name, series.cast(pl.Int32))
        tables = ctx.data.cast_subset(field, hqlt.int)

        return Data(tables_list=tables)