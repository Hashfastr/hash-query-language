import logging
import json

class Container():
    def __init__(self):
        pass
    
class IndexContainer(Container):
    def __init__(self, conf_file:str, pattern:str):
        super().__init__()
        self.type = 'index'
        self.pattern = pattern
        self.posfilters = []
        self.negfilters = []
        
        # load the template file
        with open(conf_file, mode='r') as f:
            self.conf = json.loads(f.read())
        
    def to_dict(self):
        out = {
            'ELASTIC_HOSTS': self.conf.get('ELASTIC_HOSTS', ['http://localhost:9200']),
            'ELASTIC_USER': self.conf.get('ELASTIC_USER', 'elastic'),
            'ELASTIC_PASS': self.conf.get('ELASTIC_PASS', 'changeme'),
            'VALIDATE_CERTS': self.conf.get('VALIDATE_CERTS', False),
            'SCROLL_TIME': self.conf.get('SCROLL_TIME', '10m'),
            'TIMEOUT': self.conf.get('TIMEOUT', 10),
            'INDEX': self.pattern,
            'DEBUG': self.conf.get('DEBUG', False),
            'QUERY': {}
        }
        
        out['QUERY']['must'] = self.posfilters
        out['QUERY']['must_not'] = self.negfilters
        
        return out


    def add_filter(self, expression:dict):
        filter = None
        
        # Positive filters
        if expression['type'] == '==':
            filter = {
                'term': {
                    expression['lh'] : expression['rh']
                }
            }
        elif expression['type'] == '<':
            filter = {
                'range': {
                    expression['lh'] : { 'lt': expression['rh'] }
                }
            }
        elif expression['type'] == '<=':
            filter = {
                'range': {
                    expression['lh'] : { 'lte': expression['rh'] }
                }
            }
        elif expression['type'] == '>':
            filter = {
                'range': {
                    expression['lh'] : { 'gt': expression['rh'] }
                }
            }
        elif expression['type'] == '>=':
            filter = {
                'range': {
                    expression['lh'] : { 'gte': expression['rh'] }
                }
            }
            
        if filter:
            self.posfilters.append(filter)
            return
        
        # Negative filters
        if expression['type'] == '!=':
            filter = {
                'term': {
                    expression['lh'] : expression['rh']
                }
            }
            
        if filter:
            self.negfilters.append(filter)
            return
        else:
            raise f"Invalid filter type {expression['type']}"            
    