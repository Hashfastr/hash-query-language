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

@register_op('ProjectAway')
class ProjectAway(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        self.non_conseq = [
            'Take'
        ]
        
    def eval(self, ctx:Context, **kwargs):
        paths = []
        for i in self.exprs:
            paths.append(i.eval(ctx, as_list=True))
            
        return ctx.data.drop_many(paths)

@register_op('ProjectKeep')
class ProjectKeep(Operator):
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

@register_op('ProjectReorder')
class ProjectReorder(Operator):
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

@register_op('ProjectRename')
class ProjectRename(Operator):
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