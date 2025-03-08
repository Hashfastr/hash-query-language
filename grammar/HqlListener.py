# Generated from Hql.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HqlParser import HqlParser
else:
    from HqlParser import HqlParser

# This class defines a complete listener for a parse tree produced by HqlParser.
class HqlListener(ParseTreeListener):

    # Enter a parse tree produced by HqlParser#top.
    def enterTop(self, ctx:HqlParser.TopContext):
        pass

    # Exit a parse tree produced by HqlParser#top.
    def exitTop(self, ctx:HqlParser.TopContext):
        pass


    # Enter a parse tree produced by HqlParser#query.
    def enterQuery(self, ctx:HqlParser.QueryContext):
        pass

    # Exit a parse tree produced by HqlParser#query.
    def exitQuery(self, ctx:HqlParser.QueryContext):
        pass


    # Enter a parse tree produced by HqlParser#statement.
    def enterStatement(self, ctx:HqlParser.StatementContext):
        pass

    # Exit a parse tree produced by HqlParser#statement.
    def exitStatement(self, ctx:HqlParser.StatementContext):
        pass


    # Enter a parse tree produced by HqlParser#aliasDatabaseStatement.
    def enterAliasDatabaseStatement(self, ctx:HqlParser.AliasDatabaseStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#aliasDatabaseStatement.
    def exitAliasDatabaseStatement(self, ctx:HqlParser.AliasDatabaseStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#letStatement.
    def enterLetStatement(self, ctx:HqlParser.LetStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#letStatement.
    def exitLetStatement(self, ctx:HqlParser.LetStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#letVariableDeclaration.
    def enterLetVariableDeclaration(self, ctx:HqlParser.LetVariableDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#letVariableDeclaration.
    def exitLetVariableDeclaration(self, ctx:HqlParser.LetVariableDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#letFunctionDeclaration.
    def enterLetFunctionDeclaration(self, ctx:HqlParser.LetFunctionDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#letFunctionDeclaration.
    def exitLetFunctionDeclaration(self, ctx:HqlParser.LetFunctionDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#letViewDeclaration.
    def enterLetViewDeclaration(self, ctx:HqlParser.LetViewDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#letViewDeclaration.
    def exitLetViewDeclaration(self, ctx:HqlParser.LetViewDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#letViewParameterList.
    def enterLetViewParameterList(self, ctx:HqlParser.LetViewParameterListContext):
        pass

    # Exit a parse tree produced by HqlParser#letViewParameterList.
    def exitLetViewParameterList(self, ctx:HqlParser.LetViewParameterListContext):
        pass


    # Enter a parse tree produced by HqlParser#letMaterializeDeclaration.
    def enterLetMaterializeDeclaration(self, ctx:HqlParser.LetMaterializeDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#letMaterializeDeclaration.
    def exitLetMaterializeDeclaration(self, ctx:HqlParser.LetMaterializeDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#letEntityGroupDeclaration.
    def enterLetEntityGroupDeclaration(self, ctx:HqlParser.LetEntityGroupDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#letEntityGroupDeclaration.
    def exitLetEntityGroupDeclaration(self, ctx:HqlParser.LetEntityGroupDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#letFunctionParameterList.
    def enterLetFunctionParameterList(self, ctx:HqlParser.LetFunctionParameterListContext):
        pass

    # Exit a parse tree produced by HqlParser#letFunctionParameterList.
    def exitLetFunctionParameterList(self, ctx:HqlParser.LetFunctionParameterListContext):
        pass


    # Enter a parse tree produced by HqlParser#scalarParameter.
    def enterScalarParameter(self, ctx:HqlParser.ScalarParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#scalarParameter.
    def exitScalarParameter(self, ctx:HqlParser.ScalarParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#scalarParameterDefault.
    def enterScalarParameterDefault(self, ctx:HqlParser.ScalarParameterDefaultContext):
        pass

    # Exit a parse tree produced by HqlParser#scalarParameterDefault.
    def exitScalarParameterDefault(self, ctx:HqlParser.ScalarParameterDefaultContext):
        pass


    # Enter a parse tree produced by HqlParser#tabularParameter.
    def enterTabularParameter(self, ctx:HqlParser.TabularParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#tabularParameter.
    def exitTabularParameter(self, ctx:HqlParser.TabularParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#tabularParameterOpenSchema.
    def enterTabularParameterOpenSchema(self, ctx:HqlParser.TabularParameterOpenSchemaContext):
        pass

    # Exit a parse tree produced by HqlParser#tabularParameterOpenSchema.
    def exitTabularParameterOpenSchema(self, ctx:HqlParser.TabularParameterOpenSchemaContext):
        pass


    # Enter a parse tree produced by HqlParser#tabularParameterRowSchema.
    def enterTabularParameterRowSchema(self, ctx:HqlParser.TabularParameterRowSchemaContext):
        pass

    # Exit a parse tree produced by HqlParser#tabularParameterRowSchema.
    def exitTabularParameterRowSchema(self, ctx:HqlParser.TabularParameterRowSchemaContext):
        pass


    # Enter a parse tree produced by HqlParser#tabularParameterRowSchemaColumnDeclaration.
    def enterTabularParameterRowSchemaColumnDeclaration(self, ctx:HqlParser.TabularParameterRowSchemaColumnDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#tabularParameterRowSchemaColumnDeclaration.
    def exitTabularParameterRowSchemaColumnDeclaration(self, ctx:HqlParser.TabularParameterRowSchemaColumnDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#letFunctionBody.
    def enterLetFunctionBody(self, ctx:HqlParser.LetFunctionBodyContext):
        pass

    # Exit a parse tree produced by HqlParser#letFunctionBody.
    def exitLetFunctionBody(self, ctx:HqlParser.LetFunctionBodyContext):
        pass


    # Enter a parse tree produced by HqlParser#letFunctionBodyStatement.
    def enterLetFunctionBodyStatement(self, ctx:HqlParser.LetFunctionBodyStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#letFunctionBodyStatement.
    def exitLetFunctionBodyStatement(self, ctx:HqlParser.LetFunctionBodyStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternStatement.
    def enterDeclarePatternStatement(self, ctx:HqlParser.DeclarePatternStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternStatement.
    def exitDeclarePatternStatement(self, ctx:HqlParser.DeclarePatternStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternDefinition.
    def enterDeclarePatternDefinition(self, ctx:HqlParser.DeclarePatternDefinitionContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternDefinition.
    def exitDeclarePatternDefinition(self, ctx:HqlParser.DeclarePatternDefinitionContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternParameterList.
    def enterDeclarePatternParameterList(self, ctx:HqlParser.DeclarePatternParameterListContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternParameterList.
    def exitDeclarePatternParameterList(self, ctx:HqlParser.DeclarePatternParameterListContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternParameter.
    def enterDeclarePatternParameter(self, ctx:HqlParser.DeclarePatternParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternParameter.
    def exitDeclarePatternParameter(self, ctx:HqlParser.DeclarePatternParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternPathParameter.
    def enterDeclarePatternPathParameter(self, ctx:HqlParser.DeclarePatternPathParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternPathParameter.
    def exitDeclarePatternPathParameter(self, ctx:HqlParser.DeclarePatternPathParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternRule.
    def enterDeclarePatternRule(self, ctx:HqlParser.DeclarePatternRuleContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternRule.
    def exitDeclarePatternRule(self, ctx:HqlParser.DeclarePatternRuleContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternRuleArgumentList.
    def enterDeclarePatternRuleArgumentList(self, ctx:HqlParser.DeclarePatternRuleArgumentListContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternRuleArgumentList.
    def exitDeclarePatternRuleArgumentList(self, ctx:HqlParser.DeclarePatternRuleArgumentListContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternRulePathArgument.
    def enterDeclarePatternRulePathArgument(self, ctx:HqlParser.DeclarePatternRulePathArgumentContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternRulePathArgument.
    def exitDeclarePatternRulePathArgument(self, ctx:HqlParser.DeclarePatternRulePathArgumentContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternRuleArgument.
    def enterDeclarePatternRuleArgument(self, ctx:HqlParser.DeclarePatternRuleArgumentContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternRuleArgument.
    def exitDeclarePatternRuleArgument(self, ctx:HqlParser.DeclarePatternRuleArgumentContext):
        pass


    # Enter a parse tree produced by HqlParser#declarePatternBody.
    def enterDeclarePatternBody(self, ctx:HqlParser.DeclarePatternBodyContext):
        pass

    # Exit a parse tree produced by HqlParser#declarePatternBody.
    def exitDeclarePatternBody(self, ctx:HqlParser.DeclarePatternBodyContext):
        pass


    # Enter a parse tree produced by HqlParser#restrictAccessStatement.
    def enterRestrictAccessStatement(self, ctx:HqlParser.RestrictAccessStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#restrictAccessStatement.
    def exitRestrictAccessStatement(self, ctx:HqlParser.RestrictAccessStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#restrictAccessStatementEntity.
    def enterRestrictAccessStatementEntity(self, ctx:HqlParser.RestrictAccessStatementEntityContext):
        pass

    # Exit a parse tree produced by HqlParser#restrictAccessStatementEntity.
    def exitRestrictAccessStatementEntity(self, ctx:HqlParser.RestrictAccessStatementEntityContext):
        pass


    # Enter a parse tree produced by HqlParser#setStatement.
    def enterSetStatement(self, ctx:HqlParser.SetStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#setStatement.
    def exitSetStatement(self, ctx:HqlParser.SetStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#setStatementOptionValue.
    def enterSetStatementOptionValue(self, ctx:HqlParser.SetStatementOptionValueContext):
        pass

    # Exit a parse tree produced by HqlParser#setStatementOptionValue.
    def exitSetStatementOptionValue(self, ctx:HqlParser.SetStatementOptionValueContext):
        pass


    # Enter a parse tree produced by HqlParser#declareQueryParametersStatement.
    def enterDeclareQueryParametersStatement(self, ctx:HqlParser.DeclareQueryParametersStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#declareQueryParametersStatement.
    def exitDeclareQueryParametersStatement(self, ctx:HqlParser.DeclareQueryParametersStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#declareQueryParametersStatementParameter.
    def enterDeclareQueryParametersStatementParameter(self, ctx:HqlParser.DeclareQueryParametersStatementParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#declareQueryParametersStatementParameter.
    def exitDeclareQueryParametersStatementParameter(self, ctx:HqlParser.DeclareQueryParametersStatementParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#queryStatement.
    def enterQueryStatement(self, ctx:HqlParser.QueryStatementContext):
        pass

    # Exit a parse tree produced by HqlParser#queryStatement.
    def exitQueryStatement(self, ctx:HqlParser.QueryStatementContext):
        pass


    # Enter a parse tree produced by HqlParser#expression.
    def enterExpression(self, ctx:HqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#expression.
    def exitExpression(self, ctx:HqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#pipeExpression.
    def enterPipeExpression(self, ctx:HqlParser.PipeExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#pipeExpression.
    def exitPipeExpression(self, ctx:HqlParser.PipeExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#pipedOperator.
    def enterPipedOperator(self, ctx:HqlParser.PipedOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#pipedOperator.
    def exitPipedOperator(self, ctx:HqlParser.PipedOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#pipeSubExpression.
    def enterPipeSubExpression(self, ctx:HqlParser.PipeSubExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#pipeSubExpression.
    def exitPipeSubExpression(self, ctx:HqlParser.PipeSubExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#beforePipeExpression.
    def enterBeforePipeExpression(self, ctx:HqlParser.BeforePipeExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#beforePipeExpression.
    def exitBeforePipeExpression(self, ctx:HqlParser.BeforePipeExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#afterPipeOperator.
    def enterAfterPipeOperator(self, ctx:HqlParser.AfterPipeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#afterPipeOperator.
    def exitAfterPipeOperator(self, ctx:HqlParser.AfterPipeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#beforeOrAfterPipeOperator.
    def enterBeforeOrAfterPipeOperator(self, ctx:HqlParser.BeforeOrAfterPipeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#beforeOrAfterPipeOperator.
    def exitBeforeOrAfterPipeOperator(self, ctx:HqlParser.BeforeOrAfterPipeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#forkPipeOperator.
    def enterForkPipeOperator(self, ctx:HqlParser.ForkPipeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#forkPipeOperator.
    def exitForkPipeOperator(self, ctx:HqlParser.ForkPipeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#asOperator.
    def enterAsOperator(self, ctx:HqlParser.AsOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#asOperator.
    def exitAsOperator(self, ctx:HqlParser.AsOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#assertSchemaOperator.
    def enterAssertSchemaOperator(self, ctx:HqlParser.AssertSchemaOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#assertSchemaOperator.
    def exitAssertSchemaOperator(self, ctx:HqlParser.AssertSchemaOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#consumeOperator.
    def enterConsumeOperator(self, ctx:HqlParser.ConsumeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#consumeOperator.
    def exitConsumeOperator(self, ctx:HqlParser.ConsumeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#countOperator.
    def enterCountOperator(self, ctx:HqlParser.CountOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#countOperator.
    def exitCountOperator(self, ctx:HqlParser.CountOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#countOperatorAsClause.
    def enterCountOperatorAsClause(self, ctx:HqlParser.CountOperatorAsClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#countOperatorAsClause.
    def exitCountOperatorAsClause(self, ctx:HqlParser.CountOperatorAsClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#distinctOperator.
    def enterDistinctOperator(self, ctx:HqlParser.DistinctOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#distinctOperator.
    def exitDistinctOperator(self, ctx:HqlParser.DistinctOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#distinctOperatorStarTarget.
    def enterDistinctOperatorStarTarget(self, ctx:HqlParser.DistinctOperatorStarTargetContext):
        pass

    # Exit a parse tree produced by HqlParser#distinctOperatorStarTarget.
    def exitDistinctOperatorStarTarget(self, ctx:HqlParser.DistinctOperatorStarTargetContext):
        pass


    # Enter a parse tree produced by HqlParser#distinctOperatorColumnListTarget.
    def enterDistinctOperatorColumnListTarget(self, ctx:HqlParser.DistinctOperatorColumnListTargetContext):
        pass

    # Exit a parse tree produced by HqlParser#distinctOperatorColumnListTarget.
    def exitDistinctOperatorColumnListTarget(self, ctx:HqlParser.DistinctOperatorColumnListTargetContext):
        pass


    # Enter a parse tree produced by HqlParser#evaluateOperator.
    def enterEvaluateOperator(self, ctx:HqlParser.EvaluateOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#evaluateOperator.
    def exitEvaluateOperator(self, ctx:HqlParser.EvaluateOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#evaluateOperatorSchemaClause.
    def enterEvaluateOperatorSchemaClause(self, ctx:HqlParser.EvaluateOperatorSchemaClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#evaluateOperatorSchemaClause.
    def exitEvaluateOperatorSchemaClause(self, ctx:HqlParser.EvaluateOperatorSchemaClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#extendOperator.
    def enterExtendOperator(self, ctx:HqlParser.ExtendOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#extendOperator.
    def exitExtendOperator(self, ctx:HqlParser.ExtendOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#executeAndCacheOperator.
    def enterExecuteAndCacheOperator(self, ctx:HqlParser.ExecuteAndCacheOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#executeAndCacheOperator.
    def exitExecuteAndCacheOperator(self, ctx:HqlParser.ExecuteAndCacheOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#facetByOperator.
    def enterFacetByOperator(self, ctx:HqlParser.FacetByOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#facetByOperator.
    def exitFacetByOperator(self, ctx:HqlParser.FacetByOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#facetByOperatorWithOperatorClause.
    def enterFacetByOperatorWithOperatorClause(self, ctx:HqlParser.FacetByOperatorWithOperatorClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#facetByOperatorWithOperatorClause.
    def exitFacetByOperatorWithOperatorClause(self, ctx:HqlParser.FacetByOperatorWithOperatorClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#facetByOperatorWithExpressionClause.
    def enterFacetByOperatorWithExpressionClause(self, ctx:HqlParser.FacetByOperatorWithExpressionClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#facetByOperatorWithExpressionClause.
    def exitFacetByOperatorWithExpressionClause(self, ctx:HqlParser.FacetByOperatorWithExpressionClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperator.
    def enterFindOperator(self, ctx:HqlParser.FindOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperator.
    def exitFindOperator(self, ctx:HqlParser.FindOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorParametersWhereClause.
    def enterFindOperatorParametersWhereClause(self, ctx:HqlParser.FindOperatorParametersWhereClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorParametersWhereClause.
    def exitFindOperatorParametersWhereClause(self, ctx:HqlParser.FindOperatorParametersWhereClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorInClause.
    def enterFindOperatorInClause(self, ctx:HqlParser.FindOperatorInClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorInClause.
    def exitFindOperatorInClause(self, ctx:HqlParser.FindOperatorInClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorProjectClause.
    def enterFindOperatorProjectClause(self, ctx:HqlParser.FindOperatorProjectClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorProjectClause.
    def exitFindOperatorProjectClause(self, ctx:HqlParser.FindOperatorProjectClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorProjectExpression.
    def enterFindOperatorProjectExpression(self, ctx:HqlParser.FindOperatorProjectExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorProjectExpression.
    def exitFindOperatorProjectExpression(self, ctx:HqlParser.FindOperatorProjectExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorColumnExpression.
    def enterFindOperatorColumnExpression(self, ctx:HqlParser.FindOperatorColumnExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorColumnExpression.
    def exitFindOperatorColumnExpression(self, ctx:HqlParser.FindOperatorColumnExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorOptionalColumnType.
    def enterFindOperatorOptionalColumnType(self, ctx:HqlParser.FindOperatorOptionalColumnTypeContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorOptionalColumnType.
    def exitFindOperatorOptionalColumnType(self, ctx:HqlParser.FindOperatorOptionalColumnTypeContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorPackExpression.
    def enterFindOperatorPackExpression(self, ctx:HqlParser.FindOperatorPackExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorPackExpression.
    def exitFindOperatorPackExpression(self, ctx:HqlParser.FindOperatorPackExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorProjectSmartClause.
    def enterFindOperatorProjectSmartClause(self, ctx:HqlParser.FindOperatorProjectSmartClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorProjectSmartClause.
    def exitFindOperatorProjectSmartClause(self, ctx:HqlParser.FindOperatorProjectSmartClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorProjectAwayClause.
    def enterFindOperatorProjectAwayClause(self, ctx:HqlParser.FindOperatorProjectAwayClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorProjectAwayClause.
    def exitFindOperatorProjectAwayClause(self, ctx:HqlParser.FindOperatorProjectAwayClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorProjectAwayStar.
    def enterFindOperatorProjectAwayStar(self, ctx:HqlParser.FindOperatorProjectAwayStarContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorProjectAwayStar.
    def exitFindOperatorProjectAwayStar(self, ctx:HqlParser.FindOperatorProjectAwayStarContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorProjectAwayColumnList.
    def enterFindOperatorProjectAwayColumnList(self, ctx:HqlParser.FindOperatorProjectAwayColumnListContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorProjectAwayColumnList.
    def exitFindOperatorProjectAwayColumnList(self, ctx:HqlParser.FindOperatorProjectAwayColumnListContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorSource.
    def enterFindOperatorSource(self, ctx:HqlParser.FindOperatorSourceContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorSource.
    def exitFindOperatorSource(self, ctx:HqlParser.FindOperatorSourceContext):
        pass


    # Enter a parse tree produced by HqlParser#findOperatorSourceEntityExpression.
    def enterFindOperatorSourceEntityExpression(self, ctx:HqlParser.FindOperatorSourceEntityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#findOperatorSourceEntityExpression.
    def exitFindOperatorSourceEntityExpression(self, ctx:HqlParser.FindOperatorSourceEntityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#forkOperator.
    def enterForkOperator(self, ctx:HqlParser.ForkOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#forkOperator.
    def exitForkOperator(self, ctx:HqlParser.ForkOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#forkOperatorFork.
    def enterForkOperatorFork(self, ctx:HqlParser.ForkOperatorForkContext):
        pass

    # Exit a parse tree produced by HqlParser#forkOperatorFork.
    def exitForkOperatorFork(self, ctx:HqlParser.ForkOperatorForkContext):
        pass


    # Enter a parse tree produced by HqlParser#forkOperatorExpressionName.
    def enterForkOperatorExpressionName(self, ctx:HqlParser.ForkOperatorExpressionNameContext):
        pass

    # Exit a parse tree produced by HqlParser#forkOperatorExpressionName.
    def exitForkOperatorExpressionName(self, ctx:HqlParser.ForkOperatorExpressionNameContext):
        pass


    # Enter a parse tree produced by HqlParser#forkOperatorExpression.
    def enterForkOperatorExpression(self, ctx:HqlParser.ForkOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#forkOperatorExpression.
    def exitForkOperatorExpression(self, ctx:HqlParser.ForkOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#forkOperatorPipedOperator.
    def enterForkOperatorPipedOperator(self, ctx:HqlParser.ForkOperatorPipedOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#forkOperatorPipedOperator.
    def exitForkOperatorPipedOperator(self, ctx:HqlParser.ForkOperatorPipedOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#getSchemaOperator.
    def enterGetSchemaOperator(self, ctx:HqlParser.GetSchemaOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#getSchemaOperator.
    def exitGetSchemaOperator(self, ctx:HqlParser.GetSchemaOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMarkComponentsOperator.
    def enterGraphMarkComponentsOperator(self, ctx:HqlParser.GraphMarkComponentsOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMarkComponentsOperator.
    def exitGraphMarkComponentsOperator(self, ctx:HqlParser.GraphMarkComponentsOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchOperator.
    def enterGraphMatchOperator(self, ctx:HqlParser.GraphMatchOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchOperator.
    def exitGraphMatchOperator(self, ctx:HqlParser.GraphMatchOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchPattern.
    def enterGraphMatchPattern(self, ctx:HqlParser.GraphMatchPatternContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchPattern.
    def exitGraphMatchPattern(self, ctx:HqlParser.GraphMatchPatternContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchPatternNode.
    def enterGraphMatchPatternNode(self, ctx:HqlParser.GraphMatchPatternNodeContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchPatternNode.
    def exitGraphMatchPatternNode(self, ctx:HqlParser.GraphMatchPatternNodeContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchPatternUnnamedEdge.
    def enterGraphMatchPatternUnnamedEdge(self, ctx:HqlParser.GraphMatchPatternUnnamedEdgeContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchPatternUnnamedEdge.
    def exitGraphMatchPatternUnnamedEdge(self, ctx:HqlParser.GraphMatchPatternUnnamedEdgeContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchPatternNamedEdge.
    def enterGraphMatchPatternNamedEdge(self, ctx:HqlParser.GraphMatchPatternNamedEdgeContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchPatternNamedEdge.
    def exitGraphMatchPatternNamedEdge(self, ctx:HqlParser.GraphMatchPatternNamedEdgeContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchPatternRange.
    def enterGraphMatchPatternRange(self, ctx:HqlParser.GraphMatchPatternRangeContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchPatternRange.
    def exitGraphMatchPatternRange(self, ctx:HqlParser.GraphMatchPatternRangeContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchWhereClause.
    def enterGraphMatchWhereClause(self, ctx:HqlParser.GraphMatchWhereClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchWhereClause.
    def exitGraphMatchWhereClause(self, ctx:HqlParser.GraphMatchWhereClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMatchProjectClause.
    def enterGraphMatchProjectClause(self, ctx:HqlParser.GraphMatchProjectClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMatchProjectClause.
    def exitGraphMatchProjectClause(self, ctx:HqlParser.GraphMatchProjectClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#graphMergeOperator.
    def enterGraphMergeOperator(self, ctx:HqlParser.GraphMergeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#graphMergeOperator.
    def exitGraphMergeOperator(self, ctx:HqlParser.GraphMergeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#graphToTableOperator.
    def enterGraphToTableOperator(self, ctx:HqlParser.GraphToTableOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#graphToTableOperator.
    def exitGraphToTableOperator(self, ctx:HqlParser.GraphToTableOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#graphToTableOutput.
    def enterGraphToTableOutput(self, ctx:HqlParser.GraphToTableOutputContext):
        pass

    # Exit a parse tree produced by HqlParser#graphToTableOutput.
    def exitGraphToTableOutput(self, ctx:HqlParser.GraphToTableOutputContext):
        pass


    # Enter a parse tree produced by HqlParser#graphToTableAsClause.
    def enterGraphToTableAsClause(self, ctx:HqlParser.GraphToTableAsClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#graphToTableAsClause.
    def exitGraphToTableAsClause(self, ctx:HqlParser.GraphToTableAsClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#graphShortestPathsOperator.
    def enterGraphShortestPathsOperator(self, ctx:HqlParser.GraphShortestPathsOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#graphShortestPathsOperator.
    def exitGraphShortestPathsOperator(self, ctx:HqlParser.GraphShortestPathsOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#invokeOperator.
    def enterInvokeOperator(self, ctx:HqlParser.InvokeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#invokeOperator.
    def exitInvokeOperator(self, ctx:HqlParser.InvokeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#joinOperator.
    def enterJoinOperator(self, ctx:HqlParser.JoinOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#joinOperator.
    def exitJoinOperator(self, ctx:HqlParser.JoinOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#joinOperatorOnClause.
    def enterJoinOperatorOnClause(self, ctx:HqlParser.JoinOperatorOnClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#joinOperatorOnClause.
    def exitJoinOperatorOnClause(self, ctx:HqlParser.JoinOperatorOnClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#joinOperatorWhereClause.
    def enterJoinOperatorWhereClause(self, ctx:HqlParser.JoinOperatorWhereClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#joinOperatorWhereClause.
    def exitJoinOperatorWhereClause(self, ctx:HqlParser.JoinOperatorWhereClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#lookupOperator.
    def enterLookupOperator(self, ctx:HqlParser.LookupOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#lookupOperator.
    def exitLookupOperator(self, ctx:HqlParser.LookupOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#macroExpandOperator.
    def enterMacroExpandOperator(self, ctx:HqlParser.MacroExpandOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#macroExpandOperator.
    def exitMacroExpandOperator(self, ctx:HqlParser.MacroExpandOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#macroExpandEntityGroup.
    def enterMacroExpandEntityGroup(self, ctx:HqlParser.MacroExpandEntityGroupContext):
        pass

    # Exit a parse tree produced by HqlParser#macroExpandEntityGroup.
    def exitMacroExpandEntityGroup(self, ctx:HqlParser.MacroExpandEntityGroupContext):
        pass


    # Enter a parse tree produced by HqlParser#entityGroupExpression.
    def enterEntityGroupExpression(self, ctx:HqlParser.EntityGroupExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#entityGroupExpression.
    def exitEntityGroupExpression(self, ctx:HqlParser.EntityGroupExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#makeGraphOperator.
    def enterMakeGraphOperator(self, ctx:HqlParser.MakeGraphOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#makeGraphOperator.
    def exitMakeGraphOperator(self, ctx:HqlParser.MakeGraphOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#makeGraphIdClause.
    def enterMakeGraphIdClause(self, ctx:HqlParser.MakeGraphIdClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeGraphIdClause.
    def exitMakeGraphIdClause(self, ctx:HqlParser.MakeGraphIdClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeGraphTablesAndKeysClause.
    def enterMakeGraphTablesAndKeysClause(self, ctx:HqlParser.MakeGraphTablesAndKeysClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeGraphTablesAndKeysClause.
    def exitMakeGraphTablesAndKeysClause(self, ctx:HqlParser.MakeGraphTablesAndKeysClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeGraphPartitionedByClause.
    def enterMakeGraphPartitionedByClause(self, ctx:HqlParser.MakeGraphPartitionedByClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeGraphPartitionedByClause.
    def exitMakeGraphPartitionedByClause(self, ctx:HqlParser.MakeGraphPartitionedByClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperator.
    def enterMakeSeriesOperator(self, ctx:HqlParser.MakeSeriesOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperator.
    def exitMakeSeriesOperator(self, ctx:HqlParser.MakeSeriesOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperatorOnClause.
    def enterMakeSeriesOperatorOnClause(self, ctx:HqlParser.MakeSeriesOperatorOnClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperatorOnClause.
    def exitMakeSeriesOperatorOnClause(self, ctx:HqlParser.MakeSeriesOperatorOnClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperatorAggregation.
    def enterMakeSeriesOperatorAggregation(self, ctx:HqlParser.MakeSeriesOperatorAggregationContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperatorAggregation.
    def exitMakeSeriesOperatorAggregation(self, ctx:HqlParser.MakeSeriesOperatorAggregationContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperatorExpressionDefaultClause.
    def enterMakeSeriesOperatorExpressionDefaultClause(self, ctx:HqlParser.MakeSeriesOperatorExpressionDefaultClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperatorExpressionDefaultClause.
    def exitMakeSeriesOperatorExpressionDefaultClause(self, ctx:HqlParser.MakeSeriesOperatorExpressionDefaultClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperatorInRangeClause.
    def enterMakeSeriesOperatorInRangeClause(self, ctx:HqlParser.MakeSeriesOperatorInRangeClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperatorInRangeClause.
    def exitMakeSeriesOperatorInRangeClause(self, ctx:HqlParser.MakeSeriesOperatorInRangeClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperatorFromToStepClause.
    def enterMakeSeriesOperatorFromToStepClause(self, ctx:HqlParser.MakeSeriesOperatorFromToStepClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperatorFromToStepClause.
    def exitMakeSeriesOperatorFromToStepClause(self, ctx:HqlParser.MakeSeriesOperatorFromToStepClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#makeSeriesOperatorByClause.
    def enterMakeSeriesOperatorByClause(self, ctx:HqlParser.MakeSeriesOperatorByClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#makeSeriesOperatorByClause.
    def exitMakeSeriesOperatorByClause(self, ctx:HqlParser.MakeSeriesOperatorByClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#mvapplyOperator.
    def enterMvapplyOperator(self, ctx:HqlParser.MvapplyOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#mvapplyOperator.
    def exitMvapplyOperator(self, ctx:HqlParser.MvapplyOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#mvapplyOperatorLimitClause.
    def enterMvapplyOperatorLimitClause(self, ctx:HqlParser.MvapplyOperatorLimitClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#mvapplyOperatorLimitClause.
    def exitMvapplyOperatorLimitClause(self, ctx:HqlParser.MvapplyOperatorLimitClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#mvapplyOperatorIdClause.
    def enterMvapplyOperatorIdClause(self, ctx:HqlParser.MvapplyOperatorIdClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#mvapplyOperatorIdClause.
    def exitMvapplyOperatorIdClause(self, ctx:HqlParser.MvapplyOperatorIdClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#mvapplyOperatorExpression.
    def enterMvapplyOperatorExpression(self, ctx:HqlParser.MvapplyOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#mvapplyOperatorExpression.
    def exitMvapplyOperatorExpression(self, ctx:HqlParser.MvapplyOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#mvapplyOperatorExpressionToClause.
    def enterMvapplyOperatorExpressionToClause(self, ctx:HqlParser.MvapplyOperatorExpressionToClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#mvapplyOperatorExpressionToClause.
    def exitMvapplyOperatorExpressionToClause(self, ctx:HqlParser.MvapplyOperatorExpressionToClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#mvexpandOperator.
    def enterMvexpandOperator(self, ctx:HqlParser.MvexpandOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#mvexpandOperator.
    def exitMvexpandOperator(self, ctx:HqlParser.MvexpandOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#mvexpandOperatorExpression.
    def enterMvexpandOperatorExpression(self, ctx:HqlParser.MvexpandOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#mvexpandOperatorExpression.
    def exitMvexpandOperatorExpression(self, ctx:HqlParser.MvexpandOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#parseOperator.
    def enterParseOperator(self, ctx:HqlParser.ParseOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#parseOperator.
    def exitParseOperator(self, ctx:HqlParser.ParseOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#parseOperatorKindClause.
    def enterParseOperatorKindClause(self, ctx:HqlParser.ParseOperatorKindClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#parseOperatorKindClause.
    def exitParseOperatorKindClause(self, ctx:HqlParser.ParseOperatorKindClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#parseOperatorFlagsClause.
    def enterParseOperatorFlagsClause(self, ctx:HqlParser.ParseOperatorFlagsClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#parseOperatorFlagsClause.
    def exitParseOperatorFlagsClause(self, ctx:HqlParser.ParseOperatorFlagsClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#parseOperatorNameAndOptionalType.
    def enterParseOperatorNameAndOptionalType(self, ctx:HqlParser.ParseOperatorNameAndOptionalTypeContext):
        pass

    # Exit a parse tree produced by HqlParser#parseOperatorNameAndOptionalType.
    def exitParseOperatorNameAndOptionalType(self, ctx:HqlParser.ParseOperatorNameAndOptionalTypeContext):
        pass


    # Enter a parse tree produced by HqlParser#parseOperatorPattern.
    def enterParseOperatorPattern(self, ctx:HqlParser.ParseOperatorPatternContext):
        pass

    # Exit a parse tree produced by HqlParser#parseOperatorPattern.
    def exitParseOperatorPattern(self, ctx:HqlParser.ParseOperatorPatternContext):
        pass


    # Enter a parse tree produced by HqlParser#parseOperatorPatternSegment.
    def enterParseOperatorPatternSegment(self, ctx:HqlParser.ParseOperatorPatternSegmentContext):
        pass

    # Exit a parse tree produced by HqlParser#parseOperatorPatternSegment.
    def exitParseOperatorPatternSegment(self, ctx:HqlParser.ParseOperatorPatternSegmentContext):
        pass


    # Enter a parse tree produced by HqlParser#parseWhereOperator.
    def enterParseWhereOperator(self, ctx:HqlParser.ParseWhereOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#parseWhereOperator.
    def exitParseWhereOperator(self, ctx:HqlParser.ParseWhereOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#parseKvOperator.
    def enterParseKvOperator(self, ctx:HqlParser.ParseKvOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#parseKvOperator.
    def exitParseKvOperator(self, ctx:HqlParser.ParseKvOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#parseKvWithClause.
    def enterParseKvWithClause(self, ctx:HqlParser.ParseKvWithClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#parseKvWithClause.
    def exitParseKvWithClause(self, ctx:HqlParser.ParseKvWithClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#partitionOperator.
    def enterPartitionOperator(self, ctx:HqlParser.PartitionOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#partitionOperator.
    def exitPartitionOperator(self, ctx:HqlParser.PartitionOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#partitionOperatorInClause.
    def enterPartitionOperatorInClause(self, ctx:HqlParser.PartitionOperatorInClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#partitionOperatorInClause.
    def exitPartitionOperatorInClause(self, ctx:HqlParser.PartitionOperatorInClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#partitionOperatorSubExpressionBody.
    def enterPartitionOperatorSubExpressionBody(self, ctx:HqlParser.PartitionOperatorSubExpressionBodyContext):
        pass

    # Exit a parse tree produced by HqlParser#partitionOperatorSubExpressionBody.
    def exitPartitionOperatorSubExpressionBody(self, ctx:HqlParser.PartitionOperatorSubExpressionBodyContext):
        pass


    # Enter a parse tree produced by HqlParser#partitionOperatorFullExpressionBody.
    def enterPartitionOperatorFullExpressionBody(self, ctx:HqlParser.PartitionOperatorFullExpressionBodyContext):
        pass

    # Exit a parse tree produced by HqlParser#partitionOperatorFullExpressionBody.
    def exitPartitionOperatorFullExpressionBody(self, ctx:HqlParser.PartitionOperatorFullExpressionBodyContext):
        pass


    # Enter a parse tree produced by HqlParser#partitionByOperator.
    def enterPartitionByOperator(self, ctx:HqlParser.PartitionByOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#partitionByOperator.
    def exitPartitionByOperator(self, ctx:HqlParser.PartitionByOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#partitionByOperatorIdClause.
    def enterPartitionByOperatorIdClause(self, ctx:HqlParser.PartitionByOperatorIdClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#partitionByOperatorIdClause.
    def exitPartitionByOperatorIdClause(self, ctx:HqlParser.PartitionByOperatorIdClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#printOperator.
    def enterPrintOperator(self, ctx:HqlParser.PrintOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#printOperator.
    def exitPrintOperator(self, ctx:HqlParser.PrintOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#projectAwayOperator.
    def enterProjectAwayOperator(self, ctx:HqlParser.ProjectAwayOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#projectAwayOperator.
    def exitProjectAwayOperator(self, ctx:HqlParser.ProjectAwayOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#projectKeepOperator.
    def enterProjectKeepOperator(self, ctx:HqlParser.ProjectKeepOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#projectKeepOperator.
    def exitProjectKeepOperator(self, ctx:HqlParser.ProjectKeepOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#projectOperator.
    def enterProjectOperator(self, ctx:HqlParser.ProjectOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#projectOperator.
    def exitProjectOperator(self, ctx:HqlParser.ProjectOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#projectRenameOperator.
    def enterProjectRenameOperator(self, ctx:HqlParser.ProjectRenameOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#projectRenameOperator.
    def exitProjectRenameOperator(self, ctx:HqlParser.ProjectRenameOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#projectReorderOperator.
    def enterProjectReorderOperator(self, ctx:HqlParser.ProjectReorderOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#projectReorderOperator.
    def exitProjectReorderOperator(self, ctx:HqlParser.ProjectReorderOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#projectReorderExpression.
    def enterProjectReorderExpression(self, ctx:HqlParser.ProjectReorderExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#projectReorderExpression.
    def exitProjectReorderExpression(self, ctx:HqlParser.ProjectReorderExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#reduceByOperator.
    def enterReduceByOperator(self, ctx:HqlParser.ReduceByOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#reduceByOperator.
    def exitReduceByOperator(self, ctx:HqlParser.ReduceByOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#reduceByWithClause.
    def enterReduceByWithClause(self, ctx:HqlParser.ReduceByWithClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#reduceByWithClause.
    def exitReduceByWithClause(self, ctx:HqlParser.ReduceByWithClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#renderOperator.
    def enterRenderOperator(self, ctx:HqlParser.RenderOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#renderOperator.
    def exitRenderOperator(self, ctx:HqlParser.RenderOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#renderOperatorWithClause.
    def enterRenderOperatorWithClause(self, ctx:HqlParser.RenderOperatorWithClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#renderOperatorWithClause.
    def exitRenderOperatorWithClause(self, ctx:HqlParser.RenderOperatorWithClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#renderOperatorLegacyPropertyList.
    def enterRenderOperatorLegacyPropertyList(self, ctx:HqlParser.RenderOperatorLegacyPropertyListContext):
        pass

    # Exit a parse tree produced by HqlParser#renderOperatorLegacyPropertyList.
    def exitRenderOperatorLegacyPropertyList(self, ctx:HqlParser.RenderOperatorLegacyPropertyListContext):
        pass


    # Enter a parse tree produced by HqlParser#renderOperatorProperty.
    def enterRenderOperatorProperty(self, ctx:HqlParser.RenderOperatorPropertyContext):
        pass

    # Exit a parse tree produced by HqlParser#renderOperatorProperty.
    def exitRenderOperatorProperty(self, ctx:HqlParser.RenderOperatorPropertyContext):
        pass


    # Enter a parse tree produced by HqlParser#renderPropertyNameList.
    def enterRenderPropertyNameList(self, ctx:HqlParser.RenderPropertyNameListContext):
        pass

    # Exit a parse tree produced by HqlParser#renderPropertyNameList.
    def exitRenderPropertyNameList(self, ctx:HqlParser.RenderPropertyNameListContext):
        pass


    # Enter a parse tree produced by HqlParser#renderOperatorLegacyProperty.
    def enterRenderOperatorLegacyProperty(self, ctx:HqlParser.RenderOperatorLegacyPropertyContext):
        pass

    # Exit a parse tree produced by HqlParser#renderOperatorLegacyProperty.
    def exitRenderOperatorLegacyProperty(self, ctx:HqlParser.RenderOperatorLegacyPropertyContext):
        pass


    # Enter a parse tree produced by HqlParser#sampleDistinctOperator.
    def enterSampleDistinctOperator(self, ctx:HqlParser.SampleDistinctOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#sampleDistinctOperator.
    def exitSampleDistinctOperator(self, ctx:HqlParser.SampleDistinctOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#sampleOperator.
    def enterSampleOperator(self, ctx:HqlParser.SampleOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#sampleOperator.
    def exitSampleOperator(self, ctx:HqlParser.SampleOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperator.
    def enterScanOperator(self, ctx:HqlParser.ScanOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperator.
    def exitScanOperator(self, ctx:HqlParser.ScanOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorOrderByClause.
    def enterScanOperatorOrderByClause(self, ctx:HqlParser.ScanOperatorOrderByClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorOrderByClause.
    def exitScanOperatorOrderByClause(self, ctx:HqlParser.ScanOperatorOrderByClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorPartitionByClause.
    def enterScanOperatorPartitionByClause(self, ctx:HqlParser.ScanOperatorPartitionByClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorPartitionByClause.
    def exitScanOperatorPartitionByClause(self, ctx:HqlParser.ScanOperatorPartitionByClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorDeclareClause.
    def enterScanOperatorDeclareClause(self, ctx:HqlParser.ScanOperatorDeclareClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorDeclareClause.
    def exitScanOperatorDeclareClause(self, ctx:HqlParser.ScanOperatorDeclareClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorStep.
    def enterScanOperatorStep(self, ctx:HqlParser.ScanOperatorStepContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorStep.
    def exitScanOperatorStep(self, ctx:HqlParser.ScanOperatorStepContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorStepOutputClause.
    def enterScanOperatorStepOutputClause(self, ctx:HqlParser.ScanOperatorStepOutputClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorStepOutputClause.
    def exitScanOperatorStepOutputClause(self, ctx:HqlParser.ScanOperatorStepOutputClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorBody.
    def enterScanOperatorBody(self, ctx:HqlParser.ScanOperatorBodyContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorBody.
    def exitScanOperatorBody(self, ctx:HqlParser.ScanOperatorBodyContext):
        pass


    # Enter a parse tree produced by HqlParser#scanOperatorAssignment.
    def enterScanOperatorAssignment(self, ctx:HqlParser.ScanOperatorAssignmentContext):
        pass

    # Exit a parse tree produced by HqlParser#scanOperatorAssignment.
    def exitScanOperatorAssignment(self, ctx:HqlParser.ScanOperatorAssignmentContext):
        pass


    # Enter a parse tree produced by HqlParser#searchOperator.
    def enterSearchOperator(self, ctx:HqlParser.SearchOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#searchOperator.
    def exitSearchOperator(self, ctx:HqlParser.SearchOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#searchOperatorStarAndExpression.
    def enterSearchOperatorStarAndExpression(self, ctx:HqlParser.SearchOperatorStarAndExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#searchOperatorStarAndExpression.
    def exitSearchOperatorStarAndExpression(self, ctx:HqlParser.SearchOperatorStarAndExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#searchOperatorInClause.
    def enterSearchOperatorInClause(self, ctx:HqlParser.SearchOperatorInClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#searchOperatorInClause.
    def exitSearchOperatorInClause(self, ctx:HqlParser.SearchOperatorInClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#serializeOperator.
    def enterSerializeOperator(self, ctx:HqlParser.SerializeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#serializeOperator.
    def exitSerializeOperator(self, ctx:HqlParser.SerializeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#sortOperator.
    def enterSortOperator(self, ctx:HqlParser.SortOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#sortOperator.
    def exitSortOperator(self, ctx:HqlParser.SortOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#orderedExpression.
    def enterOrderedExpression(self, ctx:HqlParser.OrderedExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#orderedExpression.
    def exitOrderedExpression(self, ctx:HqlParser.OrderedExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#sortOrdering.
    def enterSortOrdering(self, ctx:HqlParser.SortOrderingContext):
        pass

    # Exit a parse tree produced by HqlParser#sortOrdering.
    def exitSortOrdering(self, ctx:HqlParser.SortOrderingContext):
        pass


    # Enter a parse tree produced by HqlParser#summarizeOperator.
    def enterSummarizeOperator(self, ctx:HqlParser.SummarizeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#summarizeOperator.
    def exitSummarizeOperator(self, ctx:HqlParser.SummarizeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#summarizeOperatorByClause.
    def enterSummarizeOperatorByClause(self, ctx:HqlParser.SummarizeOperatorByClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#summarizeOperatorByClause.
    def exitSummarizeOperatorByClause(self, ctx:HqlParser.SummarizeOperatorByClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#summarizeOperatorLegacyBinClause.
    def enterSummarizeOperatorLegacyBinClause(self, ctx:HqlParser.SummarizeOperatorLegacyBinClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#summarizeOperatorLegacyBinClause.
    def exitSummarizeOperatorLegacyBinClause(self, ctx:HqlParser.SummarizeOperatorLegacyBinClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#takeOperator.
    def enterTakeOperator(self, ctx:HqlParser.TakeOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#takeOperator.
    def exitTakeOperator(self, ctx:HqlParser.TakeOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#topOperator.
    def enterTopOperator(self, ctx:HqlParser.TopOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#topOperator.
    def exitTopOperator(self, ctx:HqlParser.TopOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#topHittersOperator.
    def enterTopHittersOperator(self, ctx:HqlParser.TopHittersOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#topHittersOperator.
    def exitTopHittersOperator(self, ctx:HqlParser.TopHittersOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#topHittersOperatorByClause.
    def enterTopHittersOperatorByClause(self, ctx:HqlParser.TopHittersOperatorByClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#topHittersOperatorByClause.
    def exitTopHittersOperatorByClause(self, ctx:HqlParser.TopHittersOperatorByClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#topNestedOperator.
    def enterTopNestedOperator(self, ctx:HqlParser.TopNestedOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#topNestedOperator.
    def exitTopNestedOperator(self, ctx:HqlParser.TopNestedOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#topNestedOperatorPart.
    def enterTopNestedOperatorPart(self, ctx:HqlParser.TopNestedOperatorPartContext):
        pass

    # Exit a parse tree produced by HqlParser#topNestedOperatorPart.
    def exitTopNestedOperatorPart(self, ctx:HqlParser.TopNestedOperatorPartContext):
        pass


    # Enter a parse tree produced by HqlParser#topNestedOperatorWithOthersClause.
    def enterTopNestedOperatorWithOthersClause(self, ctx:HqlParser.TopNestedOperatorWithOthersClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#topNestedOperatorWithOthersClause.
    def exitTopNestedOperatorWithOthersClause(self, ctx:HqlParser.TopNestedOperatorWithOthersClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#unionOperator.
    def enterUnionOperator(self, ctx:HqlParser.UnionOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#unionOperator.
    def exitUnionOperator(self, ctx:HqlParser.UnionOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#unionOperatorExpression.
    def enterUnionOperatorExpression(self, ctx:HqlParser.UnionOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#unionOperatorExpression.
    def exitUnionOperatorExpression(self, ctx:HqlParser.UnionOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#whereOperator.
    def enterWhereOperator(self, ctx:HqlParser.WhereOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#whereOperator.
    def exitWhereOperator(self, ctx:HqlParser.WhereOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#contextualSubExpression.
    def enterContextualSubExpression(self, ctx:HqlParser.ContextualSubExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#contextualSubExpression.
    def exitContextualSubExpression(self, ctx:HqlParser.ContextualSubExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#contextualPipeExpression.
    def enterContextualPipeExpression(self, ctx:HqlParser.ContextualPipeExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#contextualPipeExpression.
    def exitContextualPipeExpression(self, ctx:HqlParser.ContextualPipeExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#contextualPipeExpressionPipedOperator.
    def enterContextualPipeExpressionPipedOperator(self, ctx:HqlParser.ContextualPipeExpressionPipedOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#contextualPipeExpressionPipedOperator.
    def exitContextualPipeExpressionPipedOperator(self, ctx:HqlParser.ContextualPipeExpressionPipedOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#strictQueryOperatorParameter.
    def enterStrictQueryOperatorParameter(self, ctx:HqlParser.StrictQueryOperatorParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#strictQueryOperatorParameter.
    def exitStrictQueryOperatorParameter(self, ctx:HqlParser.StrictQueryOperatorParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#relaxedQueryOperatorParameter.
    def enterRelaxedQueryOperatorParameter(self, ctx:HqlParser.RelaxedQueryOperatorParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#relaxedQueryOperatorParameter.
    def exitRelaxedQueryOperatorParameter(self, ctx:HqlParser.RelaxedQueryOperatorParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#queryOperatorProperty.
    def enterQueryOperatorProperty(self, ctx:HqlParser.QueryOperatorPropertyContext):
        pass

    # Exit a parse tree produced by HqlParser#queryOperatorProperty.
    def exitQueryOperatorProperty(self, ctx:HqlParser.QueryOperatorPropertyContext):
        pass


    # Enter a parse tree produced by HqlParser#namedExpression.
    def enterNamedExpression(self, ctx:HqlParser.NamedExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#namedExpression.
    def exitNamedExpression(self, ctx:HqlParser.NamedExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#namedExpressionNameClause.
    def enterNamedExpressionNameClause(self, ctx:HqlParser.NamedExpressionNameClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#namedExpressionNameClause.
    def exitNamedExpressionNameClause(self, ctx:HqlParser.NamedExpressionNameClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#namedExpressionNameList.
    def enterNamedExpressionNameList(self, ctx:HqlParser.NamedExpressionNameListContext):
        pass

    # Exit a parse tree produced by HqlParser#namedExpressionNameList.
    def exitNamedExpressionNameList(self, ctx:HqlParser.NamedExpressionNameListContext):
        pass


    # Enter a parse tree produced by HqlParser#scopedFunctionCallExpression.
    def enterScopedFunctionCallExpression(self, ctx:HqlParser.ScopedFunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#scopedFunctionCallExpression.
    def exitScopedFunctionCallExpression(self, ctx:HqlParser.ScopedFunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#unnamedExpression.
    def enterUnnamedExpression(self, ctx:HqlParser.UnnamedExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#unnamedExpression.
    def exitUnnamedExpression(self, ctx:HqlParser.UnnamedExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:HqlParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:HqlParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#logicalOrOperation.
    def enterLogicalOrOperation(self, ctx:HqlParser.LogicalOrOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#logicalOrOperation.
    def exitLogicalOrOperation(self, ctx:HqlParser.LogicalOrOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:HqlParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:HqlParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#logicalAndOperation.
    def enterLogicalAndOperation(self, ctx:HqlParser.LogicalAndOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#logicalAndOperation.
    def exitLogicalAndOperation(self, ctx:HqlParser.LogicalAndOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#equalityExpression.
    def enterEqualityExpression(self, ctx:HqlParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#equalityExpression.
    def exitEqualityExpression(self, ctx:HqlParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#equalsEqualityExpression.
    def enterEqualsEqualityExpression(self, ctx:HqlParser.EqualsEqualityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#equalsEqualityExpression.
    def exitEqualsEqualityExpression(self, ctx:HqlParser.EqualsEqualityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#listEqualityExpression.
    def enterListEqualityExpression(self, ctx:HqlParser.ListEqualityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#listEqualityExpression.
    def exitListEqualityExpression(self, ctx:HqlParser.ListEqualityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#betweenEqualityExpression.
    def enterBetweenEqualityExpression(self, ctx:HqlParser.BetweenEqualityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#betweenEqualityExpression.
    def exitBetweenEqualityExpression(self, ctx:HqlParser.BetweenEqualityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#starEqualityExpression.
    def enterStarEqualityExpression(self, ctx:HqlParser.StarEqualityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#starEqualityExpression.
    def exitStarEqualityExpression(self, ctx:HqlParser.StarEqualityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#relationalExpression.
    def enterRelationalExpression(self, ctx:HqlParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#relationalExpression.
    def exitRelationalExpression(self, ctx:HqlParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:HqlParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:HqlParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#additiveOperation.
    def enterAdditiveOperation(self, ctx:HqlParser.AdditiveOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#additiveOperation.
    def exitAdditiveOperation(self, ctx:HqlParser.AdditiveOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:HqlParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:HqlParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#multiplicativeOperation.
    def enterMultiplicativeOperation(self, ctx:HqlParser.MultiplicativeOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#multiplicativeOperation.
    def exitMultiplicativeOperation(self, ctx:HqlParser.MultiplicativeOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#stringOperatorExpression.
    def enterStringOperatorExpression(self, ctx:HqlParser.StringOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#stringOperatorExpression.
    def exitStringOperatorExpression(self, ctx:HqlParser.StringOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#stringBinaryOperatorExpression.
    def enterStringBinaryOperatorExpression(self, ctx:HqlParser.StringBinaryOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#stringBinaryOperatorExpression.
    def exitStringBinaryOperatorExpression(self, ctx:HqlParser.StringBinaryOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#stringBinaryOperation.
    def enterStringBinaryOperation(self, ctx:HqlParser.StringBinaryOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#stringBinaryOperation.
    def exitStringBinaryOperation(self, ctx:HqlParser.StringBinaryOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#stringBinaryOperator.
    def enterStringBinaryOperator(self, ctx:HqlParser.StringBinaryOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#stringBinaryOperator.
    def exitStringBinaryOperator(self, ctx:HqlParser.StringBinaryOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#stringStarOperatorExpression.
    def enterStringStarOperatorExpression(self, ctx:HqlParser.StringStarOperatorExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#stringStarOperatorExpression.
    def exitStringStarOperatorExpression(self, ctx:HqlParser.StringStarOperatorExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#invocationExpression.
    def enterInvocationExpression(self, ctx:HqlParser.InvocationExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#invocationExpression.
    def exitInvocationExpression(self, ctx:HqlParser.InvocationExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#functionCallOrPathExpression.
    def enterFunctionCallOrPathExpression(self, ctx:HqlParser.FunctionCallOrPathExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#functionCallOrPathExpression.
    def exitFunctionCallOrPathExpression(self, ctx:HqlParser.FunctionCallOrPathExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#functionCallOrPathRoot.
    def enterFunctionCallOrPathRoot(self, ctx:HqlParser.FunctionCallOrPathRootContext):
        pass

    # Exit a parse tree produced by HqlParser#functionCallOrPathRoot.
    def exitFunctionCallOrPathRoot(self, ctx:HqlParser.FunctionCallOrPathRootContext):
        pass


    # Enter a parse tree produced by HqlParser#functionCallOrPathPathExpression.
    def enterFunctionCallOrPathPathExpression(self, ctx:HqlParser.FunctionCallOrPathPathExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#functionCallOrPathPathExpression.
    def exitFunctionCallOrPathPathExpression(self, ctx:HqlParser.FunctionCallOrPathPathExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#functionCallOrPathOperation.
    def enterFunctionCallOrPathOperation(self, ctx:HqlParser.FunctionCallOrPathOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#functionCallOrPathOperation.
    def exitFunctionCallOrPathOperation(self, ctx:HqlParser.FunctionCallOrPathOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#functionalCallOrPathPathOperation.
    def enterFunctionalCallOrPathPathOperation(self, ctx:HqlParser.FunctionalCallOrPathPathOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#functionalCallOrPathPathOperation.
    def exitFunctionalCallOrPathPathOperation(self, ctx:HqlParser.FunctionalCallOrPathPathOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#functionCallOrPathElementOperation.
    def enterFunctionCallOrPathElementOperation(self, ctx:HqlParser.FunctionCallOrPathElementOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#functionCallOrPathElementOperation.
    def exitFunctionCallOrPathElementOperation(self, ctx:HqlParser.FunctionCallOrPathElementOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#legacyFunctionCallOrPathElementOperation.
    def enterLegacyFunctionCallOrPathElementOperation(self, ctx:HqlParser.LegacyFunctionCallOrPathElementOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#legacyFunctionCallOrPathElementOperation.
    def exitLegacyFunctionCallOrPathElementOperation(self, ctx:HqlParser.LegacyFunctionCallOrPathElementOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#toScalarExpression.
    def enterToScalarExpression(self, ctx:HqlParser.ToScalarExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#toScalarExpression.
    def exitToScalarExpression(self, ctx:HqlParser.ToScalarExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#toTableExpression.
    def enterToTableExpression(self, ctx:HqlParser.ToTableExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#toTableExpression.
    def exitToTableExpression(self, ctx:HqlParser.ToTableExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#noOptimizationParameter.
    def enterNoOptimizationParameter(self, ctx:HqlParser.NoOptimizationParameterContext):
        pass

    # Exit a parse tree produced by HqlParser#noOptimizationParameter.
    def exitNoOptimizationParameter(self, ctx:HqlParser.NoOptimizationParameterContext):
        pass


    # Enter a parse tree produced by HqlParser#dotCompositeFunctionCallExpression.
    def enterDotCompositeFunctionCallExpression(self, ctx:HqlParser.DotCompositeFunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#dotCompositeFunctionCallExpression.
    def exitDotCompositeFunctionCallExpression(self, ctx:HqlParser.DotCompositeFunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#dotCompositeFunctionCallOperation.
    def enterDotCompositeFunctionCallOperation(self, ctx:HqlParser.DotCompositeFunctionCallOperationContext):
        pass

    # Exit a parse tree produced by HqlParser#dotCompositeFunctionCallOperation.
    def exitDotCompositeFunctionCallOperation(self, ctx:HqlParser.DotCompositeFunctionCallOperationContext):
        pass


    # Enter a parse tree produced by HqlParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:HqlParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:HqlParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#namedFunctionCallExpression.
    def enterNamedFunctionCallExpression(self, ctx:HqlParser.NamedFunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#namedFunctionCallExpression.
    def exitNamedFunctionCallExpression(self, ctx:HqlParser.NamedFunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#argumentExpression.
    def enterArgumentExpression(self, ctx:HqlParser.ArgumentExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#argumentExpression.
    def exitArgumentExpression(self, ctx:HqlParser.ArgumentExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#countExpression.
    def enterCountExpression(self, ctx:HqlParser.CountExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#countExpression.
    def exitCountExpression(self, ctx:HqlParser.CountExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#starExpression.
    def enterStarExpression(self, ctx:HqlParser.StarExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#starExpression.
    def exitStarExpression(self, ctx:HqlParser.StarExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:HqlParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:HqlParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#nameReferenceWithDataScope.
    def enterNameReferenceWithDataScope(self, ctx:HqlParser.NameReferenceWithDataScopeContext):
        pass

    # Exit a parse tree produced by HqlParser#nameReferenceWithDataScope.
    def exitNameReferenceWithDataScope(self, ctx:HqlParser.NameReferenceWithDataScopeContext):
        pass


    # Enter a parse tree produced by HqlParser#dataScopeClause.
    def enterDataScopeClause(self, ctx:HqlParser.DataScopeClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#dataScopeClause.
    def exitDataScopeClause(self, ctx:HqlParser.DataScopeClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:HqlParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:HqlParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#rangeExpression.
    def enterRangeExpression(self, ctx:HqlParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#rangeExpression.
    def exitRangeExpression(self, ctx:HqlParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#entityExpression.
    def enterEntityExpression(self, ctx:HqlParser.EntityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#entityExpression.
    def exitEntityExpression(self, ctx:HqlParser.EntityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#entityPathOrElementExpression.
    def enterEntityPathOrElementExpression(self, ctx:HqlParser.EntityPathOrElementExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#entityPathOrElementExpression.
    def exitEntityPathOrElementExpression(self, ctx:HqlParser.EntityPathOrElementExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#entityPathOrElementOperator.
    def enterEntityPathOrElementOperator(self, ctx:HqlParser.EntityPathOrElementOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#entityPathOrElementOperator.
    def exitEntityPathOrElementOperator(self, ctx:HqlParser.EntityPathOrElementOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#entityPathOperator.
    def enterEntityPathOperator(self, ctx:HqlParser.EntityPathOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#entityPathOperator.
    def exitEntityPathOperator(self, ctx:HqlParser.EntityPathOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#entityElementOperator.
    def enterEntityElementOperator(self, ctx:HqlParser.EntityElementOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#entityElementOperator.
    def exitEntityElementOperator(self, ctx:HqlParser.EntityElementOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#legacyEntityPathElementOperator.
    def enterLegacyEntityPathElementOperator(self, ctx:HqlParser.LegacyEntityPathElementOperatorContext):
        pass

    # Exit a parse tree produced by HqlParser#legacyEntityPathElementOperator.
    def exitLegacyEntityPathElementOperator(self, ctx:HqlParser.LegacyEntityPathElementOperatorContext):
        pass


    # Enter a parse tree produced by HqlParser#entityName.
    def enterEntityName(self, ctx:HqlParser.EntityNameContext):
        pass

    # Exit a parse tree produced by HqlParser#entityName.
    def exitEntityName(self, ctx:HqlParser.EntityNameContext):
        pass


    # Enter a parse tree produced by HqlParser#entityNameReference.
    def enterEntityNameReference(self, ctx:HqlParser.EntityNameReferenceContext):
        pass

    # Exit a parse tree produced by HqlParser#entityNameReference.
    def exitEntityNameReference(self, ctx:HqlParser.EntityNameReferenceContext):
        pass


    # Enter a parse tree produced by HqlParser#atSignName.
    def enterAtSignName(self, ctx:HqlParser.AtSignNameContext):
        pass

    # Exit a parse tree produced by HqlParser#atSignName.
    def exitAtSignName(self, ctx:HqlParser.AtSignNameContext):
        pass


    # Enter a parse tree produced by HqlParser#extendedPathName.
    def enterExtendedPathName(self, ctx:HqlParser.ExtendedPathNameContext):
        pass

    # Exit a parse tree produced by HqlParser#extendedPathName.
    def exitExtendedPathName(self, ctx:HqlParser.ExtendedPathNameContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedEntityExpression.
    def enterWildcardedEntityExpression(self, ctx:HqlParser.WildcardedEntityExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedEntityExpression.
    def exitWildcardedEntityExpression(self, ctx:HqlParser.WildcardedEntityExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedPathExpression.
    def enterWildcardedPathExpression(self, ctx:HqlParser.WildcardedPathExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedPathExpression.
    def exitWildcardedPathExpression(self, ctx:HqlParser.WildcardedPathExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedPathName.
    def enterWildcardedPathName(self, ctx:HqlParser.WildcardedPathNameContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedPathName.
    def exitWildcardedPathName(self, ctx:HqlParser.WildcardedPathNameContext):
        pass


    # Enter a parse tree produced by HqlParser#contextualDataTableExpression.
    def enterContextualDataTableExpression(self, ctx:HqlParser.ContextualDataTableExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#contextualDataTableExpression.
    def exitContextualDataTableExpression(self, ctx:HqlParser.ContextualDataTableExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#dataTableExpression.
    def enterDataTableExpression(self, ctx:HqlParser.DataTableExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#dataTableExpression.
    def exitDataTableExpression(self, ctx:HqlParser.DataTableExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#rowSchema.
    def enterRowSchema(self, ctx:HqlParser.RowSchemaContext):
        pass

    # Exit a parse tree produced by HqlParser#rowSchema.
    def exitRowSchema(self, ctx:HqlParser.RowSchemaContext):
        pass


    # Enter a parse tree produced by HqlParser#rowSchemaColumnDeclaration.
    def enterRowSchemaColumnDeclaration(self, ctx:HqlParser.RowSchemaColumnDeclarationContext):
        pass

    # Exit a parse tree produced by HqlParser#rowSchemaColumnDeclaration.
    def exitRowSchemaColumnDeclaration(self, ctx:HqlParser.RowSchemaColumnDeclarationContext):
        pass


    # Enter a parse tree produced by HqlParser#externalDataExpression.
    def enterExternalDataExpression(self, ctx:HqlParser.ExternalDataExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#externalDataExpression.
    def exitExternalDataExpression(self, ctx:HqlParser.ExternalDataExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#externalDataWithClause.
    def enterExternalDataWithClause(self, ctx:HqlParser.ExternalDataWithClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#externalDataWithClause.
    def exitExternalDataWithClause(self, ctx:HqlParser.ExternalDataWithClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#externalDataWithClauseProperty.
    def enterExternalDataWithClauseProperty(self, ctx:HqlParser.ExternalDataWithClausePropertyContext):
        pass

    # Exit a parse tree produced by HqlParser#externalDataWithClauseProperty.
    def exitExternalDataWithClauseProperty(self, ctx:HqlParser.ExternalDataWithClausePropertyContext):
        pass


    # Enter a parse tree produced by HqlParser#materializedViewCombineExpression.
    def enterMaterializedViewCombineExpression(self, ctx:HqlParser.MaterializedViewCombineExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#materializedViewCombineExpression.
    def exitMaterializedViewCombineExpression(self, ctx:HqlParser.MaterializedViewCombineExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#materializeViewCombineBaseClause.
    def enterMaterializeViewCombineBaseClause(self, ctx:HqlParser.MaterializeViewCombineBaseClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#materializeViewCombineBaseClause.
    def exitMaterializeViewCombineBaseClause(self, ctx:HqlParser.MaterializeViewCombineBaseClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#materializedViewCombineDeltaClause.
    def enterMaterializedViewCombineDeltaClause(self, ctx:HqlParser.MaterializedViewCombineDeltaClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#materializedViewCombineDeltaClause.
    def exitMaterializedViewCombineDeltaClause(self, ctx:HqlParser.MaterializedViewCombineDeltaClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#materializedViewCombineAggregationsClause.
    def enterMaterializedViewCombineAggregationsClause(self, ctx:HqlParser.MaterializedViewCombineAggregationsClauseContext):
        pass

    # Exit a parse tree produced by HqlParser#materializedViewCombineAggregationsClause.
    def exitMaterializedViewCombineAggregationsClause(self, ctx:HqlParser.MaterializedViewCombineAggregationsClauseContext):
        pass


    # Enter a parse tree produced by HqlParser#scalarType.
    def enterScalarType(self, ctx:HqlParser.ScalarTypeContext):
        pass

    # Exit a parse tree produced by HqlParser#scalarType.
    def exitScalarType(self, ctx:HqlParser.ScalarTypeContext):
        pass


    # Enter a parse tree produced by HqlParser#extendedScalarType.
    def enterExtendedScalarType(self, ctx:HqlParser.ExtendedScalarTypeContext):
        pass

    # Exit a parse tree produced by HqlParser#extendedScalarType.
    def exitExtendedScalarType(self, ctx:HqlParser.ExtendedScalarTypeContext):
        pass


    # Enter a parse tree produced by HqlParser#parameterName.
    def enterParameterName(self, ctx:HqlParser.ParameterNameContext):
        pass

    # Exit a parse tree produced by HqlParser#parameterName.
    def exitParameterName(self, ctx:HqlParser.ParameterNameContext):
        pass


    # Enter a parse tree produced by HqlParser#simpleNameReference.
    def enterSimpleNameReference(self, ctx:HqlParser.SimpleNameReferenceContext):
        pass

    # Exit a parse tree produced by HqlParser#simpleNameReference.
    def exitSimpleNameReference(self, ctx:HqlParser.SimpleNameReferenceContext):
        pass


    # Enter a parse tree produced by HqlParser#extendedNameReference.
    def enterExtendedNameReference(self, ctx:HqlParser.ExtendedNameReferenceContext):
        pass

    # Exit a parse tree produced by HqlParser#extendedNameReference.
    def exitExtendedNameReference(self, ctx:HqlParser.ExtendedNameReferenceContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedNameReference.
    def enterWildcardedNameReference(self, ctx:HqlParser.WildcardedNameReferenceContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedNameReference.
    def exitWildcardedNameReference(self, ctx:HqlParser.WildcardedNameReferenceContext):
        pass


    # Enter a parse tree produced by HqlParser#simpleOrWildcardedNameReference.
    def enterSimpleOrWildcardedNameReference(self, ctx:HqlParser.SimpleOrWildcardedNameReferenceContext):
        pass

    # Exit a parse tree produced by HqlParser#simpleOrWildcardedNameReference.
    def exitSimpleOrWildcardedNameReference(self, ctx:HqlParser.SimpleOrWildcardedNameReferenceContext):
        pass


    # Enter a parse tree produced by HqlParser#identifierName.
    def enterIdentifierName(self, ctx:HqlParser.IdentifierNameContext):
        pass

    # Exit a parse tree produced by HqlParser#identifierName.
    def exitIdentifierName(self, ctx:HqlParser.IdentifierNameContext):
        pass


    # Enter a parse tree produced by HqlParser#keywordName.
    def enterKeywordName(self, ctx:HqlParser.KeywordNameContext):
        pass

    # Exit a parse tree produced by HqlParser#keywordName.
    def exitKeywordName(self, ctx:HqlParser.KeywordNameContext):
        pass


    # Enter a parse tree produced by HqlParser#extendedKeywordName.
    def enterExtendedKeywordName(self, ctx:HqlParser.ExtendedKeywordNameContext):
        pass

    # Exit a parse tree produced by HqlParser#extendedKeywordName.
    def exitExtendedKeywordName(self, ctx:HqlParser.ExtendedKeywordNameContext):
        pass


    # Enter a parse tree produced by HqlParser#escapedName.
    def enterEscapedName(self, ctx:HqlParser.EscapedNameContext):
        pass

    # Exit a parse tree produced by HqlParser#escapedName.
    def exitEscapedName(self, ctx:HqlParser.EscapedNameContext):
        pass


    # Enter a parse tree produced by HqlParser#identifierOrKeywordName.
    def enterIdentifierOrKeywordName(self, ctx:HqlParser.IdentifierOrKeywordNameContext):
        pass

    # Exit a parse tree produced by HqlParser#identifierOrKeywordName.
    def exitIdentifierOrKeywordName(self, ctx:HqlParser.IdentifierOrKeywordNameContext):
        pass


    # Enter a parse tree produced by HqlParser#identifierOrKeywordOrEscapedName.
    def enterIdentifierOrKeywordOrEscapedName(self, ctx:HqlParser.IdentifierOrKeywordOrEscapedNameContext):
        pass

    # Exit a parse tree produced by HqlParser#identifierOrKeywordOrEscapedName.
    def exitIdentifierOrKeywordOrEscapedName(self, ctx:HqlParser.IdentifierOrKeywordOrEscapedNameContext):
        pass


    # Enter a parse tree produced by HqlParser#identifierOrExtendedKeywordOrEscapedName.
    def enterIdentifierOrExtendedKeywordOrEscapedName(self, ctx:HqlParser.IdentifierOrExtendedKeywordOrEscapedNameContext):
        pass

    # Exit a parse tree produced by HqlParser#identifierOrExtendedKeywordOrEscapedName.
    def exitIdentifierOrExtendedKeywordOrEscapedName(self, ctx:HqlParser.IdentifierOrExtendedKeywordOrEscapedNameContext):
        pass


    # Enter a parse tree produced by HqlParser#identifierOrExtendedKeywordName.
    def enterIdentifierOrExtendedKeywordName(self, ctx:HqlParser.IdentifierOrExtendedKeywordNameContext):
        pass

    # Exit a parse tree produced by HqlParser#identifierOrExtendedKeywordName.
    def exitIdentifierOrExtendedKeywordName(self, ctx:HqlParser.IdentifierOrExtendedKeywordNameContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedName.
    def enterWildcardedName(self, ctx:HqlParser.WildcardedNameContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedName.
    def exitWildcardedName(self, ctx:HqlParser.WildcardedNameContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedNamePrefix.
    def enterWildcardedNamePrefix(self, ctx:HqlParser.WildcardedNamePrefixContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedNamePrefix.
    def exitWildcardedNamePrefix(self, ctx:HqlParser.WildcardedNamePrefixContext):
        pass


    # Enter a parse tree produced by HqlParser#wildcardedNameSegment.
    def enterWildcardedNameSegment(self, ctx:HqlParser.WildcardedNameSegmentContext):
        pass

    # Exit a parse tree produced by HqlParser#wildcardedNameSegment.
    def exitWildcardedNameSegment(self, ctx:HqlParser.WildcardedNameSegmentContext):
        pass


    # Enter a parse tree produced by HqlParser#literalExpression.
    def enterLiteralExpression(self, ctx:HqlParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#literalExpression.
    def exitLiteralExpression(self, ctx:HqlParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#unsignedLiteralExpression.
    def enterUnsignedLiteralExpression(self, ctx:HqlParser.UnsignedLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#unsignedLiteralExpression.
    def exitUnsignedLiteralExpression(self, ctx:HqlParser.UnsignedLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#numberLikeLiteralExpression.
    def enterNumberLikeLiteralExpression(self, ctx:HqlParser.NumberLikeLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#numberLikeLiteralExpression.
    def exitNumberLikeLiteralExpression(self, ctx:HqlParser.NumberLikeLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#numericLiteralExpression.
    def enterNumericLiteralExpression(self, ctx:HqlParser.NumericLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#numericLiteralExpression.
    def exitNumericLiteralExpression(self, ctx:HqlParser.NumericLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#signedLiteralExpression.
    def enterSignedLiteralExpression(self, ctx:HqlParser.SignedLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#signedLiteralExpression.
    def exitSignedLiteralExpression(self, ctx:HqlParser.SignedLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#longLiteralExpression.
    def enterLongLiteralExpression(self, ctx:HqlParser.LongLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#longLiteralExpression.
    def exitLongLiteralExpression(self, ctx:HqlParser.LongLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#intLiteralExpression.
    def enterIntLiteralExpression(self, ctx:HqlParser.IntLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#intLiteralExpression.
    def exitIntLiteralExpression(self, ctx:HqlParser.IntLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#realLiteralExpression.
    def enterRealLiteralExpression(self, ctx:HqlParser.RealLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#realLiteralExpression.
    def exitRealLiteralExpression(self, ctx:HqlParser.RealLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#decimalLiteralExpression.
    def enterDecimalLiteralExpression(self, ctx:HqlParser.DecimalLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#decimalLiteralExpression.
    def exitDecimalLiteralExpression(self, ctx:HqlParser.DecimalLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#dateTimeLiteralExpression.
    def enterDateTimeLiteralExpression(self, ctx:HqlParser.DateTimeLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#dateTimeLiteralExpression.
    def exitDateTimeLiteralExpression(self, ctx:HqlParser.DateTimeLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#timeSpanLiteralExpression.
    def enterTimeSpanLiteralExpression(self, ctx:HqlParser.TimeSpanLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#timeSpanLiteralExpression.
    def exitTimeSpanLiteralExpression(self, ctx:HqlParser.TimeSpanLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#booleanLiteralExpression.
    def enterBooleanLiteralExpression(self, ctx:HqlParser.BooleanLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#booleanLiteralExpression.
    def exitBooleanLiteralExpression(self, ctx:HqlParser.BooleanLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#guidLiteralExpression.
    def enterGuidLiteralExpression(self, ctx:HqlParser.GuidLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#guidLiteralExpression.
    def exitGuidLiteralExpression(self, ctx:HqlParser.GuidLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#typeLiteralExpression.
    def enterTypeLiteralExpression(self, ctx:HqlParser.TypeLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#typeLiteralExpression.
    def exitTypeLiteralExpression(self, ctx:HqlParser.TypeLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#signedLongLiteralExpression.
    def enterSignedLongLiteralExpression(self, ctx:HqlParser.SignedLongLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#signedLongLiteralExpression.
    def exitSignedLongLiteralExpression(self, ctx:HqlParser.SignedLongLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#signedRealLiteralExpression.
    def enterSignedRealLiteralExpression(self, ctx:HqlParser.SignedRealLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#signedRealLiteralExpression.
    def exitSignedRealLiteralExpression(self, ctx:HqlParser.SignedRealLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#stringLiteralExpression.
    def enterStringLiteralExpression(self, ctx:HqlParser.StringLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#stringLiteralExpression.
    def exitStringLiteralExpression(self, ctx:HqlParser.StringLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#dynamicLiteralExpression.
    def enterDynamicLiteralExpression(self, ctx:HqlParser.DynamicLiteralExpressionContext):
        pass

    # Exit a parse tree produced by HqlParser#dynamicLiteralExpression.
    def exitDynamicLiteralExpression(self, ctx:HqlParser.DynamicLiteralExpressionContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonValue.
    def enterJsonValue(self, ctx:HqlParser.JsonValueContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonValue.
    def exitJsonValue(self, ctx:HqlParser.JsonValueContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonObject.
    def enterJsonObject(self, ctx:HqlParser.JsonObjectContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonObject.
    def exitJsonObject(self, ctx:HqlParser.JsonObjectContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonPair.
    def enterJsonPair(self, ctx:HqlParser.JsonPairContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonPair.
    def exitJsonPair(self, ctx:HqlParser.JsonPairContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonArray.
    def enterJsonArray(self, ctx:HqlParser.JsonArrayContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonArray.
    def exitJsonArray(self, ctx:HqlParser.JsonArrayContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonBoolean.
    def enterJsonBoolean(self, ctx:HqlParser.JsonBooleanContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonBoolean.
    def exitJsonBoolean(self, ctx:HqlParser.JsonBooleanContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonDateTime.
    def enterJsonDateTime(self, ctx:HqlParser.JsonDateTimeContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonDateTime.
    def exitJsonDateTime(self, ctx:HqlParser.JsonDateTimeContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonGuid.
    def enterJsonGuid(self, ctx:HqlParser.JsonGuidContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonGuid.
    def exitJsonGuid(self, ctx:HqlParser.JsonGuidContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonNull.
    def enterJsonNull(self, ctx:HqlParser.JsonNullContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonNull.
    def exitJsonNull(self, ctx:HqlParser.JsonNullContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonString.
    def enterJsonString(self, ctx:HqlParser.JsonStringContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonString.
    def exitJsonString(self, ctx:HqlParser.JsonStringContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonTimeSpan.
    def enterJsonTimeSpan(self, ctx:HqlParser.JsonTimeSpanContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonTimeSpan.
    def exitJsonTimeSpan(self, ctx:HqlParser.JsonTimeSpanContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonLong.
    def enterJsonLong(self, ctx:HqlParser.JsonLongContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonLong.
    def exitJsonLong(self, ctx:HqlParser.JsonLongContext):
        pass


    # Enter a parse tree produced by HqlParser#jsonReal.
    def enterJsonReal(self, ctx:HqlParser.JsonRealContext):
        pass

    # Exit a parse tree produced by HqlParser#jsonReal.
    def exitJsonReal(self, ctx:HqlParser.JsonRealContext):
        pass



del HqlParser