from .Selection import Selection
from .Condition import Condition

class SigmaParser():
    def __init__(self, txt):
        import yaml
        self.loaded = yaml.load(txt, yaml.SafeLoader)

    def assemble(self):
        hac = dict()
        for i in self.loaded:
            if i in ('logsource', 'detection'):
                continue
            hac[i] = self.loaded[i]

        hac = self.gen_hac(hac)

        dac = self.loaded['detection']
        src = self.loaded['logsource']

        return self.parse_dac(src, dac)

    def parse_dac(self, src:dict, dac:dict):
        selections = []
        for i in dac:
            if i == 'condition':
                continue

            selections.append(Selection(i, dac[i]))

        condition = Condition(dac['condition'], selections)
        expr = condition.assemble()

        return expr

    def gen_hac(self, sigma:dict):
        from Hql.Hac import Hac
        return Hac(sigma, 'sigma')

    def gen_hql(self, src:dict, dac:dict):
        selections = []
        for i in dac:
            ...
