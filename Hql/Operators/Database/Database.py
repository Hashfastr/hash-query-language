from typing import TYPE_CHECKING
from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Context import Context

class Database(Operator):
    def __init__(self, config:dict):
        Operator.__init__(self)

        self.type = self.__class__.__name__
        
        self.ctx = None
        self.config = config
        
        self.ops = []
        self.compatible = []

        self.query = ''

    def compile(self) -> str:
        return ''

    def exec_query(self) -> 'Data':
        from Hql.Data import Data

        query = self.compile()
        # ES.query(query)

        return Data()

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'query': self.query,
            # 'ops': [x.to_dict() for x in self.ops]
        }
    
    def eval(self, ctx:'Context', **kwargs):
        if kwargs.get('preview', False):
            return self.to_dict()

        self.ctx = ctx
        return self.exec_query()
    
    def get_variable(self, name:str) -> object:
        raise hqle.QueryException(f'{self.type} database has no variables')
