from typing import TYPE_CHECKING, Union

from .__proto__ import Expression
from .Logic import *
from .References import *
from .Literals import *
from .Functions import *
from .Aggregation import *

if TYPE_CHECKING:
    from Hql.Operators import Operator

from Hql.Exceptions import HqlExceptions as hqle

class PipeExpression(Expression):
    def __init__(self, prepipe:Union['Operator', Expression], pipes:list['Operator']):
        Expression.__init__(self)
        self.prepipe                 = prepipe
        self.pipes:list['Operator']  = pipes

    def __bool__(self):
        return bool(self.prepipe)
        
    def to_dict(self):
        return {
            'type': self.type,
            'prepipe': self.prepipe.to_dict(),
            'pipes': [x.to_dict() for x in self.pipes]
        }

    def decompile(self, ctx:'Context') -> str:
        prepipe = self.prepipe.decompile(ctx)

        pipes = []
        for i in self.pipes:
            pipes.append(i.decompile(ctx))

        out = f'{prepipe}'
        for i in pipes:
            out += f'\n{i}'

        return out
    
    # Takes pipes and puts them into a compiler set
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Operators import Operator
        from Hql.Operators.Database import Database
        from Hql.Compiler import CompilerSet

        no_exec = kwargs.get('no_exec', False)

        # Resolve database references
        prepipe = self.prepipe.eval(ctx, tabular=True)

        if isinstance(prepipe, type(None)):
            raise hqle.CompilerException(f'Prepipe evaluation returned None')
        
        if not isinstance(prepipe, (Operator, CompilerSet)):
            raise hqle.CompilerException(f'Prepipe returned non-operator/cs, got {prepipe}')
        
        # can add more tabular prepipe types here
        if not isinstance(prepipe, (Database, Operator, CompilerSet)) and self.pipes != []:
            raise hqle.CompilerException(f'Attempting to use a non-tabular expression with pipe expression {self.pipes[0].type}')

        ops = [prepipe] + self.pipes
        cs = CompilerSet(ops).compile()

        if no_exec:
            return cs

        return cs.eval(ctx)

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
    def __init__(self, expr:Expression, to:Union[None, hqlt.HqlType]=None):
        Expression.__init__(self)
        self.expr = expr
        self.to = to
        
    def to_dict(self):
        d = {
            'type': self.type,
            'expr': self.expr.to_dict(),
        }

        if self.to:
            d['to'] = self.to.name

        return d

    def decompile(self, ctx: 'Context') -> str:
        expr = self.expr.decompile(ctx)

        if self.to:
            to = self.to.name
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
