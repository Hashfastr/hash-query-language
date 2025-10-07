from Hql.Functions import Function
from Hql.Context import register_func, Context
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions import StringLiteral, Multivalue
from Hql.Data import Series
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Expressions import Expression

@register_func('wide')
class wide(Function):
    def __init__(self, args: list):
        from Hql.Expressions import StringLiteral, NamedReference, Path
        Function.__init__(self, args, 1, 1)

        if isinstance(args[0], StringLiteral):
            self.static = True
        elif isinstance(args[0], (NamedReference, Path)):
            self.static = False
        else:
            raise hqle.ArgumentException(f'Invalid argument type {type(args[0])} passed to {self.name}')
            
        self.val = args[0]

    def static_eval(self, ctx:Context) -> StringLiteral:
        val = self.val.eval(ctx, as_str=True)
        if not isinstance(val, str):
            raise hqle.CompilerException(f'Static evaluation of argument {type(self.val)} to {self.name} returned {type(val)} not str')

        val = val.encode('utf-16le').decode('utf-8')
        return StringLiteral(val)
       
    def eval(self, ctx: 'Context', **kwargs) -> Union['Data', 'Expression']:
        if self.static:
            return self.static_eval(ctx)
        return StringLiteral('')
