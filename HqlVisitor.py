from grammar.HqlParser import HqlParser
from grammar.HqlVisitor import HqlVisitor

import Operator
import Expression
from Query import Query, Statement

class Visitor(HqlVisitor):
    def __init__(self):
        pass
    
    def visitQuery(self, ctx: HqlParser.QueryContext):
        query = Query()
        
        # -1 to handle EOF node
        for i in range(ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            query.statements.append(self.visit(child))
            
        return query

    def visitStatement(self, ctx: HqlParser.StatementContext):
        statement = Statement()
        
        statement.operations = self.visit(ctx.getChild(0))

        return statement
    
    def visitPipeExpression(self, ctx: HqlParser.PipeExpressionContext):
        operators = []
                
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            operators.append(self.visit(child))
                
        return operators
    
    def visitBeforePipeExpression(self, ctx: HqlParser.BeforePipeExpressionContext):
        expression = self.visit(ctx.getChild(0))
        
        index = Operator.Index(expression)
        
        return index
    
    def visitPrimaryExpression(self, ctx: HqlParser.PrimaryExpressionContext):
        expression = self.visit(ctx.getChild(0))
        return expression
        
    def visitNameReferenceWithDataScope(self, ctx: HqlParser.NameReferenceWithDataScopeContext):
        name = self.visit(ctx.getChild(0))
        
        if ctx.getChildCount() == 2:
            scope = self.visit(ctx.getChild(1))
        else:
            scope = ""
            
        return Expression.scopedNameReference(name, scope)
    
    def visitAfterPipeOperator(self, ctx: HqlParser.AfterPipeOperatorContext):
        operator = Operator.Pipe()
        return operator
        
        expression = self.visit(ctx.getChild(0))
        operator.expressions.append(expression)
        
        return operator
    
    def visitWhereOperator(self, ctx: HqlParser.WhereOperatorContext):
        return []
    
    def visitEqualsEqualityExpression(self, ctx: HqlParser.EqualsEqualityExpressionContext):
        expression = Expression.Equality()
        #expression.
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        return ctx.getText()