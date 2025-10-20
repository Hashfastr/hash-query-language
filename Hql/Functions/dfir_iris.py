from Hql.Expressions import NamedExpression, NamedReference
from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from Hql.Data import Data, Series, Table, Schema

from dfir_iris_client.session import ClientSession
from dfir_iris_client.alert import Alert

import logging
from typing import Optional

@register_func('dfir_iris')
class dfir_iris(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        Function.__init__(self, args, 0, 1, conf=conf)
        self.params = dict()

        for i in self.args:
            if not isinstance(i, NamedExpression):
                raise hqle.ArgumentException(f'Invalid argument expression given to dfir_iris: {i}')
            if not isinstance(i.paths[0], NamedReference) or len(i.paths) > 1:
                raise hqle.ArgumentException(f'Invalid parameter name given to dfir_iris: {i.paths}')
            self.params[i.paths[0].name] = i.value

        self.levels = {
            'critical': 5,
            'high': 4,
            'medium': 3,
            'low': 2,
            'informational': 1
        }

    def union(self, data:Data) -> Data:
        from Hql.Operators import Union
        from Hql.Expressions import Wildcard
        return Union([Wildcard('*')]).eval(Context(data))
    
    def alerts(self, ctx:'Context', session:ClientSession) -> Data:
        if not ctx.hac:
            return Data()

        alert = Alert(session=session)
        req = dict()
        req['alert_title'] = ctx.hac.get('title')
        req['alert_description'] = ctx.hac.get('description')
        req['alert_source'] = self.conf.get('source_name', 'Hql-HacEngine')

        if ctx.hac.get('level'):
            req['alert_severity'] = ctx.hac.get('level')

        if ctx.hac.get('authornotes'):
            req['alert_note'] = ctx.hac.get('authornotes')

        if ctx.hac.get('tags'):
            req['alert_tags'] = ','.join(ctx.hac.get('tags'))
        
        req['alert_source_content'] = ctx.hac.asm

        data = ctx.data
        if self.conf.get('always_union', True):
            data = self.union(ctx.data)
        
        limit = self.conf.get('alert_limit', 100)

        out = []
        for i in data:
            # req['alert_iocs'] = i.to_dicts()[:limit]
            res = alert.add_alert(req)
            out.append(res.as_json())

        return Data([Table(init_data=out, name='dfir_iris')])

    def eval(self, ctx:'Context', **kwargs) -> Data:
        if 'target' not in self.params:
            target = self.conf.get('default-target', 'alerts')
        else:
            target = self.params['target'].eval(ctx, as_str=True)

        if 'apikey' not in self.conf:
            raise hqle.ConfigException('Missing required parameter apikey in dfir_iris config')
        apikey = self.conf['apikey']
        server = self.conf.get('host', '127.0.0.1')
        port = self.conf.get('port', '443')
        ssl = self.conf.get('ssl', True)
        verify = self.conf.get('verify_ssl', True)

        host = 'https://' if ssl else 'http://'
        host += server + ':' + str(port)

        session = ClientSession(apikey=apikey, host=host, ssl_verify=verify)

        if target == 'alerts':
            return self.alerts(ctx, session)
        else:
            return Data()
