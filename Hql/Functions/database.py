from . import Function
from Hql import Config
from Hql.Context import register_func, Context
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions import StringLiteral

import logging

# This is a meta function resolved while parsing
@register_func('database')
class database(Function):
    def __init__(self, args:list):
        Function.__init__(self, args, 0, 1)
        self.preprocess = True

        if args and not isinstance(args[0], StringLiteral):
            raise hqle.ArgumentException(f'Bad database argument datatype {args[0].type}')

        if args:
            self.dbname = self.args[0].eval(None, as_str=True)
            self.default = self.dbname == ''
        else:
            self.dbname = ''
            self.default = True
            
    def eval(self, ctx:'Context', **kwargs):
        if self.default:
            dbconf = ctx.config.get_default_db()
            name = 'default'
        else:
            dbconf = ctx.config.get_database(self.dbname)
            name = self.dbname
        
        if 'type' not in dbconf:
            logging.critical('Missing database type in database config')
            logging.critical(f"Available DB types: {', '.join(ctx.get_db_types())}")
            raise hqle.ConfigException(f'Missing TYPE definition in database config for {name}')

        return ctx.get_db(dbconf['type'])(dbconf, name=name)
