from typing import TYPE_CHECKING
from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Context import Context

class Database(Operator):
    def __init__(self, config:dict):
        from Hql.Compiler import Compiler

        Operator.__init__(self)

        self.type = self.__class__.__name__
        
        self.ctx = None
        self.config = config
        self.compiler = Compiler()

    def add_op(self, op:Operator):
        self.compiler.add_op(op)

    def exec_query(self) -> 'Data':
        from Hql.Data import Data

        query = self.compiler.compile()
        # ES.query(query)

        return Data()

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'query': self.compiler.compile(),
            # 'ops': [x.to_dict() for x in self.ops]
        }
    
    def eval(self, ctx:'Context', **kwargs):
        self.ctx = ctx
        return self.exec_query()
    
    def get_variable(self, name:str) -> object:
        raise hqle.QueryException(f'{self.type} database has no variables')
