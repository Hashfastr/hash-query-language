from .Operator import Operator
from ..Results import Results
from HqlCompiler.Expression import Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.PolarsTools import PolarsTools
import polars as pl

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs

    def extend(self, data:pl.DataFrame, lh:Expression, rh:Expression):
        if rh.type == 'Path':
            src = [x.get_name() for x in rh.path]
        elif rh.type in ('Identifier'):
            src = [rh.get_name()]
        else:
            raise CompilerException(f'Unhandled Right-Hand expression type for extend: {rh.type}')

        if lh.type == 'Path':
            dest = [x.get_name() for x in lh.path]
        elif lh.type in ('Identifier'):
            dest = [lh.get_name()]
        else:
            raise CompilerException(f'Unhandled Left-Hand expression type for extend: {lh.type}')
        
        src_data = PolarsTools.get_element_series(data, src)
        # Can do whatever with src_data here
        
        
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