from HqlCompiler.Exceptions import *
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import *

import os
import polars as pl
from csv import DictReader
import logging

from HqlCompiler.Operators.Operator import Operator
from .__proto__ import Database

# Index in a database to grab data from, extremely simple.
@register_database('CSV')
class CSV(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.files = None
        self.base_path = config.get('BASE_PATH', None)
        if not self.base_path:
            raise ConfigException('CSV database config missing base_path parameter.')
        
        self.methods = [
            'file'
        ]
        
        self.compatible = [
            'Take'
        ]
        
        self.n_rows = None
    
    def eval_ops(self):
        for op in self.ops:
            if op.type == 'Take':
                self.n_rows = op.expr.eval(self.ctx)
                if not isinstance(self.n_rows, int):
                    raise QueryException(f'Take operator passed non-int type {self.n_rows}')
    
    def load_file(self, filename:str) -> Table:        
        with open(f'{self.base_path}{os.sep}{filename}', mode='r') as f:
            data = pl.read_csv(f, n_rows=self.n_rows)
                
        return Table(df=data, name=filename)

    def make_query(self) -> dict:
        # just check file, base_path is check upon instanciation
        if not self.files:
            logging.critical('No file provided to CSV database')
            logging.critical('Correct usage: database("csv").file("filename")')
            logging.critical('Where filename exists relative to the configured base_path')
            raise QueryException('No file provided to CSV database')
        
        self.eval_ops()
                
        return Data(tables_list=[self.load_file(x) for x in self.files])