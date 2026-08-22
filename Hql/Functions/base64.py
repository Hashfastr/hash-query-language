from __future__ import annotations

from typing import Optional, TYPE_CHECKING, Union

from Hql.Context import register_func
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Functions import Function

if TYPE_CHECKING:
    from Hql.Expressions.Literals import StringLiteral
    from Hql.Expressions import Expression
    from Hql.Context import Context
    from Hql.Expressions.Literals import Multivalue

@register_func('base64')
@register_func('b64')
class base64enc(Function):
    def __init__(self, args: list, conf:Optional[dict]=None):
        from Hql.Expressions.Literals import StringLiteral
        from Hql.Expressions.References import Reference
        Function.__init__(self, args, 1, 2, conf=conf)

        for i in args:
            if not isinstance(i, (StringLiteral, Reference)):
                raise hqle.ArgumentException(f'Invalid argument type {type(i)} passed to {self.name}')
            
        self.val:Union[StringLiteral, Reference] = args[0]
        self.enc = args[1] if len(args) == 2 else StringLiteral('ascii')

    def preprocess(self, ctx: Context, receiver=None) -> object:
        from Hql.Expressions.Literals import StringLiteral

        def static(val:str, enc:str) -> StringLiteral:
            from base64 import b64encode
            val = b64encode(bytes(val, enc)).decode()
            return StringLiteral(val)

        val = self.val.preprocess(ctx)
        enc = self.enc.preprocess(ctx)

        if not isinstance(enc, StringLiteral):
            raise hqle.ArgumentException(f'base64 function encoding value did not resolve to a StringLiteral: {enc}')

        if not isinstance(val, StringLiteral):
            return self

        return static(val.str(), enc.str())

    def eval(self, ctx: Context, receiver=None) -> object:
        from Hql.Data import Series
        raise hqle.CompilerException('unimplemented dynamic eval')

        # return Series()

@register_func('base64dec')
@register_func('b64dec')
class base64dec(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions.Literals import StringLiteral
        from Hql.Expressions.References import Reference
        Function.__init__(self, args, 1, 2)

        for i in args:
            if not isinstance(i, (StringLiteral, Reference)):
                raise hqle.ArgumentException(f'Invalid argument type {type(i)} passed to {self.name}')
            
        self.val:Union[StringLiteral, Reference] = args[0]
        self.enc = args[1] if len(args) == 2 else StringLiteral('ascii')

    def static_eval(self, ctx:Context) -> StringLiteral:
        from base64 import b64decode

        val = self.val.str()
        enc = self.enc.str()

        val = b64decode(bytes(val, 'ascii')).decode(enc)
        return StringLiteral(val)
       
    def eval(self, ctx: Context, receiver=None) -> object:
        from Hql.Data import Series
        raise hqle.CompilerException('unimplemented dynamic eval')

        # return Series()

@register_func('base64off')
@register_func('b64off')
class base64off(Function):
    def __init__(self, args: list):
        from Hql.Expressions.Literals import StringLiteral
        from Hql.Expressions.References import Reference
        Function.__init__(self, args, 1, 2)

        for i in args:
            if not isinstance(i, (StringLiteral, Reference)):
                raise hqle.ArgumentException(f'Invalid argument type {type(i)} passed to {self.name}')
            
        self.val:Union[StringLiteral, Reference] = args[0]
        self.enc = args[1] if len(args) == 2 else StringLiteral('ascii')

    def calc_offset(self, val:str, encoding:str) -> list[StringLiteral]:
        from base64 import b64encode
        from Hql.Expressions.Literals import StringLiteral
        
        start_offsets = (0, 2, 3)
        end_offsets = (None, -3, -2)

        parts = []
        for i in range(3):
            part = b64encode(i * b" " + bytes(val, 'utf-8'))[
                start_offsets[i] : end_offsets[(len(val) + i) % 3]
            ].decode()
            parts.append(StringLiteral(part))

        return parts

    def preprocess(self, ctx: Context, receiver=None) -> Multivalue:
        val = self.val.str()
        enc = self.enc.str()

        offsets = self.calc_offset(val, enc)
        mv = Multivalue(offsets)
        return mv
       
    def eval(self, ctx: Context, receiver=None) -> object:
        from Hql.Data import Series
        raise hqle.CompilerException('unimplemented dynamic eval')

        # return Series()
