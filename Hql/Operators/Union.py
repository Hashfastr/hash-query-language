from typing import Optional
from Hql.Operators import Operator
from Hql.Expressions import Expression
from Hql.Context import register_op, Context
from Hql.Exceptions import HqlExceptions as hqle

class Union(Operator):
    def __init__(self, exprs:list[Expression], name:Optional[Expression]=None):
        Operator.__init__(self)
        self.exprs = exprs
        self.name = name

    def decompile(self, ctx: 'Context', split: bool = False) -> str:
        exprs = []
        for i in self.exprs:
            exprs.append(i.decompile(ctx))
        return 'union ' + ', '.join(exprs)

    def eval(self, ctx:'Context', **kwargs):
        from Hql.Data import Data, Table
        patterns = []
        for i in self.exprs:
            pattern = i.eval(ctx, as_str=True)
            if not isinstance(pattern, str):
                raise hqle.QueryException(f'Passed non-str expression to Union operator: {i.decompile(ctx)}')
            patterns.append(pattern)

        ignore = dict()
        for i in ctx.data:
            ignore[i.name] = i
        merge = []

        for i in patterns:
            for j in ctx.data.get_tables(i):
                if j.name in ignore:
                    merge.append(ignore.pop(j.name))

        new = Table.merge(merge, merge_rows=False)
        if self.name:
            name = self.name.eval(ctx, as_str=True)
            assert isinstance(name, str)
            new.name = name

        tables = [new]
        for i in ignore:
            tables.append(ignore[i])

        return Data(tables)
