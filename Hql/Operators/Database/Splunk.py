from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context, register_database
from Hql.Expressions.Logic import Equality
from Hql.Operators.Database import Database
from Hql.Data import Schema, Data, Table
from Hql.Compiler import SPLCompiler

from typing import TYPE_CHECKING, Union
import json
import logging

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

        self.indexes = []

    def add_index(self, index:str):
        self.indexes.append(index)

    def to_dict(self):
        self.query = self.compile()
        
        return {
            'id': self.id,
            'type': self.type,
            'limit': self.limit,
            'query': self.query
        }

    def compile(self) -> str:
        from Hql.Operators import Take, Where
        from Hql.Expressions import Integer, BinaryLogic, StringLiteral, NamedReference, PipeExpression
        from Hql.Compiler import HqlCompiler
        from Hql.Config import Config
        import copy
            
        compiler = copy.deepcopy(self.compiler)

        # Add preamble and recompile
        if self.preamble:
            new_ops = self.preamble.pipes
            
            if compiler.top_level_expr:
                op = Where(compiler.top_level_expr)
                new_ops += [op]

            new_ops += compiler.ops

            vestigial = HqlCompiler(Config())
            desc = vestigial.optimize(new_ops)

            ops = []
            for i in desc:
                ops.append(i.get_op())

            if compiler.top_level_expr:
                compiler.top_level_expr = None
                compiler.add_top_level(ops[0])
                compiler.ops = ops[1:]
            else:
                compiler.ops = ops

        if self.indexes:
            indexes = []
            for i in self.indexes:
                expr = Equality(NamedReference('index'), '=~', [StringLiteral(i, verbatim=True)])
                indexes.append(expr)
            expr = BinaryLogic(indexes[0], indexes[1:], 'or')
            compiler.add_top_level(Where(expr))

        if self.limit > 0:
            compiler.add_op(Take(Integer(self.limit), []))

        query, _ = compiler.compile(None)
        assert isinstance(query, str)
        return query

    def add_op(self, op: Union['Operator', 'BranchDescriptor']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        return self.compiler.add_op(op)

    def connect(self):
        import splunklib.client as client

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
        return service

    def eval(self, ctx:Context, **kwargs):
        self.query = self.compile()
        return self.make_query()

    def make_query(self, **kwargs) -> Data:
        import splunklib.results as results
        from Hql.Data import Table

        conn = self.connect()
        job = conn.jobs.create(self.query, output_mode='json', rf='*', **kwargs)
        res = job.results(output_mode='json')
        reader = results.JSONResultsReader(res)

        data = [x for x in reader if isinstance(x, dict)]
        table = Table(init_data=data, name=self.name)

        return Data(tables=[table])
