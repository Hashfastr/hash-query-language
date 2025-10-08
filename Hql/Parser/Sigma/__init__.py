from typing import TYPE_CHECKING, Union

from .Selection import Selection
from .Condition import Condition
from Hql.Exceptions import HqlExceptions as hqle

import logging, json

if TYPE_CHECKING:
    from Hql.Expressions import DotCompositeFunction
    from Hql.Hac import Hac

class SigmaParser():
    def __init__(self, txt:str):
        from Hql.Query import Query
        import yaml

        self.loaded = yaml.load(txt, yaml.SafeLoader)
        if isinstance(self.loaded, str):
            raise hqle.QueryException('Invalid sigma supplied to parser')

        self.assembly:Union[None, Query] = None

        if self.loaded.get('status', '') == 'deprecated':
            raise hqle.QueryException(f'Sigma rule is deprecated')

    def gen_hac(self):
        from copy import deepcopy
        from Hql.Hac import Hac
        doc:dict = deepcopy(self.loaded)

        try:
            for i in ['detection', 'logsource']:
                doc.pop(i)
        except KeyError as e:
            logging.critical(f"Missing critical field")
            logging.critical(e)
            raise hqle.QueryException(f'Invalid sigma supplied to parser')

        return Hac(doc, 'sigma')

    def assemble(self):
        from Hql.Expressions import PipeExpression
        from Hql.Query import Query, QueryStatement

        hac = self.gen_hac()
        dac = self.loaded['detection']
        src = self.loaded['logsource']

        prepipe = self.gen_src(src)
        pipe = self.parse_dac(dac)
        expr = PipeExpression([pipe], prepipe=prepipe)

        statement = QueryStatement(expr)
        self.assembly = Query([statement])

    def gen_src(self, src:dict) -> 'DotCompositeFunction':
        from Hql.Expressions import DotCompositeFunction
        from Hql.Expressions import FuncExpr, StringLiteral

        '''
        Category can contain a set of product/service combos
        Products contain a set of services, can be used to narrow down categories
        Services filter down logs from a product
        '''
        order = ['product', 'service', 'category']
        funcs = []

        for i in order:
            if i in src:
                funcs.append(FuncExpr(i, [StringLiteral(src[i])]))

        if len(funcs) == 0:
            raise hqle.QueryException(f'Sigma provided no log sources!')

        return DotCompositeFunction(funcs)

    def parse_dac(self, dac:dict):
        from Hql.Operators import Where

        selections = []
        for i in dac:
            if i == 'condition':
                continue

            selections.append(Selection(dac[i], name=i))

        condition = Condition(dac['condition'], selections)
        expr = Where(condition.assemble())

        return expr

    def gen_hql(self, src:dict, dac:dict):
        selections = []
        for i in dac:
            ...
