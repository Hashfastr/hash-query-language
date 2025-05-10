from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.PolarsTools import PolarsTools
from HqlCompiler.Functions import Function
import polars as pl
from HqlCompiler.Registry import register_op

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
            src = rh.eval_path()
        elif rh.type in ('Identifier'):
            src = [rh.get_name()]
        elif rh.type == "DotCompositeFunction":
            src = rh.resolve_func_chain()
        else:
            raise CompilerException(f'Unhandled Right-Hand expression type for extend: {rh.type}')

        if lh.type == 'Path':
            dest = lh.get_fields()
        elif lh.type in ('Identifier'):
            dest = [lh.get_name()]
        else:
            raise CompilerException(f'Unhandled Left-Hand expression type for extend: {lh.type}')
        
        if issubclass(type(src), Function):
            # Strip away any structs around the data, just want the series
            src_data = PolarsTools.get_element_series(src.eval(data))
        else:
            src_data = PolarsTools.get_element_series(data, src)        
        
        dest_data = PolarsTools.build_element(dest, src_data)
        return dest_data
            
    def execute(self, data:Results):
        new = [data]
        for i in self.exprs:
            if i.type != "NamedExpression":
                raise CompilerException(f'Extend operator given invalid expression {i.type}')
            
            lh = i.name
            rh = i.value
                
            new.append(self.extend(data, lh, rh))
        
        return pl.concat(new, how='horizontal')