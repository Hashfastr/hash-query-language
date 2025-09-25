from typing import TYPE_CHECKING, Optional, Union

from Hql.Compiler.InstructionSet import InstructionSet

from .__proto__ import Expression
from .Logic import *
from .References import *
from .Literals import *
from .Functions import *
from .Aggregation import *

if TYPE_CHECKING:
    from Hql.Operators import Operator, Database
    from Hql.Compiler import InstructionSet

from Hql.Exceptions import HqlExceptions as hqle

class PipeExpression(Expression):
    def __init__(self, pipes:list['Operator'], prepipe:Union['Expression', None]=None):
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

    def decompile(self, ctx: 'Context') -> str:
        prepipe = self.prepipe.decompile(ctx) if self.prepipe else ''

        pipes = []
        for i in self.pipes:
            pipe = i.decompile(ctx)
            
            if isinstance(pipe, str):
                pipes.append(pipe)
            else:
                pipes += pipe

        out = f'{prepipe}'
        for i in pipes:
            if out:
                out += '\n'
            out += f'| {i}'

        return out

class OpParameter(Expression):
    def __init__(self, name:str, value:Expression):
        Expression.__init__(self)
        self.name = name
        self.value = value

    def decompile(self, ctx: 'Context') -> str:
        value = self.value.decompile(ctx)
        return f'{self.name}={value}'
        
    def to_dict(self):        
        return {
            'name': self.name,
            'value': self.value.to_dict()
        }

class ToClause(Expression):
    def __init__(self, expr:Expression, to:Union[None, Expression, hqlt.HqlType]=None):
        Expression.__init__(self)
        self.expr = expr
        self.to = to
        
    def to_dict(self):
        d = {
            'type': self.type,
            'expr': self.expr.to_dict(),
        }

        if isinstance(self.to, hqlt.HqlType):
            d['to'] = self.to.name

        elif self.to:
            d['to'] = self.to.to_dict()

        return d

    def decompile(self, ctx: 'Context') -> str:
        expr = self.expr.decompile(ctx)

        if isinstance(self.to, hqlt.HqlType):
            to = self.to.name
            expr += f' to {to}'

        elif self.to:
            to = self.to.decompile(ctx)
            expr += f' to {to}'

        return expr
        
    def eval(self, ctx:'Context', **kwargs):
        as_list = kwargs.get('as_list', False)
        as_str = kwargs.get('as_str', False)

        if as_list or as_str:
            return self.expr.eval(ctx, as_list=as_list, as_str=as_str)
        
        path = self.expr.eval(ctx, as_path=True)
        
        new = []
        for table in ctx.data:
            table = table.cast_in_place(path, self.to)
            new.append(table)
        
        return Data(tables=new)
