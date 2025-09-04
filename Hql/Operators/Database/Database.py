from typing import TYPE_CHECKING, Union
from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Context import Context
    from Hql.Compiler import BranchDescriptor

class Database(Operator):
    def __init__(self, config:dict, name:str='unnamed-database'):
        from Hql.Compiler import Compiler
        from Hql.Context import Context
        from Hql.Data import Data
        Operator.__init__(self)

        self.type = self.__class__.__name__
        
        self.ctx = Context(Data())
        self.config = config
        self.compiler = Compiler()
        self.name = name
        self.index = ''

    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        return self.compiler.add_op(op)

    def add_index(self, index:str):
        self.index = index

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
        }

    def eval(self, ctx:'Context', **kwargs) -> 'Data':
        from Hql.Data import Data
        self.ctx = ctx
        return Data()
    
    def get_variable(self, name:str) -> object:
        raise hqle.QueryException(f'{self.type} database has no variables')

    def get_macro(self, name:str) -> Union[None, dict]:
        macros = self.config.get('macro', dict())
        return macros.get(name, None)
