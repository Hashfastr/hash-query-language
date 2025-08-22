from typing import Union, TYPE_CHECKING
from pathlib import Path
import logging

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context

if TYPE_CHECKING:
    from Hql.Query import Query

class HqlCompiler():
    def __init__(self, conf_file:Path, query:'Query'):
        from Hql.Data import Data

        self.query = query
        self.ctx = Context(Data())

    def run(self, ctx:Union[Context,None]=None, **kwargs):
        ctx = ctx if ctx else self.ctx
        
        if not ctx.root:
            logging.critical('No root statement compiled!')
            raise hqle.CompilerException('No root statement compiled before runtime!')
        
        return ctx.root.eval(ctx, preview=preview)

    def decompile(self):
        return self.query.decompile(self.ctx)
 
    def compile(self):
        from Hql.Query import Statement, LetStatement, QueryStatement
        from Hql.Data import Data

        self.compiled = []
        self.op_sets = []
        ctx = Context(Data())
                
        statement = self.query.statements
        
        for statement in self.query.statements:
            if isinstance(statement, Statement):
                logging.debug(f'Handling {statement.type}')
                root = statement.root

            else:
                raise hqle.CompilerException(f'Unhandled statement type {statement.type}')

            cs = root.eval(ctx, no_exec=True)
                                
            if isinstance(statement, LetStatement):
                name = statement.name.eval(ctx, as_str=True)
                ctx.symbol_table[name] = cs
                
            elif isinstance(statement, QueryStatement):
                if ctx.root:
                    logging.warning('Overwriting root compiler set, bug?')
                    
                ctx.root = cs

            else:
                raise hqle.CompilerException(f'Unhandled statement type {statement.type}')
                
        self.ctx = ctx
