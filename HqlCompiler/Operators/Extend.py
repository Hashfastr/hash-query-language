from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.PolarsTools import PolarsTools
from HqlCompiler.Functions import Function
import polars as pl
from HqlCompiler.Context import register_op, Context

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
@register_op('Extend')
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs

    def extend(self, data:pl.DataFrame, lh:Expression, rh:Expression):
        if rh.type == 'Path':
            src = rh.eval(self.ctx, list=True)
        elif rh.type in ('Identifier'):
            src = [rh.eval(self.ctx, as_str=True)]
        elif rh.type == "DotCompositeFunction":
            src = rh.eval(self.ctx, no_exec=True)
        else:
            raise CompilerException(f'Unhandled Right-Hand expression type for extend: {rh.type}')

        if lh.type == 'Path':
            dest = lh.eval(self.ctx, list=True)
        elif lh.type in ('Identifier'):
            dest = [lh.eval(self.ctx, as_str=True)]
        else:
            raise CompilerException(f'Unhandled Left-Hand expression type for extend: {lh.type}')
        
        if isinstance(src, list) and issubclass(type(src[0]), Function):
            receiver = None
            for i in src:
                receiver = i.eval(self.ctx)
            
            src_data = PolarsTools.get_element_value(receiver)
        else:
            src_data = PolarsTools.get_element_value(data, src)
        
        dest_data = PolarsTools.build_element(dest, src_data)
        return dest_data
            
    def eval(self, ctx:Context, **kwargs):
        self.ctx = ctx
        new = [ctx.data]
        for i in self.exprs:
            if i.type != "NamedExpression":
                raise CompilerException(f'Extend operator given invalid expression {i.type}')
            
            lh = i.name
            rh = i.value
            
            new.append(self.extend(ctx.data, lh, rh))
        
        return pl.concat(new, how='horizontal')