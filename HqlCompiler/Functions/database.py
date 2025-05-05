from HqlCompiler.Config import Config
import logging
from HqlCompiler.Registry import register_func, get_database
from HqlCompiler.Exceptions import *
from .__proto__ import Function

# This is a meta function resolved while parsing
@register_func('database')
class database(Function):
    def __init__(self, args:list):
        super().__init__(args)
        self.expected = 1
        self.config = None
                
        if len(self.args) != self.expected:
            logging.error(f'{self.name} call has an invalid number of arguments')
            logging.error(f'Got {len(args)}, expected {self.expected}')
            raise ArgumentException(f'Function argument exception')

        if self.args[0].type != 'StringLiteral':
            raise ArgumentException(f'Bad database argument datatype {args[0].type}')
        
    def eval(self):
        if not self.config:
            raise CompilerException('Database function not given config')
        
        dbconf = self.config.get_database(self.args[0].value)
                
        return get_database(dbconf['TYPE'])(dbconf)