from typing import TYPE_CHECKING, Union
import logging

from .__proto__ import Expression
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Context import Context

class FuncExpr(Expression):
    def __init__(self, name:Union[Expression, str], args:Union[None, list[Expression]]=None):
        from Hql.Expressions import NamedReference
        Expression.__init__(self)
        
        if isinstance(name, str):
            self.name = NamedReference(name)
        else:
            self.name = name

        self.args:list[Expression] = args if args else []

    def __bool__(self):
        return self.name.__bool__()
    
    def to_dict(self):
        return {
            'type': self.type,
            'name': self.name.to_dict(),
            'args': [x.to_dict() for x in self.args]
        }

    def decompile(self, ctx: 'Context') -> str:
        name = self.name.decompile(ctx)

        args = []
        for i in self.args:
            args.append(i.decompile(ctx))

        out = f'{name}('
        out += ', '.join(args)
        out += ')'

        return out
    
    # Evals to function objects
    def eval(self, ctx:'Context', **kwargs):
        # Do we need this? Provides no functional use
        '''
        if kwargs.get('as_list', False):
            return self.name.eval(ctx, as_list=True)
        
        if kwargs.get('as_str', False):
            return self.name.eval(ctx, as_str=True)
        '''
        
        name = self.name.eval(ctx, as_str=True)
        if not isinstance(name, str):
            raise hqle.CompilerException(f'Function name expression returned non-string {name}')
        
        func = ctx.get_func(name)
        logging.debug(f'Resolved func {func}')

        return func(self.args)
        
class DotCompositeFunction(Expression):
    def __init__(self, funcs:list[FuncExpr]):
        Expression.__init__(self)
        self.funcs = funcs

    def __bool__(self):
        return bool(self.funcs)
    
    def to_dict(self):
        return {
            'type': self.type,
            'funcs': [x.to_dict() for x in self.funcs]
        }
        
    def gen_list(self, ctx:'Context'):
        func_list = []
        for i in self.funcs:
            func_list.append(i.eval(ctx, as_str=True))
            
        return func_list

    def decompile(self, ctx: 'Context') -> str:
        funcs = []
        for i in self.funcs:
            funcs.append(i.decompile(ctx))

        return '.'.join(funcs)

    # Evals to the function objects that can be executed
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Functions import Function

        receiver = kwargs.get('receiver', None)
        no_exec = kwargs.get('no_exec', False)
        preprocess = kwargs.get('preprocess', False)
        
        # Do we even need this? Doesn't make any sense.
        '''
        if kwargs.get('as_list', False):
            return self.gen_list(ctx)
        
        if kwargs.get('as_str', False):
            return '.'.join(self.gen_list(ctx))
        '''
        
        funcs:list[Function] = []
        for func in self.funcs:
            if isinstance(func, FuncExpr):
                func = func.eval(ctx)
            funcs.append(func)

        func_list = []
        for func in funcs:
            if preprocess and not func.preprocess:
                raise hqle.QueryException(f'Attempting to use function {func.name} in a preprocess context')
            func_list.append(func)
            
            if not no_exec:
                if not isinstance(func, Function):
                    raise hqle.CompilerException(f'Function resolution returned non-function object {func}')

                receiver = func.eval(ctx, receiver=receiver)

        if no_exec:
            return func_list

        elif receiver == None:
            logging.critical(self.to_dict())
            raise hqle.CompilerException('DotCompositeFunction resulted in None! (see above)')

        else:
            return receiver
