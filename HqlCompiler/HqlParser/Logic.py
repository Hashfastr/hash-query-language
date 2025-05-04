from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser

import HqlCompiler.Expression as Expression

from HqlCompiler.Exceptions import *

import logging

class Logic(HqlVisitor):
    def __init__(self):
        pass
    
    def visitEqualsEqualityExpression(self, ctx: HqlParser.EqualsEqualityExpressionContext):
        expr = Expression.Equality(
            ctx.OperatorToken.text,
            self.visit(ctx.Left),
            self.visit(ctx.Right)
        )
                
        return expr