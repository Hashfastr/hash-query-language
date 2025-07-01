from .__proto__ import Expression
from HqlCompiler.Context import Context
from HqlCompiler.Exceptions import CompilerException
from HqlCompiler.PolarsTools import pltools

import polars as pl

# Expression expressing anything with ==, >, <, <=, >=, !=, etc
# has a left and right hand expression along with it's type.
class Equality(Expression):
    def __init__(self, type:str, lh:Expression, rh:Expression):
        super().__init__()
        self.eqtype = type
        self.lh:Expression = lh
        self.rh:Expression = rh
    
    def to_dict(self):
        return {
            'type': self.type,
            'eqtype': self.eqtype,
            'lh': self.lh.to_dict(),
            'rh': self.rh.to_dict()
        }
    
    # Generates a polars filter
    def eval(self, ctx:Context, **kwargs):
        as_pl = kwargs.get('as_pl', True)
        
        lh = self.lh.eval(ctx, as_pl=as_pl)
        rh = self.rh.eval(ctx, as_pl=as_pl)
        
        if as_pl:
            if self.eqtype == '==':
                return (lh == rh)

            if self.eqtype == '!=' or self.eqtype == '<>':
                return (lh != rh)
        
        raise CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

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
    def __init__(self, lh:Expression, type:str, rh:list[Expression]):
        super().__init__()
        self.lh = lh
        self.type = type
        self.rh = rh
    
    def to_dict(self):
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }
        
    def eval(self, ctx:Context, **kwargs):
        as_pl = kwargs.get('as_pl', True)
        
        lh = self.lh.eval(ctx, as_list=True)
        lh = pltools.path_to_expr_value(lh)
        
        filts = []
        for rh in self.rh:
            if not rh.literal:
                rh = rh.eval(ctx, as_list=True)
            
            if rh.literal:
                filt = (lh == rh.value)
                
            elif hasattr(rh, 'gen_filter'):
                filt = rh.gen_filter(lh)
                
            else:
                filt = (lh == pltools.path_to_expr_value(rh))
                
            filts.append(filt)
            
        final = filts[0].or_(*filts[1:])
                
        if as_pl:
            return final
        
        else:
            raise CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

# Handles relational expressions
# - <
# - >
# - <=
# - >=
#
# As per the grammar
# Takes after the equality expression
class Relational(Equality):
    def eval(self, ctx: Context, **kwargs):
        as_pl = kwargs.get('as_pl', True)

        lh = self.lh.eval(ctx, as_pl=as_pl)
        rh = self.rh.eval(ctx, as_pl=as_pl)

        if as_pl:
            if self.eqtype == '<':
                return (lh < rh)
            
            if self.eqtype == '>':
                return (lh > rh)
            
            if self.eqtype == '<=':
                return (lh <= rh)
            
            if self.eqtype == '>=':
                return (lh >= rh)

        raise CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

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
    
    def eval(self, ctx:Context, **kwargs):
        as_pl = kwargs.get('as_pl', True)
        
        lh = self.lh.eval(ctx, as_pl=True)
        start = self.start.eval(ctx, as_pl=True)
        end = self.end.eval(ctx, as_pl=True)
        
        filt = lh.is_between(start, end)
        
        if self.negate:
            filt = filt.not_()
        
        if as_pl:
            return filt
        
        else:
            raise CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

# Handles binary logic
# - and
# - or
# Right hand is a list as that's how it's handled
# If there is 3 items in the right list it is equal to
# a and b and c and d
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
        
    def eval(self, ctx:Context, **kwargs):
        lh = self.lh.eval(ctx, as_pl=True)
        
        rh = []
        for i in self.rh:
            rh.append(i.eval(ctx, as_pl=True))    
        
        filt = lh
        for i in rh:
            if self.bitype == 'and':
                filt = filt and i
            else:
                filt = filt or i
                
        return (filt)

class BasicRange(Expression):
    def __init__(self, start, end):
        Expression.__init__(self)
        self.start = start
        self.end = end
        
    def gen_filter(self, lh:pl.Expr):
        return (lh > self.start).and_(lh < self.end)
