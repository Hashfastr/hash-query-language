from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from . import Hac
from .grammar.HacLexer import HacLexer
from .grammar.HacParser import HacParser
from .grammar.HacVisitor import HacVisitor
import logging

from Hql.Exceptions import HacExceptions as hace

class HqlErrorListener(ErrorListener):
    def __init__(self, text:str, filename:str):
        ErrorListener.__init__(self)
        self.text = text
        self.filename = filename

    def syntaxError(self, recognizer:HacParser, offendingSymbol, line, column, msg, e):
        e = hace.LexerException(msg, self.text, line, column, offendingSymbol, filename=self.filename)
        Parser.handleException(recognizer, e)
        
class Parser():
    def __init__(self, text:str='', filename:str=''):
        if not text and filename:
            with open(filename, mode='r') as f:
                text = f.read()

        self.text = text
        self.filename = filename
        self.tree = self.parse_file()
    
    def parse_file(self):
        self.err_listener = HqlErrorListener(self.text, self.filename)
        
        lexer = HacLexer(InputStream(self.text))
        token_stream = CommonTokenStream(lexer)
        parser = HacParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(self.err_listener)
         
        return parser.dacBlock()

    def assemble(self):
        visitor = Visitor(self.filename)
        assembly = visitor.visit(self.tree)
        
        if assembly == None:
            logging.error("Compiler error!")
            logging.error("Parser returned None instead of valid assembly")
            logging.error("Import error?")
            raise Exception("Compiler error, visitor returned None")

        self.hac = Hac(assembly, self.filename)

        return self.hac
    
    @staticmethod
    def getText(ctx):
        stream = ctx.parser.getTokenStream()
        start = ctx.start.tokenIndex
        stop = ctx.stop.tokenIndex

        return stream.getText(start, stop)
    
    @staticmethod
    def handleException(ctx, e):
        logging.critical(f'Failed to parse query {e.filename}')
        
        if isinstance(e, hace.LexerException):
            text = e.text
            text = text.split('\n')[e.line - 1]
            
        else:
            text = Parser.getText(ctx)
        
        logging.critical(text)
        marker = (' ' * e.col) + '^'
        logging.critical(marker)
        raise e

class Tag():
    def __init__(self, name:str) -> None:
        self.name = name
      
class ListTag(Tag):
    def __init__(self, name: str) -> None:
        Tag.__init__(self, name)
        self.type = 'list'
        self.items = []

class TextTag(Tag):
    def __init__(self, name: str) -> None:
        Tag.__init__(self, name)
        self.type = 'text'
        self.text = ''

# Overrides the HqlVisitor templates
# If not defined here, each node only returns its children.
class Visitor(HacVisitor):
    def __init__(self, filename:str):
        self.filename = filename

    def visitDacBlock(self, ctx: HacParser.DacBlockContext):
        tags = []
        for i in ctx.Tags:
            new = self.visit(i)
            if new != None:
                tags.append(new)

        tag_dict = dict()
        for i in tags:
            if i.name in tag_dict:
                logging.warning(f'Multiple definitions of {i.name}, overwriting definition')

            if i.type == 'list':
                tag_dict[i.name] = i.items

            elif i.type == 'text':
                tag_dict[i.name] = i.text

        if ctx.Hql:
            hql = self.visit(ctx.Hql)
            tag_dict['hql'] = hql

        return tag_dict

    def visitTagSection(self, ctx: HacParser.TagSectionContext):
        if ctx.List:
            return self.visit(ctx.List)

        if ctx.Text:
            return self.visit(ctx.Text)

        return None

    def visitListStart(self, ctx: HacParser.ListStartContext):
        name = self.visit(ctx.Name)

        tag = ListTag(name)
        for i in ctx.Items:
            tag.items.append(self.visit(i))
        return tag

    def visitListTag(self, ctx: HacParser.ListTagContext):
        return ctx.Name.__getattribute__('text')

    def visitListLine(self, ctx: HacParser.ListLineContext):
        return self.visit(ctx.Item)

    def visitListItem(self, ctx: HacParser.ListItemContext):
        return self.visit(ctx.Data)

    def visitTextStart(self, ctx: HacParser.TextStartContext):
        name = self.visit(ctx.Name)
        tag = TextTag(name)

        if ctx.Root:
            tag.text += self.visit(ctx.Root)

        for i in ctx.Lines:
            tag.text += '\n'
            tag.text += self.visit(i)

        tag.text = tag.text.strip('\n')

        return tag

    def visitTextTag(self, ctx: HacParser.TextTagContext):
        return ctx.Name.__getattribute__('text')

    def visitSingleTextLine(self, ctx: HacParser.SingleTextLineContext):
        return self.visit(ctx.Line)

    def visitTextLine(self, ctx: HacParser.TextLineContext):
        return self.visit(ctx.Line) if ctx.Line else ''

    def visitData(self, ctx: HacParser.DataContext):
        data = ''
        for i in range(ctx.getChildCount()):
            data += ctx.getChild(i).getText()
        return data

    def visitAllData(self, ctx: HacParser.AllDataContext):
        data = ''
        for i in range(ctx.getChildCount()):
            data += ctx.getChild(i).getText()
        return data

    def visitHqlText(self, ctx: HacParser.HqlTextContext):
        lines = []
        for i in ctx.Lines:
            lines.append(self.visit(i))
        return '\n'.join(lines)

    def visitHqlLine(self, ctx: HacParser.HqlLineContext):
        return self.visit(ctx.Data)
