from Hql.Functions import Function
from Hql.Context import register_func, Context
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions import StringLiteral, Multivalue
from Hql.Data import Series
import polars as pl

from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Expressions import Expression

@register_func('base64')
@register_func('b64')
class base64enc(Function):
    def __init__(self, args: list):
        from Hql.Expressions import StringLiteral, NamedReference, Path
        Function.__init__(self, args, 1, 2)

        if isinstance(args[0], StringLiteral):
            self.static = True
        elif isinstance(args[0], (NamedReference, Path)):
            self.static = False
        else:
            raise hqle.ArgumentException(f'Invalid argument type {type(args[0])} passed to {self.name}')
            
        self.val = args[0]

        if len(args) > 1:
            if not isinstance(args[1], StringLiteral):
                raise hqle.ArgumentException(f'Invalid encoding argument type {type(args[0])} passed to {self.name}')
            self.encoding = args[1]
        else:
            self.encoding = StringLiteral('ascii')

    def static_eval(self, ctx:Context) -> StringLiteral:
        from base64 import b64encode

        val = self.val.eval(ctx, as_str=True)
        if not isinstance(val, str):
            raise hqle.CompilerException(f'Static evaluation of argument {type(self.val)} to {self.name} returned {type(val)} not str')

        encoding = self.encoding.eval(ctx)
        if not isinstance(encoding, str):
            raise hqle.CompilerException(f'Static evaluation of encoding argument {type(self.encoding)} to {self.name} returned {type(encoding)} not str')

        val = b64encode(bytes(val, encoding)).decode()
        return StringLiteral(val)
       
    def eval(self, ctx: 'Context', **kwargs) -> Union['Data', 'Expression']:
        if self.static:
            return self.static_eval(ctx)

        return StringLiteral('')

@register_func('base64dec')
@register_func('b64dec')
class base64dec(Function):
    def __init__(self, args: list):
        from Hql.Expressions import StringLiteral, NamedReference, Path
        Function.__init__(self, args, 1, 2)

        if isinstance(args[0], StringLiteral):
            self.static = True
        elif isinstance(args[0], (NamedReference, Path)):
            self.static = False
        else:
            raise hqle.ArgumentException(f'Invalid argument type {type(args[0])} passed to {self.name}')
            
        self.val = args[0]

        if len(args) > 1:
            if not isinstance(args[1], StringLiteral):
                raise hqle.ArgumentException(f'Invalid encoding argument type {type(args[0])} passed to {self.name}')
            self.encoding = args[1]
        else:
            self.encoding = StringLiteral('ascii')

    def static_eval(self, ctx:Context) -> StringLiteral:
        from base64 import b64decode

        val = self.val.eval(ctx, as_str=True)
        if not isinstance(val, str):
            raise hqle.CompilerException(f'Static evaluation of argument {type(self.val)} to {self.name} returned {type(val)} not str')

        encoding = self.encoding.eval(ctx)
        if not isinstance(encoding, str):
            raise hqle.CompilerException(f'Static evaluation of encoding argument {type(self.encoding)} to {self.name} returned {type(encoding)} not str')

        val = b64decode(bytes(val, 'ascii')).decode(encoding)
        return StringLiteral(val)
       
    def eval(self, ctx: 'Context', **kwargs) -> Union['Data', 'Expression']:
        if self.static:
            return self.static_eval(ctx)

        return StringLiteral('')

@register_func('base64off')
@register_func('b64off')
class base64off(Function):
    def __init__(self, args: list):
        from Hql.Expressions import StringLiteral, NamedReference, Path
        Function.__init__(self, args, 1, 2)

        if isinstance(args[0], StringLiteral):
            self.static = True
        elif isinstance(args[0], (NamedReference, Path)):
            self.static = False
        else:
            raise hqle.ArgumentException(f'Invalid argument type {type(args[0])} passed to {self.name}')
            
        self.val = args[0]

        if len(args) > 1:
            if not isinstance(args[1], StringLiteral):
                raise hqle.ArgumentException(f'Invalid encoding argument type {type(args[0])} passed to {self.name}')
            self.encoding = args[1]
        else:
            self.encoding = StringLiteral('ascii')

    def calc_offset(self, val:str, encoding:str) -> list[StringLiteral]:
        from base64 import b64encode
        from Hql.Expressions import StringLiteral
        
        start_offsets = (0, 2, 3)
        end_offsets = (None, -3, -2)

        parts = []
        for i in range(3):
            part = b64encode(i * b" " + bytes(val, 'utf-8'))[
                start_offsets[i] : end_offsets[(len(val) + i) % 3]
            ].decode()
            parts.append(StringLiteral(part))

        return parts

    def static_eval(self, ctx:Context) -> Multivalue:
        from Hql.Types.Hql import HqlTypes as hqlt

        val = self.val.eval(ctx, as_str=True)
        if not isinstance(val, str):
            raise hqle.CompilerException(f'Static evaluation of argument {type(self.val)} to {self.name} returned {type(val)} not str')

        encoding = self.encoding.eval(ctx)
        if not isinstance(encoding, str):
            raise hqle.CompilerException(f'Static evaluation of encoding argument {type(self.encoding)} to {self.name} returned {type(encoding)} not str')

        offsets = self.calc_offset(val, encoding)
        mv = Multivalue(offsets)
        return mv
       
    def eval(self, ctx: 'Context', **kwargs) -> Union['Data', Series, 'Expression']:
        if self.static:
            return self.static_eval(ctx)

        return StringLiteral('')
