from .Operator import Operator
from ..Expression import Expression
import polars as pl
from ..PolarsTools import PolarsTools as pltools
from ..Results import Results

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
class Project(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        self.non_conseq = [
            'Take'
        ]
    
    def gen_fields(self):
        fields = []
        for i in self.exprs:
            if i.is_escaped():
                fields.append([i.get_name()])
            else:
                fields.append(i.get_name().split('.'))
        return fields
        
    def execute(self, data:Results):
        fields = self.gen_fields()

        cols = []
        for i in fields:
            cols.append(pltools.get_element(data, i))
            
        new = pltools.merge(cols)
        
        return new