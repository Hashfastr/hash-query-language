#![allow(nonstandard_style)]
// Generated from Hql.g4 by ANTLR 4.8
use antlr_rust::tree::ParseTreeListener;
use super::hqlparser::*;

pub trait HqlListener<'input> : ParseTreeListener<'input,HqlParserContextType>{
/**
 * Enter a parse tree produced by {@link HqlParser#top}.
 * @param ctx the parse tree
 */
fn enter_top(&mut self, _ctx: &TopContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#top}.
 * @param ctx the parse tree
 */
fn exit_top(&mut self, _ctx: &TopContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#query}.
 * @param ctx the parse tree
 */
fn enter_query(&mut self, _ctx: &QueryContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#query}.
 * @param ctx the parse tree
 */
fn exit_query(&mut self, _ctx: &QueryContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#statement}.
 * @param ctx the parse tree
 */
fn enter_statement(&mut self, _ctx: &StatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#statement}.
 * @param ctx the parse tree
 */
fn exit_statement(&mut self, _ctx: &StatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#aliasDatabaseStatement}.
 * @param ctx the parse tree
 */
fn enter_aliasDatabaseStatement(&mut self, _ctx: &AliasDatabaseStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#aliasDatabaseStatement}.
 * @param ctx the parse tree
 */
fn exit_aliasDatabaseStatement(&mut self, _ctx: &AliasDatabaseStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letStatement}.
 * @param ctx the parse tree
 */
fn enter_letStatement(&mut self, _ctx: &LetStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letStatement}.
 * @param ctx the parse tree
 */
fn exit_letStatement(&mut self, _ctx: &LetStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letVariableDeclaration}.
 * @param ctx the parse tree
 */
fn enter_letVariableDeclaration(&mut self, _ctx: &LetVariableDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letVariableDeclaration}.
 * @param ctx the parse tree
 */
fn exit_letVariableDeclaration(&mut self, _ctx: &LetVariableDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letFunctionDeclaration}.
 * @param ctx the parse tree
 */
fn enter_letFunctionDeclaration(&mut self, _ctx: &LetFunctionDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letFunctionDeclaration}.
 * @param ctx the parse tree
 */
fn exit_letFunctionDeclaration(&mut self, _ctx: &LetFunctionDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letViewDeclaration}.
 * @param ctx the parse tree
 */
fn enter_letViewDeclaration(&mut self, _ctx: &LetViewDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letViewDeclaration}.
 * @param ctx the parse tree
 */
fn exit_letViewDeclaration(&mut self, _ctx: &LetViewDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letViewParameterList}.
 * @param ctx the parse tree
 */
fn enter_letViewParameterList(&mut self, _ctx: &LetViewParameterListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letViewParameterList}.
 * @param ctx the parse tree
 */
fn exit_letViewParameterList(&mut self, _ctx: &LetViewParameterListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letMaterializeDeclaration}.
 * @param ctx the parse tree
 */
fn enter_letMaterializeDeclaration(&mut self, _ctx: &LetMaterializeDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letMaterializeDeclaration}.
 * @param ctx the parse tree
 */
fn exit_letMaterializeDeclaration(&mut self, _ctx: &LetMaterializeDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letEntityGroupDeclaration}.
 * @param ctx the parse tree
 */
fn enter_letEntityGroupDeclaration(&mut self, _ctx: &LetEntityGroupDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letEntityGroupDeclaration}.
 * @param ctx the parse tree
 */
fn exit_letEntityGroupDeclaration(&mut self, _ctx: &LetEntityGroupDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letFunctionParameterList}.
 * @param ctx the parse tree
 */
fn enter_letFunctionParameterList(&mut self, _ctx: &LetFunctionParameterListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letFunctionParameterList}.
 * @param ctx the parse tree
 */
fn exit_letFunctionParameterList(&mut self, _ctx: &LetFunctionParameterListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scalarParameter}.
 * @param ctx the parse tree
 */
fn enter_scalarParameter(&mut self, _ctx: &ScalarParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scalarParameter}.
 * @param ctx the parse tree
 */
fn exit_scalarParameter(&mut self, _ctx: &ScalarParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scalarParameterDefault}.
 * @param ctx the parse tree
 */
fn enter_scalarParameterDefault(&mut self, _ctx: &ScalarParameterDefaultContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scalarParameterDefault}.
 * @param ctx the parse tree
 */
fn exit_scalarParameterDefault(&mut self, _ctx: &ScalarParameterDefaultContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#tabularParameter}.
 * @param ctx the parse tree
 */
fn enter_tabularParameter(&mut self, _ctx: &TabularParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#tabularParameter}.
 * @param ctx the parse tree
 */
fn exit_tabularParameter(&mut self, _ctx: &TabularParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#tabularParameterOpenSchema}.
 * @param ctx the parse tree
 */
fn enter_tabularParameterOpenSchema(&mut self, _ctx: &TabularParameterOpenSchemaContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#tabularParameterOpenSchema}.
 * @param ctx the parse tree
 */
fn exit_tabularParameterOpenSchema(&mut self, _ctx: &TabularParameterOpenSchemaContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#tabularParameterRowSchema}.
 * @param ctx the parse tree
 */
fn enter_tabularParameterRowSchema(&mut self, _ctx: &TabularParameterRowSchemaContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#tabularParameterRowSchema}.
 * @param ctx the parse tree
 */
fn exit_tabularParameterRowSchema(&mut self, _ctx: &TabularParameterRowSchemaContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#tabularParameterRowSchemaColumnDeclaration}.
 * @param ctx the parse tree
 */
fn enter_tabularParameterRowSchemaColumnDeclaration(&mut self, _ctx: &TabularParameterRowSchemaColumnDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#tabularParameterRowSchemaColumnDeclaration}.
 * @param ctx the parse tree
 */
fn exit_tabularParameterRowSchemaColumnDeclaration(&mut self, _ctx: &TabularParameterRowSchemaColumnDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letFunctionBody}.
 * @param ctx the parse tree
 */
fn enter_letFunctionBody(&mut self, _ctx: &LetFunctionBodyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letFunctionBody}.
 * @param ctx the parse tree
 */
fn exit_letFunctionBody(&mut self, _ctx: &LetFunctionBodyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#letFunctionBodyStatement}.
 * @param ctx the parse tree
 */
fn enter_letFunctionBodyStatement(&mut self, _ctx: &LetFunctionBodyStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#letFunctionBodyStatement}.
 * @param ctx the parse tree
 */
fn exit_letFunctionBodyStatement(&mut self, _ctx: &LetFunctionBodyStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternStatement}.
 * @param ctx the parse tree
 */
fn enter_declarePatternStatement(&mut self, _ctx: &DeclarePatternStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternStatement}.
 * @param ctx the parse tree
 */
fn exit_declarePatternStatement(&mut self, _ctx: &DeclarePatternStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternDefinition}.
 * @param ctx the parse tree
 */
fn enter_declarePatternDefinition(&mut self, _ctx: &DeclarePatternDefinitionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternDefinition}.
 * @param ctx the parse tree
 */
fn exit_declarePatternDefinition(&mut self, _ctx: &DeclarePatternDefinitionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternParameterList}.
 * @param ctx the parse tree
 */
fn enter_declarePatternParameterList(&mut self, _ctx: &DeclarePatternParameterListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternParameterList}.
 * @param ctx the parse tree
 */
fn exit_declarePatternParameterList(&mut self, _ctx: &DeclarePatternParameterListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternParameter}.
 * @param ctx the parse tree
 */
fn enter_declarePatternParameter(&mut self, _ctx: &DeclarePatternParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternParameter}.
 * @param ctx the parse tree
 */
fn exit_declarePatternParameter(&mut self, _ctx: &DeclarePatternParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternPathParameter}.
 * @param ctx the parse tree
 */
fn enter_declarePatternPathParameter(&mut self, _ctx: &DeclarePatternPathParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternPathParameter}.
 * @param ctx the parse tree
 */
fn exit_declarePatternPathParameter(&mut self, _ctx: &DeclarePatternPathParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternRule}.
 * @param ctx the parse tree
 */
fn enter_declarePatternRule(&mut self, _ctx: &DeclarePatternRuleContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternRule}.
 * @param ctx the parse tree
 */
fn exit_declarePatternRule(&mut self, _ctx: &DeclarePatternRuleContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternRuleArgumentList}.
 * @param ctx the parse tree
 */
fn enter_declarePatternRuleArgumentList(&mut self, _ctx: &DeclarePatternRuleArgumentListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternRuleArgumentList}.
 * @param ctx the parse tree
 */
fn exit_declarePatternRuleArgumentList(&mut self, _ctx: &DeclarePatternRuleArgumentListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternRulePathArgument}.
 * @param ctx the parse tree
 */
fn enter_declarePatternRulePathArgument(&mut self, _ctx: &DeclarePatternRulePathArgumentContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternRulePathArgument}.
 * @param ctx the parse tree
 */
fn exit_declarePatternRulePathArgument(&mut self, _ctx: &DeclarePatternRulePathArgumentContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternRuleArgument}.
 * @param ctx the parse tree
 */
fn enter_declarePatternRuleArgument(&mut self, _ctx: &DeclarePatternRuleArgumentContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternRuleArgument}.
 * @param ctx the parse tree
 */
fn exit_declarePatternRuleArgument(&mut self, _ctx: &DeclarePatternRuleArgumentContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declarePatternBody}.
 * @param ctx the parse tree
 */
fn enter_declarePatternBody(&mut self, _ctx: &DeclarePatternBodyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declarePatternBody}.
 * @param ctx the parse tree
 */
fn exit_declarePatternBody(&mut self, _ctx: &DeclarePatternBodyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#restrictAccessStatement}.
 * @param ctx the parse tree
 */
fn enter_restrictAccessStatement(&mut self, _ctx: &RestrictAccessStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#restrictAccessStatement}.
 * @param ctx the parse tree
 */
fn exit_restrictAccessStatement(&mut self, _ctx: &RestrictAccessStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#restrictAccessStatementEntity}.
 * @param ctx the parse tree
 */
fn enter_restrictAccessStatementEntity(&mut self, _ctx: &RestrictAccessStatementEntityContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#restrictAccessStatementEntity}.
 * @param ctx the parse tree
 */
fn exit_restrictAccessStatementEntity(&mut self, _ctx: &RestrictAccessStatementEntityContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#setStatement}.
 * @param ctx the parse tree
 */
fn enter_setStatement(&mut self, _ctx: &SetStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#setStatement}.
 * @param ctx the parse tree
 */
fn exit_setStatement(&mut self, _ctx: &SetStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#setStatementOptionValue}.
 * @param ctx the parse tree
 */
fn enter_setStatementOptionValue(&mut self, _ctx: &SetStatementOptionValueContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#setStatementOptionValue}.
 * @param ctx the parse tree
 */
fn exit_setStatementOptionValue(&mut self, _ctx: &SetStatementOptionValueContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declareQueryParametersStatement}.
 * @param ctx the parse tree
 */
fn enter_declareQueryParametersStatement(&mut self, _ctx: &DeclareQueryParametersStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declareQueryParametersStatement}.
 * @param ctx the parse tree
 */
fn exit_declareQueryParametersStatement(&mut self, _ctx: &DeclareQueryParametersStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#declareQueryParametersStatementParameter}.
 * @param ctx the parse tree
 */
fn enter_declareQueryParametersStatementParameter(&mut self, _ctx: &DeclareQueryParametersStatementParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#declareQueryParametersStatementParameter}.
 * @param ctx the parse tree
 */
fn exit_declareQueryParametersStatementParameter(&mut self, _ctx: &DeclareQueryParametersStatementParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#queryStatement}.
 * @param ctx the parse tree
 */
fn enter_queryStatement(&mut self, _ctx: &QueryStatementContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#queryStatement}.
 * @param ctx the parse tree
 */
fn exit_queryStatement(&mut self, _ctx: &QueryStatementContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#expression}.
 * @param ctx the parse tree
 */
fn enter_expression(&mut self, _ctx: &ExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#expression}.
 * @param ctx the parse tree
 */
fn exit_expression(&mut self, _ctx: &ExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#pipeExpression}.
 * @param ctx the parse tree
 */
fn enter_pipeExpression(&mut self, _ctx: &PipeExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#pipeExpression}.
 * @param ctx the parse tree
 */
fn exit_pipeExpression(&mut self, _ctx: &PipeExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#pipedOperator}.
 * @param ctx the parse tree
 */
fn enter_pipedOperator(&mut self, _ctx: &PipedOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#pipedOperator}.
 * @param ctx the parse tree
 */
fn exit_pipedOperator(&mut self, _ctx: &PipedOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#pipeSubExpression}.
 * @param ctx the parse tree
 */
fn enter_pipeSubExpression(&mut self, _ctx: &PipeSubExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#pipeSubExpression}.
 * @param ctx the parse tree
 */
fn exit_pipeSubExpression(&mut self, _ctx: &PipeSubExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#beforePipeExpression}.
 * @param ctx the parse tree
 */
fn enter_beforePipeExpression(&mut self, _ctx: &BeforePipeExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#beforePipeExpression}.
 * @param ctx the parse tree
 */
fn exit_beforePipeExpression(&mut self, _ctx: &BeforePipeExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#afterPipeOperator}.
 * @param ctx the parse tree
 */
fn enter_afterPipeOperator(&mut self, _ctx: &AfterPipeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#afterPipeOperator}.
 * @param ctx the parse tree
 */
fn exit_afterPipeOperator(&mut self, _ctx: &AfterPipeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#beforeOrAfterPipeOperator}.
 * @param ctx the parse tree
 */
fn enter_beforeOrAfterPipeOperator(&mut self, _ctx: &BeforeOrAfterPipeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#beforeOrAfterPipeOperator}.
 * @param ctx the parse tree
 */
fn exit_beforeOrAfterPipeOperator(&mut self, _ctx: &BeforeOrAfterPipeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#forkPipeOperator}.
 * @param ctx the parse tree
 */
fn enter_forkPipeOperator(&mut self, _ctx: &ForkPipeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#forkPipeOperator}.
 * @param ctx the parse tree
 */
fn exit_forkPipeOperator(&mut self, _ctx: &ForkPipeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#asOperator}.
 * @param ctx the parse tree
 */
fn enter_asOperator(&mut self, _ctx: &AsOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#asOperator}.
 * @param ctx the parse tree
 */
fn exit_asOperator(&mut self, _ctx: &AsOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#assertSchemaOperator}.
 * @param ctx the parse tree
 */
fn enter_assertSchemaOperator(&mut self, _ctx: &AssertSchemaOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#assertSchemaOperator}.
 * @param ctx the parse tree
 */
fn exit_assertSchemaOperator(&mut self, _ctx: &AssertSchemaOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#consumeOperator}.
 * @param ctx the parse tree
 */
fn enter_consumeOperator(&mut self, _ctx: &ConsumeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#consumeOperator}.
 * @param ctx the parse tree
 */
fn exit_consumeOperator(&mut self, _ctx: &ConsumeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#countOperator}.
 * @param ctx the parse tree
 */
fn enter_countOperator(&mut self, _ctx: &CountOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#countOperator}.
 * @param ctx the parse tree
 */
fn exit_countOperator(&mut self, _ctx: &CountOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#countOperatorAsClause}.
 * @param ctx the parse tree
 */
fn enter_countOperatorAsClause(&mut self, _ctx: &CountOperatorAsClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#countOperatorAsClause}.
 * @param ctx the parse tree
 */
fn exit_countOperatorAsClause(&mut self, _ctx: &CountOperatorAsClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#distinctOperator}.
 * @param ctx the parse tree
 */
fn enter_distinctOperator(&mut self, _ctx: &DistinctOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#distinctOperator}.
 * @param ctx the parse tree
 */
fn exit_distinctOperator(&mut self, _ctx: &DistinctOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#distinctOperatorStarTarget}.
 * @param ctx the parse tree
 */
fn enter_distinctOperatorStarTarget(&mut self, _ctx: &DistinctOperatorStarTargetContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#distinctOperatorStarTarget}.
 * @param ctx the parse tree
 */
fn exit_distinctOperatorStarTarget(&mut self, _ctx: &DistinctOperatorStarTargetContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#distinctOperatorColumnListTarget}.
 * @param ctx the parse tree
 */
fn enter_distinctOperatorColumnListTarget(&mut self, _ctx: &DistinctOperatorColumnListTargetContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#distinctOperatorColumnListTarget}.
 * @param ctx the parse tree
 */
fn exit_distinctOperatorColumnListTarget(&mut self, _ctx: &DistinctOperatorColumnListTargetContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#evaluateOperator}.
 * @param ctx the parse tree
 */
fn enter_evaluateOperator(&mut self, _ctx: &EvaluateOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#evaluateOperator}.
 * @param ctx the parse tree
 */
fn exit_evaluateOperator(&mut self, _ctx: &EvaluateOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#evaluateOperatorSchemaClause}.
 * @param ctx the parse tree
 */
fn enter_evaluateOperatorSchemaClause(&mut self, _ctx: &EvaluateOperatorSchemaClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#evaluateOperatorSchemaClause}.
 * @param ctx the parse tree
 */
fn exit_evaluateOperatorSchemaClause(&mut self, _ctx: &EvaluateOperatorSchemaClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#extendOperator}.
 * @param ctx the parse tree
 */
fn enter_extendOperator(&mut self, _ctx: &ExtendOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#extendOperator}.
 * @param ctx the parse tree
 */
fn exit_extendOperator(&mut self, _ctx: &ExtendOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#executeAndCacheOperator}.
 * @param ctx the parse tree
 */
fn enter_executeAndCacheOperator(&mut self, _ctx: &ExecuteAndCacheOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#executeAndCacheOperator}.
 * @param ctx the parse tree
 */
fn exit_executeAndCacheOperator(&mut self, _ctx: &ExecuteAndCacheOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#facetByOperator}.
 * @param ctx the parse tree
 */
fn enter_facetByOperator(&mut self, _ctx: &FacetByOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#facetByOperator}.
 * @param ctx the parse tree
 */
fn exit_facetByOperator(&mut self, _ctx: &FacetByOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#facetByOperatorWithOperatorClause}.
 * @param ctx the parse tree
 */
fn enter_facetByOperatorWithOperatorClause(&mut self, _ctx: &FacetByOperatorWithOperatorClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#facetByOperatorWithOperatorClause}.
 * @param ctx the parse tree
 */
fn exit_facetByOperatorWithOperatorClause(&mut self, _ctx: &FacetByOperatorWithOperatorClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#facetByOperatorWithExpressionClause}.
 * @param ctx the parse tree
 */
fn enter_facetByOperatorWithExpressionClause(&mut self, _ctx: &FacetByOperatorWithExpressionClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#facetByOperatorWithExpressionClause}.
 * @param ctx the parse tree
 */
fn exit_facetByOperatorWithExpressionClause(&mut self, _ctx: &FacetByOperatorWithExpressionClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperator}.
 * @param ctx the parse tree
 */
fn enter_findOperator(&mut self, _ctx: &FindOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperator}.
 * @param ctx the parse tree
 */
fn exit_findOperator(&mut self, _ctx: &FindOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorParametersWhereClause}.
 * @param ctx the parse tree
 */
fn enter_findOperatorParametersWhereClause(&mut self, _ctx: &FindOperatorParametersWhereClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorParametersWhereClause}.
 * @param ctx the parse tree
 */
fn exit_findOperatorParametersWhereClause(&mut self, _ctx: &FindOperatorParametersWhereClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorInClause}.
 * @param ctx the parse tree
 */
fn enter_findOperatorInClause(&mut self, _ctx: &FindOperatorInClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorInClause}.
 * @param ctx the parse tree
 */
fn exit_findOperatorInClause(&mut self, _ctx: &FindOperatorInClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectClause}.
 * @param ctx the parse tree
 */
fn enter_findOperatorProjectClause(&mut self, _ctx: &FindOperatorProjectClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectClause}.
 * @param ctx the parse tree
 */
fn exit_findOperatorProjectClause(&mut self, _ctx: &FindOperatorProjectClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectExpression}.
 * @param ctx the parse tree
 */
fn enter_findOperatorProjectExpression(&mut self, _ctx: &FindOperatorProjectExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectExpression}.
 * @param ctx the parse tree
 */
fn exit_findOperatorProjectExpression(&mut self, _ctx: &FindOperatorProjectExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorColumnExpression}.
 * @param ctx the parse tree
 */
fn enter_findOperatorColumnExpression(&mut self, _ctx: &FindOperatorColumnExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorColumnExpression}.
 * @param ctx the parse tree
 */
fn exit_findOperatorColumnExpression(&mut self, _ctx: &FindOperatorColumnExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorOptionalColumnType}.
 * @param ctx the parse tree
 */
fn enter_findOperatorOptionalColumnType(&mut self, _ctx: &FindOperatorOptionalColumnTypeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorOptionalColumnType}.
 * @param ctx the parse tree
 */
fn exit_findOperatorOptionalColumnType(&mut self, _ctx: &FindOperatorOptionalColumnTypeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorPackExpression}.
 * @param ctx the parse tree
 */
fn enter_findOperatorPackExpression(&mut self, _ctx: &FindOperatorPackExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorPackExpression}.
 * @param ctx the parse tree
 */
fn exit_findOperatorPackExpression(&mut self, _ctx: &FindOperatorPackExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectSmartClause}.
 * @param ctx the parse tree
 */
fn enter_findOperatorProjectSmartClause(&mut self, _ctx: &FindOperatorProjectSmartClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectSmartClause}.
 * @param ctx the parse tree
 */
fn exit_findOperatorProjectSmartClause(&mut self, _ctx: &FindOperatorProjectSmartClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectAwayClause}.
 * @param ctx the parse tree
 */
fn enter_findOperatorProjectAwayClause(&mut self, _ctx: &FindOperatorProjectAwayClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectAwayClause}.
 * @param ctx the parse tree
 */
fn exit_findOperatorProjectAwayClause(&mut self, _ctx: &FindOperatorProjectAwayClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectAwayStar}.
 * @param ctx the parse tree
 */
fn enter_findOperatorProjectAwayStar(&mut self, _ctx: &FindOperatorProjectAwayStarContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectAwayStar}.
 * @param ctx the parse tree
 */
fn exit_findOperatorProjectAwayStar(&mut self, _ctx: &FindOperatorProjectAwayStarContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectAwayColumnList}.
 * @param ctx the parse tree
 */
fn enter_findOperatorProjectAwayColumnList(&mut self, _ctx: &FindOperatorProjectAwayColumnListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectAwayColumnList}.
 * @param ctx the parse tree
 */
fn exit_findOperatorProjectAwayColumnList(&mut self, _ctx: &FindOperatorProjectAwayColumnListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorSource}.
 * @param ctx the parse tree
 */
fn enter_findOperatorSource(&mut self, _ctx: &FindOperatorSourceContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorSource}.
 * @param ctx the parse tree
 */
fn exit_findOperatorSource(&mut self, _ctx: &FindOperatorSourceContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#findOperatorSourceEntityExpression}.
 * @param ctx the parse tree
 */
fn enter_findOperatorSourceEntityExpression(&mut self, _ctx: &FindOperatorSourceEntityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#findOperatorSourceEntityExpression}.
 * @param ctx the parse tree
 */
fn exit_findOperatorSourceEntityExpression(&mut self, _ctx: &FindOperatorSourceEntityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#forkOperator}.
 * @param ctx the parse tree
 */
fn enter_forkOperator(&mut self, _ctx: &ForkOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#forkOperator}.
 * @param ctx the parse tree
 */
fn exit_forkOperator(&mut self, _ctx: &ForkOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#forkOperatorFork}.
 * @param ctx the parse tree
 */
fn enter_forkOperatorFork(&mut self, _ctx: &ForkOperatorForkContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#forkOperatorFork}.
 * @param ctx the parse tree
 */
fn exit_forkOperatorFork(&mut self, _ctx: &ForkOperatorForkContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#forkOperatorExpressionName}.
 * @param ctx the parse tree
 */
fn enter_forkOperatorExpressionName(&mut self, _ctx: &ForkOperatorExpressionNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#forkOperatorExpressionName}.
 * @param ctx the parse tree
 */
fn exit_forkOperatorExpressionName(&mut self, _ctx: &ForkOperatorExpressionNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#forkOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_forkOperatorExpression(&mut self, _ctx: &ForkOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#forkOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_forkOperatorExpression(&mut self, _ctx: &ForkOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#forkOperatorPipedOperator}.
 * @param ctx the parse tree
 */
fn enter_forkOperatorPipedOperator(&mut self, _ctx: &ForkOperatorPipedOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#forkOperatorPipedOperator}.
 * @param ctx the parse tree
 */
fn exit_forkOperatorPipedOperator(&mut self, _ctx: &ForkOperatorPipedOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#getSchemaOperator}.
 * @param ctx the parse tree
 */
fn enter_getSchemaOperator(&mut self, _ctx: &GetSchemaOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#getSchemaOperator}.
 * @param ctx the parse tree
 */
fn exit_getSchemaOperator(&mut self, _ctx: &GetSchemaOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMarkComponentsOperator}.
 * @param ctx the parse tree
 */
fn enter_graphMarkComponentsOperator(&mut self, _ctx: &GraphMarkComponentsOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMarkComponentsOperator}.
 * @param ctx the parse tree
 */
fn exit_graphMarkComponentsOperator(&mut self, _ctx: &GraphMarkComponentsOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchOperator}.
 * @param ctx the parse tree
 */
fn enter_graphMatchOperator(&mut self, _ctx: &GraphMatchOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchOperator}.
 * @param ctx the parse tree
 */
fn exit_graphMatchOperator(&mut self, _ctx: &GraphMatchOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchPattern}.
 * @param ctx the parse tree
 */
fn enter_graphMatchPattern(&mut self, _ctx: &GraphMatchPatternContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchPattern}.
 * @param ctx the parse tree
 */
fn exit_graphMatchPattern(&mut self, _ctx: &GraphMatchPatternContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternNode}.
 * @param ctx the parse tree
 */
fn enter_graphMatchPatternNode(&mut self, _ctx: &GraphMatchPatternNodeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternNode}.
 * @param ctx the parse tree
 */
fn exit_graphMatchPatternNode(&mut self, _ctx: &GraphMatchPatternNodeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternUnnamedEdge}.
 * @param ctx the parse tree
 */
fn enter_graphMatchPatternUnnamedEdge(&mut self, _ctx: &GraphMatchPatternUnnamedEdgeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternUnnamedEdge}.
 * @param ctx the parse tree
 */
fn exit_graphMatchPatternUnnamedEdge(&mut self, _ctx: &GraphMatchPatternUnnamedEdgeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternNamedEdge}.
 * @param ctx the parse tree
 */
fn enter_graphMatchPatternNamedEdge(&mut self, _ctx: &GraphMatchPatternNamedEdgeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternNamedEdge}.
 * @param ctx the parse tree
 */
fn exit_graphMatchPatternNamedEdge(&mut self, _ctx: &GraphMatchPatternNamedEdgeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternRange}.
 * @param ctx the parse tree
 */
fn enter_graphMatchPatternRange(&mut self, _ctx: &GraphMatchPatternRangeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternRange}.
 * @param ctx the parse tree
 */
fn exit_graphMatchPatternRange(&mut self, _ctx: &GraphMatchPatternRangeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchWhereClause}.
 * @param ctx the parse tree
 */
fn enter_graphMatchWhereClause(&mut self, _ctx: &GraphMatchWhereClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchWhereClause}.
 * @param ctx the parse tree
 */
fn exit_graphMatchWhereClause(&mut self, _ctx: &GraphMatchWhereClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMatchProjectClause}.
 * @param ctx the parse tree
 */
fn enter_graphMatchProjectClause(&mut self, _ctx: &GraphMatchProjectClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMatchProjectClause}.
 * @param ctx the parse tree
 */
fn exit_graphMatchProjectClause(&mut self, _ctx: &GraphMatchProjectClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphMergeOperator}.
 * @param ctx the parse tree
 */
fn enter_graphMergeOperator(&mut self, _ctx: &GraphMergeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphMergeOperator}.
 * @param ctx the parse tree
 */
fn exit_graphMergeOperator(&mut self, _ctx: &GraphMergeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphToTableOperator}.
 * @param ctx the parse tree
 */
fn enter_graphToTableOperator(&mut self, _ctx: &GraphToTableOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphToTableOperator}.
 * @param ctx the parse tree
 */
fn exit_graphToTableOperator(&mut self, _ctx: &GraphToTableOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphToTableOutput}.
 * @param ctx the parse tree
 */
fn enter_graphToTableOutput(&mut self, _ctx: &GraphToTableOutputContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphToTableOutput}.
 * @param ctx the parse tree
 */
fn exit_graphToTableOutput(&mut self, _ctx: &GraphToTableOutputContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphToTableAsClause}.
 * @param ctx the parse tree
 */
fn enter_graphToTableAsClause(&mut self, _ctx: &GraphToTableAsClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphToTableAsClause}.
 * @param ctx the parse tree
 */
fn exit_graphToTableAsClause(&mut self, _ctx: &GraphToTableAsClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#graphShortestPathsOperator}.
 * @param ctx the parse tree
 */
fn enter_graphShortestPathsOperator(&mut self, _ctx: &GraphShortestPathsOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#graphShortestPathsOperator}.
 * @param ctx the parse tree
 */
fn exit_graphShortestPathsOperator(&mut self, _ctx: &GraphShortestPathsOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#invokeOperator}.
 * @param ctx the parse tree
 */
fn enter_invokeOperator(&mut self, _ctx: &InvokeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#invokeOperator}.
 * @param ctx the parse tree
 */
fn exit_invokeOperator(&mut self, _ctx: &InvokeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#joinOperator}.
 * @param ctx the parse tree
 */
fn enter_joinOperator(&mut self, _ctx: &JoinOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#joinOperator}.
 * @param ctx the parse tree
 */
fn exit_joinOperator(&mut self, _ctx: &JoinOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#joinOperatorOnClause}.
 * @param ctx the parse tree
 */
fn enter_joinOperatorOnClause(&mut self, _ctx: &JoinOperatorOnClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#joinOperatorOnClause}.
 * @param ctx the parse tree
 */
fn exit_joinOperatorOnClause(&mut self, _ctx: &JoinOperatorOnClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#joinOperatorWhereClause}.
 * @param ctx the parse tree
 */
fn enter_joinOperatorWhereClause(&mut self, _ctx: &JoinOperatorWhereClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#joinOperatorWhereClause}.
 * @param ctx the parse tree
 */
fn exit_joinOperatorWhereClause(&mut self, _ctx: &JoinOperatorWhereClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#lookupOperator}.
 * @param ctx the parse tree
 */
fn enter_lookupOperator(&mut self, _ctx: &LookupOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#lookupOperator}.
 * @param ctx the parse tree
 */
fn exit_lookupOperator(&mut self, _ctx: &LookupOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#macroExpandOperator}.
 * @param ctx the parse tree
 */
fn enter_macroExpandOperator(&mut self, _ctx: &MacroExpandOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#macroExpandOperator}.
 * @param ctx the parse tree
 */
fn exit_macroExpandOperator(&mut self, _ctx: &MacroExpandOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#macroExpandEntityGroup}.
 * @param ctx the parse tree
 */
fn enter_macroExpandEntityGroup(&mut self, _ctx: &MacroExpandEntityGroupContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#macroExpandEntityGroup}.
 * @param ctx the parse tree
 */
fn exit_macroExpandEntityGroup(&mut self, _ctx: &MacroExpandEntityGroupContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityGroupExpression}.
 * @param ctx the parse tree
 */
fn enter_entityGroupExpression(&mut self, _ctx: &EntityGroupExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityGroupExpression}.
 * @param ctx the parse tree
 */
fn exit_entityGroupExpression(&mut self, _ctx: &EntityGroupExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeGraphOperator}.
 * @param ctx the parse tree
 */
fn enter_makeGraphOperator(&mut self, _ctx: &MakeGraphOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeGraphOperator}.
 * @param ctx the parse tree
 */
fn exit_makeGraphOperator(&mut self, _ctx: &MakeGraphOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeGraphIdClause}.
 * @param ctx the parse tree
 */
fn enter_makeGraphIdClause(&mut self, _ctx: &MakeGraphIdClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeGraphIdClause}.
 * @param ctx the parse tree
 */
fn exit_makeGraphIdClause(&mut self, _ctx: &MakeGraphIdClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeGraphTablesAndKeysClause}.
 * @param ctx the parse tree
 */
fn enter_makeGraphTablesAndKeysClause(&mut self, _ctx: &MakeGraphTablesAndKeysClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeGraphTablesAndKeysClause}.
 * @param ctx the parse tree
 */
fn exit_makeGraphTablesAndKeysClause(&mut self, _ctx: &MakeGraphTablesAndKeysClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeGraphPartitionedByClause}.
 * @param ctx the parse tree
 */
fn enter_makeGraphPartitionedByClause(&mut self, _ctx: &MakeGraphPartitionedByClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeGraphPartitionedByClause}.
 * @param ctx the parse tree
 */
fn exit_makeGraphPartitionedByClause(&mut self, _ctx: &MakeGraphPartitionedByClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperator}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperator(&mut self, _ctx: &MakeSeriesOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperator}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperator(&mut self, _ctx: &MakeSeriesOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorOnClause}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperatorOnClause(&mut self, _ctx: &MakeSeriesOperatorOnClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorOnClause}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperatorOnClause(&mut self, _ctx: &MakeSeriesOperatorOnClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorAggregation}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperatorAggregation(&mut self, _ctx: &MakeSeriesOperatorAggregationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorAggregation}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperatorAggregation(&mut self, _ctx: &MakeSeriesOperatorAggregationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorExpressionDefaultClause}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperatorExpressionDefaultClause(&mut self, _ctx: &MakeSeriesOperatorExpressionDefaultClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorExpressionDefaultClause}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperatorExpressionDefaultClause(&mut self, _ctx: &MakeSeriesOperatorExpressionDefaultClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorInRangeClause}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperatorInRangeClause(&mut self, _ctx: &MakeSeriesOperatorInRangeClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorInRangeClause}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperatorInRangeClause(&mut self, _ctx: &MakeSeriesOperatorInRangeClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorFromToStepClause}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperatorFromToStepClause(&mut self, _ctx: &MakeSeriesOperatorFromToStepClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorFromToStepClause}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperatorFromToStepClause(&mut self, _ctx: &MakeSeriesOperatorFromToStepClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorByClause}.
 * @param ctx the parse tree
 */
fn enter_makeSeriesOperatorByClause(&mut self, _ctx: &MakeSeriesOperatorByClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorByClause}.
 * @param ctx the parse tree
 */
fn exit_makeSeriesOperatorByClause(&mut self, _ctx: &MakeSeriesOperatorByClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvapplyOperator}.
 * @param ctx the parse tree
 */
fn enter_mvapplyOperator(&mut self, _ctx: &MvapplyOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvapplyOperator}.
 * @param ctx the parse tree
 */
fn exit_mvapplyOperator(&mut self, _ctx: &MvapplyOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorLimitClause}.
 * @param ctx the parse tree
 */
fn enter_mvapplyOperatorLimitClause(&mut self, _ctx: &MvapplyOperatorLimitClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorLimitClause}.
 * @param ctx the parse tree
 */
fn exit_mvapplyOperatorLimitClause(&mut self, _ctx: &MvapplyOperatorLimitClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorIdClause}.
 * @param ctx the parse tree
 */
fn enter_mvapplyOperatorIdClause(&mut self, _ctx: &MvapplyOperatorIdClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorIdClause}.
 * @param ctx the parse tree
 */
fn exit_mvapplyOperatorIdClause(&mut self, _ctx: &MvapplyOperatorIdClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_mvapplyOperatorExpression(&mut self, _ctx: &MvapplyOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_mvapplyOperatorExpression(&mut self, _ctx: &MvapplyOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorExpressionToClause}.
 * @param ctx the parse tree
 */
fn enter_mvapplyOperatorExpressionToClause(&mut self, _ctx: &MvapplyOperatorExpressionToClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorExpressionToClause}.
 * @param ctx the parse tree
 */
fn exit_mvapplyOperatorExpressionToClause(&mut self, _ctx: &MvapplyOperatorExpressionToClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvexpandOperator}.
 * @param ctx the parse tree
 */
fn enter_mvexpandOperator(&mut self, _ctx: &MvexpandOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvexpandOperator}.
 * @param ctx the parse tree
 */
fn exit_mvexpandOperator(&mut self, _ctx: &MvexpandOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#mvexpandOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_mvexpandOperatorExpression(&mut self, _ctx: &MvexpandOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#mvexpandOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_mvexpandOperatorExpression(&mut self, _ctx: &MvexpandOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseOperator}.
 * @param ctx the parse tree
 */
fn enter_parseOperator(&mut self, _ctx: &ParseOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseOperator}.
 * @param ctx the parse tree
 */
fn exit_parseOperator(&mut self, _ctx: &ParseOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseOperatorKindClause}.
 * @param ctx the parse tree
 */
fn enter_parseOperatorKindClause(&mut self, _ctx: &ParseOperatorKindClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseOperatorKindClause}.
 * @param ctx the parse tree
 */
fn exit_parseOperatorKindClause(&mut self, _ctx: &ParseOperatorKindClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseOperatorFlagsClause}.
 * @param ctx the parse tree
 */
fn enter_parseOperatorFlagsClause(&mut self, _ctx: &ParseOperatorFlagsClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseOperatorFlagsClause}.
 * @param ctx the parse tree
 */
fn exit_parseOperatorFlagsClause(&mut self, _ctx: &ParseOperatorFlagsClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseOperatorNameAndOptionalType}.
 * @param ctx the parse tree
 */
fn enter_parseOperatorNameAndOptionalType(&mut self, _ctx: &ParseOperatorNameAndOptionalTypeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseOperatorNameAndOptionalType}.
 * @param ctx the parse tree
 */
fn exit_parseOperatorNameAndOptionalType(&mut self, _ctx: &ParseOperatorNameAndOptionalTypeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseOperatorPattern}.
 * @param ctx the parse tree
 */
fn enter_parseOperatorPattern(&mut self, _ctx: &ParseOperatorPatternContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseOperatorPattern}.
 * @param ctx the parse tree
 */
fn exit_parseOperatorPattern(&mut self, _ctx: &ParseOperatorPatternContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseOperatorPatternSegment}.
 * @param ctx the parse tree
 */
fn enter_parseOperatorPatternSegment(&mut self, _ctx: &ParseOperatorPatternSegmentContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseOperatorPatternSegment}.
 * @param ctx the parse tree
 */
fn exit_parseOperatorPatternSegment(&mut self, _ctx: &ParseOperatorPatternSegmentContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseWhereOperator}.
 * @param ctx the parse tree
 */
fn enter_parseWhereOperator(&mut self, _ctx: &ParseWhereOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseWhereOperator}.
 * @param ctx the parse tree
 */
fn exit_parseWhereOperator(&mut self, _ctx: &ParseWhereOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseKvOperator}.
 * @param ctx the parse tree
 */
fn enter_parseKvOperator(&mut self, _ctx: &ParseKvOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseKvOperator}.
 * @param ctx the parse tree
 */
fn exit_parseKvOperator(&mut self, _ctx: &ParseKvOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parseKvWithClause}.
 * @param ctx the parse tree
 */
fn enter_parseKvWithClause(&mut self, _ctx: &ParseKvWithClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parseKvWithClause}.
 * @param ctx the parse tree
 */
fn exit_parseKvWithClause(&mut self, _ctx: &ParseKvWithClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#partitionOperator}.
 * @param ctx the parse tree
 */
fn enter_partitionOperator(&mut self, _ctx: &PartitionOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#partitionOperator}.
 * @param ctx the parse tree
 */
fn exit_partitionOperator(&mut self, _ctx: &PartitionOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#partitionOperatorInClause}.
 * @param ctx the parse tree
 */
fn enter_partitionOperatorInClause(&mut self, _ctx: &PartitionOperatorInClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#partitionOperatorInClause}.
 * @param ctx the parse tree
 */
fn exit_partitionOperatorInClause(&mut self, _ctx: &PartitionOperatorInClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#partitionOperatorSubExpressionBody}.
 * @param ctx the parse tree
 */
fn enter_partitionOperatorSubExpressionBody(&mut self, _ctx: &PartitionOperatorSubExpressionBodyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#partitionOperatorSubExpressionBody}.
 * @param ctx the parse tree
 */
fn exit_partitionOperatorSubExpressionBody(&mut self, _ctx: &PartitionOperatorSubExpressionBodyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#partitionOperatorFullExpressionBody}.
 * @param ctx the parse tree
 */
fn enter_partitionOperatorFullExpressionBody(&mut self, _ctx: &PartitionOperatorFullExpressionBodyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#partitionOperatorFullExpressionBody}.
 * @param ctx the parse tree
 */
fn exit_partitionOperatorFullExpressionBody(&mut self, _ctx: &PartitionOperatorFullExpressionBodyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#partitionByOperator}.
 * @param ctx the parse tree
 */
fn enter_partitionByOperator(&mut self, _ctx: &PartitionByOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#partitionByOperator}.
 * @param ctx the parse tree
 */
fn exit_partitionByOperator(&mut self, _ctx: &PartitionByOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#partitionByOperatorIdClause}.
 * @param ctx the parse tree
 */
fn enter_partitionByOperatorIdClause(&mut self, _ctx: &PartitionByOperatorIdClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#partitionByOperatorIdClause}.
 * @param ctx the parse tree
 */
fn exit_partitionByOperatorIdClause(&mut self, _ctx: &PartitionByOperatorIdClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#printOperator}.
 * @param ctx the parse tree
 */
fn enter_printOperator(&mut self, _ctx: &PrintOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#printOperator}.
 * @param ctx the parse tree
 */
fn exit_printOperator(&mut self, _ctx: &PrintOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#projectAwayOperator}.
 * @param ctx the parse tree
 */
fn enter_projectAwayOperator(&mut self, _ctx: &ProjectAwayOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#projectAwayOperator}.
 * @param ctx the parse tree
 */
fn exit_projectAwayOperator(&mut self, _ctx: &ProjectAwayOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#projectKeepOperator}.
 * @param ctx the parse tree
 */
fn enter_projectKeepOperator(&mut self, _ctx: &ProjectKeepOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#projectKeepOperator}.
 * @param ctx the parse tree
 */
fn exit_projectKeepOperator(&mut self, _ctx: &ProjectKeepOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#projectOperator}.
 * @param ctx the parse tree
 */
fn enter_projectOperator(&mut self, _ctx: &ProjectOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#projectOperator}.
 * @param ctx the parse tree
 */
fn exit_projectOperator(&mut self, _ctx: &ProjectOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#projectRenameOperator}.
 * @param ctx the parse tree
 */
fn enter_projectRenameOperator(&mut self, _ctx: &ProjectRenameOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#projectRenameOperator}.
 * @param ctx the parse tree
 */
fn exit_projectRenameOperator(&mut self, _ctx: &ProjectRenameOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#projectReorderOperator}.
 * @param ctx the parse tree
 */
fn enter_projectReorderOperator(&mut self, _ctx: &ProjectReorderOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#projectReorderOperator}.
 * @param ctx the parse tree
 */
fn exit_projectReorderOperator(&mut self, _ctx: &ProjectReorderOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#projectReorderExpression}.
 * @param ctx the parse tree
 */
fn enter_projectReorderExpression(&mut self, _ctx: &ProjectReorderExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#projectReorderExpression}.
 * @param ctx the parse tree
 */
fn exit_projectReorderExpression(&mut self, _ctx: &ProjectReorderExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#reduceByOperator}.
 * @param ctx the parse tree
 */
fn enter_reduceByOperator(&mut self, _ctx: &ReduceByOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#reduceByOperator}.
 * @param ctx the parse tree
 */
fn exit_reduceByOperator(&mut self, _ctx: &ReduceByOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#reduceByWithClause}.
 * @param ctx the parse tree
 */
fn enter_reduceByWithClause(&mut self, _ctx: &ReduceByWithClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#reduceByWithClause}.
 * @param ctx the parse tree
 */
fn exit_reduceByWithClause(&mut self, _ctx: &ReduceByWithClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#renderOperator}.
 * @param ctx the parse tree
 */
fn enter_renderOperator(&mut self, _ctx: &RenderOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#renderOperator}.
 * @param ctx the parse tree
 */
fn exit_renderOperator(&mut self, _ctx: &RenderOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#renderOperatorWithClause}.
 * @param ctx the parse tree
 */
fn enter_renderOperatorWithClause(&mut self, _ctx: &RenderOperatorWithClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#renderOperatorWithClause}.
 * @param ctx the parse tree
 */
fn exit_renderOperatorWithClause(&mut self, _ctx: &RenderOperatorWithClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#renderOperatorLegacyPropertyList}.
 * @param ctx the parse tree
 */
fn enter_renderOperatorLegacyPropertyList(&mut self, _ctx: &RenderOperatorLegacyPropertyListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#renderOperatorLegacyPropertyList}.
 * @param ctx the parse tree
 */
fn exit_renderOperatorLegacyPropertyList(&mut self, _ctx: &RenderOperatorLegacyPropertyListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#renderOperatorProperty}.
 * @param ctx the parse tree
 */
fn enter_renderOperatorProperty(&mut self, _ctx: &RenderOperatorPropertyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#renderOperatorProperty}.
 * @param ctx the parse tree
 */
fn exit_renderOperatorProperty(&mut self, _ctx: &RenderOperatorPropertyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#renderPropertyNameList}.
 * @param ctx the parse tree
 */
fn enter_renderPropertyNameList(&mut self, _ctx: &RenderPropertyNameListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#renderPropertyNameList}.
 * @param ctx the parse tree
 */
fn exit_renderPropertyNameList(&mut self, _ctx: &RenderPropertyNameListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#renderOperatorLegacyProperty}.
 * @param ctx the parse tree
 */
fn enter_renderOperatorLegacyProperty(&mut self, _ctx: &RenderOperatorLegacyPropertyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#renderOperatorLegacyProperty}.
 * @param ctx the parse tree
 */
fn exit_renderOperatorLegacyProperty(&mut self, _ctx: &RenderOperatorLegacyPropertyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#sampleDistinctOperator}.
 * @param ctx the parse tree
 */
fn enter_sampleDistinctOperator(&mut self, _ctx: &SampleDistinctOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#sampleDistinctOperator}.
 * @param ctx the parse tree
 */
fn exit_sampleDistinctOperator(&mut self, _ctx: &SampleDistinctOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#sampleOperator}.
 * @param ctx the parse tree
 */
fn enter_sampleOperator(&mut self, _ctx: &SampleOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#sampleOperator}.
 * @param ctx the parse tree
 */
fn exit_sampleOperator(&mut self, _ctx: &SampleOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperator}.
 * @param ctx the parse tree
 */
fn enter_scanOperator(&mut self, _ctx: &ScanOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperator}.
 * @param ctx the parse tree
 */
fn exit_scanOperator(&mut self, _ctx: &ScanOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorOrderByClause}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorOrderByClause(&mut self, _ctx: &ScanOperatorOrderByClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorOrderByClause}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorOrderByClause(&mut self, _ctx: &ScanOperatorOrderByClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorPartitionByClause}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorPartitionByClause(&mut self, _ctx: &ScanOperatorPartitionByClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorPartitionByClause}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorPartitionByClause(&mut self, _ctx: &ScanOperatorPartitionByClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorDeclareClause}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorDeclareClause(&mut self, _ctx: &ScanOperatorDeclareClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorDeclareClause}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorDeclareClause(&mut self, _ctx: &ScanOperatorDeclareClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorStep}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorStep(&mut self, _ctx: &ScanOperatorStepContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorStep}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorStep(&mut self, _ctx: &ScanOperatorStepContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorStepOutputClause}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorStepOutputClause(&mut self, _ctx: &ScanOperatorStepOutputClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorStepOutputClause}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorStepOutputClause(&mut self, _ctx: &ScanOperatorStepOutputClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorBody}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorBody(&mut self, _ctx: &ScanOperatorBodyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorBody}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorBody(&mut self, _ctx: &ScanOperatorBodyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scanOperatorAssignment}.
 * @param ctx the parse tree
 */
fn enter_scanOperatorAssignment(&mut self, _ctx: &ScanOperatorAssignmentContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scanOperatorAssignment}.
 * @param ctx the parse tree
 */
fn exit_scanOperatorAssignment(&mut self, _ctx: &ScanOperatorAssignmentContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#searchOperator}.
 * @param ctx the parse tree
 */
fn enter_searchOperator(&mut self, _ctx: &SearchOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#searchOperator}.
 * @param ctx the parse tree
 */
fn exit_searchOperator(&mut self, _ctx: &SearchOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#searchOperatorStarAndExpression}.
 * @param ctx the parse tree
 */
fn enter_searchOperatorStarAndExpression(&mut self, _ctx: &SearchOperatorStarAndExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#searchOperatorStarAndExpression}.
 * @param ctx the parse tree
 */
fn exit_searchOperatorStarAndExpression(&mut self, _ctx: &SearchOperatorStarAndExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#searchOperatorInClause}.
 * @param ctx the parse tree
 */
fn enter_searchOperatorInClause(&mut self, _ctx: &SearchOperatorInClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#searchOperatorInClause}.
 * @param ctx the parse tree
 */
fn exit_searchOperatorInClause(&mut self, _ctx: &SearchOperatorInClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#serializeOperator}.
 * @param ctx the parse tree
 */
fn enter_serializeOperator(&mut self, _ctx: &SerializeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#serializeOperator}.
 * @param ctx the parse tree
 */
fn exit_serializeOperator(&mut self, _ctx: &SerializeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#sortOperator}.
 * @param ctx the parse tree
 */
fn enter_sortOperator(&mut self, _ctx: &SortOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#sortOperator}.
 * @param ctx the parse tree
 */
fn exit_sortOperator(&mut self, _ctx: &SortOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#orderedExpression}.
 * @param ctx the parse tree
 */
fn enter_orderedExpression(&mut self, _ctx: &OrderedExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#orderedExpression}.
 * @param ctx the parse tree
 */
fn exit_orderedExpression(&mut self, _ctx: &OrderedExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#sortOrdering}.
 * @param ctx the parse tree
 */
fn enter_sortOrdering(&mut self, _ctx: &SortOrderingContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#sortOrdering}.
 * @param ctx the parse tree
 */
fn exit_sortOrdering(&mut self, _ctx: &SortOrderingContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#summarizeOperator}.
 * @param ctx the parse tree
 */
fn enter_summarizeOperator(&mut self, _ctx: &SummarizeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#summarizeOperator}.
 * @param ctx the parse tree
 */
fn exit_summarizeOperator(&mut self, _ctx: &SummarizeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#summarizeOperatorByClause}.
 * @param ctx the parse tree
 */
fn enter_summarizeOperatorByClause(&mut self, _ctx: &SummarizeOperatorByClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#summarizeOperatorByClause}.
 * @param ctx the parse tree
 */
fn exit_summarizeOperatorByClause(&mut self, _ctx: &SummarizeOperatorByClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#summarizeOperatorLegacyBinClause}.
 * @param ctx the parse tree
 */
fn enter_summarizeOperatorLegacyBinClause(&mut self, _ctx: &SummarizeOperatorLegacyBinClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#summarizeOperatorLegacyBinClause}.
 * @param ctx the parse tree
 */
fn exit_summarizeOperatorLegacyBinClause(&mut self, _ctx: &SummarizeOperatorLegacyBinClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#takeOperator}.
 * @param ctx the parse tree
 */
fn enter_takeOperator(&mut self, _ctx: &TakeOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#takeOperator}.
 * @param ctx the parse tree
 */
fn exit_takeOperator(&mut self, _ctx: &TakeOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#topOperator}.
 * @param ctx the parse tree
 */
fn enter_topOperator(&mut self, _ctx: &TopOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#topOperator}.
 * @param ctx the parse tree
 */
fn exit_topOperator(&mut self, _ctx: &TopOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#topHittersOperator}.
 * @param ctx the parse tree
 */
fn enter_topHittersOperator(&mut self, _ctx: &TopHittersOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#topHittersOperator}.
 * @param ctx the parse tree
 */
fn exit_topHittersOperator(&mut self, _ctx: &TopHittersOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#topHittersOperatorByClause}.
 * @param ctx the parse tree
 */
fn enter_topHittersOperatorByClause(&mut self, _ctx: &TopHittersOperatorByClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#topHittersOperatorByClause}.
 * @param ctx the parse tree
 */
fn exit_topHittersOperatorByClause(&mut self, _ctx: &TopHittersOperatorByClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#topNestedOperator}.
 * @param ctx the parse tree
 */
fn enter_topNestedOperator(&mut self, _ctx: &TopNestedOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#topNestedOperator}.
 * @param ctx the parse tree
 */
fn exit_topNestedOperator(&mut self, _ctx: &TopNestedOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#topNestedOperatorPart}.
 * @param ctx the parse tree
 */
fn enter_topNestedOperatorPart(&mut self, _ctx: &TopNestedOperatorPartContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#topNestedOperatorPart}.
 * @param ctx the parse tree
 */
fn exit_topNestedOperatorPart(&mut self, _ctx: &TopNestedOperatorPartContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#topNestedOperatorWithOthersClause}.
 * @param ctx the parse tree
 */
fn enter_topNestedOperatorWithOthersClause(&mut self, _ctx: &TopNestedOperatorWithOthersClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#topNestedOperatorWithOthersClause}.
 * @param ctx the parse tree
 */
fn exit_topNestedOperatorWithOthersClause(&mut self, _ctx: &TopNestedOperatorWithOthersClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#unionOperator}.
 * @param ctx the parse tree
 */
fn enter_unionOperator(&mut self, _ctx: &UnionOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#unionOperator}.
 * @param ctx the parse tree
 */
fn exit_unionOperator(&mut self, _ctx: &UnionOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#unionOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_unionOperatorExpression(&mut self, _ctx: &UnionOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#unionOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_unionOperatorExpression(&mut self, _ctx: &UnionOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#whereOperator}.
 * @param ctx the parse tree
 */
fn enter_whereOperator(&mut self, _ctx: &WhereOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#whereOperator}.
 * @param ctx the parse tree
 */
fn exit_whereOperator(&mut self, _ctx: &WhereOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#contextualSubExpression}.
 * @param ctx the parse tree
 */
fn enter_contextualSubExpression(&mut self, _ctx: &ContextualSubExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#contextualSubExpression}.
 * @param ctx the parse tree
 */
fn exit_contextualSubExpression(&mut self, _ctx: &ContextualSubExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#contextualPipeExpression}.
 * @param ctx the parse tree
 */
fn enter_contextualPipeExpression(&mut self, _ctx: &ContextualPipeExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#contextualPipeExpression}.
 * @param ctx the parse tree
 */
fn exit_contextualPipeExpression(&mut self, _ctx: &ContextualPipeExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#contextualPipeExpressionPipedOperator}.
 * @param ctx the parse tree
 */
fn enter_contextualPipeExpressionPipedOperator(&mut self, _ctx: &ContextualPipeExpressionPipedOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#contextualPipeExpressionPipedOperator}.
 * @param ctx the parse tree
 */
fn exit_contextualPipeExpressionPipedOperator(&mut self, _ctx: &ContextualPipeExpressionPipedOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#strictQueryOperatorParameter}.
 * @param ctx the parse tree
 */
fn enter_strictQueryOperatorParameter(&mut self, _ctx: &StrictQueryOperatorParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#strictQueryOperatorParameter}.
 * @param ctx the parse tree
 */
fn exit_strictQueryOperatorParameter(&mut self, _ctx: &StrictQueryOperatorParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#relaxedQueryOperatorParameter}.
 * @param ctx the parse tree
 */
fn enter_relaxedQueryOperatorParameter(&mut self, _ctx: &RelaxedQueryOperatorParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#relaxedQueryOperatorParameter}.
 * @param ctx the parse tree
 */
fn exit_relaxedQueryOperatorParameter(&mut self, _ctx: &RelaxedQueryOperatorParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#queryOperatorProperty}.
 * @param ctx the parse tree
 */
fn enter_queryOperatorProperty(&mut self, _ctx: &QueryOperatorPropertyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#queryOperatorProperty}.
 * @param ctx the parse tree
 */
fn exit_queryOperatorProperty(&mut self, _ctx: &QueryOperatorPropertyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#namedExpression}.
 * @param ctx the parse tree
 */
fn enter_namedExpression(&mut self, _ctx: &NamedExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#namedExpression}.
 * @param ctx the parse tree
 */
fn exit_namedExpression(&mut self, _ctx: &NamedExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#namedExpressionNameClause}.
 * @param ctx the parse tree
 */
fn enter_namedExpressionNameClause(&mut self, _ctx: &NamedExpressionNameClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#namedExpressionNameClause}.
 * @param ctx the parse tree
 */
fn exit_namedExpressionNameClause(&mut self, _ctx: &NamedExpressionNameClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#namedExpressionNameList}.
 * @param ctx the parse tree
 */
fn enter_namedExpressionNameList(&mut self, _ctx: &NamedExpressionNameListContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#namedExpressionNameList}.
 * @param ctx the parse tree
 */
fn exit_namedExpressionNameList(&mut self, _ctx: &NamedExpressionNameListContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scopedFunctionCallExpression}.
 * @param ctx the parse tree
 */
fn enter_scopedFunctionCallExpression(&mut self, _ctx: &ScopedFunctionCallExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scopedFunctionCallExpression}.
 * @param ctx the parse tree
 */
fn exit_scopedFunctionCallExpression(&mut self, _ctx: &ScopedFunctionCallExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#unnamedExpression}.
 * @param ctx the parse tree
 */
fn enter_unnamedExpression(&mut self, _ctx: &UnnamedExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#unnamedExpression}.
 * @param ctx the parse tree
 */
fn exit_unnamedExpression(&mut self, _ctx: &UnnamedExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#logicalOrExpression}.
 * @param ctx the parse tree
 */
fn enter_logicalOrExpression(&mut self, _ctx: &LogicalOrExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#logicalOrExpression}.
 * @param ctx the parse tree
 */
fn exit_logicalOrExpression(&mut self, _ctx: &LogicalOrExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#logicalOrOperation}.
 * @param ctx the parse tree
 */
fn enter_logicalOrOperation(&mut self, _ctx: &LogicalOrOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#logicalOrOperation}.
 * @param ctx the parse tree
 */
fn exit_logicalOrOperation(&mut self, _ctx: &LogicalOrOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#logicalAndExpression}.
 * @param ctx the parse tree
 */
fn enter_logicalAndExpression(&mut self, _ctx: &LogicalAndExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#logicalAndExpression}.
 * @param ctx the parse tree
 */
fn exit_logicalAndExpression(&mut self, _ctx: &LogicalAndExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#logicalAndOperation}.
 * @param ctx the parse tree
 */
fn enter_logicalAndOperation(&mut self, _ctx: &LogicalAndOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#logicalAndOperation}.
 * @param ctx the parse tree
 */
fn exit_logicalAndOperation(&mut self, _ctx: &LogicalAndOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#equalityExpression}.
 * @param ctx the parse tree
 */
fn enter_equalityExpression(&mut self, _ctx: &EqualityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#equalityExpression}.
 * @param ctx the parse tree
 */
fn exit_equalityExpression(&mut self, _ctx: &EqualityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#equalsEqualityExpression}.
 * @param ctx the parse tree
 */
fn enter_equalsEqualityExpression(&mut self, _ctx: &EqualsEqualityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#equalsEqualityExpression}.
 * @param ctx the parse tree
 */
fn exit_equalsEqualityExpression(&mut self, _ctx: &EqualsEqualityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#listEqualityExpression}.
 * @param ctx the parse tree
 */
fn enter_listEqualityExpression(&mut self, _ctx: &ListEqualityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#listEqualityExpression}.
 * @param ctx the parse tree
 */
fn exit_listEqualityExpression(&mut self, _ctx: &ListEqualityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#betweenEqualityExpression}.
 * @param ctx the parse tree
 */
fn enter_betweenEqualityExpression(&mut self, _ctx: &BetweenEqualityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#betweenEqualityExpression}.
 * @param ctx the parse tree
 */
fn exit_betweenEqualityExpression(&mut self, _ctx: &BetweenEqualityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#starEqualityExpression}.
 * @param ctx the parse tree
 */
fn enter_starEqualityExpression(&mut self, _ctx: &StarEqualityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#starEqualityExpression}.
 * @param ctx the parse tree
 */
fn exit_starEqualityExpression(&mut self, _ctx: &StarEqualityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#relationalExpression}.
 * @param ctx the parse tree
 */
fn enter_relationalExpression(&mut self, _ctx: &RelationalExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#relationalExpression}.
 * @param ctx the parse tree
 */
fn exit_relationalExpression(&mut self, _ctx: &RelationalExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#additiveExpression}.
 * @param ctx the parse tree
 */
fn enter_additiveExpression(&mut self, _ctx: &AdditiveExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#additiveExpression}.
 * @param ctx the parse tree
 */
fn exit_additiveExpression(&mut self, _ctx: &AdditiveExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#additiveOperation}.
 * @param ctx the parse tree
 */
fn enter_additiveOperation(&mut self, _ctx: &AdditiveOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#additiveOperation}.
 * @param ctx the parse tree
 */
fn exit_additiveOperation(&mut self, _ctx: &AdditiveOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#multiplicativeExpression}.
 * @param ctx the parse tree
 */
fn enter_multiplicativeExpression(&mut self, _ctx: &MultiplicativeExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#multiplicativeExpression}.
 * @param ctx the parse tree
 */
fn exit_multiplicativeExpression(&mut self, _ctx: &MultiplicativeExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#multiplicativeOperation}.
 * @param ctx the parse tree
 */
fn enter_multiplicativeOperation(&mut self, _ctx: &MultiplicativeOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#multiplicativeOperation}.
 * @param ctx the parse tree
 */
fn exit_multiplicativeOperation(&mut self, _ctx: &MultiplicativeOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#stringOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_stringOperatorExpression(&mut self, _ctx: &StringOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#stringOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_stringOperatorExpression(&mut self, _ctx: &StringOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#stringBinaryOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_stringBinaryOperatorExpression(&mut self, _ctx: &StringBinaryOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#stringBinaryOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_stringBinaryOperatorExpression(&mut self, _ctx: &StringBinaryOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#stringBinaryOperation}.
 * @param ctx the parse tree
 */
fn enter_stringBinaryOperation(&mut self, _ctx: &StringBinaryOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#stringBinaryOperation}.
 * @param ctx the parse tree
 */
fn exit_stringBinaryOperation(&mut self, _ctx: &StringBinaryOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#stringBinaryOperator}.
 * @param ctx the parse tree
 */
fn enter_stringBinaryOperator(&mut self, _ctx: &StringBinaryOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#stringBinaryOperator}.
 * @param ctx the parse tree
 */
fn exit_stringBinaryOperator(&mut self, _ctx: &StringBinaryOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#stringStarOperatorExpression}.
 * @param ctx the parse tree
 */
fn enter_stringStarOperatorExpression(&mut self, _ctx: &StringStarOperatorExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#stringStarOperatorExpression}.
 * @param ctx the parse tree
 */
fn exit_stringStarOperatorExpression(&mut self, _ctx: &StringStarOperatorExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#invocationExpression}.
 * @param ctx the parse tree
 */
fn enter_invocationExpression(&mut self, _ctx: &InvocationExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#invocationExpression}.
 * @param ctx the parse tree
 */
fn exit_invocationExpression(&mut self, _ctx: &InvocationExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathExpression}.
 * @param ctx the parse tree
 */
fn enter_functionCallOrPathExpression(&mut self, _ctx: &FunctionCallOrPathExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathExpression}.
 * @param ctx the parse tree
 */
fn exit_functionCallOrPathExpression(&mut self, _ctx: &FunctionCallOrPathExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathRoot}.
 * @param ctx the parse tree
 */
fn enter_functionCallOrPathRoot(&mut self, _ctx: &FunctionCallOrPathRootContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathRoot}.
 * @param ctx the parse tree
 */
fn exit_functionCallOrPathRoot(&mut self, _ctx: &FunctionCallOrPathRootContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathPathExpression}.
 * @param ctx the parse tree
 */
fn enter_functionCallOrPathPathExpression(&mut self, _ctx: &FunctionCallOrPathPathExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathPathExpression}.
 * @param ctx the parse tree
 */
fn exit_functionCallOrPathPathExpression(&mut self, _ctx: &FunctionCallOrPathPathExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathOperation}.
 * @param ctx the parse tree
 */
fn enter_functionCallOrPathOperation(&mut self, _ctx: &FunctionCallOrPathOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathOperation}.
 * @param ctx the parse tree
 */
fn exit_functionCallOrPathOperation(&mut self, _ctx: &FunctionCallOrPathOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionalCallOrPathPathOperation}.
 * @param ctx the parse tree
 */
fn enter_functionalCallOrPathPathOperation(&mut self, _ctx: &FunctionalCallOrPathPathOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionalCallOrPathPathOperation}.
 * @param ctx the parse tree
 */
fn exit_functionalCallOrPathPathOperation(&mut self, _ctx: &FunctionalCallOrPathPathOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathElementOperation}.
 * @param ctx the parse tree
 */
fn enter_functionCallOrPathElementOperation(&mut self, _ctx: &FunctionCallOrPathElementOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathElementOperation}.
 * @param ctx the parse tree
 */
fn exit_functionCallOrPathElementOperation(&mut self, _ctx: &FunctionCallOrPathElementOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#legacyFunctionCallOrPathElementOperation}.
 * @param ctx the parse tree
 */
fn enter_legacyFunctionCallOrPathElementOperation(&mut self, _ctx: &LegacyFunctionCallOrPathElementOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#legacyFunctionCallOrPathElementOperation}.
 * @param ctx the parse tree
 */
fn exit_legacyFunctionCallOrPathElementOperation(&mut self, _ctx: &LegacyFunctionCallOrPathElementOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#toScalarExpression}.
 * @param ctx the parse tree
 */
fn enter_toScalarExpression(&mut self, _ctx: &ToScalarExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#toScalarExpression}.
 * @param ctx the parse tree
 */
fn exit_toScalarExpression(&mut self, _ctx: &ToScalarExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#toTableExpression}.
 * @param ctx the parse tree
 */
fn enter_toTableExpression(&mut self, _ctx: &ToTableExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#toTableExpression}.
 * @param ctx the parse tree
 */
fn exit_toTableExpression(&mut self, _ctx: &ToTableExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#noOptimizationParameter}.
 * @param ctx the parse tree
 */
fn enter_noOptimizationParameter(&mut self, _ctx: &NoOptimizationParameterContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#noOptimizationParameter}.
 * @param ctx the parse tree
 */
fn exit_noOptimizationParameter(&mut self, _ctx: &NoOptimizationParameterContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#dotCompositeFunctionCallExpression}.
 * @param ctx the parse tree
 */
fn enter_dotCompositeFunctionCallExpression(&mut self, _ctx: &DotCompositeFunctionCallExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallExpression}.
 * @param ctx the parse tree
 */
fn exit_dotCompositeFunctionCallExpression(&mut self, _ctx: &DotCompositeFunctionCallExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#dotCompositeFunctionCallOperation}.
 * @param ctx the parse tree
 */
fn enter_dotCompositeFunctionCallOperation(&mut self, _ctx: &DotCompositeFunctionCallOperationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallOperation}.
 * @param ctx the parse tree
 */
fn exit_dotCompositeFunctionCallOperation(&mut self, _ctx: &DotCompositeFunctionCallOperationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#functionCallExpression}.
 * @param ctx the parse tree
 */
fn enter_functionCallExpression(&mut self, _ctx: &FunctionCallExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#functionCallExpression}.
 * @param ctx the parse tree
 */
fn exit_functionCallExpression(&mut self, _ctx: &FunctionCallExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#namedFunctionCallExpression}.
 * @param ctx the parse tree
 */
fn enter_namedFunctionCallExpression(&mut self, _ctx: &NamedFunctionCallExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#namedFunctionCallExpression}.
 * @param ctx the parse tree
 */
fn exit_namedFunctionCallExpression(&mut self, _ctx: &NamedFunctionCallExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#argumentExpression}.
 * @param ctx the parse tree
 */
fn enter_argumentExpression(&mut self, _ctx: &ArgumentExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#argumentExpression}.
 * @param ctx the parse tree
 */
fn exit_argumentExpression(&mut self, _ctx: &ArgumentExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#countExpression}.
 * @param ctx the parse tree
 */
fn enter_countExpression(&mut self, _ctx: &CountExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#countExpression}.
 * @param ctx the parse tree
 */
fn exit_countExpression(&mut self, _ctx: &CountExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#starExpression}.
 * @param ctx the parse tree
 */
fn enter_starExpression(&mut self, _ctx: &StarExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#starExpression}.
 * @param ctx the parse tree
 */
fn exit_starExpression(&mut self, _ctx: &StarExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#primaryExpression}.
 * @param ctx the parse tree
 */
fn enter_primaryExpression(&mut self, _ctx: &PrimaryExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#primaryExpression}.
 * @param ctx the parse tree
 */
fn exit_primaryExpression(&mut self, _ctx: &PrimaryExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#nameReferenceWithDataScope}.
 * @param ctx the parse tree
 */
fn enter_nameReferenceWithDataScope(&mut self, _ctx: &NameReferenceWithDataScopeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#nameReferenceWithDataScope}.
 * @param ctx the parse tree
 */
fn exit_nameReferenceWithDataScope(&mut self, _ctx: &NameReferenceWithDataScopeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#dataScopeClause}.
 * @param ctx the parse tree
 */
fn enter_dataScopeClause(&mut self, _ctx: &DataScopeClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#dataScopeClause}.
 * @param ctx the parse tree
 */
fn exit_dataScopeClause(&mut self, _ctx: &DataScopeClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parenthesizedExpression}.
 * @param ctx the parse tree
 */
fn enter_parenthesizedExpression(&mut self, _ctx: &ParenthesizedExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parenthesizedExpression}.
 * @param ctx the parse tree
 */
fn exit_parenthesizedExpression(&mut self, _ctx: &ParenthesizedExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#rangeExpression}.
 * @param ctx the parse tree
 */
fn enter_rangeExpression(&mut self, _ctx: &RangeExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#rangeExpression}.
 * @param ctx the parse tree
 */
fn exit_rangeExpression(&mut self, _ctx: &RangeExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityExpression}.
 * @param ctx the parse tree
 */
fn enter_entityExpression(&mut self, _ctx: &EntityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityExpression}.
 * @param ctx the parse tree
 */
fn exit_entityExpression(&mut self, _ctx: &EntityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityPathOrElementExpression}.
 * @param ctx the parse tree
 */
fn enter_entityPathOrElementExpression(&mut self, _ctx: &EntityPathOrElementExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityPathOrElementExpression}.
 * @param ctx the parse tree
 */
fn exit_entityPathOrElementExpression(&mut self, _ctx: &EntityPathOrElementExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityPathOrElementOperator}.
 * @param ctx the parse tree
 */
fn enter_entityPathOrElementOperator(&mut self, _ctx: &EntityPathOrElementOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityPathOrElementOperator}.
 * @param ctx the parse tree
 */
fn exit_entityPathOrElementOperator(&mut self, _ctx: &EntityPathOrElementOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityPathOperator}.
 * @param ctx the parse tree
 */
fn enter_entityPathOperator(&mut self, _ctx: &EntityPathOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityPathOperator}.
 * @param ctx the parse tree
 */
fn exit_entityPathOperator(&mut self, _ctx: &EntityPathOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityElementOperator}.
 * @param ctx the parse tree
 */
fn enter_entityElementOperator(&mut self, _ctx: &EntityElementOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityElementOperator}.
 * @param ctx the parse tree
 */
fn exit_entityElementOperator(&mut self, _ctx: &EntityElementOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#legacyEntityPathElementOperator}.
 * @param ctx the parse tree
 */
fn enter_legacyEntityPathElementOperator(&mut self, _ctx: &LegacyEntityPathElementOperatorContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#legacyEntityPathElementOperator}.
 * @param ctx the parse tree
 */
fn exit_legacyEntityPathElementOperator(&mut self, _ctx: &LegacyEntityPathElementOperatorContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityName}.
 * @param ctx the parse tree
 */
fn enter_entityName(&mut self, _ctx: &EntityNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityName}.
 * @param ctx the parse tree
 */
fn exit_entityName(&mut self, _ctx: &EntityNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#entityNameReference}.
 * @param ctx the parse tree
 */
fn enter_entityNameReference(&mut self, _ctx: &EntityNameReferenceContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#entityNameReference}.
 * @param ctx the parse tree
 */
fn exit_entityNameReference(&mut self, _ctx: &EntityNameReferenceContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#atSignName}.
 * @param ctx the parse tree
 */
fn enter_atSignName(&mut self, _ctx: &AtSignNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#atSignName}.
 * @param ctx the parse tree
 */
fn exit_atSignName(&mut self, _ctx: &AtSignNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#extendedPathName}.
 * @param ctx the parse tree
 */
fn enter_extendedPathName(&mut self, _ctx: &ExtendedPathNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#extendedPathName}.
 * @param ctx the parse tree
 */
fn exit_extendedPathName(&mut self, _ctx: &ExtendedPathNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedEntityExpression}.
 * @param ctx the parse tree
 */
fn enter_wildcardedEntityExpression(&mut self, _ctx: &WildcardedEntityExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedEntityExpression}.
 * @param ctx the parse tree
 */
fn exit_wildcardedEntityExpression(&mut self, _ctx: &WildcardedEntityExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedPathExpression}.
 * @param ctx the parse tree
 */
fn enter_wildcardedPathExpression(&mut self, _ctx: &WildcardedPathExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedPathExpression}.
 * @param ctx the parse tree
 */
fn exit_wildcardedPathExpression(&mut self, _ctx: &WildcardedPathExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedPathName}.
 * @param ctx the parse tree
 */
fn enter_wildcardedPathName(&mut self, _ctx: &WildcardedPathNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedPathName}.
 * @param ctx the parse tree
 */
fn exit_wildcardedPathName(&mut self, _ctx: &WildcardedPathNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#contextualDataTableExpression}.
 * @param ctx the parse tree
 */
fn enter_contextualDataTableExpression(&mut self, _ctx: &ContextualDataTableExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#contextualDataTableExpression}.
 * @param ctx the parse tree
 */
fn exit_contextualDataTableExpression(&mut self, _ctx: &ContextualDataTableExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#dataTableExpression}.
 * @param ctx the parse tree
 */
fn enter_dataTableExpression(&mut self, _ctx: &DataTableExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#dataTableExpression}.
 * @param ctx the parse tree
 */
fn exit_dataTableExpression(&mut self, _ctx: &DataTableExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#rowSchema}.
 * @param ctx the parse tree
 */
fn enter_rowSchema(&mut self, _ctx: &RowSchemaContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#rowSchema}.
 * @param ctx the parse tree
 */
fn exit_rowSchema(&mut self, _ctx: &RowSchemaContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#rowSchemaColumnDeclaration}.
 * @param ctx the parse tree
 */
fn enter_rowSchemaColumnDeclaration(&mut self, _ctx: &RowSchemaColumnDeclarationContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#rowSchemaColumnDeclaration}.
 * @param ctx the parse tree
 */
fn exit_rowSchemaColumnDeclaration(&mut self, _ctx: &RowSchemaColumnDeclarationContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#externalDataExpression}.
 * @param ctx the parse tree
 */
fn enter_externalDataExpression(&mut self, _ctx: &ExternalDataExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#externalDataExpression}.
 * @param ctx the parse tree
 */
fn exit_externalDataExpression(&mut self, _ctx: &ExternalDataExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#externalDataWithClause}.
 * @param ctx the parse tree
 */
fn enter_externalDataWithClause(&mut self, _ctx: &ExternalDataWithClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#externalDataWithClause}.
 * @param ctx the parse tree
 */
fn exit_externalDataWithClause(&mut self, _ctx: &ExternalDataWithClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#externalDataWithClauseProperty}.
 * @param ctx the parse tree
 */
fn enter_externalDataWithClauseProperty(&mut self, _ctx: &ExternalDataWithClausePropertyContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#externalDataWithClauseProperty}.
 * @param ctx the parse tree
 */
fn exit_externalDataWithClauseProperty(&mut self, _ctx: &ExternalDataWithClausePropertyContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#materializedViewCombineExpression}.
 * @param ctx the parse tree
 */
fn enter_materializedViewCombineExpression(&mut self, _ctx: &MaterializedViewCombineExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#materializedViewCombineExpression}.
 * @param ctx the parse tree
 */
fn exit_materializedViewCombineExpression(&mut self, _ctx: &MaterializedViewCombineExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#materializeViewCombineBaseClause}.
 * @param ctx the parse tree
 */
fn enter_materializeViewCombineBaseClause(&mut self, _ctx: &MaterializeViewCombineBaseClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#materializeViewCombineBaseClause}.
 * @param ctx the parse tree
 */
fn exit_materializeViewCombineBaseClause(&mut self, _ctx: &MaterializeViewCombineBaseClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#materializedViewCombineDeltaClause}.
 * @param ctx the parse tree
 */
fn enter_materializedViewCombineDeltaClause(&mut self, _ctx: &MaterializedViewCombineDeltaClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#materializedViewCombineDeltaClause}.
 * @param ctx the parse tree
 */
fn exit_materializedViewCombineDeltaClause(&mut self, _ctx: &MaterializedViewCombineDeltaClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#materializedViewCombineAggregationsClause}.
 * @param ctx the parse tree
 */
fn enter_materializedViewCombineAggregationsClause(&mut self, _ctx: &MaterializedViewCombineAggregationsClauseContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#materializedViewCombineAggregationsClause}.
 * @param ctx the parse tree
 */
fn exit_materializedViewCombineAggregationsClause(&mut self, _ctx: &MaterializedViewCombineAggregationsClauseContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#scalarType}.
 * @param ctx the parse tree
 */
fn enter_scalarType(&mut self, _ctx: &ScalarTypeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#scalarType}.
 * @param ctx the parse tree
 */
fn exit_scalarType(&mut self, _ctx: &ScalarTypeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#extendedScalarType}.
 * @param ctx the parse tree
 */
fn enter_extendedScalarType(&mut self, _ctx: &ExtendedScalarTypeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#extendedScalarType}.
 * @param ctx the parse tree
 */
fn exit_extendedScalarType(&mut self, _ctx: &ExtendedScalarTypeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#parameterName}.
 * @param ctx the parse tree
 */
fn enter_parameterName(&mut self, _ctx: &ParameterNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#parameterName}.
 * @param ctx the parse tree
 */
fn exit_parameterName(&mut self, _ctx: &ParameterNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#simpleNameReference}.
 * @param ctx the parse tree
 */
fn enter_simpleNameReference(&mut self, _ctx: &SimpleNameReferenceContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#simpleNameReference}.
 * @param ctx the parse tree
 */
fn exit_simpleNameReference(&mut self, _ctx: &SimpleNameReferenceContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#extendedNameReference}.
 * @param ctx the parse tree
 */
fn enter_extendedNameReference(&mut self, _ctx: &ExtendedNameReferenceContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#extendedNameReference}.
 * @param ctx the parse tree
 */
fn exit_extendedNameReference(&mut self, _ctx: &ExtendedNameReferenceContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedNameReference}.
 * @param ctx the parse tree
 */
fn enter_wildcardedNameReference(&mut self, _ctx: &WildcardedNameReferenceContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedNameReference}.
 * @param ctx the parse tree
 */
fn exit_wildcardedNameReference(&mut self, _ctx: &WildcardedNameReferenceContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#simpleOrWildcardedNameReference}.
 * @param ctx the parse tree
 */
fn enter_simpleOrWildcardedNameReference(&mut self, _ctx: &SimpleOrWildcardedNameReferenceContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#simpleOrWildcardedNameReference}.
 * @param ctx the parse tree
 */
fn exit_simpleOrWildcardedNameReference(&mut self, _ctx: &SimpleOrWildcardedNameReferenceContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#identifierName}.
 * @param ctx the parse tree
 */
fn enter_identifierName(&mut self, _ctx: &IdentifierNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#identifierName}.
 * @param ctx the parse tree
 */
fn exit_identifierName(&mut self, _ctx: &IdentifierNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#keywordName}.
 * @param ctx the parse tree
 */
fn enter_keywordName(&mut self, _ctx: &KeywordNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#keywordName}.
 * @param ctx the parse tree
 */
fn exit_keywordName(&mut self, _ctx: &KeywordNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#extendedKeywordName}.
 * @param ctx the parse tree
 */
fn enter_extendedKeywordName(&mut self, _ctx: &ExtendedKeywordNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#extendedKeywordName}.
 * @param ctx the parse tree
 */
fn exit_extendedKeywordName(&mut self, _ctx: &ExtendedKeywordNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#escapedName}.
 * @param ctx the parse tree
 */
fn enter_escapedName(&mut self, _ctx: &EscapedNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#escapedName}.
 * @param ctx the parse tree
 */
fn exit_escapedName(&mut self, _ctx: &EscapedNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#identifierOrKeywordName}.
 * @param ctx the parse tree
 */
fn enter_identifierOrKeywordName(&mut self, _ctx: &IdentifierOrKeywordNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#identifierOrKeywordName}.
 * @param ctx the parse tree
 */
fn exit_identifierOrKeywordName(&mut self, _ctx: &IdentifierOrKeywordNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#identifierOrKeywordOrEscapedName}.
 * @param ctx the parse tree
 */
fn enter_identifierOrKeywordOrEscapedName(&mut self, _ctx: &IdentifierOrKeywordOrEscapedNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#identifierOrKeywordOrEscapedName}.
 * @param ctx the parse tree
 */
fn exit_identifierOrKeywordOrEscapedName(&mut self, _ctx: &IdentifierOrKeywordOrEscapedNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordOrEscapedName}.
 * @param ctx the parse tree
 */
fn enter_identifierOrExtendedKeywordOrEscapedName(&mut self, _ctx: &IdentifierOrExtendedKeywordOrEscapedNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordOrEscapedName}.
 * @param ctx the parse tree
 */
fn exit_identifierOrExtendedKeywordOrEscapedName(&mut self, _ctx: &IdentifierOrExtendedKeywordOrEscapedNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordName}.
 * @param ctx the parse tree
 */
fn enter_identifierOrExtendedKeywordName(&mut self, _ctx: &IdentifierOrExtendedKeywordNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordName}.
 * @param ctx the parse tree
 */
fn exit_identifierOrExtendedKeywordName(&mut self, _ctx: &IdentifierOrExtendedKeywordNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedName}.
 * @param ctx the parse tree
 */
fn enter_wildcardedName(&mut self, _ctx: &WildcardedNameContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedName}.
 * @param ctx the parse tree
 */
fn exit_wildcardedName(&mut self, _ctx: &WildcardedNameContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedNamePrefix}.
 * @param ctx the parse tree
 */
fn enter_wildcardedNamePrefix(&mut self, _ctx: &WildcardedNamePrefixContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedNamePrefix}.
 * @param ctx the parse tree
 */
fn exit_wildcardedNamePrefix(&mut self, _ctx: &WildcardedNamePrefixContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#wildcardedNameSegment}.
 * @param ctx the parse tree
 */
fn enter_wildcardedNameSegment(&mut self, _ctx: &WildcardedNameSegmentContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#wildcardedNameSegment}.
 * @param ctx the parse tree
 */
fn exit_wildcardedNameSegment(&mut self, _ctx: &WildcardedNameSegmentContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#literalExpression}.
 * @param ctx the parse tree
 */
fn enter_literalExpression(&mut self, _ctx: &LiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#literalExpression}.
 * @param ctx the parse tree
 */
fn exit_literalExpression(&mut self, _ctx: &LiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#unsignedLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_unsignedLiteralExpression(&mut self, _ctx: &UnsignedLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#unsignedLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_unsignedLiteralExpression(&mut self, _ctx: &UnsignedLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#numberLikeLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_numberLikeLiteralExpression(&mut self, _ctx: &NumberLikeLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#numberLikeLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_numberLikeLiteralExpression(&mut self, _ctx: &NumberLikeLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#numericLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_numericLiteralExpression(&mut self, _ctx: &NumericLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#numericLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_numericLiteralExpression(&mut self, _ctx: &NumericLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#signedLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_signedLiteralExpression(&mut self, _ctx: &SignedLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#signedLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_signedLiteralExpression(&mut self, _ctx: &SignedLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#longLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_longLiteralExpression(&mut self, _ctx: &LongLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#longLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_longLiteralExpression(&mut self, _ctx: &LongLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#intLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_intLiteralExpression(&mut self, _ctx: &IntLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#intLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_intLiteralExpression(&mut self, _ctx: &IntLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#realLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_realLiteralExpression(&mut self, _ctx: &RealLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#realLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_realLiteralExpression(&mut self, _ctx: &RealLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#decimalLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_decimalLiteralExpression(&mut self, _ctx: &DecimalLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#decimalLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_decimalLiteralExpression(&mut self, _ctx: &DecimalLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#dateTimeLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_dateTimeLiteralExpression(&mut self, _ctx: &DateTimeLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#dateTimeLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_dateTimeLiteralExpression(&mut self, _ctx: &DateTimeLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#timeSpanLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_timeSpanLiteralExpression(&mut self, _ctx: &TimeSpanLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#timeSpanLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_timeSpanLiteralExpression(&mut self, _ctx: &TimeSpanLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#booleanLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_booleanLiteralExpression(&mut self, _ctx: &BooleanLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#booleanLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_booleanLiteralExpression(&mut self, _ctx: &BooleanLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#guidLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_guidLiteralExpression(&mut self, _ctx: &GuidLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#guidLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_guidLiteralExpression(&mut self, _ctx: &GuidLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#typeLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_typeLiteralExpression(&mut self, _ctx: &TypeLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#typeLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_typeLiteralExpression(&mut self, _ctx: &TypeLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#signedLongLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_signedLongLiteralExpression(&mut self, _ctx: &SignedLongLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#signedLongLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_signedLongLiteralExpression(&mut self, _ctx: &SignedLongLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#signedRealLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_signedRealLiteralExpression(&mut self, _ctx: &SignedRealLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#signedRealLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_signedRealLiteralExpression(&mut self, _ctx: &SignedRealLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#stringLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_stringLiteralExpression(&mut self, _ctx: &StringLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#stringLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_stringLiteralExpression(&mut self, _ctx: &StringLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#dynamicLiteralExpression}.
 * @param ctx the parse tree
 */
fn enter_dynamicLiteralExpression(&mut self, _ctx: &DynamicLiteralExpressionContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#dynamicLiteralExpression}.
 * @param ctx the parse tree
 */
fn exit_dynamicLiteralExpression(&mut self, _ctx: &DynamicLiteralExpressionContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonValue}.
 * @param ctx the parse tree
 */
fn enter_jsonValue(&mut self, _ctx: &JsonValueContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonValue}.
 * @param ctx the parse tree
 */
fn exit_jsonValue(&mut self, _ctx: &JsonValueContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonObject}.
 * @param ctx the parse tree
 */
fn enter_jsonObject(&mut self, _ctx: &JsonObjectContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonObject}.
 * @param ctx the parse tree
 */
fn exit_jsonObject(&mut self, _ctx: &JsonObjectContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonPair}.
 * @param ctx the parse tree
 */
fn enter_jsonPair(&mut self, _ctx: &JsonPairContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonPair}.
 * @param ctx the parse tree
 */
fn exit_jsonPair(&mut self, _ctx: &JsonPairContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonArray}.
 * @param ctx the parse tree
 */
fn enter_jsonArray(&mut self, _ctx: &JsonArrayContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonArray}.
 * @param ctx the parse tree
 */
fn exit_jsonArray(&mut self, _ctx: &JsonArrayContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonBoolean}.
 * @param ctx the parse tree
 */
fn enter_jsonBoolean(&mut self, _ctx: &JsonBooleanContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonBoolean}.
 * @param ctx the parse tree
 */
fn exit_jsonBoolean(&mut self, _ctx: &JsonBooleanContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonDateTime}.
 * @param ctx the parse tree
 */
fn enter_jsonDateTime(&mut self, _ctx: &JsonDateTimeContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonDateTime}.
 * @param ctx the parse tree
 */
fn exit_jsonDateTime(&mut self, _ctx: &JsonDateTimeContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonGuid}.
 * @param ctx the parse tree
 */
fn enter_jsonGuid(&mut self, _ctx: &JsonGuidContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonGuid}.
 * @param ctx the parse tree
 */
fn exit_jsonGuid(&mut self, _ctx: &JsonGuidContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonNull}.
 * @param ctx the parse tree
 */
fn enter_jsonNull(&mut self, _ctx: &JsonNullContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonNull}.
 * @param ctx the parse tree
 */
fn exit_jsonNull(&mut self, _ctx: &JsonNullContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonString}.
 * @param ctx the parse tree
 */
fn enter_jsonString(&mut self, _ctx: &JsonStringContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonString}.
 * @param ctx the parse tree
 */
fn exit_jsonString(&mut self, _ctx: &JsonStringContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonTimeSpan}.
 * @param ctx the parse tree
 */
fn enter_jsonTimeSpan(&mut self, _ctx: &JsonTimeSpanContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonTimeSpan}.
 * @param ctx the parse tree
 */
fn exit_jsonTimeSpan(&mut self, _ctx: &JsonTimeSpanContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonLong}.
 * @param ctx the parse tree
 */
fn enter_jsonLong(&mut self, _ctx: &JsonLongContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonLong}.
 * @param ctx the parse tree
 */
fn exit_jsonLong(&mut self, _ctx: &JsonLongContext<'input>) { }
/**
 * Enter a parse tree produced by {@link HqlParser#jsonReal}.
 * @param ctx the parse tree
 */
fn enter_jsonReal(&mut self, _ctx: &JsonRealContext<'input>) { }
/**
 * Exit a parse tree produced by {@link HqlParser#jsonReal}.
 * @param ctx the parse tree
 */
fn exit_jsonReal(&mut self, _ctx: &JsonRealContext<'input>) { }

}

antlr_rust::coerce_from!{ 'input : HqlListener<'input> }


