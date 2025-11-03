from typing import TYPE_CHECKING, Union
from Hql.Operators import Database
from Hql.Exceptions import HqlExceptions as hqle
import polars as pl
import sqlite3

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Operators import Operator
    from Hql.Context import Context
    from Hql.Compiler import BranchDescriptor
    from Hql.Expressions import NamedReference

class SQLite(Database):
    def __init__(self, config:dict, name:str='unnamed-database'):
        from Hql.Compiler import SqlCompiler
        Database.__init__(self, config, name=name)

        self.compiler = SqlCompiler()
        self.limit = self.config.get('max_rows', 100000)

        if 'path' not in self.config:
            raise hqle.ConfigException(f'Missing path in configuration for sqlite database {name}')
        self.path = self.config['path']

    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        from Hql.Compiler import BranchDescriptor

        if isinstance(op, BranchDescriptor):
            op = op.get_op()
        
        # Sql compiler auto-updates itself
        _, rej = self.compiler.add_op(op)
        if rej:
            return None, op
        return op, None

    def compile(self):
        from Hql.Operators import Take
        from Hql.Expressions import Integer
        import copy

        if self.limit > 0:
            compiler = copy.deepcopy(self.compiler)
            compiler.add_op(Take(Integer(self.limit), []))
        else:
            compiler = self.compiler

        return compiler.compile(None)
        
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'query': self.compile()
        }

    def eval(self, ctx:'Context', **kwargs) -> 'Data':
        from Hql.Data import Data, Table
        self.ctx = ctx
        
        query = self.compile()
        with sqlite3.connect(self.path) as conn:
            df = pl.read_database(query, conn)
        data = Data([Table(df=df, name=self.name)])

        return data
