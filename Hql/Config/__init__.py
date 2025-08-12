import json
import logging
from typing import Union
from pathlib import Path
import oyaml as yaml
from Hql.Exceptions import HqlExceptions as hqle

class Config():
    def __init__(self, conf_path:str):
        # skeleton
        self.conf = {
            'general': {},
            'databases': {}
        }

        self.load(conf_path)

    def load(self, conf_path:str):
        path = Path(conf_path)

        files = []

        # If this triggers, the below loop won't run
        if path.is_file:
            files.append(path)

        for file in path.rglob("*"):
            if file.is_file():
                files.append(file)

        for i in files:
            self.load_file(i)

    def load_file(self, path:Path):
        with open(path, mode='r') as f:
            parsed = yaml.load(f, yaml.SafeLoader)

        # elevate to the generic config format
        if 'config' not in parsed:
            parsed = {'config': [parsed]}

        src = path.name

        # loop through config groupings
        for i in parsed['config']:
            # Get top level keys for each config signifying type
            for j in i:
                if j == 'database':
                    self.add_database(src, i[j])

                if j == 'general':
                    self.load_general(src, i[j])

    def add_database(self, src:str, config:dict):
        for i in ['name', 'type', 'conf']:
            if i not in config:
                raise hqle.ConfigException(f'Database config {src} missing required key {i}')
        
        name = config['name']
        if name in self.conf['databases']:
            raise hqle.ConfigException(f'Duplicate definition of database {name} in {src}')

        self.conf['databases'][name] = config

    def load_general(self, src:str, config:dict):
        if len(self.conf['general']):
            raise hqle.ConfigException(f'Duplicate definition of the top-level general config in {src}')

        self.conf['general'] = config
    
    def is_database(self, name:str):        
        if name in self.conf['databases']:
            return True
        return False
    
    def get_database(self, dbname:str):
        try:
            return self.conf['databases'][dbname]
        except KeyError:
            logging.critical(f'Config file for {dbname} is missing databases definition')
            logging.critical('Check that your config contains a database under that name')
            raise hqle.ConfigException(f'Missing database definition {dbname}')
        
    def get_default_db(self):
        try:
            default_name = self.conf['DEFAULT_DB']
        except KeyError:
            logging.critical('Config file is missing databases definition')
            logging.critical('Check that your config contains a database')
            raise hqle.ConfigException('Missing database definition')
        
        return self.get_database(default_name)

    def get_base_path(self, dbname:str):
        try:
            return self.conf['databases'][dbname]['BASEPATH']
        except KeyError:
            logging.critical('Base path unconfigured for file operations')
            raise hqle.ConfigException('Missing base path configuration')

global HqlConfig
HqlConfig = Config()
