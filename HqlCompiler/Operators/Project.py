from HqlCompiler.Expression import Expression
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
import polars as pl

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
        op = Project(self.exprs)
        return op.eval(ctx)

@register_op('ProjectReorder')
class ProjectReorder(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        self.non_conseq = [
            'Take'
        ]
    
    '''
    Gonna take out the specific bits and move them to the front
    '''
    def eval(self, ctx:Context, **kwargs):
        new = []
        cur = ctx.data
        
        for expr in self.exprs:
            path = expr.eval(ctx, as_list=True)
            new.append(cur.select(path))
            cur = cur.drop(path)
        
        new.append(cur)
        
        return Data.merge(new)

@register_op('ProjectRename')
class ProjectRename(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        self.non_conseq = [
            'Take'
        ]

    def rename(self, ctx:Context, table:Table):
        for i in self.exprs:
            vpath = i.value.eval(ctx, as_list=True)
            value = table.get_value(vpath)
            vtype = table.schema.get_type(vpath)

            table.drop(vpath)

            for j in i.paths:
                dest = j.eval(ctx, as_list=True)
                table.insert(dest, value, vtype)

        return table
        
    def eval(self, ctx:Context, **kwargs):
        for table in ctx.data:
            self.rename(ctx, table)

        return ctx.data
