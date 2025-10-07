import logging
import re
from typing import Optional, TYPE_CHECKING, Union
from Hql.Exceptions import HacExceptions as hace

if TYPE_CHECKING:
    from Hql.Hac import Hac

class Tag():
    def __init__(self, name:str):
        self.name = name
        self.text = ''
        self.list = []

    def add_item(self, item:str):
        if self.text:
            raise hace.HacException(f'Attempting to add item to text tag {self.name}')
        self.list.append(item)

    def add_text(self, text:str):
        if self.list:
            raise hace.HacException(f'Attempting to add text to list tag {self.name}')
        text = text.strip(' \t')
        if self.text:
            self.text += '\n'
        self.text += text

    def get_val(self) -> Union[str, list]:
        if self.list:
            return self.list
        return self.text.strip(' \n')

class Parser():
    @staticmethod
    def parse_file(filename:str) -> 'Hac':
        with open(filename, mode='r') as f:
            return Parser.parse_text(f.read(), src=filename)

    @staticmethod   
    def parse_text(text:str, src:str='') -> 'Hac':
        from Hql.Hac import Hac
        tags:list[Tag] = []
        comment = Parser.get_comment(text).split('\n')

        padding = r'[\s\* ]*'

        tag:Optional[Tag] = None
        for i in comment:
            # tag
            match = re.search(r'^' + padding + r'@([a-z]+)(\s+(.*))?', i)
            if match:
                if tag:
                    tags.append(tag)

                tag = Tag(match.group(1))
                if match.group(3):
                    tag.add_text(match.group(3))

                continue

            if not tag:
                # skip leading empty lines
                if re.match(r'^' + padding + r'$', i):
                    continue
                raise hace.HacException('HaC content added without tag')

            # list item
            match = re.search(r'^' + padding + r'-\s*(.*)', i)
            if match:
                tag.add_item(match.group(1))
                continue

            # text line
            match = re.search(r'^' + padding + r'(.*)', i)
            if match and match.group(1):
                tag.add_text(match.group(1))
                continue

            if tag.text:
                # empty line
                tag.add_text('')

        if tag:
            tags.append(tag)

        asm = dict()
        for tag in tags:
            asm[tag.name] = tag.get_val()

        return Hac(asm, src)

    @staticmethod
    def get_comment(text:str) -> str:
        pattern = r'/\*\*.*?\n(.*?)\*/'

        finds = re.findall(pattern, text, flags=re.DOTALL)
        if not finds:
            return ''
        return finds[0]
