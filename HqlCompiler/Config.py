import json
import logging
import inspect
from . import Exceptions

class Config():
    def __init__(self, conf_file:str):
        with open(conf_file, mode='r') as f:
            self.conf = json.loads(f.read())
    
    def is_database(self, name:str):        
        if name in self.conf['databases']:
            return True
        return False
    
    def get_database(self, name:str):
        try:
            return self.conf['databases'][name]
        except KeyError:
            logging.critical('Config file is missing databases definition')
            logging.critical('Check that your config contains a database')
            raise Exceptions.ConfigException('Missing database definition')

global HqlConfig
HqlConfig = None