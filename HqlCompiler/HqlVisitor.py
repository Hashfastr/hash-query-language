from .grammar.HqlParser import HqlParser
from .grammar.HqlVisitor import HqlVisitor
from antlr4.tree.Tree import TerminalNodeImpl

from . import Expression
from .Exceptions import *

from . import Operators
from .Operators import Index
from .Query import Query, Statement

from .Config import Config

# Overrides the HqlVisitor templates
# If not defined here, each node only returns its children.
class Visitor(HqlVisitor):
    def __init__(self, conf_file:str):
        self.conf = Config(conf_file)
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
         
        return Index.Index(expression)
    
    def visitFunctionCallOrPathPathExpression(self, ctx: HqlParser.FunctionCallOrPathPathExpressionContext):
        path = []
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
        
            # Skip operator names, commas, etc
            if type(child) == TerminalNodeImpl:
                continue
            
            # path.append(self.visit(child))
            item = self.visit(child)
            if not issubclass(type(item), Expression.Expression):
                item = Expression.PathReference(item)
                
            path.append(item)
            
        return Expression.PathExpression(path)
        
    def visitNamedFunctionCallExpression(self, ctx: HqlParser.NamedFunctionCallExpressionContext):
        name = self.visit(ctx.getChild(0))
        args = []
        
        for i in range(1, ctx.getChildCount()):
            child = ctx.getChild(i)
        
            # Skip operator names, commas, etc
            if type(child) == TerminalNodeImpl:
                continue
            
            args.append(self.visit(child))
    
        return Expression.Function(name, args)
    
    def visitPrimaryExpression(self, ctx: HqlParser.PrimaryExpressionContext):
        expression = self.visit(ctx.getChild(0))
        return expression
        
    def visitNameReferenceWithDataScope(self, ctx: HqlParser.NameReferenceWithDataScopeContext):
        name = self.visit(ctx.getChild(0))
        escaped = False
       
        # Either we have a literal or an escaped name
        if isinstance(name, Expression.EscapedName):
            name = name.value
            escaped = True
        elif not isinstance(name, str):
            name = name.value
        
        if ctx.getChildCount() == 2:
            scope = self.visit(ctx.getChild(1))
        else:
            scope = ""
            
        return Expression.ScopedNameReference(name, escaped, scope)
    
    def visitWhereOperator(self, ctx: HqlParser.WhereOperatorContext):
        operator = Operators.Where()
        
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
        operator = Operators.Project()
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            
            # Skip operator names, commas, etc
            if type(child) == TerminalNodeImpl:
                continue

            index = child.getRuleIndex()
            
            if HqlParser.ruleNames[index] == "namedExpression":
                operator.expressions.append(self.visit(ctx.getChild(i)))

        return operator
    
    # Collects left and right hand expressions along with the type of equality.
    def visitEqualsEqualityExpression(self, ctx: HqlParser.EqualsEqualityExpressionContext):       
        expression = Expression.Equality()
        
        expression.expressions.append(self.visit(ctx.getChild(0)))
        expression.type = self.visit(ctx.getChild(1))
        expression.expressions.append(self.visit(ctx.getChild(2)))
            
        return expression

    def visitBetweenEqualityExpression(self, ctx: HqlParser.BetweenEqualityExpressionContext):
        expression = Expression.BetweenEquality()
        
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            
            # Skip operator names, commas, etc
            if type(child) == TerminalNodeImpl:
                continue
                        
            expression.expressions.append(self.visit(child))
            
        return expression
    
    def visitRelationalExpression(self, ctx: HqlParser.RelationalExpressionContext):
        return self.visit(ctx.getChild(0))
    
    def visitIdentifierName(self, ctx: HqlParser.IdentifierNameContext):
        return ctx.getText()
    
    def visitStringLiteralExpression(self, ctx: HqlParser.StringLiteralExpressionContext):
        return Expression.StringLiteral(ctx.getText())

    def visitLongLiteralExpression(self, ctx: HqlParser.LongLiteralExpressionContext):
        return Expression.Integer(ctx.getText())

    def visitEscapedName(self, ctx: HqlParser.EscapedNameContext):
        name = self.visit(ctx.getChild(1))
        return Expression.EscapedName(name.value)

    # These are nothing but plaintext strings.
    def visitTerminal(self, node):
        return node.getText()