from HqlCompiler.grammar.HqlVisitor import HqlVisitor
from HqlCompiler.grammar.HqlParser import HqlParser

import HqlCompiler.Expression as Expr
import HqlCompiler.Operators as Ops

from HqlCompiler.Exceptions import *

class Operators(HqlVisitor):
    def __init__(self):
        pass
    
    def visitStrictQueryOperatorParameter(self, ctx: HqlParser.StrictQueryOperatorParameterContext):
        name = ctx.NameToken.text
        value = self.visit(ctx.NameValue) if ctx.NameValue else self.visit(ctx.LiteralValue)
        
        return Expr.OpParameter(name, value)

    def visitRelaxedQueryOperatorParameter(self, ctx: HqlParser.RelaxedQueryOperatorParameterContext):
        name = ctx.NameToken.text

        if ctx.NameValue:
            value = self.visit(ctx.NameValue)
        else:
            value = self.visit(ctx.LiteralValue)
        
        return Expr.OpParameter(name, value)
    
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

    def visitProjectAwayOperator(self, ctx: HqlParser.ProjectAwayOperatorContext):
        exprs = []
        for i in ctx.Columns:
            exprs.append(self.visit(i))
        
        return Ops.ProjectAway(exprs)
    
    def visitProjectKeepOperator(self, ctx: HqlParser.ProjectKeepOperatorContext):
        exprs = []
        for i in ctx.Columns:
            exprs.append(self.visit(i))
        
        return Ops.ProjectKeep(exprs)

    def visitProjectRenameOperator(self, ctx: HqlParser.ProjectRenameOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Ops.ProjectRename(exprs)
    
    def visitProjectReorderOperator(self, ctx: HqlParser.ProjectReorderOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Ops.ProjectReorder(exprs)
        
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
        tables = self.visit(ctx.OnClause) if ctx.OnClause else [Expr.Wildcard('*')]
        
        return Ops.Unnest(field, tables)
    
    def visitUnnestOperatorOnClause(self, ctx: HqlParser.UnnestOperatorOnClauseContext):
        return [self.visit(x) for x in ctx.Expressions]

    def visitSummarizeOperator(self, ctx: HqlParser.SummarizeOperatorContext):
        by = None
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
                
        if ctx.ByClause:
            by = self.visit(ctx.ByClause)
        
        return Ops.Summarize(exprs, by)
    
    def visitSummarizeOperatorByClause(self, ctx: HqlParser.SummarizeOperatorByClauseContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Expr.ByExpression(exprs)

    def visitDataTableExpression(self, ctx: HqlParser.DataTableExpressionContext):
        schema = self.visit(ctx.Schema)
        values = []
        for i in ctx.Values:
            values.append(self.visit(i))
        
        return Ops.Datatable(schema, values)
    
    def visitRowSchema(self, ctx: HqlParser.RowSchemaContext):
        schema = []
        for i in ctx.Columns:
            schema.append(self.visit(i))
        
        return schema
    
    def visitRowSchemaColumnDeclaration(self, ctx: HqlParser.RowSchemaColumnDeclarationContext):
        name = self.visit(ctx.Name)
        t = self.visit(ctx.Type)
        
        return [name, t]

    def visitJoinOperator(self, ctx: HqlParser.JoinOperatorContext):
        table = self.visit(ctx.Table)
        on = None
        where = None
        
        params = []
        for i in ctx.Parameters:
            params.append(self.visit(i))
        
        if ctx.OnClause:
            on = self.visit(ctx.OnClause)
        
        if ctx.WhereClause:
            where = self.visit(ctx.WhereClause)
        
        return Ops.Join(table, params, on=on, where=where)
    
    def visitJoinOperatorOnClause(self, ctx: HqlParser.JoinOperatorOnClauseContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
            
        return exprs
            
    def visitJoinOperatorWhereClause(self, ctx: HqlParser.JoinOperatorWhereClauseContext):
        return self.visit(ctx.Predicate)

    def visitMvexpandOperator(self, ctx: HqlParser.MvexpandOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        if ctx.LimitClause:
            limit = self.visit(ctx.LimitClause)
        else:
            limit = Expr.Integer('2147483647')
        
        return Ops.MvExpand(exprs, limit)
    
    def visitMvexpandOperatorExpression(self, ctx: HqlParser.MvexpandOperatorExpressionContext):
        expr = self.visit(ctx.Expression)
        
        if ctx.ToClause:
            to = self.visit(ctx.ToClause)
        else:
            to = None

        return Expr.ToExpression(expr, to)
    
    def visitMvapplyOperatorExpressionToClause(self, ctx: HqlParser.MvapplyOperatorExpressionToClauseContext):
        return self.visit(ctx.Type)

    def visitMvapplyOperatorLimitClause(self, ctx: HqlParser.MvapplyOperatorLimitClauseContext):
        return self.visit(ctx.LimitValue)
