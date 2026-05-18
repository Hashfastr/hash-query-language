from Hql.Parser.grammar.HqlVisitor import HqlVisitor
from Hql.Parser.grammar.HqlParser import HqlParser

from Hql.Exceptions import HqlExceptions as hqle

class Logic(HqlVisitor):
    def __init__(self):
        pass
    
    def visitEqualsEqualityExpression(self, ctx: HqlParser.EqualsEqualityExpressionContext):
        from Hql.Expressions.Logic import Equality

        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        op = ctx.OperatorToken.text

        expr = Equality(
            self.visit(ctx.Left),
            [self.visit(ctx.Right)],
            cs='~' not in op,
            neq='!' in op
        )

        return expr

    def visitRelationalExpression(self, ctx: HqlParser.RelationalExpressionContext):
        from Hql.Expressions.Logic import Relational

        # Pass through in case we're doing stupid shit
        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        op = ctx.OperatorToken.text

        expr = Relational(
            self.visit(ctx.Left),
            self.visit(ctx.Right),
            '>' in op,
            '=' in op
        )

        return expr
    
    def visitBetweenEqualityExpression(self, ctx: HqlParser.BetweenEqualityExpressionContext):
        from Hql.Expressions.Logic import BetweenEquality

        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        start = self.visit(ctx.Expressions[0])
        end = self.visit(ctx.Expressions[1])

        expr = BetweenEquality(
            self.visit(ctx.Left),
            start,
            end,
            neq='!' in ctx.OperatorToken.text
        )
        
        return expr
    
    def visitLogicalOrExpression(self, ctx: HqlParser.LogicalOrExpressionContext):
        from Hql.Expressions.Logic import BinaryLogic

        exprs = [self.visit(ctx.Left)]

        for i in ctx.Operations:
            exprs.append(self.visit(i))
        
        return BinaryLogic(
            exprs,
            logic_and=False
        )
    
    def visitLogicalOrOperation(self, ctx: HqlParser.LogicalOrOperationContext):
        return self.visit(ctx.Right)

    def visitLogicalAndExpression(self, ctx: HqlParser.LogicalAndExpressionContext):
        from Hql.Expressions.Logic import BinaryLogic

        exprs = [self.visit(ctx.Left)]

        for i in ctx.Operations:
            exprs.append(self.visit(i))
        
        return BinaryLogic(
            exprs,
            logic_and=True
        )
    
    def visitLogicalAndOperation(self, ctx: HqlParser.LogicalAndOperationContext):
        return self.visit(ctx.Right)

    def visitParenthesizedExpression(self, ctx: HqlParser.ParenthesizedExpressionContext):
        return self.visit(ctx.Expression)

    def visitListEqualityExpression(self, ctx: HqlParser.ListEqualityExpressionContext):
        from Hql.Expressions.Logic import Equality, Substring

        if ctx.OperatorToken == None:
            return self.visit(ctx.Left)

        lh = self.visit(ctx.Left)
        op = ctx.OperatorToken.text
        
        rh = []
        for i in ctx.Expressions:
            rh.append(self.visit(i))

        if 'in' in op:
            return Equality(lh, rh, cs='~' not in op, neq='!' in op)
        
        return Substring(lh, rh, term='has' in op, logic_and='all' in op, cs='cs' in op)

    def visitStringBinaryOperator(self, ctx: HqlParser.StringBinaryOperatorContext):
        if not ctx.OperatorToken:
            raise hqle.CompilerException('String Binary Operator has no Operator, wut')

        return ctx.OperatorToken.text

    def visitStringBinaryOperatorExpression(self, ctx: HqlParser.StringBinaryOperatorExpressionContext):
        from Hql.Expressions.Logic import Substring, Equality, Regex

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
            return Equality(lh, [rh], cs=False, neq='!' in op)

        if op == 'matches regex':
            return Regex(lh, rh)

        return Substring(
            lh, [rh],
            term='has' in op,
            neq='!' in op,
            cs='cs' in op,
            startswith='startswith' in op or 'prefix' in op,
            endswith='endswith' in op or 'suffix' in op
        )
