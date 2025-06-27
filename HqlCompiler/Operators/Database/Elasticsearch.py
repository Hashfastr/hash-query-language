import HqlCompiler.Expression as Expr
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator
from HqlCompiler.Context import *
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Types.Elasticsearch import ESTypes

import requests
from elasticsearch import Elasticsearch as ES

import json
import logging
from .__proto__ import Database

# Index in a database to grab data from, extremely simple.
@register_database('Elasticsearch')
class Elasticsearch(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
        
        self.pattern = "*"

        # The database filter always starts as an and
        self.filter_expr = Expr.BinaryLogic(None, [], 'and')
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
            
    def get_variable(self, name: str):
        self.pattern = name
        return self
    
    def eval_ops(self):
        for op in self.ops:
            if op.type == 'Where':
                self.add_filter(op.expr)
            
            # should only have on expression
            if op.type == 'Take':
                self.limit = op.expr.eval(self.ctx)
                if not isinstance(self.limit, int):
                    raise QueryException(f'Take operator passed non-int type {self.n_rows}')

    def add_index(self, pattern:str):
        self.pattern = pattern
    
    # When executed it assumes another where op, implying 'and' with other filters
    def add_filter(self, expr:Expr):
        if not self.filter_expr.lh:
            logging.debug(f'Create initial filter for {self.dbtype}')
            self.filter_expr.lh = expr
            return
        
        logging.debug(f'Joining where filter into {self.dbtype}')
        if self.filter_expr.type == 'BinaryLogic' and self.filter_expr.bitype == 'and':
            self.filter_expr.rh.append(expr)
        else:
            self.filter_expr = Expr.BinaryLogic(self.filter_expr, expr, 'and')

    def gen_filter(self, expr:Expr):
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
            
            schema[i] = ESTypes.from_name(props[i]['type'])()

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
        
        self.eval_ops()
        
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
            results += res['hits']['hits'][:remainder]
            
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

        result_sets = dict()
        for i in results:
            if i['_index'] not in result_sets:
                result_sets[i['_index']] = []
            result_sets[i['_index']].append(i['_source'])

        tables = []
        for i in result_sets:
            table = Table(init_data=result_sets[i], name=i)
            tables.append(table)

        data = Data(tables=tables)

        for table in data:
            eschema = Schema(schema=self.gen_elastic_schema(index[i]['mappings']['properties']))
            table.change_schema(eschema)

        return data