from HqlCompiler.Exceptions import *
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import *

import os
import polars as pl
import logging
import requests
from io import StringIO

from .__proto__ import Database

# Index in a database to grab data from, extremely simple.
@register_database('CSV')
class CSV(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.files = None
        self.urls = None
        self.base_path = config.get('BASE_PATH', None)
        if not self.base_path:
            raise ConfigException('CSV database config missing base_path parameter.')
        
        self.methods = [
            'file',
            'http'
        ]
        
        self.compatible = [
            'Take'
        ]
        
        self.take_sets = None
    
    def eval_ops(self):
        if not self.take_sets:
            self.take_sets = []
        
        for op in self.ops:
            if op.type == 'Take':
                self.take_sets.append(op.get_limits(self.ctx))
    
    def from_file(self, filename:str, limit:int=None) -> str:
        try:
            base = self.base_path if self.base_path else '.'
            
            with open(f'{base}{os.sep}{filename}', mode='r') as f:
                data = pl.read_csv(f, n_rows=limit)
        except:
            logging.critical(f'Could not load csv from {filename}')
            raise QueryException('CSV databse not given valid csv data')
                
        return Table(df=data, name=filename)
        
    def from_url(self, url:str, limit:int=None) -> str:
        try:
            url = f'{self.base_path}/{url}' if self.base_path else url
            
            res = requests.get(url)
            if res.status_code != 200:
                raise QueryException(f'Could not query remote url {url}')
            
            name = url.split('/')[-1]
            reader = StringIO(res.text)
            data = pl.read_csv(reader, n_rows=limit)
        
            return Table(df=data, name=name)
        except:
            logging.critical(f'Could not load csv from {url}')
            raise QueryException('CSV databse not given valid csv data')

    def limit(self, name:str):
        min_limit = None
        for take_set in self.take_sets:
            limit = take_set[0]
            for table in take_set[1]:
                if name.startswith(table.split('*')[0]) and not min_limit:
                    min_limit = limit
                elif limit < min_limit:
                    min_limit = limit

        return min_limit
    
    def verify_tables(self, names:list[str]):
        tables = set()
        for i in self.take_sets:
            for j in i[1]:
                tables.add(j)

        unknown_tables = []
        for table in list(tables):
            matched = False
            for name in names:
                if name.startswith(table.split('*')[0]):
                    matched = True
            
            if not matched:
                logging.critical(f'Unknown table {table} referenced')
                unknown_tables.append(table)
                
        if unknown_tables:
            raise QueryException(f"Unknown table(s) {' '.join(unknown_tables)} referenced")
                
    def make_query(self) -> dict:
        # just check file, base_path is check upon instanciation
        if not self.files and not self.urls:
            logging.critical('No file or http provided to CSV database')
            logging.critical('Correct usages:')
            logging.critical('                database("csv").file("filename")')
            logging.critical('                database("csv").http("https://host/file.csv")')
            logging.critical('Where filename exists relative to the configured base_path')
            raise QueryException('No file provided to CSV database')
        
        self.eval_ops()
        
        self.files = self.files if self.files else []
        self.urls = self.urls if self.urls else []
        
        names = []
        for file in self.files:
            names.append(file)
        for url in self.urls:
            names.append(url.split('/')[-1])
        
        # Ensures that all take tables are real
        self.verify_tables(names)
        
        tables = []
        for file in self.files:
            limit = self.limit(file)
            tables.append(self.from_file(file, limit=limit))

        for url in self.urls:
            limit = self.limit(url.split('/')[-1])
            tables.append(self.from_url(url, limit=limit))
                
        return Data(tables=tables)