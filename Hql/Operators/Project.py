from Hql.Data import Data, Table
from Hql.Context import Context
from Hql.Operators.Operator import Operator
from Hql.Exceptions import HqlExceptions as hqle
from typing import Sequence, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Expressions.References import Reference, NamedExpression

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
    _exprs: Sequence[Union['Reference', 'NamedExpression']]

    def __init__(self, exprs:Sequence[Union['Reference', 'NamedExpression']]):
        Operator.__init__(self)
        self.exprs = exprs
        self.optok = 'project'

    @property
    def exprs(self) -> Sequence[Union['Reference', 'NamedExpression']]:
        return self._exprs

    @exprs.setter
    def exprs(self, value:Sequence['Expression']) -> None:
        from Hql.Expressions.References import NamedExpression, Reference
        new:list[Union[Reference, NamedExpression]] = []
        for v in value:
            if not isinstance(v, (Reference, NamedExpression)):
                raise hqle.CompilerException('Setting Project exprs to non-Reference/NamedExpression')
            new.append(v)
        self._exprs = new

    def deparse(self) -> str:
        out = self.optok

        if self.exprs:
            out += ' ' + ', '.join(x.deparse() for x in self.exprs)

        return out

    def eval(self, ctx:'Context') -> 'Context':
        from Hql.Expressions.References import NamedExpression

        ctx = ctx.copy()

        datasets = []
        for i in self.exprs:
            if isinstance(i, NamedExpression):
                datasets.append(i.eval(ctx, insert=False))
            else:
                datasets.append(i.eval(ctx))

        ctx.data = Data.merge(datasets)
        return ctx

# Identical to Project, keeping now for compat
class ProjectKeep(Project):
    def __init__(self, exprs: Sequence[Union['Reference', 'NamedExpression']]):
        super().__init__(exprs)
        self.optok = 'project-keep'

class ProjectAway(Project):
    def __init__(self, exprs: Sequence[Union['Reference', 'NamedExpression']]):
        super().__init__(exprs)
        self.optok = 'project-away'

    def eval(self, ctx:'Context') -> 'Context':
        ctx = ctx.copy()

        paths = [i.list() for i in self.exprs]
        ctx.data = ctx.data.drop_many(paths)
        return ctx

class ProjectReorder(Project):
    def __init__(self, exprs: Sequence[Union['Reference', 'NamedExpression']]):
        super().__init__(exprs)
        self.optok = 'project-reorder'

    '''
    Gonna take out the specific bits and move them to the front
    '''
    def eval(self, ctx:'Context') -> 'Context':
        from Hql.Expressions.References import NamedExpression

        ctx = ctx.copy()
        right = ctx.data

        left = super().eval(ctx).data

        paths = []
        for expr in self.exprs:
            if isinstance(expr, NamedExpression):
                paths += [x.list() for x in expr.paths]
            else:
                paths.append(expr.list())

        for path in paths:
            right = right.drop(path)

        ctx.data = Data.merge([left, right])
        return ctx

class ProjectRename(Project):
    def __init__(self, exprs: Sequence[Union['Reference', 'NamedExpression']]):
        super().__init__(exprs)
        self.optok = 'project-rename'

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

    def eval(self, ctx:'Context') -> 'Context':
        for table in ctx.data:
            self.rename(ctx, table)

        return ctx
