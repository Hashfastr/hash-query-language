from __future__ import annotations
from typing import TYPE_CHECKING, Optional
from Hql.Operators.Operator import Operator

if TYPE_CHECKING:
    from Hql.Expressions.References import NamedReference
    from Hql.Expressions.Literals import Literal
    from Hql.Context import Context
    from Hql.Types.Hql import HqlTypes

'''
Creates a simple datatable, essentially an inline dataframe/table
'''
class Datatable(Operator):
    def __init__(self, schema:list[tuple[NamedReference, HqlTypes.HqlType]], values:list[Literal], name:Optional[NamedReference]=None):
        Operator.__init__(self)
        self.values:list[Literal] = values
        self.schema:list[tuple[NamedReference, HqlTypes.HqlType]] = schema
        self.name:Optional[NamedReference] = name
        self.tabular:bool = True

    def to_dict(self):
        out = super().to_dict()
        out['schema'] = self.gen_schema().to_dict()
        return out

    def gen_schema(self) -> HqlTypes.object:
        from Hql.Types.Hql import HqlTypes

        d = dict()
        for i in self.schema:
            d[i[0].str()] = i[1]
        return HqlTypes.object(d)

    def deparse(self) -> str:
        width = len(self.schema)
        nvalues = len(self.values)

        schema = []
        for i in self.schema:
            schema.append(f'{i[0].deparse()}: {i[1].name}')
        schema = ', '.join(schema)

        values = []
        for i in range(0, nvalues, width):
            row = [x.deparse() for x in self.values[i:i+width]]
            values.append(', '.join(row))

        table = '    '
        table += ',\n    '.join(values)
        table += '\n'

        total  = f'datatable ({schema})\n'
        total += '[\n'
        total += table
        total += ']'

        if self.name:
            total += f' as {self.name.deparse()}'

        return total

    def eval(self, ctx:Context):
        from polars import DataFrame
        from Hql.Data import Data, Table, Schema

        ctx = ctx.copy()

        width = len(self.schema)
        nvalues = len(self.values)

        schema = self.gen_schema()
        keys = [x[0].str() for x in self.schema]

        data = dict()
        for i in range(width):
            rows = []
            for j in range(0, nvalues, width):
                rows.append(self.values[j + i].eval(ctx))
            data[keys[i]] = rows

        name = 'datatable'
        if self.name:
            name = self.name.str()

        table = Table(
            df=DataFrame(data),
            schema=Schema(schema=schema),
            name=name
        )
        ctx.data = Data(tables=[table])

        return ctx
