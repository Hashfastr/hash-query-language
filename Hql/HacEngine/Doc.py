from . import Hac

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
            md += '### References'
            for i in references:
                md += f'- {i}\n'
            md += '\n'

        changelog = self.hac.get('changelog')
        if changelog:
            md += '### Change Log'
            for i in changelog:
                md += f'- {i}\n'
            md += '\n'

        return md
