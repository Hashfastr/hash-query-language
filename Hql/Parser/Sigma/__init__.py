from .Selection import Selection
from .Condition import Condition

class SigmaParser():
    def __init__(self, txt):
        import yaml
        self.loaded = yaml.load(txt, yaml.SafeLoader)

    def assemble(self):
        from Hql.Expressions import PipeExpression
        
        hac = dict()
        for i in self.loaded:
            if i in ('logsource', 'detection'):
                continue
            hac[i] = self.loaded[i]

        hac = self.gen_hac(hac)

        dac = self.loaded['detection']
        src = self.loaded['logsource']

        op_expr = self.parse_dac(src, dac)
        pipe_expr = PipeExpression(None, [op_expr])

    def parse_dac(self, src:dict, dac:dict):
        from Hql.Operators import Where

        selections = []
        for i in dac:
            if i == 'condition':
                continue

            selections.append(Selection(i, dac[i]))

        condition = Condition(dac['condition'], selections)
        expr = Where(condition.assemble())

        return expr

    def gen_hac(self, sigma:dict):
        from Hql.Hac import Hac
        return Hac(sigma, 'sigma')

    def gen_hql(self, src:dict, dac:dict):
        selections = []
        for i in dac:
            ...
