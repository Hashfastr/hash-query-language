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

        op = ctx.OperatorToken.text

        expr = Expr.Equality(
            self.visit(ctx.Left),
            [self.visit(ctx.Right)],
            cs='~' not in op,
            neq='!' in op
        )

        return expr

    def visitRelationalExpression(self, ctx: HqlParser.RelationalExpressionContext):
        # Pass through in case we're doing stupid shit
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        op = ctx.OperatorToken.text

        expr = Expr.Relational(
            self.visit(ctx.Left),
            self.visit(ctx.Right),
            '>' in op,
            '=' in op
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
            neq='!' in ctx.OperatorToken.text
        )
        
        return expr
    
    def visitLogicalOrExpression(self, ctx: HqlParser.LogicalOrExpressionContext):
        exprs = [self.visit(ctx.Left)]

        for i in ctx.Operations:
            exprs.append(self.visit(i))
        
        return Expr.BinaryLogic(
            exprs,
            logic_and=False
        )
    
    def visitLogicalOrOperation(self, ctx: HqlParser.LogicalOrOperationContext):
        return self.visit(ctx.Right)

    def visitLogicalAndExpression(self, ctx: HqlParser.LogicalAndExpressionContext):
        exprs = [self.visit(ctx.Left)]

        for i in ctx.Operations:
            exprs.append(self.visit(i))
        
        return Expr.BinaryLogic(
            exprs,
            logic_and=True
        )
    
    def visitLogicalAndOperation(self, ctx: HqlParser.LogicalAndOperationContext):
        return self.visit(ctx.Right)

    def visitParenthesizedExpression(self, ctx: HqlParser.ParenthesizedExpressionContext):
        return self.visit(ctx.Expression)

    def visitListEqualityExpression(self, ctx: HqlParser.ListEqualityExpressionContext):
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        lh = self.visit(ctx.Left)
        op = ctx.OperatorToken.text
        
        rh = []
        for i in ctx.Expressions:
            rh.append(self.visit(i))

        if 'in' in op:
            return Expr.Equality(lh, rh, cs='~' not in op, neq='!' in op)
        
        return Expr.Substring(lh, rh, term='has' in op, logic_and='all' in op, cs='cs' in op)

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
            op:str = self.visit(ctx.Operator)

        elif ctx.HasOperator:
            op:str = ctx.HasOperator.text

        else:
            raise hqle.ParseException('String Binary Operator has no Operator, wut?', ctx)
        
        if op in ('=~', '!~'):
            return Expr.Equality(lh, [rh], cs=False, neq='!' in op)

        if op == 'matches regex':
            return Expr.Regex(lh, rh)

        return Expr.Substring(lh, [rh],
                              term='has' in op,
                              neq='!' in op,
                              cs='cs' in op,
                              startswith='startswith' in op or 'prefix' in op,
                              endswith='endswith' in op or 'suffix' in op
        )
