from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context, register_database
from Hql.Operators import Database
from Hql.Data import Schema, Data, Table
from Hql.Types.Elasticsearch import ESTypes
from Hql.Compiler import LuceneCompiler

from typing import TYPE_CHECKING, Union
import json
import logging

import requests
from elasticsearch import Elasticsearch as ES
from elasticsearch import AuthenticationException as ESAuthExcept

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Compiler import BranchDescriptor

# Index in a database to grab data from, extremely simple.
@register_database('Elasticsearch')
class Elasticsearch(Database):
    def __init__(self, config:dict):
        Database.__init__(self, config)
       
        # Default index pattern
        self.pattern = "*"

        conf = self.config.get('conf', dict())

        # Set to the config default to avoid DoS
        # Can be changed by the take operator for example.
        self.limit:int = conf.get('limit', 100000)
        
        # Default scroll max, cannot be higher than 10k
        # Higher values are generally better, each request has some time to it
        # 10000 is faster than 10x1000
        self.scroll_max = conf.get('scroll_max', 10000)

        self.methods = [
            'index',
            'macro'
        ]
        
        # skips ssl verification for https
        self.verify_certs = conf.get('verify_certs', True)
        self.use_ssl = conf.get('use_ssl', True)

        self.compiler = LuceneCompiler()

    def to_dict(self):
        self.compile()
        
        return {
            'id': self.id,
            'type': self.type,
            'index': self.pattern,
            'limit': self.limit,
            'query': self.query
        }

    def compile(self) -> str:
        query, rej = self.compiler.compile(None)
        assert isinstance(query, str)
        return query
            
    def get_variable(self, name:str):
        self.pattern = name
        return self

    def add_index(self, index:str):
        self.pattern = index

    def add_op(self, op: Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        from Hql.Compiler import BranchDescriptor
        from Hql.Operators import Take, Operator

        if isinstance(op, BranchDescriptor):
            op = op.get_op()

        if isinstance(op, Take):
            if op.tables:
                return None, op

            limit = op.expr.eval(self.ctx, as_str=True)
            assert isinstance(limit, int)
            self.limit = limit if limit < self.limit else self.limit

            return op, None

        acc, rej = self.compiler.compile(op)
        assert isinstance(acc, (Operator, type(None)))
        assert isinstance(rej, (Operator, type(None)))
        return acc, rej

    def gen_elastic_schema(self, props:dict) -> dict:
        schema = {}
        for i in props:
            if 'properties' in props[i]:
                schema[i] = self.gen_elastic_schema(props[i]['properties'])
                continue
            
            schema[i] = ESTypes.from_name(props[i]['type'])()

        return schema

    def eval(self, ctx:Context, **kwargs):
        try:
            self.query = self.compile()
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
