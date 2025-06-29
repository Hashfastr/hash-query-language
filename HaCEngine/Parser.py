from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from HaCEngine.grammar.HacLexer import HacLexer
from HaCEngine.grammar.HacParser import HacParser
from HaCEngine.grammar.HacVisitor import HacVisitor
import logging

from HaCEngine.Exceptions import *

class HqlErrorListener(ErrorListener):
    def __init__(self, text:str, filename:str):
        ErrorListener.__init__(self)
        self.text = text
        self.filename = filename

    def syntaxError(self, recognizer:HacParser, offendingSymbol, line, column, msg, e):
        e = LexerException(msg, self.text, line, column, offendingSymbol, filename=self.filename)
        Parser.handleException(recognizer, e)
        
class Parser():
    def __init__(self, filename:str):
        self.filename = filename
        self.tree = self.parse_file()
    
    def parse_file(self):
        try:
            with open(self.filename, 'r') as f:
                text = f.read()
        except Exception as e:
            logging.error(f"Failed to open file {self.filename}")
            logging.error(str(e))
            raise e
        
        self.err_listener = HqlErrorListener(text, self.filename)
        
        lexer = HacLexer(InputStream(text))
        token_stream = CommonTokenStream(lexer)
        parser = HacParser(token_stream)

        parser.removeErrorListeners()
        parser.addErrorListener(self.err_listener)
         
        return parser.dacBlock()

    def assemble(self):
        visitor = Visitor(self.filename)
        self.assembly = visitor.visit(self.tree)
        
        if self.assembly == None:
            logging.error("Compiler error!")
            logging.error("Parser returned None instead of valid assembly")
            logging.error("Import error?")
            raise Exception("Compiler error, visitor returned None")

        return self.assembly
    
    @staticmethod
    def getText(ctx):
        stream = ctx.parser.getTokenStream()
        start = ctx.start.tokenIndex
        stop = ctx.stop.tokenIndex

        return stream.getText(start, stop)
    
    @staticmethod
    def handleException(ctx, e):
        logging.critical(f'Failed to parse query {e.filename}')
        
        if isinstance(e, LexerException):
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
        self.items = list()

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

        return tag_dict

    def visitTagSection(self, ctx: HacParser.TagSectionContext):
        if ctx.List:
            return self.visit(ctx.List)

        if ctx.Text:
            return self.visit(ctx.Text)

        return None

    def visitListStart(self, ctx: HacParser.ListStartContext):
        # Using this instead of regular attribute getting to shut the linter up
        tag = ListTag(ctx.Name.__getattribute__('text'))
        for i in ctx.Items:
            tag.items.append(self.visit(i))
        return tag

    def visitListLine(self, ctx: HacParser.ListLineContext):
        return self.visit(ctx.Item)

    def visitListItem(self, ctx: HacParser.ListItemContext):
        return self.visit(ctx.Data)

    def visitTextStart(self, ctx: HacParser.TextStartContext):
        # Using this instead of regular attribute getting to shut the linter up
        tag = TextTag(ctx.Name.__getattribute__('text'))

        if ctx.Root:
            tag.text += self.visit(ctx.Root)

        for i in ctx.Lines:
            tag.text += '\n'
            tag.text += self.visit(i)

        tag.text = tag.text.strip('\n')

        return tag

    def visitSingleTextLine(self, ctx: HacParser.SingleTextLineContext):
        return self.visit(ctx.Line)

    def visitTextLine(self, ctx: HacParser.TextLineContext):
        return self.visit(ctx.Data) if ctx.Data else ''

    def visitData(self, ctx: HacParser.DataContext):
        data = ''
        for i in range(ctx.getChildCount()):
            data += ctx.getChild(i).getText()
        return data

