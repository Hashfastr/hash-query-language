from HaCEngine.Exceptions import *
from HaCEngine import Hac
from datetime import datetime
import logging

class Dag():
    def __init__(self, hac:Hac) -> None:
        self.hac = hac

    def gen_dag(self):
        return self.dag_decorator()

    def dag_decorator(self):
        filename = self.hac.get('filename')
        schedule = self.hac.get('schedule')
        hql = self.hac.get('hql')
        title = self.hac.get('title')

        tags = []
        tags += self.hac.get('tags')
        tag_text = ', '.join([f"'{x}'" for x in tags] + [filename])

        dagid = self.hac.get('id')

        now = datetime.now()
        md = self.hac.render(target='md')

        description = self.hac.get('description')

        if not hql:
            raise DagException(name=dagid, message='HaC file contains no detection!!')

        # Add this later if needed
        '''
        doc_md = \'\'\'
        {md}
        \'\'\'
        '''

        decorator = f'''
description = \'\'\'
{description}
\'\'\'
hql_detection = \'\'\'
{hql}
\'\'\'
@dag(
    dag_id=\'{dagid}\',
    dag_display_name=\'{title}\'
    schedule=\'{schedule}\',
    start_date=datetime.datetime({now.year}, {now.month}, {now.day}),
    doc_md=doc_md,
    tags=[{tag_text}],
    description=description,
    catchup=False
)
'''

        return decorator

    def dag_code(self):
        ...
