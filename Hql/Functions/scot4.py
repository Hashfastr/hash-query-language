from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema
from Hql.Operators import Union
from Hql.Expressions import Wildcard, NamedReference, NamedExpression, StringLiteral
from Hql.Hac import Hac
import requests
import json

import logging
from typing import Optional

@register_func('scot4')
class scot4(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        Function.__init__(self, args, 0, -1, conf)
        self.params = {
            'server': self.conf.get('default', None),
            'union': self.conf.get('union', True)
        }

        if 'source_tags' not in self.conf:
            self.conf['source_tags'] = dict()

        if 'link_transform' not in self.conf['source_tags']:
            self.conf['source_tags']['link_transform'] = 'domain'

        if 'blacklist' not in self.conf['source_tags']:
            self.conf['source_tags']['blacklist'] = []

        if 'row_limit' not in self.conf:
            self.conf['row_limit'] = 100

        for i in self.args:
            if not isinstance(i, NamedExpression):
                raise hqle.ArgumentException(f'Invalid argument expression given to scot4: {i}')
            if not isinstance(i.paths[0], StringLiteral) or len(i.paths) > 1:
                raise hqle.ArgumentException(f'Invalid parameter name(s) given to scot4: {i.paths}')
            val = i.paths[0].quote('')

            if val not in self.params:
                raise hqle.ArgumentException(f'Invalid parameter given to scot4: {val}')

            self.params[val] = i.value

        for i in self.params:
            if self.params[i] == None:
                raise hqle.ArgumentException(f'Missing required parameter {i} in scot4')

        self.server = dict()
        for i in self.conf['servers']:
            if i['name'] == self.params['server']:
                self.server = i

        if not self.server:
            raise hqle.ArgumentException(f'Attempting to use invalid scot4 server definition {self.params["server"]}')

    def eval(self, ctx:'Context', **kwargs):
        if not ctx.hac:
            return Data()

        res = self.post_alertgroup(ctx.data, ctx.hac)
        return Data([Table(init_data=res)])

    def post(self, api:str, json:dict):
        url = self.server['host'] + api
        headers = {
            'Authorization': f'apikey {self.server["apikey"]}'
        }

        res = requests.post(url=url, headers=headers, json=json)

        if res.status_code != 200:
            logging.error(f'Post to scot returned a {res.status_code}')
            logging.error(res.text)

        return res

    def post_alertgroup(self, data:Data, hac:Hac):
        union = self.conf.get('always_union', False)
        if union:
           data = Union([Wildcard('*')], NamedReference('scot4_unioned')).eval(Context(data))

        srcs = hac.get('references')
        assert isinstance(srcs, list)
        tags = hac.get('tags')
        assert isinstance(tags, list)

        out = []
        for i in data:
            alerts = self.gen_alerts(i)

            body = {
                'subject': hac.get('title'),
                'sources': self.process_sources(srcs),
                'tags': tags,
                'alerts': alerts
            }

            res = self.post('/api/v1/alertgroup/', body)
            if res.status_code != 200 or True:
                res = json.loads(res.text)
                print(json.dumps(res))
                continue

            res = json.loads(res.text)
            new = {
                'id': res['id'],
                'owner': res['owner'],
                'created': res['created']
            }
            out.append(new)

        return out

    def gen_alerts(self, table:Table):
        limit = self.conf['row_limit']
        alerts = []
        for i in table.to_dicts()[:limit]:
            alerts.append({'data': i})
        return alerts

    def process_sources(self, sources:list[str]) -> list[str]:
        import re
        pat = re.compile(r'(https?://)?(?P<domain>[^/]+)(/.*)?')

        out = []
        for i in sources:
            if self.conf['source_tags']['link_transform'] == 'domain':
                res = pat.search(i)
                if res:
                    i = res.group(2)
            out.append(i)

        return out

