from typing import Union, TYPE_CHECKING
from Hql.Exceptions import HqlExceptions as hqle
import logging

if TYPE_CHECKING:
    from Hql.Expressions import Expression, NamedReference, Path
    from Hql.Operators import Operator, Database
    from Hql.Query import Query, Statement

'''
Wraps an Expression or Operator with some tagged metadata
Helpful for finding out if we can compile something
'''
class BranchDescriptor():
    def __init__(self):
        from Hql.Data import Schema

        # contains a timeseries element
        self.attrs:dict = dict()

        self.expr:Union[None, 'Expression'] = None
        self.op:Union[None, 'Operator'] = None
        self.statement:Union[None, 'Statement'] = None
        self.query:Union[None, 'Query'] = None
        self.db:Union[None, 'Database'] = None
        self.str:str = ''
        self.join_attrs:dict = dict()
        self.list_attrs:list[str] = [
            'types',
            'functions'
        ]
        # Incomplete solution, just name checking
        self.provides:list = []
        self.references:list = []
        self.removes:list = []
        self.full_schema = False
        self.mapping:dict[Union['NamedReference', 'Path'], Union['NamedReference', 'Path']] = dict()

    def set_attr(self, name:str, value):
        self.attrs[name] = value

    def add_mapping(self, dest:Union['NamedReference', 'Path'], src:Union['NamedReference', 'Path']):
        self.mapping[dest] = src

    def get_attr(self, name:str):
        return self.attrs.get(name, None)

    def merge_attrs(self, attrs:dict):
        for i in attrs:
            cur = self.attrs.get(i, None)
            val = attrs[i]

            if i in self.list_attrs:
                if not isinstance(val, list):
                    val = [val]

                if cur:
                    cur += val
                else:
                    self.attrs[i] = val

            elif isinstance(cur, type(None)):
                self.attrs[i] = attrs[i]

            elif isinstance(cur, type(bool)) and isinstance(val, type(bool)):
                if not cur:
                    self.attrs[i] = attrs[i]

            # Default catchall for now
            else:
                self.attrs[i] = attrs[i]

    def merge(self, desc:'BranchDescriptor'):
        self.merge_attrs(desc.attrs)
        self.provides += desc.provides
        self.references += desc.references
        self.removes += desc.removes
        for i in desc.mapping:
            self.add_mapping(i, desc.mapping[i])

    def compatible(self, superset:dict) -> bool:
        for i in self.attrs:
            # Check if there's a feature this branch has that the superset doesn't
            if self.attrs[i] and not superset.get(i, False):
                logging.debug(f'{i}: {self.attrs[i]} breaks compatiblity')
                return False
        return True

    def get_expr(self) -> 'Expression':
        if isinstance(self.expr, type(None)):
            raise hqle.CompilerException('Attempting to access NoneType BranchDescriptor Expr')
        return self.expr

    def get_op(self) -> 'Operator':
        if isinstance(self.op, type(None)):
            raise hqle.CompilerException('Attempting to access NoneType BranchDescriptor Op')
        return self.op

    def get_statement(self) -> 'Statement':
        if isinstance(self.statement, type(None)):
            raise hqle.CompilerException('Attempting to access NoneType BranchDescriptor Statement')
        return self.statement
