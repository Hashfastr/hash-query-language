from HqlCompiler.Exceptions import *
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import *

import os
import json, ndjson
import requests
import logging
from .__proto__ import Database

# Index in a database to grab data from, extremely simple.
@register_database('JSON')
class JSON(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.files = None
        self.urls = None
        self.base_path = config.get('BASE_PATH', None)
        if not self.base_path:
            raise ConfigException('JSON database config missing base_path parameter.')
        
        self.methods = [
            'file',
            'http'
        ]
    
    def from_file(self, filename:str) -> str:
        base = self.base_path if self.base_path else '.'
        
        with open(f'{base}{os.sep}{filename}', mode='r') as f:
            data = self.load_data(f.read(), src=f"{self.base_path}{os.sep}{filename}")
            
        return data
        
    def from_url(self, url:str) -> str:
        url = f'{self.base_path}{url}' if self.base_path else url
        
        res = requests.get(url)
        if res.status_code != 200:
            raise QueryException(f'Could not query remote url {url}')
        
        return self.load_data(res.text, src=url)
    
    # src used for error printing
    def load_data(self, data:str, src:str) -> list[dict]:
        try:
            jdata = json.loads(data)
        except:
            try:
                jdata = ndjson.loads(data)
            except:
                logging.critical(f'Could not load json or ndjson from {src}')
                raise QueryException('JSON database not given valid json data')

        return jdata
    
    def make_query(self) -> dict:
        # just check file, base_path is check upon instanciation
        if not self.files and not self.urls:
            logging.critical('No file or http provided to JSON database')
            logging.critical('Correct usages:')
            logging.critical('                database("json").file("filename")')
            logging.critical('                database("json").http("file.json")')
            logging.critical('Where filename exists relative to the configured BASE_PATH')
            logging.critical('Similarly, file.json represents a file on a server prepended by BASE_PATH')
            logging.critical('If basepath is not specified it is taken as literal for http, or current dir for file.')
            raise QueryException('No file provided to JSON database')
        
        tables = []
        if self.files:
            for file in self.files:
                tables.append(Table(init_data=self.from_file(file), name=file))
        else:
            for url in self.urls:
                # Get the filename
                name = url.split('/')[-1]
                tables.append(Table(init_data=self.from_url(url), name=name))
                
        return Data(tables=tables)