import json
from . import Function
from Hql import Config
from Hql.Context import register_func, Context
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions import PipeExpression, StringLiteral
from typing import TYPE_CHECKING, Optional
from Hql.Compiler import HqlCompiler

import logging

if TYPE_CHECKING:
    from Hql.Expressions import PipeExpression

# This is a meta function resolved while parsing
@register_func('database')
class database(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
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

    def parse_preamble(self, preamble:dict, src:str) -> 'PipeExpression':
        from Hql.Parser import Parser
        from Hql.Expressions import PipeExpression

        if 'hql' not in preamble:
            raise hqle.ConfigException(f'Missing hql definition in config {src}')

        parser = Parser(preamble['hql'], src)
        parser.assemble(targets=['emptyPipedExpression'])
        if not isinstance(parser.assembly, PipeExpression):
            raise hqle.ConfigException(f'Invalid preamble expression in {src}')

        return parser.assembly
            
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Operators.Database import Database
        from Hql.Compiler import InstructionSet
        compiler = HqlCompiler(ctx.config)

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

        db = ctx.get_db(dbconf['type'])(dbconf, name=name)
        assert isinstance(db, Database)
        if db.get_preamble():
            preamble = self.parse_preamble(db.get_preamble(), f'{db.name}/preamble')
            db.preamble = preamble

        return db



