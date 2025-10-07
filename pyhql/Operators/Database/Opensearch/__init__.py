from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_database
from Hql.Operators.Database import Database

from Hql.Compiler import LuceneCompiler

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Compiler import BranchDescriptor
    from Hql.Data import Data
    from Hql.Context import Context

# Index in a database to grab data from, extremely simple.
@register_database('Opensearch')
class Opensearch(Database):
    def __init__(self, config:dict, name:str='Opensearch'):
        Database.__init__(self, config, name=name)
       
        # Default index pattern
        self.pattern = "*"

        conf = self.config.get('conf', dict())


        self.hosts:list[str] = conf.get('hosts', ['localhost:9200'])

        self.headers = dict()
        if 'api_key' in conf:
            self.headers['X-API-Key'] = conf['api_key']
        
        self.auth = self.get_auth(conf)

        self.methods = [
            'index',
            'macro'
        ]
        
        # skips ssl verification for https
        self.verify_certs = conf.get('verify_certs', True)
        self.use_ssl = conf.get('use_ssl', True)

        self.query = ''
        self.compiler = LuceneCompiler()

    def get_auth(self, conf:dict):
        from opensearchpy.helpers import AWSV4SignerAsyncAuth
        import boto3

        # Get amazon key or whatever
        auth_type = conf.get('auth_type', 'userpass')

        if auth_type == 'aws':
            region = conf.get('aws_region', 'us-west-2')
            creds = boto3.Session().get_credentials()
            return AWSV4SignerAsyncAuth(creds, region)

        elif auth_type == 'userpass':
            user = conf.get('username', None)
            if user == None:
                raise hqle.ConfigException(f'Opensearch missing username in {self.name} configuration')
            
            passwd = conf.get('password', None)
            if passwd == None:
                raise hqle.ConfigException(f'Opensearch missing password in {self.name} configuration')

            return (user, passwd)

        else:
            return None

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

    def add_index(self, index: str):
        self.pattern = index

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'index': self.pattern,
            'limit': self.limit,
            'query': self.compile()
        }

    def compile(self) -> str:
        query, rej = self.compiler.compile(None)
        assert isinstance(query, str)
        return query
    
    # I'll probably change how this works in the future
    def get_variable(self, name:str):
        self.pattern = name
        return self

    async def run_query(self) -> list[dict]:
        from opensearchpy import AsyncOpenSearch

        conf = self.config.get('conf', dict())
        client = AsyncOpenSearch(
            hosts=self.hosts,
            http_auth=self.auth,
            use_ssl=self.use_ssl,
            verify_certs=self.verify_certs,
            headers=self.headers
        )

        try:
            is_available = await client.ping()

            res = await client.search(
                index=self.pattern,
                body={
                    'query': {
                        'query_string': {
                            'query': self.query
                        }
                    }
                }
            )

            print(type(res))
            print(len(res))

        finally:
            await client.close()

        return []
    

    def eval(self, ctx: 'Context', **kwargs) -> 'Data':
        from Hql.Data import Data
        import asyncio
        self.query = self.compile()
        
        res = asyncio.run(self.run_query())
        print(len(res))
        print(res[0])

        return Data()
