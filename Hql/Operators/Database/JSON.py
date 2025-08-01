from .__proto__ import Database
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Data import Data, Table, Schema
from Hql.Context import Context, register_database 

import os
import requests
import logging
import polars as pl

from typing import Union

# Index in a database to grab data from, extremely simple.
@register_database('JSON')
class JSON(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.files:list[str] = []
        self.urls:list[str] = []
        self.base_path = config.get('BASE_PATH', None)
        if not self.base_path:
            raise hqle.ConfigException('JSON database config missing base_path parameter.')
        
        self.methods = [
            'file',
            'http'
        ]

        self.limit:Union[None, int] = None
    
    def from_file(self, filename:str):
        base = self.base_path if self.base_path else '.'
        return open(f'{base}{os.sep}{filename}', mode='r')
        
    def from_url(self, url:str):
        from io import StringIO

        url = f'{self.base_path}{url}' if self.base_path else url
        
        res = requests.get(url)
        if res.status_code != 200:
            raise hqle.QueryException(f'Could not query remote url {url}')
        
        return StringIO(res.text)
    
    # src used for error printing
    # Attempt to load as normal json then fall back to ndjson
    # We could use polars but it sucks in that it can't handle ambiguous multi-value
    # Maybe a rust rewrite problem? Or someone is smarter than me
    def load_data(self, f, src:str) -> list[dict]:
        import json, ndjson

        try:
            '''
            df = pl.read_json(data, infer_schema_length=1000000)
            if self.limit != None:
                df = df.limit(self.limit)
            '''

            data = json.loads(f.read())
            if self.limit != None:
                data = data[:self.limit]

        except:
            try:
                # df = pl.read_ndjson(data, n_rows=self.limit)
                reader = ndjson.reader(f)
                data = [x for x in reader]
            except:
                f.close()
                logging.critical(f'Could not load json or ndjson from {src}')
                raise hqle.QueryException('JSON database not given valid json data')

        f.close()

        return data
    
    def make_query(self) -> Data:
        # just check file, base_path is check upon instanciation
        if not self.files and not self.urls:
            logging.critical('No file or http provided to JSON database')
            logging.critical('Correct usages:')
            logging.critical('                database("json").file("filename")')
            logging.critical('                database("json").http("file.json")')
            logging.critical('Where filename exists relative to the configured BASE_PATH')
            logging.critical('Similarly, file.json represents a file on a server prepended by BASE_PATH')
            logging.critical('If basepath is not specified it is taken as literal for http, or current dir for file.')
            raise hqle.QueryException('No file provided to JSON database')
        
        tables = []
        for file in self.files:
            f = self.from_file(file)
            data = self.load_data(f, file)
            table = Table(init_data=data, name=file)
            tables.append(table)

        for url in self.urls:
            s = self.from_url(url)
            data = self.load_data(s, url)
            table = Table(init_data=data, name=url)
            tables.append(table)
                
        return Data(tables=tables)
