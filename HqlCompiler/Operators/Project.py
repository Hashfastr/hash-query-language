from HqlCompiler.Expression import Expression
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator

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
        
    def eval(self, ctx:Context, **kwargs):
        datasets = []
        for i in self.exprs:
            datasets.append(i.eval(ctx, as_value=False))
                
        return Data.merge(datasets)