from __future__ import annotations
from typing import Optional, TYPE_CHECKING
from Hql.Operators.Operator import Operator
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Context import Context

class Union(Operator):
    """Merge tables selected by one or more name expressions."""

    def __init__(self, exprs:list[Expression], name:Optional[Expression]=None):
        Operator.__init__(self)
        self.exprs = exprs
        self.name = name

        if not self.exprs:
            raise hqle.CompilerException('Union without expressions')

    def deparse(self) -> str:
        exprs = []
        for i in self.exprs:
            exprs.append(i.deparse())
        out = 'union ' + ', '.join(exprs)
        if self.name:
            out += ' as '
            out += self.name.deparse()
        return out

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'type': self.type,
            'exprs': [x.to_dict() for x in self.exprs],
            'name': self.name.to_dict() if self.name else None
        }

    def eval(self, ctx:Context, **kwargs):
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
