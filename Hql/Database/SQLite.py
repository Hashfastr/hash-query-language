from typing import TYPE_CHECKING, Union
from Hql.Compiler.Sql.Statements import SELECT
from Hql.Operators.Database import Database
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context, register_database
import polars as pl
import sqlite3
import logging
from pathlib import Path

if TYPE_CHECKING:
    from Hql.Data import Data
    from Hql.Operators import Operator
    from Hql.Compiler import BranchDescriptor
    from Hql.Expressions import NamedReference

@register_database('SQLite')
class SQLite(Database):
    def __init__(self, config:dict, name:str='unnamed-database'):
        from Hql.Compiler import SqlCompiler
        Database.__init__(self, config, name=name)
        conf = self.config.get('conf', {})

        self.compiler = SqlCompiler(parent=self)
        self.limit = conf.get('max_rows', 100000)

        if 'path' not in conf:
            raise hqle.ConfigException(f'Missing path in configuration for sqlite database {name}')
        self.path = Path(conf['path']).expanduser()

        self.methods = [
            'index',
            'macro'
        ]

        self.projected = False

    def add_index(self, index:str):
        from Hql.Expressions import NamedReference
        self.get_variable(NamedReference(index))

    def get_variable(self, name:'NamedReference') -> 'SQLite':
        from Hql.Compiler.Sql import SELECT
        if isinstance(self.compiler.statement, SELECT):
            self.compiler.statement.src = name
            return self
        else:
            raise hqle.QueryException(f'Attempting to set SQLite table {name.name} in an incompatible context')

    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        from Hql.Compiler import BranchDescriptor
        from Hql.Operators import Project

        if isinstance(op, BranchDescriptor):
            op = op.get_op()

        if isinstance(op, Project):
            self.projected = True
        
        # Sql compiler auto-updates itself
        _, rej = self.compiler.add_op(op)
        if rej:
            return None, op
        return op, None

    def compile(self) -> str:
        from Hql.Operators import Take
        from Hql.Expressions import Integer
        import copy

        if self.limit > 0:
            if isinstance(self.compiler.statement, SELECT) and self.compiler.statement.limit:
                compiler = self.compiler
            else:
                compiler = copy.deepcopy(self.compiler)
                compiler.add_op(Take(Integer(self.limit), []))
        else:
            compiler = self.compiler

        acc, _ = compiler.compile(None)
        assert isinstance(acc, str)
        return acc
        
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'query': self.compile()
        }

    def eval(self, ctx:'Context', **kwargs) -> 'Data':
        from Hql.Data import Data, Table
        from Hql.Operators import Take, Project
        from Hql.Expressions import Integer, NamedReference
        import copy
        self.ctx = ctx
        
        # Make compiler check for joins
        self.compiler.compile(None)
        with sqlite3.connect(self.path) as conn:
            if not self.projected and not self.compiler.joins:
                logging.warning(f'SELECT * with JOINs can cause issues, predicting output schema by taking one')
                sample = copy.deepcopy(self)
                sample.add_op(Take(Integer(1), []))
                query = sample.compile()
                cursor = conn.execute(query)
                cols = [NamedReference(x[0]) for x in cursor.description]
                self.add_op(Project('project', cols))

            query = self.compile()
            df = pl.read_database(query, conn)
            
        data = Data([Table(df=df, name=self.name)])

        return data
