import logging
import json
from .Operators import Operator
import polars as pl
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators.Database import Database
from HqlCompiler.Context import Context
from HqlCompiler.PolarsTools import PolarsTools
from HqlCompiler.Functions import Function

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
    def __init__(self, name:Expression, scope:str=""):
        super().__init__()
        self.name = name
        self.scope = scope
        
    def get_name(self):
        if hasattr(self.name, 'name'):
            return self.name.name
        else:
            return self.name
        
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'scope': self.scope,
        }
    
    def eval(self, ctx:Context, **kwargs):
        name_str = self.name.eval(ctx, as_str=True)
        
        if kwargs.get('as_str', False):
            return name_str
        
        if kwargs.get('list', False):
            return [name_str]
        
        receiver = kwargs.get('receiver', None)
        if receiver is not None:
            if type(receiver) == pl.DataFrame:
                return PolarsTools.get_element_value(ctx.data, [name_str])
            elif issubclass(type(receiver), Database):
                return receiver.get_variable(name_str)
            else:
                raise CompilerException(f'{type(receiver)} cannot have child named references!')
        
        return PolarsTools.get_element_value(ctx.data, [name_str])

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
        
class EscapedName(StringLiteral):
    def __init__(self, name:str):
        super().__init__(name)
        self.name = self.value
        self.escaped = True
        
    def to_dict(self):
        dict = super().to_dict()
        dict['escaped'] = self.escaped
        return dict
    
    def eval(self, ctx:Context, **kwargs):
        name_str = self.name
        
        if kwargs.get('as_str', False):
            return name_str
        
        if kwargs.get('list', False):
            return [name_str]
        
        receiver = kwargs.get('receiver', None)
        if receiver:
            if type(receiver) == pl.DataFrame:
                return PolarsTools.get_element_value(ctx.data, [name_str])
            elif issubclass(type(receiver), Database):
                return receiver.get_variable(name_str)
            else:
                raise CompilerException(f'{type(receiver)} cannot have child named references!')
            
        return PolarsTools.get_element_value(ctx.data, [name_str])

# An identifier is like a variable that is not unique across everything
# A keyword is unique across the compiler
# database('test').index('test')
# Here database is unique while index is not, multiple things can have a index child
class Identifier(Expression):
    def __init__(self, name:str, keyword:bool=False):
        super().__init__()
        self.name = name
        self.keyword = keyword
        
    def to_dict(self):
        return {
            'type': self.type,
            'keyword': self.keyword,
            'name': self.name
        }
    
    def eval(self, ctx:Context, **kwargs):
        if kwargs.get('as_str', False):
            return self.name
        
        if kwargs.get('list', False):
            return [self.name]
                
        receiver = kwargs.get('receiver', None)
        
        if receiver is not None:
            if isinstance(receiver, pl.DataFrame):
                return PolarsTools.get_element_value(receiver, [self.name])
            elif issubclass(type(receiver), Database):
                return receiver.get_variable(self.name)
            else:
                raise CompilerException(f'{type(receiver)} cannot have child named references!')
            
        return PolarsTools.get_element(ctx.data, [self.name])

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
    
    # def get_full_statement(self):
    #     args = []
    #     for i in self.args:
    #         if hasattr(i, 'get_name'):
    #             args.append(i.get_name())
    #         else:
    #             args.append(i.get_value())
        
    #     return self.name + f"({', '.join(args)})"
    
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'args': [x.to_dict() for x in self.args]
        }
    
    # Evals to function objects
    def eval(self, ctx:Context, **kwargs):        
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

    # Evals to the function objects that can be executed
    def eval(self, ctx:Context, **kwargs):
        receiver = kwargs.get('receiver', None)
        no_exec = kwargs.get('no_exec', False)
        
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
        if kwargs.get('list', False):
            return [x.eval(ctx, as_str=True) for x in self.path]
        
        as_str = kwargs.get('as_str', False)
        
        receiver = None
        for i in self.path:
            if i.type == "DotCompositeFunction":
                receiver = i.eval(ctx, receiver=receiver, as_str=as_str)
            else:
                receiver = i.eval(ctx, receiver=receiver, as_str=as_str)
        
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
    def __init__(self, name:Expression, value:Expression):
        super().__init__()
        self.name = name
        self.value = value
        
    def to_dict(self):        
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'value': self.value.to_dict()
        }
        
    def eval(self, ctx:Context, **kwargs):
        receiver = kwargs.get('receiver', None)
            
        data = self.value.eval(ctx)
        name = self.name.eval(ctx, list=True)
        return PolarsTools.build_element(name, data)
    
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