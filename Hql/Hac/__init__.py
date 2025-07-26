from .Exceptions import *
from Hql.Data import Data as HqlData

class Hac():
    '''
    asm is the output of the parser
    src is a string identifier of the origin of the HaC, e.g. a filename
    '''
    def __init__(self, asm:dict, src:str) -> None:
        self.asm = asm
        self.src = src

        # Required tags from a HaC definition
        self.required = [
            'title',
            'id',
            'status',
            'schedule',
            'description',
            'hql'
        ]

        self.validate()

    def render(self, target:str='md'):
        from .Doc import HacDoc
        from .Dag import Dag

        hd = HacDoc(self)
        
        if target in ('md', 'markdown'):
            return hd.markdown()

        if target == 'json':
            return hd.json()

        if target == 'dag':
            dag = Dag(self)
            return dag.gen_dag()

        raise HacException(f'Unknown HaC render type {target}')
    
    def get(self, name:str):
        if name == 'src':
            return self.src
        return self.asm.get(name, '')

    def validate(self):
        for i in self.required:
            if i not in self.asm:
                raise HacException(f'Missing required field {i} in {self.src}')
