from .. import Operator
from .. import Data
from .. import Context
from .. import QueryException, CompilerException

import logging

class Database(Operator):
    def __init__(self, config:dict):
        Operator.__init__(self)

        self.dbtype = self.__class__.__name__
        self.type = "Database"
        
        self.ctx = None
        self.config = config
        
        self.ops = []
        self.compatible = []

    def add_op(self, op:Operator):
        if self.can_integrate(op.type):
            self.ops.append(op)
        else:
            logging.critical(f"Attempting to add invalid op type {op.type} to {self.dbtype}")
            logging.critical(f"Are you checking against can_integrate() before adding?")
            raise CompilerException(f"Incompatible op {op.type} added to {self.dbtype}")
    
    def eval_ops(self):
        pass

    def can_integrate(self, type:str):
        return type in self.compatible
    
    def make_query(self) -> Data:
        return Data()
    
    def eval(self, ctx:Context, **kwargs):
        self.ctx = ctx
        return self.make_query()
    
    def get_variable(self, name: str):
        raise QueryException(f'{self.dbtype} database has no variables')
