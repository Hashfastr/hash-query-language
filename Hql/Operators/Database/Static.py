from . import Database
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Data import Data
from Hql.Context import register_database, Context

'''
Static DB, just give it a data object and it'll act like a Database.
Not much else to it.
'''
# @register_database('Static')
class Static(Database):
    def __init__(self, data:Data):
        Database.__init__(self, dict())
        self.data = data
     
    def eval(self, ctx: Context, **kwargs) -> Data:
        return self.data
