from antlr4 import *
from HqlCompiler.Exceptions import *
from HqlCompiler.grammar.HqlLexer import HqlLexer
from HqlCompiler.grammar.HqlParser import HqlParser
from HqlCompiler.grammar.HqlVisitor import HqlVisitor

from HqlCompiler.Query import *
import HqlCompiler.Expression as Expression

from .BaseExpressions import BaseExpressions
from .Functions import Functions
from .Operators import Operators
from .Logic import Logic

import time
import logging

class Parser():
    def __init__(self, filename:str):
        self.tree = self.parse_file(filename)
    
    def parse_file(self, filename:str) -> CommonTokenStream:
        try:
            with open(filename, 'r') as f:
                text = f.read()
        except Exception as e:
            logging.error(f"Failed to open file {filename}")
            logging.error(str(e))
            raise e
        
        lexer = HqlLexer(InputStream(text))
        token_stream = CommonTokenStream(lexer)
        parser = HqlParser(token_stream)
        
        return parser.query()

    def assemble(self):
        visitor = Visitor()
        self.assembly = visitor.visit(self.tree)
        
        if self.assembly == None:
            logging.error("Compiler error!")
            logging.error("Parser returned None instead of valid assembly")
            logging.error("Import error?")
            raise Exception("Compiler error, visitor returned None")
        

# Overrides the HqlVisitor templates
# If not defined here, each node only returns its children.
class Visitor(Operators, Functions, Logic, BaseExpressions, HqlVisitor):
    def __init__(self):
        pass
    
    def visitQuery(self, ctx: HqlParser.QueryContext):
        query = Query()
        
        # -1 to handle EOF node
        for i in range(ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            query.statements.append(self.visit(child))
                
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
        prepipe = self.visit(ctx.Expression)
        
        pipes = []
        for i in ctx.PipedOperators:
            pipes.append(self.visit(i))

        if pipes == []:
            return prepipe
        
        return Expression.PipeExpression(prepipe=prepipe, pipes=pipes)