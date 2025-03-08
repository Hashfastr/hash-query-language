// Generated from /home/hashfastr/git/hash-query-language/grammar/Hql.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HqlParser}.
 */
public interface HqlListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HqlParser#top}.
	 * @param ctx the parse tree
	 */
	void enterTop(HqlParser.TopContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#top}.
	 * @param ctx the parse tree
	 */
	void exitTop(HqlParser.TopContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#query}.
	 * @param ctx the parse tree
	 */
	void enterQuery(HqlParser.QueryContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#query}.
	 * @param ctx the parse tree
	 */
	void exitQuery(HqlParser.QueryContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(HqlParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(HqlParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#aliasDatabaseStatement}.
	 * @param ctx the parse tree
	 */
	void enterAliasDatabaseStatement(HqlParser.AliasDatabaseStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#aliasDatabaseStatement}.
	 * @param ctx the parse tree
	 */
	void exitAliasDatabaseStatement(HqlParser.AliasDatabaseStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letStatement}.
	 * @param ctx the parse tree
	 */
	void enterLetStatement(HqlParser.LetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letStatement}.
	 * @param ctx the parse tree
	 */
	void exitLetStatement(HqlParser.LetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letVariableDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLetVariableDeclaration(HqlParser.LetVariableDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letVariableDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLetVariableDeclaration(HqlParser.LetVariableDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letFunctionDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLetFunctionDeclaration(HqlParser.LetFunctionDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letFunctionDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLetFunctionDeclaration(HqlParser.LetFunctionDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letViewDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLetViewDeclaration(HqlParser.LetViewDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letViewDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLetViewDeclaration(HqlParser.LetViewDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letViewParameterList}.
	 * @param ctx the parse tree
	 */
	void enterLetViewParameterList(HqlParser.LetViewParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letViewParameterList}.
	 * @param ctx the parse tree
	 */
	void exitLetViewParameterList(HqlParser.LetViewParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letMaterializeDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLetMaterializeDeclaration(HqlParser.LetMaterializeDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letMaterializeDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLetMaterializeDeclaration(HqlParser.LetMaterializeDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letEntityGroupDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterLetEntityGroupDeclaration(HqlParser.LetEntityGroupDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letEntityGroupDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitLetEntityGroupDeclaration(HqlParser.LetEntityGroupDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letFunctionParameterList}.
	 * @param ctx the parse tree
	 */
	void enterLetFunctionParameterList(HqlParser.LetFunctionParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letFunctionParameterList}.
	 * @param ctx the parse tree
	 */
	void exitLetFunctionParameterList(HqlParser.LetFunctionParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scalarParameter}.
	 * @param ctx the parse tree
	 */
	void enterScalarParameter(HqlParser.ScalarParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scalarParameter}.
	 * @param ctx the parse tree
	 */
	void exitScalarParameter(HqlParser.ScalarParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scalarParameterDefault}.
	 * @param ctx the parse tree
	 */
	void enterScalarParameterDefault(HqlParser.ScalarParameterDefaultContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scalarParameterDefault}.
	 * @param ctx the parse tree
	 */
	void exitScalarParameterDefault(HqlParser.ScalarParameterDefaultContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#tabularParameter}.
	 * @param ctx the parse tree
	 */
	void enterTabularParameter(HqlParser.TabularParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#tabularParameter}.
	 * @param ctx the parse tree
	 */
	void exitTabularParameter(HqlParser.TabularParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#tabularParameterOpenSchema}.
	 * @param ctx the parse tree
	 */
	void enterTabularParameterOpenSchema(HqlParser.TabularParameterOpenSchemaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#tabularParameterOpenSchema}.
	 * @param ctx the parse tree
	 */
	void exitTabularParameterOpenSchema(HqlParser.TabularParameterOpenSchemaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#tabularParameterRowSchema}.
	 * @param ctx the parse tree
	 */
	void enterTabularParameterRowSchema(HqlParser.TabularParameterRowSchemaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#tabularParameterRowSchema}.
	 * @param ctx the parse tree
	 */
	void exitTabularParameterRowSchema(HqlParser.TabularParameterRowSchemaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#tabularParameterRowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterTabularParameterRowSchemaColumnDeclaration(HqlParser.TabularParameterRowSchemaColumnDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#tabularParameterRowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitTabularParameterRowSchemaColumnDeclaration(HqlParser.TabularParameterRowSchemaColumnDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letFunctionBody}.
	 * @param ctx the parse tree
	 */
	void enterLetFunctionBody(HqlParser.LetFunctionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letFunctionBody}.
	 * @param ctx the parse tree
	 */
	void exitLetFunctionBody(HqlParser.LetFunctionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#letFunctionBodyStatement}.
	 * @param ctx the parse tree
	 */
	void enterLetFunctionBodyStatement(HqlParser.LetFunctionBodyStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#letFunctionBodyStatement}.
	 * @param ctx the parse tree
	 */
	void exitLetFunctionBodyStatement(HqlParser.LetFunctionBodyStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternStatement(HqlParser.DeclarePatternStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternStatement(HqlParser.DeclarePatternStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternDefinition}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternDefinition(HqlParser.DeclarePatternDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternDefinition}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternDefinition(HqlParser.DeclarePatternDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternParameterList}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternParameterList(HqlParser.DeclarePatternParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternParameterList}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternParameterList(HqlParser.DeclarePatternParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternParameter}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternParameter(HqlParser.DeclarePatternParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternParameter}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternParameter(HqlParser.DeclarePatternParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternPathParameter}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternPathParameter(HqlParser.DeclarePatternPathParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternPathParameter}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternPathParameter(HqlParser.DeclarePatternPathParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternRule}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternRule(HqlParser.DeclarePatternRuleContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternRule}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternRule(HqlParser.DeclarePatternRuleContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternRuleArgumentList}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternRuleArgumentList(HqlParser.DeclarePatternRuleArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternRuleArgumentList}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternRuleArgumentList(HqlParser.DeclarePatternRuleArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternRulePathArgument}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternRulePathArgument(HqlParser.DeclarePatternRulePathArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternRulePathArgument}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternRulePathArgument(HqlParser.DeclarePatternRulePathArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternRuleArgument}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternRuleArgument(HqlParser.DeclarePatternRuleArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternRuleArgument}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternRuleArgument(HqlParser.DeclarePatternRuleArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declarePatternBody}.
	 * @param ctx the parse tree
	 */
	void enterDeclarePatternBody(HqlParser.DeclarePatternBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declarePatternBody}.
	 * @param ctx the parse tree
	 */
	void exitDeclarePatternBody(HqlParser.DeclarePatternBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#restrictAccessStatement}.
	 * @param ctx the parse tree
	 */
	void enterRestrictAccessStatement(HqlParser.RestrictAccessStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#restrictAccessStatement}.
	 * @param ctx the parse tree
	 */
	void exitRestrictAccessStatement(HqlParser.RestrictAccessStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#restrictAccessStatementEntity}.
	 * @param ctx the parse tree
	 */
	void enterRestrictAccessStatementEntity(HqlParser.RestrictAccessStatementEntityContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#restrictAccessStatementEntity}.
	 * @param ctx the parse tree
	 */
	void exitRestrictAccessStatementEntity(HqlParser.RestrictAccessStatementEntityContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void enterSetStatement(HqlParser.SetStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#setStatement}.
	 * @param ctx the parse tree
	 */
	void exitSetStatement(HqlParser.SetStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#setStatementOptionValue}.
	 * @param ctx the parse tree
	 */
	void enterSetStatementOptionValue(HqlParser.SetStatementOptionValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#setStatementOptionValue}.
	 * @param ctx the parse tree
	 */
	void exitSetStatementOptionValue(HqlParser.SetStatementOptionValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declareQueryParametersStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeclareQueryParametersStatement(HqlParser.DeclareQueryParametersStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declareQueryParametersStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeclareQueryParametersStatement(HqlParser.DeclareQueryParametersStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#declareQueryParametersStatementParameter}.
	 * @param ctx the parse tree
	 */
	void enterDeclareQueryParametersStatementParameter(HqlParser.DeclareQueryParametersStatementParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#declareQueryParametersStatementParameter}.
	 * @param ctx the parse tree
	 */
	void exitDeclareQueryParametersStatementParameter(HqlParser.DeclareQueryParametersStatementParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#queryStatement}.
	 * @param ctx the parse tree
	 */
	void enterQueryStatement(HqlParser.QueryStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#queryStatement}.
	 * @param ctx the parse tree
	 */
	void exitQueryStatement(HqlParser.QueryStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(HqlParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(HqlParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#pipeExpression}.
	 * @param ctx the parse tree
	 */
	void enterPipeExpression(HqlParser.PipeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#pipeExpression}.
	 * @param ctx the parse tree
	 */
	void exitPipeExpression(HqlParser.PipeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#pipedOperator}.
	 * @param ctx the parse tree
	 */
	void enterPipedOperator(HqlParser.PipedOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#pipedOperator}.
	 * @param ctx the parse tree
	 */
	void exitPipedOperator(HqlParser.PipedOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#pipeSubExpression}.
	 * @param ctx the parse tree
	 */
	void enterPipeSubExpression(HqlParser.PipeSubExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#pipeSubExpression}.
	 * @param ctx the parse tree
	 */
	void exitPipeSubExpression(HqlParser.PipeSubExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#beforePipeExpression}.
	 * @param ctx the parse tree
	 */
	void enterBeforePipeExpression(HqlParser.BeforePipeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#beforePipeExpression}.
	 * @param ctx the parse tree
	 */
	void exitBeforePipeExpression(HqlParser.BeforePipeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#afterPipeOperator}.
	 * @param ctx the parse tree
	 */
	void enterAfterPipeOperator(HqlParser.AfterPipeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#afterPipeOperator}.
	 * @param ctx the parse tree
	 */
	void exitAfterPipeOperator(HqlParser.AfterPipeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#beforeOrAfterPipeOperator}.
	 * @param ctx the parse tree
	 */
	void enterBeforeOrAfterPipeOperator(HqlParser.BeforeOrAfterPipeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#beforeOrAfterPipeOperator}.
	 * @param ctx the parse tree
	 */
	void exitBeforeOrAfterPipeOperator(HqlParser.BeforeOrAfterPipeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#forkPipeOperator}.
	 * @param ctx the parse tree
	 */
	void enterForkPipeOperator(HqlParser.ForkPipeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#forkPipeOperator}.
	 * @param ctx the parse tree
	 */
	void exitForkPipeOperator(HqlParser.ForkPipeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#asOperator}.
	 * @param ctx the parse tree
	 */
	void enterAsOperator(HqlParser.AsOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#asOperator}.
	 * @param ctx the parse tree
	 */
	void exitAsOperator(HqlParser.AsOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#assertSchemaOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssertSchemaOperator(HqlParser.AssertSchemaOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#assertSchemaOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssertSchemaOperator(HqlParser.AssertSchemaOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#consumeOperator}.
	 * @param ctx the parse tree
	 */
	void enterConsumeOperator(HqlParser.ConsumeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#consumeOperator}.
	 * @param ctx the parse tree
	 */
	void exitConsumeOperator(HqlParser.ConsumeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#countOperator}.
	 * @param ctx the parse tree
	 */
	void enterCountOperator(HqlParser.CountOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#countOperator}.
	 * @param ctx the parse tree
	 */
	void exitCountOperator(HqlParser.CountOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#countOperatorAsClause}.
	 * @param ctx the parse tree
	 */
	void enterCountOperatorAsClause(HqlParser.CountOperatorAsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#countOperatorAsClause}.
	 * @param ctx the parse tree
	 */
	void exitCountOperatorAsClause(HqlParser.CountOperatorAsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#distinctOperator}.
	 * @param ctx the parse tree
	 */
	void enterDistinctOperator(HqlParser.DistinctOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#distinctOperator}.
	 * @param ctx the parse tree
	 */
	void exitDistinctOperator(HqlParser.DistinctOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#distinctOperatorStarTarget}.
	 * @param ctx the parse tree
	 */
	void enterDistinctOperatorStarTarget(HqlParser.DistinctOperatorStarTargetContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#distinctOperatorStarTarget}.
	 * @param ctx the parse tree
	 */
	void exitDistinctOperatorStarTarget(HqlParser.DistinctOperatorStarTargetContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#distinctOperatorColumnListTarget}.
	 * @param ctx the parse tree
	 */
	void enterDistinctOperatorColumnListTarget(HqlParser.DistinctOperatorColumnListTargetContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#distinctOperatorColumnListTarget}.
	 * @param ctx the parse tree
	 */
	void exitDistinctOperatorColumnListTarget(HqlParser.DistinctOperatorColumnListTargetContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#evaluateOperator}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateOperator(HqlParser.EvaluateOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#evaluateOperator}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateOperator(HqlParser.EvaluateOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#evaluateOperatorSchemaClause}.
	 * @param ctx the parse tree
	 */
	void enterEvaluateOperatorSchemaClause(HqlParser.EvaluateOperatorSchemaClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#evaluateOperatorSchemaClause}.
	 * @param ctx the parse tree
	 */
	void exitEvaluateOperatorSchemaClause(HqlParser.EvaluateOperatorSchemaClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#extendOperator}.
	 * @param ctx the parse tree
	 */
	void enterExtendOperator(HqlParser.ExtendOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#extendOperator}.
	 * @param ctx the parse tree
	 */
	void exitExtendOperator(HqlParser.ExtendOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#executeAndCacheOperator}.
	 * @param ctx the parse tree
	 */
	void enterExecuteAndCacheOperator(HqlParser.ExecuteAndCacheOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#executeAndCacheOperator}.
	 * @param ctx the parse tree
	 */
	void exitExecuteAndCacheOperator(HqlParser.ExecuteAndCacheOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#facetByOperator}.
	 * @param ctx the parse tree
	 */
	void enterFacetByOperator(HqlParser.FacetByOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#facetByOperator}.
	 * @param ctx the parse tree
	 */
	void exitFacetByOperator(HqlParser.FacetByOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#facetByOperatorWithOperatorClause}.
	 * @param ctx the parse tree
	 */
	void enterFacetByOperatorWithOperatorClause(HqlParser.FacetByOperatorWithOperatorClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#facetByOperatorWithOperatorClause}.
	 * @param ctx the parse tree
	 */
	void exitFacetByOperatorWithOperatorClause(HqlParser.FacetByOperatorWithOperatorClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#facetByOperatorWithExpressionClause}.
	 * @param ctx the parse tree
	 */
	void enterFacetByOperatorWithExpressionClause(HqlParser.FacetByOperatorWithExpressionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#facetByOperatorWithExpressionClause}.
	 * @param ctx the parse tree
	 */
	void exitFacetByOperatorWithExpressionClause(HqlParser.FacetByOperatorWithExpressionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperator}.
	 * @param ctx the parse tree
	 */
	void enterFindOperator(HqlParser.FindOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperator}.
	 * @param ctx the parse tree
	 */
	void exitFindOperator(HqlParser.FindOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorParametersWhereClause}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorParametersWhereClause(HqlParser.FindOperatorParametersWhereClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorParametersWhereClause}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorParametersWhereClause(HqlParser.FindOperatorParametersWhereClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorInClause}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorInClause(HqlParser.FindOperatorInClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorInClause}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorInClause(HqlParser.FindOperatorInClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectClause}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorProjectClause(HqlParser.FindOperatorProjectClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectClause}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorProjectClause(HqlParser.FindOperatorProjectClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectExpression}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorProjectExpression(HqlParser.FindOperatorProjectExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectExpression}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorProjectExpression(HqlParser.FindOperatorProjectExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorColumnExpression}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorColumnExpression(HqlParser.FindOperatorColumnExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorColumnExpression}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorColumnExpression(HqlParser.FindOperatorColumnExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorOptionalColumnType}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorOptionalColumnType(HqlParser.FindOperatorOptionalColumnTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorOptionalColumnType}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorOptionalColumnType(HqlParser.FindOperatorOptionalColumnTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorPackExpression}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorPackExpression(HqlParser.FindOperatorPackExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorPackExpression}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorPackExpression(HqlParser.FindOperatorPackExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectSmartClause}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorProjectSmartClause(HqlParser.FindOperatorProjectSmartClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectSmartClause}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorProjectSmartClause(HqlParser.FindOperatorProjectSmartClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectAwayClause}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorProjectAwayClause(HqlParser.FindOperatorProjectAwayClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectAwayClause}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorProjectAwayClause(HqlParser.FindOperatorProjectAwayClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectAwayStar}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorProjectAwayStar(HqlParser.FindOperatorProjectAwayStarContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectAwayStar}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorProjectAwayStar(HqlParser.FindOperatorProjectAwayStarContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorProjectAwayColumnList}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorProjectAwayColumnList(HqlParser.FindOperatorProjectAwayColumnListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorProjectAwayColumnList}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorProjectAwayColumnList(HqlParser.FindOperatorProjectAwayColumnListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorSource}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorSource(HqlParser.FindOperatorSourceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorSource}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorSource(HqlParser.FindOperatorSourceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#findOperatorSourceEntityExpression}.
	 * @param ctx the parse tree
	 */
	void enterFindOperatorSourceEntityExpression(HqlParser.FindOperatorSourceEntityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#findOperatorSourceEntityExpression}.
	 * @param ctx the parse tree
	 */
	void exitFindOperatorSourceEntityExpression(HqlParser.FindOperatorSourceEntityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#forkOperator}.
	 * @param ctx the parse tree
	 */
	void enterForkOperator(HqlParser.ForkOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#forkOperator}.
	 * @param ctx the parse tree
	 */
	void exitForkOperator(HqlParser.ForkOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#forkOperatorFork}.
	 * @param ctx the parse tree
	 */
	void enterForkOperatorFork(HqlParser.ForkOperatorForkContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#forkOperatorFork}.
	 * @param ctx the parse tree
	 */
	void exitForkOperatorFork(HqlParser.ForkOperatorForkContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#forkOperatorExpressionName}.
	 * @param ctx the parse tree
	 */
	void enterForkOperatorExpressionName(HqlParser.ForkOperatorExpressionNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#forkOperatorExpressionName}.
	 * @param ctx the parse tree
	 */
	void exitForkOperatorExpressionName(HqlParser.ForkOperatorExpressionNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#forkOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterForkOperatorExpression(HqlParser.ForkOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#forkOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitForkOperatorExpression(HqlParser.ForkOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#forkOperatorPipedOperator}.
	 * @param ctx the parse tree
	 */
	void enterForkOperatorPipedOperator(HqlParser.ForkOperatorPipedOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#forkOperatorPipedOperator}.
	 * @param ctx the parse tree
	 */
	void exitForkOperatorPipedOperator(HqlParser.ForkOperatorPipedOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#getSchemaOperator}.
	 * @param ctx the parse tree
	 */
	void enterGetSchemaOperator(HqlParser.GetSchemaOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#getSchemaOperator}.
	 * @param ctx the parse tree
	 */
	void exitGetSchemaOperator(HqlParser.GetSchemaOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMarkComponentsOperator}.
	 * @param ctx the parse tree
	 */
	void enterGraphMarkComponentsOperator(HqlParser.GraphMarkComponentsOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMarkComponentsOperator}.
	 * @param ctx the parse tree
	 */
	void exitGraphMarkComponentsOperator(HqlParser.GraphMarkComponentsOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchOperator}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchOperator(HqlParser.GraphMatchOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchOperator}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchOperator(HqlParser.GraphMatchOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchPattern}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchPattern(HqlParser.GraphMatchPatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchPattern}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchPattern(HqlParser.GraphMatchPatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternNode}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchPatternNode(HqlParser.GraphMatchPatternNodeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternNode}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchPatternNode(HqlParser.GraphMatchPatternNodeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternUnnamedEdge}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchPatternUnnamedEdge(HqlParser.GraphMatchPatternUnnamedEdgeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternUnnamedEdge}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchPatternUnnamedEdge(HqlParser.GraphMatchPatternUnnamedEdgeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternNamedEdge}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchPatternNamedEdge(HqlParser.GraphMatchPatternNamedEdgeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternNamedEdge}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchPatternNamedEdge(HqlParser.GraphMatchPatternNamedEdgeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchPatternRange}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchPatternRange(HqlParser.GraphMatchPatternRangeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchPatternRange}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchPatternRange(HqlParser.GraphMatchPatternRangeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchWhereClause}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchWhereClause(HqlParser.GraphMatchWhereClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchWhereClause}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchWhereClause(HqlParser.GraphMatchWhereClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMatchProjectClause}.
	 * @param ctx the parse tree
	 */
	void enterGraphMatchProjectClause(HqlParser.GraphMatchProjectClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMatchProjectClause}.
	 * @param ctx the parse tree
	 */
	void exitGraphMatchProjectClause(HqlParser.GraphMatchProjectClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphMergeOperator}.
	 * @param ctx the parse tree
	 */
	void enterGraphMergeOperator(HqlParser.GraphMergeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphMergeOperator}.
	 * @param ctx the parse tree
	 */
	void exitGraphMergeOperator(HqlParser.GraphMergeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphToTableOperator}.
	 * @param ctx the parse tree
	 */
	void enterGraphToTableOperator(HqlParser.GraphToTableOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphToTableOperator}.
	 * @param ctx the parse tree
	 */
	void exitGraphToTableOperator(HqlParser.GraphToTableOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphToTableOutput}.
	 * @param ctx the parse tree
	 */
	void enterGraphToTableOutput(HqlParser.GraphToTableOutputContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphToTableOutput}.
	 * @param ctx the parse tree
	 */
	void exitGraphToTableOutput(HqlParser.GraphToTableOutputContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphToTableAsClause}.
	 * @param ctx the parse tree
	 */
	void enterGraphToTableAsClause(HqlParser.GraphToTableAsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphToTableAsClause}.
	 * @param ctx the parse tree
	 */
	void exitGraphToTableAsClause(HqlParser.GraphToTableAsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#graphShortestPathsOperator}.
	 * @param ctx the parse tree
	 */
	void enterGraphShortestPathsOperator(HqlParser.GraphShortestPathsOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#graphShortestPathsOperator}.
	 * @param ctx the parse tree
	 */
	void exitGraphShortestPathsOperator(HqlParser.GraphShortestPathsOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#invokeOperator}.
	 * @param ctx the parse tree
	 */
	void enterInvokeOperator(HqlParser.InvokeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#invokeOperator}.
	 * @param ctx the parse tree
	 */
	void exitInvokeOperator(HqlParser.InvokeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#joinOperator}.
	 * @param ctx the parse tree
	 */
	void enterJoinOperator(HqlParser.JoinOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#joinOperator}.
	 * @param ctx the parse tree
	 */
	void exitJoinOperator(HqlParser.JoinOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#joinOperatorOnClause}.
	 * @param ctx the parse tree
	 */
	void enterJoinOperatorOnClause(HqlParser.JoinOperatorOnClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#joinOperatorOnClause}.
	 * @param ctx the parse tree
	 */
	void exitJoinOperatorOnClause(HqlParser.JoinOperatorOnClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#joinOperatorWhereClause}.
	 * @param ctx the parse tree
	 */
	void enterJoinOperatorWhereClause(HqlParser.JoinOperatorWhereClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#joinOperatorWhereClause}.
	 * @param ctx the parse tree
	 */
	void exitJoinOperatorWhereClause(HqlParser.JoinOperatorWhereClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#lookupOperator}.
	 * @param ctx the parse tree
	 */
	void enterLookupOperator(HqlParser.LookupOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#lookupOperator}.
	 * @param ctx the parse tree
	 */
	void exitLookupOperator(HqlParser.LookupOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#macroExpandOperator}.
	 * @param ctx the parse tree
	 */
	void enterMacroExpandOperator(HqlParser.MacroExpandOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#macroExpandOperator}.
	 * @param ctx the parse tree
	 */
	void exitMacroExpandOperator(HqlParser.MacroExpandOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#macroExpandEntityGroup}.
	 * @param ctx the parse tree
	 */
	void enterMacroExpandEntityGroup(HqlParser.MacroExpandEntityGroupContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#macroExpandEntityGroup}.
	 * @param ctx the parse tree
	 */
	void exitMacroExpandEntityGroup(HqlParser.MacroExpandEntityGroupContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityGroupExpression}.
	 * @param ctx the parse tree
	 */
	void enterEntityGroupExpression(HqlParser.EntityGroupExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityGroupExpression}.
	 * @param ctx the parse tree
	 */
	void exitEntityGroupExpression(HqlParser.EntityGroupExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeGraphOperator}.
	 * @param ctx the parse tree
	 */
	void enterMakeGraphOperator(HqlParser.MakeGraphOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeGraphOperator}.
	 * @param ctx the parse tree
	 */
	void exitMakeGraphOperator(HqlParser.MakeGraphOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeGraphIdClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeGraphIdClause(HqlParser.MakeGraphIdClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeGraphIdClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeGraphIdClause(HqlParser.MakeGraphIdClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeGraphTablesAndKeysClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeGraphTablesAndKeysClause(HqlParser.MakeGraphTablesAndKeysClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeGraphTablesAndKeysClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeGraphTablesAndKeysClause(HqlParser.MakeGraphTablesAndKeysClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeGraphPartitionedByClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeGraphPartitionedByClause(HqlParser.MakeGraphPartitionedByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeGraphPartitionedByClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeGraphPartitionedByClause(HqlParser.MakeGraphPartitionedByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperator}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperator(HqlParser.MakeSeriesOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperator}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperator(HqlParser.MakeSeriesOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorOnClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperatorOnClause(HqlParser.MakeSeriesOperatorOnClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorOnClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperatorOnClause(HqlParser.MakeSeriesOperatorOnClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorAggregation}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperatorAggregation(HqlParser.MakeSeriesOperatorAggregationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorAggregation}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperatorAggregation(HqlParser.MakeSeriesOperatorAggregationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorExpressionDefaultClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperatorExpressionDefaultClause(HqlParser.MakeSeriesOperatorExpressionDefaultClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorExpressionDefaultClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperatorExpressionDefaultClause(HqlParser.MakeSeriesOperatorExpressionDefaultClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorInRangeClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperatorInRangeClause(HqlParser.MakeSeriesOperatorInRangeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorInRangeClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperatorInRangeClause(HqlParser.MakeSeriesOperatorInRangeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorFromToStepClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperatorFromToStepClause(HqlParser.MakeSeriesOperatorFromToStepClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorFromToStepClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperatorFromToStepClause(HqlParser.MakeSeriesOperatorFromToStepClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#makeSeriesOperatorByClause}.
	 * @param ctx the parse tree
	 */
	void enterMakeSeriesOperatorByClause(HqlParser.MakeSeriesOperatorByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#makeSeriesOperatorByClause}.
	 * @param ctx the parse tree
	 */
	void exitMakeSeriesOperatorByClause(HqlParser.MakeSeriesOperatorByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvapplyOperator}.
	 * @param ctx the parse tree
	 */
	void enterMvapplyOperator(HqlParser.MvapplyOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvapplyOperator}.
	 * @param ctx the parse tree
	 */
	void exitMvapplyOperator(HqlParser.MvapplyOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorLimitClause}.
	 * @param ctx the parse tree
	 */
	void enterMvapplyOperatorLimitClause(HqlParser.MvapplyOperatorLimitClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorLimitClause}.
	 * @param ctx the parse tree
	 */
	void exitMvapplyOperatorLimitClause(HqlParser.MvapplyOperatorLimitClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorIdClause}.
	 * @param ctx the parse tree
	 */
	void enterMvapplyOperatorIdClause(HqlParser.MvapplyOperatorIdClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorIdClause}.
	 * @param ctx the parse tree
	 */
	void exitMvapplyOperatorIdClause(HqlParser.MvapplyOperatorIdClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterMvapplyOperatorExpression(HqlParser.MvapplyOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitMvapplyOperatorExpression(HqlParser.MvapplyOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvapplyOperatorExpressionToClause}.
	 * @param ctx the parse tree
	 */
	void enterMvapplyOperatorExpressionToClause(HqlParser.MvapplyOperatorExpressionToClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvapplyOperatorExpressionToClause}.
	 * @param ctx the parse tree
	 */
	void exitMvapplyOperatorExpressionToClause(HqlParser.MvapplyOperatorExpressionToClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvexpandOperator}.
	 * @param ctx the parse tree
	 */
	void enterMvexpandOperator(HqlParser.MvexpandOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvexpandOperator}.
	 * @param ctx the parse tree
	 */
	void exitMvexpandOperator(HqlParser.MvexpandOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#mvexpandOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterMvexpandOperatorExpression(HqlParser.MvexpandOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#mvexpandOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitMvexpandOperatorExpression(HqlParser.MvexpandOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseOperator}.
	 * @param ctx the parse tree
	 */
	void enterParseOperator(HqlParser.ParseOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseOperator}.
	 * @param ctx the parse tree
	 */
	void exitParseOperator(HqlParser.ParseOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseOperatorKindClause}.
	 * @param ctx the parse tree
	 */
	void enterParseOperatorKindClause(HqlParser.ParseOperatorKindClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseOperatorKindClause}.
	 * @param ctx the parse tree
	 */
	void exitParseOperatorKindClause(HqlParser.ParseOperatorKindClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseOperatorFlagsClause}.
	 * @param ctx the parse tree
	 */
	void enterParseOperatorFlagsClause(HqlParser.ParseOperatorFlagsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseOperatorFlagsClause}.
	 * @param ctx the parse tree
	 */
	void exitParseOperatorFlagsClause(HqlParser.ParseOperatorFlagsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseOperatorNameAndOptionalType}.
	 * @param ctx the parse tree
	 */
	void enterParseOperatorNameAndOptionalType(HqlParser.ParseOperatorNameAndOptionalTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseOperatorNameAndOptionalType}.
	 * @param ctx the parse tree
	 */
	void exitParseOperatorNameAndOptionalType(HqlParser.ParseOperatorNameAndOptionalTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseOperatorPattern}.
	 * @param ctx the parse tree
	 */
	void enterParseOperatorPattern(HqlParser.ParseOperatorPatternContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseOperatorPattern}.
	 * @param ctx the parse tree
	 */
	void exitParseOperatorPattern(HqlParser.ParseOperatorPatternContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseOperatorPatternSegment}.
	 * @param ctx the parse tree
	 */
	void enterParseOperatorPatternSegment(HqlParser.ParseOperatorPatternSegmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseOperatorPatternSegment}.
	 * @param ctx the parse tree
	 */
	void exitParseOperatorPatternSegment(HqlParser.ParseOperatorPatternSegmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseWhereOperator}.
	 * @param ctx the parse tree
	 */
	void enterParseWhereOperator(HqlParser.ParseWhereOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseWhereOperator}.
	 * @param ctx the parse tree
	 */
	void exitParseWhereOperator(HqlParser.ParseWhereOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseKvOperator}.
	 * @param ctx the parse tree
	 */
	void enterParseKvOperator(HqlParser.ParseKvOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseKvOperator}.
	 * @param ctx the parse tree
	 */
	void exitParseKvOperator(HqlParser.ParseKvOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parseKvWithClause}.
	 * @param ctx the parse tree
	 */
	void enterParseKvWithClause(HqlParser.ParseKvWithClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parseKvWithClause}.
	 * @param ctx the parse tree
	 */
	void exitParseKvWithClause(HqlParser.ParseKvWithClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#partitionOperator}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOperator(HqlParser.PartitionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#partitionOperator}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOperator(HqlParser.PartitionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#partitionOperatorInClause}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOperatorInClause(HqlParser.PartitionOperatorInClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#partitionOperatorInClause}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOperatorInClause(HqlParser.PartitionOperatorInClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#partitionOperatorSubExpressionBody}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOperatorSubExpressionBody(HqlParser.PartitionOperatorSubExpressionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#partitionOperatorSubExpressionBody}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOperatorSubExpressionBody(HqlParser.PartitionOperatorSubExpressionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#partitionOperatorFullExpressionBody}.
	 * @param ctx the parse tree
	 */
	void enterPartitionOperatorFullExpressionBody(HqlParser.PartitionOperatorFullExpressionBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#partitionOperatorFullExpressionBody}.
	 * @param ctx the parse tree
	 */
	void exitPartitionOperatorFullExpressionBody(HqlParser.PartitionOperatorFullExpressionBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#partitionByOperator}.
	 * @param ctx the parse tree
	 */
	void enterPartitionByOperator(HqlParser.PartitionByOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#partitionByOperator}.
	 * @param ctx the parse tree
	 */
	void exitPartitionByOperator(HqlParser.PartitionByOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#partitionByOperatorIdClause}.
	 * @param ctx the parse tree
	 */
	void enterPartitionByOperatorIdClause(HqlParser.PartitionByOperatorIdClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#partitionByOperatorIdClause}.
	 * @param ctx the parse tree
	 */
	void exitPartitionByOperatorIdClause(HqlParser.PartitionByOperatorIdClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#printOperator}.
	 * @param ctx the parse tree
	 */
	void enterPrintOperator(HqlParser.PrintOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#printOperator}.
	 * @param ctx the parse tree
	 */
	void exitPrintOperator(HqlParser.PrintOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#projectAwayOperator}.
	 * @param ctx the parse tree
	 */
	void enterProjectAwayOperator(HqlParser.ProjectAwayOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#projectAwayOperator}.
	 * @param ctx the parse tree
	 */
	void exitProjectAwayOperator(HqlParser.ProjectAwayOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#projectKeepOperator}.
	 * @param ctx the parse tree
	 */
	void enterProjectKeepOperator(HqlParser.ProjectKeepOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#projectKeepOperator}.
	 * @param ctx the parse tree
	 */
	void exitProjectKeepOperator(HqlParser.ProjectKeepOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#projectOperator}.
	 * @param ctx the parse tree
	 */
	void enterProjectOperator(HqlParser.ProjectOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#projectOperator}.
	 * @param ctx the parse tree
	 */
	void exitProjectOperator(HqlParser.ProjectOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#projectRenameOperator}.
	 * @param ctx the parse tree
	 */
	void enterProjectRenameOperator(HqlParser.ProjectRenameOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#projectRenameOperator}.
	 * @param ctx the parse tree
	 */
	void exitProjectRenameOperator(HqlParser.ProjectRenameOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#projectReorderOperator}.
	 * @param ctx the parse tree
	 */
	void enterProjectReorderOperator(HqlParser.ProjectReorderOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#projectReorderOperator}.
	 * @param ctx the parse tree
	 */
	void exitProjectReorderOperator(HqlParser.ProjectReorderOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#projectReorderExpression}.
	 * @param ctx the parse tree
	 */
	void enterProjectReorderExpression(HqlParser.ProjectReorderExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#projectReorderExpression}.
	 * @param ctx the parse tree
	 */
	void exitProjectReorderExpression(HqlParser.ProjectReorderExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#reduceByOperator}.
	 * @param ctx the parse tree
	 */
	void enterReduceByOperator(HqlParser.ReduceByOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#reduceByOperator}.
	 * @param ctx the parse tree
	 */
	void exitReduceByOperator(HqlParser.ReduceByOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#reduceByWithClause}.
	 * @param ctx the parse tree
	 */
	void enterReduceByWithClause(HqlParser.ReduceByWithClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#reduceByWithClause}.
	 * @param ctx the parse tree
	 */
	void exitReduceByWithClause(HqlParser.ReduceByWithClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#renderOperator}.
	 * @param ctx the parse tree
	 */
	void enterRenderOperator(HqlParser.RenderOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#renderOperator}.
	 * @param ctx the parse tree
	 */
	void exitRenderOperator(HqlParser.RenderOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#renderOperatorWithClause}.
	 * @param ctx the parse tree
	 */
	void enterRenderOperatorWithClause(HqlParser.RenderOperatorWithClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#renderOperatorWithClause}.
	 * @param ctx the parse tree
	 */
	void exitRenderOperatorWithClause(HqlParser.RenderOperatorWithClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#renderOperatorLegacyPropertyList}.
	 * @param ctx the parse tree
	 */
	void enterRenderOperatorLegacyPropertyList(HqlParser.RenderOperatorLegacyPropertyListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#renderOperatorLegacyPropertyList}.
	 * @param ctx the parse tree
	 */
	void exitRenderOperatorLegacyPropertyList(HqlParser.RenderOperatorLegacyPropertyListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#renderOperatorProperty}.
	 * @param ctx the parse tree
	 */
	void enterRenderOperatorProperty(HqlParser.RenderOperatorPropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#renderOperatorProperty}.
	 * @param ctx the parse tree
	 */
	void exitRenderOperatorProperty(HqlParser.RenderOperatorPropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#renderPropertyNameList}.
	 * @param ctx the parse tree
	 */
	void enterRenderPropertyNameList(HqlParser.RenderPropertyNameListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#renderPropertyNameList}.
	 * @param ctx the parse tree
	 */
	void exitRenderPropertyNameList(HqlParser.RenderPropertyNameListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#renderOperatorLegacyProperty}.
	 * @param ctx the parse tree
	 */
	void enterRenderOperatorLegacyProperty(HqlParser.RenderOperatorLegacyPropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#renderOperatorLegacyProperty}.
	 * @param ctx the parse tree
	 */
	void exitRenderOperatorLegacyProperty(HqlParser.RenderOperatorLegacyPropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#sampleDistinctOperator}.
	 * @param ctx the parse tree
	 */
	void enterSampleDistinctOperator(HqlParser.SampleDistinctOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#sampleDistinctOperator}.
	 * @param ctx the parse tree
	 */
	void exitSampleDistinctOperator(HqlParser.SampleDistinctOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#sampleOperator}.
	 * @param ctx the parse tree
	 */
	void enterSampleOperator(HqlParser.SampleOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#sampleOperator}.
	 * @param ctx the parse tree
	 */
	void exitSampleOperator(HqlParser.SampleOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperator}.
	 * @param ctx the parse tree
	 */
	void enterScanOperator(HqlParser.ScanOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperator}.
	 * @param ctx the parse tree
	 */
	void exitScanOperator(HqlParser.ScanOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorOrderByClause}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorOrderByClause(HqlParser.ScanOperatorOrderByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorOrderByClause}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorOrderByClause(HqlParser.ScanOperatorOrderByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorPartitionByClause}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorPartitionByClause(HqlParser.ScanOperatorPartitionByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorPartitionByClause}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorPartitionByClause(HqlParser.ScanOperatorPartitionByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorDeclareClause}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorDeclareClause(HqlParser.ScanOperatorDeclareClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorDeclareClause}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorDeclareClause(HqlParser.ScanOperatorDeclareClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorStep}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorStep(HqlParser.ScanOperatorStepContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorStep}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorStep(HqlParser.ScanOperatorStepContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorStepOutputClause}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorStepOutputClause(HqlParser.ScanOperatorStepOutputClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorStepOutputClause}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorStepOutputClause(HqlParser.ScanOperatorStepOutputClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorBody}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorBody(HqlParser.ScanOperatorBodyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorBody}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorBody(HqlParser.ScanOperatorBodyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scanOperatorAssignment}.
	 * @param ctx the parse tree
	 */
	void enterScanOperatorAssignment(HqlParser.ScanOperatorAssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scanOperatorAssignment}.
	 * @param ctx the parse tree
	 */
	void exitScanOperatorAssignment(HqlParser.ScanOperatorAssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#searchOperator}.
	 * @param ctx the parse tree
	 */
	void enterSearchOperator(HqlParser.SearchOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#searchOperator}.
	 * @param ctx the parse tree
	 */
	void exitSearchOperator(HqlParser.SearchOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#searchOperatorStarAndExpression}.
	 * @param ctx the parse tree
	 */
	void enterSearchOperatorStarAndExpression(HqlParser.SearchOperatorStarAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#searchOperatorStarAndExpression}.
	 * @param ctx the parse tree
	 */
	void exitSearchOperatorStarAndExpression(HqlParser.SearchOperatorStarAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#searchOperatorInClause}.
	 * @param ctx the parse tree
	 */
	void enterSearchOperatorInClause(HqlParser.SearchOperatorInClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#searchOperatorInClause}.
	 * @param ctx the parse tree
	 */
	void exitSearchOperatorInClause(HqlParser.SearchOperatorInClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#serializeOperator}.
	 * @param ctx the parse tree
	 */
	void enterSerializeOperator(HqlParser.SerializeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#serializeOperator}.
	 * @param ctx the parse tree
	 */
	void exitSerializeOperator(HqlParser.SerializeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#sortOperator}.
	 * @param ctx the parse tree
	 */
	void enterSortOperator(HqlParser.SortOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#sortOperator}.
	 * @param ctx the parse tree
	 */
	void exitSortOperator(HqlParser.SortOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#orderedExpression}.
	 * @param ctx the parse tree
	 */
	void enterOrderedExpression(HqlParser.OrderedExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#orderedExpression}.
	 * @param ctx the parse tree
	 */
	void exitOrderedExpression(HqlParser.OrderedExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#sortOrdering}.
	 * @param ctx the parse tree
	 */
	void enterSortOrdering(HqlParser.SortOrderingContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#sortOrdering}.
	 * @param ctx the parse tree
	 */
	void exitSortOrdering(HqlParser.SortOrderingContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#summarizeOperator}.
	 * @param ctx the parse tree
	 */
	void enterSummarizeOperator(HqlParser.SummarizeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#summarizeOperator}.
	 * @param ctx the parse tree
	 */
	void exitSummarizeOperator(HqlParser.SummarizeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#summarizeOperatorByClause}.
	 * @param ctx the parse tree
	 */
	void enterSummarizeOperatorByClause(HqlParser.SummarizeOperatorByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#summarizeOperatorByClause}.
	 * @param ctx the parse tree
	 */
	void exitSummarizeOperatorByClause(HqlParser.SummarizeOperatorByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#summarizeOperatorLegacyBinClause}.
	 * @param ctx the parse tree
	 */
	void enterSummarizeOperatorLegacyBinClause(HqlParser.SummarizeOperatorLegacyBinClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#summarizeOperatorLegacyBinClause}.
	 * @param ctx the parse tree
	 */
	void exitSummarizeOperatorLegacyBinClause(HqlParser.SummarizeOperatorLegacyBinClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#takeOperator}.
	 * @param ctx the parse tree
	 */
	void enterTakeOperator(HqlParser.TakeOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#takeOperator}.
	 * @param ctx the parse tree
	 */
	void exitTakeOperator(HqlParser.TakeOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#topOperator}.
	 * @param ctx the parse tree
	 */
	void enterTopOperator(HqlParser.TopOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#topOperator}.
	 * @param ctx the parse tree
	 */
	void exitTopOperator(HqlParser.TopOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#topHittersOperator}.
	 * @param ctx the parse tree
	 */
	void enterTopHittersOperator(HqlParser.TopHittersOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#topHittersOperator}.
	 * @param ctx the parse tree
	 */
	void exitTopHittersOperator(HqlParser.TopHittersOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#topHittersOperatorByClause}.
	 * @param ctx the parse tree
	 */
	void enterTopHittersOperatorByClause(HqlParser.TopHittersOperatorByClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#topHittersOperatorByClause}.
	 * @param ctx the parse tree
	 */
	void exitTopHittersOperatorByClause(HqlParser.TopHittersOperatorByClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#topNestedOperator}.
	 * @param ctx the parse tree
	 */
	void enterTopNestedOperator(HqlParser.TopNestedOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#topNestedOperator}.
	 * @param ctx the parse tree
	 */
	void exitTopNestedOperator(HqlParser.TopNestedOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#topNestedOperatorPart}.
	 * @param ctx the parse tree
	 */
	void enterTopNestedOperatorPart(HqlParser.TopNestedOperatorPartContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#topNestedOperatorPart}.
	 * @param ctx the parse tree
	 */
	void exitTopNestedOperatorPart(HqlParser.TopNestedOperatorPartContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#topNestedOperatorWithOthersClause}.
	 * @param ctx the parse tree
	 */
	void enterTopNestedOperatorWithOthersClause(HqlParser.TopNestedOperatorWithOthersClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#topNestedOperatorWithOthersClause}.
	 * @param ctx the parse tree
	 */
	void exitTopNestedOperatorWithOthersClause(HqlParser.TopNestedOperatorWithOthersClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#unionOperator}.
	 * @param ctx the parse tree
	 */
	void enterUnionOperator(HqlParser.UnionOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#unionOperator}.
	 * @param ctx the parse tree
	 */
	void exitUnionOperator(HqlParser.UnionOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#unionOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnionOperatorExpression(HqlParser.UnionOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#unionOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnionOperatorExpression(HqlParser.UnionOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#whereOperator}.
	 * @param ctx the parse tree
	 */
	void enterWhereOperator(HqlParser.WhereOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#whereOperator}.
	 * @param ctx the parse tree
	 */
	void exitWhereOperator(HqlParser.WhereOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#contextualSubExpression}.
	 * @param ctx the parse tree
	 */
	void enterContextualSubExpression(HqlParser.ContextualSubExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#contextualSubExpression}.
	 * @param ctx the parse tree
	 */
	void exitContextualSubExpression(HqlParser.ContextualSubExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#contextualPipeExpression}.
	 * @param ctx the parse tree
	 */
	void enterContextualPipeExpression(HqlParser.ContextualPipeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#contextualPipeExpression}.
	 * @param ctx the parse tree
	 */
	void exitContextualPipeExpression(HqlParser.ContextualPipeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#contextualPipeExpressionPipedOperator}.
	 * @param ctx the parse tree
	 */
	void enterContextualPipeExpressionPipedOperator(HqlParser.ContextualPipeExpressionPipedOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#contextualPipeExpressionPipedOperator}.
	 * @param ctx the parse tree
	 */
	void exitContextualPipeExpressionPipedOperator(HqlParser.ContextualPipeExpressionPipedOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#strictQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
	void enterStrictQueryOperatorParameter(HqlParser.StrictQueryOperatorParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#strictQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
	void exitStrictQueryOperatorParameter(HqlParser.StrictQueryOperatorParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#relaxedQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
	void enterRelaxedQueryOperatorParameter(HqlParser.RelaxedQueryOperatorParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#relaxedQueryOperatorParameter}.
	 * @param ctx the parse tree
	 */
	void exitRelaxedQueryOperatorParameter(HqlParser.RelaxedQueryOperatorParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#queryOperatorProperty}.
	 * @param ctx the parse tree
	 */
	void enterQueryOperatorProperty(HqlParser.QueryOperatorPropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#queryOperatorProperty}.
	 * @param ctx the parse tree
	 */
	void exitQueryOperatorProperty(HqlParser.QueryOperatorPropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#namedExpression}.
	 * @param ctx the parse tree
	 */
	void enterNamedExpression(HqlParser.NamedExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#namedExpression}.
	 * @param ctx the parse tree
	 */
	void exitNamedExpression(HqlParser.NamedExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#namedExpressionNameClause}.
	 * @param ctx the parse tree
	 */
	void enterNamedExpressionNameClause(HqlParser.NamedExpressionNameClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#namedExpressionNameClause}.
	 * @param ctx the parse tree
	 */
	void exitNamedExpressionNameClause(HqlParser.NamedExpressionNameClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#namedExpressionNameList}.
	 * @param ctx the parse tree
	 */
	void enterNamedExpressionNameList(HqlParser.NamedExpressionNameListContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#namedExpressionNameList}.
	 * @param ctx the parse tree
	 */
	void exitNamedExpressionNameList(HqlParser.NamedExpressionNameListContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scopedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	void enterScopedFunctionCallExpression(HqlParser.ScopedFunctionCallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scopedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	void exitScopedFunctionCallExpression(HqlParser.ScopedFunctionCallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#unnamedExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnnamedExpression(HqlParser.UnnamedExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#unnamedExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnnamedExpression(HqlParser.UnnamedExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpression(HqlParser.LogicalOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpression(HqlParser.LogicalOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#logicalOrOperation}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrOperation(HqlParser.LogicalOrOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#logicalOrOperation}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrOperation(HqlParser.LogicalOrOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpression(HqlParser.LogicalAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpression(HqlParser.LogicalAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#logicalAndOperation}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndOperation(HqlParser.LogicalAndOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#logicalAndOperation}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndOperation(HqlParser.LogicalAndOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(HqlParser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(HqlParser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#equalsEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualsEqualityExpression(HqlParser.EqualsEqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#equalsEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualsEqualityExpression(HqlParser.EqualsEqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#listEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void enterListEqualityExpression(HqlParser.ListEqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#listEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void exitListEqualityExpression(HqlParser.ListEqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#betweenEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void enterBetweenEqualityExpression(HqlParser.BetweenEqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#betweenEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void exitBetweenEqualityExpression(HqlParser.BetweenEqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#starEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void enterStarEqualityExpression(HqlParser.StarEqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#starEqualityExpression}.
	 * @param ctx the parse tree
	 */
	void exitStarEqualityExpression(HqlParser.StarEqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(HqlParser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(HqlParser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(HqlParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(HqlParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#additiveOperation}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveOperation(HqlParser.AdditiveOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#additiveOperation}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveOperation(HqlParser.AdditiveOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(HqlParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(HqlParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#multiplicativeOperation}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeOperation(HqlParser.MultiplicativeOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#multiplicativeOperation}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeOperation(HqlParser.MultiplicativeOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#stringOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringOperatorExpression(HqlParser.StringOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#stringOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringOperatorExpression(HqlParser.StringOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#stringBinaryOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringBinaryOperatorExpression(HqlParser.StringBinaryOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#stringBinaryOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringBinaryOperatorExpression(HqlParser.StringBinaryOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#stringBinaryOperation}.
	 * @param ctx the parse tree
	 */
	void enterStringBinaryOperation(HqlParser.StringBinaryOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#stringBinaryOperation}.
	 * @param ctx the parse tree
	 */
	void exitStringBinaryOperation(HqlParser.StringBinaryOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#stringBinaryOperator}.
	 * @param ctx the parse tree
	 */
	void enterStringBinaryOperator(HqlParser.StringBinaryOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#stringBinaryOperator}.
	 * @param ctx the parse tree
	 */
	void exitStringBinaryOperator(HqlParser.StringBinaryOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#stringStarOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringStarOperatorExpression(HqlParser.StringStarOperatorExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#stringStarOperatorExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringStarOperatorExpression(HqlParser.StringStarOperatorExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#invocationExpression}.
	 * @param ctx the parse tree
	 */
	void enterInvocationExpression(HqlParser.InvocationExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#invocationExpression}.
	 * @param ctx the parse tree
	 */
	void exitInvocationExpression(HqlParser.InvocationExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathExpression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallOrPathExpression(HqlParser.FunctionCallOrPathExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathExpression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallOrPathExpression(HqlParser.FunctionCallOrPathExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathRoot}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallOrPathRoot(HqlParser.FunctionCallOrPathRootContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathRoot}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallOrPathRoot(HqlParser.FunctionCallOrPathRootContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathPathExpression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallOrPathPathExpression(HqlParser.FunctionCallOrPathPathExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathPathExpression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallOrPathPathExpression(HqlParser.FunctionCallOrPathPathExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathOperation}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallOrPathOperation(HqlParser.FunctionCallOrPathOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathOperation}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallOrPathOperation(HqlParser.FunctionCallOrPathOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionalCallOrPathPathOperation}.
	 * @param ctx the parse tree
	 */
	void enterFunctionalCallOrPathPathOperation(HqlParser.FunctionalCallOrPathPathOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionalCallOrPathPathOperation}.
	 * @param ctx the parse tree
	 */
	void exitFunctionalCallOrPathPathOperation(HqlParser.FunctionalCallOrPathPathOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallOrPathElementOperation(HqlParser.FunctionCallOrPathElementOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallOrPathElementOperation(HqlParser.FunctionCallOrPathElementOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#legacyFunctionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
	void enterLegacyFunctionCallOrPathElementOperation(HqlParser.LegacyFunctionCallOrPathElementOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#legacyFunctionCallOrPathElementOperation}.
	 * @param ctx the parse tree
	 */
	void exitLegacyFunctionCallOrPathElementOperation(HqlParser.LegacyFunctionCallOrPathElementOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#toScalarExpression}.
	 * @param ctx the parse tree
	 */
	void enterToScalarExpression(HqlParser.ToScalarExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#toScalarExpression}.
	 * @param ctx the parse tree
	 */
	void exitToScalarExpression(HqlParser.ToScalarExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#toTableExpression}.
	 * @param ctx the parse tree
	 */
	void enterToTableExpression(HqlParser.ToTableExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#toTableExpression}.
	 * @param ctx the parse tree
	 */
	void exitToTableExpression(HqlParser.ToTableExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#noOptimizationParameter}.
	 * @param ctx the parse tree
	 */
	void enterNoOptimizationParameter(HqlParser.NoOptimizationParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#noOptimizationParameter}.
	 * @param ctx the parse tree
	 */
	void exitNoOptimizationParameter(HqlParser.NoOptimizationParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#dotCompositeFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	void enterDotCompositeFunctionCallExpression(HqlParser.DotCompositeFunctionCallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	void exitDotCompositeFunctionCallExpression(HqlParser.DotCompositeFunctionCallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#dotCompositeFunctionCallOperation}.
	 * @param ctx the parse tree
	 */
	void enterDotCompositeFunctionCallOperation(HqlParser.DotCompositeFunctionCallOperationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#dotCompositeFunctionCallOperation}.
	 * @param ctx the parse tree
	 */
	void exitDotCompositeFunctionCallOperation(HqlParser.DotCompositeFunctionCallOperationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#functionCallExpression}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCallExpression(HqlParser.FunctionCallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#functionCallExpression}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCallExpression(HqlParser.FunctionCallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#namedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	void enterNamedFunctionCallExpression(HqlParser.NamedFunctionCallExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#namedFunctionCallExpression}.
	 * @param ctx the parse tree
	 */
	void exitNamedFunctionCallExpression(HqlParser.NamedFunctionCallExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#argumentExpression}.
	 * @param ctx the parse tree
	 */
	void enterArgumentExpression(HqlParser.ArgumentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#argumentExpression}.
	 * @param ctx the parse tree
	 */
	void exitArgumentExpression(HqlParser.ArgumentExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#countExpression}.
	 * @param ctx the parse tree
	 */
	void enterCountExpression(HqlParser.CountExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#countExpression}.
	 * @param ctx the parse tree
	 */
	void exitCountExpression(HqlParser.CountExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#starExpression}.
	 * @param ctx the parse tree
	 */
	void enterStarExpression(HqlParser.StarExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#starExpression}.
	 * @param ctx the parse tree
	 */
	void exitStarExpression(HqlParser.StarExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(HqlParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(HqlParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#nameReferenceWithDataScope}.
	 * @param ctx the parse tree
	 */
	void enterNameReferenceWithDataScope(HqlParser.NameReferenceWithDataScopeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#nameReferenceWithDataScope}.
	 * @param ctx the parse tree
	 */
	void exitNameReferenceWithDataScope(HqlParser.NameReferenceWithDataScopeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#dataScopeClause}.
	 * @param ctx the parse tree
	 */
	void enterDataScopeClause(HqlParser.DataScopeClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#dataScopeClause}.
	 * @param ctx the parse tree
	 */
	void exitDataScopeClause(HqlParser.DataScopeClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parenthesizedExpression}.
	 * @param ctx the parse tree
	 */
	void enterParenthesizedExpression(HqlParser.ParenthesizedExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parenthesizedExpression}.
	 * @param ctx the parse tree
	 */
	void exitParenthesizedExpression(HqlParser.ParenthesizedExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#rangeExpression}.
	 * @param ctx the parse tree
	 */
	void enterRangeExpression(HqlParser.RangeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#rangeExpression}.
	 * @param ctx the parse tree
	 */
	void exitRangeExpression(HqlParser.RangeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEntityExpression(HqlParser.EntityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEntityExpression(HqlParser.EntityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityPathOrElementExpression}.
	 * @param ctx the parse tree
	 */
	void enterEntityPathOrElementExpression(HqlParser.EntityPathOrElementExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityPathOrElementExpression}.
	 * @param ctx the parse tree
	 */
	void exitEntityPathOrElementExpression(HqlParser.EntityPathOrElementExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityPathOrElementOperator}.
	 * @param ctx the parse tree
	 */
	void enterEntityPathOrElementOperator(HqlParser.EntityPathOrElementOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityPathOrElementOperator}.
	 * @param ctx the parse tree
	 */
	void exitEntityPathOrElementOperator(HqlParser.EntityPathOrElementOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityPathOperator}.
	 * @param ctx the parse tree
	 */
	void enterEntityPathOperator(HqlParser.EntityPathOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityPathOperator}.
	 * @param ctx the parse tree
	 */
	void exitEntityPathOperator(HqlParser.EntityPathOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityElementOperator}.
	 * @param ctx the parse tree
	 */
	void enterEntityElementOperator(HqlParser.EntityElementOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityElementOperator}.
	 * @param ctx the parse tree
	 */
	void exitEntityElementOperator(HqlParser.EntityElementOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#legacyEntityPathElementOperator}.
	 * @param ctx the parse tree
	 */
	void enterLegacyEntityPathElementOperator(HqlParser.LegacyEntityPathElementOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#legacyEntityPathElementOperator}.
	 * @param ctx the parse tree
	 */
	void exitLegacyEntityPathElementOperator(HqlParser.LegacyEntityPathElementOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityName}.
	 * @param ctx the parse tree
	 */
	void enterEntityName(HqlParser.EntityNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityName}.
	 * @param ctx the parse tree
	 */
	void exitEntityName(HqlParser.EntityNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#entityNameReference}.
	 * @param ctx the parse tree
	 */
	void enterEntityNameReference(HqlParser.EntityNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#entityNameReference}.
	 * @param ctx the parse tree
	 */
	void exitEntityNameReference(HqlParser.EntityNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#atSignName}.
	 * @param ctx the parse tree
	 */
	void enterAtSignName(HqlParser.AtSignNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#atSignName}.
	 * @param ctx the parse tree
	 */
	void exitAtSignName(HqlParser.AtSignNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#extendedPathName}.
	 * @param ctx the parse tree
	 */
	void enterExtendedPathName(HqlParser.ExtendedPathNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#extendedPathName}.
	 * @param ctx the parse tree
	 */
	void exitExtendedPathName(HqlParser.ExtendedPathNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedEntityExpression}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedEntityExpression(HqlParser.WildcardedEntityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedEntityExpression}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedEntityExpression(HqlParser.WildcardedEntityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedPathExpression}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedPathExpression(HqlParser.WildcardedPathExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedPathExpression}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedPathExpression(HqlParser.WildcardedPathExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedPathName}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedPathName(HqlParser.WildcardedPathNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedPathName}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedPathName(HqlParser.WildcardedPathNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#contextualDataTableExpression}.
	 * @param ctx the parse tree
	 */
	void enterContextualDataTableExpression(HqlParser.ContextualDataTableExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#contextualDataTableExpression}.
	 * @param ctx the parse tree
	 */
	void exitContextualDataTableExpression(HqlParser.ContextualDataTableExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#dataTableExpression}.
	 * @param ctx the parse tree
	 */
	void enterDataTableExpression(HqlParser.DataTableExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#dataTableExpression}.
	 * @param ctx the parse tree
	 */
	void exitDataTableExpression(HqlParser.DataTableExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#rowSchema}.
	 * @param ctx the parse tree
	 */
	void enterRowSchema(HqlParser.RowSchemaContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#rowSchema}.
	 * @param ctx the parse tree
	 */
	void exitRowSchema(HqlParser.RowSchemaContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#rowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
	void enterRowSchemaColumnDeclaration(HqlParser.RowSchemaColumnDeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#rowSchemaColumnDeclaration}.
	 * @param ctx the parse tree
	 */
	void exitRowSchemaColumnDeclaration(HqlParser.RowSchemaColumnDeclarationContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#externalDataExpression}.
	 * @param ctx the parse tree
	 */
	void enterExternalDataExpression(HqlParser.ExternalDataExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#externalDataExpression}.
	 * @param ctx the parse tree
	 */
	void exitExternalDataExpression(HqlParser.ExternalDataExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#externalDataWithClause}.
	 * @param ctx the parse tree
	 */
	void enterExternalDataWithClause(HqlParser.ExternalDataWithClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#externalDataWithClause}.
	 * @param ctx the parse tree
	 */
	void exitExternalDataWithClause(HqlParser.ExternalDataWithClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#externalDataWithClauseProperty}.
	 * @param ctx the parse tree
	 */
	void enterExternalDataWithClauseProperty(HqlParser.ExternalDataWithClausePropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#externalDataWithClauseProperty}.
	 * @param ctx the parse tree
	 */
	void exitExternalDataWithClauseProperty(HqlParser.ExternalDataWithClausePropertyContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#materializedViewCombineExpression}.
	 * @param ctx the parse tree
	 */
	void enterMaterializedViewCombineExpression(HqlParser.MaterializedViewCombineExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#materializedViewCombineExpression}.
	 * @param ctx the parse tree
	 */
	void exitMaterializedViewCombineExpression(HqlParser.MaterializedViewCombineExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#materializeViewCombineBaseClause}.
	 * @param ctx the parse tree
	 */
	void enterMaterializeViewCombineBaseClause(HqlParser.MaterializeViewCombineBaseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#materializeViewCombineBaseClause}.
	 * @param ctx the parse tree
	 */
	void exitMaterializeViewCombineBaseClause(HqlParser.MaterializeViewCombineBaseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#materializedViewCombineDeltaClause}.
	 * @param ctx the parse tree
	 */
	void enterMaterializedViewCombineDeltaClause(HqlParser.MaterializedViewCombineDeltaClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#materializedViewCombineDeltaClause}.
	 * @param ctx the parse tree
	 */
	void exitMaterializedViewCombineDeltaClause(HqlParser.MaterializedViewCombineDeltaClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#materializedViewCombineAggregationsClause}.
	 * @param ctx the parse tree
	 */
	void enterMaterializedViewCombineAggregationsClause(HqlParser.MaterializedViewCombineAggregationsClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#materializedViewCombineAggregationsClause}.
	 * @param ctx the parse tree
	 */
	void exitMaterializedViewCombineAggregationsClause(HqlParser.MaterializedViewCombineAggregationsClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#scalarType}.
	 * @param ctx the parse tree
	 */
	void enterScalarType(HqlParser.ScalarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#scalarType}.
	 * @param ctx the parse tree
	 */
	void exitScalarType(HqlParser.ScalarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#extendedScalarType}.
	 * @param ctx the parse tree
	 */
	void enterExtendedScalarType(HqlParser.ExtendedScalarTypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#extendedScalarType}.
	 * @param ctx the parse tree
	 */
	void exitExtendedScalarType(HqlParser.ExtendedScalarTypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#parameterName}.
	 * @param ctx the parse tree
	 */
	void enterParameterName(HqlParser.ParameterNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#parameterName}.
	 * @param ctx the parse tree
	 */
	void exitParameterName(HqlParser.ParameterNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#simpleNameReference}.
	 * @param ctx the parse tree
	 */
	void enterSimpleNameReference(HqlParser.SimpleNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#simpleNameReference}.
	 * @param ctx the parse tree
	 */
	void exitSimpleNameReference(HqlParser.SimpleNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#extendedNameReference}.
	 * @param ctx the parse tree
	 */
	void enterExtendedNameReference(HqlParser.ExtendedNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#extendedNameReference}.
	 * @param ctx the parse tree
	 */
	void exitExtendedNameReference(HqlParser.ExtendedNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedNameReference}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedNameReference(HqlParser.WildcardedNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedNameReference}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedNameReference(HqlParser.WildcardedNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#simpleOrWildcardedNameReference}.
	 * @param ctx the parse tree
	 */
	void enterSimpleOrWildcardedNameReference(HqlParser.SimpleOrWildcardedNameReferenceContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#simpleOrWildcardedNameReference}.
	 * @param ctx the parse tree
	 */
	void exitSimpleOrWildcardedNameReference(HqlParser.SimpleOrWildcardedNameReferenceContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#identifierName}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierName(HqlParser.IdentifierNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#identifierName}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierName(HqlParser.IdentifierNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#keywordName}.
	 * @param ctx the parse tree
	 */
	void enterKeywordName(HqlParser.KeywordNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#keywordName}.
	 * @param ctx the parse tree
	 */
	void exitKeywordName(HqlParser.KeywordNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#extendedKeywordName}.
	 * @param ctx the parse tree
	 */
	void enterExtendedKeywordName(HqlParser.ExtendedKeywordNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#extendedKeywordName}.
	 * @param ctx the parse tree
	 */
	void exitExtendedKeywordName(HqlParser.ExtendedKeywordNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#escapedName}.
	 * @param ctx the parse tree
	 */
	void enterEscapedName(HqlParser.EscapedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#escapedName}.
	 * @param ctx the parse tree
	 */
	void exitEscapedName(HqlParser.EscapedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#identifierOrKeywordName}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierOrKeywordName(HqlParser.IdentifierOrKeywordNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#identifierOrKeywordName}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierOrKeywordName(HqlParser.IdentifierOrKeywordNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#identifierOrKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierOrKeywordOrEscapedName(HqlParser.IdentifierOrKeywordOrEscapedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#identifierOrKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierOrKeywordOrEscapedName(HqlParser.IdentifierOrKeywordOrEscapedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierOrExtendedKeywordOrEscapedName(HqlParser.IdentifierOrExtendedKeywordOrEscapedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordOrEscapedName}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierOrExtendedKeywordOrEscapedName(HqlParser.IdentifierOrExtendedKeywordOrEscapedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordName}.
	 * @param ctx the parse tree
	 */
	void enterIdentifierOrExtendedKeywordName(HqlParser.IdentifierOrExtendedKeywordNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#identifierOrExtendedKeywordName}.
	 * @param ctx the parse tree
	 */
	void exitIdentifierOrExtendedKeywordName(HqlParser.IdentifierOrExtendedKeywordNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedName}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedName(HqlParser.WildcardedNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedName}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedName(HqlParser.WildcardedNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedNamePrefix}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedNamePrefix(HqlParser.WildcardedNamePrefixContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedNamePrefix}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedNamePrefix(HqlParser.WildcardedNamePrefixContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#wildcardedNameSegment}.
	 * @param ctx the parse tree
	 */
	void enterWildcardedNameSegment(HqlParser.WildcardedNameSegmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#wildcardedNameSegment}.
	 * @param ctx the parse tree
	 */
	void exitWildcardedNameSegment(HqlParser.WildcardedNameSegmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#literalExpression}.
	 * @param ctx the parse tree
	 */
	void enterLiteralExpression(HqlParser.LiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#literalExpression}.
	 * @param ctx the parse tree
	 */
	void exitLiteralExpression(HqlParser.LiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#unsignedLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnsignedLiteralExpression(HqlParser.UnsignedLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#unsignedLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnsignedLiteralExpression(HqlParser.UnsignedLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#numberLikeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterNumberLikeLiteralExpression(HqlParser.NumberLikeLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#numberLikeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitNumberLikeLiteralExpression(HqlParser.NumberLikeLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#numericLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterNumericLiteralExpression(HqlParser.NumericLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#numericLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitNumericLiteralExpression(HqlParser.NumericLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#signedLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterSignedLiteralExpression(HqlParser.SignedLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#signedLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitSignedLiteralExpression(HqlParser.SignedLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#longLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterLongLiteralExpression(HqlParser.LongLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#longLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitLongLiteralExpression(HqlParser.LongLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#intLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterIntLiteralExpression(HqlParser.IntLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#intLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitIntLiteralExpression(HqlParser.IntLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#realLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterRealLiteralExpression(HqlParser.RealLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#realLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitRealLiteralExpression(HqlParser.RealLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#decimalLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterDecimalLiteralExpression(HqlParser.DecimalLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#decimalLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitDecimalLiteralExpression(HqlParser.DecimalLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#dateTimeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterDateTimeLiteralExpression(HqlParser.DateTimeLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#dateTimeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitDateTimeLiteralExpression(HqlParser.DateTimeLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#timeSpanLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterTimeSpanLiteralExpression(HqlParser.TimeSpanLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#timeSpanLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitTimeSpanLiteralExpression(HqlParser.TimeSpanLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#booleanLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterBooleanLiteralExpression(HqlParser.BooleanLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#booleanLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitBooleanLiteralExpression(HqlParser.BooleanLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#guidLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterGuidLiteralExpression(HqlParser.GuidLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#guidLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitGuidLiteralExpression(HqlParser.GuidLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#typeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterTypeLiteralExpression(HqlParser.TypeLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#typeLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitTypeLiteralExpression(HqlParser.TypeLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#signedLongLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterSignedLongLiteralExpression(HqlParser.SignedLongLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#signedLongLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitSignedLongLiteralExpression(HqlParser.SignedLongLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#signedRealLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterSignedRealLiteralExpression(HqlParser.SignedRealLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#signedRealLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitSignedRealLiteralExpression(HqlParser.SignedRealLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#stringLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterStringLiteralExpression(HqlParser.StringLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#stringLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitStringLiteralExpression(HqlParser.StringLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#dynamicLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void enterDynamicLiteralExpression(HqlParser.DynamicLiteralExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#dynamicLiteralExpression}.
	 * @param ctx the parse tree
	 */
	void exitDynamicLiteralExpression(HqlParser.DynamicLiteralExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonValue}.
	 * @param ctx the parse tree
	 */
	void enterJsonValue(HqlParser.JsonValueContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonValue}.
	 * @param ctx the parse tree
	 */
	void exitJsonValue(HqlParser.JsonValueContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonObject}.
	 * @param ctx the parse tree
	 */
	void enterJsonObject(HqlParser.JsonObjectContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonObject}.
	 * @param ctx the parse tree
	 */
	void exitJsonObject(HqlParser.JsonObjectContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonPair}.
	 * @param ctx the parse tree
	 */
	void enterJsonPair(HqlParser.JsonPairContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonPair}.
	 * @param ctx the parse tree
	 */
	void exitJsonPair(HqlParser.JsonPairContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonArray}.
	 * @param ctx the parse tree
	 */
	void enterJsonArray(HqlParser.JsonArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonArray}.
	 * @param ctx the parse tree
	 */
	void exitJsonArray(HqlParser.JsonArrayContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonBoolean}.
	 * @param ctx the parse tree
	 */
	void enterJsonBoolean(HqlParser.JsonBooleanContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonBoolean}.
	 * @param ctx the parse tree
	 */
	void exitJsonBoolean(HqlParser.JsonBooleanContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonDateTime}.
	 * @param ctx the parse tree
	 */
	void enterJsonDateTime(HqlParser.JsonDateTimeContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonDateTime}.
	 * @param ctx the parse tree
	 */
	void exitJsonDateTime(HqlParser.JsonDateTimeContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonGuid}.
	 * @param ctx the parse tree
	 */
	void enterJsonGuid(HqlParser.JsonGuidContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonGuid}.
	 * @param ctx the parse tree
	 */
	void exitJsonGuid(HqlParser.JsonGuidContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonNull}.
	 * @param ctx the parse tree
	 */
	void enterJsonNull(HqlParser.JsonNullContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonNull}.
	 * @param ctx the parse tree
	 */
	void exitJsonNull(HqlParser.JsonNullContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonString}.
	 * @param ctx the parse tree
	 */
	void enterJsonString(HqlParser.JsonStringContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonString}.
	 * @param ctx the parse tree
	 */
	void exitJsonString(HqlParser.JsonStringContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonTimeSpan}.
	 * @param ctx the parse tree
	 */
	void enterJsonTimeSpan(HqlParser.JsonTimeSpanContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonTimeSpan}.
	 * @param ctx the parse tree
	 */
	void exitJsonTimeSpan(HqlParser.JsonTimeSpanContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonLong}.
	 * @param ctx the parse tree
	 */
	void enterJsonLong(HqlParser.JsonLongContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonLong}.
	 * @param ctx the parse tree
	 */
	void exitJsonLong(HqlParser.JsonLongContext ctx);
	/**
	 * Enter a parse tree produced by {@link HqlParser#jsonReal}.
	 * @param ctx the parse tree
	 */
	void enterJsonReal(HqlParser.JsonRealContext ctx);
	/**
	 * Exit a parse tree produced by {@link HqlParser#jsonReal}.
	 * @param ctx the parse tree
	 */
	void exitJsonReal(HqlParser.JsonRealContext ctx);
}