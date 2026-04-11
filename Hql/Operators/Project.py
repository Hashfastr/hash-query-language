from Hql.Data import Data, Table
from Hql.Context import Context
from Hql.Operators import Operator
from typing import Sequence, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Reference, NamedExpression

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
    def __init__(self, optok:str, exprs:Sequence[Union['Reference', 'NamedExpression']]):
        Operator.__init__(self)
        self.exprs = exprs
        self.optok = optok
    
    def deparse(self) -> str:
        out = self.optok

        if self.exprs:
            out += ' '
            exprs = []
            for i in self.exprs:
                exprs.append(i.deparse())
            out += ', '.join(exprs)

        return out
        
    def eval(self, ctx:'Context'):
        ctx = ctx.copy()

        datasets = []
        for i in self.exprs:
            if isinstance(i, 'NamedExpression'):
                datasets.append(i.eval(ctx, insert=False))
            else:
                datasets.append(i.eval(ctx))
                
        ctx.data = Data.merge(datasets)
        return ctx

# Identical to Project, keeping now for compat
class ProjectKeep(Project):
    ...

class ProjectAway(Project):
    def eval(self, ctx:'Context'):
        ctx = ctx.copy()

        paths = []
        for i in self.exprs:
            paths.append(i.list())
        
        ctx.data = ctx.data.drop_many(paths)
        return ctx

class ProjectReorder(Project):
    '''
    Gonna take out the specific bits and move them to the front
    '''
    def eval(self, ctx:'Context'):
        ctx = ctx.copy()
        right = ctx.data

        left = super().eval(ctx).data

        paths = []
        for expr in self.exprs:
            if isinstance(expr, 'NamedExpression'):
                paths += [x.list() for x in expr.paths]
            else:
                paths.append(expr.list())

        for path in paths:
            right = right.drop(path)

        ctx.data = Data.merge([left, right])
        return ctx

class ProjectRename(Project):
    def rename(self, ctx:'Context', table:Table):
        for i in self.exprs:
            vpath = i.value.eval(ctx, as_list=True)
            value = table.get_value(vpath)
            vtype = table.schema.get_type(vpath)

            table.drop(vpath)

            for j in i.paths:
                dest = j.eval(ctx, as_list=True)
                table.insert(dest, value, vtype)

        return table
        
    def eval(self, ctx:'Context'):
        def rename(table:Table, dest:'Reference', src:'Reference') -> Table:
            destl = dest.list()
            srcl = src.list()
            
            value = table.get_value(srcl)
            vtype = table.get_type(srcl)
            table.drop(src)
            table.insert(destl, value, vtype)

            return table

        for table in ctx.data:
            self.rename(ctx, table)

        return ctx.data
