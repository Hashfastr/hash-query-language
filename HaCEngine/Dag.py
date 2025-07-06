from HaCEngine.Exceptions import *
from HaCEngine.Doc import HacDoc
from datetime import datetime
import logging

class Dag():
    def __init__(self, hac:dict, hql:str) -> None:
        self.hac = hac
        self.hql = hql

    def dag_decorator(self):
        filename = self.hac.get('filename', '')
        schedule = self.hac.get('schedule', '')
        if not schedule:
            raise DagException(filename, f'Schedule not defined in dag')

        tags = []
        tags += self.hac.get('tags', [])
        
        if 'level' not in self.hac:
            logging.warning(f'level undefined in HaC {filename}')
        else:
            tags.append(self.hac['level'])

        if 'id' not in self.hac:
            raise DagException(filename, f'id undefined in HaC')
        dagid = self.hac['id']

        now = datetime.now()

        decorator = f'''
        @dag(
            dag_id=\'{dagid}\',
            schedule=\'{schedule}\',
            start_date=datetime.datetime({now.year}, {now.month}, {now.day}),
            
        )
        '''
