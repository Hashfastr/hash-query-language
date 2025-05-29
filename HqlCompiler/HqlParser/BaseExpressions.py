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
        
        if isinstance(name, Expression.NamedReference):
            #name.scope = self.visit(ctx.Scope)
            return name
        
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
        
        if isinstance(name, Expression.NamedReference):
            return name
        
        return Expression.NamedReference(name)

    def visitNamedExpression(self, ctx: HqlParser.NamedExpressionContext):
        if not ctx.Name:
            return self.visit(ctx.Expression)
                
        name = self.visit(ctx.Name)
        value = self.visit(ctx.Expression)
                
        return Expression.NamedExpression(name, value)
    
    def visitNamedExpressionNameClause(self, ctx: HqlParser.NamedExpressionNameClauseContext):
        if ctx.Name:
            return self.visit(ctx.Name)
        else:
            return self.visit(ctx.NameList)
    
    def visitKeywordName(self, ctx: HqlParser.KeywordNameContext):
        return Expression.Identifier(ctx.Token.text, keyword=True)
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        return Expression.Identifier(ctx.Token.text)

    def visitLongLiteralExpression(self, ctx: HqlParser.LongLiteralExpressionContext):
        return Expression.Integer(ctx.Token.text)
    
    def visitBooleanLiteralExpression(self, ctx: HqlParser.BooleanLiteralExpressionContext):
        return Expression.Bool(ctx.Token.text)

    def visitOrderedExpression(self, ctx: HqlParser.OrderedExpressionContext):
        expr = self.visit(ctx.Ordering)
        expr.name = self.visit(ctx.Expression)
        return expr
    
    def visitSortOrdering(self, ctx: HqlParser.SortOrderingContext):
        order = 'desc'
        nulls = 'last'
        
        if ctx.OrderKind:
            order = ctx.OrderKind.text
        
        if ctx.NullsKind:
            nulls = ctx.NullsKind.text
        
        expr = Expression.OrderedExpression(order=order, nulls=nulls)
        return expr

    # def visitTableNameReference(self, ctx: HqlParser.TableNameReferenceContext):
    #     return 