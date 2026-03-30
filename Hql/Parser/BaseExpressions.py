from .grammar.HqlVisitor import HqlVisitor
from .grammar.HqlParser import HqlParser

import Hql.Expressions as Expr
from Hql.Exceptions import HqlExceptions as hqle

class BaseExpressions(HqlVisitor):
    def __init__(self):
        pass
    
    '''
    Name references
    
    Not values, but references to values such as columns and tables.
    '''

    def visitEscapedName(self, ctx: HqlParser.EscapedNameContext):
        # Probably need to unescape these eventually
        literal = self.visit(ctx.StringLiteral)
        return Expr.EscapedNamedReference(literal.quote(''))

    def visitWildcardedName(self, ctx: HqlParser.WildcardedNameContext):
        if ctx.Star:
            txt = ctx.Star.getText()
        elif ctx.Name:
            txt = ctx.Name.getText()
        else:
            raise hqle.ParseException("Wildcarded name given nothing", ctx)
        return Expr.Wildcard(txt)
    
    def visitKeywordName(self, ctx: HqlParser.KeywordNameContext):
        if ctx.Token == None:
            raise hqle.ParseException('Keyword has no string token', ctx)
        return Expr.NamedReference(ctx.Token.text)
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        if ctx.Token == None:
            raise hqle.ParseException('Identifier has no string token', ctx)
        return Expr.NamedReference(ctx.Token.text)
    
    def visitNamedExpression(self, ctx: HqlParser.NamedExpressionContext):
        if not ctx.Name:
            return self.visit(ctx.Expression)
                
        names = self.visit(ctx.Name)
        value = self.visit(ctx.Expression)
        return Expr.NamedExpression(names, value)
    
    def visitNamedExpressionNameClause(self, ctx: HqlParser.NamedExpressionNameClauseContext):
        return [self.visit(ctx.Name)] if ctx.Name else self.visit(ctx.NameList)
        
    def visitNamedExpressionNameList(self, ctx: HqlParser.NamedExpressionNameListContext):
        return [self.visit(x) for x in ctx.Names]
    
    def visitPathReference(self, ctx: HqlParser.PathReferenceContext):
        parts = [self.visit(x) for x in ctx.Parts]
        return Expr.Path(parts)

    '''
    Individual constant values
    
    Strings
    Longs
    Bools
    Ints
    '''
    
    def visitStringLiteralExpression(self, ctx: HqlParser.StringLiteralExpressionContext):
        import re

        parts = []
        for i in ctx.Tokens:
            cur = i.text
            verbatim = False
            obfuscated = False

            if i.text[0] in ('h', 'H'):
                cur = cur[1:]
                obfuscated = True

            if i.text[0] == '@':
                cur = cur[1:]
                verbatim = True
                
            if i.text[:3] == '"""' or i.text[:3] == "'''":
                verbatim = True

            if not verbatim:
                cur = eval(cur)
                assert isinstance(cur, str)
                cur = cur.encode('utf-8')

            else:
                if i.text[:3] == '"""' or i.text[:3] == "'''":
                    quote = i.text[:3]
                    cur = cur[3:-3]
                else:
                    quote = cur[0]
                    cur = cur[1:-1]

                # unescape any quotes
                old = ''.join([fr'\{x}' for x in quote])
                cur = re.sub(old, quote, cur).encode('utf-8')

            parts.append(Expr.StringLiteral(cur, verbatim=verbatim, obfuscated=obfuscated))

        if len(parts) == 1:
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

    def visitDateTimeLiteralExpression(self, ctx: HqlParser.DateTimeLiteralExpressionContext):
        import re

        if ctx.Token == None:
            raise hqle.ParseException('DatetimeLiteral has no string token', ctx)

        datestr = re.findall(r'datetime\([\'"]?([^\)]+)[\'"]?\)', ctx.Token.text)[0]
        lit = Expr.StringLiteral(datestr)

        return Expr.Datetime(lit)
    
    '''
    Sort specific
    '''
    
    def visitOrderedExpression(self, ctx: HqlParser.OrderedExpressionContext):
        order = ctx.OrderKind.text if ctx.OrderKind else 'desc'
        nulls = ctx.NullsKind.text if ctx.NullsKind else ''
        expr = self.visit(ctx.Expression)

        return Expr.OrderedExpression(expr, order=order, nulls=nulls)

    def visitScalarType(self, ctx: HqlParser.ScalarTypeContext):
        if ctx.Token == None:
            raise hqle.ParseException('ScalarType has no string token', ctx)
        return Expr.TypeExpression(ctx.Token.text)

    def visitStaticNamedExpression(self, ctx: HqlParser.StaticNamedExpressionContext):
        name = self.visit(ctx.Name)
        value = self.visit(ctx.Value)
        return Expr.NamedExpression([name], value)
