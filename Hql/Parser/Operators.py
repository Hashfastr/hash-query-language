from .grammar.HqlVisitor import HqlVisitor
from .grammar.HqlParser import HqlParser

import Hql.Expressions as Exprs
import Hql.Operators as Ops

from Hql.Exceptions import HqlExceptions as hqle

class Operators(HqlVisitor):
    def __init__(self):
        pass
    
    def visitStrictQueryOperatorParameter(self, ctx: HqlParser.StrictQueryOperatorParameterContext):
        if ctx.NameToken == None:
            raise hqle.ParseException('QueryParameter NameToken is None!', ctx)

        name = ctx.NameToken.text
        value = self.visit(ctx.NameValue) if ctx.NameValue else self.visit(ctx.LiteralValue)
        
        return Exprs.OpParameter(name, value)

    def visitRelaxedQueryOperatorParameter(self, ctx: HqlParser.RelaxedQueryOperatorParameterContext):
        if ctx.NameToken == None:
            raise hqle.ParseException('QueryParameter NameToken is None!', ctx)

        name = ctx.NameToken.text

        if ctx.NameValue:
            value = self.visit(ctx.NameValue)
        else:
            value = self.visit(ctx.LiteralValue)
        
        return Exprs.OpParameter(name, value)

    def visitRenameOperator(self, ctx: HqlParser.RenameOperatorContext):
        exprs = [self.visit(x) for x in ctx.Expressions]
        return Ops.Rename(exprs)

    def visitRenameToExpression(self, ctx: HqlParser.RenameToExpressionContext):
        src = self.visit(ctx.Source)
        dst = self.visit(ctx.Destination)
        return Exprs.ToClause(src, dst)
    
    def visitWhereOperator(self, ctx: HqlParser.WhereOperatorContext):
        predicate = self.visit(ctx.Predicate)
                
        params = []
        for i in ctx.Parameters:
            params.append(self.visit(i))

        if not predicate:
            raise hqle.ParseException('Where instanciated with None type predicate', ctx)
            
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
        
        return Ops.Project('project', exprs)

    def visitProjectAwayOperator(self, ctx: HqlParser.ProjectAwayOperatorContext):
        exprs = []
        for i in ctx.Columns:
            exprs.append(self.visit(i))
        
        return Ops.ProjectAway('project-away', exprs)
    
    def visitProjectKeepOperator(self, ctx: HqlParser.ProjectKeepOperatorContext):
        exprs = []
        for i in ctx.Columns:
            exprs.append(self.visit(i))
        
        return Ops.ProjectKeep('project-keep', exprs)

    def visitProjectRenameOperator(self, ctx: HqlParser.ProjectRenameOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Ops.ProjectRename('project-rename', exprs)
    
    def visitProjectReorderOperator(self, ctx: HqlParser.ProjectReorderOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Ops.ProjectReorder('project-reorder', exprs)
        
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
        tables = self.visit(ctx.OnClause) if ctx.OnClause else [Exprs.Wildcard('*')]
        
        return Ops.Unnest(field, tables)
    
    def visitUnnestOperatorOnClause(self, ctx: HqlParser.UnnestOperatorOnClauseContext):
        return [self.visit(x) for x in ctx.Expressions]

    def visitUnionOperator(self, ctx: HqlParser.UnionOperatorContext):
        exprs = [self.visit(x) for x in ctx.Expressions]
        name = self.visit(ctx.TableName) if ctx.TableName else None

        return Ops.Union(exprs, name=name)

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
        
        return Exprs.ByExpression(exprs)

    def visitDataTableExpression(self, ctx: HqlParser.DataTableExpressionContext):
        schema = self.visit(ctx.Schema)
        values = []
        for i in ctx.Values:
            values.append(self.visit(i))

        name = None
        if ctx.TableName:
            name = self.visit(ctx.TableName)
        
        return Ops.Datatable(schema, values, name=name)
    
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
            limit = None
        
        return Ops.MvExpand(exprs, limit=limit)
    
    def visitMvexpandOperatorExpression(self, ctx: HqlParser.MvexpandOperatorExpressionContext):
        from Hql.Types.Hql import HqlTypes as hqlt

        expr = self.visit(ctx.Expression)
        
        if ctx.ToClause:
            to:hqlt.HqlType = self.visit(ctx.ToClause)
            return Exprs.ToClause(expr, to)

        return Exprs.ToClause(expr)
    
    def visitMvapplyOperatorExpressionToClause(self, ctx: HqlParser.MvapplyOperatorExpressionToClauseContext):
        return self.visit(ctx.Type)

    def visitMvapplyOperatorLimitClause(self, ctx: HqlParser.MvapplyOperatorLimitClauseContext):
        return self.visit(ctx.LimitValue)
    
    def visitSortOperator(self, ctx: HqlParser.SortOperatorContext):
        exprs = []
        for i in ctx.Expressions:
            exprs.append(self.visit(i))
        
        return Ops.Sort(exprs)
