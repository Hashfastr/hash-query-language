from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser

import HqlCompiler.Expression as Expression

from HqlCompiler.Exceptions import *

import logging

class BaseExpressions(HqlVisitor):
    def __init__(self):
        pass
    
    def visitNameReferenceWithDataScope(self, ctx: HqlParser.NameReferenceWithDataScopeContext):
        name = self.visit(ctx.Name)
        # scope unimplemented
        expr = Expression.NamedReference(name)
        return expr
    
    def visitEscapedName(self, ctx: HqlParser.EscapedNameContext):
        # Probably need to unescape these eventually
        literal = self.visit(ctx.StringLiteral)
        expr = Expression.EscapedName(literal.value)
        return expr
    
    def visitStringLiteralExpression(self, ctx: HqlParser.StringLiteralExpressionContext):
        text = ""
        
        # how do you handle multiple tokens in a string literal? Unsure.
        # Just quits after the one
        for i in ctx.Tokens:
            text += i.text.strip("\"").strip('\'')
            break
            
        return Expression.StringLiteral(text)
    
    def visitSimpleNameReference(self, ctx: HqlParser.SimpleNameReferenceContext):
        name = self.visit(ctx.Name)
                
        if name == None:
            logging.error('None given to NamedReference, unimplemented feature?')
            raise ParseException()
        
        return Expression.NamedReference(name)
    
    def visitKeywordName(self, ctx: HqlParser.KeywordNameContext):
        return Expression.Identifier(ctx.Token.text, keyword=True)
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        return Expression.Identifier(ctx.Token.text)

    def visitLongLiteralExpression(self, ctx: HqlParser.LongLiteralExpressionContext):
        return Expression.Integer(ctx.Token.text)
    
    def visitBooleanLiteralExpression(self, ctx: HqlParser.BooleanLiteralExpressionContext):
        return Expression.Bool(ctx.Token.text)