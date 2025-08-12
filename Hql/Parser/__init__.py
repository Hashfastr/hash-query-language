from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from Hql.Exceptions import HqlExceptions as hqle 
from .grammar.HqlLexer import HqlLexer
from .grammar.HqlParser import HqlParser
from .grammar.HqlVisitor import HqlVisitor

from Hql.Query import Query, QueryStatement, LetStatement

from Hql.Parser.BaseExpressions import BaseExpressions as ParseBaseExpressions
from Hql.Parser.Functions import Functions as ParseFunctions
from Hql.Parser.Operators import Operators as ParseOperators
from Hql.Parser.Logic import Logic as ParseLogic

from Hql.Parser.Sigma import SigmaParser

import logging

class HqlErrorListener(ErrorListener):
    def __init__(self, text:str, filename:str):
        ErrorListener.__init__(self)
        self.text = text
        self.filename = filename

    def syntaxError(self, recognizer:HqlParser, offendingSymbol, line, column, msg, e):
        e = hqle.LexerException(msg, self.text, line, column, offendingSymbol, filename=self.filename)
        Parser.handleException(recognizer, e)
        
class Parser():
    def __init__(self, filename:str):
        self.filename = filename
        self.tree = self.parse_file()
    
    def parse_file(self) -> HqlParser.QueryContext:
        try:
            with open(self.filename, 'r') as f:
                text = f.read()
        except Exception as e:
            logging.error(f"Failed to open file {self.filename}")
            logging.error(str(e))
            raise e

        if not text:
            logging.error(f'Query file is empty: {self.filename}')
            raise hqle.QueryException('Empty query given')
        
        self.err_listener = HqlErrorListener(text, self.filename)
        
        lexer = HqlLexer(InputStream(text))
        token_stream = CommonTokenStream(lexer)
        parser = HqlParser(token_stream)
        
        parser.removeErrorListeners()
        parser.addErrorListener(self.err_listener)
         
        return parser.query()

    def assemble(self):
        visitor = Visitor(self.filename)
        self.assembly = visitor.visit(self.tree)
        
        if self.assembly == None:
            logging.error("Compiler error!")
            logging.error("Parser returned None instead of valid assembly")
            logging.error("Import error?")
            raise Exception("Compiler error, visitor returned None")
    
    @staticmethod
    def getText(ctx):
        stream = ctx.parser.getTokenStream()
        start = ctx.start.tokenIndex
        stop = ctx.stop.tokenIndex

        return stream.getText(start, stop)
    
    @staticmethod
    def handleException(ctx, e:hqle.ParseException):
        logging.critical(f'Failed to parse query {e.filename}')
        
        if isinstance(e, hqle.LexerException):
            text = e.text
            text = text.split('\n')[e.line - 1]
            
        else:
            text = Parser.getText(ctx)
        
        logging.critical(text)
        marker = (' ' * e.col) + '^'
        logging.critical(marker)
        raise e

# Overrides the HqlVisitor templates
# If not defined here, each node only returns its children.
class Visitor(ParseOperators, ParseFunctions, ParseLogic, ParseBaseExpressions, HqlVisitor):
    def __init__(self, filename:str):
        self.filename = filename
    
    def visitQuery(self, ctx: HqlParser.QueryContext):
        statements = []
        for i in ctx.Statements:
            statements.append(self.visit(i))
                
        return Query(statements)
    
    def visitQueryStatement(self, ctx: HqlParser.QueryStatementContext):
        expr = self.visit(ctx.Expression)
        
        if not expr:
            raise hqle.ParseException(
                'Query statement given None',
                ctx.start.line,
                ctx.start.column 
            )
        
        statement = QueryStatement(expr)
        
        return statement

    def visitPipeExpression(self, ctx: HqlParser.PipeExpressionContext):
        from Hql.Expressions import PipeExpression
        from Hql.Operators import PrePipe
        
        prepipe = PrePipe(self.visit(ctx.Expression))
        pipes = self.visit(ctx.PipedOperators)
        
        return PipeExpression(prepipe, pipes)

    def visitEmptyPipedExpression(self, ctx: HqlParser.EmptyPipedExpressionContext):
        pipes = []
        for i in ctx.Operators:
            try:
                pipes.append(self.visit(i))
            except hqle.ParseException as e:
                e.filename = self.filename
                Parser.handleException(i, e)
        return pipes

    def visitLetVariableDeclaration(self, ctx: HqlParser.LetVariableDeclarationContext):
        name = self.visit(ctx.Name)
        value = self.visit(ctx.Expression)
        return LetStatement(name, value, 'variable')

    def visitLetMacroDeclaration(self, ctx: HqlParser.LetMacroDeclarationContext):
        name = self.visit(ctx.Name)
        pipes = self.visit(ctx.Pipes)
        return LetStatement(name, pipes, 'macro')
