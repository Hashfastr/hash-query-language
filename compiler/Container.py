import compiler.Guid as Guid
import json

class Container():
    def __init__(self):
        self.type = ''
        self.guid = Guid.gen_guid()
        
    def get_type(self):
        return self.type
    
    def to_dict(self):
        return {}
    
    def __str__(self):
        return json.dumps(self.to_dict(), indent=2)
    
    def __repr__(self):
        return self.__str__()
    
class IndexContainer(Container):
    def __init__(self, conf:str, pattern:str):
        super().__init__()
        self.type = 'index'
        self.pattern = pattern
        self.posfilters = []
        self.negfilters = []
        self.conf = conf
        
    def to_dict(self):
        out = {
            'type': self.type,
            'guid': self.guid,
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
        
        out['QUERY']['bool'] = {}
        
        if self.posfilters != []:
            out['QUERY']['bool']['must'] = self.posfilters
            
        if self.negfilters != []:
            out['QUERY']['bool']['must_not'] = self.negfilters
        
        return out

    def add_filter(self, expression:dict):
        filter = None
        
        # Positive filters
        if expression['type'] == '==':
            filter = {
                'term': {
                    expression['lh']['name'] : expression['rh']['value']
                }
            }
        elif expression['type'] == '<':
            filter = {
                'range': {
                    expression['lh']['name'] : { 'lt': expression['rh']['value'] }
                }
            }
        elif expression['type'] == '<=':
            filter = {
                'range': {
                    expression['lh']['name'] : { 'lte': expression['rh']['value'] }
                }
            }
        elif expression['type'] == '>':
            filter = {
                'range': {
                    expression['lh']['name'] : { 'gt': expression['rh']['value'] }
                }
            }
        elif expression['type'] == '>=':
            filter = {
                'range': {
                    expression['lh']['name'] : { 'gte': expression['rh']['value'] }
                }
            }
        elif expression['type'] == 'between':
            filter = {
                'range': {
                    expression['lh']['name'] : {
                        'gte': expression['rh']['start']['value'],
                        'lte': expression['rh']['end']['value']
                    }
                }
            }
            
        if filter:
            self.posfilters.append(filter)
            return
        
        # Negative filters
        if expression['type'] == '!=':
            filter = {
                'term': {
                    expression['lh']['name'] : expression['rh']['value']
                }
            }
            
        if filter:
            self.negfilters.append(filter)
            return
        else:
            raise Exception(f"Invalid filter type {expression['type']}")
    