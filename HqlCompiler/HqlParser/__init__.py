from antlr4 import *
from HqlCompiler.Exceptions import *
from HqlCompiler.grammar.HqlLexer import HqlLexer
from HqlCompiler.grammar.HqlParser import HqlParser
from HqlCompiler.grammar.HqlVisitor import HqlVisitor

from HqlCompiler.Query import Query, Statement
from HqlCompiler.Operators import Operator
from HqlCompiler.Operators.Index import Index

from .BaseExpressions import BaseExpressions

import time
import logging

class Parser():
    def __init__(self, filename:str):
        self.tree = self.parse_file(filename)
    
    def parse_file(self, filename:str) -> CommonTokenStream:
        start = time.perf_counter()
        
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
        
        end = time.perf_counter()
        logging.debug(f'Parsing took {end - start}')
        
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
class Visitor(BaseExpressions, HqlVisitor):
    def __init__(self):
        pass
    
    def visitQuery(self, ctx: HqlParser.QueryContext):
        query = Query()
        
        # -1 to handle EOF node
        for i in range(ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            query.statements.append(self.visit(child))
                
        return query
    
    def visitStatement(self, ctx: HqlParser.StatementContext):
        statement = Statement()
        
        statement.operations = self.visit(ctx.getChild(0))
        
        if statement.operations == None:
            raise SemanticException(
                'Statement has no operations, given None',
                ctx.start.line,
                ctx.start.column
            )

        if not isinstance(statement.operations, list):
            logging.error(type(statement.operations))
            raise SemanticException(
                'Statement given a non-list of operations',
                ctx.start.line,
                ctx.start.column
            )
            
        if not isinstance(statement.operations[0], Operator):
            logging.error([type(x) for x in statement.operations])
            raise SemanticException(
                'Statement given list of non-Operators',
                ctx.start.line,
                ctx.start.column
            )
        
        return statement

    def visitPipeExpression(self, ctx: HqlParser.PipeExpressionContext):
        operators = [Index(self.visit(ctx.Expression))]
        
        for i in ctx.PipedOperators:
            operators.append(self.visit(i))
        
        return operators