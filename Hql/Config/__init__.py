import json
import logging
from typing import Union
from pathlib import Path
import oyaml as yaml
from Hql.Exceptions import HqlExceptions as hqle

class Config():
    def __init__(self, path:Union[Path, None]=None):
        # skeleton
        self.conf = {
            'general': {},
            'databases': {},
            'products': {}
        }

        if path:
            self.load(path)

    def load(self, path:Path):
        files = []

        # If this triggers, the below loop won't run
        if path.is_file():
            files.append(path)

        for file in path.rglob("*"):
            if file.is_file():
                files.append(file)

        for i in files:
            self.load_file(i)

    def load_file(self, path:Path):
        with path.open(mode='r') as f:
            parsed = yaml.load(f, yaml.SafeLoader)

        if not parsed:
            return

        # Elevate to the generic config format
        # That is, a top level 'config' with a list of dicts
        if 'config' not in parsed:
            parsed = {'config': [parsed]}

        src = path.name

        # loop through config groupings
        for i in parsed['config']:
            # Get top level keys for each config signifying type
            for j in i:
                if j == 'database':
                    self.add_database(src, i[j])

                elif j == 'general':
                    self.load_general(src, i[j])

                elif j == 'product':
                    self.load_product(src, i[j])

                else:
                    logging.error(f'Invalid config block {j}')

    def add_database(self, src:str, config:dict):
        for i in ['name', 'type', 'conf']:
            if i not in config:
                raise hqle.ConfigException(f'Database config {src} missing required key {i}')
        
        name = config['name']
        if name in self.conf['databases']:
            raise hqle.ConfigException(f'Duplicate definition of database {name} in {src}')

        self.conf['databases'][name] = config
    
    def is_database(self, name:str) -> bool:
        return name in self.conf['databases']
    
    def get_database(self, dbname:str) -> dict:
        if dbname not in self.conf['databases']:
            logging.critical(f'Config file for {dbname} is missing databases definition')
            logging.critical('Check that your config contains a database under that name')
            raise hqle.ConfigException(f'Missing database definition {dbname}')
            
        return self.conf['databases'][dbname]

    def load_general(self, src:str, config:dict):
        if self.conf['general']:
            raise hqle.ConfigException(f'Duplicate definition of the top-level general config in {src}')

        self.conf['general'] = config
        
    def get_default_db(self) -> dict:
        if 'default_db' not in self.conf['general']:
            logging.critical('Config file is missing databases definition')
            logging.critical('Check that your config contains a database')
            raise hqle.ConfigException('Missing database definition')
        
        name = self.conf['general']['default_db']
        return self.get_database(name)

    def load_product(self, src:str, config:dict):
        if not config.get('configured', True):
            return

        for i in ['name', 'hql']:
            if i not in config:
                raise hqle.ConfigException(f'Product config {src} missing required key {i}')
        name = config['name']

        if name in self.conf['products']:
            raise hqle.ConfigException(f'Duplicate product definition: {name} in {src}')

        self.conf['products'][name] = config

    def get_product(self, name:str) -> dict:
        if name in self.conf['products']:
            return self.conf['products'][name]
        raise hqle.ConfigException(f'Attempting to get undefined product {name}')
