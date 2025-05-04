from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser
from antlr4.tree.Tree import TerminalNodeImpl

import HqlCompiler.Expression as Expression

from HqlCompiler.Exceptions import *

import logging

class Functions(HqlVisitor):
    def __init__(self):
        pass
    
    def visitFunctionCallOrPathPathExpression(self, ctx: HqlParser.FunctionCallOrPathPathExpressionContext):
        path = Expression.Path()
        
        expr = self.visit(ctx.Expression)
        if expr == None:
            logging.error('Path expression given NoneType root expression')
            raise SemanticException(
                'NoneType root path expression',
                ctx.start.line,
                ctx.start.column
            )
                
        # Get the root item
        path.path.append(expr)
        
        for i in ctx.Operations:
            path.path.append(self.visit(i))
        
        return path
    
    def visitNamedFunctionCallExpression(self, ctx: HqlParser.NamedFunctionCallExpressionContext):
        expr = Expression.Function(self.visit(ctx.Name))
        
        for i in ctx.Arguments:
            expr.args.append(self.visit(i))
        
        return expr
    
    def visitDotCompositeFunctionCallExpression(self, ctx: HqlParser.DotCompositeFunctionCallExpressionContext):
        funcs = [self.visit(ctx.Call)]
                
        for i in ctx.Operations:
            funcs.append(self.visit(i))
        
        return Expression.DotCompositeFunction(funcs)