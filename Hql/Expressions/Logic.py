from .__proto__ import Expression
from Hql.Exceptions import HqlExceptions as hqle

from typing import TYPE_CHECKING, Union
import logging
import polars as pl

if TYPE_CHECKING:
    from Hql.Context import Context

class Comparator(Expression):
    def __init__(self, lh:Expression, op:str, rh:list[Expression]) -> None:
        Expression.__init__(self)

        self.lh = lh
        self.op = op
        self.rh = rh

        self.cs       = True
        self.neq      = False
        self.term     = False
        self.logic    = True

    def to_dict(self):
        return {
            'type': self.type,
            'cs': self.cs,
            'neq': self.neq,
            'term': self.term,
            'op': self.op,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }

'''
Handles the following direct comparators:
- ==/!=
- =~/!~
- in/!in
- in~/!in~
Not substring comparators
'''
class Equality(Comparator):
    def __init__(self, lh:Expression, op:str, rh:list[Expression]):
        Comparator.__init__(self, lh, op, rh)

        self.cs = '~' not in op
        self.neq = '!' in op

        self.list = 'in' in op

        if len(rh) > 1 and not self.list:
            raise hqle.CompilerException('Non-list equality given more than one righthand')

    def as_pl(self, ctx:'Context'):
        from Hql.Expressions import Literal, StringLiteral
        lh = self.lh.eval(ctx, as_pl=True)

        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'lh evaluated to non-pl.Expr type {type(lh)}')
        
        rh = []
        for i in self.rh:
            rh.append(i.eval(ctx, as_pl=True))

        expr = None
        for i in rh:
            if self.cs:
                new = (lh == i)
            else:
                i = pl.select(i.str.escape_regex()).item()
                regex = f'(?i)^{i}$'
                new = lh.str.contains(regex)

            if self.neq:
                new = ~new

            if isinstance(expr, type(None)):
                expr = new
            else:
                expr = (expr | new)

        if isinstance(expr, type(None)):
            raise hqle.CompilerException('Equality returned None expression')

        return expr

    def decompile(self, ctx):
        lh = self.lh.decompile(ctx)

        # Non-list decomp
        if len(self.rh) == 1 and not self.list:
            return f'{lh} {self.op} {self.rh[0].decompile(ctx)}'

        rh = []
        for i in self.rh:
            rh.append(i.decompile(ctx))

        rh = ', '.join(rh)

        return f'{lh} {self.op} ({rh})'
    
    # Generates a polars filter
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('as_pl', True):
            return self.as_pl(ctx)
        
        raise hqle.CompilerException(f'Unhandled kwarg as type, as_pl set to false {kwargs}')

'''
Handles the following term operators:
- has/has_cs
    - term substring
- has_all/has_all_cs
    - term substring list and
    - field has 'test' and field has 'foo'
- has_any/has_any_cs
    - term substring list or
    - field has 'test' or field has 'foo'
- hasprefix/hasprefix_cs
    - Term prefix/startswith
- hassuffix/hassuffix_cs
    - Term suffix/endswith

Non-term operators:
- contains/contains_cs
    - non-term substring
- contains_all/contains_all_cs
    - contains substring list and
    - field contains 'test' and field contains 'foo'
- contains_any/contains_any_cs
    - contains substring list or
    - field contains 'test' or field contains 'foo'
- startswith/startswith_cs
    - non-term prefix/startswith
- endswith/endswith_cs
    - non-term suffix/endswith
'''
class Substring(Comparator):
    def __init__(self, lh:Expression, op:str, rh:list[Expression]):
        Comparator.__init__(self, lh, op, rh)

        self.term = 'has' in op

        # only affects *_all, *_any right now
        self.logic_and = True if 'all' in op else False
        
        self.neq = op[0] == '!'
        self.cs = op.endswith('_cs')

        self.list = ('all' in op or 'any' in op)

        if len(rh) > 1 and not self.list:
            raise hqle.CompilerException('Non-list substring given multiple rh expressions')
 
    def to_dict(self):
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'op': self.op,
            'rh': [x.to_dict() for x in self.rh]
        }

    def has(self, ctx:'Context', lh:pl.Expr, rh:Expression):
        rh_str = rh.eval(ctx, as_str=True)
        if not isinstance(rh_str, str):
            raise hqle.CompilerException(f'Substring righthand returned non-str {type(rh_str)}')

        rh_str = pl.escape_regex(rh_str)

        regex = '' if self.cs else '(?i)'
        regex += rh_str

        return lh.str.contains(regex)

    # as_pl representation
    def prefix(self, ctx:'Context', lh:pl.Expr, rh:Expression, prefix:bool):
        rh_str = rh.eval(ctx, as_str=True)
        if not isinstance(rh_str, str):
            raise hqle.CompilerException(f'Substring righthand returned non-str {type(rh_str)}')

        # regex escape
        rh_str = pl.escape_regex(rh_str)
        
        regex = '' if self.cs else '(?i)'
        regex += '^' if prefix else ''
        regex += f'{rh_str}'
        regex += '' if prefix else '$'

        return lh.str.contains(regex)

    def all_any(self, ctx:'Context', lh:pl.Expr, rh:list[Expression]):
        exprs = []
        for i in rh:
            exprs.append(self.has(ctx, lh, i))

        expr = exprs[0]
        for i in exprs[1:]:
            expr = expr & i if 'all' in self.op else expr | i

        return expr

    def decompile(self, ctx: 'Context') -> str:
        lh = self.lh.decompile(ctx)

        # Non-list decomp
        if len(self.rh) == 1 and not self.list:
            return f'{lh} {self.op} {self.rh[0].decompile(ctx)}'

        rh = []
        for i in self.rh:
            rh.append(i.decompile(ctx))

        rh = ', '.join(rh)

        return f'{lh} {self.op} ({rh})'

    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('decomp', False):
            return self.decompile(ctx)

        as_pl = kwargs.get('as_pl', True)
        if not as_pl:
            raise hqle.CompilerException(f'{as_pl} in Substring comparator only supported as True')
        
        if self.term:
            logging.warning('Term matching not supported in Hql-land, do not expect increased performance')
        
        lh = self.lh.eval(ctx, as_pl=True)
        expr = None
        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'lh.eval() returned non-pl.Expr type {type(lh)}')

        if 'prefix' in self.op or 'startswith' in self.op:
            # no list right hand supported atm
            expr = self.prefix(ctx, lh, self.rh[0], True)

        if 'suffix' in self.op or 'endswith' in self.op:
            # no list right hand supported atm
            expr = self.prefix(ctx, lh, self.rh[0], False)

        if 'all' in self.op or 'any' in self.op:
            expr = self.all_any(ctx, lh, self.rh)

        if not isinstance(expr, type(None)):
            return ~expr if self.neq else expr

        raise hqle.CompilerException(f'Substring comparator got to the end of execution, unhandled operator {self.op} ?')

# Handles relational expressions
# - <
# - >
# - <=
# - >=
# As per the grammar
# Takes after the equality expression
class Relational(Comparator):
    def __init__(self, lh: Expression, op: str, rh: list[Expression]) -> None:
        Comparator.__init__(self, lh, op, rh)

        if len(self.rh) > 1:
            raise hqle.CompilerException(f'Relational expression given a incompatible number of right hand expressions {len(rh)} > 1')

    def decompile(self, ctx: 'Context') -> str:
        lh = self.lh.decompile(ctx)
        rh = self.rh[0].decompile(ctx)
        return f'{lh} {self.op} {rh}'

    def eval(self, ctx:'Context', **kwargs):
        as_pl = kwargs.get('as_pl', True)

        lh = self.lh.eval(ctx, as_pl=as_pl)
        # list right hand not supported atm
        rh = self.rh[0].eval(ctx, as_pl=as_pl)

        if as_pl:
            if not isinstance(lh, pl.Expr):
                raise hqle.CompilerException(f'Relational left hand {type(self.lh)} returned non-polars expression {type(lh)}')
            
            if not isinstance(rh, pl.Expr):
                raise hqle.CompilerException(f'Relational right hand {type(self.rh[0])} returned non-polars expression {type(rh)}')

            if self.op == '<':
                return (lh < rh)
            
            if self.op == '>':
                return (lh > rh)
            
            if self.op == '<=':
                return (lh <= rh)
            
            if self.op == '>=':
                return (lh >= rh)

            raise hqle.CompilerException(f'Unhandled op type {self.op}')

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
    def __init__(self, lh:Expression, start:Expression, end:Expression, op:str):
        Expression.__init__(self)

        self.lh = lh
        self.start = start
        self.end = end
        self.op = op
        self.negate = '!' in op
    
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

    def decompile(self, ctx: 'Context') -> str:
        lh = self.lh.decompile(ctx)
        start = self.start.decompile(ctx)
        end = self.end.decompile(ctx)
        op = '!between' if self.negate else 'between'

        return f'{lh} {op} ({start} .. {end})'
    
    def eval(self, ctx:'Context', **kwargs):
        as_pl = kwargs.get('as_pl', True)
        
        lh = self.lh.eval(ctx, as_pl=True)
        start = self.start.eval(ctx, as_pl=True)
        end = self.end.eval(ctx, as_pl=True)

        if not isinstance(lh, pl.Expr):
            raise hqle.CompilerException(f'Between left hand {self.lh.type} returned non-polars expression')

        if not isinstance(start, pl.Expr):
            raise hqle.CompilerException(f'Start field returned non-pl.Expr type {type(start)}')

        if not isinstance(end, pl.Expr):
            raise hqle.CompilerException(f'Start field returned non-pl.Expr type {type(end)}')
        
        filt = lh.is_between(start, end)
        
        if self.negate:
            filt = ~filt
        
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
    def __init__(self, lh:Expression, rh:list[Expression], bitype:str):
        Expression.__init__(self)
        self.bitype = bitype.lower()
        self.lh = lh
        self.rh = rh
        
    def to_dict(self):
        return {
            'type': self.type,
            'bitype': self.bitype,
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }

    def decompile(self, ctx: 'Context') -> str:
        exprs = [self.lh] + self.rh

        decomp = []
        for i in exprs:
            j = i.decompile(ctx)
            if isinstance(i, BinaryLogic):
                j = f'({j})'
            decomp.append(j)

        bitype = f' {self.bitype} '

        return bitype.join(decomp)
        
    def eval(self, ctx:'Context', **kwargs):
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
                filt = filt & i
            else:
                filt = filt | i
                
        return (filt)

class BasicRange(Expression):
    def __init__(self, start:Expression, end:Expression):
        Expression.__init__(self)
        self.start = start
        self.end = end
        self.logic = True

    def decompile(self, ctx: 'Context') -> str:
        start = self.start.decompile(ctx)
        end = self.end.decompile(ctx)

        return f'{start} .. {end}'
    
    def eval(self, ctx:'Context', **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
        lh = kwargs.get('lh', None)
        start = self.start.eval(ctx, as_pl=True)
        end = self.end.eval(ctx, as_pl=True)

        if isinstance(lh, type(None)):
            raise hqle.CompilerException('BasicRange given a NoneType left-hand expression!')

        return (lh > start).and_(lh < end)

class Regex(Expression):
    def __init__(self, lh:Expression, rh:Expression, i:bool=False, m:bool=False, s:bool=False, g:bool=False) -> None:
        Expression.__init__(self)
        self.lh = lh
        self.rh = rh

        self.i = i
        self.m = m
        self.s = s
        self.g = g

    def decompile(self, ctx: 'Context') -> str:
        lh = self.lh.decompile(ctx)
        rh = self.rh.decompile(ctx)

        return f'{lh} matches regex {rh}'

    def eval(self, ctx:'Context', **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
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

        if not (isinstance(rh, pl.Expr) or isinstance(rh, str)):
            raise hqle.CompilerException(f'Passed regex is not a string {rh}')

        return lh.str.contains(rh)
