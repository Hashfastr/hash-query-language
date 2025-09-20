from Hql.Context import Context
from Hql.Parser import Parser
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Query import Query
import logging

class Source():
    def __init__(self, ctx:Context) -> None:
        self.ctx = ctx
        self.products:list[Product] = []


    def assemble(self):
        ...

    def product(self, pattern:str):
        from fnmatch import fnmatch
        for i in self.ctx.config.conf['products']:
            if not fnmatch(i, pattern):
                continue
            self.products.append(Product(i, self.ctx))
        return self

    def service(self, pattern:str):
        for i in self.products:
            i.service(pattern)
        return self

    def category(self, pattern:str):
        for i in self.products:
            i.category(pattern)
        return self

class Product():
    def __init__(self, name:str, ctx:Context) -> None:
        self.name = name
        self.ctx = ctx
        self.conf = ctx.config.get_product(name)
        self.services = self.conf.get('services', dict())
        self.categories = self.conf.get('categories', dict())
        
        self.product = self.parse(f'product for {name}', self.conf['Hql'])
        if not isinstance(self.product, Query):
            raise hqle.ConfigException(f'Invalid product Hql type {type(self.product)}')

        self.selection = {
            'services': [],
            'categories': []
        }

    def parse(self, msg:str, text:str):
        parser = Parser(text)
        try:
            parser.assemble(targets=['queryStatement', 'emptyPipedExpression'])
        except:
            logging.critical(f'Failed to parse Hql in {msg}')

        if not parser.assembly:
            raise hqle.ConfigException(f'Invalid Hql definition in {msg}')

        return parser.assembly

    def assemble(self):
        product = self.product

        if not self.selection['services']:
            self.service('*')

        # for i in self.selection['services']

    def service(self, pat:str) -> 'Product':
        from fnmatch import fnmatch

        services = []
        for i in self.services:
            if not fnmatch(i, pat):
                continue

            hql = self.services[i]['hql']
            services.append(self.parse(f'service {i}', hql))

        if not services:
            raise hqle.QueryException(f'Invalid service: {pat}')
        self.services += services

        return self

    def category(self, pat:str) -> 'Product':
        from fnmatch import fnmatch

        categories = []
        for i in self.categories:
            if not fnmatch(i, pat):
                continue

            hql = self.categories[i]['hql']
            categories.append(self.parse(f'category {i}', hql))

        if not categories:
            raise hqle.QueryException(f'Invalid category: {pat}')
        self.categories += categories

        return self
