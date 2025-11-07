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

# A named reference, can be scoped
# Scopes are not implemented yet.
class NamedReference(Expression):
    def __init__(self, name:str, scope:Optional[Expression]=None):
        Expression.__init__(self)
        self.name = name
        self.scope = scope

    def to_dict(self):
        d:dict = {
            'type': self.type,
            'name': self.name,
        }

        if self.scope:
            d['scope'] = self.scope.to_dict()

        return d

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, NamedReference):
            return self.name == value.name
        return super().__eq__(value)

    def __hash__(self):
        return hash((self.name))

    def decompile(self, ctx: 'Context') -> str:
        decomp = self.name
        
        if self.scope:
            scope = self.scope.decompile(ctx)
            decomp += f' {scope}'

        return decomp

    def get_symbol(self, ctx:'Context', name:str):
        if name not in ctx.symbol_table:
            return None
        
        return ctx.symbol_table[name]
    
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decomp', False):
            return self.decompile(ctx)

        if kwargs.get('as_pl', False):
            return pltools.path_to_expr([self.name])

        if kwargs.get('as_list', False):
            return [self.name]
        
        if kwargs.get('as_str', False):
            return self.name

        if kwargs.get('sym_table', False) and self.name in ctx.symbol_table:
            return ctx.symbol_table[self.name]
        
        as_value = kwargs.get('as_value', True)
        receiver = kwargs.get('receiver', ctx.data)
        receiver = receiver if receiver else ctx.data

        # Ensure we have the right field
        if receiver == None or not receiver.assert_field([self.name]):
            # Symbol table lookup
            # Named search or static value or the like
            if self.name in ctx.symbol_table:
                return ctx.symbol_table[self.name]
            
            raise hqle.QueryException(f"Referenced field {self.name} not found")
        
        # If we're operating on a dataset
        elif isinstance(receiver, Data):
            return receiver.unnest([self.name]) if as_value else receiver.select([self.name])
        
        # If we're operating on something that support variables
        elif hasattr(receiver, 'get_variable'):
            return receiver.get_variable(self)
        
        # Not implemented, or bug
        else:
            raise hqle.CompilerException(f'{type(receiver)} cannot have child named references!')
        
class EscapedNamedReference(NamedReference):
    def decompile(self, ctx: 'Context') -> str:
        from Hql.Expressions import StringLiteral
        return "[" + StringLiteral(self.name).quote("'") + "]"
    
class Keyword(NamedReference):
    ...
    
class Identifier(NamedReference):
    ...
    
class Wildcard(NamedReference):
    ...

class HacNamedReference(NamedReference):
    ...

class Path(Expression):
    def __init__(self, path:Sequence[Union[NamedReference, Path]]):
        # if not isinstance(self, Path):
        #     return

        new = []
        for i in path:
            if isinstance(i, NamedReference):
                new.append(i)
            else:
                new += i.path

        Expression.__init__(self)
        self.path:list[NamedReference] = new

        if not self.path:
            raise hqle.CompilerException('Attempting to init path with 0 path parts')

    def __new__(cls, path:list):
        if len(path) == 1:
            return path[0]
        return super().__new__(cls)

    def __reduce__(self):
        return (self.__class__, (self.path,))

    def __iter__(self):
        return iter(self.path)
      
    def to_dict(self) -> Optional[dict]:
        try:
            return {
                'type': self.type,
                'path': [x.to_dict() for x in self.path]
            }
        except Exception as e:
            logging.debug(self.path)
            logging.debug(e)

    def decompile(self, ctx: 'Context') -> str:
        return '.'.join([x.decompile(ctx) for x in self.path])

    def gen_list(self, ctx:'Context'):
        return [x.eval(ctx, as_str=True) for x in self.path]

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, Path):
            if len(self.path) != len(value.path):
                return False

            for i in range(len(self.path)):
                if self.path[i] != value.path[i]:
                    return False

            return True
        return super().__eq__(value)

    def __hash__(self):
        return hash(tuple([x.__hash__() for x in self.path]))

    def eval(self, ctx:'Context', **kwargs):
        decomp = kwargs.get('decomp', False)
        as_list = kwargs.get('as_list', False)
        as_pl = kwargs.get('as_pl', False)
        as_str = kwargs.get('as_str', False)
        as_value = kwargs.get('as_value', True)

        if decomp:
            return self.decompile(ctx)
        
        if as_pl:
            return pltools.path_to_expr(self.gen_list(ctx))

        if as_list:
            return self.gen_list(ctx)
        
        if as_str:
            return '.'.join(self.gen_list(ctx))
        
        '''
        Quick note on this.
        If we have a path that looks like this:
        
        field1.field2.somefunc().field3
        
        We split and eval the first two path segments, then eval somefunc,
        then eval field3 as a path element of somefunc's output
        
        So in this case we would eval
        
        consumed = ['field1', 'field2']
        # eval consumed then some func, reset consumed
        consumed = ['field3']
        # eval new consumed on the output of somefunc
        '''        
        consumed = []
        
        receiver = ctx.data
        for i in self.path:
            if i.type == "DotCompositeFunction":
                if consumed:
                    # Get the value of the path elements consumed so far
                    receiver = receiver.unnest(consumed)
                
                # Evalute the function
                receiver = i.eval(ctx, receiver=receiver)
                
                # Reset consumed since we're now operating with function'd data
                consumed = []
            else:
                # Append another path element that we've consumed
                consumed.append(i.eval(ctx, receiver=receiver, as_str=True))
              
        # If we have static elements we need to evaluate on the current receiver
        if consumed:
            receiver = receiver.unnest(consumed) if as_value else receiver.select(consumed)
            
        return receiver

'''
Sets a name a value

ip_addr = ip4(destination.ip)
'''
class NamedExpression(Expression):
    def __init__(self, paths:list[Expression], value:Union[Expression, Function]):
        Expression.__init__(self)
        self.paths = paths
        self.value = value
        
    def to_dict(self):        
        return {
            'type': self.type,
            'name': [x.to_dict() for x in self.paths],
            'value': self.value.to_dict()
        }

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, NamedExpression):
            if len(self.paths) != len(value.paths):
                return False

            # Create a shallow copy
            # Unordered comparison
            value_paths = [x for x in value.paths]
            for i in self.paths:
                for j in value_paths:
                    if i == j:
                        value_paths.remove(j)
                        break

            if value_paths:
                return False

            if self.value != value.value:
                return False

            return True
        return super().__eq__(value)

    def decompile(self, ctx: 'Context') -> str:
        paths = []
        for i in self.paths:
            paths.append(i.decompile(ctx))

        lh = ', '.join(paths)
        value = self.value.decompile(ctx)

        return f'{lh}={value}'
        
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Expressions import Literal
        insert = kwargs.get('insert', False)
        as_value = kwargs.get('as_value', False)

        if isinstance(self.value, Literal):
            series = self.value.make_series()
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
