#![allow(nonstandard_style)]
// Generated from Hql.g4 by ANTLR 4.8
use antlr_rust::tree::{ParseTreeVisitor,ParseTreeVisitorCompat};
use super::hqlparser::*;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link HqlParser}.
 */
pub trait HqlVisitor<'input>: ParseTreeVisitor<'input,HqlParserContextType>{
	/**
	 * Visit a parse tree produced by {@link HqlParser#top}.
	 * @param ctx the parse tree
	 */
	fn visit_top(&mut self, ctx: &TopContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#query}.
	 * @param ctx the parse tree
	 */
	fn visit_query(&mut self, ctx: &QueryContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#statement}.
	 * @param ctx the parse tree
	 */
	fn visit_statement(&mut self, ctx: &StatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#aliasDatabaseStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_aliasDatabaseStatement(&mut self, ctx: &AliasDatabaseStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_letStatement(&mut self, ctx: &LetStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letVariableDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_letVariableDeclaration(&mut self, ctx: &LetVariableDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_letFunctionDeclaration(&mut self, ctx: &LetFunctionDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letViewDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_letViewDeclaration(&mut self, ctx: &LetViewDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letViewParameterList}.
	 * @param ctx the parse tree
	 */
	fn visit_letViewParameterList(&mut self, ctx: &LetViewParameterListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letMaterializeDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_letMaterializeDeclaration(&mut self, ctx: &LetMaterializeDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letEntityGroupDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_letEntityGroupDeclaration(&mut self, ctx: &LetEntityGroupDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionParameterList}.
	 * @param ctx the parse tree
	 */
	fn visit_letFunctionParameterList(&mut self, ctx: &LetFunctionParameterListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scalarParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_scalarParameter(&mut self, ctx: &ScalarParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scalarParameterDefault}.
	 * @param ctx the parse tree
	 */
	fn visit_scalarParameterDefault(&mut self, ctx: &ScalarParameterDefaultContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_tabularParameter(&mut self, ctx: &TabularParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameterOpenSchema}.
	 * @param ctx the parse tree
	 */
	fn visit_tabularParameterOpenSchema(&mut self, ctx: &TabularParameterOpenSchemaContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameterRowSchema}.
	 * @param ctx the parse tree
	 */
	fn visit_tabularParameterRowSchema(&mut self, ctx: &TabularParameterRowSchemaContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameterRowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_tabularParameterRowSchemaColumnDeclaration(&mut self, ctx: &TabularParameterRowSchemaColumnDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionBody}.
	 * @param ctx the parse tree
	 */
	fn visit_letFunctionBody(&mut self, ctx: &LetFunctionBodyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionBodyStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_letFunctionBodyStatement(&mut self, ctx: &LetFunctionBodyStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternStatement(&mut self, ctx: &DeclarePatternStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternDefinition}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternDefinition(&mut self, ctx: &DeclarePatternDefinitionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternParameterList}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternParameterList(&mut self, ctx: &DeclarePatternParameterListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternParameter(&mut self, ctx: &DeclarePatternParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternPathParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternPathParameter(&mut self, ctx: &DeclarePatternPathParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRule}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternRule(&mut self, ctx: &DeclarePatternRuleContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRuleArgumentList}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternRuleArgumentList(&mut self, ctx: &DeclarePatternRuleArgumentListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRulePathArgument}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternRulePathArgument(&mut self, ctx: &DeclarePatternRulePathArgumentContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRuleArgument}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternRuleArgument(&mut self, ctx: &DeclarePatternRuleArgumentContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternBody}.
	 * @param ctx the parse tree
	 */
	fn visit_declarePatternBody(&mut self, ctx: &DeclarePatternBodyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#restrictAccessStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_restrictAccessStatement(&mut self, ctx: &RestrictAccessStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#restrictAccessStatementEntity}.
	 * @param ctx the parse tree
	 */
	fn visit_restrictAccessStatementEntity(&mut self, ctx: &RestrictAccessStatementEntityContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_setStatement(&mut self, ctx: &SetStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#setStatementOptionValue}.
	 * @param ctx the parse tree
	 */
	fn visit_setStatementOptionValue(&mut self, ctx: &SetStatementOptionValueContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declareQueryParametersStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_declareQueryParametersStatement(&mut self, ctx: &DeclareQueryParametersStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#declareQueryParametersStatementParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_declareQueryParametersStatementParameter(&mut self, ctx: &DeclareQueryParametersStatementParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#queryStatement}.
	 * @param ctx the parse tree
	 */
	fn visit_queryStatement(&mut self, ctx: &QueryStatementContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#expression}.
	 * @param ctx the parse tree
	 */
	fn visit_expression(&mut self, ctx: &ExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#pipeExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_pipeExpression(&mut self, ctx: &PipeExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#pipedOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_pipedOperator(&mut self, ctx: &PipedOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#pipeSubExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_pipeSubExpression(&mut self, ctx: &PipeSubExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#beforePipeExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_beforePipeExpression(&mut self, ctx: &BeforePipeExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#afterPipeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_afterPipeOperator(&mut self, ctx: &AfterPipeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#beforeOrAfterPipeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_beforeOrAfterPipeOperator(&mut self, ctx: &BeforeOrAfterPipeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkPipeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_forkPipeOperator(&mut self, ctx: &ForkPipeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#asOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_asOperator(&mut self, ctx: &AsOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#assertSchemaOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_assertSchemaOperator(&mut self, ctx: &AssertSchemaOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#consumeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_consumeOperator(&mut self, ctx: &ConsumeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#countOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_countOperator(&mut self, ctx: &CountOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#countOperatorAsClause}.
	 * @param ctx the parse tree
	 */
	fn visit_countOperatorAsClause(&mut self, ctx: &CountOperatorAsClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#distinctOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_distinctOperator(&mut self, ctx: &DistinctOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#distinctOperatorStarTarget}.
	 * @param ctx the parse tree
	 */
	fn visit_distinctOperatorStarTarget(&mut self, ctx: &DistinctOperatorStarTargetContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#distinctOperatorColumnListTarget}.
	 * @param ctx the parse tree
	 */
	fn visit_distinctOperatorColumnListTarget(&mut self, ctx: &DistinctOperatorColumnListTargetContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#evaluateOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_evaluateOperator(&mut self, ctx: &EvaluateOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#evaluateOperatorSchemaClause}.
	 * @param ctx the parse tree
	 */
	fn visit_evaluateOperatorSchemaClause(&mut self, ctx: &EvaluateOperatorSchemaClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_extendOperator(&mut self, ctx: &ExtendOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#executeAndCacheOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_executeAndCacheOperator(&mut self, ctx: &ExecuteAndCacheOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#facetByOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_facetByOperator(&mut self, ctx: &FacetByOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#facetByOperatorWithOperatorClause}.
	 * @param ctx the parse tree
	 */
	fn visit_facetByOperatorWithOperatorClause(&mut self, ctx: &FacetByOperatorWithOperatorClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#facetByOperatorWithExpressionClause}.
	 * @param ctx the parse tree
	 */
	fn visit_facetByOperatorWithExpressionClause(&mut self, ctx: &FacetByOperatorWithExpressionClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperator(&mut self, ctx: &FindOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorParametersWhereClause}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorParametersWhereClause(&mut self, ctx: &FindOperatorParametersWhereClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorInClause}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorInClause(&mut self, ctx: &FindOperatorInClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectClause}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorProjectClause(&mut self, ctx: &FindOperatorProjectClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorProjectExpression(&mut self, ctx: &FindOperatorProjectExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorColumnExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorColumnExpression(&mut self, ctx: &FindOperatorColumnExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorOptionalColumnType}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorOptionalColumnType(&mut self, ctx: &FindOperatorOptionalColumnTypeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorPackExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorPackExpression(&mut self, ctx: &FindOperatorPackExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectSmartClause}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorProjectSmartClause(&mut self, ctx: &FindOperatorProjectSmartClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectAwayClause}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorProjectAwayClause(&mut self, ctx: &FindOperatorProjectAwayClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectAwayStar}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorProjectAwayStar(&mut self, ctx: &FindOperatorProjectAwayStarContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectAwayColumnList}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorProjectAwayColumnList(&mut self, ctx: &FindOperatorProjectAwayColumnListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorSource}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorSource(&mut self, ctx: &FindOperatorSourceContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorSourceEntityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_findOperatorSourceEntityExpression(&mut self, ctx: &FindOperatorSourceEntityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_forkOperator(&mut self, ctx: &ForkOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorFork}.
	 * @param ctx the parse tree
	 */
	fn visit_forkOperatorFork(&mut self, ctx: &ForkOperatorForkContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorExpressionName}.
	 * @param ctx the parse tree
	 */
	fn visit_forkOperatorExpressionName(&mut self, ctx: &ForkOperatorExpressionNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_forkOperatorExpression(&mut self, ctx: &ForkOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorPipedOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_forkOperatorPipedOperator(&mut self, ctx: &ForkOperatorPipedOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#getSchemaOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_getSchemaOperator(&mut self, ctx: &GetSchemaOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMarkComponentsOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMarkComponentsOperator(&mut self, ctx: &GraphMarkComponentsOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchOperator(&mut self, ctx: &GraphMatchOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPattern}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchPattern(&mut self, ctx: &GraphMatchPatternContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternNode}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchPatternNode(&mut self, ctx: &GraphMatchPatternNodeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternUnnamedEdge}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchPatternUnnamedEdge(&mut self, ctx: &GraphMatchPatternUnnamedEdgeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternNamedEdge}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchPatternNamedEdge(&mut self, ctx: &GraphMatchPatternNamedEdgeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternRange}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchPatternRange(&mut self, ctx: &GraphMatchPatternRangeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchWhereClause}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchWhereClause(&mut self, ctx: &GraphMatchWhereClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchProjectClause}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMatchProjectClause(&mut self, ctx: &GraphMatchProjectClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMergeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_graphMergeOperator(&mut self, ctx: &GraphMergeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphToTableOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_graphToTableOperator(&mut self, ctx: &GraphToTableOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphToTableOutput}.
	 * @param ctx the parse tree
	 */
	fn visit_graphToTableOutput(&mut self, ctx: &GraphToTableOutputContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphToTableAsClause}.
	 * @param ctx the parse tree
	 */
	fn visit_graphToTableAsClause(&mut self, ctx: &GraphToTableAsClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphShortestPathsOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_graphShortestPathsOperator(&mut self, ctx: &GraphShortestPathsOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#invokeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_invokeOperator(&mut self, ctx: &InvokeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#joinOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_joinOperator(&mut self, ctx: &JoinOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#joinOperatorOnClause}.
	 * @param ctx the parse tree
	 */
	fn visit_joinOperatorOnClause(&mut self, ctx: &JoinOperatorOnClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#joinOperatorWhereClause}.
	 * @param ctx the parse tree
	 */
	fn visit_joinOperatorWhereClause(&mut self, ctx: &JoinOperatorWhereClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#lookupOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_lookupOperator(&mut self, ctx: &LookupOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#macroExpandOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_macroExpandOperator(&mut self, ctx: &MacroExpandOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#macroExpandEntityGroup}.
	 * @param ctx the parse tree
	 */
	fn visit_macroExpandEntityGroup(&mut self, ctx: &MacroExpandEntityGroupContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityGroupExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_entityGroupExpression(&mut self, ctx: &EntityGroupExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_makeGraphOperator(&mut self, ctx: &MakeGraphOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphIdClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeGraphIdClause(&mut self, ctx: &MakeGraphIdClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphTablesAndKeysClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeGraphTablesAndKeysClause(&mut self, ctx: &MakeGraphTablesAndKeysClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphPartitionedByClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeGraphPartitionedByClause(&mut self, ctx: &MakeGraphPartitionedByClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperator(&mut self, ctx: &MakeSeriesOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorOnClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperatorOnClause(&mut self, ctx: &MakeSeriesOperatorOnClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorAggregation}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperatorAggregation(&mut self, ctx: &MakeSeriesOperatorAggregationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorExpressionDefaultClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperatorExpressionDefaultClause(&mut self, ctx: &MakeSeriesOperatorExpressionDefaultClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorInRangeClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperatorInRangeClause(&mut self, ctx: &MakeSeriesOperatorInRangeClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorFromToStepClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperatorFromToStepClause(&mut self, ctx: &MakeSeriesOperatorFromToStepClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorByClause}.
	 * @param ctx the parse tree
	 */
	fn visit_makeSeriesOperatorByClause(&mut self, ctx: &MakeSeriesOperatorByClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_mvapplyOperator(&mut self, ctx: &MvapplyOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorLimitClause}.
	 * @param ctx the parse tree
	 */
	fn visit_mvapplyOperatorLimitClause(&mut self, ctx: &MvapplyOperatorLimitClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorIdClause}.
	 * @param ctx the parse tree
	 */
	fn visit_mvapplyOperatorIdClause(&mut self, ctx: &MvapplyOperatorIdClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_mvapplyOperatorExpression(&mut self, ctx: &MvapplyOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorExpressionToClause}.
	 * @param ctx the parse tree
	 */
	fn visit_mvapplyOperatorExpressionToClause(&mut self, ctx: &MvapplyOperatorExpressionToClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvexpandOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_mvexpandOperator(&mut self, ctx: &MvexpandOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvexpandOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_mvexpandOperatorExpression(&mut self, ctx: &MvexpandOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_parseOperator(&mut self, ctx: &ParseOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorKindClause}.
	 * @param ctx the parse tree
	 */
	fn visit_parseOperatorKindClause(&mut self, ctx: &ParseOperatorKindClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorFlagsClause}.
	 * @param ctx the parse tree
	 */
	fn visit_parseOperatorFlagsClause(&mut self, ctx: &ParseOperatorFlagsClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorNameAndOptionalType}.
	 * @param ctx the parse tree
	 */
	fn visit_parseOperatorNameAndOptionalType(&mut self, ctx: &ParseOperatorNameAndOptionalTypeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorPattern}.
	 * @param ctx the parse tree
	 */
	fn visit_parseOperatorPattern(&mut self, ctx: &ParseOperatorPatternContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorPatternSegment}.
	 * @param ctx the parse tree
	 */
	fn visit_parseOperatorPatternSegment(&mut self, ctx: &ParseOperatorPatternSegmentContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseWhereOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_parseWhereOperator(&mut self, ctx: &ParseWhereOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseKvOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_parseKvOperator(&mut self, ctx: &ParseKvOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseKvWithClause}.
	 * @param ctx the parse tree
	 */
	fn visit_parseKvWithClause(&mut self, ctx: &ParseKvWithClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_partitionOperator(&mut self, ctx: &PartitionOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperatorInClause}.
	 * @param ctx the parse tree
	 */
	fn visit_partitionOperatorInClause(&mut self, ctx: &PartitionOperatorInClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperatorSubExpressionBody}.
	 * @param ctx the parse tree
	 */
	fn visit_partitionOperatorSubExpressionBody(&mut self, ctx: &PartitionOperatorSubExpressionBodyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperatorFullExpressionBody}.
	 * @param ctx the parse tree
	 */
	fn visit_partitionOperatorFullExpressionBody(&mut self, ctx: &PartitionOperatorFullExpressionBodyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionByOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_partitionByOperator(&mut self, ctx: &PartitionByOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionByOperatorIdClause}.
	 * @param ctx the parse tree
	 */
	fn visit_partitionByOperatorIdClause(&mut self, ctx: &PartitionByOperatorIdClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#printOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_printOperator(&mut self, ctx: &PrintOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectAwayOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_projectAwayOperator(&mut self, ctx: &ProjectAwayOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectKeepOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_projectKeepOperator(&mut self, ctx: &ProjectKeepOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_projectOperator(&mut self, ctx: &ProjectOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectRenameOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_projectRenameOperator(&mut self, ctx: &ProjectRenameOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectReorderOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_projectReorderOperator(&mut self, ctx: &ProjectReorderOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectReorderExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_projectReorderExpression(&mut self, ctx: &ProjectReorderExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#reduceByOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_reduceByOperator(&mut self, ctx: &ReduceByOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#reduceByWithClause}.
	 * @param ctx the parse tree
	 */
	fn visit_reduceByWithClause(&mut self, ctx: &ReduceByWithClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_renderOperator(&mut self, ctx: &RenderOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorWithClause}.
	 * @param ctx the parse tree
	 */
	fn visit_renderOperatorWithClause(&mut self, ctx: &RenderOperatorWithClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorLegacyPropertyList}.
	 * @param ctx the parse tree
	 */
	fn visit_renderOperatorLegacyPropertyList(&mut self, ctx: &RenderOperatorLegacyPropertyListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorProperty}.
	 * @param ctx the parse tree
	 */
	fn visit_renderOperatorProperty(&mut self, ctx: &RenderOperatorPropertyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderPropertyNameList}.
	 * @param ctx the parse tree
	 */
	fn visit_renderPropertyNameList(&mut self, ctx: &RenderPropertyNameListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorLegacyProperty}.
	 * @param ctx the parse tree
	 */
	fn visit_renderOperatorLegacyProperty(&mut self, ctx: &RenderOperatorLegacyPropertyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#sampleDistinctOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_sampleDistinctOperator(&mut self, ctx: &SampleDistinctOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#sampleOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_sampleOperator(&mut self, ctx: &SampleOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperator(&mut self, ctx: &ScanOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorOrderByClause}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorOrderByClause(&mut self, ctx: &ScanOperatorOrderByClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorPartitionByClause}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorPartitionByClause(&mut self, ctx: &ScanOperatorPartitionByClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorDeclareClause}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorDeclareClause(&mut self, ctx: &ScanOperatorDeclareClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorStep}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorStep(&mut self, ctx: &ScanOperatorStepContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorStepOutputClause}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorStepOutputClause(&mut self, ctx: &ScanOperatorStepOutputClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorBody}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorBody(&mut self, ctx: &ScanOperatorBodyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorAssignment}.
	 * @param ctx the parse tree
	 */
	fn visit_scanOperatorAssignment(&mut self, ctx: &ScanOperatorAssignmentContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#searchOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_searchOperator(&mut self, ctx: &SearchOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#searchOperatorStarAndExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_searchOperatorStarAndExpression(&mut self, ctx: &SearchOperatorStarAndExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#searchOperatorInClause}.
	 * @param ctx the parse tree
	 */
	fn visit_searchOperatorInClause(&mut self, ctx: &SearchOperatorInClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#serializeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_serializeOperator(&mut self, ctx: &SerializeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#sortOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_sortOperator(&mut self, ctx: &SortOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#orderedExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_orderedExpression(&mut self, ctx: &OrderedExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#sortOrdering}.
	 * @param ctx the parse tree
	 */
	fn visit_sortOrdering(&mut self, ctx: &SortOrderingContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#summarizeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_summarizeOperator(&mut self, ctx: &SummarizeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#summarizeOperatorByClause}.
	 * @param ctx the parse tree
	 */
	fn visit_summarizeOperatorByClause(&mut self, ctx: &SummarizeOperatorByClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#summarizeOperatorLegacyBinClause}.
	 * @param ctx the parse tree
	 */
	fn visit_summarizeOperatorLegacyBinClause(&mut self, ctx: &SummarizeOperatorLegacyBinClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#takeOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_takeOperator(&mut self, ctx: &TakeOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#topOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_topOperator(&mut self, ctx: &TopOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#topHittersOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_topHittersOperator(&mut self, ctx: &TopHittersOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#topHittersOperatorByClause}.
	 * @param ctx the parse tree
	 */
	fn visit_topHittersOperatorByClause(&mut self, ctx: &TopHittersOperatorByClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#topNestedOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_topNestedOperator(&mut self, ctx: &TopNestedOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#topNestedOperatorPart}.
	 * @param ctx the parse tree
	 */
	fn visit_topNestedOperatorPart(&mut self, ctx: &TopNestedOperatorPartContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#topNestedOperatorWithOthersClause}.
	 * @param ctx the parse tree
	 */
	fn visit_topNestedOperatorWithOthersClause(&mut self, ctx: &TopNestedOperatorWithOthersClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#unionOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_unionOperator(&mut self, ctx: &UnionOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#unionOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_unionOperatorExpression(&mut self, ctx: &UnionOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#whereOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_whereOperator(&mut self, ctx: &WhereOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualSubExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_contextualSubExpression(&mut self, ctx: &ContextualSubExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualPipeExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_contextualPipeExpression(&mut self, ctx: &ContextualPipeExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualPipeExpressionPipedOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_contextualPipeExpressionPipedOperator(&mut self, ctx: &ContextualPipeExpressionPipedOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#strictQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_strictQueryOperatorParameter(&mut self, ctx: &StrictQueryOperatorParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#relaxedQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_relaxedQueryOperatorParameter(&mut self, ctx: &RelaxedQueryOperatorParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#queryOperatorProperty}.
	 * @param ctx the parse tree
	 */
	fn visit_queryOperatorProperty(&mut self, ctx: &QueryOperatorPropertyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_namedExpression(&mut self, ctx: &NamedExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedExpressionNameClause}.
	 * @param ctx the parse tree
	 */
	fn visit_namedExpressionNameClause(&mut self, ctx: &NamedExpressionNameClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedExpressionNameList}.
	 * @param ctx the parse tree
	 */
	fn visit_namedExpressionNameList(&mut self, ctx: &NamedExpressionNameListContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scopedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_scopedFunctionCallExpression(&mut self, ctx: &ScopedFunctionCallExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#unnamedExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_unnamedExpression(&mut self, ctx: &UnnamedExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_logicalOrExpression(&mut self, ctx: &LogicalOrExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalOrOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_logicalOrOperation(&mut self, ctx: &LogicalOrOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_logicalAndExpression(&mut self, ctx: &LogicalAndExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalAndOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_logicalAndOperation(&mut self, ctx: &LogicalAndOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_equalityExpression(&mut self, ctx: &EqualityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#equalsEqualityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_equalsEqualityExpression(&mut self, ctx: &EqualsEqualityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#listEqualityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_listEqualityExpression(&mut self, ctx: &ListEqualityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#betweenEqualityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_betweenEqualityExpression(&mut self, ctx: &BetweenEqualityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#starEqualityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_starEqualityExpression(&mut self, ctx: &StarEqualityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_relationalExpression(&mut self, ctx: &RelationalExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_additiveExpression(&mut self, ctx: &AdditiveExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#additiveOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_additiveOperation(&mut self, ctx: &AdditiveOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_multiplicativeExpression(&mut self, ctx: &MultiplicativeExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#multiplicativeOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_multiplicativeOperation(&mut self, ctx: &MultiplicativeOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_stringOperatorExpression(&mut self, ctx: &StringOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringBinaryOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_stringBinaryOperatorExpression(&mut self, ctx: &StringBinaryOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringBinaryOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_stringBinaryOperation(&mut self, ctx: &StringBinaryOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringBinaryOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_stringBinaryOperator(&mut self, ctx: &StringBinaryOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringStarOperatorExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_stringStarOperatorExpression(&mut self, ctx: &StringStarOperatorExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#invocationExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_invocationExpression(&mut self, ctx: &InvocationExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_functionCallOrPathExpression(&mut self, ctx: &FunctionCallOrPathExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathRoot}.
	 * @param ctx the parse tree
	 */
	fn visit_functionCallOrPathRoot(&mut self, ctx: &FunctionCallOrPathRootContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathPathExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_functionCallOrPathPathExpression(&mut self, ctx: &FunctionCallOrPathPathExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_functionCallOrPathOperation(&mut self, ctx: &FunctionCallOrPathOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionalCallOrPathPathOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_functionalCallOrPathPathOperation(&mut self, ctx: &FunctionalCallOrPathPathOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_functionCallOrPathElementOperation(&mut self, ctx: &FunctionCallOrPathElementOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#legacyFunctionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_legacyFunctionCallOrPathElementOperation(&mut self, ctx: &LegacyFunctionCallOrPathElementOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#toScalarExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_toScalarExpression(&mut self, ctx: &ToScalarExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#toTableExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_toTableExpression(&mut self, ctx: &ToTableExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#noOptimizationParameter}.
	 * @param ctx the parse tree
	 */
	fn visit_noOptimizationParameter(&mut self, ctx: &NoOptimizationParameterContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_dotCompositeFunctionCallExpression(&mut self, ctx: &DotCompositeFunctionCallExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallOperation}.
	 * @param ctx the parse tree
	 */
	fn visit_dotCompositeFunctionCallOperation(&mut self, ctx: &DotCompositeFunctionCallOperationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_functionCallExpression(&mut self, ctx: &FunctionCallExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_namedFunctionCallExpression(&mut self, ctx: &NamedFunctionCallExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#argumentExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_argumentExpression(&mut self, ctx: &ArgumentExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#countExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_countExpression(&mut self, ctx: &CountExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#starExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_starExpression(&mut self, ctx: &StarExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_primaryExpression(&mut self, ctx: &PrimaryExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#nameReferenceWithDataScope}.
	 * @param ctx the parse tree
	 */
	fn visit_nameReferenceWithDataScope(&mut self, ctx: &NameReferenceWithDataScopeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#dataScopeClause}.
	 * @param ctx the parse tree
	 */
	fn visit_dataScopeClause(&mut self, ctx: &DataScopeClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parenthesizedExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_parenthesizedExpression(&mut self, ctx: &ParenthesizedExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#rangeExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_rangeExpression(&mut self, ctx: &RangeExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_entityExpression(&mut self, ctx: &EntityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityPathOrElementExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_entityPathOrElementExpression(&mut self, ctx: &EntityPathOrElementExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityPathOrElementOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_entityPathOrElementOperator(&mut self, ctx: &EntityPathOrElementOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityPathOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_entityPathOperator(&mut self, ctx: &EntityPathOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityElementOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_entityElementOperator(&mut self, ctx: &EntityElementOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#legacyEntityPathElementOperator}.
	 * @param ctx the parse tree
	 */
	fn visit_legacyEntityPathElementOperator(&mut self, ctx: &LegacyEntityPathElementOperatorContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityName}.
	 * @param ctx the parse tree
	 */
	fn visit_entityName(&mut self, ctx: &EntityNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityNameReference}.
	 * @param ctx the parse tree
	 */
	fn visit_entityNameReference(&mut self, ctx: &EntityNameReferenceContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#atSignName}.
	 * @param ctx the parse tree
	 */
	fn visit_atSignName(&mut self, ctx: &AtSignNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedPathName}.
	 * @param ctx the parse tree
	 */
	fn visit_extendedPathName(&mut self, ctx: &ExtendedPathNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedEntityExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedEntityExpression(&mut self, ctx: &WildcardedEntityExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedPathExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedPathExpression(&mut self, ctx: &WildcardedPathExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedPathName}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedPathName(&mut self, ctx: &WildcardedPathNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualDataTableExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_contextualDataTableExpression(&mut self, ctx: &ContextualDataTableExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#dataTableExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_dataTableExpression(&mut self, ctx: &DataTableExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#rowSchema}.
	 * @param ctx the parse tree
	 */
	fn visit_rowSchema(&mut self, ctx: &RowSchemaContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#rowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
	fn visit_rowSchemaColumnDeclaration(&mut self, ctx: &RowSchemaColumnDeclarationContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#externalDataExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_externalDataExpression(&mut self, ctx: &ExternalDataExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#externalDataWithClause}.
	 * @param ctx the parse tree
	 */
	fn visit_externalDataWithClause(&mut self, ctx: &ExternalDataWithClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#externalDataWithClauseProperty}.
	 * @param ctx the parse tree
	 */
	fn visit_externalDataWithClauseProperty(&mut self, ctx: &ExternalDataWithClausePropertyContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializedViewCombineExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_materializedViewCombineExpression(&mut self, ctx: &MaterializedViewCombineExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializeViewCombineBaseClause}.
	 * @param ctx the parse tree
	 */
	fn visit_materializeViewCombineBaseClause(&mut self, ctx: &MaterializeViewCombineBaseClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializedViewCombineDeltaClause}.
	 * @param ctx the parse tree
	 */
	fn visit_materializedViewCombineDeltaClause(&mut self, ctx: &MaterializedViewCombineDeltaClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializedViewCombineAggregationsClause}.
	 * @param ctx the parse tree
	 */
	fn visit_materializedViewCombineAggregationsClause(&mut self, ctx: &MaterializedViewCombineAggregationsClauseContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#scalarType}.
	 * @param ctx the parse tree
	 */
	fn visit_scalarType(&mut self, ctx: &ScalarTypeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedScalarType}.
	 * @param ctx the parse tree
	 */
	fn visit_extendedScalarType(&mut self, ctx: &ExtendedScalarTypeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#parameterName}.
	 * @param ctx the parse tree
	 */
	fn visit_parameterName(&mut self, ctx: &ParameterNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#simpleNameReference}.
	 * @param ctx the parse tree
	 */
	fn visit_simpleNameReference(&mut self, ctx: &SimpleNameReferenceContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedNameReference}.
	 * @param ctx the parse tree
	 */
	fn visit_extendedNameReference(&mut self, ctx: &ExtendedNameReferenceContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedNameReference}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedNameReference(&mut self, ctx: &WildcardedNameReferenceContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#simpleOrWildcardedNameReference}.
	 * @param ctx the parse tree
	 */
	fn visit_simpleOrWildcardedNameReference(&mut self, ctx: &SimpleOrWildcardedNameReferenceContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierName}.
	 * @param ctx the parse tree
	 */
	fn visit_identifierName(&mut self, ctx: &IdentifierNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#keywordName}.
	 * @param ctx the parse tree
	 */
	fn visit_keywordName(&mut self, ctx: &KeywordNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedKeywordName}.
	 * @param ctx the parse tree
	 */
	fn visit_extendedKeywordName(&mut self, ctx: &ExtendedKeywordNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#escapedName}.
	 * @param ctx the parse tree
	 */
	fn visit_escapedName(&mut self, ctx: &EscapedNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrKeywordName}.
	 * @param ctx the parse tree
	 */
	fn visit_identifierOrKeywordName(&mut self, ctx: &IdentifierOrKeywordNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
	fn visit_identifierOrKeywordOrEscapedName(&mut self, ctx: &IdentifierOrKeywordOrEscapedNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
	fn visit_identifierOrExtendedKeywordOrEscapedName(&mut self, ctx: &IdentifierOrExtendedKeywordOrEscapedNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordName}.
	 * @param ctx the parse tree
	 */
	fn visit_identifierOrExtendedKeywordName(&mut self, ctx: &IdentifierOrExtendedKeywordNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedName}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedName(&mut self, ctx: &WildcardedNameContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedNamePrefix}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedNamePrefix(&mut self, ctx: &WildcardedNamePrefixContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedNameSegment}.
	 * @param ctx the parse tree
	 */
	fn visit_wildcardedNameSegment(&mut self, ctx: &WildcardedNameSegmentContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#literalExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_literalExpression(&mut self, ctx: &LiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#unsignedLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_unsignedLiteralExpression(&mut self, ctx: &UnsignedLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#numberLikeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_numberLikeLiteralExpression(&mut self, ctx: &NumberLikeLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#numericLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_numericLiteralExpression(&mut self, ctx: &NumericLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#signedLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_signedLiteralExpression(&mut self, ctx: &SignedLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#longLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_longLiteralExpression(&mut self, ctx: &LongLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#intLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_intLiteralExpression(&mut self, ctx: &IntLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#realLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_realLiteralExpression(&mut self, ctx: &RealLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#decimalLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_decimalLiteralExpression(&mut self, ctx: &DecimalLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#dateTimeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_dateTimeLiteralExpression(&mut self, ctx: &DateTimeLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#timeSpanLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_timeSpanLiteralExpression(&mut self, ctx: &TimeSpanLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#booleanLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_booleanLiteralExpression(&mut self, ctx: &BooleanLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#guidLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_guidLiteralExpression(&mut self, ctx: &GuidLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#typeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_typeLiteralExpression(&mut self, ctx: &TypeLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#signedLongLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_signedLongLiteralExpression(&mut self, ctx: &SignedLongLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#signedRealLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_signedRealLiteralExpression(&mut self, ctx: &SignedRealLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_stringLiteralExpression(&mut self, ctx: &StringLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#dynamicLiteralExpression}.
	 * @param ctx the parse tree
	 */
	fn visit_dynamicLiteralExpression(&mut self, ctx: &DynamicLiteralExpressionContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonValue}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonValue(&mut self, ctx: &JsonValueContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonObject}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonObject(&mut self, ctx: &JsonObjectContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonPair}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonPair(&mut self, ctx: &JsonPairContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonArray}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonArray(&mut self, ctx: &JsonArrayContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonBoolean}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonBoolean(&mut self, ctx: &JsonBooleanContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonDateTime}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonDateTime(&mut self, ctx: &JsonDateTimeContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonGuid}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonGuid(&mut self, ctx: &JsonGuidContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonNull}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonNull(&mut self, ctx: &JsonNullContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonString}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonString(&mut self, ctx: &JsonStringContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonTimeSpan}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonTimeSpan(&mut self, ctx: &JsonTimeSpanContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonLong}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonLong(&mut self, ctx: &JsonLongContext<'input>) { self.visit_children(ctx) }

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonReal}.
	 * @param ctx the parse tree
	 */
	fn visit_jsonReal(&mut self, ctx: &JsonRealContext<'input>) { self.visit_children(ctx) }

}

pub trait HqlVisitorCompat<'input>:ParseTreeVisitorCompat<'input, Node= HqlParserContextType>{
	/**
	 * Visit a parse tree produced by {@link HqlParser#top}.
	 * @param ctx the parse tree
	 */
		fn visit_top(&mut self, ctx: &TopContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#query}.
	 * @param ctx the parse tree
	 */
		fn visit_query(&mut self, ctx: &QueryContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#statement}.
	 * @param ctx the parse tree
	 */
		fn visit_statement(&mut self, ctx: &StatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#aliasDatabaseStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_aliasDatabaseStatement(&mut self, ctx: &AliasDatabaseStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_letStatement(&mut self, ctx: &LetStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letVariableDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_letVariableDeclaration(&mut self, ctx: &LetVariableDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_letFunctionDeclaration(&mut self, ctx: &LetFunctionDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letViewDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_letViewDeclaration(&mut self, ctx: &LetViewDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letViewParameterList}.
	 * @param ctx the parse tree
	 */
		fn visit_letViewParameterList(&mut self, ctx: &LetViewParameterListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letMaterializeDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_letMaterializeDeclaration(&mut self, ctx: &LetMaterializeDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letEntityGroupDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_letEntityGroupDeclaration(&mut self, ctx: &LetEntityGroupDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionParameterList}.
	 * @param ctx the parse tree
	 */
		fn visit_letFunctionParameterList(&mut self, ctx: &LetFunctionParameterListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scalarParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_scalarParameter(&mut self, ctx: &ScalarParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scalarParameterDefault}.
	 * @param ctx the parse tree
	 */
		fn visit_scalarParameterDefault(&mut self, ctx: &ScalarParameterDefaultContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_tabularParameter(&mut self, ctx: &TabularParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameterOpenSchema}.
	 * @param ctx the parse tree
	 */
		fn visit_tabularParameterOpenSchema(&mut self, ctx: &TabularParameterOpenSchemaContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameterRowSchema}.
	 * @param ctx the parse tree
	 */
		fn visit_tabularParameterRowSchema(&mut self, ctx: &TabularParameterRowSchemaContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#tabularParameterRowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_tabularParameterRowSchemaColumnDeclaration(&mut self, ctx: &TabularParameterRowSchemaColumnDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionBody}.
	 * @param ctx the parse tree
	 */
		fn visit_letFunctionBody(&mut self, ctx: &LetFunctionBodyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#letFunctionBodyStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_letFunctionBodyStatement(&mut self, ctx: &LetFunctionBodyStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternStatement(&mut self, ctx: &DeclarePatternStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternDefinition}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternDefinition(&mut self, ctx: &DeclarePatternDefinitionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternParameterList}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternParameterList(&mut self, ctx: &DeclarePatternParameterListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternParameter(&mut self, ctx: &DeclarePatternParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternPathParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternPathParameter(&mut self, ctx: &DeclarePatternPathParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRule}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternRule(&mut self, ctx: &DeclarePatternRuleContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRuleArgumentList}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternRuleArgumentList(&mut self, ctx: &DeclarePatternRuleArgumentListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRulePathArgument}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternRulePathArgument(&mut self, ctx: &DeclarePatternRulePathArgumentContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternRuleArgument}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternRuleArgument(&mut self, ctx: &DeclarePatternRuleArgumentContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declarePatternBody}.
	 * @param ctx the parse tree
	 */
		fn visit_declarePatternBody(&mut self, ctx: &DeclarePatternBodyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#restrictAccessStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_restrictAccessStatement(&mut self, ctx: &RestrictAccessStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#restrictAccessStatementEntity}.
	 * @param ctx the parse tree
	 */
		fn visit_restrictAccessStatementEntity(&mut self, ctx: &RestrictAccessStatementEntityContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#setStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_setStatement(&mut self, ctx: &SetStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#setStatementOptionValue}.
	 * @param ctx the parse tree
	 */
		fn visit_setStatementOptionValue(&mut self, ctx: &SetStatementOptionValueContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declareQueryParametersStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_declareQueryParametersStatement(&mut self, ctx: &DeclareQueryParametersStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#declareQueryParametersStatementParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_declareQueryParametersStatementParameter(&mut self, ctx: &DeclareQueryParametersStatementParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#queryStatement}.
	 * @param ctx the parse tree
	 */
		fn visit_queryStatement(&mut self, ctx: &QueryStatementContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#expression}.
	 * @param ctx the parse tree
	 */
		fn visit_expression(&mut self, ctx: &ExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#pipeExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_pipeExpression(&mut self, ctx: &PipeExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#pipedOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_pipedOperator(&mut self, ctx: &PipedOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#pipeSubExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_pipeSubExpression(&mut self, ctx: &PipeSubExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#beforePipeExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_beforePipeExpression(&mut self, ctx: &BeforePipeExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#afterPipeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_afterPipeOperator(&mut self, ctx: &AfterPipeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#beforeOrAfterPipeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_beforeOrAfterPipeOperator(&mut self, ctx: &BeforeOrAfterPipeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkPipeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_forkPipeOperator(&mut self, ctx: &ForkPipeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#asOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_asOperator(&mut self, ctx: &AsOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#assertSchemaOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_assertSchemaOperator(&mut self, ctx: &AssertSchemaOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#consumeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_consumeOperator(&mut self, ctx: &ConsumeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#countOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_countOperator(&mut self, ctx: &CountOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#countOperatorAsClause}.
	 * @param ctx the parse tree
	 */
		fn visit_countOperatorAsClause(&mut self, ctx: &CountOperatorAsClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#distinctOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_distinctOperator(&mut self, ctx: &DistinctOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#distinctOperatorStarTarget}.
	 * @param ctx the parse tree
	 */
		fn visit_distinctOperatorStarTarget(&mut self, ctx: &DistinctOperatorStarTargetContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#distinctOperatorColumnListTarget}.
	 * @param ctx the parse tree
	 */
		fn visit_distinctOperatorColumnListTarget(&mut self, ctx: &DistinctOperatorColumnListTargetContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#evaluateOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_evaluateOperator(&mut self, ctx: &EvaluateOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#evaluateOperatorSchemaClause}.
	 * @param ctx the parse tree
	 */
		fn visit_evaluateOperatorSchemaClause(&mut self, ctx: &EvaluateOperatorSchemaClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_extendOperator(&mut self, ctx: &ExtendOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#executeAndCacheOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_executeAndCacheOperator(&mut self, ctx: &ExecuteAndCacheOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#facetByOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_facetByOperator(&mut self, ctx: &FacetByOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#facetByOperatorWithOperatorClause}.
	 * @param ctx the parse tree
	 */
		fn visit_facetByOperatorWithOperatorClause(&mut self, ctx: &FacetByOperatorWithOperatorClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#facetByOperatorWithExpressionClause}.
	 * @param ctx the parse tree
	 */
		fn visit_facetByOperatorWithExpressionClause(&mut self, ctx: &FacetByOperatorWithExpressionClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperator(&mut self, ctx: &FindOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorParametersWhereClause}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorParametersWhereClause(&mut self, ctx: &FindOperatorParametersWhereClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorInClause}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorInClause(&mut self, ctx: &FindOperatorInClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectClause}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorProjectClause(&mut self, ctx: &FindOperatorProjectClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorProjectExpression(&mut self, ctx: &FindOperatorProjectExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorColumnExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorColumnExpression(&mut self, ctx: &FindOperatorColumnExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorOptionalColumnType}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorOptionalColumnType(&mut self, ctx: &FindOperatorOptionalColumnTypeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorPackExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorPackExpression(&mut self, ctx: &FindOperatorPackExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectSmartClause}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorProjectSmartClause(&mut self, ctx: &FindOperatorProjectSmartClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectAwayClause}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorProjectAwayClause(&mut self, ctx: &FindOperatorProjectAwayClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectAwayStar}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorProjectAwayStar(&mut self, ctx: &FindOperatorProjectAwayStarContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorProjectAwayColumnList}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorProjectAwayColumnList(&mut self, ctx: &FindOperatorProjectAwayColumnListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorSource}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorSource(&mut self, ctx: &FindOperatorSourceContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#findOperatorSourceEntityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_findOperatorSourceEntityExpression(&mut self, ctx: &FindOperatorSourceEntityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_forkOperator(&mut self, ctx: &ForkOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorFork}.
	 * @param ctx the parse tree
	 */
		fn visit_forkOperatorFork(&mut self, ctx: &ForkOperatorForkContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorExpressionName}.
	 * @param ctx the parse tree
	 */
		fn visit_forkOperatorExpressionName(&mut self, ctx: &ForkOperatorExpressionNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_forkOperatorExpression(&mut self, ctx: &ForkOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#forkOperatorPipedOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_forkOperatorPipedOperator(&mut self, ctx: &ForkOperatorPipedOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#getSchemaOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_getSchemaOperator(&mut self, ctx: &GetSchemaOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMarkComponentsOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMarkComponentsOperator(&mut self, ctx: &GraphMarkComponentsOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchOperator(&mut self, ctx: &GraphMatchOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPattern}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchPattern(&mut self, ctx: &GraphMatchPatternContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternNode}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchPatternNode(&mut self, ctx: &GraphMatchPatternNodeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternUnnamedEdge}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchPatternUnnamedEdge(&mut self, ctx: &GraphMatchPatternUnnamedEdgeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternNamedEdge}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchPatternNamedEdge(&mut self, ctx: &GraphMatchPatternNamedEdgeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchPatternRange}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchPatternRange(&mut self, ctx: &GraphMatchPatternRangeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchWhereClause}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchWhereClause(&mut self, ctx: &GraphMatchWhereClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMatchProjectClause}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMatchProjectClause(&mut self, ctx: &GraphMatchProjectClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphMergeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_graphMergeOperator(&mut self, ctx: &GraphMergeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphToTableOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_graphToTableOperator(&mut self, ctx: &GraphToTableOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphToTableOutput}.
	 * @param ctx the parse tree
	 */
		fn visit_graphToTableOutput(&mut self, ctx: &GraphToTableOutputContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphToTableAsClause}.
	 * @param ctx the parse tree
	 */
		fn visit_graphToTableAsClause(&mut self, ctx: &GraphToTableAsClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#graphShortestPathsOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_graphShortestPathsOperator(&mut self, ctx: &GraphShortestPathsOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#invokeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_invokeOperator(&mut self, ctx: &InvokeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#joinOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_joinOperator(&mut self, ctx: &JoinOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#joinOperatorOnClause}.
	 * @param ctx the parse tree
	 */
		fn visit_joinOperatorOnClause(&mut self, ctx: &JoinOperatorOnClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#joinOperatorWhereClause}.
	 * @param ctx the parse tree
	 */
		fn visit_joinOperatorWhereClause(&mut self, ctx: &JoinOperatorWhereClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#lookupOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_lookupOperator(&mut self, ctx: &LookupOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#macroExpandOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_macroExpandOperator(&mut self, ctx: &MacroExpandOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#macroExpandEntityGroup}.
	 * @param ctx the parse tree
	 */
		fn visit_macroExpandEntityGroup(&mut self, ctx: &MacroExpandEntityGroupContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityGroupExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_entityGroupExpression(&mut self, ctx: &EntityGroupExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_makeGraphOperator(&mut self, ctx: &MakeGraphOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphIdClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeGraphIdClause(&mut self, ctx: &MakeGraphIdClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphTablesAndKeysClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeGraphTablesAndKeysClause(&mut self, ctx: &MakeGraphTablesAndKeysClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeGraphPartitionedByClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeGraphPartitionedByClause(&mut self, ctx: &MakeGraphPartitionedByClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperator(&mut self, ctx: &MakeSeriesOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorOnClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperatorOnClause(&mut self, ctx: &MakeSeriesOperatorOnClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorAggregation}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperatorAggregation(&mut self, ctx: &MakeSeriesOperatorAggregationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorExpressionDefaultClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperatorExpressionDefaultClause(&mut self, ctx: &MakeSeriesOperatorExpressionDefaultClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorInRangeClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperatorInRangeClause(&mut self, ctx: &MakeSeriesOperatorInRangeClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorFromToStepClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperatorFromToStepClause(&mut self, ctx: &MakeSeriesOperatorFromToStepClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#makeSeriesOperatorByClause}.
	 * @param ctx the parse tree
	 */
		fn visit_makeSeriesOperatorByClause(&mut self, ctx: &MakeSeriesOperatorByClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_mvapplyOperator(&mut self, ctx: &MvapplyOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorLimitClause}.
	 * @param ctx the parse tree
	 */
		fn visit_mvapplyOperatorLimitClause(&mut self, ctx: &MvapplyOperatorLimitClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorIdClause}.
	 * @param ctx the parse tree
	 */
		fn visit_mvapplyOperatorIdClause(&mut self, ctx: &MvapplyOperatorIdClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_mvapplyOperatorExpression(&mut self, ctx: &MvapplyOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvapplyOperatorExpressionToClause}.
	 * @param ctx the parse tree
	 */
		fn visit_mvapplyOperatorExpressionToClause(&mut self, ctx: &MvapplyOperatorExpressionToClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvexpandOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_mvexpandOperator(&mut self, ctx: &MvexpandOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#mvexpandOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_mvexpandOperatorExpression(&mut self, ctx: &MvexpandOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_parseOperator(&mut self, ctx: &ParseOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorKindClause}.
	 * @param ctx the parse tree
	 */
		fn visit_parseOperatorKindClause(&mut self, ctx: &ParseOperatorKindClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorFlagsClause}.
	 * @param ctx the parse tree
	 */
		fn visit_parseOperatorFlagsClause(&mut self, ctx: &ParseOperatorFlagsClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorNameAndOptionalType}.
	 * @param ctx the parse tree
	 */
		fn visit_parseOperatorNameAndOptionalType(&mut self, ctx: &ParseOperatorNameAndOptionalTypeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorPattern}.
	 * @param ctx the parse tree
	 */
		fn visit_parseOperatorPattern(&mut self, ctx: &ParseOperatorPatternContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseOperatorPatternSegment}.
	 * @param ctx the parse tree
	 */
		fn visit_parseOperatorPatternSegment(&mut self, ctx: &ParseOperatorPatternSegmentContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseWhereOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_parseWhereOperator(&mut self, ctx: &ParseWhereOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseKvOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_parseKvOperator(&mut self, ctx: &ParseKvOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parseKvWithClause}.
	 * @param ctx the parse tree
	 */
		fn visit_parseKvWithClause(&mut self, ctx: &ParseKvWithClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_partitionOperator(&mut self, ctx: &PartitionOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperatorInClause}.
	 * @param ctx the parse tree
	 */
		fn visit_partitionOperatorInClause(&mut self, ctx: &PartitionOperatorInClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperatorSubExpressionBody}.
	 * @param ctx the parse tree
	 */
		fn visit_partitionOperatorSubExpressionBody(&mut self, ctx: &PartitionOperatorSubExpressionBodyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionOperatorFullExpressionBody}.
	 * @param ctx the parse tree
	 */
		fn visit_partitionOperatorFullExpressionBody(&mut self, ctx: &PartitionOperatorFullExpressionBodyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionByOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_partitionByOperator(&mut self, ctx: &PartitionByOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#partitionByOperatorIdClause}.
	 * @param ctx the parse tree
	 */
		fn visit_partitionByOperatorIdClause(&mut self, ctx: &PartitionByOperatorIdClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#printOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_printOperator(&mut self, ctx: &PrintOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectAwayOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_projectAwayOperator(&mut self, ctx: &ProjectAwayOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectKeepOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_projectKeepOperator(&mut self, ctx: &ProjectKeepOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_projectOperator(&mut self, ctx: &ProjectOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectRenameOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_projectRenameOperator(&mut self, ctx: &ProjectRenameOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectReorderOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_projectReorderOperator(&mut self, ctx: &ProjectReorderOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#projectReorderExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_projectReorderExpression(&mut self, ctx: &ProjectReorderExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#reduceByOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_reduceByOperator(&mut self, ctx: &ReduceByOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#reduceByWithClause}.
	 * @param ctx the parse tree
	 */
		fn visit_reduceByWithClause(&mut self, ctx: &ReduceByWithClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_renderOperator(&mut self, ctx: &RenderOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorWithClause}.
	 * @param ctx the parse tree
	 */
		fn visit_renderOperatorWithClause(&mut self, ctx: &RenderOperatorWithClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorLegacyPropertyList}.
	 * @param ctx the parse tree
	 */
		fn visit_renderOperatorLegacyPropertyList(&mut self, ctx: &RenderOperatorLegacyPropertyListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorProperty}.
	 * @param ctx the parse tree
	 */
		fn visit_renderOperatorProperty(&mut self, ctx: &RenderOperatorPropertyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderPropertyNameList}.
	 * @param ctx the parse tree
	 */
		fn visit_renderPropertyNameList(&mut self, ctx: &RenderPropertyNameListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#renderOperatorLegacyProperty}.
	 * @param ctx the parse tree
	 */
		fn visit_renderOperatorLegacyProperty(&mut self, ctx: &RenderOperatorLegacyPropertyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#sampleDistinctOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_sampleDistinctOperator(&mut self, ctx: &SampleDistinctOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#sampleOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_sampleOperator(&mut self, ctx: &SampleOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperator(&mut self, ctx: &ScanOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorOrderByClause}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorOrderByClause(&mut self, ctx: &ScanOperatorOrderByClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorPartitionByClause}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorPartitionByClause(&mut self, ctx: &ScanOperatorPartitionByClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorDeclareClause}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorDeclareClause(&mut self, ctx: &ScanOperatorDeclareClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorStep}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorStep(&mut self, ctx: &ScanOperatorStepContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorStepOutputClause}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorStepOutputClause(&mut self, ctx: &ScanOperatorStepOutputClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorBody}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorBody(&mut self, ctx: &ScanOperatorBodyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scanOperatorAssignment}.
	 * @param ctx the parse tree
	 */
		fn visit_scanOperatorAssignment(&mut self, ctx: &ScanOperatorAssignmentContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#searchOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_searchOperator(&mut self, ctx: &SearchOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#searchOperatorStarAndExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_searchOperatorStarAndExpression(&mut self, ctx: &SearchOperatorStarAndExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#searchOperatorInClause}.
	 * @param ctx the parse tree
	 */
		fn visit_searchOperatorInClause(&mut self, ctx: &SearchOperatorInClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#serializeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_serializeOperator(&mut self, ctx: &SerializeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#sortOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_sortOperator(&mut self, ctx: &SortOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#orderedExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_orderedExpression(&mut self, ctx: &OrderedExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#sortOrdering}.
	 * @param ctx the parse tree
	 */
		fn visit_sortOrdering(&mut self, ctx: &SortOrderingContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#summarizeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_summarizeOperator(&mut self, ctx: &SummarizeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#summarizeOperatorByClause}.
	 * @param ctx the parse tree
	 */
		fn visit_summarizeOperatorByClause(&mut self, ctx: &SummarizeOperatorByClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#summarizeOperatorLegacyBinClause}.
	 * @param ctx the parse tree
	 */
		fn visit_summarizeOperatorLegacyBinClause(&mut self, ctx: &SummarizeOperatorLegacyBinClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#takeOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_takeOperator(&mut self, ctx: &TakeOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#topOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_topOperator(&mut self, ctx: &TopOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#topHittersOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_topHittersOperator(&mut self, ctx: &TopHittersOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#topHittersOperatorByClause}.
	 * @param ctx the parse tree
	 */
		fn visit_topHittersOperatorByClause(&mut self, ctx: &TopHittersOperatorByClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#topNestedOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_topNestedOperator(&mut self, ctx: &TopNestedOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#topNestedOperatorPart}.
	 * @param ctx the parse tree
	 */
		fn visit_topNestedOperatorPart(&mut self, ctx: &TopNestedOperatorPartContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#topNestedOperatorWithOthersClause}.
	 * @param ctx the parse tree
	 */
		fn visit_topNestedOperatorWithOthersClause(&mut self, ctx: &TopNestedOperatorWithOthersClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#unionOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_unionOperator(&mut self, ctx: &UnionOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#unionOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_unionOperatorExpression(&mut self, ctx: &UnionOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#whereOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_whereOperator(&mut self, ctx: &WhereOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualSubExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_contextualSubExpression(&mut self, ctx: &ContextualSubExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualPipeExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_contextualPipeExpression(&mut self, ctx: &ContextualPipeExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualPipeExpressionPipedOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_contextualPipeExpressionPipedOperator(&mut self, ctx: &ContextualPipeExpressionPipedOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#strictQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_strictQueryOperatorParameter(&mut self, ctx: &StrictQueryOperatorParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#relaxedQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_relaxedQueryOperatorParameter(&mut self, ctx: &RelaxedQueryOperatorParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#queryOperatorProperty}.
	 * @param ctx the parse tree
	 */
		fn visit_queryOperatorProperty(&mut self, ctx: &QueryOperatorPropertyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_namedExpression(&mut self, ctx: &NamedExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedExpressionNameClause}.
	 * @param ctx the parse tree
	 */
		fn visit_namedExpressionNameClause(&mut self, ctx: &NamedExpressionNameClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedExpressionNameList}.
	 * @param ctx the parse tree
	 */
		fn visit_namedExpressionNameList(&mut self, ctx: &NamedExpressionNameListContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scopedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_scopedFunctionCallExpression(&mut self, ctx: &ScopedFunctionCallExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#unnamedExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_unnamedExpression(&mut self, ctx: &UnnamedExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_logicalOrExpression(&mut self, ctx: &LogicalOrExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalOrOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_logicalOrOperation(&mut self, ctx: &LogicalOrOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_logicalAndExpression(&mut self, ctx: &LogicalAndExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#logicalAndOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_logicalAndOperation(&mut self, ctx: &LogicalAndOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_equalityExpression(&mut self, ctx: &EqualityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#equalsEqualityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_equalsEqualityExpression(&mut self, ctx: &EqualsEqualityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#listEqualityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_listEqualityExpression(&mut self, ctx: &ListEqualityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#betweenEqualityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_betweenEqualityExpression(&mut self, ctx: &BetweenEqualityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#starEqualityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_starEqualityExpression(&mut self, ctx: &StarEqualityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_relationalExpression(&mut self, ctx: &RelationalExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_additiveExpression(&mut self, ctx: &AdditiveExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#additiveOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_additiveOperation(&mut self, ctx: &AdditiveOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_multiplicativeExpression(&mut self, ctx: &MultiplicativeExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#multiplicativeOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_multiplicativeOperation(&mut self, ctx: &MultiplicativeOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_stringOperatorExpression(&mut self, ctx: &StringOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringBinaryOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_stringBinaryOperatorExpression(&mut self, ctx: &StringBinaryOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringBinaryOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_stringBinaryOperation(&mut self, ctx: &StringBinaryOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringBinaryOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_stringBinaryOperator(&mut self, ctx: &StringBinaryOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringStarOperatorExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_stringStarOperatorExpression(&mut self, ctx: &StringStarOperatorExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#invocationExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_invocationExpression(&mut self, ctx: &InvocationExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_functionCallOrPathExpression(&mut self, ctx: &FunctionCallOrPathExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathRoot}.
	 * @param ctx the parse tree
	 */
		fn visit_functionCallOrPathRoot(&mut self, ctx: &FunctionCallOrPathRootContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathPathExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_functionCallOrPathPathExpression(&mut self, ctx: &FunctionCallOrPathPathExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_functionCallOrPathOperation(&mut self, ctx: &FunctionCallOrPathOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionalCallOrPathPathOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_functionalCallOrPathPathOperation(&mut self, ctx: &FunctionalCallOrPathPathOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_functionCallOrPathElementOperation(&mut self, ctx: &FunctionCallOrPathElementOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#legacyFunctionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_legacyFunctionCallOrPathElementOperation(&mut self, ctx: &LegacyFunctionCallOrPathElementOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#toScalarExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_toScalarExpression(&mut self, ctx: &ToScalarExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#toTableExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_toTableExpression(&mut self, ctx: &ToTableExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#noOptimizationParameter}.
	 * @param ctx the parse tree
	 */
		fn visit_noOptimizationParameter(&mut self, ctx: &NoOptimizationParameterContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_dotCompositeFunctionCallExpression(&mut self, ctx: &DotCompositeFunctionCallExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallOperation}.
	 * @param ctx the parse tree
	 */
		fn visit_dotCompositeFunctionCallOperation(&mut self, ctx: &DotCompositeFunctionCallOperationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#functionCallExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_functionCallExpression(&mut self, ctx: &FunctionCallExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#namedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_namedFunctionCallExpression(&mut self, ctx: &NamedFunctionCallExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#argumentExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_argumentExpression(&mut self, ctx: &ArgumentExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#countExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_countExpression(&mut self, ctx: &CountExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#starExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_starExpression(&mut self, ctx: &StarExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_primaryExpression(&mut self, ctx: &PrimaryExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#nameReferenceWithDataScope}.
	 * @param ctx the parse tree
	 */
		fn visit_nameReferenceWithDataScope(&mut self, ctx: &NameReferenceWithDataScopeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#dataScopeClause}.
	 * @param ctx the parse tree
	 */
		fn visit_dataScopeClause(&mut self, ctx: &DataScopeClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parenthesizedExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_parenthesizedExpression(&mut self, ctx: &ParenthesizedExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#rangeExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_rangeExpression(&mut self, ctx: &RangeExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_entityExpression(&mut self, ctx: &EntityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityPathOrElementExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_entityPathOrElementExpression(&mut self, ctx: &EntityPathOrElementExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityPathOrElementOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_entityPathOrElementOperator(&mut self, ctx: &EntityPathOrElementOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityPathOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_entityPathOperator(&mut self, ctx: &EntityPathOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityElementOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_entityElementOperator(&mut self, ctx: &EntityElementOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#legacyEntityPathElementOperator}.
	 * @param ctx the parse tree
	 */
		fn visit_legacyEntityPathElementOperator(&mut self, ctx: &LegacyEntityPathElementOperatorContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityName}.
	 * @param ctx the parse tree
	 */
		fn visit_entityName(&mut self, ctx: &EntityNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#entityNameReference}.
	 * @param ctx the parse tree
	 */
		fn visit_entityNameReference(&mut self, ctx: &EntityNameReferenceContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#atSignName}.
	 * @param ctx the parse tree
	 */
		fn visit_atSignName(&mut self, ctx: &AtSignNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedPathName}.
	 * @param ctx the parse tree
	 */
		fn visit_extendedPathName(&mut self, ctx: &ExtendedPathNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedEntityExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedEntityExpression(&mut self, ctx: &WildcardedEntityExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedPathExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedPathExpression(&mut self, ctx: &WildcardedPathExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedPathName}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedPathName(&mut self, ctx: &WildcardedPathNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#contextualDataTableExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_contextualDataTableExpression(&mut self, ctx: &ContextualDataTableExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#dataTableExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_dataTableExpression(&mut self, ctx: &DataTableExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#rowSchema}.
	 * @param ctx the parse tree
	 */
		fn visit_rowSchema(&mut self, ctx: &RowSchemaContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#rowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
		fn visit_rowSchemaColumnDeclaration(&mut self, ctx: &RowSchemaColumnDeclarationContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#externalDataExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_externalDataExpression(&mut self, ctx: &ExternalDataExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#externalDataWithClause}.
	 * @param ctx the parse tree
	 */
		fn visit_externalDataWithClause(&mut self, ctx: &ExternalDataWithClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#externalDataWithClauseProperty}.
	 * @param ctx the parse tree
	 */
		fn visit_externalDataWithClauseProperty(&mut self, ctx: &ExternalDataWithClausePropertyContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializedViewCombineExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_materializedViewCombineExpression(&mut self, ctx: &MaterializedViewCombineExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializeViewCombineBaseClause}.
	 * @param ctx the parse tree
	 */
		fn visit_materializeViewCombineBaseClause(&mut self, ctx: &MaterializeViewCombineBaseClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializedViewCombineDeltaClause}.
	 * @param ctx the parse tree
	 */
		fn visit_materializedViewCombineDeltaClause(&mut self, ctx: &MaterializedViewCombineDeltaClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#materializedViewCombineAggregationsClause}.
	 * @param ctx the parse tree
	 */
		fn visit_materializedViewCombineAggregationsClause(&mut self, ctx: &MaterializedViewCombineAggregationsClauseContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#scalarType}.
	 * @param ctx the parse tree
	 */
		fn visit_scalarType(&mut self, ctx: &ScalarTypeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedScalarType}.
	 * @param ctx the parse tree
	 */
		fn visit_extendedScalarType(&mut self, ctx: &ExtendedScalarTypeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#parameterName}.
	 * @param ctx the parse tree
	 */
		fn visit_parameterName(&mut self, ctx: &ParameterNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#simpleNameReference}.
	 * @param ctx the parse tree
	 */
		fn visit_simpleNameReference(&mut self, ctx: &SimpleNameReferenceContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedNameReference}.
	 * @param ctx the parse tree
	 */
		fn visit_extendedNameReference(&mut self, ctx: &ExtendedNameReferenceContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedNameReference}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedNameReference(&mut self, ctx: &WildcardedNameReferenceContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#simpleOrWildcardedNameReference}.
	 * @param ctx the parse tree
	 */
		fn visit_simpleOrWildcardedNameReference(&mut self, ctx: &SimpleOrWildcardedNameReferenceContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierName}.
	 * @param ctx the parse tree
	 */
		fn visit_identifierName(&mut self, ctx: &IdentifierNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#keywordName}.
	 * @param ctx the parse tree
	 */
		fn visit_keywordName(&mut self, ctx: &KeywordNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#extendedKeywordName}.
	 * @param ctx the parse tree
	 */
		fn visit_extendedKeywordName(&mut self, ctx: &ExtendedKeywordNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#escapedName}.
	 * @param ctx the parse tree
	 */
		fn visit_escapedName(&mut self, ctx: &EscapedNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrKeywordName}.
	 * @param ctx the parse tree
	 */
		fn visit_identifierOrKeywordName(&mut self, ctx: &IdentifierOrKeywordNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
		fn visit_identifierOrKeywordOrEscapedName(&mut self, ctx: &IdentifierOrKeywordOrEscapedNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
		fn visit_identifierOrExtendedKeywordOrEscapedName(&mut self, ctx: &IdentifierOrExtendedKeywordOrEscapedNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordName}.
	 * @param ctx the parse tree
	 */
		fn visit_identifierOrExtendedKeywordName(&mut self, ctx: &IdentifierOrExtendedKeywordNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedName}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedName(&mut self, ctx: &WildcardedNameContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedNamePrefix}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedNamePrefix(&mut self, ctx: &WildcardedNamePrefixContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#wildcardedNameSegment}.
	 * @param ctx the parse tree
	 */
		fn visit_wildcardedNameSegment(&mut self, ctx: &WildcardedNameSegmentContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#literalExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_literalExpression(&mut self, ctx: &LiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#unsignedLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_unsignedLiteralExpression(&mut self, ctx: &UnsignedLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#numberLikeLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_numberLikeLiteralExpression(&mut self, ctx: &NumberLikeLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#numericLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_numericLiteralExpression(&mut self, ctx: &NumericLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#signedLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_signedLiteralExpression(&mut self, ctx: &SignedLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#longLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_longLiteralExpression(&mut self, ctx: &LongLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#intLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_intLiteralExpression(&mut self, ctx: &IntLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#realLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_realLiteralExpression(&mut self, ctx: &RealLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#decimalLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_decimalLiteralExpression(&mut self, ctx: &DecimalLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#dateTimeLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_dateTimeLiteralExpression(&mut self, ctx: &DateTimeLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#timeSpanLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_timeSpanLiteralExpression(&mut self, ctx: &TimeSpanLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#booleanLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_booleanLiteralExpression(&mut self, ctx: &BooleanLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#guidLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_guidLiteralExpression(&mut self, ctx: &GuidLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#typeLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_typeLiteralExpression(&mut self, ctx: &TypeLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#signedLongLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_signedLongLiteralExpression(&mut self, ctx: &SignedLongLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#signedRealLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_signedRealLiteralExpression(&mut self, ctx: &SignedRealLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#stringLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_stringLiteralExpression(&mut self, ctx: &StringLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#dynamicLiteralExpression}.
	 * @param ctx the parse tree
	 */
		fn visit_dynamicLiteralExpression(&mut self, ctx: &DynamicLiteralExpressionContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonValue}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonValue(&mut self, ctx: &JsonValueContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonObject}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonObject(&mut self, ctx: &JsonObjectContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonPair}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonPair(&mut self, ctx: &JsonPairContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonArray}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonArray(&mut self, ctx: &JsonArrayContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonBoolean}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonBoolean(&mut self, ctx: &JsonBooleanContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonDateTime}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonDateTime(&mut self, ctx: &JsonDateTimeContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonGuid}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonGuid(&mut self, ctx: &JsonGuidContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonNull}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonNull(&mut self, ctx: &JsonNullContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonString}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonString(&mut self, ctx: &JsonStringContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonTimeSpan}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonTimeSpan(&mut self, ctx: &JsonTimeSpanContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonLong}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonLong(&mut self, ctx: &JsonLongContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

	/**
	 * Visit a parse tree produced by {@link HqlParser#jsonReal}.
	 * @param ctx the parse tree
	 */
		fn visit_jsonReal(&mut self, ctx: &JsonRealContext<'input>) -> Self::Return {
			self.visit_children(ctx)
		}

}

impl<'input,T> HqlVisitor<'input> for T
where
	T: HqlVisitorCompat<'input>
{
	fn visit_top(&mut self, ctx: &TopContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_top(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_query(&mut self, ctx: &QueryContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_query(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_statement(&mut self, ctx: &StatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_statement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_aliasDatabaseStatement(&mut self, ctx: &AliasDatabaseStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_aliasDatabaseStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letStatement(&mut self, ctx: &LetStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letVariableDeclaration(&mut self, ctx: &LetVariableDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letVariableDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letFunctionDeclaration(&mut self, ctx: &LetFunctionDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letFunctionDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letViewDeclaration(&mut self, ctx: &LetViewDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letViewDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letViewParameterList(&mut self, ctx: &LetViewParameterListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letViewParameterList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letMaterializeDeclaration(&mut self, ctx: &LetMaterializeDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letMaterializeDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letEntityGroupDeclaration(&mut self, ctx: &LetEntityGroupDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letEntityGroupDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letFunctionParameterList(&mut self, ctx: &LetFunctionParameterListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letFunctionParameterList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scalarParameter(&mut self, ctx: &ScalarParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scalarParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scalarParameterDefault(&mut self, ctx: &ScalarParameterDefaultContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scalarParameterDefault(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_tabularParameter(&mut self, ctx: &TabularParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_tabularParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_tabularParameterOpenSchema(&mut self, ctx: &TabularParameterOpenSchemaContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_tabularParameterOpenSchema(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_tabularParameterRowSchema(&mut self, ctx: &TabularParameterRowSchemaContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_tabularParameterRowSchema(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_tabularParameterRowSchemaColumnDeclaration(&mut self, ctx: &TabularParameterRowSchemaColumnDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_tabularParameterRowSchemaColumnDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letFunctionBody(&mut self, ctx: &LetFunctionBodyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letFunctionBody(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_letFunctionBodyStatement(&mut self, ctx: &LetFunctionBodyStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_letFunctionBodyStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternStatement(&mut self, ctx: &DeclarePatternStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternDefinition(&mut self, ctx: &DeclarePatternDefinitionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternDefinition(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternParameterList(&mut self, ctx: &DeclarePatternParameterListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternParameterList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternParameter(&mut self, ctx: &DeclarePatternParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternPathParameter(&mut self, ctx: &DeclarePatternPathParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternPathParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternRule(&mut self, ctx: &DeclarePatternRuleContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternRule(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternRuleArgumentList(&mut self, ctx: &DeclarePatternRuleArgumentListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternRuleArgumentList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternRulePathArgument(&mut self, ctx: &DeclarePatternRulePathArgumentContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternRulePathArgument(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternRuleArgument(&mut self, ctx: &DeclarePatternRuleArgumentContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternRuleArgument(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declarePatternBody(&mut self, ctx: &DeclarePatternBodyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declarePatternBody(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_restrictAccessStatement(&mut self, ctx: &RestrictAccessStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_restrictAccessStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_restrictAccessStatementEntity(&mut self, ctx: &RestrictAccessStatementEntityContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_restrictAccessStatementEntity(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_setStatement(&mut self, ctx: &SetStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_setStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_setStatementOptionValue(&mut self, ctx: &SetStatementOptionValueContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_setStatementOptionValue(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declareQueryParametersStatement(&mut self, ctx: &DeclareQueryParametersStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declareQueryParametersStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_declareQueryParametersStatementParameter(&mut self, ctx: &DeclareQueryParametersStatementParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_declareQueryParametersStatementParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_queryStatement(&mut self, ctx: &QueryStatementContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_queryStatement(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_expression(&mut self, ctx: &ExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_expression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_pipeExpression(&mut self, ctx: &PipeExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_pipeExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_pipedOperator(&mut self, ctx: &PipedOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_pipedOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_pipeSubExpression(&mut self, ctx: &PipeSubExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_pipeSubExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_beforePipeExpression(&mut self, ctx: &BeforePipeExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_beforePipeExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_afterPipeOperator(&mut self, ctx: &AfterPipeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_afterPipeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_beforeOrAfterPipeOperator(&mut self, ctx: &BeforeOrAfterPipeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_beforeOrAfterPipeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_forkPipeOperator(&mut self, ctx: &ForkPipeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_forkPipeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_asOperator(&mut self, ctx: &AsOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_asOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_assertSchemaOperator(&mut self, ctx: &AssertSchemaOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_assertSchemaOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_consumeOperator(&mut self, ctx: &ConsumeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_consumeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_countOperator(&mut self, ctx: &CountOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_countOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_countOperatorAsClause(&mut self, ctx: &CountOperatorAsClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_countOperatorAsClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_distinctOperator(&mut self, ctx: &DistinctOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_distinctOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_distinctOperatorStarTarget(&mut self, ctx: &DistinctOperatorStarTargetContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_distinctOperatorStarTarget(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_distinctOperatorColumnListTarget(&mut self, ctx: &DistinctOperatorColumnListTargetContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_distinctOperatorColumnListTarget(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_evaluateOperator(&mut self, ctx: &EvaluateOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_evaluateOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_evaluateOperatorSchemaClause(&mut self, ctx: &EvaluateOperatorSchemaClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_evaluateOperatorSchemaClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_extendOperator(&mut self, ctx: &ExtendOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_extendOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_executeAndCacheOperator(&mut self, ctx: &ExecuteAndCacheOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_executeAndCacheOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_facetByOperator(&mut self, ctx: &FacetByOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_facetByOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_facetByOperatorWithOperatorClause(&mut self, ctx: &FacetByOperatorWithOperatorClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_facetByOperatorWithOperatorClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_facetByOperatorWithExpressionClause(&mut self, ctx: &FacetByOperatorWithExpressionClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_facetByOperatorWithExpressionClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperator(&mut self, ctx: &FindOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorParametersWhereClause(&mut self, ctx: &FindOperatorParametersWhereClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorParametersWhereClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorInClause(&mut self, ctx: &FindOperatorInClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorInClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorProjectClause(&mut self, ctx: &FindOperatorProjectClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorProjectClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorProjectExpression(&mut self, ctx: &FindOperatorProjectExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorProjectExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorColumnExpression(&mut self, ctx: &FindOperatorColumnExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorColumnExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorOptionalColumnType(&mut self, ctx: &FindOperatorOptionalColumnTypeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorOptionalColumnType(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorPackExpression(&mut self, ctx: &FindOperatorPackExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorPackExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorProjectSmartClause(&mut self, ctx: &FindOperatorProjectSmartClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorProjectSmartClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorProjectAwayClause(&mut self, ctx: &FindOperatorProjectAwayClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorProjectAwayClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorProjectAwayStar(&mut self, ctx: &FindOperatorProjectAwayStarContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorProjectAwayStar(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorProjectAwayColumnList(&mut self, ctx: &FindOperatorProjectAwayColumnListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorProjectAwayColumnList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorSource(&mut self, ctx: &FindOperatorSourceContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorSource(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_findOperatorSourceEntityExpression(&mut self, ctx: &FindOperatorSourceEntityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_findOperatorSourceEntityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_forkOperator(&mut self, ctx: &ForkOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_forkOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_forkOperatorFork(&mut self, ctx: &ForkOperatorForkContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_forkOperatorFork(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_forkOperatorExpressionName(&mut self, ctx: &ForkOperatorExpressionNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_forkOperatorExpressionName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_forkOperatorExpression(&mut self, ctx: &ForkOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_forkOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_forkOperatorPipedOperator(&mut self, ctx: &ForkOperatorPipedOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_forkOperatorPipedOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_getSchemaOperator(&mut self, ctx: &GetSchemaOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_getSchemaOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMarkComponentsOperator(&mut self, ctx: &GraphMarkComponentsOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMarkComponentsOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchOperator(&mut self, ctx: &GraphMatchOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchPattern(&mut self, ctx: &GraphMatchPatternContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchPattern(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchPatternNode(&mut self, ctx: &GraphMatchPatternNodeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchPatternNode(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchPatternUnnamedEdge(&mut self, ctx: &GraphMatchPatternUnnamedEdgeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchPatternUnnamedEdge(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchPatternNamedEdge(&mut self, ctx: &GraphMatchPatternNamedEdgeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchPatternNamedEdge(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchPatternRange(&mut self, ctx: &GraphMatchPatternRangeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchPatternRange(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchWhereClause(&mut self, ctx: &GraphMatchWhereClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchWhereClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMatchProjectClause(&mut self, ctx: &GraphMatchProjectClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMatchProjectClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphMergeOperator(&mut self, ctx: &GraphMergeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphMergeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphToTableOperator(&mut self, ctx: &GraphToTableOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphToTableOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphToTableOutput(&mut self, ctx: &GraphToTableOutputContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphToTableOutput(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphToTableAsClause(&mut self, ctx: &GraphToTableAsClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphToTableAsClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_graphShortestPathsOperator(&mut self, ctx: &GraphShortestPathsOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_graphShortestPathsOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_invokeOperator(&mut self, ctx: &InvokeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_invokeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_joinOperator(&mut self, ctx: &JoinOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_joinOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_joinOperatorOnClause(&mut self, ctx: &JoinOperatorOnClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_joinOperatorOnClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_joinOperatorWhereClause(&mut self, ctx: &JoinOperatorWhereClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_joinOperatorWhereClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_lookupOperator(&mut self, ctx: &LookupOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_lookupOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_macroExpandOperator(&mut self, ctx: &MacroExpandOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_macroExpandOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_macroExpandEntityGroup(&mut self, ctx: &MacroExpandEntityGroupContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_macroExpandEntityGroup(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityGroupExpression(&mut self, ctx: &EntityGroupExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityGroupExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeGraphOperator(&mut self, ctx: &MakeGraphOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeGraphOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeGraphIdClause(&mut self, ctx: &MakeGraphIdClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeGraphIdClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeGraphTablesAndKeysClause(&mut self, ctx: &MakeGraphTablesAndKeysClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeGraphTablesAndKeysClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeGraphPartitionedByClause(&mut self, ctx: &MakeGraphPartitionedByClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeGraphPartitionedByClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperator(&mut self, ctx: &MakeSeriesOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperatorOnClause(&mut self, ctx: &MakeSeriesOperatorOnClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperatorOnClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperatorAggregation(&mut self, ctx: &MakeSeriesOperatorAggregationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperatorAggregation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperatorExpressionDefaultClause(&mut self, ctx: &MakeSeriesOperatorExpressionDefaultClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperatorExpressionDefaultClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperatorInRangeClause(&mut self, ctx: &MakeSeriesOperatorInRangeClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperatorInRangeClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperatorFromToStepClause(&mut self, ctx: &MakeSeriesOperatorFromToStepClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperatorFromToStepClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_makeSeriesOperatorByClause(&mut self, ctx: &MakeSeriesOperatorByClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_makeSeriesOperatorByClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvapplyOperator(&mut self, ctx: &MvapplyOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvapplyOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvapplyOperatorLimitClause(&mut self, ctx: &MvapplyOperatorLimitClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvapplyOperatorLimitClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvapplyOperatorIdClause(&mut self, ctx: &MvapplyOperatorIdClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvapplyOperatorIdClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvapplyOperatorExpression(&mut self, ctx: &MvapplyOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvapplyOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvapplyOperatorExpressionToClause(&mut self, ctx: &MvapplyOperatorExpressionToClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvapplyOperatorExpressionToClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvexpandOperator(&mut self, ctx: &MvexpandOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvexpandOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_mvexpandOperatorExpression(&mut self, ctx: &MvexpandOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_mvexpandOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseOperator(&mut self, ctx: &ParseOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseOperatorKindClause(&mut self, ctx: &ParseOperatorKindClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseOperatorKindClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseOperatorFlagsClause(&mut self, ctx: &ParseOperatorFlagsClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseOperatorFlagsClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseOperatorNameAndOptionalType(&mut self, ctx: &ParseOperatorNameAndOptionalTypeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseOperatorNameAndOptionalType(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseOperatorPattern(&mut self, ctx: &ParseOperatorPatternContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseOperatorPattern(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseOperatorPatternSegment(&mut self, ctx: &ParseOperatorPatternSegmentContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseOperatorPatternSegment(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseWhereOperator(&mut self, ctx: &ParseWhereOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseWhereOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseKvOperator(&mut self, ctx: &ParseKvOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseKvOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parseKvWithClause(&mut self, ctx: &ParseKvWithClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parseKvWithClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_partitionOperator(&mut self, ctx: &PartitionOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_partitionOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_partitionOperatorInClause(&mut self, ctx: &PartitionOperatorInClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_partitionOperatorInClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_partitionOperatorSubExpressionBody(&mut self, ctx: &PartitionOperatorSubExpressionBodyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_partitionOperatorSubExpressionBody(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_partitionOperatorFullExpressionBody(&mut self, ctx: &PartitionOperatorFullExpressionBodyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_partitionOperatorFullExpressionBody(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_partitionByOperator(&mut self, ctx: &PartitionByOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_partitionByOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_partitionByOperatorIdClause(&mut self, ctx: &PartitionByOperatorIdClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_partitionByOperatorIdClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_printOperator(&mut self, ctx: &PrintOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_printOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_projectAwayOperator(&mut self, ctx: &ProjectAwayOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_projectAwayOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_projectKeepOperator(&mut self, ctx: &ProjectKeepOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_projectKeepOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_projectOperator(&mut self, ctx: &ProjectOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_projectOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_projectRenameOperator(&mut self, ctx: &ProjectRenameOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_projectRenameOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_projectReorderOperator(&mut self, ctx: &ProjectReorderOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_projectReorderOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_projectReorderExpression(&mut self, ctx: &ProjectReorderExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_projectReorderExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_reduceByOperator(&mut self, ctx: &ReduceByOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_reduceByOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_reduceByWithClause(&mut self, ctx: &ReduceByWithClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_reduceByWithClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_renderOperator(&mut self, ctx: &RenderOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_renderOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_renderOperatorWithClause(&mut self, ctx: &RenderOperatorWithClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_renderOperatorWithClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_renderOperatorLegacyPropertyList(&mut self, ctx: &RenderOperatorLegacyPropertyListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_renderOperatorLegacyPropertyList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_renderOperatorProperty(&mut self, ctx: &RenderOperatorPropertyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_renderOperatorProperty(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_renderPropertyNameList(&mut self, ctx: &RenderPropertyNameListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_renderPropertyNameList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_renderOperatorLegacyProperty(&mut self, ctx: &RenderOperatorLegacyPropertyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_renderOperatorLegacyProperty(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_sampleDistinctOperator(&mut self, ctx: &SampleDistinctOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_sampleDistinctOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_sampleOperator(&mut self, ctx: &SampleOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_sampleOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperator(&mut self, ctx: &ScanOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorOrderByClause(&mut self, ctx: &ScanOperatorOrderByClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorOrderByClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorPartitionByClause(&mut self, ctx: &ScanOperatorPartitionByClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorPartitionByClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorDeclareClause(&mut self, ctx: &ScanOperatorDeclareClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorDeclareClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorStep(&mut self, ctx: &ScanOperatorStepContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorStep(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorStepOutputClause(&mut self, ctx: &ScanOperatorStepOutputClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorStepOutputClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorBody(&mut self, ctx: &ScanOperatorBodyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorBody(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scanOperatorAssignment(&mut self, ctx: &ScanOperatorAssignmentContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scanOperatorAssignment(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_searchOperator(&mut self, ctx: &SearchOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_searchOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_searchOperatorStarAndExpression(&mut self, ctx: &SearchOperatorStarAndExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_searchOperatorStarAndExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_searchOperatorInClause(&mut self, ctx: &SearchOperatorInClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_searchOperatorInClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_serializeOperator(&mut self, ctx: &SerializeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_serializeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_sortOperator(&mut self, ctx: &SortOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_sortOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_orderedExpression(&mut self, ctx: &OrderedExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_orderedExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_sortOrdering(&mut self, ctx: &SortOrderingContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_sortOrdering(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_summarizeOperator(&mut self, ctx: &SummarizeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_summarizeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_summarizeOperatorByClause(&mut self, ctx: &SummarizeOperatorByClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_summarizeOperatorByClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_summarizeOperatorLegacyBinClause(&mut self, ctx: &SummarizeOperatorLegacyBinClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_summarizeOperatorLegacyBinClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_takeOperator(&mut self, ctx: &TakeOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_takeOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_topOperator(&mut self, ctx: &TopOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_topOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_topHittersOperator(&mut self, ctx: &TopHittersOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_topHittersOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_topHittersOperatorByClause(&mut self, ctx: &TopHittersOperatorByClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_topHittersOperatorByClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_topNestedOperator(&mut self, ctx: &TopNestedOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_topNestedOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_topNestedOperatorPart(&mut self, ctx: &TopNestedOperatorPartContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_topNestedOperatorPart(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_topNestedOperatorWithOthersClause(&mut self, ctx: &TopNestedOperatorWithOthersClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_topNestedOperatorWithOthersClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_unionOperator(&mut self, ctx: &UnionOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_unionOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_unionOperatorExpression(&mut self, ctx: &UnionOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_unionOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_whereOperator(&mut self, ctx: &WhereOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_whereOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_contextualSubExpression(&mut self, ctx: &ContextualSubExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_contextualSubExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_contextualPipeExpression(&mut self, ctx: &ContextualPipeExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_contextualPipeExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_contextualPipeExpressionPipedOperator(&mut self, ctx: &ContextualPipeExpressionPipedOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_contextualPipeExpressionPipedOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_strictQueryOperatorParameter(&mut self, ctx: &StrictQueryOperatorParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_strictQueryOperatorParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_relaxedQueryOperatorParameter(&mut self, ctx: &RelaxedQueryOperatorParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_relaxedQueryOperatorParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_queryOperatorProperty(&mut self, ctx: &QueryOperatorPropertyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_queryOperatorProperty(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_namedExpression(&mut self, ctx: &NamedExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_namedExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_namedExpressionNameClause(&mut self, ctx: &NamedExpressionNameClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_namedExpressionNameClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_namedExpressionNameList(&mut self, ctx: &NamedExpressionNameListContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_namedExpressionNameList(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scopedFunctionCallExpression(&mut self, ctx: &ScopedFunctionCallExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scopedFunctionCallExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_unnamedExpression(&mut self, ctx: &UnnamedExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_unnamedExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_logicalOrExpression(&mut self, ctx: &LogicalOrExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_logicalOrExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_logicalOrOperation(&mut self, ctx: &LogicalOrOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_logicalOrOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_logicalAndExpression(&mut self, ctx: &LogicalAndExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_logicalAndExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_logicalAndOperation(&mut self, ctx: &LogicalAndOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_logicalAndOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_equalityExpression(&mut self, ctx: &EqualityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_equalityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_equalsEqualityExpression(&mut self, ctx: &EqualsEqualityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_equalsEqualityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_listEqualityExpression(&mut self, ctx: &ListEqualityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_listEqualityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_betweenEqualityExpression(&mut self, ctx: &BetweenEqualityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_betweenEqualityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_starEqualityExpression(&mut self, ctx: &StarEqualityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_starEqualityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_relationalExpression(&mut self, ctx: &RelationalExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_relationalExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_additiveExpression(&mut self, ctx: &AdditiveExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_additiveExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_additiveOperation(&mut self, ctx: &AdditiveOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_additiveOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_multiplicativeExpression(&mut self, ctx: &MultiplicativeExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_multiplicativeExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_multiplicativeOperation(&mut self, ctx: &MultiplicativeOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_multiplicativeOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_stringOperatorExpression(&mut self, ctx: &StringOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_stringOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_stringBinaryOperatorExpression(&mut self, ctx: &StringBinaryOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_stringBinaryOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_stringBinaryOperation(&mut self, ctx: &StringBinaryOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_stringBinaryOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_stringBinaryOperator(&mut self, ctx: &StringBinaryOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_stringBinaryOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_stringStarOperatorExpression(&mut self, ctx: &StringStarOperatorExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_stringStarOperatorExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_invocationExpression(&mut self, ctx: &InvocationExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_invocationExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionCallOrPathExpression(&mut self, ctx: &FunctionCallOrPathExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionCallOrPathExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionCallOrPathRoot(&mut self, ctx: &FunctionCallOrPathRootContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionCallOrPathRoot(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionCallOrPathPathExpression(&mut self, ctx: &FunctionCallOrPathPathExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionCallOrPathPathExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionCallOrPathOperation(&mut self, ctx: &FunctionCallOrPathOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionCallOrPathOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionalCallOrPathPathOperation(&mut self, ctx: &FunctionalCallOrPathPathOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionalCallOrPathPathOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionCallOrPathElementOperation(&mut self, ctx: &FunctionCallOrPathElementOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionCallOrPathElementOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_legacyFunctionCallOrPathElementOperation(&mut self, ctx: &LegacyFunctionCallOrPathElementOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_legacyFunctionCallOrPathElementOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_toScalarExpression(&mut self, ctx: &ToScalarExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_toScalarExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_toTableExpression(&mut self, ctx: &ToTableExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_toTableExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_noOptimizationParameter(&mut self, ctx: &NoOptimizationParameterContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_noOptimizationParameter(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_dotCompositeFunctionCallExpression(&mut self, ctx: &DotCompositeFunctionCallExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_dotCompositeFunctionCallExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_dotCompositeFunctionCallOperation(&mut self, ctx: &DotCompositeFunctionCallOperationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_dotCompositeFunctionCallOperation(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_functionCallExpression(&mut self, ctx: &FunctionCallExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_functionCallExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_namedFunctionCallExpression(&mut self, ctx: &NamedFunctionCallExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_namedFunctionCallExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_argumentExpression(&mut self, ctx: &ArgumentExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_argumentExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_countExpression(&mut self, ctx: &CountExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_countExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_starExpression(&mut self, ctx: &StarExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_starExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_primaryExpression(&mut self, ctx: &PrimaryExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_primaryExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_nameReferenceWithDataScope(&mut self, ctx: &NameReferenceWithDataScopeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_nameReferenceWithDataScope(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_dataScopeClause(&mut self, ctx: &DataScopeClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_dataScopeClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parenthesizedExpression(&mut self, ctx: &ParenthesizedExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parenthesizedExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_rangeExpression(&mut self, ctx: &RangeExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_rangeExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityExpression(&mut self, ctx: &EntityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityPathOrElementExpression(&mut self, ctx: &EntityPathOrElementExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityPathOrElementExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityPathOrElementOperator(&mut self, ctx: &EntityPathOrElementOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityPathOrElementOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityPathOperator(&mut self, ctx: &EntityPathOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityPathOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityElementOperator(&mut self, ctx: &EntityElementOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityElementOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_legacyEntityPathElementOperator(&mut self, ctx: &LegacyEntityPathElementOperatorContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_legacyEntityPathElementOperator(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityName(&mut self, ctx: &EntityNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_entityNameReference(&mut self, ctx: &EntityNameReferenceContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_entityNameReference(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_atSignName(&mut self, ctx: &AtSignNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_atSignName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_extendedPathName(&mut self, ctx: &ExtendedPathNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_extendedPathName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedEntityExpression(&mut self, ctx: &WildcardedEntityExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedEntityExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedPathExpression(&mut self, ctx: &WildcardedPathExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedPathExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedPathName(&mut self, ctx: &WildcardedPathNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedPathName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_contextualDataTableExpression(&mut self, ctx: &ContextualDataTableExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_contextualDataTableExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_dataTableExpression(&mut self, ctx: &DataTableExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_dataTableExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_rowSchema(&mut self, ctx: &RowSchemaContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_rowSchema(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_rowSchemaColumnDeclaration(&mut self, ctx: &RowSchemaColumnDeclarationContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_rowSchemaColumnDeclaration(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_externalDataExpression(&mut self, ctx: &ExternalDataExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_externalDataExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_externalDataWithClause(&mut self, ctx: &ExternalDataWithClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_externalDataWithClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_externalDataWithClauseProperty(&mut self, ctx: &ExternalDataWithClausePropertyContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_externalDataWithClauseProperty(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_materializedViewCombineExpression(&mut self, ctx: &MaterializedViewCombineExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_materializedViewCombineExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_materializeViewCombineBaseClause(&mut self, ctx: &MaterializeViewCombineBaseClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_materializeViewCombineBaseClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_materializedViewCombineDeltaClause(&mut self, ctx: &MaterializedViewCombineDeltaClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_materializedViewCombineDeltaClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_materializedViewCombineAggregationsClause(&mut self, ctx: &MaterializedViewCombineAggregationsClauseContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_materializedViewCombineAggregationsClause(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_scalarType(&mut self, ctx: &ScalarTypeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_scalarType(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_extendedScalarType(&mut self, ctx: &ExtendedScalarTypeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_extendedScalarType(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_parameterName(&mut self, ctx: &ParameterNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_parameterName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_simpleNameReference(&mut self, ctx: &SimpleNameReferenceContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_simpleNameReference(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_extendedNameReference(&mut self, ctx: &ExtendedNameReferenceContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_extendedNameReference(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedNameReference(&mut self, ctx: &WildcardedNameReferenceContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedNameReference(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_simpleOrWildcardedNameReference(&mut self, ctx: &SimpleOrWildcardedNameReferenceContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_simpleOrWildcardedNameReference(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_identifierName(&mut self, ctx: &IdentifierNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_identifierName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_keywordName(&mut self, ctx: &KeywordNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_keywordName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_extendedKeywordName(&mut self, ctx: &ExtendedKeywordNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_extendedKeywordName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_escapedName(&mut self, ctx: &EscapedNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_escapedName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_identifierOrKeywordName(&mut self, ctx: &IdentifierOrKeywordNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_identifierOrKeywordName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_identifierOrKeywordOrEscapedName(&mut self, ctx: &IdentifierOrKeywordOrEscapedNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_identifierOrKeywordOrEscapedName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_identifierOrExtendedKeywordOrEscapedName(&mut self, ctx: &IdentifierOrExtendedKeywordOrEscapedNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_identifierOrExtendedKeywordOrEscapedName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_identifierOrExtendedKeywordName(&mut self, ctx: &IdentifierOrExtendedKeywordNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_identifierOrExtendedKeywordName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedName(&mut self, ctx: &WildcardedNameContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedName(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedNamePrefix(&mut self, ctx: &WildcardedNamePrefixContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedNamePrefix(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_wildcardedNameSegment(&mut self, ctx: &WildcardedNameSegmentContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_wildcardedNameSegment(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_literalExpression(&mut self, ctx: &LiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_literalExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_unsignedLiteralExpression(&mut self, ctx: &UnsignedLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_unsignedLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_numberLikeLiteralExpression(&mut self, ctx: &NumberLikeLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_numberLikeLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_numericLiteralExpression(&mut self, ctx: &NumericLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_numericLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_signedLiteralExpression(&mut self, ctx: &SignedLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_signedLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_longLiteralExpression(&mut self, ctx: &LongLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_longLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_intLiteralExpression(&mut self, ctx: &IntLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_intLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_realLiteralExpression(&mut self, ctx: &RealLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_realLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_decimalLiteralExpression(&mut self, ctx: &DecimalLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_decimalLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_dateTimeLiteralExpression(&mut self, ctx: &DateTimeLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_dateTimeLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_timeSpanLiteralExpression(&mut self, ctx: &TimeSpanLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_timeSpanLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_booleanLiteralExpression(&mut self, ctx: &BooleanLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_booleanLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_guidLiteralExpression(&mut self, ctx: &GuidLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_guidLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_typeLiteralExpression(&mut self, ctx: &TypeLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_typeLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_signedLongLiteralExpression(&mut self, ctx: &SignedLongLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_signedLongLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_signedRealLiteralExpression(&mut self, ctx: &SignedRealLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_signedRealLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_stringLiteralExpression(&mut self, ctx: &StringLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_stringLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_dynamicLiteralExpression(&mut self, ctx: &DynamicLiteralExpressionContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_dynamicLiteralExpression(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonValue(&mut self, ctx: &JsonValueContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonValue(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonObject(&mut self, ctx: &JsonObjectContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonObject(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonPair(&mut self, ctx: &JsonPairContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonPair(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonArray(&mut self, ctx: &JsonArrayContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonArray(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonBoolean(&mut self, ctx: &JsonBooleanContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonBoolean(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonDateTime(&mut self, ctx: &JsonDateTimeContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonDateTime(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonGuid(&mut self, ctx: &JsonGuidContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonGuid(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonNull(&mut self, ctx: &JsonNullContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonNull(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonString(&mut self, ctx: &JsonStringContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonString(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonTimeSpan(&mut self, ctx: &JsonTimeSpanContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonTimeSpan(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonLong(&mut self, ctx: &JsonLongContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonLong(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

	fn visit_jsonReal(&mut self, ctx: &JsonRealContext<'input>){
		let result = <Self as HqlVisitorCompat>::visit_jsonReal(self, ctx);
        *<Self as ParseTreeVisitorCompat>::temp_result(self) = result;
	}

}