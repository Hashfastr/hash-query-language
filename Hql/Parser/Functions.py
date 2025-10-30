from .grammar.HqlVisitor import HqlVisitor
from .grammar.HqlParser import HqlParser

from Hql.Exceptions import HqlExceptions as hqle

import logging

class Functions(HqlVisitor):
    def __init__(self):
        pass
    
    def visitFunctionCallOrPathPathExpression(self, ctx: HqlParser.FunctionCallOrPathPathExpressionContext):
        from Hql.Expressions import Path
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
    
    def visitNamedFunctionCallExpression(self, ctx: HqlParser.NamedFunctionCallExpressionContext):
        from Hql.Expressions import FuncExpr
        expr = FuncExpr(self.visit(ctx.Name))
        
        for i in ctx.Arguments:
            expr.args.append(self.visit(i))
        
        return expr
    
    def visitDotCompositeFunctionCallExpression(self, ctx: HqlParser.DotCompositeFunctionCallExpressionContext):
        from Hql.Expressions import DotCompositeFunction
        funcs = [self.visit(ctx.Call)]
                
        for i in ctx.Operations:
            funcs.append(self.visit(i))
        
        return DotCompositeFunction(funcs)
    
    def visitCountExpression(self, ctx: HqlParser.CountExpressionContext):
        from Hql.Expressions import Identifier, FuncExpr
        name = Identifier('count')
        return FuncExpr(name, args=[])
