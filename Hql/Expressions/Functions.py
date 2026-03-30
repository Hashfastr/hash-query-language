from .__proto__ import Expression

from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Functions import Function, DotCompositeFunction
    from Hql.Expressions import NamedReference

class FuncProto(Expression):
    ...

class FuncExpr(FuncProto):
    # I know I'm gettinG rid of allowing protos for this stuff but 
    def __init__(self, name:'NamedReference', args:Optional[list[Expression]]=None):
        FuncProto.__init__(self)
        self.name = name
        self.args:list[Expression] = args if args else []

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
    def preprocess(self, ctx:'Context') -> 'Function':
        name = self.name.str()
        func = ctx.get_func(name)
        return func(self.args, conf=ctx.config.get_function(name))

class DotFuncExpr(FuncProto):
    def __init__(self, funcs:list[FuncExpr]):
        FuncProto.__init__(self)
        self.funcs = funcs

    def __new__(cls, funcs:list[FuncExpr]):
        if len(funcs) == 1:
            return funcs[0]
        return super().__new__(cls)

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
    
    def preprocess(self, ctx:'Context') -> Union['DotCompositeFunction', 'Function']:
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
