from .grammar.HqlVisitor import HqlVisitor
from .grammar.HqlParser import HqlParser

import Hql.Expressions as Expr
from Hql.Types.Hql import HqlTypes as hqlt

from Hql.Exceptions import HqlExceptions as hqle

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
        assert ctx.Name != None
        return Expr.Wildcard(ctx.Name.getText())

        # prefix = self.visit(ctx.Prefix) if ctx.Prefix else ''
        # segments = []
        # for i in ctx.Segments:
        #     segments.append(self.visit(i))
        #
        # name = prefix + '*' + ''.join(segments)
        #
        # return Expr.Wildcard(name)
    
    # def visitWildcardedNamePrefix(self, ctx: HqlParser.WildcardedNamePrefixContext):
    #     if ctx.Identifier:
    #         return ctx.getText()
    #
    #     if ctx.Keyword:
    #         return self.visit(ctx.Keyword)
    #
    #     if ctx.ExtendedKeyword:
    #         return self.visit(ctx.ExtendedKeyword)
        
    def visitKeywordName(self, ctx: HqlParser.KeywordNameContext):
        if ctx.Token == None:
            raise hqle.ParseException('Keyword has no string token', ctx)

        return Expr.Keyword(ctx.Token.text)
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        if ctx.Token == None:
            raise hqle.ParseException('Identifier has no string token', ctx)

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
    
    def visitPathReference(self, ctx: HqlParser.PathReferenceContext):
        parts = []
        
        for i in ctx.Parts:
            parts.append(self.visit(i))

        if len(parts) == 1:
            return parts[0]
        return Expr.Path(parts)

    '''
    Individual constant values
    
    Strings
    Longs
    Bools
    Ints
    '''
    def visitStringLiteralExpression(self, ctx: HqlParser.StringLiteralExpressionContext):
        parts = []
        
        # how do you handle multiple tokens in a string literal? Unsure.
        # Just quits after the one
        for i in ctx.Tokens:
            cur = i.text
            lquote = ''
            rquote = ''
            if i.text[0] in ('h', 'H'):
                lquote += 'h'
                cur = cur[1:]

            if i.text[0] == '@':
                lquote += '@'
                cur = cur[1:]

            if i.text[:3] == '```' or i.text[:3] == '~~~':
                lquote += i.text[:3]
                rquote = i.text[:3]
                cur = cur[3:-3]
            else:
                lquote += cur[0]
                rquote = cur[0]
                cur = cur[1:-1]

            parts.append(Expr.StringLiteral(cur, lquote=lquote, rquote=rquote))

        if len(parts) == 0:
            return parts[0]
        else:
            return Expr.MultiString(parts)

    def visitLongLiteralExpression(self, ctx: HqlParser.LongLiteralExpressionContext):
        if ctx.Token == None:
            raise hqle.ParseException('LongLiteral has no string token', ctx)

        return Expr.Integer(ctx.Token.text)
    
    def visitBooleanLiteralExpression(self, ctx: HqlParser.BooleanLiteralExpressionContext):
        if ctx.Token == None:
            raise hqle.ParseException('BooleanLiteral has no string token', ctx)

        return Expr.Bool(ctx.Token.text)

    def visitRealLiteralExpression(self, ctx: HqlParser.RealLiteralExpressionContext):
        if ctx.Token == None:
            raise hqle.ParseException('RealLiteral has no string token', ctx)

        return Expr.Float(ctx.Token.text)

    def visitOrderedExpression(self, ctx: HqlParser.OrderedExpressionContext):
        expr = self.visit(ctx.Ordering)
        expr.expr = self.visit(ctx.Expression)
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
        if ctx.Token == None:
            raise hqle.ParseException('ScalarType has no string token', ctx)
        return Expr.TypeExpression(ctx.Token.text)

    def visitStaticNamedExpression(self, ctx: HqlParser.StaticNamedExpressionContext):
        name = self.visit(ctx.Name)
        value = self.visit(ctx.Value)
        return Expr.NamedExpression([name], value)
