from typing import Union

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_database
from Hql.Data import Schema, Data, Table
from Hql.Operators.Operator import Operator
import Hql.Expressions as Expr
import Hql.Operators as Ops
from Hql.Types.Elasticsearch import ESTypes
from Hql.Context import Context

import requests
from elasticsearch import Elasticsearch as ES
from elasticsearch import AuthenticationException as ESAuthExcept

import json
import logging
from .. import Database

from .Features import ESFeatureSet
from .Compiler import get_expr

# Index in a database to grab data from, extremely simple.
@register_database('Elasticsearch')
class Elasticsearch(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
       
        # Default index pattern
        self.pattern = "*"

        self.expr:Union[None, Expr.Expression] = None
        self.filters = []
        
        self.feature_set = ESFeatureSet()

        # Set to the config default to avoid DoS
        # Can be changed by the take operator for example.
        self.limit:int = self.config.get('LIMIT', 100000)
        
        # Default scroll max, cannot be higher than 10k
        # Higher values are generally better, each request has some time to it
        # 10000 is faster than 10x1000
        self.scroll_max = self.config.get('SCROLL_MAX', 10000)

        self.methods = [
            'index'
        ]

        self.query = ''

    def to_dict(self):
        self.compile()
        
        return {
            'id': self.id,
            'type': self.type,
            'index': self.pattern,
            'limit': self.limit,
            'query': self.query
        }
            
    def get_variable(self, name:str):
        self.pattern = name
        return self
    
    def integrate(self, op:Operator) -> Union[None, Operator]:
        if isinstance(op, Ops.Take):
            return self.add_limit(op.expr)
        
        if isinstance(op, Ops.Where):
            ret = self.add_filter(op.expr)
            return Ops.Where(ret) if ret else None

        return op

    def add_limit(self, expr:Expr.Integer) -> None:
        from Hql.Context import Context

        if not isinstance(expr, Expr.Integer):
            raise hqle.CompilerException(f'Attempting to add limit with expression of type {type(expr)}')

        # the ctx does not matter here, this is a literal int
        ctx = self.ctx if self.ctx else Context(None)
        limit = expr.eval(ctx)

        if not isinstance(limit, int):
            raise hqle.CompilerException('Take passed non-int to Elasticsearch')

        self.limit = limit

        return None

    def add_filter(self, expr:Union[None, Expr.Expression]) -> Union[None, Expr.Expression, Ops.Operator]:
        if expr == None:
            return expr

        acc, unsupported = self.feature_set.validate_feature(expr)

            
        if isinstance(acc, Ops.Operator):
            return acc

        if self.expr == None:
            self.expr = acc
            return unsupported

        acc, rej = self.feature_set.merge_binary(self.expr, acc, 'and')
        # acc, rej = self.feature_set.merge_binary(self.expr, rej, 'or')
        
        # attempts to merge have failed
        if rej:
            self.expr = Expr.BinaryLogic(self.expr, [], 'and')
            self.feature_set.merge_binary(self.expr, rej, 'and')

        return unsupported

    def add_index(self, pattern:str):
        self.pattern = pattern
    
    def compile(self) -> str:
        if self.expr == None:
            query = ''
        else:
            query = get_expr(self.expr)(self.expr)

        if not isinstance(query, str):
            raise hqle.CompilerException('Elasticsearch compiler returned non-str')

        self.query = query
        return query

    def gen_elastic_schema(self, props:dict) -> dict:
        schema = {}
        for i in props:
            if 'properties' in props[i]:
                schema[i] = self.gen_elastic_schema(props[i]['properties'])
                continue
            
            schema[i] = ESTypes.from_name(props[i]['type'])()

        return schema

    def eval(self, ctx:Context, **kwargs):
        if kwargs.get('preview', False):
            return self.to_dict()

        try:
            return self.make_query()
        except ESAuthExcept:
            user = self.config.get('ELASTIC_USER', 'elastic')
            raise hqle.ConfigException(f'Elasticsearch authentication with user {user} failed') from None

    def make_query(self) -> Data:
        # Host, or hosts, to use for the query.
        # Should be in array format
        HOSTS = self.config.get('ELASTIC_HOSTS', ['http://localhost:9200'])
        # Elastic user to use
        USER = self.config.get('ELASTIC_USER', 'elastic')
        # Elastic user password to use
        PASS = self.config.get('ELASTIC_PASS', 'changeme')
        # SSL Validation
        VALIDATE_CERTS = self.config.get('VALIDATE_CERTS', 'true')
        # How long should the scroll session be kept alive?
        SCROLL_TIME = self.config.get('SCROLL_TIME', '1m')
        # Query results limit per scroll
        # If the total limit is less than this number, it is set to the query limit.
        SCROLL_MAX = self.scroll_max if self.limit >= self.scroll_max else self.limit
        # Request timeout in seconds
        TIMEOUT = self.config.get('TIMEOUT', 10)
        
        client = ES(
            HOSTS,
            basic_auth=(USER, PASS),
            verify_certs=VALIDATE_CERTS,
            request_timeout=TIMEOUT,
            retry_on_timeout=True,
        )
        
        logging.debug("Starting initial query")

        logging.debug(f"{self.type} query, using the following Lucene:")
        logging.debug(self.query)
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
            q=self.query
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

            # schema = self.gen_elastic_schema(index[i]['mappings']['properties'])
            # schema = Schema(schema=schema).convert_schema(target='hql')
            # schema = Schema.merge([table.schema.schema, schema])

            # table.set_schema(schema)
            tables.append(table)

        return Data(tables=tables)
