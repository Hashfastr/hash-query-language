from HqlCompiler.Operators.Operator import Operator
from HqlCompiler.Expression import Expression

# Index in a database to grab data from, extremely simple. 
class Index(Operator):
    def __init__(self, expression:Expression):
        super().__init__()
        self.type = 'index'
        self.expressions.append(expression)
        
        self.posfilters = []
        self.negfilters = []

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
    