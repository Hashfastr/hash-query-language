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
    
    def visitBetweenEqualityExpression(self, ctx: HqlParser.BetweenEqualityExpressionContext):
        expr = Expression.BetweenEquality(
            self.visit(ctx.Left),
            self.visit(ctx.StartExpression),
            self.visit(ctx.EndExpression),
            ctx.OperatorToken.text
        )
        
        return expr
    
    def visitLogicalOrExpression(self, ctx: HqlParser.LogicalOrExpressionContext):
        left = self.visit(ctx.Left)
        right = []
        
        for i in ctx.Operations:
            right.append(self.visit(i))
                        
        if len(right) == 0:
            return left
        
        expr = Expression.BinaryLogic(
            left,
            right,
            'or'
        )
        
        return expr
    
    def visitLogicalOrOperation(self, ctx: HqlParser.LogicalOrOperationContext):
        return self.visit(ctx.Right)

    def visitLogicalAndExpression(self, ctx: HqlParser.LogicalAndExpressionContext):
        left = self.visit(ctx.Left)
        right = []
        
        for i in ctx.Operations:
            right.append(self.visit(i))
                        
        if len(right) == 0:
            return left
        
        expr = Expression.BinaryLogic(
            left,
            right,
            'and'
        )
        
        return expr
    
    def visitLogicalAndOperation(self, ctx: HqlParser.LogicalAndOperationContext):
        return self.visit(ctx.Right)        

    def visitParenthesizedExpression(self, ctx: HqlParser.ParenthesizedExpressionContext):
        return self.visit(ctx.Expression)