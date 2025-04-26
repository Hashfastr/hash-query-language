from HqlCompiler.Expression import Expression
from HqlCompiler.Registry import *

# Index in a database to grab data from, extremely simple.
@regsiter_index('Elasticsearch')
class Elasticsearch():
    def __init__(self, expression:Expression, config:dict):
        self.type = 'index'
        self.config = config
        
        self.posfilters = []
        self.negfilters = []

    def add_filter(self, expression:Expression):
        filter = None
        
        expr = expression.to_dict()
        
        # Positive filters
        if expr['type'] == '==':
            filter = {
                'term': {
                    expr['lh']['name'] : expr['rh']['value']
                }
            }
        elif expr['type'] == '<':
            filter = {
                'range': {
                    expr['lh']['name'] : { 'lt': expr['rh']['value'] }
                }
            }
        elif expr['type'] == '<=':
            filter = {
                'range': {
                    expr['lh']['name'] : { 'lte': expr['rh']['value'] }
                }
            }
        elif expr['type'] == '>':
            filter = {
                'range': {
                    expr['lh']['name'] : { 'gt': expr['rh']['value'] }
                }
            }
        elif expr['type'] == '>=':
            filter = {
                'range': {
                    expr['lh']['name'] : { 'gte': expr['rh']['value'] }
                }
            }
        elif expr['type'] == 'between':
            filter = {
                'range': {
                    expr['lh']['name'] : {
                        'gte': expr['rh']['start']['value'],
                        'lte': expr['rh']['end']['value']
                    }
                }
            }
            
        if filter:
            self.posfilters.append(filter)
            return
        
        # Negative filters
        if expr['type'] == '!=':
            filter = {
                'term': {
                    expr['lh']['name'] : expr['rh']['value']
                }
            }
            
        if filter:
            self.negfilters.append(filter)
            return
        else:
            raise Exception(f"Invalid filter type {expr['type']}")
    