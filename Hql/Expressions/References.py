from .__proto__ import Expression
from Hql.PolarsTools import pltools
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Data import Data, Table, Series
import polars as pl

from typing import TYPE_CHECKING, Sequence, Union, Optional
import logging

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Functions import Function
    from Hql.Data import Data

class Reference(Expression):
    def __init__(self):
        Expression.__init__(self)

    def polars(self) -> 'pl.Expr':
        return NotImplemented

    def polars_value(self) -> 'pl.Expr':
        return NotImplemented

    def polars_reference(self) -> 'pl.Expr':
        return NotImplemented
    
    def get_symbol(self, ctx:'Context'):
        return NotImplemented

# A named reference, can be scoped
# Scopes are not implemented yet.
class NamedReference(Reference):
    def __init__(self, name:str):
        Reference.__init__(self)
        self.name = name

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, NamedReference):
            return self.name == value.name
        return super().__eq__(value)

    def __hash__(self):
        return hash((self.name))

    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'name': self.name,
        }

    def get_symbol(self, ctx:'Context'):
        return ctx.symbol_table.get(self.name, None)

    def deparse(self) -> str:
        return self.name

    def str(self) -> str:
        return self.name

    def list(self) -> list[str]:
        return [self.name]

    def polars(self) -> 'pl.Expr':
        return pl.col(self.name)

    def polars_value(self) -> 'pl.Expr':
        return pl.col(self.name)

    def eval(self, ctx: 'Context', unnest:bool=False) -> 'Context':
        if unnest:
            ctx.data = ctx.data.unnest(self)
        else:
            ctx.data = ctx.data.select(self)
        return ctx
        
class EscapedNamedReference(NamedReference):
    def deparse(self) -> str:
        from Hql.Expressions import StringLiteral
        return "[" + StringLiteral(self.name).quote("'") + "]"

# Why again?
# class HacNamedReference(NamedReference):
#     ...

class Path(Reference):
    def __init__(self, path:Sequence[Union[NamedReference, Path]]):
        Reference.__init__(self)

        new = []
        for i in path:
            if isinstance(i, NamedReference):
                new.append(i)
            else:
                new += i.path

        self.path:list[NamedReference] = new

        if not self.path:
            raise hqle.CompilerException('Attempting to init path with 0 path parts')

    # allows for collapsing single length paths
    def __new__(cls, path:list):
        if len(path) == 1:
            return path[0]
        return super().__new__(cls)

    # for copying/pickling
    def __reduce__(self):
        return (self.__class__, (self.path))

    def __iter__(self):
        return iter(self.path)

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, Path):
            return super().__eq__(value)

        if len(self.path) != len(value.path):
            return False

        for i in range(len(self.path)):
            if self.path[i] != value.path[i]:
                return False
        return True

    def __hash__(self):
        return hash(tuple([x.__hash__() for x in self.path]))
      
    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'path': [x.to_dict() for x in self.path]
        }

    def deparse(self) -> str:
        return '.'.join([x.deparse() for x in self.path])

    def str(self) -> str:
        return self.deparse()

    def list(self) -> list[str]:
        return [x.str() for x in self.path]

    def polars(self) -> 'pl.Expr':
        expr = self.polars_value()
        for i in self.path[::-1][1:]:
            expr = pl.struct(expr).alias(i.str())
        return expr

    def polars_value(self) -> 'pl.Expr':
        expr = self.path[0].polars_value()
        for i in self.path[1:]:
            expr = expr.struct.field(i.str())
        return expr

    def eval(self, ctx: 'Context', unnest:bool=False) -> 'Context':
        if unnest:
            ctx.data = ctx.data.unnest(self)
        else:
            ctx.data = ctx.data.select(self)
        return ctx

'''
Sets a name a value

ip_addr = ip4(destination.ip)
'''
class NamedExpression(Expression):
    def __init__(self, paths:list[Reference], value:Union[Expression, Function]):
        Expression.__init__(self)
        self.paths = paths
        self.value = value

    def __eq__(self, value: object, /) -> bool:
        if not isinstance(value, NamedExpression):
            return super().__eq__(value)

        if len(self.paths) != len(value.paths):
            return False

        # Create a shallow copy
        # Unordered comparison
        value_paths = [x for x in value.paths]
        for i in self.paths:
            if i in value_paths:
                value_paths.remove(i)
            else:
                return False

        if value_paths:
            return False

        if self.value != value.value:
            return False

        return True

    def to_dict(self):        
        return {
            'type': self.type,
            'name': [x.to_dict() for x in self.paths],
            'value': self.value.to_dict()
        }

    def deparse(self) -> str:
        paths = []
        for i in self.paths:
            paths.append(i.deparse())

        lh = ', '.join(paths)
        value = self.value.deparse()

        return f'{lh}={value}'

    def can_polars(self) -> bool:
        from Hql.Functions import Function
        if isinstance(self.value, Function):
            return False
        return True

    def polars(self) -> 'pl.Expr':
        if isinstance(self.value, Function):
            logging.error(self.deparse())
            raise hqle.CompilerException(f'Attempting to polars non-polars expression')

        value = self.polars_value()
        exprs = []

        for i in self.paths:
            i.polars()

        return 

    def polars_value(self) -> 'pl.Expr':
        if isinstance(self.value, Function):
            logging.error(self.deparse())
            raise hqle.CompilerException(f'Attempting to polars non-polars expression')
        return self.value.polars()

    def eval(self, ctx:'Context', insert:bool=True) -> 'Context':
        from Hql.Expressions import Literal

        if isinstance(self.value, Literal):
            series = self.value.series()
            value = Data()
            for i in ctx.data:
                value.add_table(Table(name=i.name, series=series))
        else:
            value = self.value.eval(ctx)

        if not isinstance(value, Data):
            raise hqle.CompilerException(f'Named expression right hand {self.value} returned non-Data object {type(value)}')
        
        if as_value:
            return value
        
        # Chose which dataset to insert on
        # If set to false it'll create it's own blank dataset
        if insert:
            data = ctx.data
        else:
            data = Data()

        # loop through value tables as those are the only ones we can vouch for
        for table in value:
            # Need this if we're creating a new dataset instead of inserting
            if table.name not in data.tables:
                data.add_table(Table(name=table.name))
            
            # We can assign to multiple names
            for path in self.paths:
                path = path.eval(ctx, as_list=True)
                
                cur = table

                if cur.series:
                    # Get the series and set the type
                    schema = cur.series.type
                    cur = cur.series.series
                    
                else:
                    # Get the value of the dataframe and schema
                    cur = cur.strip()

                    if len(cur.df):
                        schema = cur.schema
                        cur = cur.df

                    elif cur.series:
                        schema = cur.series.type
                        cur = cur.series.series

                    else:
                        continue

                # Insert properly
                data.tables[table.name].insert(path, cur, schema)

        # print(data.to_dict())

        return data
