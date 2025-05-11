import HqlCompiler.Config as Config
import logging
from HqlCompiler.Context import register_func, get_database, Context
from HqlCompiler.Exceptions import *
from .__proto__ import Function

# This is a meta function resolved while parsing
@register_func('database')
class database(Function):
    def __init__(self, args:list):
        super().__init__(args, 0, 1)
        
        # later feature to use, maybe
        self.disallowed = (
            'HOSTS',
            'HOST',
            'USER',
            'PASS',
            'VALIDATE_CERTS',
            'TYPE'
        )

        if self.args != [] and self.args[0].type != 'StringLiteral':
            raise ArgumentException(f'Bad database argument datatype {args[0].type}')
        
    def eval(self, ctx:Context, **kwargs):
        if self.args == [] or self.args[0].eval(ctx, as_str=True) == '':
            dbconf = Config.HqlConfig.get_default_db()
        else:
            dbconf = Config.HqlConfig.get_database(self.args[0].eval(ctx, as_str=True))
        
        # This will probably have some unintended consequences
        # Enable when ready
        # Enables dynamic conf changes to a dbconfig
        # for i in self.args[1:]:
        #     arg = i.get_value().split('=')
            
        #     if arg[0] in disallowed:
        #         raise CompilerException(f'Invalid variable set in database call {arg[0]}')
            
        #     dbconf[arg[0]] = arg[1]
                
        return ctx.get_db(dbconf['TYPE'])(dbconf)