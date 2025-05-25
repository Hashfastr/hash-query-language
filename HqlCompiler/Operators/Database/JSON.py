from HqlCompiler.Exceptions import *
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import *

import os
import ndjson
import json
import logging
from .__proto__ import Database

# Index in a database to grab data from, extremely simple.
@register_database('JSON')
class JSON(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.file = None
        self.base_path = config.get('BASE_PATH', None)
        if not self.base_path:
            raise ConfigException('JSON database config missing base_path parameter.')
        
        self.methods = [
            'file'
        ]
       
    def make_query(self) -> dict:
        # just check file, base_path is check upon instanciation
        if not self.file:
            logging.critical('No file provided to JSON database')
            logging.critical('Correct usage: database("json").file("filename")')
            logging.critical('Where filename exists relative to the configured base_path')
            raise QueryException('No file provided to JSON database')
        
        with open(f'{self.base_path}{os.sep}{self.file}', mode='r') as f:
            data = f.read()
            
        try:
            jdata = json.loads(data)
        except:
            try:
                jdata = ndjson.loads(data)
            except:
                logging.critical(f'Could not load json or ndjson from file {self.base_path}{os.sep}{self.file}')
                raise QueryException('JSON database not given valid json data')

        table = Table(init_data=jdata, name=self.file)
        return Data.Data(tables_list=[table])