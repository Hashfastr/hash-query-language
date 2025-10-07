from . import Database

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Data import Data, Table, Schema
from Hql.Context import register_database

from typing import TYPE_CHECKING, Union

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
            'http'
        ]
        
        self.compatible = [
            'Take'
        ]
        
        self.take_sets = []
    
    def eval_ops(self):
        for op in self.ops:
            if op.type == 'Take':
                self.take_sets.append(op.get_limits())
    
    def from_file(self, filename:str, limit:Union[None, int]=None) -> Table:
        try:
            base = self.base_path if self.base_path else '.'
            
            with open(f'{base}{os.sep}{filename}', mode='r') as f:
                data = pl.read_csv(f, n_rows=limit)
        except:
            logging.critical(f'Could not load csv from {filename}')
            raise hqle.QueryException('CSV databse not given valid csv data')
                
        return Table(df=data, name=filename)
        
    def from_url(self, url:str, limit:Union[None, int]=None) -> Table:
        try:
            url = f'{self.base_path}/{url}' if self.base_path else url
            
            res = requests.get(url)
            if res.status_code != 200:
                raise hqle.QueryException(f'Could not query remote url {url}')
            
            name = url.split('/')[-1]
            reader = StringIO(res.text)
            data = pl.read_csv(reader, n_rows=limit)
        
            return Table(df=data, name=name)
        except:
            logging.critical(f'Could not load csv from {url}')
            raise hqle.QueryException('CSV databse not given valid csv data')

    def limit(self, name:str):
        min_limit = None
        for take_set in self.take_sets:
            limit = take_set['limit']

            # In the case of no tables specified, meaning all tables
            if len(take_set['tables']) == 0:
                min_limit = limit
                continue

            for table in take_set['tables']:
                if name.startswith(table.split('*')[0]) and not min_limit:
                    min_limit = limit
                elif limit < min_limit:
                    min_limit = limit

        return min_limit
                
    def make_query(self) -> Data:
        # just check file, base_path is check upon instanciation
        if not self.files and not self.urls:
            logging.critical('No file or http provided to CSV database')
            logging.critical('Correct usages:')
            logging.critical('                database("csv").file("filename")')
            logging.critical('                database("csv").http("https://host/file.csv")')
            logging.critical('Where filename exists relative to the configured base_path')
            raise hqle.QueryException('No file provided to CSV database')
        
        self.eval_ops()
        
        self.files = self.files if self.files else []
        self.urls = self.urls if self.urls else []
        
        tables = []
        for file in self.files:
            limit = self.limit(file)
            tables.append(self.from_file(file, limit=limit))

        for url in self.urls:
            limit = self.limit(url.split('/')[-1])
            tables.append(self.from_url(url, limit=limit))
                
        return Data(tables=tables)
