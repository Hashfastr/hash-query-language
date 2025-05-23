import HqlCompiler.Expression as Expression
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
from HqlCompiler.Context import *
from HqlCompiler.Data import Schema
from HqlCompiler.Context import Context
import HqlCompiler.Types as t

import requests
from elasticsearch import Elasticsearch as ES
import polars as pl

import time
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
            # 'Count'
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

    def gen_elastic_schema(self, props:dict):
        schema = {}
        for i in props:
            if 'properties' in props[i]:
                schema[i] = self.gen_elastic_schema(props[i]['properties'])
                continue
            
            ptype = props[i]['type']
            if ptype in  ('scaled_float'):
                schema[i] = t.decimal
            elif ptype in ('half_float', 'float'):
                schema[i] = t.float
            elif ptype in ('double'):
                schema[i] = t.double
            elif ptype in ('byte'):
                schema[i] = t.byte
            elif ptype in ('short'):
                schema[i] = t.short
            elif ptype in ('integer'):
                schema[i] = t.int
            elif ptype in ('long'):
                schema[i] = t.long
            elif ptype in ('unsigned_long'):
                schema[i] = t.ulong
            elif ptype in ('ip'):
                schema[i] = t.ip
            elif ptype in ('date', 'date_nanos'):
                schema[i] = t.datetime
            elif ptype in ('date_range', 'integer_range', 'float_range', 'long_range', 'double_range', 'ip_range'):
                rtype = self.gen_elastic_schema({'rtype': {'type': ptype.replace('_range', '')}})['rtype']
                schema[i] = t.range(rtype, rtype)
            elif ptype in ('keyword', 'constant_keyword', 'wildcard', 'binary', 'text', 'match_only_text'):
                schema[i] = t.string
            elif ptype in ('boolean'):
                schema[i] = t.bool
            elif ptype in ('flattened', 'object'):
                schema[i] = t.object([])
            elif ptype in ('nested'):
                schema[i] = t.string
            elif ptype in ('point', 'geo_point'):
                # ptype = t.float
                # schema[i] = t.multivalue(ptype)
                schema[i] = {
                    'lon': t.float,
                    'lat': t.float
                }
            # elif ptype in ('object', 'flattened', 'nested'):
            #     schema[i] = pl.
            # elif ptype in ('geo_point'):
            #     schema[i] = pl.String
            # elif ptype in ('')
            else:
                print(f'{i} {ptype}')

        return schema

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
        results = []
        while len(results) < self.limit:            
            if len(res['hits']['hits']) == 0:
                logging.debug(f"No more results to evaluate")
                logging.debug(f"Timed out? {res['timed_out']}")
                break
            
            # Ensure that we only print the number of remaining rows
            results += [x['_source'] for x in res['hits']['hits'][:remainder]]
            
            remainder = self.limit - len(results)
            
            if len(results) >= self.limit:
                logging.debug('Quota reached')
                break
            
            logging.debug(f"Scroll {len(results)} < {self.limit} max")
            
            res = client.scroll(
                scroll_id=sid,
                scroll=SCROLL_TIME,
            )

        client.clear_scroll(scroll_id=sid)

        iname = [x for x in index][0]
        props = index[iname]['mappings']['properties']

        start = time.perf_counter()
        jschema = Schema(results)
        end = time.perf_counter()
        logging.debug(f"Loading intermediate schema took {end - start}")

        start = time.perf_counter() 
        results = jschema.adjust_mv(results)
        end = time.perf_counter()
        logging.debug(f"Making multivalue adjustments took {end - start}")
        
        start = time.perf_counter()
        df = pl.from_dicts(results, schema=jschema.to_pl_schema())
        end = time.perf_counter()
        logging.debug(f"Loading raw data into intermediate dataframe took {end - start}")
        
        start = time.perf_counter()
        eschema = Schema(schema=self.gen_elastic_schema(props))
        end = time.perf_counter()
        logging.debug(f"Creating elastic schema took {end - start}")
        
        start = time.perf_counter()
        df = eschema.cast_to_schema(df, mv_fields=jschema.mv_fields)
        end = time.perf_counter()
        logging.debug(f"Casting intermediate dataframe to final took {end - start}")

        return df