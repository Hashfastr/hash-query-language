from . import Hac
import logging
import datetime

class HacDoc():
    def __init__(self, hac:Hac) -> None:
        self.hac:Hac = hac
        self.md_table_fields = [
            'status',
            'level',
            'schedule'
        ]

    def json(self):
        import json
        return json.dumps(self.hac.asm, indent=2)

    def markdown(self):
        md = f"# {self.hac.get('title')}\n"
        md += f"*{self.hac.get('id')}*\n"
        
        author = self.hac.get('author')
        if author:
            md += f"{author}\n"
        md += '\n'

        # Build table values
        # Two table fields are required so we always add a table header
        md += '| | |\n'
        md += '|-|-|\n'
        for i in self.md_table_fields:
            j = self.hac.get(i)

            if not j:
                continue

            name = i[0].upper() + i[1:]
            md += f"| {name} | {j} |\n"
        md += '\n'

        md += '### Description\n'
        md += self.hac.get('description')
        md += '\n'

        tags = self.hac.get('tags')
        if tags:
            md += '### Tags\n'
            for i in tags:
                md += f'- {i}\n'
            md += '\n'

        triage = self.hac.get('triage')
        if triage:
            md += '### Triage\n'
            md += f'{triage}\n'
            md += '\n'

        falsepositives = self.hac.get('falsepositives')
        if falsepositives:
            md += '### False Positives\n'
            for i in falsepositives:
                md += f'- {i}\n'
            md += '\n'

        authornotes = self.hac.get('authornotes')
        if authornotes:
            md += '### Author Notes\n'
            md += f'{authornotes}\n'
            md += '\n'

        references = self.hac.get('references')
        if references:
            md += '### References\n'
            for i in references:
                md += f'- {i}\n'
            md += '\n'

        changelog = self.hac.get('changelog')
        if changelog:
            md += '### Change Log\n'
            for i in changelog:
                md += f'- {i}\n'
            md += '\n'

        return md

    def decompile(self):
        from copy import deepcopy
        asm:dict = deepcopy(self.hac.asm)
        long = False
        extra_space = [
            'id',
            'description',
        ]

        out = '/**\n'
        for i in asm:
            out += ' * '
            out += f'@{i}'
            
            if isinstance(asm[i], str):
                if len(asm[i]) < 60 or i == 'title':
                    out += f' {asm[i]}\n'
                else:
                    out += '\n * '
                    out += asm[i].strip().replace('\n', '\n * ')
                    out += '\n'
                    long = True

            elif isinstance(asm[i], list):
                out += '\n'
                for j in asm[i]:
                    out += f' * - {j}\n'
                long = True

            elif isinstance(asm[i], datetime.date):
                out += ' '
                out += str(asm[i])
                out += '\n'

            else:
                logging.critical(f'Attempting to decompile impossible Hac datatype {type(asm[i])}, skipping')
                out += '\n'

            if long or i in extra_space:
                out += ' * \n'
                long = False

        # Check for a trailing empty comment line from 'long' instances
        if out[-4:] == ' * \n':
            out = out[:-4]
        
        out += ' */'

        return out

    def html(self):
        html = f"<h1>{self.hac.get('title')}</h1><br>"
        html += f"<i>{self.hac.get('id')}</i><br>"
        
        author = self.hac.get('author')
        if author:
            html += f"{author}<br>"
        html += '<br>'

        # Build table values
        # Two table fields are required so we always add a table header
        if self.md_table_fields:
            html += '<table>'
            for i in self.md_table_fields:
                j = self.hac.get(i)

                if not j:
                    continue

                name = i[0].upper() + i[1:]
                html += f"<tr><th>{name}</th> <th>{j}</th></tr>"
            html += '</table>'
            html += '<br>'

        html += '<h3>Description</h3><br><p>'
        html += str(self.hac.get('description'))
        html += '</p><br>'

        tags = self.hac.get('tags')
        if tags:
            html += '<h3>Tags</h3><br>'
            html += '<ul>'
            for i in tags:
                html += f'<li>{i}</li>'
            html += '</ul>'
            html += '<br>'

        triage = self.hac.get('triage')
        if triage:
            html += '<h3>Triage</h3><br><p>'
            html += f'{triage}<br>'
            html += '</p><br>'

        falsepositives = self.hac.get('falsepositives')
        if falsepositives:
            html += '<h3>False Positives</h3><br>'
            html += '<ul>'
            for i in falsepositives:
                html += f'<li>{i}</li>'
            html += '</ul>'
            html += '<br>'

        authornotes = self.hac.get('authornotes')
        if authornotes:
            html += '<h3>Author Notes</h3><br><p>'
            html += f'{authornotes}<br>'
            html += '</p><br>'

        references = self.hac.get('references')
        if references:
            html += '<h3>References</h3><br>'
            html += '<ul>'
            for i in references:
                html += f'<li>{i}</li>'
            html += '</ul>'
            html += '<br>'

        changelog = self.hac.get('changelog')
        if changelog:
            html += '<h3>Change Log</h3><br>'
            html += '<ul>'
            for i in changelog:
                html += f'<li>{i}</li>'
            html += '</ul>'
            html += '<br>'

        return html
