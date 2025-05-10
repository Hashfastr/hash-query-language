from HqlCompiler.Exceptions import *
from HqlCompiler.Registry import register_func
from HqlCompiler.Operators.Database import Database
import logging
from .__proto__ import Function

# This is a meta function resolved while parsing
@register_func('index')
class index(Function):
    def __init__(self, args:list):
        super().__init__(args, 1, 1)

        if self.args[0].type not in ('StringLiteral', 'EscapedName'):
            raise ArgumentException(f'Bad database argument datatype {args[0].type}')
        
    def eval(self, *args):
        db = args[0]
        
        if db and issubclass(type(db), Database):
            db.add_index(self.args[0].get_value())
        else:
            raise CompilerException(f'Function {self.name} cannot be called on {db}')
        
        return db
        
    