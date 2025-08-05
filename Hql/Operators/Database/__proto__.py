from typing import TYPE_CHECKING
import logging

from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Context import Context

class Database(Operator):
    def __init__(self, config:dict):
        Operator.__init__(self)

        # self.type = self.__class__.__name__
        
        self.ctx = None
        self.config = config
        
        self.ops = []
        self.compatible = []

    def add_op(self, op:Operator):
        if self.can_integrate(op.type):
            self.ops.append(op)
        else:
            logging.critical(f"Attempting to add invalid op type {op.type} to {self.type}")
            logging.critical(f"Are you checking against can_integrate() before adding?")
            raise hqle.CompilerException(f"Incompatible op {op.type} added to {self.type}")
    
    def eval_ops(self):
        pass
    
    def make_query(self) -> 'Data':
        from Hql.Data import Data
        return Data()
    
    def eval(self, ctx:'Context', **kwargs):
        self.ctx = ctx
        return self.make_query()
    
    def get_variable(self, name:str) -> object:
        raise hqle.QueryException(f'{self.type} database has no variables')
