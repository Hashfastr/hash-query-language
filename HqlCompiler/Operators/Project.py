from .Operator import Operator
from ..Expression import Expression
import polars as pl
from ..PolarsTools import PolarsTools as pltools
from ..Results import Results
from HqlCompiler.Registry import register_op
from HqlCompiler.Exceptions import *

# Project my beloved
# Defines a number of fields to be kept in the output following this operator.
#
# {"test1":"val","test2":"val","test3":"val","test4":"val","test5":"val"}
# | project test1, test3, test5
# 
# Would result in
#
# {"test1":"val","test3":"val","test5":"val"}
# https://learn.microsoft.com/en-us/kusto/query/project-operator
@register_op('Project')
class Project(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        self.non_conseq = [
            'Take'
        ]
        
    def execute(self, data:Results):
        data_sets = []
        for i in self.exprs:
            if i.type == "NamedReference":
                fields = [i.get_name()]
                df = pltools.get_element(data, fields)
            
            elif i.type == "Path":
                fields = i.eval_path()
                df = pltools.get_element(data, fields)

            elif i.type == "DotCompositeFunction":
                funcs = i.resolve_func_chain()
                df = funcs.eval_chain(data)
                
            else:
                raise CompilerException(f'Unhandled project expression {i.type}')
                
            data_sets.append(df)
            
        new = pltools.merge(data_sets)
        
        return new