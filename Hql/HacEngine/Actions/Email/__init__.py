import smtplib
from email.message import EmailMessage
import logging

from .. import HqlData
from .. import ActionException

class EmailAction():
    def __init__(self, conf:dict) -> None:
        self.conf = conf

    def gen_header(self, keys:list[str]):
        html = '<tr>\n'
        for i in keys:
            html += ('<th>' + i + '<th>\n')
        html += '</tr>\n'
        return html

    def gen_row(self, keys:list[str], row:dict):
        html = '<tr>\n'
        for i in keys:
            html += ('<td>' + row[i] + '<td>\n')
        html += '</tr>\n'
        return html

    def gen_table(self, table:HqlData.Table):
        dicts = table.to_dicts()

        if table.schema:
            keys = list(table.schema.schema.keys())

        else:
            keys = list(dicts[0].keys())

        html  = '<table>\n'
        html += self.gen_header(keys)
        for i in dicts:
            html += self.gen_row(keys, i)
        html += '</table>\n'

        return html

    def gen_body(self):
        html = '<html>\n'

        html += f"<h1>{self.hac['title']}</h1>\n"
        html += '<br><br>\n'

        for table in self.data:
            html += f"<h2>{table.name}</h2>\n"
            html += self.gen_table(table)
            html += '<br><br>\n'

        html += '</html>\n'
        return html

    # Can probably use kwargs later to state style or something
    # Or just put that into the config
    def eval(self, hac:dict, data:HqlData.Data, **kwargs):
        self.hac = hac
        self.data = data

        body = self.gen_body()

        msg = EmailMessage()
        msg.set_content(body)
        
        msg['Subject'] = f"Detection Fired: {self.hac['title']}"

        sender = self.conf.get('sender', '')
        if not sender:
            import socket
            logging.warning('Sender address not specified, might prevent sending.')
            sender = f'hacengine@{socket.gethostname()}'
        msg['From'] = sender

        receiver = self.conf.get('receiver', '')
        if not receiver:
            raise ActionException(self.conf, "Receiver not set in configuration")
        msg['To'] = receiver

        server = self.conf.get('server', '')
        if not server:
            raise ActionException(self.conf, 'Server not set in configuration')

        s = smtplib.SMTP(server)
        s.send_message(msg)
        s.quit()
