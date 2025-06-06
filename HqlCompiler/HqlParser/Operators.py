from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser

import HqlCompiler.Expression as Expression
import HqlCompiler.Operators as Ops

from HqlCompiler.Exceptions import *

class Operators(HqlVisitor):
    def __init__(self):
        pass
    
    def visitStrictQueryOperatorParameter(self, ctx: HqlParser.StrictQueryOperatorParameterContext):
        name = ctx.NameToken.text
        value = self.visit(ctx.NameValue) if ctx.NameValue else self.visit(ctx.LiteralValue)
        
        return Expression.OpParameter(name, value)
    
    def visitWhereOperator(self, ctx: HqlParser.WhereOperatorContext):
        predicate = self.visit(ctx.Predicate)
                
        params = []
        for i in ctx.Parameters:
            params.append(self.visit(i))
            
        return Ops.Where(predicate, params)

    def visitTakeOperator(self, ctx: HqlParser.TakeOperatorContext):
        limit = self.visit(ctx.Limit)
        
        tables = []
        for i in ctx.Tables:
            tables.append(self.visit(i))
        
        return Ops.Take(limit, tables)

    def visitCountOperator(self, ctx: HqlParser.CountOperatorContext):
        name = self.visit(ctx.Name) if ctx.Name else None
        
        return Ops.Count(name)
    
    def visitProjectOperator(self, ctx: HqlParser.ProjectOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Ops.Project(exprs)

    def visitExtendOperator(self, ctx: HqlParser.ExtendOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
            
        return Ops.Extend(exprs)

    def visitRangeExpression(self, ctx: HqlParser.RangeExpressionContext):
        rangeexpr = Ops.Range(
            self.visit(ctx.Expression),
            self.visit(ctx.FromExpression),
            self.visit(ctx.ToExpression),
            self.visit(ctx.StepExpression)
        )
        
        return rangeexpr

    def visitTopOperator(self, ctx: HqlParser.TopOperatorContext):
        expr = Ops.Top(
            self.visit(ctx.Expression),
            self.visit(ctx.ByExpression)
        )
        
        return expr

    def visitUnnestOperator(self, ctx: HqlParser.UnnestOperatorContext):
        field = self.visit(ctx.Field)
        tables = self.visit(ctx.OnClause)
        
        return Ops.Unnest(field, tables)
    
    def visitUnnestOperatorOnClause(self, ctx: HqlParser.UnnestOperatorOnClauseContext):
        return [self.visit(x) for x in ctx.Expressions]