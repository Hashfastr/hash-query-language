from antlr4 import CommonTokenStream, InputStream
from antlr4.error.ErrorListener import ErrorListener
from HqlCompiler.Exceptions import ParseException, LexerException 
from HqlCompiler.grammar.HqlLexer import HqlLexer
from HqlCompiler.grammar.HqlParser import HqlParser
from HqlCompiler.grammar.HqlVisitor import HqlVisitor

from HqlCompiler.Query import Query, QueryStatement, LetStatement
import HqlCompiler.Expressions as Expr
import HqlCompiler.Operators as Ops

from HqlCompiler.HqlParser.BaseExpressions import BaseExpressions
from HqlCompiler.HqlParser.Functions import Functions
from HqlCompiler.HqlParser.Operators import Operators
from HqlCompiler.HqlParser.Logic import Logic

import logging

class HqlErrorListener(ErrorListener):
    def __init__(self, text:str, filename:str):
        ErrorListener.__init__(self)
        self.text = text
        self.filename = filename

    def syntaxError(self, recognizer:HqlParser, offendingSymbol, line, column, msg, e):
        e = LexerException(msg, self.text, line, column, offendingSymbol, filename=self.filename)
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
    def handleException(ctx, e:ParseException):
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

# Overrides the HqlVisitor templates
# If not defined here, each node only returns its children.
class Visitor(Operators, Functions, Logic, BaseExpressions, HqlVisitor):
    def __init__(self, filename:str):
        self.filename = filename
    
    def visitQuery(self, ctx: HqlParser.QueryContext):
        query = Query()
        
        for i in ctx.Statements:
            query.statements.append(self.visit(i))
                
        return query
    
    def visitQueryStatement(self, ctx: HqlParser.QueryStatementContext):
        expr = self.visit(ctx.Expression)
        
        if not expr:
            raise ParseException(
                'Query statement given None',
                ctx.start.line,
                ctx.start.column 
            )
        
        statement = QueryStatement(expr)
        
        return statement

    def visitPipeExpression(self, ctx: HqlParser.PipeExpressionContext):
        prepipe = Ops.PrePipe(self.visit(ctx.Expression))
        
        pipes = []
        for i in ctx.PipedOperators:
            try:
                pipes.append(self.visit(i))
            except ParseException as e:
                e.filename = self.filename
                Parser.handleException(i, e)
        
        return Expr.PipeExpression(prepipe, pipes)

    def visitLetVariableDeclaration(self, ctx: HqlParser.LetVariableDeclarationContext):
        name = self.visit(ctx.Name)
        value = self.visit(ctx.Expression)
        return LetStatement(name, value, 'variable')
