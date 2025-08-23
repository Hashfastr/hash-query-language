from typing import Union, TYPE_CHECKING
import logging
import time

from Hql.Compiler import Compiler
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context

if TYPE_CHECKING:
    from Hql.Query import Query
    from Hql.Config import Config

class HqlCompiler(Compiler):
    def __init__(self, config:'Config', query:Union[None, 'Query']=None):
        Compiler.__init__(self)
        self.config = config
        self.Query(query)
        
    def run(self, ctx: Union[Context, None] = None) -> Context:
        ctx = ctx if ctx else self.ctx

        if not self.ops:
            raise hqle.QueryException('Running an empty compiler has no effect!')

        for i in self.ops:
            start = time.perf_counter()
            logging.debug(f'Executing {i.type}: {i.id}')
            
            ctx.data = i.eval(ctx)
            
            end = time.perf_counter()
            logging.debug(f"{i.id} - {end - start}")

        return ctx

