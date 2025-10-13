from Hql.Exceptions import HacExceptions as hace
from Hql.Hac.Sources import Source, Product
from Hql.Hac.Parser import Tag, Parser

class Hac():
    '''
    asm is the output of the parser
    src is a string identifier of the origin of the HaC, e.g. a filename
    default_schedule is if there is an undefined schedule, safe defaults to hourly
    '''
    def __init__(self, asm:dict, src:str, default_schedule:str='0 * * * *') -> None:
        import uuid

        self.asm = asm
        self.src = src
        self.schedule = default_schedule

        # Required tags from a HaC definition
        self.required = [
            'title',
            'id',
            'status',
            'schedule',
            'description',
            'author',
        ]

        self.validate()
        self.reorder_keys()

        self.id = str(uuid.uuid4())

    def render(self, target:str='md'):
        from .Doc import HacDoc

        hd = HacDoc(self)
        
        if target in ('md', 'markdown'):
            return hd.markdown()

        if target == 'json':
            return hd.json()

        if target == 'decompile':
            return hd.decompile()

        raise hace.HacException(f'Unknown HaC render type {target}')
    
    def get(self, name:str):
        if name == 'src':
            return self.src
        return self.asm.get(name, '')

    def reorder_keys(self):
        new = dict()

        for i in self.required:
            new[i] = self.asm.pop(i)

        for i in self.asm:
            new[i] = self.asm[i]

        self.asm = new

    def validate(self):
        for i in self.required:
            if i not in self.asm:
                if i == 'schedule':
                    self.asm['schedule'] = self.schedule

                elif i == 'author':
                    self.asm['author'] = 'Unknown'

                elif i == 'id':
                    self.asm['id'] = self.id

                else:
                    raise hace.HacException(f'Missing required field {i} in {self.src}')

        self.id = self.asm['id']
        self.schedule = self.asm['schedule']
