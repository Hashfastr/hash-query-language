from .__proto__ import Expression
from Hql.Exceptions import HqlExceptions as hqle

from typing import TYPE_CHECKING, Optional, Union
import logging
import polars as pl

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Expressions import StringLiteral, Reference, Literal
    from Hql.Expressions import BinaryLogic

# descriptive class
class Logic(Expression):
    def __init__(self):
        Expression.__init__(self)

    def merge(self, expr:'Logic') -> Optional['Logic']:
        return NotImplemented

    def reduce(self):
        return self

class Comparator(Logic):
    def __init__(self, lh:'Reference', rh:Union[list[Expression], Expression], cs:bool=True, neq:bool=False, term:bool=False, logic_and:bool=False) -> None:
        Logic.__init__(self)

        self.lh:'Reference' = lh
        self.rh:list[Expression] = rh if isinstance(rh, list) else [rh]
        
        for i in self.rh:
            if not isinstance(i, Expression):
                hqle.CompilerException(f'Comparator {self.type} given non-Expression rh {type(i)}')

        # case sensitive compare
        self.cs:bool        = cs
        # is negated
        self.neq:bool       = neq
        # term matching
        self.term:bool      = term
        # How right hand logic should be handled
        # expr AND expr AND expr
        # vs
        # expr OR expr OR expr
        self.logic_and:bool = logic_and
        # if a comparator can be a righthand list
        self.can_list:bool  = True

    def set_rh(self, rh:Union[list[Expression], Expression]):
        self.rh = rh if isinstance(rh, list) else [rh]
    
    def add_rh(self, rh:Union[list[Expression], Expression]) -> Logic:
        return NotImplemented

    '''
    Simplifys some things, breaks out rhs to a set of singular comparators and a BinaryOperator
    Most languages don't support list right hands, so a lot of repeated code to do this:
    '''
    def expand_rh(self) -> Logic:
        exprs = []
        for i in self.rh:
            new = self.dupe()
            new.set_rh(i)
            exprs.append(new)
        return BinaryLogic(exprs, logic_and=self.logic_and)

    '''
    Create a copy duplicate of this object.
    Expressions can be reused many places, not costy to copy
    '''    
    def dupe(self):
        import copy
        return copy.deepcopy(self)

    def to_dict(self):
        return {
            'type': self.type,
            'cs': self.cs,
            'neq': self.neq,
            'term': self.term,
            'op': self.build_op(),
            'lh': self.lh.to_dict(),
            'rh': [x.to_dict() for x in self.rh]
        }
    
    def build_op(self) -> str:
        return NotImplemented

'''
Handles the following direct comparators:
- ==/!=
- =~/!~
- in/!in
- in~/!in~
Not substring comparators
'''
class Equality(Comparator):
    def __init__(self, lh:'Reference', rh:Union[list[Expression], Expression], cs:bool=True, neq:bool=False):
        Comparator.__init__(self, lh, rh, cs=cs, neq=neq)
        self.cs = cs
        self.neq = neq
        self.logic_and = False
        self.can_list = True

    # for pickle (aka deepcopy)
    def __reduce__(self):
        return (self.__class__, (self.lh, self.rh, self.cs, self.neq))

    def reduce(self) -> Logic:
        new = self.dupe()

        or_exprs = []
        rhs = []
        for i in new.rh:
            if isinstance(i, BasicRange):
                or_exprs.append(BetweenEquality(new.lh, i.start, i.end))
                continue
            rhs.append(i)

        # avoids recurse
        if or_exprs:
            new.rh = rhs
            or_exprs = [new] + or_exprs
            return BinaryLogic(or_exprs, logic_and=False)

        return self
    
    def merge(self, expr: 'Logic') -> Optional['Logic']:
        if not (isinstance(expr, type(self)) and self.lh == expr.lh):
            return expr

        attrs = ['cs', 'neq', 'logic_and']
        for i in attrs:
            if getattr(self, i) != getattr(expr, i):
                return expr

        self.rh += expr.rh
        return None

    '''
    Justifies the operator to correctly represent the flags given
    '''
    def build_op(self) -> str:
        op = ''
        if len(self.rh) > 1:
            if self.neq:
                op += '!'
            op += 'in'
            if not self.cs:
                op += '~'
        else:
            if self.neq:
                if self.cs:
                    op += '!~'
                else:
                    op += '!='
            else:
                if not self.cs:
                    op += '=~'
                else:
                    op += '=='
        return op

    def polars(self) -> pl.Expr:
        reduced = self.reduce()
        if not isinstance(reduced, Equality):
            return reduced.polars()

        if len(reduced.rh) > 1:
            return reduced.expand_rh().polars()

        lh = reduced.lh.polars()
        rh = reduced.rh[0].polars()

        if reduced.cs:
            new = (lh == rh)
        else:
            rh = pl.select(rh.str.escape_regex()).item()
            regex = f'(?i)^{rh}$'
            new = lh.str.contains(regex)

        if reduced.neq:
            new = ~new
        return new

    def deparse(self):
        reduced = self.reduce()
        if not isinstance(reduced, Equality):
            return reduced.deparse()

        lh = reduced.lh.deparse()

        op = f'{lh} {reduced.build_op()} '

        if len(reduced.rh) == 1:
            return op + reduced.rh[0].deparse()

        rh = []
        for i in reduced.rh:
            rh.append(i.deparse())
        rh = ', '.join(rh)

        return op + f'({rh})'

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
    def __init__(self, lh:'Reference', rh:list[StringLiteral], term:bool=False, logic_and:bool=False, neq:bool=False, cs:bool=False, startswith:bool=False, endswith:bool=False):
        Comparator.__init__(self, lh, rh)
        # narrow type defs
        self.lh:'Reference' = lh
        self.rh:list[StringLiteral] = rh

        self.term = term
        self.logic_and = logic_and
        self.neq = neq
        self.cs = cs
        self.startswith = startswith
        self.endswith = endswith
        self.can_list = True

    def to_dict(self):
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'op': self.build_op(),
            'rh': [x.to_dict() for x in self.rh]
        }

    def build_op(self) -> str:
        if self.startswith:
            core = 'startswith'
        elif self.endswith:
            core = 'endswith'
        elif self.term:
            core = 'has'
        else:
            core = 'contains'

        if self.neq:
            core = '!' + core
        
        if len(self.rh) > 1:
            core += '_all' if self.logic_and else '_any'
        
        if self.cs:
            core += '_cs'

        return core

    '''
    contains and has operators
    '''
    def has(self, lh:pl.Expr, rh:Expression):
        rh_str = pl.escape_regex(rh.str())

        regex = '' if self.cs else '(?i)'
        regex += rh_str

        return lh.str.contains(regex)

    '''
    prefix and suffix operators
    '''
    def prefix(self, lh:pl.Expr, rh:Expression):
        rh_str = pl.escape_regex(rh.str())
        
        regex = '' if self.cs else '(?i)'
        regex += '^' if self.startswith else ''
        regex += rh_str
        regex += '$' if self.endswith else ''

        return lh.str.contains(regex)

    def deparse(self) -> str:
        lh = self.lh.deparse()
        op = self.build_op()

        rh = []
        for i in self.rh:
            rh.append(i.deparse())
        rh = ', '.join(rh)

        out = f'{lh} {op} '
        if len(self.rh) > 1:
            out += f'({rh})'
        else:
            out += rh

        return out

    def polars(self) -> pl.Expr:
        if self.term:
            logging.warning('Term matching not supported in Hql-land, do not expect increased performance')

        if len(self.rh) > 1:
            return self.expand_rh().polars()
        
        lh = self.lh.polars()
        if self.startswith or self.endswith:
            expr = self.prefix(lh, self.rh[0])
        else:
            expr = self.has(lh, self.rh[0])

        return ~expr if self.neq else expr

    def merge(self, expr: 'Logic') -> Optional['Logic']:
        if not isinstance(expr, type(self)) or self.lh != expr.lh:
            return expr

        attrs = ['term', 'logic_and', 'neq', 'cs', 'startswith', 'endswith']
        for i in attrs:
            if getattr(self, i) != getattr(expr, i):
                return expr

        self.add_rh(expr)
        return None

# Handles relational expressions
# - <
# - >
# - <=
# - >=
# As per the grammar
# Takes after the equality expression
class Relational(Comparator):
    def __init__(self, lh:'Reference', rh:Expression, gt:bool, eq:bool) -> None:
        Comparator.__init__(self, lh, rh, logic_and=True)
        self.gt = gt
        self.eq = eq
        self.can_list = False

    def __reduce__(self):
        return (self.__class__, (self.lh, self.rh, self.gt, self.eq))

    def deparse(self) -> str:
        lh = self.lh.deparse()
        rh = self.rh[0].deparse()
        return f'{lh} {self.build_op()} {rh}'
    
    def build_op(self) -> str:
        op =  '>' if self.gt else '<'
        op += '=' if self.eq else ''
        return op

    def polars(self) -> pl.Expr:
        lh = self.lh.polars()
        rh = self.rh[0].polars()

        if self.gt:
            if self.eq:
                return (lh >= rh)
            else:
                return (lh > rh)
        else:
            if self.eq:
                return (lh <= rh)
            else:
                return (lh < rh)

# Data range functionality
# Left hand side is the expression to evaluate in being between two values.
# The right hand has a start and end expression showing the range of the values.
#
# | where ['@timestamp'] between ("2022-10-21T15:50:00.000Z" .. "2022-10-21T15:55:00.000Z")
# 
# Here lh is the '@timestamp' escaped string literal, and the right hand has
# the start and end values for the time range.
class BetweenEquality(Comparator):
    def __init__(self, lh:'Reference', start:'Literal', end:'Literal', neq:bool=False):
        Logic.__init__(self)

        self.lh = lh
        self.start = start
        self.end = end
        self.neq = neq
    
    def to_dict(self) -> dict:
        return {
            'type': self.type,
            'negate': self.neq,
            'lh': self.lh.to_dict(),
            'rh': {
                'start': self.start.to_dict(),
                'end': self.end.to_dict()
            }
        }

    def deparse(self) -> str:
        lh = self.lh.deparse()
        start = self.start.deparse()
        end = self.end.deparse()
        op = '!between' if self.neq else 'between'
        return f'{lh} {op} ({start} .. {end})'

    def polars(self) -> pl.Expr:
        lh = self.lh.polars()
        start = self.start.polars()
        end = self.end.polars()
        
        filt = lh.is_between(start, end)
        if self.neq:
            filt = ~filt
        return filt

'''
Handles binary logic, simple ands and ors
'''
class BinaryLogic(Logic):
    def __init__(self, exprs:list[Logic], logic_and:bool=True):
        Logic.__init__(self)
        self.logic_and = logic_and
        
        if len(exprs) == 0:
            raise hqle.CompilerException(f'BinaryLogic given a empty list of expressions')

        for i in exprs:
            if not isinstance(i, Logic):
                raise hqle.CompilerException(f'BinaryLogic passed invalid non-logic expression: {type(i)}')
        
        self.exprs:list[Logic] = exprs
        self.exprs = self.condense()

    # immediately break down if there's only 1 expr
    def __new__(cls, exprs:list, logic_and:bool=True) -> Logic:
        if len(exprs) == 1:
            return exprs[0]
        return super().__new__(cls)

    def __reduce__(self):
        return (self.__class__, (self.exprs, self.logic_and))
    
    def __iter__(self):
        return iter(self.exprs)

    '''
    Condense down equality operators so they're more syntactically condensed.
    Flatten nested logic
    '''
    def condense(self) -> Logic:
        new:list[Logic] = []
        for i in self.exprs:
            if isinstance(i, BinaryLogic):
                i = i.condense()
            
            # second pass, integrate
            if isinstance(i, BinaryLogic) and i.logic_and == self.logic_and:
                new += i.exprs
                continue

            if isinstance(i, Logic):
                new.append(i)
                continue

            for j in new:
                if j.can_merge(i):
                    j.merge(i)

            new.append(i)

        return total
        
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

class BasicRange(Logic):
    def __init__(self, start:Literal, end:Literal):
        Logic.__init__(self)
        self.start = start
        self.end = end

    def decompile(self, ctx: 'Context') -> str:
        start = self.start.decompile(ctx)
        end = self.end.decompile(ctx)

        return f'({start} .. {end})'
    
    def eval(self, ctx:'Context', **kwargs) -> Union[pl.Expr, "Expression", list[str], str]:
        lh = kwargs.get('lh', None)
        start = self.start.eval(ctx, as_pl=True)
        end = self.end.eval(ctx, as_pl=True)
        
        if isinstance(lh, type(None)):
            raise hqle.CompilerException('BasicRange given a NoneType left-hand expression!')
        
        if isinstance(lh, Expression):
            lh = self.eval(ctx, as_pl=True)

        assert isinstance(lh, pl.Expr)
        assert isinstance(start, pl.Expr)
        assert isinstance(end, pl.Expr)

        lh = pl.col('source').struct['ip']
        return lh.is_between(start, end)

class Regex(Logic):
    def __init__(self, lh:Union['NamedReference', 'Path', 'StringLiteral'], rh:'StringLiteral', i:bool=False, m:bool=False, s:bool=False, g:bool=False) -> None:
        Logic.__init__(self)
        self.lh = lh
        self.rh = rh

        self.i = i # case insentive
        self.m = m # multiline
        self.s = s # dotall
        self.g = g # global

    def to_dict(self) -> Union[None, dict]:
        return {
            'type': self.type,
            'lh': self.lh.to_dict(),
            'rh': self.rh.to_dict(),
            'i': self.i,
            'm': self.m,
            's': self.s,
            'g': self.g,
        }

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
            raise hqle.CompilerException(f'String inary left hand {self.lh.type} returned a non-polars expression ')

        if not (isinstance(rh, pl.Expr) or isinstance(rh, str)):
            raise hqle.CompilerException(f'Passed regex is not a string {rh}')

        return lh.str.contains(rh)

class Not(Logic):
    def __init__(self, expr:Expression) -> None:
        Logic.__init__(self)
        self.expr = expr

    def decompile(self, ctx: 'Context') -> str:
        expr = self.expr.decompile(ctx)
        return f'not({expr})'

    def eval(self, ctx: 'Context', **kwargs) -> Union[pl.Expr, 'Expression']:
        expr = self.expr.eval(ctx, as_pl=True)
        assert isinstance(expr, pl.Expr)
        return expr.not_()
