from . import Function
from Hql import Config
from Hql.Context import register_func, Context
from Hql.Exceptions import HqlExceptions as hqle

import logging

# This is a meta function resolved while parsing
@register_func('database')
class database(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 0, 1)
        self.preprocess = True
        
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
            raise hqle.ArgumentException(f'Bad database argument datatype {args[0].type}')
            
    def eval(self, ctx:'Context', **kwargs):
        name = self.args[0].eval(None, as_str=True)
        if self.args == [] or name == '':
            dbconf = ctx.config.get_default_db()
            name = 'default'
        else:
            dbconf = ctx.config.get_database(name)
        
        if 'type' not in dbconf:
            logging.critical('Missing database type in database config')
            logging.critical(f"Available DB types: {', '.join(ctx.get_db_types())}")
            raise hqle.ConfigException(f'Missing TYPE definition in database config for {name}')

        return ctx.get_db(dbconf['type'])(dbconf, name=name)
