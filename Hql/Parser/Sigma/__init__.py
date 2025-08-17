from typing import TYPE_CHECKING, Union
from .Selection import Selection
from .Condition import Condition

if TYPE_CHECKING:
    from Hql.Expressions import DotCompositeFunction
    from Hql.Hac import Hac

class SigmaParser():
    def __init__(self, txt):
        from Hql.Query import Query
        import yaml

        self.loaded = yaml.load(txt, yaml.SafeLoader)
        self.assembly:Union[None, Query] = None

    def gen_hac(self):
        from copy import deepcopy
        from Hql.Hac import Hac
        doc:dict = deepcopy(self.loaded)

        for i in ['detection', 'logsource']:
            doc.pop(i)

        return Hac(doc, 'sigma')

    def assemble(self):
        from Hql.Expressions import PipeExpression
        from Hql.Query import Query, QueryStatement

        hac = self.gen_hac()
        dac = self.loaded['detection']
        src = self.loaded['logsource']

        prepipe = self.gen_src(src)
        pipe = self.parse_dac(dac)
        expr = PipeExpression(prepipe, [pipe])

        statement = QueryStatement(expr)
        self.assembly = Query([statement])

    def gen_src(self, src:dict) -> 'DotCompositeFunction':
        from Hql.Expressions import DotCompositeFunction
        from Hql.Expressions import FuncExpr, StringLiteral

        product = StringLiteral(src['product'])
        category = StringLiteral(src['category'])

        funcs = [
            FuncExpr('product', [product]),
            FuncExpr('category', [category])
        ]

        return DotCompositeFunction(funcs)

    def parse_dac(self, dac:dict):
        from Hql.Operators import Where

        selections = []
        for i in dac:
            if i == 'condition':
                continue

            selections.append(Selection(i, dac[i]))

        condition = Condition(dac['condition'], selections)
        expr = Where(condition.assemble())

        return expr

    def gen_hql(self, src:dict, dac:dict):
        selections = []
        for i in dac:
            ...
