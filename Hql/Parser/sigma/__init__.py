from .Selection import SigmaSelection

class SigmaParser():
    def __init__(self, txt):
        import yaml
        self.loaded = yaml.load(txt, yaml.SafeLoader)

    def parse(self):
        hac = dict()
        for i in self.loaded:
            if i in ('logsource', 'detection'):
                continue
            hac[i] = self.loaded[i]

        hac = self.gen_hac(hac)

        dac = self.loaded['detection']
        src = self.loaded['logsource']

    def gen_hac(self, sigma:dict):
        from Hql.Hac import Hac
        return Hac(sigma, 'sigma')

    def gen_hql(self, src:dict, dac:dict):
        selections = []
        for i in dac:
            ...
