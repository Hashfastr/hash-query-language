from HqlCompiler.Exceptions import *
from HqlCompiler.Context import register_func, Context
from .__proto__ import Function
import polars as pl
from HqlCompiler.Types.Hql import HqlTypes as hqlt
from HqlCompiler.Expressions import BasicRange
from HqlCompiler.Expressions import Integer

@register_func('ip4subnet')
class ip4subnet(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1)
    
    def eval(self, ctx:Context, **kwargs):
        import re
        subnet_regex = '(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3})\\/(\\d{1,2})'
        
        subnet_text = self.args[0].eval(ctx, as_str=True)
        ip_text   = re.match(subnet_regex, subnet_text)
        mask_text = re.match(subnet_regex, subnet_text)

        if ip_text == None or mask_text == None:
            raise QueryException(f'Invalid subnet given {subnet_text}')

        ip_text = ip_text.group(1)
        mask_text = mask_text.group(2)
        
        mask = 0xFFFFFFFF - ((1 << (32 - int(mask_text))) - 1)        
        ip_int = hqlt.ip4().cast(pl.Series([ip_text]))[0]

        ip_start = ip_int &  mask
        ip_end   = ip_int | (mask ^ 0xFFFFFFFF)

        ip_start = Integer(ip_start)
        ip_end = Integer(ip_end)
        
        return BasicRange(ip_start, ip_end)
