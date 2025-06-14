from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser

import HqlCompiler.Expression as Expr
from HqlCompiler.Types.Hql import HqlTypes as hqlt

from HqlCompiler.Exceptions import *

import logging

class BaseExpressions(HqlVisitor):
    def __init__(self):
        pass
    
    '''
    Name references
    
    Not values, but references to values such as columns and tables.
    '''
    def visitNameReferenceWithDataScope(self, ctx: HqlParser.NameReferenceWithDataScopeContext):
        name = self.visit(ctx.Name)
        #name.scope = self.visit(ctx.Scope)
        return name
    
    def visitEscapedName(self, ctx: HqlParser.EscapedNameContext):
        # Probably need to unescape these eventually
        literal = self.visit(ctx.StringLiteral)
        return Expr.EscapedNamedReference(literal.value)

    def visitWildcardedName(self, ctx: HqlParser.WildcardedNameContext):
        prefix = self.visit(ctx.Prefix) if ctx.Prefix else ''
        segments = []
        for i in ctx.Segments:
            segments.append(self.visit(i))

        name = prefix + '*' + ''.join(segments)
        
        return Expr.Wildcard(name)
    
    def visitWildcardedNamePrefix(self, ctx: HqlParser.WildcardedNamePrefixContext):
        if ctx.Identifier:
            return ctx.getText()
        
        if ctx.Keyword:
            return self.visit(ctx.Keyword)
        
        if ctx.ExtendedKeyword:
            return self.visit(ctx.ExtendedKeyword)
        
    def visitKeywordName(self, ctx: HqlParser.KeywordNameContext):
        return Expr.Keyword(ctx.Token.text)
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        return Expr.Identifier(ctx.Token.text)
    
    '''
    Variable assignment, i.e. an expression given a name
    
    foo=toint(bar)
    '''
    def visitNamedExpression(self, ctx: HqlParser.NamedExpressionContext):
        if not ctx.Name:
            return self.visit(ctx.Expression)
                
        names = self.visit(ctx.Name)
        value = self.visit(ctx.Expression)
                
        return Expr.NamedExpression(names, value)
    
    def visitNamedExpressionNameClause(self, ctx: HqlParser.NamedExpressionNameClauseContext):
        if ctx.Name:
            return [self.visit(ctx.Name)]
        else:
            return self.visit(ctx.NameList)
        
    def visitNamedExpressionNameList(self, ctx: HqlParser.NamedExpressionNameListContext):
        names = []
        for name in ctx.Names:
            names.append(self.visit(name))
            
        return names

    '''
    Individual constant values
    
    Strings
    Longs
    Bools
    Ints
    '''
    def visitStringLiteralExpression(self, ctx: HqlParser.StringLiteralExpressionContext):
        text = ""
        
        # how do you handle multiple tokens in a string literal? Unsure.
        # Just quits after the one
        for i in ctx.Tokens:
            text += i.text.strip("\"").strip('\'')
            break
        
        return Expr.StringLiteral(text)

    def visitLongLiteralExpression(self, ctx: HqlParser.LongLiteralExpressionContext):
        return Expr.Integer(ctx.Token.text)
    
    def visitBooleanLiteralExpression(self, ctx: HqlParser.BooleanLiteralExpressionContext):
        return Expr.Bool(ctx.Token.text)

    def visitOrderedExpression(self, ctx: HqlParser.OrderedExpressionContext):
        expr = self.visit(ctx.Ordering)
        expr.name = self.visit(ctx.Expression)
        return expr
    
    '''
    Sort specific
    '''
    
    def visitSortOrdering(self, ctx: HqlParser.SortOrderingContext):
        order = 'desc'
        nulls = 'last'
        
        if ctx.OrderKind:
            order = ctx.OrderKind.text
        
        if ctx.NullsKind:
            nulls = ctx.NullsKind.text
        
        expr = Expr.OrderedExpression(order=order, nulls=nulls)
        return expr

    def visitScalarType(self, ctx: HqlParser.ScalarTypeContext):
        return hqlt.from_name(ctx.Token.text)()