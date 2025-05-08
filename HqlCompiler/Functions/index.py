from HqlCompiler.Exceptions import *
from HqlCompiler.Registry import register_func
import logging
from .__proto__ import Function

# This is a meta function resolved while parsing
@register_func('index')
class index(Function):
    def __init__(self, args:list):
        super().__init__(args)
        self.expected = 1
        
        if len(self.args) != self.expected:
            logging.error(f'{self.name} call has an invalid number of arguments')
            logging.error(f'Got {len(args)}, expected {self.expected}')
            raise ArgumentException(f'Function argument exception')

        if self.args[0].type not in ('StringLiteral', 'EscapedName'):
            raise ArgumentException(f'Bad database argument datatype {args[0].type}')
        
    def eval(self):
        raise CompilerException('Function type index not supposed to be called directly')
        
    