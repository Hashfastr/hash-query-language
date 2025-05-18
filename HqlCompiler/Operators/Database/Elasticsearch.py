import HqlCompiler.Expression as Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
from HqlCompiler.Context import *
from HqlCompiler.Functions import Function
from HqlCompiler.PolarsTools import PolarsTools
from HqlCompiler.Context import Context

import requests
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
            'Take',
            'Count'
        ]
        
        # Set to the config default to avoid DoS
        # Can be changed by the take operator for example.
        self.limit = self.config.get('LIMIT', 100000)
        
        # Default scroll max, cannot be higher than 10k
        # Higher values are generally better, each request has some time to it
        # 10000 is faster than 10x1000
        self.scroll_max = self.config.get('SCROLL_MAX', 10000)

        self.methods = [
            'index'
        ]
    
        self.ctx = None
        
    def get_variable(self, name: str):
        self.pattern = name
        
        return self
    
    def can_integrate(self, type:str):
        return type in self.compatible
    
    def add_op(self, op:Operator):
        if op.type == 'Where':
            self.add_filter(op.expr)
        
        # should only have on expression
        if op.type == 'Take':
            self.add_limit(op.expr.value)

    def eval(self, ctx:Context, **kwargs):
        self.ctx = ctx
        return self.make_query()
    
    def add_limit(self, limit:int):
        self.limit = limit

    def add_index(self, pattern:str):
        self.pattern = pattern
    
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
            op = ' AND ' if expr.bitype == 'and' else ' OR '
            
            # base empty filter case
            if not expr.lh:
                return ""
            
            terms = [
                self.gen_filter(expr.lh)
            ] + [self.gen_filter(x) for x in expr.rh]
            
            return op.join(terms)
        
        if expr.type == 'Equality':
            lh = expr.lh.eval(self.ctx, as_str=True)    
            rh = expr.rh.eval(self.ctx, as_str=True)
            
            if expr.eqtype == '==':
                return f"{lh}:\"{rh}\""
                
            if expr.eqtype in ('<>', '!='):
                return f"-{lh}:\"{rh}\""
        
        if expr.type == "BetweenEquality":
            lh = expr.lh.eval(self.ctx, as_str=True)
            start = expr.start.eval(self.ctx, as_str=True)
            end = expr.end.eval(self.ctx, as_str=True)
            
            return f"{lh}:[{start} TO {end}]"

        raise CompilerException(f"Invalid filter type {expr.type}")
    
    def make_query(self) -> dict:
        # Host, or hosts, to use for the query.
        # Should be in array format
        HOSTS = self.config.get('HOSTS', ['http://localhost:9200'])
        # Elastic user to use
        USER = self.config.get('USER', 'elastic')
        # Elastic user password to use
        PASS = self.config.get('PASS', 'changeme')
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
            HOSTS,
            basic_auth=(USER, PASS),
            verify_certs=VALIDATE_CERTS,
            request_timeout=TIMEOUT,
            retry_on_timeout=True,
        )
        
        logging.debug("Starting initial query")

        q = self.gen_filter(self.filter_expr)
        
        logging.debug(f"{self.dbtype} query, using the following Lucene:")
        logging.debug(q)
        logging.debug(f'Index pattern: {self.pattern}')
        logging.debug(f'Limit: {self.limit}')
        
        res = requests.get(
            f'{HOSTS[0]}/{self.pattern}',
            auth=(USER, PASS)
        )
        index = json.loads(res.text)
        
        res = client.search(
            index=self.pattern,
            size=SCROLL_MAX,
            scroll=SCROLL_TIME,
            q=q
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
            
            if results.is_empty():
                results = df
            else:
                results = pl.concat([results, df], how='diagonal_relaxed')
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