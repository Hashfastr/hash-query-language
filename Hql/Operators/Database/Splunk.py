from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context, register_database
from Hql.Operators.Database import Database
from Hql.Data import Schema, Data, Table
from Hql.Compiler import SPLCompiler

from typing import TYPE_CHECKING, Union
import json
import logging

import splunklib.client as client
import splunklib.results as results

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
        self.port = int(conf.get('port', 8089))

        self.username = conf.get('username', None)
        self.password = conf.get('password', None)
        self.token = conf.get('token', None)

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
        from Hql.Operators import Take
        from Hql.Expressions import Integer
        import copy

        if self.limit > 0:
            compiler = copy.deepcopy(self.compiler)
            compiler.add_op(Take(Integer(self.limit), []))
        else:
            compiler = self.compiler

        query, _ = compiler.compile(None)
        assert isinstance(query, str)
        return query

    def add_op(self, op: Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        return self.compiler.add_op(op)

    def connect(self):
        auth_params = {
            'host': self.host,
            'port': self.port
        }

        if self.token:
            auth_params['token'] = self.token
        else:
            if self.username == None:
                raise hqle.ConfigException(f'Unconfigured username in Splunk config {self.name}')
            if self.password == None:
                raise hqle.ConfigException(f'Unconfigured password in Splunk config {self.name}')

            auth_params['username'] = self.username
            auth_params['password'] = self.password

        service = client.connect(**auth_params)
        print(type(service))
        return service

    def eval(self, ctx:Context, **kwargs):
        try:
            self.query = self.compile()
            return self.make_query()
        except Exception as e:
            logging.critical(e)
            user = self.config.get('ELASTIC_USER', 'elastic')
            raise hqle.ConfigException(f'Elasticsearch authentication with user {user} failed') from None

    def make_query(self, **kwargs) -> Data:
        from Hql.Data import Table

        conn = self.connect()
        job = conn.jobs.create(self.query, output_mode='json', **kwargs)
        reader = results.JSONResultsReader(job)

        data = [x for x in reader if isinstance(x, dict)]
        print(json.dumps(data[0], indent=2))
        table = Table(init_data=data, name=self.name)

        return Data(tables=[table])
