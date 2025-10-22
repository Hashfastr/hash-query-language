from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context, register_database
from Hql.Operators.Database import Database
from Hql.Data import Schema, Data, Table
from Hql.Compiler import SPLCompiler

from typing import TYPE_CHECKING, Union
import json
import logging

import splunklib

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Compiler import BranchDescriptor
    from Hql.Expressions import NamedReference

# Index in a database to grab data from, extremely simple.
@register_database('Splunk')
class Splunk(Database):
    def __init__(self, config:dict, name:str='Splunk'):
        Database.__init__(self, config)
        self.name = name
        conf = self.config.get('conf', dict())

        # Set to the config default to avoid DoS
        # Can be changed by the take operator for example.
        self.limit:int = conf.get('limit', 100000)
        
        # Default scroll max, cannot be higher than 10k
        # Higher values are generally better, each request has some time to it
        # 10000 is faster than 10x1000
        self.scroll_max = conf.get('scroll_max', 10000)
        self.scroll_time = conf.get('scroll_time', '1m')
        self.timeout = conf.get('timeout', 10)

        self.methods = [
            'index',
            'macro'
        ]
        
        # skips ssl verification for https
        self.verify_certs = conf.get('verify_certs', True)
        self.use_ssl = conf.get('use_ssl', True)

        if 'host' in conf:
            self.host = conf.get('host')
        else:
            raise hqle.ConfigException(f'Missing host config in Splunk config for {self.name}')

        self.username = conf.get('username', None)
        self.password = conf.get('password', None)

        if self.username == None:
            raise hqle.ConfigException(f'Unconfigured username in Splunk config {self.name}')
        if self.password == None:
            raise hqle.ConfigException(f'Unconfigured password in Splunk config {self.name}')

        self.compiler = SPLCompiler()

    def to_dict(self):
        self.query = self.compile()
        
        return {
            'id': self.id,
            'type': self.type,
            'limit': self.limit,
            'query': self.query
        }

    def compile(self) -> str:
        query, rej = self.compiler.compile(None)
        assert isinstance(query, str)
        return query

    def add_op(self, op: Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        return self.compiler.add_op(op)

    def eval(self, ctx:Context, **kwargs):
        try:
            self.query = self.compile()
            return self.make_query()
        except Exception as e:
            logging.critical(e)
            user = self.config.get('ELASTIC_USER', 'elastic')
            raise hqle.ConfigException(f'Elasticsearch authentication with user {user} failed') from None

    def make_query(self) -> Data:
        # client = ES(
        #     self.hosts,
        #     basic_auth=(self.username, self.password),
        #     verify_certs=self.verify_certs,
        #     request_timeout=self.timeout,
        #     retry_on_timeout=True,
        # )
        
        logging.debug("Starting initial query")

        logging.debug(f"{self.type} query, using the following Lucene:")
        logging.debug(self.query)
        logging.debug(f'Index pattern: {self.pattern}')
        logging.debug(f'Limit: {self.limit}')
        
        # This gets the schema
        # res = requests.get(
        #     f'{self.hosts[0]}/{self.pattern}',
        #     auth=(self.username, self.password)
        # )
        # index = json.loads(res.text)
        # print(json.dumps(index, indent=2))
        
        res = client.search(
            index=self.pattern,
            size=self.scroll_max,
            scroll=self.scroll_time,
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
                scroll=self.scroll_time,
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
