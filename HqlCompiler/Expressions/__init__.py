from .__proto__ import Expression
from .Logic import *
from .References import *
from .Literals import *
from .Functions import *
from .Aggregation import *

from HqlCompiler.Operators import Operator
from HqlCompiler.Operators.Database import Database

class PipeExpression(Expression):
    def __init__(self, prepipe:Expression, pipes:list[Operator]):
        Expression.__init__(self)
        self.prepipe:Expression      = prepipe
        self.pipes:list[Operator]    = pipes
        
    def to_dict(self):
        return {
            'type': self.type,
            'prepipe': self.prepipe.to_dict(),
            'pipes': [x.to_dict() for x in self.pipes]
        }
    
    # Takes pipes and puts them into a compiler set
    def eval(self, ctx:Context, **kwargs):
        no_exec = kwargs.get('no_exec', False)

        from HqlCompiler import CompilerSet

        # Resolve database references
        prepipe = self.prepipe.eval(ctx, tabular=True)

        if prepipe == None:
            raise CompilerException(f'Prepipe evaluation returned None')
        
        # can add more tabular prepipe types here
        if not issubclass(type(prepipe), (Database)) and self.pipes != []:
            raise CompilerException(f'Attempting to use a non-tabular expression with pipe expression {self.pipes[0].type}')

        ops = [prepipe] + self.pipes
        cs = CompilerSet(ops).compile()

        if no_exec:
            return cs

        return cs.eval(ctx)

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
        for table in ctx.data:
            table = table.cast_in_place(path, self.to)
            new.append(table)
        
        return Data(tables=new)
