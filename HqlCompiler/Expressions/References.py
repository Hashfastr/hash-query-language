from .__proto__ import Expression
from HqlCompiler.Context import Context
from HqlCompiler.PolarsTools import pltools
from HqlCompiler.Exceptions import QueryException, CompilerException
from HqlCompiler.Data import Data, Table
import logging

# A named reference, can be scoped
# Scopes are not implemented yet.
class NamedReference(Expression):
    def __init__(self, name:str, scope:str=""):
        Expression.__init__(self)
        self.name = name
        self.scope = scope

    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name,
            'scope': self.scope,
        }
        
    def get_symbol(self, ctx:Context, name:str):
        if name not in ctx.symbol_table:
            return None
        
        return ctx.symbol_table[name]
    
    def eval(self, ctx:Context, **kwargs):
        if kwargs.get('as_pl', False):
            return pltools.path_to_expr([self.name])

        if kwargs.get('as_list', False):
            return [self.name]
        
        if kwargs.get('as_str', False):
            return self.name
        
        as_value = kwargs.get('as_value', True)
        receiver = kwargs.get('receiver', ctx.data)
        receiver = receiver if receiver else ctx.data

        # Ensure we have the right field
        if receiver == None or not receiver.assert_field([self.name]):
            # Symbol table lookup
            # Named search or static value or the like
            if self.name in ctx.symbol_table:
                return ctx.symbol_table[self.name]
            
            raise QueryException(f"Referenced field {self.name} not found")
        
        # If we're operating on a dataset
        elif isinstance(receiver, Data):
            return receiver.unnest([self.name]) if as_value else receiver.select([self.name])
        
        # If we're operating on something that support variables
        elif hasattr(receiver, 'get_variable'):
            return receiver.get_variable(self.name)
        
        # Not implemented, or bug
        else:
            raise CompilerException(f'{type(receiver)} cannot have child named references!')
        
class EscapedNamedReference(NamedReference):
    ...
    
class Keyword(NamedReference):
    ...
    
class Identifier(NamedReference):
    ...
    
class Wildcard(NamedReference):
    ...

class Path(Expression):
    def __init__(self, path:list=None):
        super().__init__()
        self.path = path if path else []
      
    def to_dict(self):
        try:
            return {
                'type': self.type,
                'path': [x.to_dict() for x in self.path]
            }
        except Exception as e:
            logging.debug(self.path)
            logging.debug(e)

    def gen_list(self, ctx:Context):
        return [x.eval(ctx, as_str=True) for x in self.path]
    
    def eval(self, ctx:Context, **kwargs):
        as_list = kwargs.get('as_list', False)
        as_pl = kwargs.get('as_pl', False)
        as_str = kwargs.get('as_str', False)
        as_value = kwargs.get('as_value', True)
        
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


class NamedExpression(Expression):
    def __init__(self, paths:list[Expression], value:Expression):
        Expression.__init__(self)
        self.paths = paths
        self.value = value
        
    def to_dict(self):        
        return {
            'type': self.type,
            'name': [x.to_dict() for x in self.paths],
            'value': self.value.to_dict()
        }
        
    def eval(self, ctx:Context, **kwargs):
        insert = kwargs.get('insert', True)
        as_value = kwargs.get('as_value', False)
        value = self.value.eval(ctx)
        
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
                    schema = cur.schema
                    cur = cur.df
                
                # Insert properly
                data.tables[table.name].insert(path, cur, schema)

        return data
