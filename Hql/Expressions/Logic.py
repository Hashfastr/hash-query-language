from .__proto__ import Expression
from .Functions import DotCompositeFunction, FuncExpr
from Hql.Context import Context
from Hql.Exceptions import HqlExceptions as hqle
from Hql.PolarsTools import pltools

from typing import Union
import logging
import polars as pl

# Expression expressing anything with ==, >, <, <=, >=, !=, etc
# has a left and right hand expression along with it's type.
class Equality(Expression):
    def __init__(self, type:str, lh:Expression, rh:Expression):
        super().__init__()
        self.eqtype = type
        self.lh:Expression = lh
        self.rh:Expression = rh
        self.logic = True
    
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
        
        raise hqle.CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

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
    def __init__(self, lh:Expression, op:str, rh:list[Expression]):
        super().__init__()
        self.lh = lh
        self.op = op
        self.rh = rh
        self.logic = True
    
    def to_dict(self):
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }

    def comparator(self, lh, rh=None):
        if rh == None:
            if self.op == 'in':
                return (lh)

            if self.op == '!in':
                return (pl.not_(lh))

        if self.op == 'in':
            return (lh == rh)

        if self.op == '!in':
            return (lh != rh)
        
    def eval(self, ctx:Context, **kwargs):
        as_pl = kwargs.get('as_pl', True)
        
        lh = self.lh.eval(ctx, as_list=True)

        if not (isinstance(lh, list) and lh and isinstance(lh[0], str)):
            raise hqle.CompilerException(f'List equality lh returns non-list[str]: {lh}')

        lh = pltools.path_to_expr_value(lh)
        
        filts = []
        for rh in self.rh:
            if isinstance(rh, FuncExpr) or isinstance(rh, DotCompositeFunction):
                rh = rh.eval(ctx)

            if rh == None:
                raise hqle.CompilerException('Given rh is NoneType')

            # path was returned from a function
            if isinstance(rh, list):
                rh = pltools.path_to_expr_value(rh)
                filt = self.comparator(lh, rh=rh)

            # Literal comparator
            elif rh.literal:
                filt = self.comparator(lh, rh=rh.value)
            
            # Logic comparator
            elif rh.logic:
                filt = self.comparator(rh.eval(ctx, lh=lh))
            
            # Expression we need to resolve
            else:
                rh = rh.eval(ctx, as_list=True)

                if not (isinstance(rh, list) and rh and isinstance(rh[0], str)):
                    raise hqle.CompilerException(f'List equality rh returns non-list[str]: {rh}')

                rh = pltools.path_to_expr_value(rh)
                filt = self.comparator(lh, rh=rh)
                
            filts.append(filt)
        
        if self.op == 'in':
            final = filts[0].or_(*filts[1:])
        
        else:
            final = filts[0].and_(*filts[1:])
                
        if as_pl:
            return final
        
        else:
            raise hqle.CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

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
            if not isinstance(lh, pl.Expr):
                raise hqle.CompilerException(f'Relational left hand {self.lh.type} returned non-polars expression')
            
            if not isinstance(rh, pl.Expr):
                raise hqle.CompilerException(f'Relational right hand {self.rh.type} returned non-polars expression')

            if self.eqtype == '<':
                return (lh < rh)
            
            if self.eqtype == '>':
                return (lh > rh)
            
            if self.eqtype == '<=':
                return (lh <= rh)
            
            if self.eqtype == '>=':
                return (lh >= rh)

        raise hqle.CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

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

        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'Between left hand {self.lh.type} returned non-polars expression')
        
        filt = lh.is_between(start, end)
        
        if self.negate:
            filt = filt.not_()
        
        if as_pl:
            return filt
        
        else:
            raise hqle.CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

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
        a
    def eval(self, ctx:Context, **kwargs):
        as_pl = kwargs.get('as_pl', True)
        if not as_pl:
            logging.critical(f'Odd kwargs passed to Binary Logic {kwargs}')
            raise hqle.CompilerException(f'BinaryLogic expression given as_pl=False in kwargs')

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
    def __init__(self, start:Expression, end:Expression):
        Expression.__init__(self)
        self.start = start
        self.end = end
        self.logic = True
    
    def eval(self, ctx: Context, **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
        lh = kwargs.get('lh', None)
        start = self.start.eval(ctx, as_pl=True)
        end = self.end.eval(ctx, as_pl=True)

        if isinstance(lh, type(None)):
            raise hqle.CompilerException('BasicRange given a NoneType left-hand expression!')

        return (lh > start).and_(lh < end)

class InsensitiveStringCmp(Expression):
    def __init__(self, lh:Expression, op:str, rh:Expression) -> None:
        Expression.__init__(self)
        self.cs = False
        self.lh = lh
        self.rh = rh
        self.neq = op == '!~'

    def eval(self, ctx: Context, **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
        as_pl = kwargs.get('as_pl', True)
        if not as_pl:
            logging.critical(f'Odd kwargs passed to InsensitiveStringCmp {kwargs}')
            raise hqle.CompilerException(f'InsensitiveStringCmp expression given as_pl=False in kwargs')
        
        lh = self.lh.eval(ctx, as_pl=True)
        
        if self.rh.literal:
            if self.rh.type != "StringLiteral":
                hqle.QueryException(f'Righthand {self.type} expression is not a string')

            rh = self.rh.value

        else:
            raise hqle.QueryException(f'Dynamic right hands not supported in {self.type} just yet')

        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'String binary left hand {self.lh.type} returned a non-polars expression ')

        # Case insensitive match
        expr = lh.str.contains(f'(?i){rh}')

        if self.neq:
            expr = pl.not_(expr)

        return expr

class Regex(Expression):
    def __init__(self, lh:Expression, rh:Expression) -> None:
        Expression.__init__(self)
        self.lh = lh
        self.rh = rh

    def eval(self, ctx: Context, **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
        as_pl = kwargs.get('as_pl', True)
        if not as_pl:
            logging.critical(f'Odd kwargs passed to Regex {kwargs}')
            raise hqle.CompilerException(f'Regex expression given as_pl=False in kwargs')
        
        lh = self.lh.eval(ctx, as_pl=True)
        
        if self.rh.literal:
            if self.rh.type != "StringLiteral":
                hqle.QueryException(f'Righthand {self.type} expression is not a string')

            rh = self.rh.value

        else:
            raise hqle.QueryException(f'Dynamic right hands not supported in {self.type} just yet')

        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'String binary left hand {self.lh.type} returned a non-polars expression ')

        if not (isinstance(rh, pl.Expr) and isinstance(rh, str)):
            raise hqle.CompilerException(f'Passed regex is not a string {rh}')

        return lh.str.contains(rh)

class Contains(Expression):
    def __init__(self, lh:Expression, op:str, rh:Expression) -> None:
        Expression.__init__(self)
        self.lh = lh
        self.op = op
        self.rh = rh
        self.startswith = False
        self.endswith = False

        self.term = 'has' in op
        self.neq = '!' in op
        self.cs = '_cs' in op

        if 'startswith' in op or 'prefix' in op:
            self.startswith = True
        
        if 'endswith' in op or 'suffix' in op:
            self.endswith = True

    def eval(self, ctx: Context, **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
        as_pl = kwargs.get('as_pl', True)
        if not as_pl:
            logging.critical(f'Odd kwargs passed to Contains {kwargs}')
            raise hqle.CompilerException(f'Contains expression given as_pl=False in kwargs')
        
        if self.term:
            logging.warning('Term matching with using has is not supported in Hql-land')
            logging.warning('Semantically equivalent to contains, no performance benefits')

        lh = self.lh.eval(ctx, as_pl=True)

        if self.rh.literal:
            if self.rh.type != "StringLiteral":
                hqle.QueryException(f'Righthand {self.type} expression is not a string')

            rh = self.rh.value

            if rh == None:
                raise hqle.CompilerException(f'Literal value is None for {self.rh.type}')

        else:
            raise hqle.QueryException(f'Dynamic right hands not supported in {self.type} just yet')

        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'String binary left hand {self.lh.type} returned a non-polars expression ')

        if not self.cs:
            rh = rh.lower()
            lh = lh.str.to_lowercase()

        if self.startswith:
            expr = lh.str.starts_with(rh)

        elif self.endswith:
            expr = lh.str.ends_with(rh)

        else:
            expr = lh.str.contains(rh)

        if self.neq:
            expr = pl.not_(expr)

        return expr
