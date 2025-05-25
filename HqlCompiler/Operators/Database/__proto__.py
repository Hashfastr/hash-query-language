from HqlCompiler.Operators.Operator import Operator
from HqlCompiler.Data import Data
from HqlCompiler.Context import Context
from HqlCompiler.Exceptions import *

class Database(Operator):
    def __init__(self, config:dict):
        Operator.__init__(self)

        self.dbtype = self.__class__.__name__
        self.type = "Database"
        
        self.ctx = None
        self.config = config

    def add_op(self, op:Operator):
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