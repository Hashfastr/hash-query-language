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

    def extend(self, data:pl.DataFrame, src:list[str], dest:list[str]):
        src_data = PolarsTools.get_element_series(data, src)
        # Can do whatever with src_data here
        dest_data = PolarsTools.build_element(dest, src_data)
        return dest_data
            
    def execute(self, data:Results):
        new = [data]
        for i in self.exprs:
            if i.type != "NamedExpression":
                raise CompilerException(f'Extend operator given invalid expression {i.type}')
            
            if i.name.type == 'Path':
                dest = [x.get_name() for x in i.name.path]
            else:
                dest = [i.name.get_name()]
            
            if i.value.type == 'Path':
                src = [x.get_name() for x in i.value.path]
            else:
                raise CompilerException(f'Unhandled NamedExpression value type {i.value.type}')
                
            new.append(self.extend(data, src, dest))
        
        return pl.concat(new, how='horizontal')