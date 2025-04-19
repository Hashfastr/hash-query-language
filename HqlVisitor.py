from grammar.HqlParser import HqlParser
from grammar.HqlVisitor import HqlVisitor
from antlr4.tree.Tree import TerminalNodeImpl

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
            
        return Expression.ScopedNameReference(name, scope)
    
    def visitWhereOperator(self, ctx: HqlParser.WhereOperatorContext):
        operator = Operator.Where()
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            
            # Skip operator names, commas, etc
            if type(child) == TerminalNodeImpl:
                continue
            
            index = child.getRuleIndex()
            
            if HqlParser.ruleNames[index] == "namedExpression":
                operator.expressions.append(self.visit(ctx.getChild(i)))
        
        return operator

    def visitProjectOperator(self, ctx: HqlParser.ProjectOperatorContext):
        operator = Operator.Project()
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            
            # Skip operator names, commas, etc
            if type(child) == TerminalNodeImpl:
                continue

            index = child.getRuleIndex()
            
            if HqlParser.ruleNames[index] == "namedExpression":
                operator.expressions.append(self.visit(ctx.getChild(i)))

        return operator
            
    
    def visitEqualsEqualityExpression(self, ctx: HqlParser.EqualsEqualityExpressionContext):       
        expression = Expression.Equality()
        
        expression.expressions.append(self.visit(ctx.getChild(0)))
        expression.type = self.visit(ctx.getChild(1))
        expression.expressions.append(self.visit(ctx.getChild(2)))
            
        return expression
    
    def visitRelationalExpression(self, ctx: HqlParser.RelationalExpressionContext):
        return self.visit(ctx.getChild(0))
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        return ctx.getText()
    
    def visitStringLiteralExpression(self, ctx: HqlParser.StringLiteralExpressionContext):
        return Expression.StringLiteral(ctx.getText())

    def visitLongLiteralExpression(self, ctx: HqlParser.LongLiteralExpressionContext):
        return Expression.Integer(ctx.getText())

    def visitTerminal(self, node):
        return node.getText()