import json
import logging
from typing import Optional, Union
from pathlib import Path
import oyaml as yaml
from Hql.Exceptions import HqlExceptions as hqle

class Config():
    def __init__(self, path:Union[Path, None]=None):
        # skeleton
        self.conf = {
            'general': {},
            'databases': {},
            'products': {},
            'functions': {},
            'sigma': {
                'posthql': {}
            }
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

                elif j == 'function':
                    self.load_function(src, i[j])

                elif j == 'sigma':
                    self.load_sigma(src, i[j])

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

        if 'name' not in config:
            raise hqle.ConfigException(f'Product config {src} missing required key name')

        if 'hql' not in config and 'upstream' not in config:
            raise hqle.ConfigException(f'Product config {src} missing required key hql or upstream')

        if 'hql' in config:
            config['upstream'] = [config.pop('hql')]

        name = config['name']

        if name in self.conf['products']:
            raise hqle.ConfigException(f'Duplicate product definition: {name} in {src}')

        self.conf['products'][name] = config

    def load_function(self, src:str, config:dict):
        for i in ['name', 'conf']:
            if i not in config:
                raise hqle.ConfigException(f'Function config {src} missing required key {i}')
        
        name = config['name']
        if name in self.conf['functions']:
            raise hqle.ConfigException(f'Duplicate definition of function {name} in {src}')

        self.conf['functions'][name] = config

    def load_sigma(self, src:str, config:dict):
        posthql = config.get('posthql', dict())
        default = ''
        for i in posthql:
            if i == 'default':
                default = posthql[i]
                continue

            if 'hql' not in posthql[i]:
                raise hqle.ConfigException(f'Missing sigma posthql field hql in {src}')
            
            if i in self.conf['sigma']['posthql']:
                raise hqle.ConfigException(f'Duplicate definition of sigma posthql {i} in {src}')

            self.conf['sigma']['posthql'][i] = posthql[i]

        if default:
            if default not in self.conf['sigma']['posthql']:
                raise hqle.ConfigException(f'Default sigma posthql identifier {default} points to nowhere')
            self.conf['sigma']['posthql']['default'] = self.conf['sigma']['posthql'][default]

    def get_function(self, name:str) -> dict:
        if name in self.conf['functions']:
            return self.conf['functions'][name].get('conf', dict())
        return dict()

    def get_product(self, name:str) -> dict:
        if name in self.conf['products']:
            return self.conf['products'][name]
        raise hqle.ConfigException(f'Attempting to get undefined product {name}')

    def get_posthql(self, name:str) -> dict:
        if name in self.conf['sigma']['posthql']:
            return self.conf['sigma']['posthql'][name]
        raise hqle.ConfigException(f'Attempting to get unconfigured posthql sigma definition {name}')
