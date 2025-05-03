from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser
from antlr4.tree.Tree import TerminalNodeImpl

import HqlCompiler.Expression as Expression

from HqlCompiler.Exceptions import *

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
        return Expression.NamedReference(self.visit(ctx.Name))
    
    def visitKeywordName(self, ctx: HqlParser.KeywordNameContext):
        return Expression.Keyword(ctx.Token.text)
