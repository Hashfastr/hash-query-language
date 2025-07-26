from Hql.Exceptions import HacExceptions as hace
from . import Hac
from datetime import datetime

class Dag():
    def __init__(self, hac:Hac) -> None:
        self.hac = hac

    def gen_dag(self):
        return self.dag_header()

    def dag_header(self):
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
            raise hace.DagException(name=dagid, message='HaC file contains no detection!!')

        # Add this later if needed
        f'''
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
