import json
import logging
from typing import Union
from Hql.Exceptions import HqlExceptions as hqle

class Config():
    def __init__(self, conf_file:Union[None, str]=None):
        if conf_file:
            with open(conf_file, mode='r') as f:
                self.conf = json.loads(f.read())
    
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
