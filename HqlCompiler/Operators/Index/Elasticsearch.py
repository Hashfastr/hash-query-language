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
            'Where'
        ]
        
    def can_integrate(self, type:str):
        return type in self.compatible
    
    def add_op(self, op:Operator):
        if op.type == 'Where':
            self.add_filter(op.expressions[0])

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
        # How many rows should we scroll per scroll?
        # Max is 10000
        SCROLL_SIZE = self.config.get('SCROLL_SIZE', 10000)
        # Request timeout in seconds
        TIMEOUT = self.config.get('TIMEOUT', 10)
        # The max amount querying from elastic
        LIMIT = self.config.get('LIMIT', 100000)

        # Debug?
        DEBUG = self.config.get('DEBUG', False)
        
        client = ES(
            ELASTIC_HOSTS,
            basic_auth=(ELASTIC_USER, ELASTIC_PASS),
            verify_certs=VALIDATE_CERTS,
            request_timeout=TIMEOUT,
            retry_on_timeout=True
        )
        
        logging.debug("Starting initial query")

        res = client.search(
            index=self.pattern,
            size=SCROLL_SIZE,
            scroll=SCROLL_TIME,
            query=self.get_filter(),
        )
        sid = res['_scroll_id']
        
        logging.debug("Start scrolling")
        
        # Will scroll through until we reach our limit, or no more results.
        # Enables the take operator
        remainder = LIMIT
        result_count = 0
        results = None
        while result_count < LIMIT:
            logging.debug(f"Scroll {result_count} < {LIMIT} max")
            
            if len(res['hits']['hits']) == 0:
                logging.debug(f"No more results to evaluate")
                logging.debug(f"Timed out? {res['timed_out']}")
                break
            
            # Ensure that we only print the number of remaining rows
            df = pl.from_dicts(res['hits']['hits'][:remainder]).unnest('_source')

            # print(json.dumps(data, indent=2))
            if results == None:
                results = df
            else:
                pl.concat([results, df])
            result_count += len(df)
            
            remainder = LIMIT - result_count
            
            res = client.scroll(
                scroll_id=sid,
                scroll=SCROLL_TIME,
            )                

        client.clear_scroll(scroll_id=sid)

        return results