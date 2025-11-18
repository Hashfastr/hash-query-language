from . import Database

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Data import Data, Table, Schema
from Hql.Context import register_database

from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from Hql.Context import Context
    from Hql.Operators import Operator
    from Hql.Compiler import BranchDescriptor

import os
import polars as pl
import logging
import requests
from io import StringIO

# Index in a database to grab data from, extremely simple.
@register_database('CSV')
class CSV(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.files = None
        self.urls = None
        self.base_path = config.get('BASE_PATH', None)
        if not self.base_path:
            raise hqle.ConfigException('CSV database config missing base_path parameter.')
        
        self.methods = [
            'file',
            'http',
            'macro'
        ]
        
        self.limits:dict[str, int] = dict()

    def from_file(self, filename:str, limit:Optional[int]=None) -> Table:
        try:
            base = self.base_path if self.base_path else '.'
            
            with open(f'{base}{os.sep}{filename}', mode='r') as f:
                if limit != None:
                    data = pl.read_csv(f, n_rows=limit)
                else:
                    data = pl.read_csv(f)
        except:
            logging.critical(f'Could not load csv from {filename}')
            raise hqle.QueryException('CSV databse not given valid csv data')
                
        return Table(df=data, name=filename)
        
    def from_url(self, url:str, limit:Optional[int]=None) -> Table:
        try:
            url = f'{self.base_path}/{url}' if self.base_path else url
            
            res = requests.get(url)
            if res.status_code != 200:
                raise hqle.QueryException(f'Could not query remote url {url}')
            
            name = url.split('/')[-1]
            reader = StringIO(res.text)

            if limit != None:
                data = pl.read_csv(reader, n_rows=limit)
            else:
                data = pl.read_csv(reader)
        
            return Table(df=data, name=name)
        except:
            logging.critical(f'Could not load csv from {url}')
            raise hqle.QueryException('CSV databse not given valid csv data')

    def get_limit(self, name:str) -> Optional[int]:
        from fnmatch import fnmatch

        cur = None
        for i in self.limits:
            if fnmatch(name, i):
                if cur == None:
                    cur = self.limits[i]
                    continue
                cur = self.limits[i] if self.limits[i] < cur else cur

        return cur

    def set_limit(self, name:str, limit:int):
        cur = self.get_limit(name)
        if cur == None:
            self.limits[name] = limit
        else:
            # Ensure we don't override a smaller take
            self.limits[name] = limit if limit < cur else cur

    def add_op(self, op: Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        from Hql.Compiler import BranchDescriptor
        from Hql.Operators import Take, Operator

        if isinstance(op, BranchDescriptor):
            op = op.get_op()

        if isinstance(op, Take):
            limit = op.expr.eval(self.ctx)
            assert isinstance(limit, int)

            if not op.tables:
                self.set_limit('*', limit)

            for i in op.tables:
                name = i.eval(self.ctx, as_str=True)
                assert isinstance(name, str)
                self.set_limit(name, limit)

            return op, None

        return None, op
                
    def eval(self, ctx:'Context', **kwargs) -> Data:
        # just check file, base_path is check upon instanciation
        if not self.files and not self.urls:
            logging.critical('No file or http provided to CSV database')
            logging.critical('Correct usages:')
            logging.critical('                database("csv").file("filename")')
            logging.critical('                database("csv").http("https://host/file.csv")')
            logging.critical('Where filename exists relative to the configured base_path')
            raise hqle.QueryException('No file provided to CSV database')
        
        self.files = self.files if self.files else []
        self.urls = self.urls if self.urls else []
        
        tables = []
        for file in self.files:
            limit = self.get_limit(file)
            tables.append(self.from_file(file, limit=limit))

        for url in self.urls:
            limit = self.get_limit(url.split('/')[-1])
            tables.append(self.from_url(url, limit=limit))
                
        return Data(tables=tables)
