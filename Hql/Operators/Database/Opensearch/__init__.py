from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_database
from Hql.Operators.Database import Database

from opensearchpy import AsyncOpenSearch
from Hql.Compiler import LuceneCompiler

from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    from Hql.Operators import Operator
    from Hql.Compiler import BranchDescriptor

# Index in a database to grab data from, extremely simple.
@register_database('Opensearch')
class Opensearch(Database):
    def __init__(self, config:dict, name:str='Opensearch'):
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
        self.insecure = self.config.get('insecure', False)

        self.compiler = LuceneCompiler()

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
    

