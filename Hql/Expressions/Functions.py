from __future__ import annotations

from .__proto__ import Expression

from typing import TYPE_CHECKING, Optional, Sequence, Union

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Functions import Function, DotCompositeFunction
    from Hql.Expressions.References import NamedReference, Reference

class FuncProto(Expression):
    ...

class FuncExpr(FuncProto):
    # I know I'm getting rid of allowing protos for this stuff but 
    def __init__(self, name:NamedReference, args:Optional[Sequence[Expression]]=None):
        FuncProto.__init__(self)
        self.name = name
        self.args:Sequence[Expression] = args if args else []

    def __bool__(self):
        return bool(self.name)
    
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'args': [x.to_dict() for x in self.args]
        }

    def deparse(self) -> str:
        name = self.name.deparse()

        args = []
        for i in self.args:
            args.append(i.deparse())

        out = f'{name}('
        out += ', '.join(args)
        out += ')'

        return out

    # Evals to function objects
    def preprocess(self, ctx:Context) -> Function:
        name = self.name.str()
        func = ctx.get_func(name)
        return func(self.args, conf=ctx.config.get_function(name))

class ReceiverFuncExpr(FuncProto):
    def __init__(self, receiver:Reference, call:FuncExpr):
        FuncProto.__init__(self)
        self.receiver = receiver
        self.call = call

    def __bool__(self):
        return bool(self.receiver) and bool(self.call)

    def to_dict(self):
        return {
            'type': self.type,
            'receiver': self.receiver.to_dict(),
            'call': self.call.to_dict()
        }

    def deparse(self) -> str:
        return f'{self.receiver.deparse()}.{self.call.deparse()}'

    def preprocess(self, ctx:Context) -> object:
        func = self.call.preprocess(ctx)
        receiver = self.receiver.preprocess(ctx)
        receiver = receiver.preprocess(ctx) if hasattr(receiver, 'preprocess') and receiver is not self.receiver else receiver
        return func.eval(ctx, receiver=receiver)

class DotFuncExpr(FuncProto):
    def __init__(self, funcs:list[FuncExpr]):
        FuncProto.__init__(self)
        self.funcs = funcs

    def __new__(cls, funcs:list[FuncExpr]):
        if len(funcs) == 1:
            return funcs[0]
        return super().__new__(cls)

    def __reduce__(self):
        return (self.__class__, (self.funcs,))

    def __bool__(self):
        return bool(self.funcs)

    def to_dict(self):
        return {
            'type': self.type,
            'funcs': [x.to_dict() for x in self.funcs]
        }

    def deparse(self) -> str:
        funcs = []
        for i in self.funcs:
            funcs.append(i.deparse())
        return '.'.join(funcs)
    
    def preprocess(self, ctx:Context) -> Union[DotCompositeFunction, Function]:
        from Hql.Functions import DotCompositeFunction

        funcs = []
        for i in self.funcs:
            try:
                funcs.append(i.preprocess(ctx))
            except Exception as e:
                # catching for handling for if a function can't preprocess within the chain
                e.add_note(f'Occured in {self.deparse()}')
                raise

        return DotCompositeFunction(funcs)
