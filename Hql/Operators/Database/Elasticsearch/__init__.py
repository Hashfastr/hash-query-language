from typing import Union
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_database
from Hql.Data import Schema, Data, Table
from Hql.Operators.Operator import Operator
import Hql.Expressions as Expr
import Hql.Operators as Ops
from Hql.Types.Elasticsearch import ESTypes
from .Features import ESFeatureSet

import requests
from elasticsearch import Elasticsearch as ES

import json
import logging
from .. import Database

# Index in a database to grab data from, extremely simple.
@register_database('Elasticsearch')
class Elasticsearch(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
       
        # Default index pattern
        self.pattern = "*"

        self.expr = None
        self.filters = []
        
        self.feature_set = ESFeatureSet()

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
    
    def integrate(self, op:Operator) -> Union[None, Operator]:
        if isinstance(op, Ops.Take):
            return self.add_limit(op)
        
        if isinstance(op, Ops.Where):
            ret = self.add_filter(op.expr)
            return Ops.Where(ret) if ret else None

    def add_limit(self, op:Operator) -> Union[None, Operator]:
        # Safely handle the wtf case
        if op.expr == None:
            return op

        self.limit = op.expr.eval(self.ctx)
        return None

    def add_filter(self, expr:Union[None, Expr.Expression]) -> Union[None, Expr.Expression]:
        if expr == None:
            return expr

        acc, rej = self.feature_set.validate_feature(expr)

        if self.expr == None:
            self.expr = acc
            return rej

        acc = self.feature_set.merge_binary(acc, 'and')
        acc = self.feature_set.merge_binary(acc, 'or')

        # attempts to merge have failed
        if acc:
            self.expr = Expr.BinaryLogic(self.expr, [], 'and')
            self.feature_set.merge_binary(acc, 'and')

        return rej

    def add_index(self, pattern:str):
        self.pattern = pattern
    
    def gen_filter(self, expr:Union[None, Expr.Expression]=None):
        expr = expr if expr else self.expr
        if not self.expr:
            return ''

        

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

        i = 0

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
