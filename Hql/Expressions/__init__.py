from typing import TYPE_CHECKING, Union

from .__proto__ import Expression

from .Logic import Logic, Comparator, Equality, Substring
from .Logic import Relational, BetweenEquality, BinaryLogic
from .Logic import BasicRange, Regex, Not

from .References import Reference, NamedReference, Wildcard
from .References import EscapedNamedReference, Path, NamedExpression

from .Literals import Literal, TypeExpression, StringLiteral
from .Literals import MultiString, Integer, IP4, Float, Bool
from .Literals import Multivalue, Datetime, Null

from .Functions import FuncProto, FuncExpr, DotFuncExpr

from .Aggregation import OrderedExpression, ByExpression

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Database import Database
    from Hql.Types.Hql import HqlTypes as hqlt
    from Hql.Context import Context

class PipeExpression(Expression):
    def __init__(self, pipes:list['Operator'], prepipe:Union['Database', 'Expression', None]=None):
        Expression.__init__(self)
        self.prepipe                = prepipe
        self.pipes:list['Operator'] = pipes

    def __bool__(self):
        return bool(self.prepipe) or bool(self.pipes)
        
    def to_dict(self):
        d:dict = {
            'type': self.type,
        }
        
        if self.prepipe:
            d['prepipe'] = self.prepipe.to_dict()

        d['pipes'] = [x.to_dict() for x in self.pipes]

        return d

    def deparse(self) -> str:
        prepipe = self.prepipe.deparse() if self.prepipe else ''
        pipes = [x.deparse() for x in self.pipes]

        out = prepipe
        for i in pipes:
            if out:
                out += '\n'
            out += f'| {i}'

        return out

class OpParameter(Expression):
    def __init__(self, name:Reference, value:Expression):
        Expression.__init__(self)
        self.name = name
        self.value = value

    def deparse(self) -> str:
        name = self.name.deparse()
        value = self.value.deparse()
        return f'{name}={value}'
        
    def to_dict(self):        
        return {
            'name': self.name.to_dict(),
            'value': self.value.to_dict()
        }

class ToClause(Expression):
    def __init__(self, expr:Reference, to:Union[TypeExpression, 'hqlt.HqlType']):
        Expression.__init__(self)
        self.expr = expr
        if isinstance(to, TypeExpression):
            to = to.dtype()
        self.to = to
        
    def to_dict(self):
        return {
            'type': self.type,
            'expr': self.expr.to_dict(),
            'to': self.to.to_dict()
        }

    def deparse(self) -> str:
        expr = self.expr.deparse()
        expr += ' to ' + self.to.deparse()
        return expr
        
    def eval(self, ctx:'Context') -> 'Context':
        from Hql.Data import Data
        ctx = ctx.copy()

        new = []
        for table in ctx.data:
            table = table.cast_in_place(self.expr, self.to)
            new.append(table)
        
        ctx.data = Data(tables=new)
        return ctx
