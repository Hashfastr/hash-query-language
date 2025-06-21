import logging
import json
from .Operators import Operator
import polars as pl
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators.Database import Database
from HqlCompiler.Context import Context
from HqlCompiler.PolarsTools import pltools
from HqlCompiler.Functions import Function
from HqlCompiler.Data import Data, Table, Schema
from enum import Enum
from HqlCompiler.Types.Hql import HqlTypes as hqlt

# An expression is any grouping of other expressions
# Typically children of an operation, an expression can also contain operators itself
# Such as a subsearch, which is an expression, and contains operators
# All other expressions are children of this one
class Expression():
    def __init__(self):
        self.type = self.__class__.__name__
        self.escaped = False
        self.name = []
    
    def to_dict(self):
        return {}
    
    # List of strings, mainly showing a path for nested names
    def get_name(self) -> list[str]:
        return self.name
    
    def eval(self, ctx:Context, **kwargs):
        return None
    
    def is_escaped(self):
        return self.escaped
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()
    
class PipeExpression(Expression):
    def __init__(self, prepipe:Expression=None, pipes:list[Operator]=None):
        super().__init__()
        self.prepipe = prepipe
        self.pipes = pipes if pipes else []
        self.compiled = []
        self.op_sets = []
        
    def to_dict(self):
        return {
            'type': self.type,
            'prepipe': self.prepipe.to_dict(),
            'pipes': [x.to_dict() for x in self.pipes]
        }
    
    # Compiles a pipe expression into a set of optimized Operators
    # Or alternatively into logic, e.g. (a and b)
    def eval(self, ctx:Context, **kwargs):        
        prepipe = self.prepipe.eval(ctx.data)
        self.compiled.append(prepipe)
        self.op_sets.append([prepipe.type])
        
        # can add more tabular prepipe types here
        if not issubclass(type(prepipe), (Database)) and self.pipes != []:
            raise CompilerException(f'Attempting to use a non-tabular expression with pipe expression {self.pipes[0].type}')
        
        for op in self.pipes:
            i = -1
            while i >= -len(self.compiled):
                nonconseq = self.compiled[i].non_consequential(op.type)
                integrate = self.compiled[i].can_integrate(op.type)
                    
                if nonconseq and not integrate:
                    logging.debug(f'Can optimize {op.type} passing {self.compiled[i].type}')
                    i -= 1
                if integrate:
                    logging.debug(f'Integrating {op.type} into {self.compiled[i].type}')
                    self.compiled[i].add_op(op)
                    self.op_sets[i].append(op.type)
                    break
                elif not nonconseq and not integrate:
                    logging.debug(f'As high as we can go for type {op.type}')
                    self.compiled.append(op)
                    self.op_sets.append([op.type])
                    break

# Expression expressing anything with ==, >, <, <=, >=, !=, etc
# has a left and right hand expression along with it's type.
class Equality(Expression):
    def __init__(self, type:str, lh:Expression, rh:Expression):
        super().__init__()
        self.eqtype = type
        self.lh = lh
        self.rh = rh
    
    def to_dict(self):
        return {
            'type': self.type,
            'eqtype': self.eqtype,
            'lh': self.lh.to_dict(),
            'rh': self.rh.to_dict()
        }
    
    # # Generates a polars filter
    # def eval(self, **kwargs):
    #     lh = 

# List equality
# Essenitally a filter stating that a field should have any value in a tuple.
# 
# | where event.code in (10, 11, 13, 3)
#
# is semantically identical to
#
# | where event.code == 10 or event.code == 11 or event.code == 13 or event.code == 3
#
# But is much easier to write and read
class ListEquality(Expression):
    def __init__(self, lh:Expression, rh:list[Expression]):
        super().__init__()
        self.lh = lh
        self.rh = rh
    
    def to_dict(self):
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }


# Data range functionality
# Left hand side is the expression to evaluate in being between two values.
# The right hand has a start and end expression showing the range of the values.
#
# | where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
# 
# Here lh is the '@timestamp' escaped string literal, and the right hand has
# the start and end values for the time range.
class BetweenEquality(Expression):
    def __init__(self, lh:Expression, start:Expression, end:Expression, negate:str="BETWEEN"):
        super().__init__()
        self.lh = lh
        self.start = start
        self.end = end
        self.negate = True if negate == "NOT_BETWEEN" else False
    
    def to_dict(self):
        return {
            'type': self.type,
            'negate': self.negate,
            'lh': self.lh.to_dict(),
            'rh': {
                'start': self.start.to_dict(),
                'end': self.end.to_dict()
            }
        }

# A named reference, can be scoped
# Scopes are not implemented yet.
class NamedReference(Expression):
    def __init__(self, name:str, scope:str=""):
        super().__init__()
        self.name = name
        self.scope = scope

    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name,
            'scope': self.scope,
        }
        
    def get_symbol(ctx:Context, name:str):
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

# A string literal
# literally a string
# we strip off quotes when constructing as the parser doesn't remove them for us.
class StringLiteral(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = value.strip('"').strip("'")
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

# Integer
# An integer
# Z
# unreal, not real
class Integer(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = int(value)
    
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class Float(Expression):
    def __init__(self, value:str):
        Expression.__init__(self)
        self.value = float(value)
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class Bool(Expression):
    def __init__(self, value:str):
        super().__init__()
        self.value = value.lower() == 'true'
        
    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value
        }
        
    def eval(self, ctx:Context, **kwargs):
        return self.value

class FuncExpr(Expression):
    def __init__(self, name:Expression, args:list=None):
        super().__init__()
        self.name = name
        self.args = args if args else []
    
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'args': [x.to_dict() for x in self.args]
        }
    
    # Evals to function objects
    def eval(self, ctx:Context, **kwargs):
        if kwargs.get('as_list', False):
            return self.name.eval(ctx, as_list=True)
        
        if kwargs.get('as_str', False):
            return self.name.eval(ctx, as_str=True)
        
        func = ctx.get_func(self.name.eval(ctx, as_str=True))
        logging.debug(f'Resolved func {func}')

        return func(self.args)
        
class DotCompositeFunction(Expression):
    def __init__(self, funcs:list[FuncExpr]):
        super().__init__()
        self.funcs = funcs
    
    def to_dict(self):
        return {
            'type': self.type,
            'funcs': [x.to_dict() for x in self.funcs]
        }
        
    def gen_list(self, ctx:Context):
        func_list = []
        for i in self.funcs:
            func_list.append(i.eval(ctx, as_str=True))
            
        return func_list

    # Evals to the function objects that can be executed
    def eval(self, ctx:Context, **kwargs):
        receiver = kwargs.get('receiver', None)
        no_exec = kwargs.get('no_exec', False)
        
        if kwargs.get('as_list', False):
            return self.gen_list(ctx)
        
        if kwargs.get('as_str', False):
            return '.'.join(self.gen_list(ctx))

        func_list = []
        for i in self.funcs:
            func = i.eval(ctx)
            func_list.append(func)
            
            if not no_exec:
                receiver = func.eval(ctx, receiver=receiver)
         
        if no_exec:
            return func_list
        else:
            return receiver

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
    
    def eval(self, ctx:Context, **kwargs):
        as_list = kwargs.get('as_list', False)
        as_pl = kwargs.get('as_pl', False)
        as_str = kwargs.get('as_str', False)
        as_value = kwargs.get('as_value', True)
        
        if as_list or as_pl or as_str:
            list = [x.eval(ctx, as_str=True) for x in self.path]
        
        if as_pl:
            return pltools.path_to_expr(list)

        if as_list:
            return list
        
        if as_str:
            return '.'.join(list)
        
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
    
class BinaryLogic(Expression):
    def __init__(self, lh:Expression, rh:list[Expression], type:str):
        super().__init__()
        self.bitype = type.lower()
        self.lh = lh
        self.rh = rh
        
    def to_dict(self):
        return {
            'type': self.type,
            'bitype': self.bitype,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }
        
    # def eval(self, ctx:Context, **kwargs):
        

class OpParameter(Expression):
    def __init__(self, name:str, value:Expression):
        super().__init__()
        self.name = name
        self.value = value
        
    def to_dict(self):        
        return {
            'name': self.name,
            'value': self.value.to_dict()
        }

class NamedExpression(Expression):
    def __init__(self, paths:list[Expression], value:Expression):
        super().__init__()
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
        for table in value.tables:
            # Need this if we're creating a new dataset instead of inserting
            if table not in data.tables:
                data.add_table(Table(name=table))
            
            # We can assign to multiple names
            for path in self.paths:
                path = path.eval(ctx, as_list=True)
                
                cur = value.tables[table]
                
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
                data.tables[table].insert(path, cur, schema)

        return data

class OrderedExpression(Expression):
    def __init__(self, name:Expression=None, order:str='desc', nulls:str=''):
        super().__init__()
        self.name = name
        self.order = order
        
        if nulls == '':
            if order == 'asc':
                self.nulls = 'first'
            if order == 'desc':
                self.nulls = 'last'
        else:
            self.nulls = nulls
        
    def to_dict(self):
        return {
            'name': self.name.to_dict(),
            'order': self.order,
            'nulls': self.nulls
        }

class ByExpression(Expression):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        
    def build_table_agg(self, ctx:Context, table:Table):
        paths = []
        schema = []
        for expr in self.exprs:
            path = expr.eval(ctx, as_list=True)
            ptype = table.schema.get_type(path)
            
            # if isinstance(ptype, hqlt.multivalue):
                
            
            paths.append(path)
            schema.append(table.schema.select(path))
        
        pl_exprs = []
        for expr in self.exprs:
            pl_expr = expr.eval(ctx, as_pl=True)
            
            if not table.assert_field(path):
                continue

            pl_exprs.append(pl_expr)
        
        # Groups and coelesces the schemas together for each field
        # Probably need to rework and change maintain_order here in the future
        # Without it, it fucks up the aggregation functions but is much faster
        table.agg = table.df.group_by(pl_exprs, maintain_order=True)
        table.agg_paths = paths
        table.agg_schema = Schema.merge(schema)
        
        return table
    
    def eval(self, ctx:Context, **kwargs):
        new = []
        
        for table in ctx.data.tables:
            new.append(self.build_table_agg(ctx, ctx.data.tables[table]))
            
        return Data(tables_list=new)

class LetExpression(Expression):
    def __init__(self, name:Expression, value:Expression):
        Expression.__init__(self)
        self.name = name
        self.value = value
        
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'value': self.value.to_dict()
        }
        
    def eval(self, ctx:Context, **kwargs):
        name = self.name.eval(ctx, as_str=True)
                
        if kwargs.get('no_exec', False):
            ctx.symbol_table[name] = self.value
        else:
            ctx.symbol_table[name] = self.value.eval(ctx)

class TypeExpression(Expression):
    def __init__(self, type:str):
        Expression.__init__(self)
        self.type = type
        
    def eval(self):
        return hqlt.from_name(self.type)

class ToExpression(Expression):
    def __init__(self, expr:Expression, to:hqlt.HqlType):
        Expression.__init__(self)
        self.expr = expr
        self.to = to
        
    def to_dict(self):
        return {
            'type': self.type,
            'expr': self.expr.to_dict(),
            'to': self.to.name
        }
        
    def eval(self, ctx:Context, **kwargs):
        as_list = kwargs.get('as_list', False)
        as_str = kwargs.get('as_str', False)
        
        if as_list or as_str:
            return self.expr.eval(ctx, as_list=as_list, as_str=as_str)
        
        path = self.expr.eval(ctx, as_path=True)
        
        new = []
        for name in ctx.data.tables:
            table = ctx.data.tables[name].cast_in_place(path, self.to)
            new.append(table)
        
        return Data(tables_list=new)