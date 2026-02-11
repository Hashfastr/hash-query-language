from . import Database
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Data import Data, Table, Schema
from Hql.Context import Context, register_database 

import os
import requests
import logging
import polars as pl

from typing import Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Compiler import BranchDescriptor
    from Hql.Operators import Operator

# Index in a database to grab data from, extremely simple.
@register_database('JSON')
class JSON(Database):
    def __init__(self, config:dict, name:str='unnamed-json'):
        Database.__init__(self, config, name=name)
        
        self.name = name
        self.files:list[str] = []
        self.urls:list[str] = []
        conf = config.get('conf', dict())
        self.local_base = conf.get('local-base', None)
        self.http_base = conf.get('http-base', None)

        if not (self.local_base or self.http_base):
            raise hqle.ConfigException('JSON database config missing both local-base and http-base params')
        
        self.methods = [
            'file',
            'http',
            'macro'
        ]

        self.limits:dict[str, int] = dict()

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'files': [self.local_base + x for x in self.files],
            'urls': [self.http_base + x for x in self.urls],
            'limits': self.limits
        }

    def add_op(self, op: Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        from Hql.Compiler import BranchDescriptor
        from Hql.Operators import Take

        if isinstance(op, BranchDescriptor):
            assert op.op
            op = op.op

        if not isinstance(op, Take):
            return None, op

        limits = op.get_limits()

        if not limits['tables']:
            self.set_limit('*', limits['limit'])

        for i in limits['tables']:
            self.set_limit(i, limits['limit'])

        return op, None

    def recurse(self, path:str) -> list[str]:
        if self.local_base:
            path = f'{self.local_base}{os.sep}{path}'

        if not os.path.exists(path):
            return []

        if not os.path.isdir(path):
            return [path]

        json_files = []

        for filename in os.listdir(path):
            full_path = os.path.join(path, filename)
            if os.path.isfile(full_path) and filename.lower().endswith('.json'):
                json_files.append(full_path)

        return json_files
    
    def from_file(self, filename:str):
        # if self.local_base:
        #     path = f'{self.local_base}{os.sep}{filename}'
        # else:
        path = filename

        return open(path, mode='r')
        
    def from_url(self, url:str):
        from io import StringIO

        if self.http_base:
            url = f'{self.http_base}{url}'
        else:
            if not url.startswith('http'):
                raise hqle.ConfigException(f'Url is not a valid HTTP url: {url}')

        res = requests.get(url)
        if res.status_code != 200:
            raise hqle.QueryException(f'Could not query remote url {url}')
        
        return StringIO(res.text)
    
    # src used for error printing
    # Attempt to load as normal json then fall back to ndjson
    # We could use polars but it sucks in that it can't handle ambiguous multi-value
    # Maybe a rust rewrite problem? Or someone is smarter than me
    def load_data(self, f, name:str) -> list[dict]:
        import json, ndjson

        try:
            data = json.loads(f.read())
        except:
            try:
                # df = pl.read_ndjson(data, n_rows=self.limit)
                f.seek(0)
                reader = ndjson.reader(f)
                data = [x for x in reader]
            except:
                f.close()
                logging.critical(f'Could not load json or ndjson from {name}')
                raise hqle.QueryException('JSON database not given valid json data')

        f.close()

        limit = self.get_limit(name)
        if limit != None:
            data = data[:limit]

        return data

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
    
    def eval(self, ctx:Context, **kwargs) -> Data:
        from pathlib import Path

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
            for i in self.recurse(file):
                name = Path(i).parent.name
                f = self.from_file(i)
                data = self.load_data(f, name)
                table = Table(init_data=data, name=name)
                tables.append(table)

        for url in self.urls:
            s = self.from_url(url)
            data = self.load_data(s, url)
            table = Table(init_data=data, name=url)
            tables.append(table)
                
        return Data(tables=tables)
