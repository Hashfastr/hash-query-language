from Hql.Exceptions import HacExceptions as hace
from Hql.Hac.Sources import Source, Product
from Hql.Hac.Parser import Tag, Parser
import json
from typing import Union

class Hac():
    '''
    asm is the output of the parser
    src is a string identifier of the origin of the HaC, e.g. a filename
    default_schedule is if there is an undefined schedule, safe defaults to hourly
    '''
    def __init__(self, asm:dict, src:str, default_schedule:str='0 * * * *', username:str='Username') -> None:
        from datetime import datetime
        import uuid
        self.id = str(uuid.uuid4())
        self.schedule = default_schedule

        if not asm:
            asm = {
                'title': 'my detection',
                'author': 'Unknown',
                'id': self.id,
                'status': 'testing',
                'level': 'medium',
                'schedule': self.schedule,
                'description': 'Parasaurolophus is a great dinosaur',
                'tags': ['tag'],
                'triage': 'drink celsius',
                'falsepositives': ['certainly'],
                'authornotes': '',
                'references': ['https://hql.dev'],
                'changelog': [
                    f'{datetime.now().strftime("%Y-%m-%d")} {username}: Init detection'
                ]
            }

        self.asm = asm
        self.src = src

        # Required tags from a HaC definition
        self.required = [
            'title',
            'author',
            'id',
            'status',
            'schedule',
            'description',
        ]

        self.order = [
            'title',
            'author',
            'id',
            'status',
            'level',
            'schedule',
            'description',
            'tags',
            'triage',
            'falsepositives',
            'authornotes',
            'references',
            'changelog'
        ]

        self.validate()
        self.reorder_keys()

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
    
    def get(self, name:str) -> Union[str, list[str]]:
        if name == 'src':
            return self.src
        return self.asm.get(name, '')

    def reorder_keys(self):
        new = dict()

        for i in self.order:
            if i not in self.asm:
                continue
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
