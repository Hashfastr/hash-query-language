from .grammar.HqlVisitor import HqlVisitor
from .grammar.HqlParser import HqlParser

import Hql.Expressions as Expr

from Hql.Exceptions import HqlExceptions as hqle

class Logic(HqlVisitor):
    def __init__(self):
        pass
    
    def visitEqualsEqualityExpression(self, ctx: HqlParser.EqualsEqualityExpressionContext):
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        expr = Expr.Equality(
            ctx.OperatorToken.text,
            self.visit(ctx.Left),
            self.visit(ctx.Right)
        )
                
        return expr

    def visitRelationalExpression(self, ctx: HqlParser.RelationalExpressionContext):
        # Pass through in case we're doing stupid shit
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        expr = Expr.Relational(
            ctx.OperatorToken.text,
            self.visit(ctx.Left),
            self.visit(ctx.Right)
        )

        return expr
    
    def visitBetweenEqualityExpression(self, ctx: HqlParser.BetweenEqualityExpressionContext):
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        start = self.visit(ctx.Expressions[0])
        end = self.visit(ctx.Expressions[1])

        expr = Expr.BetweenEquality(
            self.visit(ctx.Left),
            start,
            end,
            ctx.OperatorToken.text
        )
        
        return expr
    
    def visitLogicalOrExpression(self, ctx: HqlParser.LogicalOrExpressionContext):
        left = self.visit(ctx.Left)
        right = []

        if len(ctx.Operations) == 0:
            return left
        
        for i in ctx.Operations:
            right.append(self.visit(i))
                        
        if len(right) == 0:
            return left
        
        expr = Expr.BinaryLogic(
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

        if len(ctx.Operations) == 0:
            return left
        
        for i in ctx.Operations:
            right.append(self.visit(i))
                        
        if len(right) == 0:
            return left
        
        expr = Expr.BinaryLogic(
            left,
            right,
            'and'
        )
        
        return expr
    
    def visitLogicalAndOperation(self, ctx: HqlParser.LogicalAndOperationContext):
        return self.visit(ctx.Right)        

    def visitParenthesizedExpression(self, ctx: HqlParser.ParenthesizedExpressionContext):
        return self.visit(ctx.Expression)

    def visitListEqualityExpression(self, ctx: HqlParser.ListEqualityExpressionContext):
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        lh = self.visit(ctx.Left)
        token = ctx.OperatorToken.text
        
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Expr.ListEquality(lh, token, exprs)

    def visitStringBinaryOperator(self, ctx: HqlParser.StringBinaryOperatorContext):
        if not ctx.OperatorToken:
            raise hqle.CompilerException('String Binary Operator has no Operator, wut')

        return ctx.OperatorToken.text

    def visitStringBinaryOperatorExpression(self, ctx: HqlParser.StringBinaryOperatorExpressionContext):
        if not ctx.Right:
            return self.visit(ctx.Left)

        lh = self.visit(ctx.Left)
        rh = self.visit(ctx.Right)

        if ctx.Operator:
            op = self.visit(ctx.Operator)

        elif ctx.HasOperator:
            op = ctx.HasOperator.text

        else:
            raise hqle.ParseException('String Binary Operator has no Operator, wut?', ctx)
        
        if op in ('=~', '!~'):
            return Expr.InsensitiveStringCmp(lh, op, rh)

        return Expr.Contains(lh, op, rh)
