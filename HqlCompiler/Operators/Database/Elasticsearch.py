import HqlCompiler.Expression as Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
from HqlCompiler.Registry import *
from HqlCompiler.Functions import Function

from elasticsearch import Elasticsearch as ES
import polars as pl

import json
import logging
from .__proto__ import Database

# Index in a database to grab data from, extremely simple.
@register_database('Elasticsearch')
class Elasticsearch(Database):
    def __init__(self, config:dict):
        super().__init__()
        
        self.pattern = "*"

        self.config = config

        # The database filter always starts as an and
        self.filter_expr = Expression.BinaryLogic(None, [], 'and')
        self.filters = []
        
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

    def exec_func_chain(self, chain:list[Function]):
        return self.exec_func(chain[0])

    def exec_func(self, func:Function):
        if func.name in ("index"):
            self.pattern = func.args[0].value
            return self
        else:
            raise CompilerException(f"Unimplemented subfunction to DB type {self.dbtype}")
    
    def can_integrate(self, type:str):
        return type in self.compatible
    
    def add_op(self, op:Operator):
        if op.type == 'Where':
            self.add_filter(op.expr)
        
        # should only have on expression
        if op.type == 'Take':
            self.add_limit(op.expr.value)

    def execute(self, data:pl.DataFrame):
        return self.make_query()
    
    def add_limit(self, limit:int):
        self.limit = limit
    
    # When executed it assumes another where op, implying 'and' with other filters
    def add_filter(self, expr:Expression):
        if not self.filter_expr.lh:
            logging.debug(f'Create initial filter for {self.dbtype}')
            self.filter_expr.lh = expr
            return
        
        logging.debug(f'Joining where filter into {self.dbtype}')
        if self.filter_expr.type == 'BinaryLogic' and self.filter_expr.bitype == 'and':
            self.filter_expr.rh.append(expr)
        else:
            self.filter_expr = Expression.BinaryLogic(self.filter_expr, expr, 'and')

    def gen_filter(self, expr:Expression):
        filter = None

        if expr.type == "BinaryLogic":
            op = 'must' if expr.bitype == 'and' else 'should'
            
            # base empty filter case
            if not expr.lh:
                return {
                    'match_all': {}
                }
            
            return {
                'bool': {
                    op: [
                        self.gen_filter(expr.lh)
                    ] + [self.gen_filter(x) for x in expr.rh]
                }
            }
        
        if expr.type == 'Equality':
            # Need to check for these because of elastic limitations
            # Might implement these at a high level at sometime
            # Or translate to equvalent logic
            # (field1=2 and field2=3) == (field3=4 or field4=5)
            # (field1=2 and field2=3) and (field3=4 or field4=5)
            if not hasattr(expr.lh, 'get_name'):
                raise CompilerException('Equality left-hand is not a named reference')
                
            if not hasattr(expr.rh, 'get_value'):
                raise CompilerException('Equality right-hand is not a basic value')
            
            if expr.eqtype == '==':
                return {
                    'term': {
                        expr.lh.get_name() : expr.rh.get_value()
                    }
                }
                
            if expr.eqtype in ('<>', '!='):
                return {
                    'bool': {
                        'must_not': {
                            'term': {expr.lh.get_name() : expr.rh.get_value()}
                        }
                    }
                }
        
        if expr.type == "BetweenEquality":
            # Don't think this can ever be something non-basic
            if not hasattr(expr.lh, 'get_name'):
                raise CompilerException('BetweenEquality left-hand is not a named reference')
            
            if not hasattr(expr.start, 'get_value'):
                raise CompilerException('BetweenEquality right-hand start is not a basic value')
            
            if not hasattr(expr.end, 'get_value'):
                raise CompilerException('BetweenEquality right-hand end is not a basic value')
            
            return {
                'range': {
                    expr.lh.get_name() : {
                        'gte': expr.start.get_value(),
                        'lte': expr.end.get_value()
                    }
                }
            }

        if not filter:
            raise CompilerException(f"Invalid filter type {expr['type']}")
            
        return filter

        if expr['type'] == '<':
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
        elif expr['type'] == 'ListEquality':
            kvs = []
            for i in expr['rh']:
                kv = {
                    'match': {
                        expr['lh']['name']: i['value']
                    }
                }
                kvs.append(kv)
            
            filter = {
                'bool': {
                    'should': kvs
                }
            }
        
        # Negative filters
        if expr['type'] == '!=':
            filter = {
                'term': {
                    expr['lh']['name'] : expr['rh']['value']
                }
            }
            
        if not filter:
            raise CompilerException(f"Invalid filter type {expr['type']}")
            
        return filter
    
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
            'query': self.gen_filter(self.filter_expr)
        }
        
        logging.debug(f"{self.dbtype} query, using the following DSL:")
        logging.debug(json.dumps(body))
        
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
            
            if result_count >= self.limit:
                logging.debug('Quota reached')
                break
            
            logging.debug(f"Scroll {result_count} < {self.limit} max")
            
            res = client.scroll(
                scroll_id=sid,
                scroll=SCROLL_TIME,
            )                

        client.clear_scroll(scroll_id=sid)

        return results