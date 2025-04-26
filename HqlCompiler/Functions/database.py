from ..Config import Config
import logging
import json
from ..Registry import register_func
import HqlCompiler.Exceptions

# This is a meta function resolved while parsing
@register_func('database')
class database():
    def __init__(self, args:list):
        self.args = args
        self.name = 'database'
        self.expected = 1
        
        if len(args) != self.expected:
            logging.error(f'{self.name} call has an invalid number of arguments')
            logging.error(f'Got {len(args)}, expected {self.expected}')
            raise ArgumentException(f'Function argument exception')

        if args[0].type != 'StringLiteral':
            raise ArgumentException(f'Bad database argument datatype {args[0].type}')

    def to_dict(self):
        return {
            'type': 'function',
            'name': self.name,
            'args': self.args
        }
    
    def __str__(self) -> str:
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self) -> str:
        return self.__str__()
        
    def eval(self, config:Config):
        return {
            'results': [
                config.get_database(self.args[0].value)
            ]
        }