from Hql.Context import Context
from Hql.Parser import Parser
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Query import Query, QueryStatement
from Hql.Expressions import PipeExpression
import logging
from typing import Optional, Union

class Source():
    def __init__(self, ctx:Context) -> None:
        self.ctx = ctx
        self.products:list[Product] = []

    def assemble(self):
        from Hql.Compiler import InstructionSet

        isets = []
        for i in self.products:
            iset = i.assemble()
            if iset.is_empty():
                continue
            isets.append(iset)

        return InstructionSet(isets)

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

class Splits():
    def __init__(self):
        self.parent:list[HaCStatement] = []
        self.cur:list[HaCStatement] = []

    def add_level(self):
        # create new list for this
        self.parent = [x for x in self.cur]
        self.cur = []

    def add_query(self, query:Query):
        from copy import deepcopy

        if not self.parent:
            new = HaCStatement()
            new.add_query(query)
            self.cur.append(new)
            return

        for i in self.parent:
            new = deepcopy(i)
            new.add_query(query)
            self.cur.append(new)

    def add_pipes(self, pipes:PipeExpression):
        from copy import deepcopy

        if not self.parent:
            raise hqle.ConfigException('Attempting to add pipes without parent')

        for i in self.parent:
            new = deepcopy(i)
            new.add_pipes(pipes)
            self.cur.append(new)

class HaCStatement():
    def __init__(self):
        # all statements pre the root query
        self.pre = []
        self.query:Optional[PipeExpression] = None
        # all statements after
        # self.post = []

    def add_query(self, query:Query):
        for idx, i in enumerate(query.statements):
            if isinstance(i, QueryStatement):
                # This might be super wrong, trying to be as generic as possible
                # Right now trashing statements after the main statement as they're irrelevant
                self.pre += query.statements[0:idx]
                self.add_pipes(i.root)
                # self.post = query.statements[idx+1:]
                break
 
        if not self.query:
            self.pre = query.statements
        
    def add_pipes(self, pipes:PipeExpression):
        if self.query:
            if pipes.prepipe:
                raise hqle.ConfigException('Attempting to override prepipe tabular expression with HaC')
            else:
                self.query.pipes += pipes.pipes
        elif pipes.prepipe:
            self.query = pipes
        else:
            raise hqle.ConfigException('Attempting to add empty pipes to empty query with HaC')

class Product():
    def __init__(self, name:str, ctx:Context) -> None:
        self.name = name
        self.ctx = ctx
        self.conf = ctx.config.get_product(name)
        self.services = self.conf.get('services', dict())
        self.set_services = False
        self.categories = self.conf.get('categories', dict())
        self.set_categories = False
        self.splits = Splits()
        
        parser = Parser(self.conf['hql'])
        try:
            parser.assemble(target='query')
        except:
            logging.critical(f'Failed to parse Hql for product {name}')

        if not parser.assembly:
            raise hqle.ConfigException(f'Invalid Hql definition in category {name}')

        if not isinstance(parser.assembly, Query):
            raise hqle.ConfigException(f'Invalid product Hql type {type(self.product)}')
        self.product:Query = parser.assembly

        self.selection = {
            'services': [],
            'categories': []
        }

    def parse_service(self, name:str, text:str):
        parser = Parser(text)
        try:
            parser.assemble(targets=['query', 'emptyPipedExpression'])
        except:
            logging.critical(f'Failed to parse Hql in service {name}')

        if not parser.assembly:
            raise hqle.ConfigException(f'Invalid Hql definition in service {name}')

        return parser.assembly

    def parse_category(self, name:str, text:str):
        parser = Parser(text)
        try:
            parser.assemble(targets=['query', 'emptyPipedExpression'])
        except:
            logging.critical(f'Failed to parse Hql in category {name}')

        if not parser.assembly:
            raise hqle.ConfigException(f'Invalid Hql definition in category {name}')

        return parser.assembly

    def integrate(self, expr:Union[Query, PipeExpression]):
        if isinstance(expr, Query):
            self.splits.add_query(expr)
        else:
            self.splits.add_pipes(expr)

    def assemble(self):
        from Hql.Query import Query, QueryStatement
        from Hql.Compiler import InstructionSet, HqlCompiler
        self.splits.add_query(self.product)
        self.splits.add_level()

        # Assume using all services
        if not self.selection['services']:
            if self.set_services:
                return InstructionSet([])
            self.service('*')

        for i in self.selection['services']:
            self.integrate(i)
        self.splits.add_level()
        
        if not self.selection['categories']:
            if self.set_categories:
                return InstructionSet([])
            self.category('*')

        for i in self.selection['categories']:
            self.integrate(i)

        isets = []
        for i in self.splits.cur:
            # Skip over useless stuff
            if not i.query:
                continue
            
            query = Query(i.pre + [QueryStatement(i.query)])
            iset = HqlCompiler(self.ctx.config, query).root
            isets.append(iset)

        return InstructionSet(isets)

    def service(self, pat:str) -> 'Product':
        from fnmatch import fnmatch
        self.set_categories = True

        services = []
        for i in self.services:
            if not fnmatch(i, pat):
                continue

            hql = self.services[i]['hql']
            services.append(self.parse_service(i, hql))

        if not services:
            raise hqle.QueryException(f'Invalid service: {pat}')
        self.selection['services'] += services

        return self

    def category(self, pat:str) -> 'Product':
        from fnmatch import fnmatch
        self.set_categories = True

        categories = []
        for i in self.categories:
            if not fnmatch(i, pat):
                continue

            hql = self.categories[i]['hql']
            categories.append(self.parse_category(i, hql))

        if not categories:
            raise hqle.QueryException(f'Invalid category: {pat}')
        self.selection['categories'] += categories

        return self
