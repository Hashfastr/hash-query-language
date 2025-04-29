from HqlCompiler.Expression import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Registry import *
from elasticsearch import Elasticsearch as ES
import polars as pl
import logging
import json

# Index in a database to grab data from, extremely simple.
@regsiter_index('Elasticsearch')
class Elasticsearch():
    def __init__(self, expression:Expression, config:dict):
        self.type = 'Index'
        self.config = config
        
        if expression.type == "PathExpression":
            self.pattern = '.'.join([x.ref for x in expression.path[1:]])
        else:
            raise Exception("Invalid Elasticsearch init expression")
                
        self.posfilters = []
        self.negfilters = []
        
        self.compatible = [
            'Where',
            'Take'
        ]
        
        # Set to the config default to avoid DoS
        # Can be changed by the take operator for example.
        self.limit = self.config.get('LIMIT', 100000)
        
        # Default scroll max, cannot be higher than 10k
        # Higher values are generally better, each request has some time to it
        # 10000 is faster than 10x1000
        self.scroll_max = self.config.get('SCROLL_MAX', 10000)
        
    def can_integrate(self, type:str):
        return type in self.compatible
    
    def add_op(self, op:Operator):
        if op.type == 'Where':
            self.add_filter(op.expressions[0])
        
        # should only have on expression
        if op.type == 'Take':
            self.add_limit(op.expressions[0].value)

    def execute(self, data:pl.DataFrame):
        return self.make_query()

    def get_filter(self):
        filter = {
            'bool': {
            }
        }
        
        if self.posfilters != []:
            filter['bool']['must'] = self.posfilters

        if self.negfilters != []:
            filter['bool']['must_not'] = self.negfilters
                    
        return filter
    
    def add_limit(self, limit:int):
        self.limit = limit

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
        elif expr['type'] == 'BetweenEquality':
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
    
    def make_query(self) -> dict:
        # Host, or hosts, to use for the query.
        # Should be in array format
        ELASTIC_HOSTS = self.config.get('ELASTIC_HOSTS', ['http://localhost:9200'])
        # Elastic user to use
        ELASTIC_USER = self.config.get('ELASTIC_USER', 'elastic')
        # Elastic user password to use
        ELASTIC_PASS = self.config.get('ELASTIC_PASS', 'changeme')
        # SSL Validation
        VALIDATE_CERTS = self.config.get('VALIDATE_CERTS', 'true')
        # How long should the scroll session be kept alive?
        SCROLL_TIME = self.config.get('SCROLL_TIME', '1m')
        # Query results limit per scroll
        # If the total limit is less than this number, it is set to the query limit.
        SCROLL_MAX = self.scroll_max if self.limit >= self.scroll_max else self.limit
        # Request timeout in seconds
        TIMEOUT = self.config.get('TIMEOUT', 10)

        # Debug?
        DEBUG = self.config.get('DEBUG', False)
        
        client = ES(
            ELASTIC_HOSTS,
            basic_auth=(ELASTIC_USER, ELASTIC_PASS),
            verify_certs=VALIDATE_CERTS,
            request_timeout=TIMEOUT,
            retry_on_timeout=True,
        )
        
        logging.debug("Starting initial query")

        body = {
            'query': self.get_filter()
        }

        res = client.search(
            index=self.pattern,
            size=SCROLL_MAX,
            scroll=SCROLL_TIME,
            body=body
        )
        sid = res['_scroll_id']
        
        logging.debug("Start scrolling")
        
        # Will scroll through until we reach our limit, or no more results.
        # Enables the take operator
        remainder = self.limit
        result_count = 0
        results = pl.DataFrame()
        while result_count < self.limit:
            logging.debug(f"Scroll {result_count} < {self.limit} max")
            
            if len(res['hits']['hits']) == 0:
                logging.debug(f"No more results to evaluate")
                logging.debug(f"Timed out? {res['timed_out']}")
                break
            
            # Ensure that we only print the number of remaining rows
            df = pl.from_dicts(res['hits']['hits'][:remainder]).unnest('_source')

            # print(json.dumps(data, indent=2))
            if results.is_empty():
                results = df
            else:
                pl.concat([results, df])
            result_count += len(df)
            
            remainder = self.limit - result_count
            
            res = client.scroll(
                scroll_id=sid,
                scroll=SCROLL_TIME,
            )                

        client.clear_scroll(scroll_id=sid)

        return results