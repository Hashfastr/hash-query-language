from Hql.Parser.grammar.HqlVisitor import HqlVisitor
from Hql.Parser.grammar.HqlParser import HqlParser

from Hql.Exceptions import HqlExceptions as hqle

import logging

class Functions(HqlVisitor):
    def __init__(self):
        pass
    
    '''
    Couldn't remember what this does but it handles paths with function calls and namedreferences in it

    myfunc().Name
    '''
    def visitFunctionCallOrPathPathExpression(self, ctx: HqlParser.FunctionCallOrPathPathExpressionContext):
        from Hql.Expressions.References import Path
        path = []
        
        expr = self.visit(ctx.Expression)
        if expr == None:
            logging.error('Path expression given NoneType root expression')
            raise hqle.SemanticException(
                'NoneType root path expression',
                ctx.start.line,
                ctx.start.column
            )
                
        path.append(expr)
        for i in ctx.Operations:
            path.append(self.visit(i))
        
        return Path(path)
    
    '''
    The basic function call
    '''
    def visitFunctionCallExpression(self, ctx: HqlParser.FunctionCallExpressionContext):
        from Hql.Expressions.Functions import FuncExpr
        expr = FuncExpr(self.visit(ctx.Name))
        
        for i in ctx.Arguments:
            expr.args.append(self.visit(i))
        
        return expr
    
    '''
    Pure path of functions
    '''
    def visitDotCompositeFunctionCallExpression(self, ctx: HqlParser.DotCompositeFunctionCallExpressionContext):
        from Hql.Expressions.Functions import DotFuncExpr
        funcs = [self.visit(ctx.Call)]
                
        for i in ctx.Operations:
            funcs.append(self.visit(i))
        
        return DotFuncExpr(funcs)
