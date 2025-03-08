// Generated from /home/hashfastr/git/hash-query-language/grammar/Hql.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class HqlParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASTERISK=1, ATSIGN=2, BAR=3, CLOSEBRACE=4, CLOSEBRACKET=5, CLOSEBRACKET_DASH=6, 
		CLOSEBRACKET_DASH_GREATERTHAN=7, CLOSEPAREN=8, COMMA=9, COLON=10, DASH=11, 
		DASHDASH=12, DASHDASH_GREATERTHAN=13, DASH_OPENBRACKET=14, DOT=15, DOTDOT=16, 
		EQUAL=17, EQUALEQUAL=18, EQUALTILDE=19, EXCLAIMATIONPOINT_EQUAL=20, EXCLAIMATIONPOINT_TILDE=21, 
		GREATERTHAN=22, GREATERTHAN_EQUAL=23, LESSTHAN=24, LESSTHAN_DASHDASH=25, 
		LESSTHAN_DASH_OPENBRACKET=26, LESSTHAN_EQUAL=27, LESSTHAN_GREATERTHAN=28, 
		OPENBRACE=29, OPENBRACKET=30, OPENPAREN=31, PERCENTSIGN=32, PLUS=33, SEMICOLON=34, 
		SLASH=35, EQUAL_GREATERTHAN=36, CHART3D_=37, ACCESS=38, ACCUMULATE=39, 
		AGGREGATIONS=40, ALIAS=41, ALL=42, AND=43, ANOMALYCHART=44, ANOMALYCOLUMNS=45, 
		AREACHART=46, AS=47, ASC=48, ASSERTSCHEMA=49, AXES=50, BAGEXPANSION=51, 
		BARCHART=52, BASE=53, BETWEEN=54, BIN=55, BIN_LEGACY=56, BY=57, CARD=58, 
		CLUSTER=59, COLUMNCHART=60, CONSUME=61, CONTAINS=62, CONTAINSCS=63, CONTAINS_CS=64, 
		CONTEXTUAL_DATATABLE=65, COUNT=66, CROSSCLUSTER__=67, CROSSDB__=68, DATABASE=69, 
		DATASCOPE=70, DATATABLE=71, DECLARE=72, DECODEBLOCKS=73, DEFAULT=74, DELTA=75, 
		DESC=76, DISTINCT=77, EDGES=78, ENDSWITH=79, ENDSWITH_CS=80, ENTITYGROUP=81, 
		EVALUATE=82, EXECUTE=83, EXECUTE_AND_CACHE=84, EXPANDOUTPUT=85, EXTEND=86, 
		EXTERNALDATA=87, EXTERNAL_DATA=88, FACET=89, FILTER=90, FIND=91, FIRST=92, 
		FLAGS=93, FORK=94, FROM=95, GETSCHEMA=96, GRANNYASC=97, GRANNYDESC=98, 
		GRAPHMARKCOMPONENTS=99, GRAPHMATCH=100, GRAPHMERGE=101, GRAPHSHORTESTPATHS=102, 
		GRAPHTOTABLE=103, HAS=104, HAS_ALL=105, HAS_ANY=106, HAS_CS=107, HASPREFIX=108, 
		HASPREFIX_CS=109, HASSUFFIX=110, HASSUFFIX_CS=111, HIDDEN_=112, HINT_CONCURRENCY=113, 
		HINT_DISTRIBUTION=114, HINT_MATERIALIZED=115, HINT_NUM_PARTITIONS=116, 
		HINT_PASS_FILTERS=117, HINT_PASS_FILTERS_COLUMN=118, HINT_PROGRESSIVE_TOP=119, 
		HINT_REMOTE=120, HINT_SUFFLEKEY=121, HINT_SPREAD=122, HINT_STRATEGY=123, 
		HOT=124, HOTCACHE=125, HOTDATA=126, HOTINDEX=127, ID=128, ID__=129, IN=130, 
		IN_CI=131, INTO=132, INVOKE=133, ISFUZZY=134, ISFUZZY__=135, JOIN=136, 
		KIND=137, LADDERCHART=138, LAST=139, LEGEND=140, LET=141, LIKE=142, LIKECS=143, 
		LIMIT=144, LINEAR=145, LINECHART=146, LIST=147, LOOKUP=148, LOG=149, MACROEXPAND=150, 
		MAKEGRAPH=151, MAKESERIES=152, MAP=153, MATCHES_REGEX=154, MATERIALIZE=155, 
		MATERIALIZED_VIEW_COMBINE=156, MV_APPLY=157, MV_EXPAND=158, MVAPPLY=159, 
		MVEXPAND=160, NODES=161, NONE=162, NOOPTIMIZATION=163, NOT_BETWEEN=164, 
		NOT_CONTAINS=165, NOT_CONTAINS_CS=166, NOT_ENDSWITH_CS=167, NOT_ENDSWITH=168, 
		NOT_HAS=169, NOT_HAS_CS=170, NOT_HASPREFIX=171, NOT_HASPREFIX_CS=172, 
		NOT_HASSUFFIX=173, NOT_HASSUFFIX_CS=174, NOT_IN=175, NOT_IN_CI=176, NOT_STARTSWITH=177, 
		NOT_STARTSWITH_CS=178, NOTCONTAINS=179, NOTCONTAINSCS=180, NOTLIKE=181, 
		NOTLIKECS=182, NULL=183, NULLS=184, OF=185, ON=186, OPTIONAL=187, OR=188, 
		ORDER=189, OTHERS=190, OUTPUT=191, PACK=192, PANELS=193, PARSE=194, PARSEKV=195, 
		PARSEWHERE=196, PARTITION=197, PARTITIONBY=198, PARTITIONEDBY=199, PATTERN=200, 
		PACKEDCOLUMN__=201, PIECHART=202, PIVOTCHART=203, PLUGIN=204, PRINT=205, 
		PROJECT=206, PROJECTAWAY=207, PROJECTAWAY_=208, PROJECTKEEP=209, PROJECTRENAME=210, 
		PROJECTREORDER=211, PROJECTSMART=212, QUERYPARAMETERS=213, RANGE=214, 
		REDUCE=215, REGEX=216, RELAXED=217, RENDER=218, REPLACE=219, RESTRICT=220, 
		SAMPLE=221, SAMPLE_DISTINCT=222, SCAN=223, SCATTERCHART=224, SEARCH=225, 
		SERIALIZE=226, SERIES=227, SET=228, SIMPLE=229, SORT=230, SOURCECOLUMNINDEX__=231, 
		STACKED=232, STACKED100=233, STACKEDAREACHART=234, STARTSWITH=235, STARTSWITH_CS=236, 
		STEP=237, SUMMARIZE=238, TABLE=239, TAKE=240, THRESHOLD=241, TIMECHART=242, 
		TIMELINE=243, TIMEPIVOT=244, TITLE=245, TO=246, TOP=247, TOP_HITTERS=248, 
		TOP_NESTED=249, TOSCALAR=250, TOTABLE=251, TREEMAP=252, TYPEOF=253, UNION=254, 
		UNSTACKED=255, UUID=256, VIEW=257, VISIBLE=258, WHERE=259, WITH=260, WITHNOSOURCE__=261, 
		WITHSOURCE=262, WITH_ITEM_INDEX=263, WITH_MATCH_ID=264, WITH_NODE_ID=265, 
		WITH_SOURCE=266, WITH_STEP_NAME=267, XAXIS=268, XCOLUMN=269, XMAX=270, 
		XMIN=271, XTITLE=272, YAXIS=273, YCOLUMNS=274, YMAX=275, YMIN=276, YSPLIT=277, 
		YTITLE=278, BOOL=279, BOOLEAN=280, DATE=281, DATETIME=282, DECIMAL=283, 
		DOUBLE=284, DYNAMIC=285, FLOAT=286, GUID=287, INT=288, INT8=289, INT16=290, 
		INT32=291, INT64=292, LONG=293, STRING=294, REAL=295, TIME=296, TIMESPAN=297, 
		UINT=298, UINT8=299, UINT16=300, UINT32=301, UINT64=302, ULONG=303, UNIQUEID=304, 
		LONGLITERAL=305, INTLITERAL=306, REALLITERAL=307, DECIMALLITERAL=308, 
		STRINGLITERAL=309, BOOLEANLITERAL=310, DATETIMELITERAL=311, TIMESPANLITERAL=312, 
		TYPELITERAL=313, RAWGUIDLITERAL=314, GUIDLITERAL=315, IDENTIFIER=316, 
		WHITESPACE=317, COMMENT=318;
	public static final int
		RULE_top = 0, RULE_query = 1, RULE_statement = 2, RULE_aliasDatabaseStatement = 3, 
		RULE_letStatement = 4, RULE_letVariableDeclaration = 5, RULE_letFunctionDeclaration = 6, 
		RULE_letViewDeclaration = 7, RULE_letViewParameterList = 8, RULE_letMaterializeDeclaration = 9, 
		RULE_letEntityGroupDeclaration = 10, RULE_letFunctionParameterList = 11, 
		RULE_scalarParameter = 12, RULE_scalarParameterDefault = 13, RULE_tabularParameter = 14, 
		RULE_tabularParameterOpenSchema = 15, RULE_tabularParameterRowSchema = 16, 
		RULE_tabularParameterRowSchemaColumnDeclaration = 17, RULE_letFunctionBody = 18, 
		RULE_letFunctionBodyStatement = 19, RULE_declarePatternStatement = 20, 
		RULE_declarePatternDefinition = 21, RULE_declarePatternParameterList = 22, 
		RULE_declarePatternParameter = 23, RULE_declarePatternPathParameter = 24, 
		RULE_declarePatternRule = 25, RULE_declarePatternRuleArgumentList = 26, 
		RULE_declarePatternRulePathArgument = 27, RULE_declarePatternRuleArgument = 28, 
		RULE_declarePatternBody = 29, RULE_restrictAccessStatement = 30, RULE_restrictAccessStatementEntity = 31, 
		RULE_setStatement = 32, RULE_setStatementOptionValue = 33, RULE_declareQueryParametersStatement = 34, 
		RULE_declareQueryParametersStatementParameter = 35, RULE_queryStatement = 36, 
		RULE_expression = 37, RULE_pipeExpression = 38, RULE_pipedOperator = 39, 
		RULE_pipeSubExpression = 40, RULE_beforePipeExpression = 41, RULE_afterPipeOperator = 42, 
		RULE_beforeOrAfterPipeOperator = 43, RULE_forkPipeOperator = 44, RULE_asOperator = 45, 
		RULE_assertSchemaOperator = 46, RULE_consumeOperator = 47, RULE_countOperator = 48, 
		RULE_countOperatorAsClause = 49, RULE_distinctOperator = 50, RULE_distinctOperatorStarTarget = 51, 
		RULE_distinctOperatorColumnListTarget = 52, RULE_evaluateOperator = 53, 
		RULE_evaluateOperatorSchemaClause = 54, RULE_extendOperator = 55, RULE_executeAndCacheOperator = 56, 
		RULE_facetByOperator = 57, RULE_facetByOperatorWithOperatorClause = 58, 
		RULE_facetByOperatorWithExpressionClause = 59, RULE_findOperator = 60, 
		RULE_findOperatorParametersWhereClause = 61, RULE_findOperatorInClause = 62, 
		RULE_findOperatorProjectClause = 63, RULE_findOperatorProjectExpression = 64, 
		RULE_findOperatorColumnExpression = 65, RULE_findOperatorOptionalColumnType = 66, 
		RULE_findOperatorPackExpression = 67, RULE_findOperatorProjectSmartClause = 68, 
		RULE_findOperatorProjectAwayClause = 69, RULE_findOperatorProjectAwayStar = 70, 
		RULE_findOperatorProjectAwayColumnList = 71, RULE_findOperatorSource = 72, 
		RULE_findOperatorSourceEntityExpression = 73, RULE_forkOperator = 74, 
		RULE_forkOperatorFork = 75, RULE_forkOperatorExpressionName = 76, RULE_forkOperatorExpression = 77, 
		RULE_forkOperatorPipedOperator = 78, RULE_getSchemaOperator = 79, RULE_graphMarkComponentsOperator = 80, 
		RULE_graphMatchOperator = 81, RULE_graphMatchPattern = 82, RULE_graphMatchPatternNode = 83, 
		RULE_graphMatchPatternUnnamedEdge = 84, RULE_graphMatchPatternNamedEdge = 85, 
		RULE_graphMatchPatternRange = 86, RULE_graphMatchWhereClause = 87, RULE_graphMatchProjectClause = 88, 
		RULE_graphMergeOperator = 89, RULE_graphToTableOperator = 90, RULE_graphToTableOutput = 91, 
		RULE_graphToTableAsClause = 92, RULE_graphShortestPathsOperator = 93, 
		RULE_invokeOperator = 94, RULE_joinOperator = 95, RULE_joinOperatorOnClause = 96, 
		RULE_joinOperatorWhereClause = 97, RULE_lookupOperator = 98, RULE_macroExpandOperator = 99, 
		RULE_macroExpandEntityGroup = 100, RULE_entityGroupExpression = 101, RULE_makeGraphOperator = 102, 
		RULE_makeGraphIdClause = 103, RULE_makeGraphTablesAndKeysClause = 104, 
		RULE_makeGraphPartitionedByClause = 105, RULE_makeSeriesOperator = 106, 
		RULE_makeSeriesOperatorOnClause = 107, RULE_makeSeriesOperatorAggregation = 108, 
		RULE_makeSeriesOperatorExpressionDefaultClause = 109, RULE_makeSeriesOperatorInRangeClause = 110, 
		RULE_makeSeriesOperatorFromToStepClause = 111, RULE_makeSeriesOperatorByClause = 112, 
		RULE_mvapplyOperator = 113, RULE_mvapplyOperatorLimitClause = 114, RULE_mvapplyOperatorIdClause = 115, 
		RULE_mvapplyOperatorExpression = 116, RULE_mvapplyOperatorExpressionToClause = 117, 
		RULE_mvexpandOperator = 118, RULE_mvexpandOperatorExpression = 119, RULE_parseOperator = 120, 
		RULE_parseOperatorKindClause = 121, RULE_parseOperatorFlagsClause = 122, 
		RULE_parseOperatorNameAndOptionalType = 123, RULE_parseOperatorPattern = 124, 
		RULE_parseOperatorPatternSegment = 125, RULE_parseWhereOperator = 126, 
		RULE_parseKvOperator = 127, RULE_parseKvWithClause = 128, RULE_partitionOperator = 129, 
		RULE_partitionOperatorInClause = 130, RULE_partitionOperatorSubExpressionBody = 131, 
		RULE_partitionOperatorFullExpressionBody = 132, RULE_partitionByOperator = 133, 
		RULE_partitionByOperatorIdClause = 134, RULE_printOperator = 135, RULE_projectAwayOperator = 136, 
		RULE_projectKeepOperator = 137, RULE_projectOperator = 138, RULE_projectRenameOperator = 139, 
		RULE_projectReorderOperator = 140, RULE_projectReorderExpression = 141, 
		RULE_reduceByOperator = 142, RULE_reduceByWithClause = 143, RULE_renderOperator = 144, 
		RULE_renderOperatorWithClause = 145, RULE_renderOperatorLegacyPropertyList = 146, 
		RULE_renderOperatorProperty = 147, RULE_renderPropertyNameList = 148, 
		RULE_renderOperatorLegacyProperty = 149, RULE_sampleDistinctOperator = 150, 
		RULE_sampleOperator = 151, RULE_scanOperator = 152, RULE_scanOperatorOrderByClause = 153, 
		RULE_scanOperatorPartitionByClause = 154, RULE_scanOperatorDeclareClause = 155, 
		RULE_scanOperatorStep = 156, RULE_scanOperatorStepOutputClause = 157, 
		RULE_scanOperatorBody = 158, RULE_scanOperatorAssignment = 159, RULE_searchOperator = 160, 
		RULE_searchOperatorStarAndExpression = 161, RULE_searchOperatorInClause = 162, 
		RULE_serializeOperator = 163, RULE_sortOperator = 164, RULE_orderedExpression = 165, 
		RULE_sortOrdering = 166, RULE_summarizeOperator = 167, RULE_summarizeOperatorByClause = 168, 
		RULE_summarizeOperatorLegacyBinClause = 169, RULE_takeOperator = 170, 
		RULE_topOperator = 171, RULE_topHittersOperator = 172, RULE_topHittersOperatorByClause = 173, 
		RULE_topNestedOperator = 174, RULE_topNestedOperatorPart = 175, RULE_topNestedOperatorWithOthersClause = 176, 
		RULE_unionOperator = 177, RULE_unionOperatorExpression = 178, RULE_whereOperator = 179, 
		RULE_contextualSubExpression = 180, RULE_contextualPipeExpression = 181, 
		RULE_contextualPipeExpressionPipedOperator = 182, RULE_strictQueryOperatorParameter = 183, 
		RULE_relaxedQueryOperatorParameter = 184, RULE_queryOperatorProperty = 185, 
		RULE_namedExpression = 186, RULE_namedExpressionNameClause = 187, RULE_namedExpressionNameList = 188, 
		RULE_scopedFunctionCallExpression = 189, RULE_unnamedExpression = 190, 
		RULE_logicalOrExpression = 191, RULE_logicalOrOperation = 192, RULE_logicalAndExpression = 193, 
		RULE_logicalAndOperation = 194, RULE_equalityExpression = 195, RULE_equalsEqualityExpression = 196, 
		RULE_listEqualityExpression = 197, RULE_betweenEqualityExpression = 198, 
		RULE_starEqualityExpression = 199, RULE_relationalExpression = 200, RULE_additiveExpression = 201, 
		RULE_additiveOperation = 202, RULE_multiplicativeExpression = 203, RULE_multiplicativeOperation = 204, 
		RULE_stringOperatorExpression = 205, RULE_stringBinaryOperatorExpression = 206, 
		RULE_stringBinaryOperation = 207, RULE_stringBinaryOperator = 208, RULE_stringStarOperatorExpression = 209, 
		RULE_invocationExpression = 210, RULE_functionCallOrPathExpression = 211, 
		RULE_functionCallOrPathRoot = 212, RULE_functionCallOrPathPathExpression = 213, 
		RULE_functionCallOrPathOperation = 214, RULE_functionalCallOrPathPathOperation = 215, 
		RULE_functionCallOrPathElementOperation = 216, RULE_legacyFunctionCallOrPathElementOperation = 217, 
		RULE_toScalarExpression = 218, RULE_toTableExpression = 219, RULE_noOptimizationParameter = 220, 
		RULE_dotCompositeFunctionCallExpression = 221, RULE_dotCompositeFunctionCallOperation = 222, 
		RULE_functionCallExpression = 223, RULE_namedFunctionCallExpression = 224, 
		RULE_argumentExpression = 225, RULE_countExpression = 226, RULE_starExpression = 227, 
		RULE_primaryExpression = 228, RULE_nameReferenceWithDataScope = 229, RULE_dataScopeClause = 230, 
		RULE_parenthesizedExpression = 231, RULE_rangeExpression = 232, RULE_entityExpression = 233, 
		RULE_entityPathOrElementExpression = 234, RULE_entityPathOrElementOperator = 235, 
		RULE_entityPathOperator = 236, RULE_entityElementOperator = 237, RULE_legacyEntityPathElementOperator = 238, 
		RULE_entityName = 239, RULE_entityNameReference = 240, RULE_atSignName = 241, 
		RULE_extendedPathName = 242, RULE_wildcardedEntityExpression = 243, RULE_wildcardedPathExpression = 244, 
		RULE_wildcardedPathName = 245, RULE_contextualDataTableExpression = 246, 
		RULE_dataTableExpression = 247, RULE_rowSchema = 248, RULE_rowSchemaColumnDeclaration = 249, 
		RULE_externalDataExpression = 250, RULE_externalDataWithClause = 251, 
		RULE_externalDataWithClauseProperty = 252, RULE_materializedViewCombineExpression = 253, 
		RULE_materializeViewCombineBaseClause = 254, RULE_materializedViewCombineDeltaClause = 255, 
		RULE_materializedViewCombineAggregationsClause = 256, RULE_scalarType = 257, 
		RULE_extendedScalarType = 258, RULE_parameterName = 259, RULE_simpleNameReference = 260, 
		RULE_extendedNameReference = 261, RULE_wildcardedNameReference = 262, 
		RULE_simpleOrWildcardedNameReference = 263, RULE_identifierName = 264, 
		RULE_keywordName = 265, RULE_extendedKeywordName = 266, RULE_escapedName = 267, 
		RULE_identifierOrKeywordName = 268, RULE_identifierOrKeywordOrEscapedName = 269, 
		RULE_identifierOrExtendedKeywordOrEscapedName = 270, RULE_identifierOrExtendedKeywordName = 271, 
		RULE_wildcardedName = 272, RULE_wildcardedNamePrefix = 273, RULE_wildcardedNameSegment = 274, 
		RULE_literalExpression = 275, RULE_unsignedLiteralExpression = 276, RULE_numberLikeLiteralExpression = 277, 
		RULE_numericLiteralExpression = 278, RULE_signedLiteralExpression = 279, 
		RULE_longLiteralExpression = 280, RULE_intLiteralExpression = 281, RULE_realLiteralExpression = 282, 
		RULE_decimalLiteralExpression = 283, RULE_dateTimeLiteralExpression = 284, 
		RULE_timeSpanLiteralExpression = 285, RULE_booleanLiteralExpression = 286, 
		RULE_guidLiteralExpression = 287, RULE_typeLiteralExpression = 288, RULE_signedLongLiteralExpression = 289, 
		RULE_signedRealLiteralExpression = 290, RULE_stringLiteralExpression = 291, 
		RULE_dynamicLiteralExpression = 292, RULE_jsonValue = 293, RULE_jsonObject = 294, 
		RULE_jsonPair = 295, RULE_jsonArray = 296, RULE_jsonBoolean = 297, RULE_jsonDateTime = 298, 
		RULE_jsonGuid = 299, RULE_jsonNull = 300, RULE_jsonString = 301, RULE_jsonTimeSpan = 302, 
		RULE_jsonLong = 303, RULE_jsonReal = 304;
	private static String[] makeRuleNames() {
		return new String[] {
			"top", "query", "statement", "aliasDatabaseStatement", "letStatement", 
			"letVariableDeclaration", "letFunctionDeclaration", "letViewDeclaration", 
			"letViewParameterList", "letMaterializeDeclaration", "letEntityGroupDeclaration", 
			"letFunctionParameterList", "scalarParameter", "scalarParameterDefault", 
			"tabularParameter", "tabularParameterOpenSchema", "tabularParameterRowSchema", 
			"tabularParameterRowSchemaColumnDeclaration", "letFunctionBody", "letFunctionBodyStatement", 
			"declarePatternStatement", "declarePatternDefinition", "declarePatternParameterList", 
			"declarePatternParameter", "declarePatternPathParameter", "declarePatternRule", 
			"declarePatternRuleArgumentList", "declarePatternRulePathArgument", "declarePatternRuleArgument", 
			"declarePatternBody", "restrictAccessStatement", "restrictAccessStatementEntity", 
			"setStatement", "setStatementOptionValue", "declareQueryParametersStatement", 
			"declareQueryParametersStatementParameter", "queryStatement", "expression", 
			"pipeExpression", "pipedOperator", "pipeSubExpression", "beforePipeExpression", 
			"afterPipeOperator", "beforeOrAfterPipeOperator", "forkPipeOperator", 
			"asOperator", "assertSchemaOperator", "consumeOperator", "countOperator", 
			"countOperatorAsClause", "distinctOperator", "distinctOperatorStarTarget", 
			"distinctOperatorColumnListTarget", "evaluateOperator", "evaluateOperatorSchemaClause", 
			"extendOperator", "executeAndCacheOperator", "facetByOperator", "facetByOperatorWithOperatorClause", 
			"facetByOperatorWithExpressionClause", "findOperator", "findOperatorParametersWhereClause", 
			"findOperatorInClause", "findOperatorProjectClause", "findOperatorProjectExpression", 
			"findOperatorColumnExpression", "findOperatorOptionalColumnType", "findOperatorPackExpression", 
			"findOperatorProjectSmartClause", "findOperatorProjectAwayClause", "findOperatorProjectAwayStar", 
			"findOperatorProjectAwayColumnList", "findOperatorSource", "findOperatorSourceEntityExpression", 
			"forkOperator", "forkOperatorFork", "forkOperatorExpressionName", "forkOperatorExpression", 
			"forkOperatorPipedOperator", "getSchemaOperator", "graphMarkComponentsOperator", 
			"graphMatchOperator", "graphMatchPattern", "graphMatchPatternNode", "graphMatchPatternUnnamedEdge", 
			"graphMatchPatternNamedEdge", "graphMatchPatternRange", "graphMatchWhereClause", 
			"graphMatchProjectClause", "graphMergeOperator", "graphToTableOperator", 
			"graphToTableOutput", "graphToTableAsClause", "graphShortestPathsOperator", 
			"invokeOperator", "joinOperator", "joinOperatorOnClause", "joinOperatorWhereClause", 
			"lookupOperator", "macroExpandOperator", "macroExpandEntityGroup", "entityGroupExpression", 
			"makeGraphOperator", "makeGraphIdClause", "makeGraphTablesAndKeysClause", 
			"makeGraphPartitionedByClause", "makeSeriesOperator", "makeSeriesOperatorOnClause", 
			"makeSeriesOperatorAggregation", "makeSeriesOperatorExpressionDefaultClause", 
			"makeSeriesOperatorInRangeClause", "makeSeriesOperatorFromToStepClause", 
			"makeSeriesOperatorByClause", "mvapplyOperator", "mvapplyOperatorLimitClause", 
			"mvapplyOperatorIdClause", "mvapplyOperatorExpression", "mvapplyOperatorExpressionToClause", 
			"mvexpandOperator", "mvexpandOperatorExpression", "parseOperator", "parseOperatorKindClause", 
			"parseOperatorFlagsClause", "parseOperatorNameAndOptionalType", "parseOperatorPattern", 
			"parseOperatorPatternSegment", "parseWhereOperator", "parseKvOperator", 
			"parseKvWithClause", "partitionOperator", "partitionOperatorInClause", 
			"partitionOperatorSubExpressionBody", "partitionOperatorFullExpressionBody", 
			"partitionByOperator", "partitionByOperatorIdClause", "printOperator", 
			"projectAwayOperator", "projectKeepOperator", "projectOperator", "projectRenameOperator", 
			"projectReorderOperator", "projectReorderExpression", "reduceByOperator", 
			"reduceByWithClause", "renderOperator", "renderOperatorWithClause", "renderOperatorLegacyPropertyList", 
			"renderOperatorProperty", "renderPropertyNameList", "renderOperatorLegacyProperty", 
			"sampleDistinctOperator", "sampleOperator", "scanOperator", "scanOperatorOrderByClause", 
			"scanOperatorPartitionByClause", "scanOperatorDeclareClause", "scanOperatorStep", 
			"scanOperatorStepOutputClause", "scanOperatorBody", "scanOperatorAssignment", 
			"searchOperator", "searchOperatorStarAndExpression", "searchOperatorInClause", 
			"serializeOperator", "sortOperator", "orderedExpression", "sortOrdering", 
			"summarizeOperator", "summarizeOperatorByClause", "summarizeOperatorLegacyBinClause", 
			"takeOperator", "topOperator", "topHittersOperator", "topHittersOperatorByClause", 
			"topNestedOperator", "topNestedOperatorPart", "topNestedOperatorWithOthersClause", 
			"unionOperator", "unionOperatorExpression", "whereOperator", "contextualSubExpression", 
			"contextualPipeExpression", "contextualPipeExpressionPipedOperator", 
			"strictQueryOperatorParameter", "relaxedQueryOperatorParameter", "queryOperatorProperty", 
			"namedExpression", "namedExpressionNameClause", "namedExpressionNameList", 
			"scopedFunctionCallExpression", "unnamedExpression", "logicalOrExpression", 
			"logicalOrOperation", "logicalAndExpression", "logicalAndOperation", 
			"equalityExpression", "equalsEqualityExpression", "listEqualityExpression", 
			"betweenEqualityExpression", "starEqualityExpression", "relationalExpression", 
			"additiveExpression", "additiveOperation", "multiplicativeExpression", 
			"multiplicativeOperation", "stringOperatorExpression", "stringBinaryOperatorExpression", 
			"stringBinaryOperation", "stringBinaryOperator", "stringStarOperatorExpression", 
			"invocationExpression", "functionCallOrPathExpression", "functionCallOrPathRoot", 
			"functionCallOrPathPathExpression", "functionCallOrPathOperation", "functionalCallOrPathPathOperation", 
			"functionCallOrPathElementOperation", "legacyFunctionCallOrPathElementOperation", 
			"toScalarExpression", "toTableExpression", "noOptimizationParameter", 
			"dotCompositeFunctionCallExpression", "dotCompositeFunctionCallOperation", 
			"functionCallExpression", "namedFunctionCallExpression", "argumentExpression", 
			"countExpression", "starExpression", "primaryExpression", "nameReferenceWithDataScope", 
			"dataScopeClause", "parenthesizedExpression", "rangeExpression", "entityExpression", 
			"entityPathOrElementExpression", "entityPathOrElementOperator", "entityPathOperator", 
			"entityElementOperator", "legacyEntityPathElementOperator", "entityName", 
			"entityNameReference", "atSignName", "extendedPathName", "wildcardedEntityExpression", 
			"wildcardedPathExpression", "wildcardedPathName", "contextualDataTableExpression", 
			"dataTableExpression", "rowSchema", "rowSchemaColumnDeclaration", "externalDataExpression", 
			"externalDataWithClause", "externalDataWithClauseProperty", "materializedViewCombineExpression", 
			"materializeViewCombineBaseClause", "materializedViewCombineDeltaClause", 
			"materializedViewCombineAggregationsClause", "scalarType", "extendedScalarType", 
			"parameterName", "simpleNameReference", "extendedNameReference", "wildcardedNameReference", 
			"simpleOrWildcardedNameReference", "identifierName", "keywordName", "extendedKeywordName", 
			"escapedName", "identifierOrKeywordName", "identifierOrKeywordOrEscapedName", 
			"identifierOrExtendedKeywordOrEscapedName", "identifierOrExtendedKeywordName", 
			"wildcardedName", "wildcardedNamePrefix", "wildcardedNameSegment", "literalExpression", 
			"unsignedLiteralExpression", "numberLikeLiteralExpression", "numericLiteralExpression", 
			"signedLiteralExpression", "longLiteralExpression", "intLiteralExpression", 
			"realLiteralExpression", "decimalLiteralExpression", "dateTimeLiteralExpression", 
			"timeSpanLiteralExpression", "booleanLiteralExpression", "guidLiteralExpression", 
			"typeLiteralExpression", "signedLongLiteralExpression", "signedRealLiteralExpression", 
			"stringLiteralExpression", "dynamicLiteralExpression", "jsonValue", "jsonObject", 
			"jsonPair", "jsonArray", "jsonBoolean", "jsonDateTime", "jsonGuid", "jsonNull", 
			"jsonString", "jsonTimeSpan", "jsonLong", "jsonReal"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", "'@'", "'|'", "'}'", "']'", "']-'", "']->'", "')'", "','", 
			"':'", "'-'", "'--'", "'-->'", "'-['", "'.'", "'..'", "'='", "'=='", 
			"'=~'", "'!='", "'!~'", "'>'", "'>='", "'<'", "'<--'", "'<-['", "'<='", 
			"'<>'", "'{'", "'['", "'('", "'%'", "'+'", "';'", "'/'", "'=>'", "'3Dchart'", 
			"'access'", "'accumulate'", "'aggregations'", "'alias'", "'all'", "'and'", 
			"'anomalychart'", "'anomalycolumns'", "'areachart'", "'as'", "'asc'", 
			"'assert-schema'", "'axes'", "'bagexpansion'", "'barchart'", "'base'", 
			"'between'", "'bin'", "'bin_legacy'", "'by'", "'card'", "'cluster'", 
			"'columnchart'", "'consume'", "'contains'", "'containscs'", "'contains_cs'", 
			"'__contextual_datatable'", "'count'", "'__crossCluster'", "'__crossDB'", 
			"'database'", "'datascope'", "'datatable'", "'declare'", "'decodeblocks'", 
			"'default'", "'delta'", "'desc'", "'distinct'", "'edges'", "'endswith'", 
			"'endswith_cs'", "'entity_group'", "'evaluate'", "'execute'", "'__executeAndCache'", 
			"'expandoutput'", "'extend'", "'externaldata'", "'external_data'", "'facet'", 
			"'filter'", "'find'", "'first'", "'flags'", "'fork'", "'from'", "'getschema'", 
			"'granny-asc'", "'granny-desc'", "'graph-mark-components'", "'graph-match'", 
			"'graph-merge'", "'graph-shortest-paths'", "'graph-to-table'", "'has'", 
			"'has_all'", "'has_any'", "'has_cs'", "'hasprefix'", "'hasprefix_cs'", 
			"'hassuffix'", "'hassuffix_cs'", "'hidden'", "'hint.concurrency'", "'hint.distribution'", 
			"'hint.materialized'", "'hint.num_partitions'", "'hint.pass_filters'", 
			"'hint.pass_filters_column'", "'hint.progressive_top'", "'hint.remote'", 
			"'hint.shufflekey'", "'hint.spread'", "'hint.strategy'", "'hot'", "'hotcache'", 
			"'hotdata'", "'hotindex'", "'id'", "'__id'", "'in'", "'in~'", "'into'", 
			"'invoke'", "'isfuzzy'", "'__isFuzzy'", "'join'", "'kind'", "'ladderchart'", 
			"'last'", "'legend'", "'let'", "'like'", "'likecs'", "'limit'", "'linear'", 
			"'linechart'", "'list'", "'lookup'", "'log'", "'macro-expand'", "'make-graph'", 
			"'make-series'", "'map'", "'matches regex'", "'materialize'", "'materialized-view-combine'", 
			"'mv-apply'", "'mv-expand'", "'mvapply'", "'mvexpand'", "'nodes'", "'none'", 
			"'nooptimization'", "'!between'", "'!contains'", "'!contains_cs'", "'!endswith_cs'", 
			"'!endswith'", "'!has'", "'!has_cs'", "'!hasprefix'", "'!hasprefix_cs'", 
			"'!hassuffix'", "'!hassuffix_cs'", "'!in'", "'!in~'", "'!startswith'", 
			"'!startswith_cs'", "'notcontains'", "'notcontainscs'", "'notlike'", 
			"'notlikecs'", "'null'", "'nulls'", "'of'", "'on'", "'optional'", "'or'", 
			"'order'", "'others'", "'output'", "'pack'", "'panels'", "'parse'", "'parse-kv'", 
			"'parse-where'", "'partition'", "'__partitionby'", "'partitioned-by'", 
			"'pattern'", "'__packedColumn'", "'piechart'", "'pivotchart'", "'plugin'", 
			"'print'", "'project'", "'project-away'", "'__projectAway'", "'project-keep'", 
			"'project-rename'", "'project-reorder'", "'project-smart'", "'query_parameters'", 
			"'range'", "'reduce'", "'regex'", "'relaxed'", "'render'", "'replace'", 
			"'restrict'", "'sample'", "'sample-distinct'", "'scan'", "'scatterchart'", 
			"'search'", "'serialize'", "'series'", "'set'", "'simple'", "'sort'", 
			"'__sourceColumnIndex'", "'stacked'", "'stacked100'", "'stackedareachart'", 
			"'startswith'", "'startswith_cs'", "'step'", "'summarize'", "'table'", 
			"'take'", "'threshold'", "'timechart'", "'timeline'", "'timepivot'", 
			"'title'", "'to'", "'top'", "'top-hitters'", "'top-nested'", "'toscalar'", 
			"'totable'", "'treemap'", "'typeof'", "'union'", "'unstacked'", "'uuid'", 
			"'view'", "'visible'", "'where'", "'with'", "'__noWithSource'", "'withsource'", 
			"'with_itemindex'", "'with_match_id'", "'with_node_id'", "'with_source'", 
			"'with_step_name'", "'xaxis'", "'xcolumn'", "'xmax'", "'xmin'", "'xtitle'", 
			"'yaxis'", "'ycolumns'", "'ymax'", "'ymin'", "'ysplit'", "'ytitle'", 
			"'bool'", "'boolean'", "'date'", "'datetime'", "'decimal'", "'double'", 
			"'dynamic'", "'float'", "'guid'", "'int'", "'int8'", "'int16'", "'int32'", 
			"'int64'", "'long'", "'string'", "'real'", "'time'", "'timespan'", "'uint'", 
			"'uint8'", "'uint16'", "'uint32'", "'uint64'", "'ulong'", "'uniqueid'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASTERISK", "ATSIGN", "BAR", "CLOSEBRACE", "CLOSEBRACKET", "CLOSEBRACKET_DASH", 
			"CLOSEBRACKET_DASH_GREATERTHAN", "CLOSEPAREN", "COMMA", "COLON", "DASH", 
			"DASHDASH", "DASHDASH_GREATERTHAN", "DASH_OPENBRACKET", "DOT", "DOTDOT", 
			"EQUAL", "EQUALEQUAL", "EQUALTILDE", "EXCLAIMATIONPOINT_EQUAL", "EXCLAIMATIONPOINT_TILDE", 
			"GREATERTHAN", "GREATERTHAN_EQUAL", "LESSTHAN", "LESSTHAN_DASHDASH", 
			"LESSTHAN_DASH_OPENBRACKET", "LESSTHAN_EQUAL", "LESSTHAN_GREATERTHAN", 
			"OPENBRACE", "OPENBRACKET", "OPENPAREN", "PERCENTSIGN", "PLUS", "SEMICOLON", 
			"SLASH", "EQUAL_GREATERTHAN", "CHART3D_", "ACCESS", "ACCUMULATE", "AGGREGATIONS", 
			"ALIAS", "ALL", "AND", "ANOMALYCHART", "ANOMALYCOLUMNS", "AREACHART", 
			"AS", "ASC", "ASSERTSCHEMA", "AXES", "BAGEXPANSION", "BARCHART", "BASE", 
			"BETWEEN", "BIN", "BIN_LEGACY", "BY", "CARD", "CLUSTER", "COLUMNCHART", 
			"CONSUME", "CONTAINS", "CONTAINSCS", "CONTAINS_CS", "CONTEXTUAL_DATATABLE", 
			"COUNT", "CROSSCLUSTER__", "CROSSDB__", "DATABASE", "DATASCOPE", "DATATABLE", 
			"DECLARE", "DECODEBLOCKS", "DEFAULT", "DELTA", "DESC", "DISTINCT", "EDGES", 
			"ENDSWITH", "ENDSWITH_CS", "ENTITYGROUP", "EVALUATE", "EXECUTE", "EXECUTE_AND_CACHE", 
			"EXPANDOUTPUT", "EXTEND", "EXTERNALDATA", "EXTERNAL_DATA", "FACET", "FILTER", 
			"FIND", "FIRST", "FLAGS", "FORK", "FROM", "GETSCHEMA", "GRANNYASC", "GRANNYDESC", 
			"GRAPHMARKCOMPONENTS", "GRAPHMATCH", "GRAPHMERGE", "GRAPHSHORTESTPATHS", 
			"GRAPHTOTABLE", "HAS", "HAS_ALL", "HAS_ANY", "HAS_CS", "HASPREFIX", "HASPREFIX_CS", 
			"HASSUFFIX", "HASSUFFIX_CS", "HIDDEN_", "HINT_CONCURRENCY", "HINT_DISTRIBUTION", 
			"HINT_MATERIALIZED", "HINT_NUM_PARTITIONS", "HINT_PASS_FILTERS", "HINT_PASS_FILTERS_COLUMN", 
			"HINT_PROGRESSIVE_TOP", "HINT_REMOTE", "HINT_SUFFLEKEY", "HINT_SPREAD", 
			"HINT_STRATEGY", "HOT", "HOTCACHE", "HOTDATA", "HOTINDEX", "ID", "ID__", 
			"IN", "IN_CI", "INTO", "INVOKE", "ISFUZZY", "ISFUZZY__", "JOIN", "KIND", 
			"LADDERCHART", "LAST", "LEGEND", "LET", "LIKE", "LIKECS", "LIMIT", "LINEAR", 
			"LINECHART", "LIST", "LOOKUP", "LOG", "MACROEXPAND", "MAKEGRAPH", "MAKESERIES", 
			"MAP", "MATCHES_REGEX", "MATERIALIZE", "MATERIALIZED_VIEW_COMBINE", "MV_APPLY", 
			"MV_EXPAND", "MVAPPLY", "MVEXPAND", "NODES", "NONE", "NOOPTIMIZATION", 
			"NOT_BETWEEN", "NOT_CONTAINS", "NOT_CONTAINS_CS", "NOT_ENDSWITH_CS", 
			"NOT_ENDSWITH", "NOT_HAS", "NOT_HAS_CS", "NOT_HASPREFIX", "NOT_HASPREFIX_CS", 
			"NOT_HASSUFFIX", "NOT_HASSUFFIX_CS", "NOT_IN", "NOT_IN_CI", "NOT_STARTSWITH", 
			"NOT_STARTSWITH_CS", "NOTCONTAINS", "NOTCONTAINSCS", "NOTLIKE", "NOTLIKECS", 
			"NULL", "NULLS", "OF", "ON", "OPTIONAL", "OR", "ORDER", "OTHERS", "OUTPUT", 
			"PACK", "PANELS", "PARSE", "PARSEKV", "PARSEWHERE", "PARTITION", "PARTITIONBY", 
			"PARTITIONEDBY", "PATTERN", "PACKEDCOLUMN__", "PIECHART", "PIVOTCHART", 
			"PLUGIN", "PRINT", "PROJECT", "PROJECTAWAY", "PROJECTAWAY_", "PROJECTKEEP", 
			"PROJECTRENAME", "PROJECTREORDER", "PROJECTSMART", "QUERYPARAMETERS", 
			"RANGE", "REDUCE", "REGEX", "RELAXED", "RENDER", "REPLACE", "RESTRICT", 
			"SAMPLE", "SAMPLE_DISTINCT", "SCAN", "SCATTERCHART", "SEARCH", "SERIALIZE", 
			"SERIES", "SET", "SIMPLE", "SORT", "SOURCECOLUMNINDEX__", "STACKED", 
			"STACKED100", "STACKEDAREACHART", "STARTSWITH", "STARTSWITH_CS", "STEP", 
			"SUMMARIZE", "TABLE", "TAKE", "THRESHOLD", "TIMECHART", "TIMELINE", "TIMEPIVOT", 
			"TITLE", "TO", "TOP", "TOP_HITTERS", "TOP_NESTED", "TOSCALAR", "TOTABLE", 
			"TREEMAP", "TYPEOF", "UNION", "UNSTACKED", "UUID", "VIEW", "VISIBLE", 
			"WHERE", "WITH", "WITHNOSOURCE__", "WITHSOURCE", "WITH_ITEM_INDEX", "WITH_MATCH_ID", 
			"WITH_NODE_ID", "WITH_SOURCE", "WITH_STEP_NAME", "XAXIS", "XCOLUMN", 
			"XMAX", "XMIN", "XTITLE", "YAXIS", "YCOLUMNS", "YMAX", "YMIN", "YSPLIT", 
			"YTITLE", "BOOL", "BOOLEAN", "DATE", "DATETIME", "DECIMAL", "DOUBLE", 
			"DYNAMIC", "FLOAT", "GUID", "INT", "INT8", "INT16", "INT32", "INT64", 
			"LONG", "STRING", "REAL", "TIME", "TIMESPAN", "UINT", "UINT8", "UINT16", 
			"UINT32", "UINT64", "ULONG", "UNIQUEID", "LONGLITERAL", "INTLITERAL", 
			"REALLITERAL", "DECIMALLITERAL", "STRINGLITERAL", "BOOLEANLITERAL", "DATETIMELITERAL", 
			"TIMESPANLITERAL", "TYPELITERAL", "RAWGUIDLITERAL", "GUIDLITERAL", "IDENTIFIER", 
			"WHITESPACE", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Hql.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public HqlParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopContext extends ParserRuleContext {
		public QueryContext query() {
			return getRuleContext(QueryContext.class,0);
		}
		public TopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_top; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTop(this);
		}
	}

	public final TopContext top() throws RecognitionException {
		TopContext _localctx = new TopContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_top);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(610);
			query();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryContext extends ParserRuleContext {
		public StatementContext statement;
		public List<StatementContext> Statements = new ArrayList<StatementContext>();
		public TerminalNode EOF() { return getToken(HqlParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(HqlParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(HqlParser.SEMICOLON, i);
		}
		public QueryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_query; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterQuery(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitQuery(this);
		}
	}

	public final QueryContext query() throws RecognitionException {
		QueryContext _localctx = new QueryContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_query);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(612);
			((QueryContext)_localctx).statement = statement();
			((QueryContext)_localctx).Statements.add(((QueryContext)_localctx).statement);
			setState(617);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(613);
					match(SEMICOLON);
					setState(614);
					((QueryContext)_localctx).statement = statement();
					((QueryContext)_localctx).Statements.add(((QueryContext)_localctx).statement);
					}
					} 
				}
				setState(619);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(621);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(620);
				match(SEMICOLON);
				}
			}

			setState(623);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public AliasDatabaseStatementContext AliasDatabase;
		public DeclarePatternStatementContext DeclarePattern;
		public DeclareQueryParametersStatementContext DeclareQueryParameters;
		public LetStatementContext Let;
		public QueryStatementContext Query;
		public RestrictAccessStatementContext RestrictAccess;
		public SetStatementContext Set;
		public AliasDatabaseStatementContext aliasDatabaseStatement() {
			return getRuleContext(AliasDatabaseStatementContext.class,0);
		}
		public DeclarePatternStatementContext declarePatternStatement() {
			return getRuleContext(DeclarePatternStatementContext.class,0);
		}
		public DeclareQueryParametersStatementContext declareQueryParametersStatement() {
			return getRuleContext(DeclareQueryParametersStatementContext.class,0);
		}
		public LetStatementContext letStatement() {
			return getRuleContext(LetStatementContext.class,0);
		}
		public QueryStatementContext queryStatement() {
			return getRuleContext(QueryStatementContext.class,0);
		}
		public RestrictAccessStatementContext restrictAccessStatement() {
			return getRuleContext(RestrictAccessStatementContext.class,0);
		}
		public SetStatementContext setStatement() {
			return getRuleContext(SetStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(632);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(625);
				((StatementContext)_localctx).AliasDatabase = aliasDatabaseStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(626);
				((StatementContext)_localctx).DeclarePattern = declarePatternStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(627);
				((StatementContext)_localctx).DeclareQueryParameters = declareQueryParametersStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(628);
				((StatementContext)_localctx).Let = letStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(629);
				((StatementContext)_localctx).Query = queryStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(630);
				((StatementContext)_localctx).RestrictAccess = restrictAccessStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(631);
				((StatementContext)_localctx).Set = setStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AliasDatabaseStatementContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public UnnamedExpressionContext Expression;
		public TerminalNode ALIAS() { return getToken(HqlParser.ALIAS, 0); }
		public TerminalNode DATABASE() { return getToken(HqlParser.DATABASE, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public AliasDatabaseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_aliasDatabaseStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAliasDatabaseStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAliasDatabaseStatement(this);
		}
	}

	public final AliasDatabaseStatementContext aliasDatabaseStatement() throws RecognitionException {
		AliasDatabaseStatementContext _localctx = new AliasDatabaseStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_aliasDatabaseStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(634);
			match(ALIAS);
			setState(635);
			match(DATABASE);
			setState(636);
			((AliasDatabaseStatementContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(637);
			match(EQUAL);
			setState(638);
			((AliasDatabaseStatementContext)_localctx).Expression = unnamedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetStatementContext extends ParserRuleContext {
		public LetFunctionDeclarationContext Function;
		public LetViewDeclarationContext View;
		public LetVariableDeclarationContext Variable;
		public LetMaterializeDeclarationContext Materialized;
		public LetEntityGroupDeclarationContext EntityGroup;
		public LetFunctionDeclarationContext letFunctionDeclaration() {
			return getRuleContext(LetFunctionDeclarationContext.class,0);
		}
		public LetViewDeclarationContext letViewDeclaration() {
			return getRuleContext(LetViewDeclarationContext.class,0);
		}
		public LetVariableDeclarationContext letVariableDeclaration() {
			return getRuleContext(LetVariableDeclarationContext.class,0);
		}
		public LetMaterializeDeclarationContext letMaterializeDeclaration() {
			return getRuleContext(LetMaterializeDeclarationContext.class,0);
		}
		public LetEntityGroupDeclarationContext letEntityGroupDeclaration() {
			return getRuleContext(LetEntityGroupDeclarationContext.class,0);
		}
		public LetStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetStatement(this);
		}
	}

	public final LetStatementContext letStatement() throws RecognitionException {
		LetStatementContext _localctx = new LetStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_letStatement);
		try {
			setState(645);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(640);
				((LetStatementContext)_localctx).Function = letFunctionDeclaration();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(641);
				((LetStatementContext)_localctx).View = letViewDeclaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(642);
				((LetStatementContext)_localctx).Variable = letVariableDeclaration();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(643);
				((LetStatementContext)_localctx).Materialized = letMaterializeDeclaration();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(644);
				((LetStatementContext)_localctx).EntityGroup = letEntityGroupDeclaration();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetVariableDeclarationContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public ExpressionContext Expression;
		public TerminalNode LET() { return getToken(HqlParser.LET, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LetVariableDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letVariableDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetVariableDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetVariableDeclaration(this);
		}
	}

	public final LetVariableDeclarationContext letVariableDeclaration() throws RecognitionException {
		LetVariableDeclarationContext _localctx = new LetVariableDeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_letVariableDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(647);
			match(LET);
			setState(648);
			((LetVariableDeclarationContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(649);
			match(EQUAL);
			setState(650);
			((LetVariableDeclarationContext)_localctx).Expression = expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetFunctionDeclarationContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public LetFunctionParameterListContext ParameterList;
		public LetFunctionBodyContext Body;
		public TerminalNode LET() { return getToken(HqlParser.LET, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public LetFunctionBodyContext letFunctionBody() {
			return getRuleContext(LetFunctionBodyContext.class,0);
		}
		public LetFunctionParameterListContext letFunctionParameterList() {
			return getRuleContext(LetFunctionParameterListContext.class,0);
		}
		public LetFunctionDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letFunctionDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetFunctionDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetFunctionDeclaration(this);
		}
	}

	public final LetFunctionDeclarationContext letFunctionDeclaration() throws RecognitionException {
		LetFunctionDeclarationContext _localctx = new LetFunctionDeclarationContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_letFunctionDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(652);
			match(LET);
			setState(653);
			((LetFunctionDeclarationContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(654);
			match(EQUAL);
			setState(655);
			match(OPENPAREN);
			setState(657);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416123978121216L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(656);
				((LetFunctionDeclarationContext)_localctx).ParameterList = letFunctionParameterList();
				}
			}

			setState(659);
			match(CLOSEPAREN);
			setState(660);
			((LetFunctionDeclarationContext)_localctx).Body = letFunctionBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetViewDeclarationContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public LetViewParameterListContext ParameterList;
		public LetFunctionBodyContext Body;
		public TerminalNode LET() { return getToken(HqlParser.LET, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode VIEW() { return getToken(HqlParser.VIEW, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public LetFunctionBodyContext letFunctionBody() {
			return getRuleContext(LetFunctionBodyContext.class,0);
		}
		public LetViewParameterListContext letViewParameterList() {
			return getRuleContext(LetViewParameterListContext.class,0);
		}
		public LetViewDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letViewDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetViewDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetViewDeclaration(this);
		}
	}

	public final LetViewDeclarationContext letViewDeclaration() throws RecognitionException {
		LetViewDeclarationContext _localctx = new LetViewDeclarationContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_letViewDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(662);
			match(LET);
			setState(663);
			((LetViewDeclarationContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(664);
			match(EQUAL);
			setState(665);
			match(VIEW);
			setState(666);
			match(OPENPAREN);
			setState(668);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416123978121216L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(667);
				((LetViewDeclarationContext)_localctx).ParameterList = letViewParameterList();
				}
			}

			setState(670);
			match(CLOSEPAREN);
			setState(671);
			((LetViewDeclarationContext)_localctx).Body = letFunctionBody();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetViewParameterListContext extends ParserRuleContext {
		public ScalarParameterContext scalarParameter;
		public List<ScalarParameterContext> Parameters = new ArrayList<ScalarParameterContext>();
		public List<ScalarParameterContext> scalarParameter() {
			return getRuleContexts(ScalarParameterContext.class);
		}
		public ScalarParameterContext scalarParameter(int i) {
			return getRuleContext(ScalarParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public LetViewParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letViewParameterList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetViewParameterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetViewParameterList(this);
		}
	}

	public final LetViewParameterListContext letViewParameterList() throws RecognitionException {
		LetViewParameterListContext _localctx = new LetViewParameterListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_letViewParameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(673);
			((LetViewParameterListContext)_localctx).scalarParameter = scalarParameter();
			((LetViewParameterListContext)_localctx).Parameters.add(((LetViewParameterListContext)_localctx).scalarParameter);
			setState(678);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(674);
				match(COMMA);
				setState(675);
				((LetViewParameterListContext)_localctx).scalarParameter = scalarParameter();
				((LetViewParameterListContext)_localctx).Parameters.add(((LetViewParameterListContext)_localctx).scalarParameter);
				}
				}
				setState(680);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetMaterializeDeclarationContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public PipeExpressionContext Expression;
		public TerminalNode LET() { return getToken(HqlParser.LET, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode MATERIALIZE() { return getToken(HqlParser.MATERIALIZE, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public PipeExpressionContext pipeExpression() {
			return getRuleContext(PipeExpressionContext.class,0);
		}
		public LetMaterializeDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letMaterializeDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetMaterializeDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetMaterializeDeclaration(this);
		}
	}

	public final LetMaterializeDeclarationContext letMaterializeDeclaration() throws RecognitionException {
		LetMaterializeDeclarationContext _localctx = new LetMaterializeDeclarationContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_letMaterializeDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(681);
			match(LET);
			setState(682);
			((LetMaterializeDeclarationContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(683);
			match(EQUAL);
			setState(684);
			match(MATERIALIZE);
			setState(685);
			match(OPENPAREN);
			setState(686);
			((LetMaterializeDeclarationContext)_localctx).Expression = pipeExpression();
			setState(687);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetEntityGroupDeclarationContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode LET() { return getToken(HqlParser.LET, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public EntityGroupExpressionContext entityGroupExpression() {
			return getRuleContext(EntityGroupExpressionContext.class,0);
		}
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public LetEntityGroupDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letEntityGroupDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetEntityGroupDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetEntityGroupDeclaration(this);
		}
	}

	public final LetEntityGroupDeclarationContext letEntityGroupDeclaration() throws RecognitionException {
		LetEntityGroupDeclarationContext _localctx = new LetEntityGroupDeclarationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_letEntityGroupDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(689);
			match(LET);
			setState(690);
			((LetEntityGroupDeclarationContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(691);
			match(EQUAL);
			setState(692);
			entityGroupExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetFunctionParameterListContext extends ParserRuleContext {
		public TabularParameterContext tabularParameter;
		public List<TabularParameterContext> TabularParameters = new ArrayList<TabularParameterContext>();
		public ScalarParameterContext scalarParameter;
		public List<ScalarParameterContext> ScalarParameters = new ArrayList<ScalarParameterContext>();
		public List<TabularParameterContext> tabularParameter() {
			return getRuleContexts(TabularParameterContext.class);
		}
		public TabularParameterContext tabularParameter(int i) {
			return getRuleContext(TabularParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<ScalarParameterContext> scalarParameter() {
			return getRuleContexts(ScalarParameterContext.class);
		}
		public ScalarParameterContext scalarParameter(int i) {
			return getRuleContext(ScalarParameterContext.class,i);
		}
		public LetFunctionParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letFunctionParameterList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetFunctionParameterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetFunctionParameterList(this);
		}
	}

	public final LetFunctionParameterListContext letFunctionParameterList() throws RecognitionException {
		LetFunctionParameterListContext _localctx = new LetFunctionParameterListContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_letFunctionParameterList);
		try {
			setState(705);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(694);
				((LetFunctionParameterListContext)_localctx).tabularParameter = tabularParameter();
				((LetFunctionParameterListContext)_localctx).TabularParameters.add(((LetFunctionParameterListContext)_localctx).tabularParameter);
				{
				setState(695);
				match(COMMA);
				setState(696);
				((LetFunctionParameterListContext)_localctx).tabularParameter = tabularParameter();
				((LetFunctionParameterListContext)_localctx).TabularParameters.add(((LetFunctionParameterListContext)_localctx).tabularParameter);
				}
				{
				setState(698);
				match(COMMA);
				setState(699);
				((LetFunctionParameterListContext)_localctx).scalarParameter = scalarParameter();
				((LetFunctionParameterListContext)_localctx).ScalarParameters.add(((LetFunctionParameterListContext)_localctx).scalarParameter);
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(701);
				((LetFunctionParameterListContext)_localctx).scalarParameter = scalarParameter();
				((LetFunctionParameterListContext)_localctx).ScalarParameters.add(((LetFunctionParameterListContext)_localctx).scalarParameter);
				{
				setState(702);
				match(COMMA);
				setState(703);
				((LetFunctionParameterListContext)_localctx).scalarParameter = scalarParameter();
				((LetFunctionParameterListContext)_localctx).ScalarParameters.add(((LetFunctionParameterListContext)_localctx).scalarParameter);
				}
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScalarParameterContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public ScalarTypeContext Type;
		public ScalarParameterDefaultContext Default;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public ScalarTypeContext scalarType() {
			return getRuleContext(ScalarTypeContext.class,0);
		}
		public ScalarParameterDefaultContext scalarParameterDefault() {
			return getRuleContext(ScalarParameterDefaultContext.class,0);
		}
		public ScalarParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalarParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScalarParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScalarParameter(this);
		}
	}

	public final ScalarParameterContext scalarParameter() throws RecognitionException {
		ScalarParameterContext _localctx = new ScalarParameterContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_scalarParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(707);
			((ScalarParameterContext)_localctx).Name = parameterName();
			setState(708);
			match(COLON);
			setState(709);
			((ScalarParameterContext)_localctx).Type = scalarType();
			setState(711);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(710);
				((ScalarParameterContext)_localctx).Default = scalarParameterDefault();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScalarParameterDefaultContext extends ParserRuleContext {
		public LiteralExpressionContext Value;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public LiteralExpressionContext literalExpression() {
			return getRuleContext(LiteralExpressionContext.class,0);
		}
		public ScalarParameterDefaultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalarParameterDefault; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScalarParameterDefault(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScalarParameterDefault(this);
		}
	}

	public final ScalarParameterDefaultContext scalarParameterDefault() throws RecognitionException {
		ScalarParameterDefaultContext _localctx = new ScalarParameterDefaultContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_scalarParameterDefault);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(713);
			match(EQUAL);
			setState(714);
			((ScalarParameterDefaultContext)_localctx).Value = literalExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TabularParameterContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public TabularParameterOpenSchemaContext OpenSchema;
		public TabularParameterRowSchemaContext RowSchema;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public TabularParameterOpenSchemaContext tabularParameterOpenSchema() {
			return getRuleContext(TabularParameterOpenSchemaContext.class,0);
		}
		public TabularParameterRowSchemaContext tabularParameterRowSchema() {
			return getRuleContext(TabularParameterRowSchemaContext.class,0);
		}
		public TabularParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tabularParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTabularParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTabularParameter(this);
		}
	}

	public final TabularParameterContext tabularParameter() throws RecognitionException {
		TabularParameterContext _localctx = new TabularParameterContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_tabularParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(716);
			((TabularParameterContext)_localctx).Name = parameterName();
			setState(717);
			match(COLON);
			setState(720);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(718);
				((TabularParameterContext)_localctx).OpenSchema = tabularParameterOpenSchema();
				}
				break;
			case 2:
				{
				setState(719);
				((TabularParameterContext)_localctx).RowSchema = tabularParameterRowSchema();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TabularParameterOpenSchemaContext extends ParserRuleContext {
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public TabularParameterOpenSchemaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tabularParameterOpenSchema; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTabularParameterOpenSchema(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTabularParameterOpenSchema(this);
		}
	}

	public final TabularParameterOpenSchemaContext tabularParameterOpenSchema() throws RecognitionException {
		TabularParameterOpenSchemaContext _localctx = new TabularParameterOpenSchemaContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_tabularParameterOpenSchema);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(722);
			match(OPENPAREN);
			setState(723);
			match(ASTERISK);
			setState(724);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TabularParameterRowSchemaContext extends ParserRuleContext {
		public TabularParameterRowSchemaColumnDeclarationContext tabularParameterRowSchemaColumnDeclaration;
		public List<TabularParameterRowSchemaColumnDeclarationContext> Columns = new ArrayList<TabularParameterRowSchemaColumnDeclarationContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<TabularParameterRowSchemaColumnDeclarationContext> tabularParameterRowSchemaColumnDeclaration() {
			return getRuleContexts(TabularParameterRowSchemaColumnDeclarationContext.class);
		}
		public TabularParameterRowSchemaColumnDeclarationContext tabularParameterRowSchemaColumnDeclaration(int i) {
			return getRuleContext(TabularParameterRowSchemaColumnDeclarationContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public TabularParameterRowSchemaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tabularParameterRowSchema; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTabularParameterRowSchema(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTabularParameterRowSchema(this);
		}
	}

	public final TabularParameterRowSchemaContext tabularParameterRowSchema() throws RecognitionException {
		TabularParameterRowSchemaContext _localctx = new TabularParameterRowSchemaContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_tabularParameterRowSchema);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(726);
			match(OPENPAREN);
			setState(727);
			((TabularParameterRowSchemaContext)_localctx).tabularParameterRowSchemaColumnDeclaration = tabularParameterRowSchemaColumnDeclaration();
			((TabularParameterRowSchemaContext)_localctx).Columns.add(((TabularParameterRowSchemaContext)_localctx).tabularParameterRowSchemaColumnDeclaration);
			setState(732);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(728);
				match(COMMA);
				setState(729);
				((TabularParameterRowSchemaContext)_localctx).tabularParameterRowSchemaColumnDeclaration = tabularParameterRowSchemaColumnDeclaration();
				((TabularParameterRowSchemaContext)_localctx).Columns.add(((TabularParameterRowSchemaContext)_localctx).tabularParameterRowSchemaColumnDeclaration);
				}
				}
				setState(734);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(735);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TabularParameterRowSchemaColumnDeclarationContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public ScalarTypeContext Type;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public ScalarTypeContext scalarType() {
			return getRuleContext(ScalarTypeContext.class,0);
		}
		public TabularParameterRowSchemaColumnDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tabularParameterRowSchemaColumnDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTabularParameterRowSchemaColumnDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTabularParameterRowSchemaColumnDeclaration(this);
		}
	}

	public final TabularParameterRowSchemaColumnDeclarationContext tabularParameterRowSchemaColumnDeclaration() throws RecognitionException {
		TabularParameterRowSchemaColumnDeclarationContext _localctx = new TabularParameterRowSchemaColumnDeclarationContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_tabularParameterRowSchemaColumnDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(737);
			((TabularParameterRowSchemaColumnDeclarationContext)_localctx).Name = parameterName();
			setState(738);
			match(COLON);
			setState(739);
			((TabularParameterRowSchemaColumnDeclarationContext)_localctx).Type = scalarType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetFunctionBodyContext extends ParserRuleContext {
		public LetFunctionBodyStatementContext letFunctionBodyStatement;
		public List<LetFunctionBodyStatementContext> Statements = new ArrayList<LetFunctionBodyStatementContext>();
		public ExpressionContext Expression;
		public TerminalNode OPENBRACE() { return getToken(HqlParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(HqlParser.CLOSEBRACE, 0); }
		public List<TerminalNode> SEMICOLON() { return getTokens(HqlParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(HqlParser.SEMICOLON, i);
		}
		public List<LetFunctionBodyStatementContext> letFunctionBodyStatement() {
			return getRuleContexts(LetFunctionBodyStatementContext.class);
		}
		public LetFunctionBodyStatementContext letFunctionBodyStatement(int i) {
			return getRuleContext(LetFunctionBodyStatementContext.class,i);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public LetFunctionBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letFunctionBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetFunctionBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetFunctionBody(this);
		}
	}

	public final LetFunctionBodyContext letFunctionBody() throws RecognitionException {
		LetFunctionBodyContext _localctx = new LetFunctionBodyContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_letFunctionBody);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(741);
			match(OPENBRACE);
			setState(747);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(742);
					((LetFunctionBodyContext)_localctx).letFunctionBodyStatement = letFunctionBodyStatement();
					((LetFunctionBodyContext)_localctx).Statements.add(((LetFunctionBodyContext)_localctx).letFunctionBodyStatement);
					setState(743);
					match(SEMICOLON);
					}
					} 
				}
				setState(749);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			}
			setState(751);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622630631754434562L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1729241517714430253L) != 0) || ((((_la - 132)) & ~0x3f) == 0 && ((1L << (_la - 132)) & 1790180853509759745L) != 0) || ((((_la - 197)) & ~0x3f) == 0 && ((1L << (_la - 197)) & -4656703218566889077L) != 0) || ((((_la - 268)) & ~0x3f) == 0 && ((1L << (_la - 268)) & 492443770949631L) != 0)) {
				{
				setState(750);
				((LetFunctionBodyContext)_localctx).Expression = expression();
				}
			}

			setState(754);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(753);
				match(SEMICOLON);
				}
			}

			setState(756);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LetFunctionBodyStatementContext extends ParserRuleContext {
		public LetStatementContext Let;
		public DeclareQueryParametersStatementContext DeclareQueryParameters;
		public LetStatementContext letStatement() {
			return getRuleContext(LetStatementContext.class,0);
		}
		public DeclareQueryParametersStatementContext declareQueryParametersStatement() {
			return getRuleContext(DeclareQueryParametersStatementContext.class,0);
		}
		public LetFunctionBodyStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letFunctionBodyStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLetFunctionBodyStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLetFunctionBodyStatement(this);
		}
	}

	public final LetFunctionBodyStatementContext letFunctionBodyStatement() throws RecognitionException {
		LetFunctionBodyStatementContext _localctx = new LetFunctionBodyStatementContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_letFunctionBodyStatement);
		try {
			setState(760);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				enterOuterAlt(_localctx, 1);
				{
				setState(758);
				((LetFunctionBodyStatementContext)_localctx).Let = letStatement();
				}
				break;
			case DECLARE:
				enterOuterAlt(_localctx, 2);
				{
				setState(759);
				((LetFunctionBodyStatementContext)_localctx).DeclareQueryParameters = declareQueryParametersStatement();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternStatementContext extends ParserRuleContext {
		public SimpleNameReferenceContext Name;
		public DeclarePatternDefinitionContext Definition;
		public TerminalNode DECLARE() { return getToken(HqlParser.DECLARE, 0); }
		public TerminalNode PATTERN() { return getToken(HqlParser.PATTERN, 0); }
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public DeclarePatternDefinitionContext declarePatternDefinition() {
			return getRuleContext(DeclarePatternDefinitionContext.class,0);
		}
		public DeclarePatternStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternStatement(this);
		}
	}

	public final DeclarePatternStatementContext declarePatternStatement() throws RecognitionException {
		DeclarePatternStatementContext _localctx = new DeclarePatternStatementContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_declarePatternStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(762);
			match(DECLARE);
			setState(763);
			match(PATTERN);
			setState(764);
			((DeclarePatternStatementContext)_localctx).Name = simpleNameReference();
			setState(766);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(765);
				((DeclarePatternStatementContext)_localctx).Definition = declarePatternDefinition();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternDefinitionContext extends ParserRuleContext {
		public DeclarePatternParameterListContext ParameterList;
		public DeclarePatternPathParameterContext Path;
		public DeclarePatternRuleContext declarePatternRule;
		public List<DeclarePatternRuleContext> Rules = new ArrayList<DeclarePatternRuleContext>();
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode OPENBRACE() { return getToken(HqlParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(HqlParser.CLOSEBRACE, 0); }
		public DeclarePatternParameterListContext declarePatternParameterList() {
			return getRuleContext(DeclarePatternParameterListContext.class,0);
		}
		public DeclarePatternPathParameterContext declarePatternPathParameter() {
			return getRuleContext(DeclarePatternPathParameterContext.class,0);
		}
		public List<DeclarePatternRuleContext> declarePatternRule() {
			return getRuleContexts(DeclarePatternRuleContext.class);
		}
		public DeclarePatternRuleContext declarePatternRule(int i) {
			return getRuleContext(DeclarePatternRuleContext.class,i);
		}
		public DeclarePatternDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternDefinition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternDefinition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternDefinition(this);
		}
	}

	public final DeclarePatternDefinitionContext declarePatternDefinition() throws RecognitionException {
		DeclarePatternDefinitionContext _localctx = new DeclarePatternDefinitionContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_declarePatternDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(768);
			match(EQUAL);
			setState(769);
			((DeclarePatternDefinitionContext)_localctx).ParameterList = declarePatternParameterList();
			setState(771);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPENBRACKET) {
				{
				setState(770);
				((DeclarePatternDefinitionContext)_localctx).Path = declarePatternPathParameter();
				}
			}

			setState(773);
			match(OPENBRACE);
			setState(775); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(774);
				((DeclarePatternDefinitionContext)_localctx).declarePatternRule = declarePatternRule();
				((DeclarePatternDefinitionContext)_localctx).Rules.add(((DeclarePatternDefinitionContext)_localctx).declarePatternRule);
				}
				}
				setState(777); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==OPENPAREN );
			setState(779);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternParameterListContext extends ParserRuleContext {
		public DeclarePatternParameterContext declarePatternParameter;
		public List<DeclarePatternParameterContext> Parameters = new ArrayList<DeclarePatternParameterContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<DeclarePatternParameterContext> declarePatternParameter() {
			return getRuleContexts(DeclarePatternParameterContext.class);
		}
		public DeclarePatternParameterContext declarePatternParameter(int i) {
			return getRuleContext(DeclarePatternParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public DeclarePatternParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternParameterList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternParameterList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternParameterList(this);
		}
	}

	public final DeclarePatternParameterListContext declarePatternParameterList() throws RecognitionException {
		DeclarePatternParameterListContext _localctx = new DeclarePatternParameterListContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_declarePatternParameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(781);
			match(OPENPAREN);
			setState(782);
			((DeclarePatternParameterListContext)_localctx).declarePatternParameter = declarePatternParameter();
			((DeclarePatternParameterListContext)_localctx).Parameters.add(((DeclarePatternParameterListContext)_localctx).declarePatternParameter);
			setState(787);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(783);
				match(COMMA);
				setState(784);
				((DeclarePatternParameterListContext)_localctx).declarePatternParameter = declarePatternParameter();
				((DeclarePatternParameterListContext)_localctx).Parameters.add(((DeclarePatternParameterListContext)_localctx).declarePatternParameter);
				}
				}
				setState(789);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(790);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternParameterContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public ScalarTypeContext Type;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public ScalarTypeContext scalarType() {
			return getRuleContext(ScalarTypeContext.class,0);
		}
		public DeclarePatternParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternParameter(this);
		}
	}

	public final DeclarePatternParameterContext declarePatternParameter() throws RecognitionException {
		DeclarePatternParameterContext _localctx = new DeclarePatternParameterContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_declarePatternParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(792);
			((DeclarePatternParameterContext)_localctx).Name = parameterName();
			setState(793);
			match(COLON);
			setState(794);
			((DeclarePatternParameterContext)_localctx).Type = scalarType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternPathParameterContext extends ParserRuleContext {
		public DeclarePatternParameterContext Parameter;
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public DeclarePatternParameterContext declarePatternParameter() {
			return getRuleContext(DeclarePatternParameterContext.class,0);
		}
		public DeclarePatternPathParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternPathParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternPathParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternPathParameter(this);
		}
	}

	public final DeclarePatternPathParameterContext declarePatternPathParameter() throws RecognitionException {
		DeclarePatternPathParameterContext _localctx = new DeclarePatternPathParameterContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_declarePatternPathParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(796);
			match(OPENBRACKET);
			setState(797);
			((DeclarePatternPathParameterContext)_localctx).Parameter = declarePatternParameter();
			setState(798);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternRuleContext extends ParserRuleContext {
		public DeclarePatternRuleArgumentListContext ArgumentList;
		public DeclarePatternRulePathArgumentContext PathArgument;
		public DeclarePatternBodyContext Body;
		public Token TrailingSemicolon;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public DeclarePatternRuleArgumentListContext declarePatternRuleArgumentList() {
			return getRuleContext(DeclarePatternRuleArgumentListContext.class,0);
		}
		public DeclarePatternBodyContext declarePatternBody() {
			return getRuleContext(DeclarePatternBodyContext.class,0);
		}
		public DeclarePatternRulePathArgumentContext declarePatternRulePathArgument() {
			return getRuleContext(DeclarePatternRulePathArgumentContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(HqlParser.SEMICOLON, 0); }
		public DeclarePatternRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternRule; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternRule(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternRule(this);
		}
	}

	public final DeclarePatternRuleContext declarePatternRule() throws RecognitionException {
		DeclarePatternRuleContext _localctx = new DeclarePatternRuleContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_declarePatternRule);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(800);
			((DeclarePatternRuleContext)_localctx).ArgumentList = declarePatternRuleArgumentList();
			setState(802);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DOT) {
				{
				setState(801);
				((DeclarePatternRuleContext)_localctx).PathArgument = declarePatternRulePathArgument();
				}
			}

			setState(804);
			match(EQUAL);
			setState(805);
			((DeclarePatternRuleContext)_localctx).Body = declarePatternBody();
			setState(807);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(806);
				((DeclarePatternRuleContext)_localctx).TrailingSemicolon = match(SEMICOLON);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternRuleArgumentListContext extends ParserRuleContext {
		public DeclarePatternRuleArgumentContext declarePatternRuleArgument;
		public List<DeclarePatternRuleArgumentContext> Arguments = new ArrayList<DeclarePatternRuleArgumentContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<DeclarePatternRuleArgumentContext> declarePatternRuleArgument() {
			return getRuleContexts(DeclarePatternRuleArgumentContext.class);
		}
		public DeclarePatternRuleArgumentContext declarePatternRuleArgument(int i) {
			return getRuleContext(DeclarePatternRuleArgumentContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public DeclarePatternRuleArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternRuleArgumentList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternRuleArgumentList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternRuleArgumentList(this);
		}
	}

	public final DeclarePatternRuleArgumentListContext declarePatternRuleArgumentList() throws RecognitionException {
		DeclarePatternRuleArgumentListContext _localctx = new DeclarePatternRuleArgumentListContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_declarePatternRuleArgumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(809);
			match(OPENPAREN);
			setState(810);
			((DeclarePatternRuleArgumentListContext)_localctx).declarePatternRuleArgument = declarePatternRuleArgument();
			((DeclarePatternRuleArgumentListContext)_localctx).Arguments.add(((DeclarePatternRuleArgumentListContext)_localctx).declarePatternRuleArgument);
			setState(815);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(811);
				match(COMMA);
				setState(812);
				((DeclarePatternRuleArgumentListContext)_localctx).declarePatternRuleArgument = declarePatternRuleArgument();
				((DeclarePatternRuleArgumentListContext)_localctx).Arguments.add(((DeclarePatternRuleArgumentListContext)_localctx).declarePatternRuleArgument);
				}
				}
				setState(817);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(818);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternRulePathArgumentContext extends ParserRuleContext {
		public DeclarePatternRuleArgumentContext Expression;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public DeclarePatternRuleArgumentContext declarePatternRuleArgument() {
			return getRuleContext(DeclarePatternRuleArgumentContext.class,0);
		}
		public DeclarePatternRulePathArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternRulePathArgument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternRulePathArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternRulePathArgument(this);
		}
	}

	public final DeclarePatternRulePathArgumentContext declarePatternRulePathArgument() throws RecognitionException {
		DeclarePatternRulePathArgumentContext _localctx = new DeclarePatternRulePathArgumentContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_declarePatternRulePathArgument);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(820);
			match(DOT);
			setState(821);
			match(OPENBRACKET);
			setState(822);
			((DeclarePatternRulePathArgumentContext)_localctx).Expression = declarePatternRuleArgument();
			setState(823);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternRuleArgumentContext extends ParserRuleContext {
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public DeclarePatternRuleArgumentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternRuleArgument; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternRuleArgument(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternRuleArgument(this);
		}
	}

	public final DeclarePatternRuleArgumentContext declarePatternRuleArgument() throws RecognitionException {
		DeclarePatternRuleArgumentContext _localctx = new DeclarePatternRuleArgumentContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_declarePatternRuleArgument);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(825);
			stringLiteralExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarePatternBodyContext extends ParserRuleContext {
		public LetFunctionBodyStatementContext letFunctionBodyStatement;
		public List<LetFunctionBodyStatementContext> Statements = new ArrayList<LetFunctionBodyStatementContext>();
		public ExpressionContext Expression;
		public TerminalNode OPENBRACE() { return getToken(HqlParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(HqlParser.CLOSEBRACE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(HqlParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(HqlParser.SEMICOLON, i);
		}
		public List<LetFunctionBodyStatementContext> letFunctionBodyStatement() {
			return getRuleContexts(LetFunctionBodyStatementContext.class);
		}
		public LetFunctionBodyStatementContext letFunctionBodyStatement(int i) {
			return getRuleContext(LetFunctionBodyStatementContext.class,i);
		}
		public DeclarePatternBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarePatternBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclarePatternBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclarePatternBody(this);
		}
	}

	public final DeclarePatternBodyContext declarePatternBody() throws RecognitionException {
		DeclarePatternBodyContext _localctx = new DeclarePatternBodyContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_declarePatternBody);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(827);
			match(OPENBRACE);
			setState(833);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(828);
					((DeclarePatternBodyContext)_localctx).letFunctionBodyStatement = letFunctionBodyStatement();
					((DeclarePatternBodyContext)_localctx).Statements.add(((DeclarePatternBodyContext)_localctx).letFunctionBodyStatement);
					setState(829);
					match(SEMICOLON);
					}
					} 
				}
				setState(835);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,22,_ctx);
			}
			setState(836);
			((DeclarePatternBodyContext)_localctx).Expression = expression();
			setState(837);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RestrictAccessStatementContext extends ParserRuleContext {
		public RestrictAccessStatementEntityContext restrictAccessStatementEntity;
		public List<RestrictAccessStatementEntityContext> Entities = new ArrayList<RestrictAccessStatementEntityContext>();
		public TerminalNode RESTRICT() { return getToken(HqlParser.RESTRICT, 0); }
		public TerminalNode ACCESS() { return getToken(HqlParser.ACCESS, 0); }
		public TerminalNode TO() { return getToken(HqlParser.TO, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<RestrictAccessStatementEntityContext> restrictAccessStatementEntity() {
			return getRuleContexts(RestrictAccessStatementEntityContext.class);
		}
		public RestrictAccessStatementEntityContext restrictAccessStatementEntity(int i) {
			return getRuleContext(RestrictAccessStatementEntityContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public RestrictAccessStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_restrictAccessStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRestrictAccessStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRestrictAccessStatement(this);
		}
	}

	public final RestrictAccessStatementContext restrictAccessStatement() throws RecognitionException {
		RestrictAccessStatementContext _localctx = new RestrictAccessStatementContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_restrictAccessStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(839);
			match(RESTRICT);
			setState(840);
			match(ACCESS);
			setState(841);
			match(TO);
			setState(842);
			match(OPENPAREN);
			setState(843);
			((RestrictAccessStatementContext)_localctx).restrictAccessStatementEntity = restrictAccessStatementEntity();
			((RestrictAccessStatementContext)_localctx).Entities.add(((RestrictAccessStatementContext)_localctx).restrictAccessStatementEntity);
			setState(848);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(844);
				match(COMMA);
				setState(845);
				((RestrictAccessStatementContext)_localctx).restrictAccessStatementEntity = restrictAccessStatementEntity();
				((RestrictAccessStatementContext)_localctx).Entities.add(((RestrictAccessStatementContext)_localctx).restrictAccessStatementEntity);
				}
				}
				setState(850);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(851);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RestrictAccessStatementEntityContext extends ParserRuleContext {
		public SimpleNameReferenceContext SimpleName;
		public WildcardedEntityExpressionContext WildcardedEntity;
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public WildcardedEntityExpressionContext wildcardedEntityExpression() {
			return getRuleContext(WildcardedEntityExpressionContext.class,0);
		}
		public RestrictAccessStatementEntityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_restrictAccessStatementEntity; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRestrictAccessStatementEntity(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRestrictAccessStatementEntity(this);
		}
	}

	public final RestrictAccessStatementEntityContext restrictAccessStatementEntity() throws RecognitionException {
		RestrictAccessStatementEntityContext _localctx = new RestrictAccessStatementEntityContext(_ctx, getState());
		enterRule(_localctx, 62, RULE_restrictAccessStatementEntity);
		try {
			setState(855);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(853);
				((RestrictAccessStatementEntityContext)_localctx).SimpleName = simpleNameReference();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(854);
				((RestrictAccessStatementEntityContext)_localctx).WildcardedEntity = wildcardedEntityExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetStatementContext extends ParserRuleContext {
		public IdentifierOrKeywordNameContext Name;
		public SetStatementOptionValueContext Value;
		public TerminalNode SET() { return getToken(HqlParser.SET, 0); }
		public IdentifierOrKeywordNameContext identifierOrKeywordName() {
			return getRuleContext(IdentifierOrKeywordNameContext.class,0);
		}
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public SetStatementOptionValueContext setStatementOptionValue() {
			return getRuleContext(SetStatementOptionValueContext.class,0);
		}
		public SetStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSetStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSetStatement(this);
		}
	}

	public final SetStatementContext setStatement() throws RecognitionException {
		SetStatementContext _localctx = new SetStatementContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_setStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(857);
			match(SET);
			setState(858);
			((SetStatementContext)_localctx).Name = identifierOrKeywordName();
			setState(861);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(859);
				match(EQUAL);
				setState(860);
				((SetStatementContext)_localctx).Value = setStatementOptionValue();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SetStatementOptionValueContext extends ParserRuleContext {
		public IdentifierOrKeywordNameContext Name;
		public LiteralExpressionContext Literal;
		public IdentifierOrKeywordNameContext identifierOrKeywordName() {
			return getRuleContext(IdentifierOrKeywordNameContext.class,0);
		}
		public LiteralExpressionContext literalExpression() {
			return getRuleContext(LiteralExpressionContext.class,0);
		}
		public SetStatementOptionValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setStatementOptionValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSetStatementOptionValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSetStatementOptionValue(this);
		}
	}

	public final SetStatementOptionValueContext setStatementOptionValue() throws RecognitionException {
		SetStatementOptionValueContext _localctx = new SetStatementOptionValueContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_setStatementOptionValue);
		try {
			setState(865);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(863);
				((SetStatementOptionValueContext)_localctx).Name = identifierOrKeywordName();
				}
				break;
			case DASH:
			case PLUS:
			case DYNAMIC:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(864);
				((SetStatementOptionValueContext)_localctx).Literal = literalExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclareQueryParametersStatementContext extends ParserRuleContext {
		public DeclareQueryParametersStatementParameterContext declareQueryParametersStatementParameter;
		public List<DeclareQueryParametersStatementParameterContext> Parameters = new ArrayList<DeclareQueryParametersStatementParameterContext>();
		public TerminalNode DECLARE() { return getToken(HqlParser.DECLARE, 0); }
		public TerminalNode QUERYPARAMETERS() { return getToken(HqlParser.QUERYPARAMETERS, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<DeclareQueryParametersStatementParameterContext> declareQueryParametersStatementParameter() {
			return getRuleContexts(DeclareQueryParametersStatementParameterContext.class);
		}
		public DeclareQueryParametersStatementParameterContext declareQueryParametersStatementParameter(int i) {
			return getRuleContext(DeclareQueryParametersStatementParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public DeclareQueryParametersStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declareQueryParametersStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclareQueryParametersStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclareQueryParametersStatement(this);
		}
	}

	public final DeclareQueryParametersStatementContext declareQueryParametersStatement() throws RecognitionException {
		DeclareQueryParametersStatementContext _localctx = new DeclareQueryParametersStatementContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_declareQueryParametersStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(867);
			match(DECLARE);
			setState(868);
			match(QUERYPARAMETERS);
			setState(869);
			match(OPENPAREN);
			setState(870);
			((DeclareQueryParametersStatementContext)_localctx).declareQueryParametersStatementParameter = declareQueryParametersStatementParameter();
			((DeclareQueryParametersStatementContext)_localctx).Parameters.add(((DeclareQueryParametersStatementContext)_localctx).declareQueryParametersStatementParameter);
			setState(875);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(871);
				match(COMMA);
				setState(872);
				((DeclareQueryParametersStatementContext)_localctx).declareQueryParametersStatementParameter = declareQueryParametersStatementParameter();
				((DeclareQueryParametersStatementContext)_localctx).Parameters.add(((DeclareQueryParametersStatementContext)_localctx).declareQueryParametersStatementParameter);
				}
				}
				setState(877);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(878);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclareQueryParametersStatementParameterContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public ScalarTypeContext Type;
		public ScalarParameterDefaultContext Default;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public ScalarTypeContext scalarType() {
			return getRuleContext(ScalarTypeContext.class,0);
		}
		public ScalarParameterDefaultContext scalarParameterDefault() {
			return getRuleContext(ScalarParameterDefaultContext.class,0);
		}
		public DeclareQueryParametersStatementParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declareQueryParametersStatementParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDeclareQueryParametersStatementParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDeclareQueryParametersStatementParameter(this);
		}
	}

	public final DeclareQueryParametersStatementParameterContext declareQueryParametersStatementParameter() throws RecognitionException {
		DeclareQueryParametersStatementParameterContext _localctx = new DeclareQueryParametersStatementParameterContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_declareQueryParametersStatementParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(880);
			((DeclareQueryParametersStatementParameterContext)_localctx).Name = parameterName();
			setState(881);
			match(COLON);
			setState(882);
			((DeclareQueryParametersStatementParameterContext)_localctx).Type = scalarType();
			setState(884);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL) {
				{
				setState(883);
				((DeclareQueryParametersStatementParameterContext)_localctx).Default = scalarParameterDefault();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryStatementContext extends ParserRuleContext {
		public ExpressionContext Expression;
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public QueryStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryStatement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterQueryStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitQueryStatement(this);
		}
	}

	public final QueryStatementContext queryStatement() throws RecognitionException {
		QueryStatementContext _localctx = new QueryStatementContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_queryStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(886);
			((QueryStatementContext)_localctx).Expression = expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public PipeExpressionContext pipeExpression() {
			return getRuleContext(PipeExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExpression(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(888);
			pipeExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipeExpressionContext extends ParserRuleContext {
		public BeforePipeExpressionContext Expression;
		public PipedOperatorContext pipedOperator;
		public List<PipedOperatorContext> PipedOperators = new ArrayList<PipedOperatorContext>();
		public BeforePipeExpressionContext beforePipeExpression() {
			return getRuleContext(BeforePipeExpressionContext.class,0);
		}
		public List<PipedOperatorContext> pipedOperator() {
			return getRuleContexts(PipedOperatorContext.class);
		}
		public PipedOperatorContext pipedOperator(int i) {
			return getRuleContext(PipedOperatorContext.class,i);
		}
		public PipeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipeExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPipeExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPipeExpression(this);
		}
	}

	public final PipeExpressionContext pipeExpression() throws RecognitionException {
		PipeExpressionContext _localctx = new PipeExpressionContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_pipeExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(890);
			((PipeExpressionContext)_localctx).Expression = beforePipeExpression();
			setState(894);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(891);
					((PipeExpressionContext)_localctx).pipedOperator = pipedOperator();
					((PipeExpressionContext)_localctx).PipedOperators.add(((PipeExpressionContext)_localctx).pipedOperator);
					}
					} 
				}
				setState(896);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,29,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipedOperatorContext extends ParserRuleContext {
		public AfterPipeOperatorContext Operator;
		public TerminalNode BAR() { return getToken(HqlParser.BAR, 0); }
		public AfterPipeOperatorContext afterPipeOperator() {
			return getRuleContext(AfterPipeOperatorContext.class,0);
		}
		public PipedOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipedOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPipedOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPipedOperator(this);
		}
	}

	public final PipedOperatorContext pipedOperator() throws RecognitionException {
		PipedOperatorContext _localctx = new PipedOperatorContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_pipedOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(897);
			match(BAR);
			setState(898);
			((PipedOperatorContext)_localctx).Operator = afterPipeOperator();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PipeSubExpressionContext extends ParserRuleContext {
		public AfterPipeOperatorContext Expression;
		public PipedOperatorContext pipedOperator;
		public List<PipedOperatorContext> PipedOperators = new ArrayList<PipedOperatorContext>();
		public AfterPipeOperatorContext afterPipeOperator() {
			return getRuleContext(AfterPipeOperatorContext.class,0);
		}
		public List<PipedOperatorContext> pipedOperator() {
			return getRuleContexts(PipedOperatorContext.class);
		}
		public PipedOperatorContext pipedOperator(int i) {
			return getRuleContext(PipedOperatorContext.class,i);
		}
		public PipeSubExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pipeSubExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPipeSubExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPipeSubExpression(this);
		}
	}

	public final PipeSubExpressionContext pipeSubExpression() throws RecognitionException {
		PipeSubExpressionContext _localctx = new PipeSubExpressionContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_pipeSubExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(900);
			((PipeSubExpressionContext)_localctx).Expression = afterPipeOperator();
			setState(904);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BAR) {
				{
				{
				setState(901);
				((PipeSubExpressionContext)_localctx).pipedOperator = pipedOperator();
				((PipeSubExpressionContext)_localctx).PipedOperators.add(((PipeSubExpressionContext)_localctx).pipedOperator);
				}
				}
				setState(906);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BeforePipeExpressionContext extends ParserRuleContext {
		public BeforeOrAfterPipeOperatorContext beforeOrAfterPipeOperator() {
			return getRuleContext(BeforeOrAfterPipeOperatorContext.class,0);
		}
		public PrintOperatorContext printOperator() {
			return getRuleContext(PrintOperatorContext.class,0);
		}
		public MacroExpandOperatorContext macroExpandOperator() {
			return getRuleContext(MacroExpandOperatorContext.class,0);
		}
		public RangeExpressionContext rangeExpression() {
			return getRuleContext(RangeExpressionContext.class,0);
		}
		public ScopedFunctionCallExpressionContext scopedFunctionCallExpression() {
			return getRuleContext(ScopedFunctionCallExpressionContext.class,0);
		}
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public BeforePipeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_beforePipeExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterBeforePipeExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitBeforePipeExpression(this);
		}
	}

	public final BeforePipeExpressionContext beforePipeExpression() throws RecognitionException {
		BeforePipeExpressionContext _localctx = new BeforePipeExpressionContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_beforePipeExpression);
		try {
			setState(913);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(907);
				beforeOrAfterPipeOperator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(908);
				printOperator();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(909);
				macroExpandOperator();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(910);
				rangeExpression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(911);
				scopedFunctionCallExpression();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(912);
				unnamedExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AfterPipeOperatorContext extends ParserRuleContext {
		public AsOperatorContext asOperator() {
			return getRuleContext(AsOperatorContext.class,0);
		}
		public AssertSchemaOperatorContext assertSchemaOperator() {
			return getRuleContext(AssertSchemaOperatorContext.class,0);
		}
		public ConsumeOperatorContext consumeOperator() {
			return getRuleContext(ConsumeOperatorContext.class,0);
		}
		public CountOperatorContext countOperator() {
			return getRuleContext(CountOperatorContext.class,0);
		}
		public DistinctOperatorContext distinctOperator() {
			return getRuleContext(DistinctOperatorContext.class,0);
		}
		public ExecuteAndCacheOperatorContext executeAndCacheOperator() {
			return getRuleContext(ExecuteAndCacheOperatorContext.class,0);
		}
		public ExtendOperatorContext extendOperator() {
			return getRuleContext(ExtendOperatorContext.class,0);
		}
		public FacetByOperatorContext facetByOperator() {
			return getRuleContext(FacetByOperatorContext.class,0);
		}
		public FindOperatorContext findOperator() {
			return getRuleContext(FindOperatorContext.class,0);
		}
		public ForkOperatorContext forkOperator() {
			return getRuleContext(ForkOperatorContext.class,0);
		}
		public GetSchemaOperatorContext getSchemaOperator() {
			return getRuleContext(GetSchemaOperatorContext.class,0);
		}
		public GraphMarkComponentsOperatorContext graphMarkComponentsOperator() {
			return getRuleContext(GraphMarkComponentsOperatorContext.class,0);
		}
		public GraphMatchOperatorContext graphMatchOperator() {
			return getRuleContext(GraphMatchOperatorContext.class,0);
		}
		public GraphMergeOperatorContext graphMergeOperator() {
			return getRuleContext(GraphMergeOperatorContext.class,0);
		}
		public GraphShortestPathsOperatorContext graphShortestPathsOperator() {
			return getRuleContext(GraphShortestPathsOperatorContext.class,0);
		}
		public GraphToTableOperatorContext graphToTableOperator() {
			return getRuleContext(GraphToTableOperatorContext.class,0);
		}
		public InvokeOperatorContext invokeOperator() {
			return getRuleContext(InvokeOperatorContext.class,0);
		}
		public JoinOperatorContext joinOperator() {
			return getRuleContext(JoinOperatorContext.class,0);
		}
		public LookupOperatorContext lookupOperator() {
			return getRuleContext(LookupOperatorContext.class,0);
		}
		public MakeGraphOperatorContext makeGraphOperator() {
			return getRuleContext(MakeGraphOperatorContext.class,0);
		}
		public MakeSeriesOperatorContext makeSeriesOperator() {
			return getRuleContext(MakeSeriesOperatorContext.class,0);
		}
		public MvexpandOperatorContext mvexpandOperator() {
			return getRuleContext(MvexpandOperatorContext.class,0);
		}
		public MvapplyOperatorContext mvapplyOperator() {
			return getRuleContext(MvapplyOperatorContext.class,0);
		}
		public EvaluateOperatorContext evaluateOperator() {
			return getRuleContext(EvaluateOperatorContext.class,0);
		}
		public ParseOperatorContext parseOperator() {
			return getRuleContext(ParseOperatorContext.class,0);
		}
		public ParseKvOperatorContext parseKvOperator() {
			return getRuleContext(ParseKvOperatorContext.class,0);
		}
		public ParseWhereOperatorContext parseWhereOperator() {
			return getRuleContext(ParseWhereOperatorContext.class,0);
		}
		public PartitionOperatorContext partitionOperator() {
			return getRuleContext(PartitionOperatorContext.class,0);
		}
		public PartitionByOperatorContext partitionByOperator() {
			return getRuleContext(PartitionByOperatorContext.class,0);
		}
		public ProjectOperatorContext projectOperator() {
			return getRuleContext(ProjectOperatorContext.class,0);
		}
		public ProjectAwayOperatorContext projectAwayOperator() {
			return getRuleContext(ProjectAwayOperatorContext.class,0);
		}
		public ProjectRenameOperatorContext projectRenameOperator() {
			return getRuleContext(ProjectRenameOperatorContext.class,0);
		}
		public ProjectReorderOperatorContext projectReorderOperator() {
			return getRuleContext(ProjectReorderOperatorContext.class,0);
		}
		public ProjectKeepOperatorContext projectKeepOperator() {
			return getRuleContext(ProjectKeepOperatorContext.class,0);
		}
		public ReduceByOperatorContext reduceByOperator() {
			return getRuleContext(ReduceByOperatorContext.class,0);
		}
		public RenderOperatorContext renderOperator() {
			return getRuleContext(RenderOperatorContext.class,0);
		}
		public SampleOperatorContext sampleOperator() {
			return getRuleContext(SampleOperatorContext.class,0);
		}
		public SampleDistinctOperatorContext sampleDistinctOperator() {
			return getRuleContext(SampleDistinctOperatorContext.class,0);
		}
		public ScanOperatorContext scanOperator() {
			return getRuleContext(ScanOperatorContext.class,0);
		}
		public SearchOperatorContext searchOperator() {
			return getRuleContext(SearchOperatorContext.class,0);
		}
		public SerializeOperatorContext serializeOperator() {
			return getRuleContext(SerializeOperatorContext.class,0);
		}
		public SortOperatorContext sortOperator() {
			return getRuleContext(SortOperatorContext.class,0);
		}
		public SummarizeOperatorContext summarizeOperator() {
			return getRuleContext(SummarizeOperatorContext.class,0);
		}
		public TakeOperatorContext takeOperator() {
			return getRuleContext(TakeOperatorContext.class,0);
		}
		public TopHittersOperatorContext topHittersOperator() {
			return getRuleContext(TopHittersOperatorContext.class,0);
		}
		public TopOperatorContext topOperator() {
			return getRuleContext(TopOperatorContext.class,0);
		}
		public TopNestedOperatorContext topNestedOperator() {
			return getRuleContext(TopNestedOperatorContext.class,0);
		}
		public UnionOperatorContext unionOperator() {
			return getRuleContext(UnionOperatorContext.class,0);
		}
		public WhereOperatorContext whereOperator() {
			return getRuleContext(WhereOperatorContext.class,0);
		}
		public AfterPipeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_afterPipeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAfterPipeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAfterPipeOperator(this);
		}
	}

	public final AfterPipeOperatorContext afterPipeOperator() throws RecognitionException {
		AfterPipeOperatorContext _localctx = new AfterPipeOperatorContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_afterPipeOperator);
		try {
			setState(964);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AS:
				enterOuterAlt(_localctx, 1);
				{
				setState(915);
				asOperator();
				}
				break;
			case ASSERTSCHEMA:
				enterOuterAlt(_localctx, 2);
				{
				setState(916);
				assertSchemaOperator();
				}
				break;
			case CONSUME:
				enterOuterAlt(_localctx, 3);
				{
				setState(917);
				consumeOperator();
				}
				break;
			case COUNT:
				enterOuterAlt(_localctx, 4);
				{
				setState(918);
				countOperator();
				}
				break;
			case DISTINCT:
				enterOuterAlt(_localctx, 5);
				{
				setState(919);
				distinctOperator();
				}
				break;
			case EXECUTE_AND_CACHE:
				enterOuterAlt(_localctx, 6);
				{
				setState(920);
				executeAndCacheOperator();
				}
				break;
			case EXTEND:
				enterOuterAlt(_localctx, 7);
				{
				setState(921);
				extendOperator();
				}
				break;
			case FACET:
				enterOuterAlt(_localctx, 8);
				{
				setState(922);
				facetByOperator();
				}
				break;
			case FIND:
				enterOuterAlt(_localctx, 9);
				{
				setState(923);
				findOperator();
				}
				break;
			case FORK:
				enterOuterAlt(_localctx, 10);
				{
				setState(924);
				forkOperator();
				}
				break;
			case GETSCHEMA:
				enterOuterAlt(_localctx, 11);
				{
				setState(925);
				getSchemaOperator();
				}
				break;
			case GRAPHMARKCOMPONENTS:
				enterOuterAlt(_localctx, 12);
				{
				setState(926);
				graphMarkComponentsOperator();
				}
				break;
			case GRAPHMATCH:
				enterOuterAlt(_localctx, 13);
				{
				setState(927);
				graphMatchOperator();
				}
				break;
			case GRAPHMERGE:
				enterOuterAlt(_localctx, 14);
				{
				setState(928);
				graphMergeOperator();
				}
				break;
			case GRAPHSHORTESTPATHS:
				enterOuterAlt(_localctx, 15);
				{
				setState(929);
				graphShortestPathsOperator();
				}
				break;
			case GRAPHTOTABLE:
				enterOuterAlt(_localctx, 16);
				{
				setState(930);
				graphToTableOperator();
				}
				break;
			case INVOKE:
				enterOuterAlt(_localctx, 17);
				{
				setState(931);
				invokeOperator();
				}
				break;
			case JOIN:
				enterOuterAlt(_localctx, 18);
				{
				setState(932);
				joinOperator();
				}
				break;
			case LOOKUP:
				enterOuterAlt(_localctx, 19);
				{
				setState(933);
				lookupOperator();
				}
				break;
			case MAKEGRAPH:
				enterOuterAlt(_localctx, 20);
				{
				setState(934);
				makeGraphOperator();
				}
				break;
			case MAKESERIES:
				enterOuterAlt(_localctx, 21);
				{
				setState(935);
				makeSeriesOperator();
				}
				break;
			case MV_EXPAND:
			case MVEXPAND:
				enterOuterAlt(_localctx, 22);
				{
				setState(936);
				mvexpandOperator();
				}
				break;
			case MV_APPLY:
			case MVAPPLY:
				enterOuterAlt(_localctx, 23);
				{
				setState(937);
				mvapplyOperator();
				}
				break;
			case EVALUATE:
				enterOuterAlt(_localctx, 24);
				{
				setState(938);
				evaluateOperator();
				}
				break;
			case PARSE:
				enterOuterAlt(_localctx, 25);
				{
				setState(939);
				parseOperator();
				}
				break;
			case PARSEKV:
				enterOuterAlt(_localctx, 26);
				{
				setState(940);
				parseKvOperator();
				}
				break;
			case PARSEWHERE:
				enterOuterAlt(_localctx, 27);
				{
				setState(941);
				parseWhereOperator();
				}
				break;
			case PARTITION:
				enterOuterAlt(_localctx, 28);
				{
				setState(942);
				partitionOperator();
				}
				break;
			case PARTITIONBY:
				enterOuterAlt(_localctx, 29);
				{
				setState(943);
				partitionByOperator();
				}
				break;
			case PROJECT:
				enterOuterAlt(_localctx, 30);
				{
				setState(944);
				projectOperator();
				}
				break;
			case PROJECTAWAY:
				enterOuterAlt(_localctx, 31);
				{
				setState(945);
				projectAwayOperator();
				}
				break;
			case PROJECTRENAME:
				enterOuterAlt(_localctx, 32);
				{
				setState(946);
				projectRenameOperator();
				}
				break;
			case PROJECTREORDER:
				enterOuterAlt(_localctx, 33);
				{
				setState(947);
				projectReorderOperator();
				}
				break;
			case PROJECTKEEP:
				enterOuterAlt(_localctx, 34);
				{
				setState(948);
				projectKeepOperator();
				}
				break;
			case REDUCE:
				enterOuterAlt(_localctx, 35);
				{
				setState(949);
				reduceByOperator();
				}
				break;
			case RENDER:
				enterOuterAlt(_localctx, 36);
				{
				setState(950);
				renderOperator();
				}
				break;
			case SAMPLE:
				enterOuterAlt(_localctx, 37);
				{
				setState(951);
				sampleOperator();
				}
				break;
			case SAMPLE_DISTINCT:
				enterOuterAlt(_localctx, 38);
				{
				setState(952);
				sampleDistinctOperator();
				}
				break;
			case SCAN:
				enterOuterAlt(_localctx, 39);
				{
				setState(953);
				scanOperator();
				}
				break;
			case SEARCH:
				enterOuterAlt(_localctx, 40);
				{
				setState(954);
				searchOperator();
				}
				break;
			case SERIALIZE:
				enterOuterAlt(_localctx, 41);
				{
				setState(955);
				serializeOperator();
				}
				break;
			case ORDER:
			case SORT:
				enterOuterAlt(_localctx, 42);
				{
				setState(956);
				sortOperator();
				}
				break;
			case SUMMARIZE:
				enterOuterAlt(_localctx, 43);
				{
				setState(957);
				summarizeOperator();
				}
				break;
			case LIMIT:
			case TAKE:
				enterOuterAlt(_localctx, 44);
				{
				setState(958);
				takeOperator();
				}
				break;
			case TOP_HITTERS:
				enterOuterAlt(_localctx, 45);
				{
				setState(959);
				topHittersOperator();
				}
				break;
			case TOP:
				enterOuterAlt(_localctx, 46);
				{
				setState(960);
				topOperator();
				}
				break;
			case TOP_NESTED:
				enterOuterAlt(_localctx, 47);
				{
				setState(961);
				topNestedOperator();
				}
				break;
			case UNION:
				enterOuterAlt(_localctx, 48);
				{
				setState(962);
				unionOperator();
				}
				break;
			case FILTER:
			case WHERE:
				enterOuterAlt(_localctx, 49);
				{
				setState(963);
				whereOperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BeforeOrAfterPipeOperatorContext extends ParserRuleContext {
		public FindOperatorContext findOperator() {
			return getRuleContext(FindOperatorContext.class,0);
		}
		public SearchOperatorContext searchOperator() {
			return getRuleContext(SearchOperatorContext.class,0);
		}
		public UnionOperatorContext unionOperator() {
			return getRuleContext(UnionOperatorContext.class,0);
		}
		public EvaluateOperatorContext evaluateOperator() {
			return getRuleContext(EvaluateOperatorContext.class,0);
		}
		public BeforeOrAfterPipeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_beforeOrAfterPipeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterBeforeOrAfterPipeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitBeforeOrAfterPipeOperator(this);
		}
	}

	public final BeforeOrAfterPipeOperatorContext beforeOrAfterPipeOperator() throws RecognitionException {
		BeforeOrAfterPipeOperatorContext _localctx = new BeforeOrAfterPipeOperatorContext(_ctx, getState());
		enterRule(_localctx, 86, RULE_beforeOrAfterPipeOperator);
		try {
			setState(970);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FIND:
				enterOuterAlt(_localctx, 1);
				{
				setState(966);
				findOperator();
				}
				break;
			case SEARCH:
				enterOuterAlt(_localctx, 2);
				{
				setState(967);
				searchOperator();
				}
				break;
			case UNION:
				enterOuterAlt(_localctx, 3);
				{
				setState(968);
				unionOperator();
				}
				break;
			case EVALUATE:
				enterOuterAlt(_localctx, 4);
				{
				setState(969);
				evaluateOperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForkPipeOperatorContext extends ParserRuleContext {
		public CountOperatorContext countOperator() {
			return getRuleContext(CountOperatorContext.class,0);
		}
		public ExtendOperatorContext extendOperator() {
			return getRuleContext(ExtendOperatorContext.class,0);
		}
		public WhereOperatorContext whereOperator() {
			return getRuleContext(WhereOperatorContext.class,0);
		}
		public ParseOperatorContext parseOperator() {
			return getRuleContext(ParseOperatorContext.class,0);
		}
		public ParseWhereOperatorContext parseWhereOperator() {
			return getRuleContext(ParseWhereOperatorContext.class,0);
		}
		public TakeOperatorContext takeOperator() {
			return getRuleContext(TakeOperatorContext.class,0);
		}
		public TopNestedOperatorContext topNestedOperator() {
			return getRuleContext(TopNestedOperatorContext.class,0);
		}
		public ProjectOperatorContext projectOperator() {
			return getRuleContext(ProjectOperatorContext.class,0);
		}
		public ProjectAwayOperatorContext projectAwayOperator() {
			return getRuleContext(ProjectAwayOperatorContext.class,0);
		}
		public ProjectRenameOperatorContext projectRenameOperator() {
			return getRuleContext(ProjectRenameOperatorContext.class,0);
		}
		public ProjectReorderOperatorContext projectReorderOperator() {
			return getRuleContext(ProjectReorderOperatorContext.class,0);
		}
		public ProjectKeepOperatorContext projectKeepOperator() {
			return getRuleContext(ProjectKeepOperatorContext.class,0);
		}
		public SummarizeOperatorContext summarizeOperator() {
			return getRuleContext(SummarizeOperatorContext.class,0);
		}
		public DistinctOperatorContext distinctOperator() {
			return getRuleContext(DistinctOperatorContext.class,0);
		}
		public TopHittersOperatorContext topHittersOperator() {
			return getRuleContext(TopHittersOperatorContext.class,0);
		}
		public TopOperatorContext topOperator() {
			return getRuleContext(TopOperatorContext.class,0);
		}
		public SortOperatorContext sortOperator() {
			return getRuleContext(SortOperatorContext.class,0);
		}
		public MvexpandOperatorContext mvexpandOperator() {
			return getRuleContext(MvexpandOperatorContext.class,0);
		}
		public ReduceByOperatorContext reduceByOperator() {
			return getRuleContext(ReduceByOperatorContext.class,0);
		}
		public SampleOperatorContext sampleOperator() {
			return getRuleContext(SampleOperatorContext.class,0);
		}
		public SampleDistinctOperatorContext sampleDistinctOperator() {
			return getRuleContext(SampleDistinctOperatorContext.class,0);
		}
		public AsOperatorContext asOperator() {
			return getRuleContext(AsOperatorContext.class,0);
		}
		public InvokeOperatorContext invokeOperator() {
			return getRuleContext(InvokeOperatorContext.class,0);
		}
		public ExecuteAndCacheOperatorContext executeAndCacheOperator() {
			return getRuleContext(ExecuteAndCacheOperatorContext.class,0);
		}
		public ScanOperatorContext scanOperator() {
			return getRuleContext(ScanOperatorContext.class,0);
		}
		public ForkPipeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forkPipeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterForkPipeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitForkPipeOperator(this);
		}
	}

	public final ForkPipeOperatorContext forkPipeOperator() throws RecognitionException {
		ForkPipeOperatorContext _localctx = new ForkPipeOperatorContext(_ctx, getState());
		enterRule(_localctx, 88, RULE_forkPipeOperator);
		try {
			setState(997);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case COUNT:
				enterOuterAlt(_localctx, 1);
				{
				setState(972);
				countOperator();
				}
				break;
			case EXTEND:
				enterOuterAlt(_localctx, 2);
				{
				setState(973);
				extendOperator();
				}
				break;
			case FILTER:
			case WHERE:
				enterOuterAlt(_localctx, 3);
				{
				setState(974);
				whereOperator();
				}
				break;
			case PARSE:
				enterOuterAlt(_localctx, 4);
				{
				setState(975);
				parseOperator();
				}
				break;
			case PARSEWHERE:
				enterOuterAlt(_localctx, 5);
				{
				setState(976);
				parseWhereOperator();
				}
				break;
			case LIMIT:
			case TAKE:
				enterOuterAlt(_localctx, 6);
				{
				setState(977);
				takeOperator();
				}
				break;
			case TOP_NESTED:
				enterOuterAlt(_localctx, 7);
				{
				setState(978);
				topNestedOperator();
				}
				break;
			case PROJECT:
				enterOuterAlt(_localctx, 8);
				{
				setState(979);
				projectOperator();
				}
				break;
			case PROJECTAWAY:
				enterOuterAlt(_localctx, 9);
				{
				setState(980);
				projectAwayOperator();
				}
				break;
			case PROJECTRENAME:
				enterOuterAlt(_localctx, 10);
				{
				setState(981);
				projectRenameOperator();
				}
				break;
			case PROJECTREORDER:
				enterOuterAlt(_localctx, 11);
				{
				setState(982);
				projectReorderOperator();
				}
				break;
			case PROJECTKEEP:
				enterOuterAlt(_localctx, 12);
				{
				setState(983);
				projectKeepOperator();
				}
				break;
			case SUMMARIZE:
				enterOuterAlt(_localctx, 13);
				{
				setState(984);
				summarizeOperator();
				}
				break;
			case DISTINCT:
				enterOuterAlt(_localctx, 14);
				{
				setState(985);
				distinctOperator();
				}
				break;
			case TOP_HITTERS:
				enterOuterAlt(_localctx, 15);
				{
				setState(986);
				topHittersOperator();
				}
				break;
			case TOP:
				enterOuterAlt(_localctx, 16);
				{
				setState(987);
				topOperator();
				}
				break;
			case ORDER:
			case SORT:
				enterOuterAlt(_localctx, 17);
				{
				setState(988);
				sortOperator();
				}
				break;
			case MV_EXPAND:
			case MVEXPAND:
				enterOuterAlt(_localctx, 18);
				{
				setState(989);
				mvexpandOperator();
				}
				break;
			case REDUCE:
				enterOuterAlt(_localctx, 19);
				{
				setState(990);
				reduceByOperator();
				}
				break;
			case SAMPLE:
				enterOuterAlt(_localctx, 20);
				{
				setState(991);
				sampleOperator();
				}
				break;
			case SAMPLE_DISTINCT:
				enterOuterAlt(_localctx, 21);
				{
				setState(992);
				sampleDistinctOperator();
				}
				break;
			case AS:
				enterOuterAlt(_localctx, 22);
				{
				setState(993);
				asOperator();
				}
				break;
			case INVOKE:
				enterOuterAlt(_localctx, 23);
				{
				setState(994);
				invokeOperator();
				}
				break;
			case EXECUTE_AND_CACHE:
				enterOuterAlt(_localctx, 24);
				{
				setState(995);
				executeAndCacheOperator();
				}
				break;
			case SCAN:
				enterOuterAlt(_localctx, 25);
				{
				setState(996);
				scanOperator();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode AS() { return getToken(HqlParser.AS, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public AsOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAsOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAsOperator(this);
		}
	}

	public final AsOperatorContext asOperator() throws RecognitionException {
		AsOperatorContext _localctx = new AsOperatorContext(_ctx, getState());
		enterRule(_localctx, 90, RULE_asOperator);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(999);
			match(AS);
			setState(1003);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1000);
					((AsOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((AsOperatorContext)_localctx).Parameters.add(((AsOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1005);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			}
			setState(1006);
			((AsOperatorContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssertSchemaOperatorContext extends ParserRuleContext {
		public RowSchemaContext Schema;
		public TerminalNode ASSERTSCHEMA() { return getToken(HqlParser.ASSERTSCHEMA, 0); }
		public RowSchemaContext rowSchema() {
			return getRuleContext(RowSchemaContext.class,0);
		}
		public AssertSchemaOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assertSchemaOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAssertSchemaOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAssertSchemaOperator(this);
		}
	}

	public final AssertSchemaOperatorContext assertSchemaOperator() throws RecognitionException {
		AssertSchemaOperatorContext _localctx = new AssertSchemaOperatorContext(_ctx, getState());
		enterRule(_localctx, 92, RULE_assertSchemaOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1008);
			match(ASSERTSCHEMA);
			setState(1009);
			((AssertSchemaOperatorContext)_localctx).Schema = rowSchema();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConsumeOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public TerminalNode CONSUME() { return getToken(HqlParser.CONSUME, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public ConsumeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_consumeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterConsumeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitConsumeOperator(this);
		}
	}

	public final ConsumeOperatorContext consumeOperator() throws RecognitionException {
		ConsumeOperatorContext _localctx = new ConsumeOperatorContext(_ctx, getState());
		enterRule(_localctx, 94, RULE_consumeOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1011);
			match(CONSUME);
			setState(1015);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1012);
				((ConsumeOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((ConsumeOperatorContext)_localctx).Parameters.add(((ConsumeOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1017);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CountOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public TerminalNode COUNT() { return getToken(HqlParser.COUNT, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public CountOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_countOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterCountOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitCountOperator(this);
		}
	}

	public final CountOperatorContext countOperator() throws RecognitionException {
		CountOperatorContext _localctx = new CountOperatorContext(_ctx, getState());
		enterRule(_localctx, 96, RULE_countOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1018);
			match(COUNT);
			setState(1022);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1019);
				((CountOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((CountOperatorContext)_localctx).Parameters.add(((CountOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1024);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CountOperatorAsClauseContext extends ParserRuleContext {
		public IdentifierNameContext Name;
		public TerminalNode AS() { return getToken(HqlParser.AS, 0); }
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public CountOperatorAsClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_countOperatorAsClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterCountOperatorAsClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitCountOperatorAsClause(this);
		}
	}

	public final CountOperatorAsClauseContext countOperatorAsClause() throws RecognitionException {
		CountOperatorAsClauseContext _localctx = new CountOperatorAsClauseContext(_ctx, getState());
		enterRule(_localctx, 98, RULE_countOperatorAsClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1025);
			match(AS);
			setState(1026);
			((CountOperatorAsClauseContext)_localctx).Name = identifierName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DistinctOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public DistinctOperatorStarTargetContext Star;
		public DistinctOperatorColumnListTargetContext ColumnList;
		public TerminalNode DISTINCT() { return getToken(HqlParser.DISTINCT, 0); }
		public DistinctOperatorStarTargetContext distinctOperatorStarTarget() {
			return getRuleContext(DistinctOperatorStarTargetContext.class,0);
		}
		public DistinctOperatorColumnListTargetContext distinctOperatorColumnListTarget() {
			return getRuleContext(DistinctOperatorColumnListTargetContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public DistinctOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_distinctOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDistinctOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDistinctOperator(this);
		}
	}

	public final DistinctOperatorContext distinctOperator() throws RecognitionException {
		DistinctOperatorContext _localctx = new DistinctOperatorContext(_ctx, getState());
		enterRule(_localctx, 100, RULE_distinctOperator);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1028);
			match(DISTINCT);
			setState(1032);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1029);
					((DistinctOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((DistinctOperatorContext)_localctx).Parameters.add(((DistinctOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1034);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,38,_ctx);
			}
			setState(1037);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,39,_ctx) ) {
			case 1:
				{
				setState(1035);
				((DistinctOperatorContext)_localctx).Star = distinctOperatorStarTarget();
				}
				break;
			case 2:
				{
				setState(1036);
				((DistinctOperatorContext)_localctx).ColumnList = distinctOperatorColumnListTarget();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DistinctOperatorStarTargetContext extends ParserRuleContext {
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public DistinctOperatorStarTargetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_distinctOperatorStarTarget; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDistinctOperatorStarTarget(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDistinctOperatorStarTarget(this);
		}
	}

	public final DistinctOperatorStarTargetContext distinctOperatorStarTarget() throws RecognitionException {
		DistinctOperatorStarTargetContext _localctx = new DistinctOperatorStarTargetContext(_ctx, getState());
		enterRule(_localctx, 102, RULE_distinctOperatorStarTarget);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1039);
			match(ASTERISK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DistinctOperatorColumnListTargetContext extends ParserRuleContext {
		public UnnamedExpressionContext unnamedExpression;
		public List<UnnamedExpressionContext> Expressions = new ArrayList<UnnamedExpressionContext>();
		public List<UnnamedExpressionContext> unnamedExpression() {
			return getRuleContexts(UnnamedExpressionContext.class);
		}
		public UnnamedExpressionContext unnamedExpression(int i) {
			return getRuleContext(UnnamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public DistinctOperatorColumnListTargetContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_distinctOperatorColumnListTarget; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDistinctOperatorColumnListTarget(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDistinctOperatorColumnListTarget(this);
		}
	}

	public final DistinctOperatorColumnListTargetContext distinctOperatorColumnListTarget() throws RecognitionException {
		DistinctOperatorColumnListTargetContext _localctx = new DistinctOperatorColumnListTargetContext(_ctx, getState());
		enterRule(_localctx, 104, RULE_distinctOperatorColumnListTarget);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1041);
			((DistinctOperatorColumnListTargetContext)_localctx).unnamedExpression = unnamedExpression();
			((DistinctOperatorColumnListTargetContext)_localctx).Expressions.add(((DistinctOperatorColumnListTargetContext)_localctx).unnamedExpression);
			setState(1046);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1042);
				match(COMMA);
				setState(1043);
				((DistinctOperatorColumnListTargetContext)_localctx).unnamedExpression = unnamedExpression();
				((DistinctOperatorColumnListTargetContext)_localctx).Expressions.add(((DistinctOperatorColumnListTargetContext)_localctx).unnamedExpression);
				}
				}
				setState(1048);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EvaluateOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public FunctionCallExpressionContext PlugInCall;
		public EvaluateOperatorSchemaClauseContext SchemaClause;
		public TerminalNode EVALUATE() { return getToken(HqlParser.EVALUATE, 0); }
		public FunctionCallExpressionContext functionCallExpression() {
			return getRuleContext(FunctionCallExpressionContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public EvaluateOperatorSchemaClauseContext evaluateOperatorSchemaClause() {
			return getRuleContext(EvaluateOperatorSchemaClauseContext.class,0);
		}
		public EvaluateOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_evaluateOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEvaluateOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEvaluateOperator(this);
		}
	}

	public final EvaluateOperatorContext evaluateOperator() throws RecognitionException {
		EvaluateOperatorContext _localctx = new EvaluateOperatorContext(_ctx, getState());
		enterRule(_localctx, 106, RULE_evaluateOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1049);
			match(EVALUATE);
			setState(1053);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1050);
					((EvaluateOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((EvaluateOperatorContext)_localctx).Parameters.add(((EvaluateOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1055);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,41,_ctx);
			}
			setState(1056);
			((EvaluateOperatorContext)_localctx).PlugInCall = functionCallExpression();
			setState(1058);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(1057);
				((EvaluateOperatorContext)_localctx).SchemaClause = evaluateOperatorSchemaClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EvaluateOperatorSchemaClauseContext extends ParserRuleContext {
		public RowSchemaContext Schema;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public RowSchemaContext rowSchema() {
			return getRuleContext(RowSchemaContext.class,0);
		}
		public EvaluateOperatorSchemaClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_evaluateOperatorSchemaClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEvaluateOperatorSchemaClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEvaluateOperatorSchemaClause(this);
		}
	}

	public final EvaluateOperatorSchemaClauseContext evaluateOperatorSchemaClause() throws RecognitionException {
		EvaluateOperatorSchemaClauseContext _localctx = new EvaluateOperatorSchemaClauseContext(_ctx, getState());
		enterRule(_localctx, 108, RULE_evaluateOperatorSchemaClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1060);
			match(COLON);
			setState(1061);
			((EvaluateOperatorSchemaClauseContext)_localctx).Schema = rowSchema();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExtendOperatorContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode EXTEND() { return getToken(HqlParser.EXTEND, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ExtendOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extendOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExtendOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExtendOperator(this);
		}
	}

	public final ExtendOperatorContext extendOperator() throws RecognitionException {
		ExtendOperatorContext _localctx = new ExtendOperatorContext(_ctx, getState());
		enterRule(_localctx, 110, RULE_extendOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1063);
			match(EXTEND);
			setState(1064);
			((ExtendOperatorContext)_localctx).namedExpression = namedExpression();
			((ExtendOperatorContext)_localctx).Expressions.add(((ExtendOperatorContext)_localctx).namedExpression);
			setState(1069);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1065);
				match(COMMA);
				setState(1066);
				((ExtendOperatorContext)_localctx).namedExpression = namedExpression();
				((ExtendOperatorContext)_localctx).Expressions.add(((ExtendOperatorContext)_localctx).namedExpression);
				}
				}
				setState(1071);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExecuteAndCacheOperatorContext extends ParserRuleContext {
		public TerminalNode EXECUTE_AND_CACHE() { return getToken(HqlParser.EXECUTE_AND_CACHE, 0); }
		public ExecuteAndCacheOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_executeAndCacheOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExecuteAndCacheOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExecuteAndCacheOperator(this);
		}
	}

	public final ExecuteAndCacheOperatorContext executeAndCacheOperator() throws RecognitionException {
		ExecuteAndCacheOperatorContext _localctx = new ExecuteAndCacheOperatorContext(_ctx, getState());
		enterRule(_localctx, 112, RULE_executeAndCacheOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1072);
			match(EXECUTE_AND_CACHE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FacetByOperatorContext extends ParserRuleContext {
		public EntityExpressionContext entityExpression;
		public List<EntityExpressionContext> Entities = new ArrayList<EntityExpressionContext>();
		public FacetByOperatorWithOperatorClauseContext WithOperatorClause;
		public FacetByOperatorWithExpressionClauseContext WithExpressionClause;
		public TerminalNode FACET() { return getToken(HqlParser.FACET, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<EntityExpressionContext> entityExpression() {
			return getRuleContexts(EntityExpressionContext.class);
		}
		public EntityExpressionContext entityExpression(int i) {
			return getRuleContext(EntityExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public FacetByOperatorWithOperatorClauseContext facetByOperatorWithOperatorClause() {
			return getRuleContext(FacetByOperatorWithOperatorClauseContext.class,0);
		}
		public FacetByOperatorWithExpressionClauseContext facetByOperatorWithExpressionClause() {
			return getRuleContext(FacetByOperatorWithExpressionClauseContext.class,0);
		}
		public FacetByOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_facetByOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFacetByOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFacetByOperator(this);
		}
	}

	public final FacetByOperatorContext facetByOperator() throws RecognitionException {
		FacetByOperatorContext _localctx = new FacetByOperatorContext(_ctx, getState());
		enterRule(_localctx, 114, RULE_facetByOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1074);
			match(FACET);
			setState(1075);
			match(BY);
			setState(1076);
			((FacetByOperatorContext)_localctx).entityExpression = entityExpression();
			((FacetByOperatorContext)_localctx).Entities.add(((FacetByOperatorContext)_localctx).entityExpression);
			setState(1081);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1077);
				match(COMMA);
				setState(1078);
				((FacetByOperatorContext)_localctx).entityExpression = entityExpression();
				((FacetByOperatorContext)_localctx).Entities.add(((FacetByOperatorContext)_localctx).entityExpression);
				}
				}
				setState(1083);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1086);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,45,_ctx) ) {
			case 1:
				{
				setState(1084);
				((FacetByOperatorContext)_localctx).WithOperatorClause = facetByOperatorWithOperatorClause();
				}
				break;
			case 2:
				{
				setState(1085);
				((FacetByOperatorContext)_localctx).WithExpressionClause = facetByOperatorWithExpressionClause();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FacetByOperatorWithOperatorClauseContext extends ParserRuleContext {
		public ForkPipeOperatorContext Operator;
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public ForkPipeOperatorContext forkPipeOperator() {
			return getRuleContext(ForkPipeOperatorContext.class,0);
		}
		public FacetByOperatorWithOperatorClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_facetByOperatorWithOperatorClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFacetByOperatorWithOperatorClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFacetByOperatorWithOperatorClause(this);
		}
	}

	public final FacetByOperatorWithOperatorClauseContext facetByOperatorWithOperatorClause() throws RecognitionException {
		FacetByOperatorWithOperatorClauseContext _localctx = new FacetByOperatorWithOperatorClauseContext(_ctx, getState());
		enterRule(_localctx, 116, RULE_facetByOperatorWithOperatorClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1088);
			match(WITH);
			setState(1089);
			((FacetByOperatorWithOperatorClauseContext)_localctx).Operator = forkPipeOperator();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FacetByOperatorWithExpressionClauseContext extends ParserRuleContext {
		public ForkOperatorExpressionContext Expression;
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public ForkOperatorExpressionContext forkOperatorExpression() {
			return getRuleContext(ForkOperatorExpressionContext.class,0);
		}
		public FacetByOperatorWithExpressionClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_facetByOperatorWithExpressionClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFacetByOperatorWithExpressionClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFacetByOperatorWithExpressionClause(this);
		}
	}

	public final FacetByOperatorWithExpressionClauseContext facetByOperatorWithExpressionClause() throws RecognitionException {
		FacetByOperatorWithExpressionClauseContext _localctx = new FacetByOperatorWithExpressionClauseContext(_ctx, getState());
		enterRule(_localctx, 118, RULE_facetByOperatorWithExpressionClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1091);
			match(WITH);
			setState(1092);
			match(OPENPAREN);
			setState(1093);
			((FacetByOperatorWithExpressionClauseContext)_localctx).Expression = forkOperatorExpression();
			setState(1094);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorContext extends ParserRuleContext {
		public DataScopeClauseContext DataScopeClause;
		public FindOperatorParametersWhereClauseContext ParameterWhereClause;
		public UnnamedExpressionContext Expression;
		public FindOperatorProjectClauseContext ProjectClause;
		public FindOperatorProjectSmartClauseContext ProjectSmartClause;
		public FindOperatorProjectAwayClauseContext ProjectAwayClause;
		public TerminalNode FIND() { return getToken(HqlParser.FIND, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public DataScopeClauseContext dataScopeClause() {
			return getRuleContext(DataScopeClauseContext.class,0);
		}
		public FindOperatorParametersWhereClauseContext findOperatorParametersWhereClause() {
			return getRuleContext(FindOperatorParametersWhereClauseContext.class,0);
		}
		public FindOperatorProjectClauseContext findOperatorProjectClause() {
			return getRuleContext(FindOperatorProjectClauseContext.class,0);
		}
		public FindOperatorProjectSmartClauseContext findOperatorProjectSmartClause() {
			return getRuleContext(FindOperatorProjectSmartClauseContext.class,0);
		}
		public FindOperatorProjectAwayClauseContext findOperatorProjectAwayClause() {
			return getRuleContext(FindOperatorProjectAwayClauseContext.class,0);
		}
		public FindOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperator(this);
		}
	}

	public final FindOperatorContext findOperator() throws RecognitionException {
		FindOperatorContext _localctx = new FindOperatorContext(_ctx, getState());
		enterRule(_localctx, 120, RULE_findOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1096);
			match(FIND);
			setState(1098);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DATASCOPE) {
				{
				setState(1097);
				((FindOperatorContext)_localctx).DataScopeClause = dataScopeClause();
				}
			}

			setState(1101);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,47,_ctx) ) {
			case 1:
				{
				setState(1100);
				((FindOperatorContext)_localctx).ParameterWhereClause = findOperatorParametersWhereClause();
				}
				break;
			}
			setState(1103);
			((FindOperatorContext)_localctx).Expression = unnamedExpression();
			setState(1106);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,48,_ctx) ) {
			case 1:
				{
				setState(1104);
				((FindOperatorContext)_localctx).ProjectClause = findOperatorProjectClause();
				}
				break;
			case 2:
				{
				setState(1105);
				((FindOperatorContext)_localctx).ProjectSmartClause = findOperatorProjectSmartClause();
				}
				break;
			}
			setState(1109);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PROJECTAWAY_) {
				{
				setState(1108);
				((FindOperatorContext)_localctx).ProjectAwayClause = findOperatorProjectAwayClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorParametersWhereClauseContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public FindOperatorInClauseContext InClause;
		public TerminalNode WHERE() { return getToken(HqlParser.WHERE, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public FindOperatorInClauseContext findOperatorInClause() {
			return getRuleContext(FindOperatorInClauseContext.class,0);
		}
		public FindOperatorParametersWhereClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorParametersWhereClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorParametersWhereClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorParametersWhereClause(this);
		}
	}

	public final FindOperatorParametersWhereClauseContext findOperatorParametersWhereClause() throws RecognitionException {
		FindOperatorParametersWhereClauseContext _localctx = new FindOperatorParametersWhereClauseContext(_ctx, getState());
		enterRule(_localctx, 122, RULE_findOperatorParametersWhereClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1114);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1111);
				((FindOperatorParametersWhereClauseContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((FindOperatorParametersWhereClauseContext)_localctx).Parameters.add(((FindOperatorParametersWhereClauseContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1116);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1118);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IN) {
				{
				setState(1117);
				((FindOperatorParametersWhereClauseContext)_localctx).InClause = findOperatorInClause();
				}
			}

			setState(1120);
			match(WHERE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorInClauseContext extends ParserRuleContext {
		public FindOperatorSourceContext findOperatorSource;
		public List<FindOperatorSourceContext> Expressions = new ArrayList<FindOperatorSourceContext>();
		public TerminalNode IN() { return getToken(HqlParser.IN, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<FindOperatorSourceContext> findOperatorSource() {
			return getRuleContexts(FindOperatorSourceContext.class);
		}
		public FindOperatorSourceContext findOperatorSource(int i) {
			return getRuleContext(FindOperatorSourceContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public FindOperatorInClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorInClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorInClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorInClause(this);
		}
	}

	public final FindOperatorInClauseContext findOperatorInClause() throws RecognitionException {
		FindOperatorInClauseContext _localctx = new FindOperatorInClauseContext(_ctx, getState());
		enterRule(_localctx, 124, RULE_findOperatorInClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1122);
			match(IN);
			setState(1123);
			match(OPENPAREN);
			setState(1124);
			((FindOperatorInClauseContext)_localctx).findOperatorSource = findOperatorSource();
			((FindOperatorInClauseContext)_localctx).Expressions.add(((FindOperatorInClauseContext)_localctx).findOperatorSource);
			setState(1129);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1125);
				match(COMMA);
				setState(1126);
				((FindOperatorInClauseContext)_localctx).findOperatorSource = findOperatorSource();
				((FindOperatorInClauseContext)_localctx).Expressions.add(((FindOperatorInClauseContext)_localctx).findOperatorSource);
				}
				}
				setState(1131);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1132);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorProjectClauseContext extends ParserRuleContext {
		public FindOperatorProjectExpressionContext findOperatorProjectExpression;
		public List<FindOperatorProjectExpressionContext> Expressions = new ArrayList<FindOperatorProjectExpressionContext>();
		public TerminalNode PROJECT() { return getToken(HqlParser.PROJECT, 0); }
		public List<FindOperatorProjectExpressionContext> findOperatorProjectExpression() {
			return getRuleContexts(FindOperatorProjectExpressionContext.class);
		}
		public FindOperatorProjectExpressionContext findOperatorProjectExpression(int i) {
			return getRuleContext(FindOperatorProjectExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public FindOperatorProjectClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorProjectClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorProjectClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorProjectClause(this);
		}
	}

	public final FindOperatorProjectClauseContext findOperatorProjectClause() throws RecognitionException {
		FindOperatorProjectClauseContext _localctx = new FindOperatorProjectClauseContext(_ctx, getState());
		enterRule(_localctx, 126, RULE_findOperatorProjectClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1134);
			match(PROJECT);
			setState(1135);
			((FindOperatorProjectClauseContext)_localctx).findOperatorProjectExpression = findOperatorProjectExpression();
			((FindOperatorProjectClauseContext)_localctx).Expressions.add(((FindOperatorProjectClauseContext)_localctx).findOperatorProjectExpression);
			setState(1140);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1136);
				match(COMMA);
				setState(1137);
				((FindOperatorProjectClauseContext)_localctx).findOperatorProjectExpression = findOperatorProjectExpression();
				((FindOperatorProjectClauseContext)_localctx).Expressions.add(((FindOperatorProjectClauseContext)_localctx).findOperatorProjectExpression);
				}
				}
				setState(1142);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorProjectExpressionContext extends ParserRuleContext {
		public FindOperatorColumnExpressionContext Column;
		public FindOperatorPackExpressionContext Pack;
		public FindOperatorColumnExpressionContext findOperatorColumnExpression() {
			return getRuleContext(FindOperatorColumnExpressionContext.class,0);
		}
		public FindOperatorPackExpressionContext findOperatorPackExpression() {
			return getRuleContext(FindOperatorPackExpressionContext.class,0);
		}
		public FindOperatorProjectExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorProjectExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorProjectExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorProjectExpression(this);
		}
	}

	public final FindOperatorProjectExpressionContext findOperatorProjectExpression() throws RecognitionException {
		FindOperatorProjectExpressionContext _localctx = new FindOperatorProjectExpressionContext(_ctx, getState());
		enterRule(_localctx, 128, RULE_findOperatorProjectExpression);
		try {
			setState(1145);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,54,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1143);
				((FindOperatorProjectExpressionContext)_localctx).Column = findOperatorColumnExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1144);
				((FindOperatorProjectExpressionContext)_localctx).Pack = findOperatorPackExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorColumnExpressionContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public FindOperatorOptionalColumnTypeContext OptionalType;
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public FindOperatorOptionalColumnTypeContext findOperatorOptionalColumnType() {
			return getRuleContext(FindOperatorOptionalColumnTypeContext.class,0);
		}
		public FindOperatorColumnExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorColumnExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorColumnExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorColumnExpression(this);
		}
	}

	public final FindOperatorColumnExpressionContext findOperatorColumnExpression() throws RecognitionException {
		FindOperatorColumnExpressionContext _localctx = new FindOperatorColumnExpressionContext(_ctx, getState());
		enterRule(_localctx, 130, RULE_findOperatorColumnExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1147);
			((FindOperatorColumnExpressionContext)_localctx).Name = parameterName();
			setState(1149);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(1148);
				((FindOperatorColumnExpressionContext)_localctx).OptionalType = findOperatorOptionalColumnType();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorOptionalColumnTypeContext extends ParserRuleContext {
		public ExtendedScalarTypeContext Type;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ExtendedScalarTypeContext extendedScalarType() {
			return getRuleContext(ExtendedScalarTypeContext.class,0);
		}
		public FindOperatorOptionalColumnTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorOptionalColumnType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorOptionalColumnType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorOptionalColumnType(this);
		}
	}

	public final FindOperatorOptionalColumnTypeContext findOperatorOptionalColumnType() throws RecognitionException {
		FindOperatorOptionalColumnTypeContext _localctx = new FindOperatorOptionalColumnTypeContext(_ctx, getState());
		enterRule(_localctx, 132, RULE_findOperatorOptionalColumnType);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1151);
			match(COLON);
			setState(1152);
			((FindOperatorOptionalColumnTypeContext)_localctx).Type = extendedScalarType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorPackExpressionContext extends ParserRuleContext {
		public TerminalNode PACK() { return getToken(HqlParser.PACK, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public FindOperatorPackExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorPackExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorPackExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorPackExpression(this);
		}
	}

	public final FindOperatorPackExpressionContext findOperatorPackExpression() throws RecognitionException {
		FindOperatorPackExpressionContext _localctx = new FindOperatorPackExpressionContext(_ctx, getState());
		enterRule(_localctx, 134, RULE_findOperatorPackExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1154);
			match(PACK);
			setState(1155);
			match(OPENPAREN);
			setState(1156);
			match(ASTERISK);
			setState(1157);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorProjectSmartClauseContext extends ParserRuleContext {
		public TerminalNode PROJECTSMART() { return getToken(HqlParser.PROJECTSMART, 0); }
		public FindOperatorProjectSmartClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorProjectSmartClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorProjectSmartClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorProjectSmartClause(this);
		}
	}

	public final FindOperatorProjectSmartClauseContext findOperatorProjectSmartClause() throws RecognitionException {
		FindOperatorProjectSmartClauseContext _localctx = new FindOperatorProjectSmartClauseContext(_ctx, getState());
		enterRule(_localctx, 136, RULE_findOperatorProjectSmartClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1159);
			match(PROJECTSMART);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorProjectAwayClauseContext extends ParserRuleContext {
		public FindOperatorProjectAwayStarContext Star;
		public FindOperatorProjectAwayColumnListContext ColumnList;
		public TerminalNode PROJECTAWAY_() { return getToken(HqlParser.PROJECTAWAY_, 0); }
		public FindOperatorProjectAwayStarContext findOperatorProjectAwayStar() {
			return getRuleContext(FindOperatorProjectAwayStarContext.class,0);
		}
		public FindOperatorProjectAwayColumnListContext findOperatorProjectAwayColumnList() {
			return getRuleContext(FindOperatorProjectAwayColumnListContext.class,0);
		}
		public FindOperatorProjectAwayClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorProjectAwayClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorProjectAwayClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorProjectAwayClause(this);
		}
	}

	public final FindOperatorProjectAwayClauseContext findOperatorProjectAwayClause() throws RecognitionException {
		FindOperatorProjectAwayClauseContext _localctx = new FindOperatorProjectAwayClauseContext(_ctx, getState());
		enterRule(_localctx, 138, RULE_findOperatorProjectAwayClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1161);
			match(PROJECTAWAY_);
			setState(1164);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ASTERISK:
				{
				setState(1162);
				((FindOperatorProjectAwayClauseContext)_localctx).Star = findOperatorProjectAwayStar();
				}
				break;
			case OPENBRACKET:
			case ACCESS:
			case ACCUMULATE:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AS:
			case AXES:
			case BASE:
			case BIN:
			case BY:
			case CLUSTER:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATABASE:
			case DATATABLE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case DISTINCT:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case EXTEND:
			case EXTERNALDATA:
			case FACET:
			case FILTER:
			case FIND:
			case FORK:
			case FROM:
			case HAS:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case IN:
			case INTO:
			case INVOKE:
			case LEGEND:
			case LET:
			case LIMIT:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case MATERIALIZE:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case OF:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARSE:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case PRINT:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SERIES:
			case SET:
			case SORT:
			case STACKED:
			case STACKED100:
			case STEP:
			case SUMMARIZE:
			case TAKE:
			case THRESHOLD:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WHERE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(1163);
				((FindOperatorProjectAwayClauseContext)_localctx).ColumnList = findOperatorProjectAwayColumnList();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorProjectAwayStarContext extends ParserRuleContext {
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public FindOperatorProjectAwayStarContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorProjectAwayStar; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorProjectAwayStar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorProjectAwayStar(this);
		}
	}

	public final FindOperatorProjectAwayStarContext findOperatorProjectAwayStar() throws RecognitionException {
		FindOperatorProjectAwayStarContext _localctx = new FindOperatorProjectAwayStarContext(_ctx, getState());
		enterRule(_localctx, 140, RULE_findOperatorProjectAwayStar);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1166);
			match(ASTERISK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorProjectAwayColumnListContext extends ParserRuleContext {
		public FindOperatorColumnExpressionContext findOperatorColumnExpression;
		public List<FindOperatorColumnExpressionContext> Columns = new ArrayList<FindOperatorColumnExpressionContext>();
		public List<FindOperatorColumnExpressionContext> findOperatorColumnExpression() {
			return getRuleContexts(FindOperatorColumnExpressionContext.class);
		}
		public FindOperatorColumnExpressionContext findOperatorColumnExpression(int i) {
			return getRuleContext(FindOperatorColumnExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public FindOperatorProjectAwayColumnListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorProjectAwayColumnList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorProjectAwayColumnList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorProjectAwayColumnList(this);
		}
	}

	public final FindOperatorProjectAwayColumnListContext findOperatorProjectAwayColumnList() throws RecognitionException {
		FindOperatorProjectAwayColumnListContext _localctx = new FindOperatorProjectAwayColumnListContext(_ctx, getState());
		enterRule(_localctx, 142, RULE_findOperatorProjectAwayColumnList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1168);
			((FindOperatorProjectAwayColumnListContext)_localctx).findOperatorColumnExpression = findOperatorColumnExpression();
			((FindOperatorProjectAwayColumnListContext)_localctx).Columns.add(((FindOperatorProjectAwayColumnListContext)_localctx).findOperatorColumnExpression);
			setState(1173);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1169);
				match(COMMA);
				setState(1170);
				((FindOperatorProjectAwayColumnListContext)_localctx).findOperatorColumnExpression = findOperatorColumnExpression();
				((FindOperatorProjectAwayColumnListContext)_localctx).Columns.add(((FindOperatorProjectAwayColumnListContext)_localctx).findOperatorColumnExpression);
				}
				}
				setState(1175);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorSourceContext extends ParserRuleContext {
		public FindOperatorSourceEntityExpressionContext Entity;
		public WildcardedEntityExpressionContext WildcardedEntity;
		public FindOperatorSourceEntityExpressionContext findOperatorSourceEntityExpression() {
			return getRuleContext(FindOperatorSourceEntityExpressionContext.class,0);
		}
		public WildcardedEntityExpressionContext wildcardedEntityExpression() {
			return getRuleContext(WildcardedEntityExpressionContext.class,0);
		}
		public FindOperatorSourceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorSource; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorSource(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorSource(this);
		}
	}

	public final FindOperatorSourceContext findOperatorSource() throws RecognitionException {
		FindOperatorSourceContext _localctx = new FindOperatorSourceContext(_ctx, getState());
		enterRule(_localctx, 144, RULE_findOperatorSource);
		try {
			setState(1178);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,58,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1176);
				((FindOperatorSourceContext)_localctx).Entity = findOperatorSourceEntityExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1177);
				((FindOperatorSourceContext)_localctx).WildcardedEntity = wildcardedEntityExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FindOperatorSourceEntityExpressionContext extends ParserRuleContext {
		public EntityNameReferenceContext Entity;
		public AsOperatorContext asOperator;
		public List<AsOperatorContext> AsOperators = new ArrayList<AsOperatorContext>();
		public EntityNameReferenceContext entityNameReference() {
			return getRuleContext(EntityNameReferenceContext.class,0);
		}
		public List<TerminalNode> BAR() { return getTokens(HqlParser.BAR); }
		public TerminalNode BAR(int i) {
			return getToken(HqlParser.BAR, i);
		}
		public List<AsOperatorContext> asOperator() {
			return getRuleContexts(AsOperatorContext.class);
		}
		public AsOperatorContext asOperator(int i) {
			return getRuleContext(AsOperatorContext.class,i);
		}
		public FindOperatorSourceEntityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_findOperatorSourceEntityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFindOperatorSourceEntityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFindOperatorSourceEntityExpression(this);
		}
	}

	public final FindOperatorSourceEntityExpressionContext findOperatorSourceEntityExpression() throws RecognitionException {
		FindOperatorSourceEntityExpressionContext _localctx = new FindOperatorSourceEntityExpressionContext(_ctx, getState());
		enterRule(_localctx, 146, RULE_findOperatorSourceEntityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1180);
			((FindOperatorSourceEntityExpressionContext)_localctx).Entity = entityNameReference();
			setState(1185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BAR) {
				{
				{
				setState(1181);
				match(BAR);
				setState(1182);
				((FindOperatorSourceEntityExpressionContext)_localctx).asOperator = asOperator();
				((FindOperatorSourceEntityExpressionContext)_localctx).AsOperators.add(((FindOperatorSourceEntityExpressionContext)_localctx).asOperator);
				}
				}
				setState(1187);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForkOperatorContext extends ParserRuleContext {
		public TerminalNode FORK() { return getToken(HqlParser.FORK, 0); }
		public List<ForkOperatorForkContext> forkOperatorFork() {
			return getRuleContexts(ForkOperatorForkContext.class);
		}
		public ForkOperatorForkContext forkOperatorFork(int i) {
			return getRuleContext(ForkOperatorForkContext.class,i);
		}
		public ForkOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forkOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterForkOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitForkOperator(this);
		}
	}

	public final ForkOperatorContext forkOperator() throws RecognitionException {
		ForkOperatorContext _localctx = new ForkOperatorContext(_ctx, getState());
		enterRule(_localctx, 148, RULE_forkOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1188);
			match(FORK);
			setState(1190); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(1189);
				forkOperatorFork();
				}
				}
				setState(1192); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 622630623164497920L) != 0) || ((((_la - 69)) & ~0x3f) == 0 && ((1L << (_la - 69)) & -8178528127110061463L) != 0) || ((((_la - 140)) & ~0x3f) == 0 && ((1L << (_la - 140)) & 1592259962793370531L) != 0) || ((((_la - 204)) & ~0x3f) == 0 && ((1L << (_la - 204)) & 106397688039329281L) != 0) || ((((_la - 268)) & ~0x3f) == 0 && ((1L << (_la - 268)) & 281474977239039L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForkOperatorForkContext extends ParserRuleContext {
		public ForkOperatorExpressionNameContext Name;
		public ForkOperatorExpressionContext Expression;
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public ForkOperatorExpressionContext forkOperatorExpression() {
			return getRuleContext(ForkOperatorExpressionContext.class,0);
		}
		public ForkOperatorExpressionNameContext forkOperatorExpressionName() {
			return getRuleContext(ForkOperatorExpressionNameContext.class,0);
		}
		public ForkOperatorForkContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forkOperatorFork; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterForkOperatorFork(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitForkOperatorFork(this);
		}
	}

	public final ForkOperatorForkContext forkOperatorFork() throws RecognitionException {
		ForkOperatorForkContext _localctx = new ForkOperatorForkContext(_ctx, getState());
		enterRule(_localctx, 150, RULE_forkOperatorFork);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1195);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622630621017014272L) != 0) || ((((_la - 69)) & ~0x3f) == 0 && ((1L << (_la - 69)) & -8178528127110061463L) != 0) || ((((_la - 140)) & ~0x3f) == 0 && ((1L << (_la - 140)) & 1592259962793370531L) != 0) || ((((_la - 204)) & ~0x3f) == 0 && ((1L << (_la - 204)) & 106397688039329281L) != 0) || ((((_la - 268)) & ~0x3f) == 0 && ((1L << (_la - 268)) & 281474977239039L) != 0)) {
				{
				setState(1194);
				((ForkOperatorForkContext)_localctx).Name = forkOperatorExpressionName();
				}
			}

			setState(1197);
			match(OPENPAREN);
			setState(1198);
			((ForkOperatorForkContext)_localctx).Expression = forkOperatorExpression();
			setState(1199);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForkOperatorExpressionNameContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public ForkOperatorExpressionNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forkOperatorExpressionName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterForkOperatorExpressionName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitForkOperatorExpressionName(this);
		}
	}

	public final ForkOperatorExpressionNameContext forkOperatorExpressionName() throws RecognitionException {
		ForkOperatorExpressionNameContext _localctx = new ForkOperatorExpressionNameContext(_ctx, getState());
		enterRule(_localctx, 152, RULE_forkOperatorExpressionName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1201);
			((ForkOperatorExpressionNameContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(1202);
			match(EQUAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForkOperatorExpressionContext extends ParserRuleContext {
		public ForkPipeOperatorContext Operator;
		public ForkOperatorPipedOperatorContext forkOperatorPipedOperator;
		public List<ForkOperatorPipedOperatorContext> PipedOperators = new ArrayList<ForkOperatorPipedOperatorContext>();
		public ForkPipeOperatorContext forkPipeOperator() {
			return getRuleContext(ForkPipeOperatorContext.class,0);
		}
		public List<ForkOperatorPipedOperatorContext> forkOperatorPipedOperator() {
			return getRuleContexts(ForkOperatorPipedOperatorContext.class);
		}
		public ForkOperatorPipedOperatorContext forkOperatorPipedOperator(int i) {
			return getRuleContext(ForkOperatorPipedOperatorContext.class,i);
		}
		public ForkOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forkOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterForkOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitForkOperatorExpression(this);
		}
	}

	public final ForkOperatorExpressionContext forkOperatorExpression() throws RecognitionException {
		ForkOperatorExpressionContext _localctx = new ForkOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 154, RULE_forkOperatorExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1204);
			((ForkOperatorExpressionContext)_localctx).Operator = forkPipeOperator();
			setState(1208);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BAR) {
				{
				{
				setState(1205);
				((ForkOperatorExpressionContext)_localctx).forkOperatorPipedOperator = forkOperatorPipedOperator();
				((ForkOperatorExpressionContext)_localctx).PipedOperators.add(((ForkOperatorExpressionContext)_localctx).forkOperatorPipedOperator);
				}
				}
				setState(1210);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForkOperatorPipedOperatorContext extends ParserRuleContext {
		public ForkPipeOperatorContext Operator;
		public TerminalNode BAR() { return getToken(HqlParser.BAR, 0); }
		public ForkPipeOperatorContext forkPipeOperator() {
			return getRuleContext(ForkPipeOperatorContext.class,0);
		}
		public ForkOperatorPipedOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forkOperatorPipedOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterForkOperatorPipedOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitForkOperatorPipedOperator(this);
		}
	}

	public final ForkOperatorPipedOperatorContext forkOperatorPipedOperator() throws RecognitionException {
		ForkOperatorPipedOperatorContext _localctx = new ForkOperatorPipedOperatorContext(_ctx, getState());
		enterRule(_localctx, 156, RULE_forkOperatorPipedOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1211);
			match(BAR);
			setState(1212);
			((ForkOperatorPipedOperatorContext)_localctx).Operator = forkPipeOperator();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GetSchemaOperatorContext extends ParserRuleContext {
		public TerminalNode GETSCHEMA() { return getToken(HqlParser.GETSCHEMA, 0); }
		public GetSchemaOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_getSchemaOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGetSchemaOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGetSchemaOperator(this);
		}
	}

	public final GetSchemaOperatorContext getSchemaOperator() throws RecognitionException {
		GetSchemaOperatorContext _localctx = new GetSchemaOperatorContext(_ctx, getState());
		enterRule(_localctx, 158, RULE_getSchemaOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1214);
			match(GETSCHEMA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMarkComponentsOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parametems = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public TerminalNode GRAPHMARKCOMPONENTS() { return getToken(HqlParser.GRAPHMARKCOMPONENTS, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public GraphMarkComponentsOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMarkComponentsOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMarkComponentsOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMarkComponentsOperator(this);
		}
	}

	public final GraphMarkComponentsOperatorContext graphMarkComponentsOperator() throws RecognitionException {
		GraphMarkComponentsOperatorContext _localctx = new GraphMarkComponentsOperatorContext(_ctx, getState());
		enterRule(_localctx, 160, RULE_graphMarkComponentsOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1216);
			match(GRAPHMARKCOMPONENTS);
			setState(1220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1217);
				((GraphMarkComponentsOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((GraphMarkComponentsOperatorContext)_localctx).Parametems.add(((GraphMarkComponentsOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1222);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public GraphMatchPatternContext graphMatchPattern;
		public List<GraphMatchPatternContext> Patterns = new ArrayList<GraphMatchPatternContext>();
		public GraphMatchWhereClauseContext WhereClause;
		public GraphMatchProjectClauseContext ProjectClause;
		public TerminalNode GRAPHMATCH() { return getToken(HqlParser.GRAPHMATCH, 0); }
		public List<GraphMatchPatternContext> graphMatchPattern() {
			return getRuleContexts(GraphMatchPatternContext.class);
		}
		public GraphMatchPatternContext graphMatchPattern(int i) {
			return getRuleContext(GraphMatchPatternContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(HqlParser.COMMA, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public GraphMatchWhereClauseContext graphMatchWhereClause() {
			return getRuleContext(GraphMatchWhereClauseContext.class,0);
		}
		public GraphMatchProjectClauseContext graphMatchProjectClause() {
			return getRuleContext(GraphMatchProjectClauseContext.class,0);
		}
		public GraphMatchOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchOperator(this);
		}
	}

	public final GraphMatchOperatorContext graphMatchOperator() throws RecognitionException {
		GraphMatchOperatorContext _localctx = new GraphMatchOperatorContext(_ctx, getState());
		enterRule(_localctx, 162, RULE_graphMatchOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1223);
			match(GRAPHMATCH);
			setState(1227);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1224);
				((GraphMatchOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((GraphMatchOperatorContext)_localctx).Parameters.add(((GraphMatchOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1229);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1230);
			((GraphMatchOperatorContext)_localctx).graphMatchPattern = graphMatchPattern();
			((GraphMatchOperatorContext)_localctx).Patterns.add(((GraphMatchOperatorContext)_localctx).graphMatchPattern);
			{
			setState(1231);
			match(COMMA);
			setState(1232);
			((GraphMatchOperatorContext)_localctx).graphMatchPattern = graphMatchPattern();
			((GraphMatchOperatorContext)_localctx).Patterns.add(((GraphMatchOperatorContext)_localctx).graphMatchPattern);
			}
			setState(1235);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(1234);
				((GraphMatchOperatorContext)_localctx).WhereClause = graphMatchWhereClause();
				}
			}

			setState(1238);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,66,_ctx) ) {
			case 1:
				{
				setState(1237);
				((GraphMatchOperatorContext)_localctx).ProjectClause = graphMatchProjectClause();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchPatternContext extends ParserRuleContext {
		public GraphMatchPatternNodeContext Node;
		public GraphMatchPatternUnnamedEdgeContext UnnamedEdge;
		public GraphMatchPatternNamedEdgeContext NamedEdge;
		public GraphMatchPatternNodeContext graphMatchPatternNode() {
			return getRuleContext(GraphMatchPatternNodeContext.class,0);
		}
		public GraphMatchPatternUnnamedEdgeContext graphMatchPatternUnnamedEdge() {
			return getRuleContext(GraphMatchPatternUnnamedEdgeContext.class,0);
		}
		public GraphMatchPatternNamedEdgeContext graphMatchPatternNamedEdge() {
			return getRuleContext(GraphMatchPatternNamedEdgeContext.class,0);
		}
		public GraphMatchPatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchPattern; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchPattern(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchPattern(this);
		}
	}

	public final GraphMatchPatternContext graphMatchPattern() throws RecognitionException {
		GraphMatchPatternContext _localctx = new GraphMatchPatternContext(_ctx, getState());
		enterRule(_localctx, 164, RULE_graphMatchPattern);
		try {
			setState(1243);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPENPAREN:
				enterOuterAlt(_localctx, 1);
				{
				setState(1240);
				((GraphMatchPatternContext)_localctx).Node = graphMatchPatternNode();
				}
				break;
			case DASHDASH:
			case DASHDASH_GREATERTHAN:
			case LESSTHAN_DASHDASH:
				enterOuterAlt(_localctx, 2);
				{
				setState(1241);
				((GraphMatchPatternContext)_localctx).UnnamedEdge = graphMatchPatternUnnamedEdge();
				}
				break;
			case DASH_OPENBRACKET:
			case LESSTHAN_DASH_OPENBRACKET:
				enterOuterAlt(_localctx, 3);
				{
				setState(1242);
				((GraphMatchPatternContext)_localctx).NamedEdge = graphMatchPatternNamedEdge();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchPatternNodeContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public GraphMatchPatternNodeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchPatternNode; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchPatternNode(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchPatternNode(this);
		}
	}

	public final GraphMatchPatternNodeContext graphMatchPatternNode() throws RecognitionException {
		GraphMatchPatternNodeContext _localctx = new GraphMatchPatternNodeContext(_ctx, getState());
		enterRule(_localctx, 166, RULE_graphMatchPatternNode);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1245);
			match(OPENPAREN);
			setState(1246);
			((GraphMatchPatternNodeContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(1247);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchPatternUnnamedEdgeContext extends ParserRuleContext {
		public Token Direction;
		public TerminalNode DASHDASH_GREATERTHAN() { return getToken(HqlParser.DASHDASH_GREATERTHAN, 0); }
		public TerminalNode LESSTHAN_DASHDASH() { return getToken(HqlParser.LESSTHAN_DASHDASH, 0); }
		public TerminalNode DASHDASH() { return getToken(HqlParser.DASHDASH, 0); }
		public GraphMatchPatternUnnamedEdgeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchPatternUnnamedEdge; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchPatternUnnamedEdge(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchPatternUnnamedEdge(this);
		}
	}

	public final GraphMatchPatternUnnamedEdgeContext graphMatchPatternUnnamedEdge() throws RecognitionException {
		GraphMatchPatternUnnamedEdgeContext _localctx = new GraphMatchPatternUnnamedEdgeContext(_ctx, getState());
		enterRule(_localctx, 168, RULE_graphMatchPatternUnnamedEdge);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1249);
			((GraphMatchPatternUnnamedEdgeContext)_localctx).Direction = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 33566720L) != 0)) ) {
				((GraphMatchPatternUnnamedEdgeContext)_localctx).Direction = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchPatternNamedEdgeContext extends ParserRuleContext {
		public Token OpenBracket;
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public GraphMatchPatternRangeContext Range;
		public Token CloseBracket;
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public TerminalNode DASH_OPENBRACKET() { return getToken(HqlParser.DASH_OPENBRACKET, 0); }
		public TerminalNode LESSTHAN_DASH_OPENBRACKET() { return getToken(HqlParser.LESSTHAN_DASH_OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET_DASH_GREATERTHAN() { return getToken(HqlParser.CLOSEBRACKET_DASH_GREATERTHAN, 0); }
		public TerminalNode CLOSEBRACKET_DASH() { return getToken(HqlParser.CLOSEBRACKET_DASH, 0); }
		public GraphMatchPatternRangeContext graphMatchPatternRange() {
			return getRuleContext(GraphMatchPatternRangeContext.class,0);
		}
		public GraphMatchPatternNamedEdgeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchPatternNamedEdge; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchPatternNamedEdge(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchPatternNamedEdge(this);
		}
	}

	public final GraphMatchPatternNamedEdgeContext graphMatchPatternNamedEdge() throws RecognitionException {
		GraphMatchPatternNamedEdgeContext _localctx = new GraphMatchPatternNamedEdgeContext(_ctx, getState());
		enterRule(_localctx, 170, RULE_graphMatchPatternNamedEdge);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1251);
			((GraphMatchPatternNamedEdgeContext)_localctx).OpenBracket = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==DASH_OPENBRACKET || _la==LESSTHAN_DASH_OPENBRACKET) ) {
				((GraphMatchPatternNamedEdgeContext)_localctx).OpenBracket = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1252);
			((GraphMatchPatternNamedEdgeContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			setState(1254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASTERISK) {
				{
				setState(1253);
				((GraphMatchPatternNamedEdgeContext)_localctx).Range = graphMatchPatternRange();
				}
			}

			setState(1256);
			((GraphMatchPatternNamedEdgeContext)_localctx).CloseBracket = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==CLOSEBRACKET_DASH || _la==CLOSEBRACKET_DASH_GREATERTHAN) ) {
				((GraphMatchPatternNamedEdgeContext)_localctx).CloseBracket = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchPatternRangeContext extends ParserRuleContext {
		public InvocationExpressionContext LowerBound;
		public InvocationExpressionContext UpperBound;
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public TerminalNode DOTDOT() { return getToken(HqlParser.DOTDOT, 0); }
		public List<InvocationExpressionContext> invocationExpression() {
			return getRuleContexts(InvocationExpressionContext.class);
		}
		public InvocationExpressionContext invocationExpression(int i) {
			return getRuleContext(InvocationExpressionContext.class,i);
		}
		public GraphMatchPatternRangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchPatternRange; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchPatternRange(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchPatternRange(this);
		}
	}

	public final GraphMatchPatternRangeContext graphMatchPatternRange() throws RecognitionException {
		GraphMatchPatternRangeContext _localctx = new GraphMatchPatternRangeContext(_ctx, getState());
		enterRule(_localctx, 172, RULE_graphMatchPatternRange);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1258);
			match(ASTERISK);
			setState(1259);
			((GraphMatchPatternRangeContext)_localctx).LowerBound = invocationExpression();
			setState(1260);
			match(DOTDOT);
			setState(1261);
			((GraphMatchPatternRangeContext)_localctx).UpperBound = invocationExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchWhereClauseContext extends ParserRuleContext {
		public ExpressionContext Expression;
		public TerminalNode WHERE() { return getToken(HqlParser.WHERE, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public GraphMatchWhereClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchWhereClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchWhereClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchWhereClause(this);
		}
	}

	public final GraphMatchWhereClauseContext graphMatchWhereClause() throws RecognitionException {
		GraphMatchWhereClauseContext _localctx = new GraphMatchWhereClauseContext(_ctx, getState());
		enterRule(_localctx, 174, RULE_graphMatchWhereClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1263);
			match(WHERE);
			setState(1264);
			((GraphMatchWhereClauseContext)_localctx).Expression = expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMatchProjectClauseContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode PROJECT() { return getToken(HqlParser.PROJECT, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public GraphMatchProjectClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMatchProjectClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMatchProjectClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMatchProjectClause(this);
		}
	}

	public final GraphMatchProjectClauseContext graphMatchProjectClause() throws RecognitionException {
		GraphMatchProjectClauseContext _localctx = new GraphMatchProjectClauseContext(_ctx, getState());
		enterRule(_localctx, 176, RULE_graphMatchProjectClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1266);
			match(PROJECT);
			setState(1267);
			((GraphMatchProjectClauseContext)_localctx).namedExpression = namedExpression();
			((GraphMatchProjectClauseContext)_localctx).Expressions.add(((GraphMatchProjectClauseContext)_localctx).namedExpression);
			setState(1272);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1268);
				match(COMMA);
				setState(1269);
				((GraphMatchProjectClauseContext)_localctx).namedExpression = namedExpression();
				((GraphMatchProjectClauseContext)_localctx).Expressions.add(((GraphMatchProjectClauseContext)_localctx).namedExpression);
				}
				}
				setState(1274);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphMergeOperatorContext extends ParserRuleContext {
		public InvocationExpressionContext Graph;
		public JoinOperatorOnClauseContext OnClause;
		public TerminalNode GRAPHMERGE() { return getToken(HqlParser.GRAPHMERGE, 0); }
		public InvocationExpressionContext invocationExpression() {
			return getRuleContext(InvocationExpressionContext.class,0);
		}
		public JoinOperatorOnClauseContext joinOperatorOnClause() {
			return getRuleContext(JoinOperatorOnClauseContext.class,0);
		}
		public GraphMergeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphMergeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphMergeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphMergeOperator(this);
		}
	}

	public final GraphMergeOperatorContext graphMergeOperator() throws RecognitionException {
		GraphMergeOperatorContext _localctx = new GraphMergeOperatorContext(_ctx, getState());
		enterRule(_localctx, 178, RULE_graphMergeOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1275);
			match(GRAPHMERGE);
			setState(1276);
			((GraphMergeOperatorContext)_localctx).Graph = invocationExpression();
			setState(1278);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ON) {
				{
				setState(1277);
				((GraphMergeOperatorContext)_localctx).OnClause = joinOperatorOnClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphToTableOperatorContext extends ParserRuleContext {
		public GraphToTableOutputContext graphToTableOutput;
		public List<GraphToTableOutputContext> Outputs = new ArrayList<GraphToTableOutputContext>();
		public TerminalNode GRAPHTOTABLE() { return getToken(HqlParser.GRAPHTOTABLE, 0); }
		public List<GraphToTableOutputContext> graphToTableOutput() {
			return getRuleContexts(GraphToTableOutputContext.class);
		}
		public GraphToTableOutputContext graphToTableOutput(int i) {
			return getRuleContext(GraphToTableOutputContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(HqlParser.COMMA, 0); }
		public GraphToTableOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphToTableOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphToTableOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphToTableOperator(this);
		}
	}

	public final GraphToTableOperatorContext graphToTableOperator() throws RecognitionException {
		GraphToTableOperatorContext _localctx = new GraphToTableOperatorContext(_ctx, getState());
		enterRule(_localctx, 180, RULE_graphToTableOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1280);
			match(GRAPHTOTABLE);
			setState(1281);
			((GraphToTableOperatorContext)_localctx).graphToTableOutput = graphToTableOutput();
			((GraphToTableOperatorContext)_localctx).Outputs.add(((GraphToTableOperatorContext)_localctx).graphToTableOutput);
			{
			setState(1282);
			match(COMMA);
			setState(1283);
			((GraphToTableOperatorContext)_localctx).graphToTableOutput = graphToTableOutput();
			((GraphToTableOperatorContext)_localctx).Outputs.add(((GraphToTableOperatorContext)_localctx).graphToTableOutput);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphToTableOutputContext extends ParserRuleContext {
		public Token Keyword;
		public GraphToTableAsClauseContext AsClause;
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public TerminalNode NODES() { return getToken(HqlParser.NODES, 0); }
		public TerminalNode EDGES() { return getToken(HqlParser.EDGES, 0); }
		public GraphToTableAsClauseContext graphToTableAsClause() {
			return getRuleContext(GraphToTableAsClauseContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public GraphToTableOutputContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphToTableOutput; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphToTableOutput(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphToTableOutput(this);
		}
	}

	public final GraphToTableOutputContext graphToTableOutput() throws RecognitionException {
		GraphToTableOutputContext _localctx = new GraphToTableOutputContext(_ctx, getState());
		enterRule(_localctx, 182, RULE_graphToTableOutput);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1285);
			((GraphToTableOutputContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==EDGES || _la==NODES) ) {
				((GraphToTableOutputContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1287);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==AS) {
				{
				setState(1286);
				((GraphToTableOutputContext)_localctx).AsClause = graphToTableAsClause();
				}
			}

			setState(1292);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1289);
				((GraphToTableOutputContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((GraphToTableOutputContext)_localctx).Parameters.add(((GraphToTableOutputContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1294);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphToTableAsClauseContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode AS() { return getToken(HqlParser.AS, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public GraphToTableAsClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphToTableAsClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphToTableAsClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphToTableAsClause(this);
		}
	}

	public final GraphToTableAsClauseContext graphToTableAsClause() throws RecognitionException {
		GraphToTableAsClauseContext _localctx = new GraphToTableAsClauseContext(_ctx, getState());
		enterRule(_localctx, 184, RULE_graphToTableAsClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1295);
			match(AS);
			setState(1296);
			((GraphToTableAsClauseContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GraphShortestPathsOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public GraphMatchPatternContext graphMatchPattern;
		public List<GraphMatchPatternContext> Patterns = new ArrayList<GraphMatchPatternContext>();
		public GraphMatchWhereClauseContext WhereClause;
		public GraphMatchProjectClauseContext ProjectClause;
		public TerminalNode GRAPHSHORTESTPATHS() { return getToken(HqlParser.GRAPHSHORTESTPATHS, 0); }
		public List<GraphMatchPatternContext> graphMatchPattern() {
			return getRuleContexts(GraphMatchPatternContext.class);
		}
		public GraphMatchPatternContext graphMatchPattern(int i) {
			return getRuleContext(GraphMatchPatternContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(HqlParser.COMMA, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public GraphMatchWhereClauseContext graphMatchWhereClause() {
			return getRuleContext(GraphMatchWhereClauseContext.class,0);
		}
		public GraphMatchProjectClauseContext graphMatchProjectClause() {
			return getRuleContext(GraphMatchProjectClauseContext.class,0);
		}
		public GraphShortestPathsOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_graphShortestPathsOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGraphShortestPathsOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGraphShortestPathsOperator(this);
		}
	}

	public final GraphShortestPathsOperatorContext graphShortestPathsOperator() throws RecognitionException {
		GraphShortestPathsOperatorContext _localctx = new GraphShortestPathsOperatorContext(_ctx, getState());
		enterRule(_localctx, 186, RULE_graphShortestPathsOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1298);
			match(GRAPHSHORTESTPATHS);
			setState(1302);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1299);
				((GraphShortestPathsOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((GraphShortestPathsOperatorContext)_localctx).Parameters.add(((GraphShortestPathsOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1304);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1305);
			((GraphShortestPathsOperatorContext)_localctx).graphMatchPattern = graphMatchPattern();
			((GraphShortestPathsOperatorContext)_localctx).Patterns.add(((GraphShortestPathsOperatorContext)_localctx).graphMatchPattern);
			{
			setState(1306);
			match(COMMA);
			setState(1307);
			((GraphShortestPathsOperatorContext)_localctx).graphMatchPattern = graphMatchPattern();
			((GraphShortestPathsOperatorContext)_localctx).Patterns.add(((GraphShortestPathsOperatorContext)_localctx).graphMatchPattern);
			}
			setState(1310);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WHERE) {
				{
				setState(1309);
				((GraphShortestPathsOperatorContext)_localctx).WhereClause = graphMatchWhereClause();
				}
			}

			setState(1313);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,75,_ctx) ) {
			case 1:
				{
				setState(1312);
				((GraphShortestPathsOperatorContext)_localctx).ProjectClause = graphMatchProjectClause();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InvokeOperatorContext extends ParserRuleContext {
		public DotCompositeFunctionCallExpressionContext FunctionCall;
		public TerminalNode INVOKE() { return getToken(HqlParser.INVOKE, 0); }
		public DotCompositeFunctionCallExpressionContext dotCompositeFunctionCallExpression() {
			return getRuleContext(DotCompositeFunctionCallExpressionContext.class,0);
		}
		public InvokeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_invokeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterInvokeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitInvokeOperator(this);
		}
	}

	public final InvokeOperatorContext invokeOperator() throws RecognitionException {
		InvokeOperatorContext _localctx = new InvokeOperatorContext(_ctx, getState());
		enterRule(_localctx, 188, RULE_invokeOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1315);
			match(INVOKE);
			setState(1316);
			((InvokeOperatorContext)_localctx).FunctionCall = dotCompositeFunctionCallExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JoinOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public UnnamedExpressionContext Table;
		public JoinOperatorOnClauseContext OnClause;
		public JoinOperatorWhereClauseContext WhereClause;
		public TerminalNode JOIN() { return getToken(HqlParser.JOIN, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public JoinOperatorOnClauseContext joinOperatorOnClause() {
			return getRuleContext(JoinOperatorOnClauseContext.class,0);
		}
		public JoinOperatorWhereClauseContext joinOperatorWhereClause() {
			return getRuleContext(JoinOperatorWhereClauseContext.class,0);
		}
		public JoinOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJoinOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJoinOperator(this);
		}
	}

	public final JoinOperatorContext joinOperator() throws RecognitionException {
		JoinOperatorContext _localctx = new JoinOperatorContext(_ctx, getState());
		enterRule(_localctx, 190, RULE_joinOperator);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1318);
			match(JOIN);
			setState(1322);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,76,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1319);
					((JoinOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((JoinOperatorContext)_localctx).Parameters.add(((JoinOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1324);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,76,_ctx);
			}
			setState(1325);
			((JoinOperatorContext)_localctx).Table = unnamedExpression();
			setState(1328);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ON:
				{
				setState(1326);
				((JoinOperatorContext)_localctx).OnClause = joinOperatorOnClause();
				}
				break;
			case WHERE:
				{
				setState(1327);
				((JoinOperatorContext)_localctx).WhereClause = joinOperatorWhereClause();
				}
				break;
			case EOF:
			case BAR:
			case CLOSEBRACE:
			case CLOSEPAREN:
			case SEMICOLON:
			case PROJECT:
				break;
			default:
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JoinOperatorOnClauseContext extends ParserRuleContext {
		public UnnamedExpressionContext unnamedExpression;
		public List<UnnamedExpressionContext> Expressions = new ArrayList<UnnamedExpressionContext>();
		public TerminalNode ON() { return getToken(HqlParser.ON, 0); }
		public List<UnnamedExpressionContext> unnamedExpression() {
			return getRuleContexts(UnnamedExpressionContext.class);
		}
		public UnnamedExpressionContext unnamedExpression(int i) {
			return getRuleContext(UnnamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public JoinOperatorOnClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinOperatorOnClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJoinOperatorOnClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJoinOperatorOnClause(this);
		}
	}

	public final JoinOperatorOnClauseContext joinOperatorOnClause() throws RecognitionException {
		JoinOperatorOnClauseContext _localctx = new JoinOperatorOnClauseContext(_ctx, getState());
		enterRule(_localctx, 192, RULE_joinOperatorOnClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1330);
			match(ON);
			setState(1339);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622630631754434562L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1729241517781539117L) != 0) || ((((_la - 132)) & ~0x3f) == 0 && ((1L << (_la - 132)) & 1790180853509497601L) != 0) || ((((_la - 197)) & ~0x3f) == 0 && ((1L << (_la - 197)) & -4800818406911180661L) != 0) || ((((_la - 268)) & ~0x3f) == 0 && ((1L << (_la - 268)) & 492443770949631L) != 0)) {
				{
				setState(1331);
				((JoinOperatorOnClauseContext)_localctx).unnamedExpression = unnamedExpression();
				((JoinOperatorOnClauseContext)_localctx).Expressions.add(((JoinOperatorOnClauseContext)_localctx).unnamedExpression);
				setState(1336);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1332);
					match(COMMA);
					setState(1333);
					((JoinOperatorOnClauseContext)_localctx).unnamedExpression = unnamedExpression();
					((JoinOperatorOnClauseContext)_localctx).Expressions.add(((JoinOperatorOnClauseContext)_localctx).unnamedExpression);
					}
					}
					setState(1338);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JoinOperatorWhereClauseContext extends ParserRuleContext {
		public UnnamedExpressionContext Predicate;
		public TerminalNode WHERE() { return getToken(HqlParser.WHERE, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public JoinOperatorWhereClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_joinOperatorWhereClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJoinOperatorWhereClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJoinOperatorWhereClause(this);
		}
	}

	public final JoinOperatorWhereClauseContext joinOperatorWhereClause() throws RecognitionException {
		JoinOperatorWhereClauseContext _localctx = new JoinOperatorWhereClauseContext(_ctx, getState());
		enterRule(_localctx, 194, RULE_joinOperatorWhereClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1341);
			match(WHERE);
			setState(1342);
			((JoinOperatorWhereClauseContext)_localctx).Predicate = unnamedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LookupOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public UnnamedExpressionContext Table;
		public JoinOperatorOnClauseContext OnClause;
		public TerminalNode LOOKUP() { return getToken(HqlParser.LOOKUP, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public JoinOperatorOnClauseContext joinOperatorOnClause() {
			return getRuleContext(JoinOperatorOnClauseContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public LookupOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lookupOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLookupOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLookupOperator(this);
		}
	}

	public final LookupOperatorContext lookupOperator() throws RecognitionException {
		LookupOperatorContext _localctx = new LookupOperatorContext(_ctx, getState());
		enterRule(_localctx, 196, RULE_lookupOperator);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1344);
			match(LOOKUP);
			setState(1348);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,80,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1345);
					((LookupOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((LookupOperatorContext)_localctx).Parameters.add(((LookupOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1350);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,80,_ctx);
			}
			setState(1351);
			((LookupOperatorContext)_localctx).Table = unnamedExpression();
			setState(1352);
			((LookupOperatorContext)_localctx).OnClause = joinOperatorOnClause();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MacroExpandOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public MacroExpandEntityGroupContext EntityGroup;
		public IdentifierOrKeywordOrEscapedNameContext ScopeName;
		public StatementContext statement;
		public List<StatementContext> Statements = new ArrayList<StatementContext>();
		public TerminalNode MACROEXPAND() { return getToken(HqlParser.MACROEXPAND, 0); }
		public TerminalNode AS() { return getToken(HqlParser.AS, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public MacroExpandEntityGroupContext macroExpandEntityGroup() {
			return getRuleContext(MacroExpandEntityGroupContext.class,0);
		}
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<TerminalNode> SEMICOLON() { return getTokens(HqlParser.SEMICOLON); }
		public TerminalNode SEMICOLON(int i) {
			return getToken(HqlParser.SEMICOLON, i);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public MacroExpandOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macroExpandOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMacroExpandOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMacroExpandOperator(this);
		}
	}

	public final MacroExpandOperatorContext macroExpandOperator() throws RecognitionException {
		MacroExpandOperatorContext _localctx = new MacroExpandOperatorContext(_ctx, getState());
		enterRule(_localctx, 198, RULE_macroExpandOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1354);
			match(MACROEXPAND);
			setState(1358);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,81,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1355);
					((MacroExpandOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((MacroExpandOperatorContext)_localctx).Parameters.add(((MacroExpandOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1360);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,81,_ctx);
			}
			setState(1361);
			((MacroExpandOperatorContext)_localctx).EntityGroup = macroExpandEntityGroup();
			setState(1362);
			match(AS);
			setState(1363);
			((MacroExpandOperatorContext)_localctx).ScopeName = identifierOrKeywordOrEscapedName();
			setState(1364);
			match(OPENPAREN);
			setState(1365);
			((MacroExpandOperatorContext)_localctx).statement = statement();
			((MacroExpandOperatorContext)_localctx).Statements.add(((MacroExpandOperatorContext)_localctx).statement);
			setState(1370);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,82,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1366);
					match(SEMICOLON);
					setState(1367);
					((MacroExpandOperatorContext)_localctx).statement = statement();
					((MacroExpandOperatorContext)_localctx).Statements.add(((MacroExpandOperatorContext)_localctx).statement);
					}
					} 
				}
				setState(1372);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,82,_ctx);
			}
			setState(1374);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SEMICOLON) {
				{
				setState(1373);
				match(SEMICOLON);
				}
			}

			setState(1376);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MacroExpandEntityGroupContext extends ParserRuleContext {
		public EntityGroupExpressionContext EntityGroup;
		public SimpleNameReferenceContext Name;
		public EntityExpressionContext Entity;
		public EntityGroupExpressionContext entityGroupExpression() {
			return getRuleContext(EntityGroupExpressionContext.class,0);
		}
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public EntityExpressionContext entityExpression() {
			return getRuleContext(EntityExpressionContext.class,0);
		}
		public MacroExpandEntityGroupContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_macroExpandEntityGroup; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMacroExpandEntityGroup(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMacroExpandEntityGroup(this);
		}
	}

	public final MacroExpandEntityGroupContext macroExpandEntityGroup() throws RecognitionException {
		MacroExpandEntityGroupContext _localctx = new MacroExpandEntityGroupContext(_ctx, getState());
		enterRule(_localctx, 200, RULE_macroExpandEntityGroup);
		try {
			setState(1381);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,84,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(1378);
				((MacroExpandEntityGroupContext)_localctx).EntityGroup = entityGroupExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(1379);
				((MacroExpandEntityGroupContext)_localctx).Name = simpleNameReference();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(1380);
				((MacroExpandEntityGroupContext)_localctx).Entity = entityExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityGroupExpressionContext extends ParserRuleContext {
		public UnnamedExpressionContext unnamedExpression;
		public List<UnnamedExpressionContext> Expressions = new ArrayList<UnnamedExpressionContext>();
		public TerminalNode ENTITYGROUP() { return getToken(HqlParser.ENTITYGROUP, 0); }
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public List<UnnamedExpressionContext> unnamedExpression() {
			return getRuleContexts(UnnamedExpressionContext.class);
		}
		public UnnamedExpressionContext unnamedExpression(int i) {
			return getRuleContext(UnnamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public EntityGroupExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityGroupExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityGroupExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityGroupExpression(this);
		}
	}

	public final EntityGroupExpressionContext entityGroupExpression() throws RecognitionException {
		EntityGroupExpressionContext _localctx = new EntityGroupExpressionContext(_ctx, getState());
		enterRule(_localctx, 202, RULE_entityGroupExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1383);
			match(ENTITYGROUP);
			setState(1384);
			match(OPENBRACKET);
			setState(1385);
			((EntityGroupExpressionContext)_localctx).unnamedExpression = unnamedExpression();
			((EntityGroupExpressionContext)_localctx).Expressions.add(((EntityGroupExpressionContext)_localctx).unnamedExpression);
			setState(1390);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1386);
				match(COMMA);
				setState(1387);
				((EntityGroupExpressionContext)_localctx).unnamedExpression = unnamedExpression();
				((EntityGroupExpressionContext)_localctx).Expressions.add(((EntityGroupExpressionContext)_localctx).unnamedExpression);
				}
				}
				setState(1392);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1393);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeGraphOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public SimpleNameReferenceContext SourceColumn;
		public Token Direction;
		public SimpleNameReferenceContext TargetColumn;
		public MakeGraphIdClauseContext IdClause;
		public MakeGraphTablesAndKeysClauseContext TablesAndKeysClause;
		public MakeGraphPartitionedByClauseContext PartitionedByClause;
		public TerminalNode MAKEGRAPH() { return getToken(HqlParser.MAKEGRAPH, 0); }
		public List<SimpleNameReferenceContext> simpleNameReference() {
			return getRuleContexts(SimpleNameReferenceContext.class);
		}
		public SimpleNameReferenceContext simpleNameReference(int i) {
			return getRuleContext(SimpleNameReferenceContext.class,i);
		}
		public TerminalNode DASHDASH_GREATERTHAN() { return getToken(HqlParser.DASHDASH_GREATERTHAN, 0); }
		public TerminalNode DASHDASH() { return getToken(HqlParser.DASHDASH, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public MakeGraphIdClauseContext makeGraphIdClause() {
			return getRuleContext(MakeGraphIdClauseContext.class,0);
		}
		public MakeGraphTablesAndKeysClauseContext makeGraphTablesAndKeysClause() {
			return getRuleContext(MakeGraphTablesAndKeysClauseContext.class,0);
		}
		public MakeGraphPartitionedByClauseContext makeGraphPartitionedByClause() {
			return getRuleContext(MakeGraphPartitionedByClauseContext.class,0);
		}
		public MakeGraphOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeGraphOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeGraphOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeGraphOperator(this);
		}
	}

	public final MakeGraphOperatorContext makeGraphOperator() throws RecognitionException {
		MakeGraphOperatorContext _localctx = new MakeGraphOperatorContext(_ctx, getState());
		enterRule(_localctx, 204, RULE_makeGraphOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1395);
			match(MAKEGRAPH);
			setState(1399);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,86,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1396);
					((MakeGraphOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((MakeGraphOperatorContext)_localctx).Parameters.add(((MakeGraphOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1401);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,86,_ctx);
			}
			setState(1402);
			((MakeGraphOperatorContext)_localctx).SourceColumn = simpleNameReference();
			setState(1403);
			((MakeGraphOperatorContext)_localctx).Direction = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==DASHDASH || _la==DASHDASH_GREATERTHAN) ) {
				((MakeGraphOperatorContext)_localctx).Direction = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1404);
			((MakeGraphOperatorContext)_localctx).TargetColumn = simpleNameReference();
			setState(1407);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case WITH_NODE_ID:
				{
				setState(1405);
				((MakeGraphOperatorContext)_localctx).IdClause = makeGraphIdClause();
				}
				break;
			case WITH:
				{
				setState(1406);
				((MakeGraphOperatorContext)_localctx).TablesAndKeysClause = makeGraphTablesAndKeysClause();
				}
				break;
			case EOF:
			case BAR:
			case CLOSEBRACE:
			case CLOSEPAREN:
			case SEMICOLON:
			case PARTITIONEDBY:
			case PROJECT:
				break;
			default:
				break;
			}
			setState(1410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARTITIONEDBY) {
				{
				setState(1409);
				((MakeGraphOperatorContext)_localctx).PartitionedByClause = makeGraphPartitionedByClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeGraphIdClauseContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode WITH_NODE_ID() { return getToken(HqlParser.WITH_NODE_ID, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public MakeGraphIdClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeGraphIdClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeGraphIdClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeGraphIdClause(this);
		}
	}

	public final MakeGraphIdClauseContext makeGraphIdClause() throws RecognitionException {
		MakeGraphIdClauseContext _localctx = new MakeGraphIdClauseContext(_ctx, getState());
		enterRule(_localctx, 206, RULE_makeGraphIdClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1412);
			match(WITH_NODE_ID);
			setState(1413);
			match(EQUAL);
			setState(1414);
			((MakeGraphIdClauseContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeGraphTablesAndKeysClauseContext extends ParserRuleContext {
		public InvocationExpressionContext Table;
		public SimpleNameReferenceContext Column;
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode ON() { return getToken(HqlParser.ON, 0); }
		public InvocationExpressionContext invocationExpression() {
			return getRuleContext(InvocationExpressionContext.class,0);
		}
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public MakeGraphTablesAndKeysClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeGraphTablesAndKeysClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeGraphTablesAndKeysClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeGraphTablesAndKeysClause(this);
		}
	}

	public final MakeGraphTablesAndKeysClauseContext makeGraphTablesAndKeysClause() throws RecognitionException {
		MakeGraphTablesAndKeysClauseContext _localctx = new MakeGraphTablesAndKeysClauseContext(_ctx, getState());
		enterRule(_localctx, 208, RULE_makeGraphTablesAndKeysClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1416);
			match(WITH);
			setState(1417);
			((MakeGraphTablesAndKeysClauseContext)_localctx).Table = invocationExpression();
			setState(1418);
			match(ON);
			setState(1419);
			((MakeGraphTablesAndKeysClauseContext)_localctx).Column = simpleNameReference();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeGraphPartitionedByClauseContext extends ParserRuleContext {
		public EntityPathOrElementExpressionContext Entity;
		public ContextualSubExpressionContext SubQuery;
		public TerminalNode PARTITIONEDBY() { return getToken(HqlParser.PARTITIONEDBY, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public EntityPathOrElementExpressionContext entityPathOrElementExpression() {
			return getRuleContext(EntityPathOrElementExpressionContext.class,0);
		}
		public ContextualSubExpressionContext contextualSubExpression() {
			return getRuleContext(ContextualSubExpressionContext.class,0);
		}
		public MakeGraphPartitionedByClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeGraphPartitionedByClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeGraphPartitionedByClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeGraphPartitionedByClause(this);
		}
	}

	public final MakeGraphPartitionedByClauseContext makeGraphPartitionedByClause() throws RecognitionException {
		MakeGraphPartitionedByClauseContext _localctx = new MakeGraphPartitionedByClauseContext(_ctx, getState());
		enterRule(_localctx, 210, RULE_makeGraphPartitionedByClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1421);
			match(PARTITIONEDBY);
			setState(1422);
			((MakeGraphPartitionedByClauseContext)_localctx).Entity = entityPathOrElementExpression();
			setState(1423);
			match(OPENPAREN);
			setState(1424);
			((MakeGraphPartitionedByClauseContext)_localctx).SubQuery = contextualSubExpression();
			setState(1425);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public MakeSeriesOperatorAggregationContext makeSeriesOperatorAggregation;
		public List<MakeSeriesOperatorAggregationContext> Aggregations = new ArrayList<MakeSeriesOperatorAggregationContext>();
		public MakeSeriesOperatorOnClauseContext OnClause;
		public MakeSeriesOperatorInRangeClauseContext InRangeClause;
		public MakeSeriesOperatorFromToStepClauseContext FromToStepClause;
		public MakeSeriesOperatorByClauseContext ByClause;
		public TerminalNode MAKESERIES() { return getToken(HqlParser.MAKESERIES, 0); }
		public List<MakeSeriesOperatorAggregationContext> makeSeriesOperatorAggregation() {
			return getRuleContexts(MakeSeriesOperatorAggregationContext.class);
		}
		public MakeSeriesOperatorAggregationContext makeSeriesOperatorAggregation(int i) {
			return getRuleContext(MakeSeriesOperatorAggregationContext.class,i);
		}
		public MakeSeriesOperatorOnClauseContext makeSeriesOperatorOnClause() {
			return getRuleContext(MakeSeriesOperatorOnClauseContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public MakeSeriesOperatorInRangeClauseContext makeSeriesOperatorInRangeClause() {
			return getRuleContext(MakeSeriesOperatorInRangeClauseContext.class,0);
		}
		public MakeSeriesOperatorFromToStepClauseContext makeSeriesOperatorFromToStepClause() {
			return getRuleContext(MakeSeriesOperatorFromToStepClauseContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public MakeSeriesOperatorByClauseContext makeSeriesOperatorByClause() {
			return getRuleContext(MakeSeriesOperatorByClauseContext.class,0);
		}
		public MakeSeriesOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperator(this);
		}
	}

	public final MakeSeriesOperatorContext makeSeriesOperator() throws RecognitionException {
		MakeSeriesOperatorContext _localctx = new MakeSeriesOperatorContext(_ctx, getState());
		enterRule(_localctx, 212, RULE_makeSeriesOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1427);
			match(MAKESERIES);
			setState(1431);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,89,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1428);
					((MakeSeriesOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((MakeSeriesOperatorContext)_localctx).Parameters.add(((MakeSeriesOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1433);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,89,_ctx);
			}
			setState(1434);
			((MakeSeriesOperatorContext)_localctx).makeSeriesOperatorAggregation = makeSeriesOperatorAggregation();
			((MakeSeriesOperatorContext)_localctx).Aggregations.add(((MakeSeriesOperatorContext)_localctx).makeSeriesOperatorAggregation);
			setState(1439);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1435);
				match(COMMA);
				setState(1436);
				((MakeSeriesOperatorContext)_localctx).makeSeriesOperatorAggregation = makeSeriesOperatorAggregation();
				((MakeSeriesOperatorContext)_localctx).Aggregations.add(((MakeSeriesOperatorContext)_localctx).makeSeriesOperatorAggregation);
				}
				}
				setState(1441);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1442);
			((MakeSeriesOperatorContext)_localctx).OnClause = makeSeriesOperatorOnClause();
			setState(1445);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IN:
				{
				setState(1443);
				((MakeSeriesOperatorContext)_localctx).InRangeClause = makeSeriesOperatorInRangeClause();
				}
				break;
			case FROM:
			case STEP:
			case TO:
				{
				setState(1444);
				((MakeSeriesOperatorContext)_localctx).FromToStepClause = makeSeriesOperatorFromToStepClause();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(1448);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BY) {
				{
				setState(1447);
				((MakeSeriesOperatorContext)_localctx).ByClause = makeSeriesOperatorByClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorOnClauseContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public TerminalNode ON() { return getToken(HqlParser.ON, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public MakeSeriesOperatorOnClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperatorOnClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperatorOnClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperatorOnClause(this);
		}
	}

	public final MakeSeriesOperatorOnClauseContext makeSeriesOperatorOnClause() throws RecognitionException {
		MakeSeriesOperatorOnClauseContext _localctx = new MakeSeriesOperatorOnClauseContext(_ctx, getState());
		enterRule(_localctx, 214, RULE_makeSeriesOperatorOnClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1450);
			match(ON);
			setState(1451);
			((MakeSeriesOperatorOnClauseContext)_localctx).Expression = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorAggregationContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public MakeSeriesOperatorExpressionDefaultClauseContext Default;
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public MakeSeriesOperatorExpressionDefaultClauseContext makeSeriesOperatorExpressionDefaultClause() {
			return getRuleContext(MakeSeriesOperatorExpressionDefaultClauseContext.class,0);
		}
		public MakeSeriesOperatorAggregationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperatorAggregation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperatorAggregation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperatorAggregation(this);
		}
	}

	public final MakeSeriesOperatorAggregationContext makeSeriesOperatorAggregation() throws RecognitionException {
		MakeSeriesOperatorAggregationContext _localctx = new MakeSeriesOperatorAggregationContext(_ctx, getState());
		enterRule(_localctx, 216, RULE_makeSeriesOperatorAggregation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1453);
			((MakeSeriesOperatorAggregationContext)_localctx).Expression = namedExpression();
			setState(1455);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULT) {
				{
				setState(1454);
				((MakeSeriesOperatorAggregationContext)_localctx).Default = makeSeriesOperatorExpressionDefaultClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorExpressionDefaultClauseContext extends ParserRuleContext {
		public NamedExpressionContext Value;
		public TerminalNode DEFAULT() { return getToken(HqlParser.DEFAULT, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public MakeSeriesOperatorExpressionDefaultClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperatorExpressionDefaultClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperatorExpressionDefaultClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperatorExpressionDefaultClause(this);
		}
	}

	public final MakeSeriesOperatorExpressionDefaultClauseContext makeSeriesOperatorExpressionDefaultClause() throws RecognitionException {
		MakeSeriesOperatorExpressionDefaultClauseContext _localctx = new MakeSeriesOperatorExpressionDefaultClauseContext(_ctx, getState());
		enterRule(_localctx, 218, RULE_makeSeriesOperatorExpressionDefaultClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1457);
			match(DEFAULT);
			setState(1458);
			match(EQUAL);
			setState(1459);
			((MakeSeriesOperatorExpressionDefaultClauseContext)_localctx).Value = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorInRangeClauseContext extends ParserRuleContext {
		public NamedExpressionContext FromExpression;
		public Token ToComma;
		public NamedExpressionContext ToExpression;
		public Token StepComma;
		public NamedExpressionContext StepExpression;
		public TerminalNode IN() { return getToken(HqlParser.IN, 0); }
		public TerminalNode RANGE() { return getToken(HqlParser.RANGE, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public MakeSeriesOperatorInRangeClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperatorInRangeClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperatorInRangeClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperatorInRangeClause(this);
		}
	}

	public final MakeSeriesOperatorInRangeClauseContext makeSeriesOperatorInRangeClause() throws RecognitionException {
		MakeSeriesOperatorInRangeClauseContext _localctx = new MakeSeriesOperatorInRangeClauseContext(_ctx, getState());
		enterRule(_localctx, 220, RULE_makeSeriesOperatorInRangeClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1461);
			match(IN);
			setState(1462);
			match(RANGE);
			setState(1463);
			match(OPENPAREN);
			setState(1464);
			((MakeSeriesOperatorInRangeClauseContext)_localctx).FromExpression = namedExpression();
			setState(1465);
			((MakeSeriesOperatorInRangeClauseContext)_localctx).ToComma = match(COMMA);
			setState(1466);
			((MakeSeriesOperatorInRangeClauseContext)_localctx).ToExpression = namedExpression();
			setState(1467);
			((MakeSeriesOperatorInRangeClauseContext)_localctx).StepComma = match(COMMA);
			setState(1468);
			((MakeSeriesOperatorInRangeClauseContext)_localctx).StepExpression = namedExpression();
			setState(1469);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorFromToStepClauseContext extends ParserRuleContext {
		public NamedExpressionContext FromExpression;
		public NamedExpressionContext ToExpression;
		public NamedExpressionContext StepExpression;
		public TerminalNode STEP() { return getToken(HqlParser.STEP, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public TerminalNode FROM() { return getToken(HqlParser.FROM, 0); }
		public TerminalNode TO() { return getToken(HqlParser.TO, 0); }
		public MakeSeriesOperatorFromToStepClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperatorFromToStepClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperatorFromToStepClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperatorFromToStepClause(this);
		}
	}

	public final MakeSeriesOperatorFromToStepClauseContext makeSeriesOperatorFromToStepClause() throws RecognitionException {
		MakeSeriesOperatorFromToStepClauseContext _localctx = new MakeSeriesOperatorFromToStepClauseContext(_ctx, getState());
		enterRule(_localctx, 222, RULE_makeSeriesOperatorFromToStepClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1473);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FROM) {
				{
				setState(1471);
				match(FROM);
				setState(1472);
				((MakeSeriesOperatorFromToStepClauseContext)_localctx).FromExpression = namedExpression();
				}
			}

			setState(1477);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TO) {
				{
				setState(1475);
				match(TO);
				setState(1476);
				((MakeSeriesOperatorFromToStepClauseContext)_localctx).ToExpression = namedExpression();
				}
			}

			setState(1479);
			match(STEP);
			setState(1480);
			((MakeSeriesOperatorFromToStepClauseContext)_localctx).StepExpression = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MakeSeriesOperatorByClauseContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public MakeSeriesOperatorByClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_makeSeriesOperatorByClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMakeSeriesOperatorByClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMakeSeriesOperatorByClause(this);
		}
	}

	public final MakeSeriesOperatorByClauseContext makeSeriesOperatorByClause() throws RecognitionException {
		MakeSeriesOperatorByClauseContext _localctx = new MakeSeriesOperatorByClauseContext(_ctx, getState());
		enterRule(_localctx, 224, RULE_makeSeriesOperatorByClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1482);
			match(BY);
			setState(1483);
			((MakeSeriesOperatorByClauseContext)_localctx).namedExpression = namedExpression();
			((MakeSeriesOperatorByClauseContext)_localctx).Expressions.add(((MakeSeriesOperatorByClauseContext)_localctx).namedExpression);
			setState(1488);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1484);
				match(COMMA);
				setState(1485);
				((MakeSeriesOperatorByClauseContext)_localctx).namedExpression = namedExpression();
				((MakeSeriesOperatorByClauseContext)_localctx).Expressions.add(((MakeSeriesOperatorByClauseContext)_localctx).namedExpression);
				}
				}
				setState(1490);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvapplyOperatorContext extends ParserRuleContext {
		public Token Keyword;
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public MvapplyOperatorExpressionContext mvapplyOperatorExpression;
		public List<MvapplyOperatorExpressionContext> Expressions = new ArrayList<MvapplyOperatorExpressionContext>();
		public MvapplyOperatorLimitClauseContext LimitClause;
		public MvapplyOperatorIdClauseContext IdClause;
		public ContextualSubExpressionContext OnExpression;
		public TerminalNode ON() { return getToken(HqlParser.ON, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<MvapplyOperatorExpressionContext> mvapplyOperatorExpression() {
			return getRuleContexts(MvapplyOperatorExpressionContext.class);
		}
		public MvapplyOperatorExpressionContext mvapplyOperatorExpression(int i) {
			return getRuleContext(MvapplyOperatorExpressionContext.class,i);
		}
		public ContextualSubExpressionContext contextualSubExpression() {
			return getRuleContext(ContextualSubExpressionContext.class,0);
		}
		public TerminalNode MVAPPLY() { return getToken(HqlParser.MVAPPLY, 0); }
		public TerminalNode MV_APPLY() { return getToken(HqlParser.MV_APPLY, 0); }
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public MvapplyOperatorLimitClauseContext mvapplyOperatorLimitClause() {
			return getRuleContext(MvapplyOperatorLimitClauseContext.class,0);
		}
		public MvapplyOperatorIdClauseContext mvapplyOperatorIdClause() {
			return getRuleContext(MvapplyOperatorIdClauseContext.class,0);
		}
		public MvapplyOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvapplyOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvapplyOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvapplyOperator(this);
		}
	}

	public final MvapplyOperatorContext mvapplyOperator() throws RecognitionException {
		MvapplyOperatorContext _localctx = new MvapplyOperatorContext(_ctx, getState());
		enterRule(_localctx, 226, RULE_mvapplyOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1491);
			((MvapplyOperatorContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==MV_APPLY || _la==MVAPPLY) ) {
				((MvapplyOperatorContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1495);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(1492);
				((MvapplyOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((MvapplyOperatorContext)_localctx).Parameters.add(((MvapplyOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(1497);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1498);
			((MvapplyOperatorContext)_localctx).mvapplyOperatorExpression = mvapplyOperatorExpression();
			((MvapplyOperatorContext)_localctx).Expressions.add(((MvapplyOperatorContext)_localctx).mvapplyOperatorExpression);
			setState(1503);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1499);
				match(COMMA);
				setState(1500);
				((MvapplyOperatorContext)_localctx).mvapplyOperatorExpression = mvapplyOperatorExpression();
				((MvapplyOperatorContext)_localctx).Expressions.add(((MvapplyOperatorContext)_localctx).mvapplyOperatorExpression);
				}
				}
				setState(1505);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1507);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LIMIT) {
				{
				setState(1506);
				((MvapplyOperatorContext)_localctx).LimitClause = mvapplyOperatorLimitClause();
				}
			}

			setState(1510);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(1509);
				((MvapplyOperatorContext)_localctx).IdClause = mvapplyOperatorIdClause();
				}
			}

			setState(1512);
			match(ON);
			setState(1513);
			match(OPENPAREN);
			setState(1514);
			((MvapplyOperatorContext)_localctx).OnExpression = contextualSubExpression();
			setState(1515);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvapplyOperatorLimitClauseContext extends ParserRuleContext {
		public Token LimitValue;
		public TerminalNode LIMIT() { return getToken(HqlParser.LIMIT, 0); }
		public TerminalNode LONGLITERAL() { return getToken(HqlParser.LONGLITERAL, 0); }
		public MvapplyOperatorLimitClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvapplyOperatorLimitClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvapplyOperatorLimitClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvapplyOperatorLimitClause(this);
		}
	}

	public final MvapplyOperatorLimitClauseContext mvapplyOperatorLimitClause() throws RecognitionException {
		MvapplyOperatorLimitClauseContext _localctx = new MvapplyOperatorLimitClauseContext(_ctx, getState());
		enterRule(_localctx, 228, RULE_mvapplyOperatorLimitClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1517);
			match(LIMIT);
			setState(1518);
			((MvapplyOperatorLimitClauseContext)_localctx).LimitValue = match(LONGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvapplyOperatorIdClauseContext extends ParserRuleContext {
		public Token IdValue;
		public TerminalNode ID() { return getToken(HqlParser.ID, 0); }
		public TerminalNode GUIDLITERAL() { return getToken(HqlParser.GUIDLITERAL, 0); }
		public MvapplyOperatorIdClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvapplyOperatorIdClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvapplyOperatorIdClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvapplyOperatorIdClause(this);
		}
	}

	public final MvapplyOperatorIdClauseContext mvapplyOperatorIdClause() throws RecognitionException {
		MvapplyOperatorIdClauseContext _localctx = new MvapplyOperatorIdClauseContext(_ctx, getState());
		enterRule(_localctx, 230, RULE_mvapplyOperatorIdClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1520);
			match(ID);
			setState(1521);
			((MvapplyOperatorIdClauseContext)_localctx).IdValue = match(GUIDLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvapplyOperatorExpressionContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public MvapplyOperatorExpressionToClauseContext ToClause;
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public MvapplyOperatorExpressionToClauseContext mvapplyOperatorExpressionToClause() {
			return getRuleContext(MvapplyOperatorExpressionToClauseContext.class,0);
		}
		public MvapplyOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvapplyOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvapplyOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvapplyOperatorExpression(this);
		}
	}

	public final MvapplyOperatorExpressionContext mvapplyOperatorExpression() throws RecognitionException {
		MvapplyOperatorExpressionContext _localctx = new MvapplyOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 232, RULE_mvapplyOperatorExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1523);
			((MvapplyOperatorExpressionContext)_localctx).Expression = namedExpression();
			setState(1525);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TO) {
				{
				setState(1524);
				((MvapplyOperatorExpressionContext)_localctx).ToClause = mvapplyOperatorExpressionToClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvapplyOperatorExpressionToClauseContext extends ParserRuleContext {
		public Token Type;
		public TerminalNode TO() { return getToken(HqlParser.TO, 0); }
		public TerminalNode TYPELITERAL() { return getToken(HqlParser.TYPELITERAL, 0); }
		public MvapplyOperatorExpressionToClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvapplyOperatorExpressionToClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvapplyOperatorExpressionToClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvapplyOperatorExpressionToClause(this);
		}
	}

	public final MvapplyOperatorExpressionToClauseContext mvapplyOperatorExpressionToClause() throws RecognitionException {
		MvapplyOperatorExpressionToClauseContext _localctx = new MvapplyOperatorExpressionToClauseContext(_ctx, getState());
		enterRule(_localctx, 234, RULE_mvapplyOperatorExpressionToClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1527);
			match(TO);
			setState(1528);
			((MvapplyOperatorExpressionToClauseContext)_localctx).Type = match(TYPELITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvexpandOperatorContext extends ParserRuleContext {
		public Token Keyword;
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public MvexpandOperatorExpressionContext mvexpandOperatorExpression;
		public List<MvexpandOperatorExpressionContext> Expressions = new ArrayList<MvexpandOperatorExpressionContext>();
		public MvapplyOperatorLimitClauseContext LimitClause;
		public List<MvexpandOperatorExpressionContext> mvexpandOperatorExpression() {
			return getRuleContexts(MvexpandOperatorExpressionContext.class);
		}
		public MvexpandOperatorExpressionContext mvexpandOperatorExpression(int i) {
			return getRuleContext(MvexpandOperatorExpressionContext.class,i);
		}
		public TerminalNode MVEXPAND() { return getToken(HqlParser.MVEXPAND, 0); }
		public TerminalNode MV_EXPAND() { return getToken(HqlParser.MV_EXPAND, 0); }
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public MvapplyOperatorLimitClauseContext mvapplyOperatorLimitClause() {
			return getRuleContext(MvapplyOperatorLimitClauseContext.class,0);
		}
		public MvexpandOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvexpandOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvexpandOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvexpandOperator(this);
		}
	}

	public final MvexpandOperatorContext mvexpandOperator() throws RecognitionException {
		MvexpandOperatorContext _localctx = new MvexpandOperatorContext(_ctx, getState());
		enterRule(_localctx, 236, RULE_mvexpandOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1530);
			((MvexpandOperatorContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==MV_EXPAND || _la==MVEXPAND) ) {
				((MvexpandOperatorContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1534);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(1531);
				((MvexpandOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((MvexpandOperatorContext)_localctx).Parameters.add(((MvexpandOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(1536);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1537);
			((MvexpandOperatorContext)_localctx).mvexpandOperatorExpression = mvexpandOperatorExpression();
			((MvexpandOperatorContext)_localctx).Expressions.add(((MvexpandOperatorContext)_localctx).mvexpandOperatorExpression);
			setState(1542);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1538);
				match(COMMA);
				setState(1539);
				((MvexpandOperatorContext)_localctx).mvexpandOperatorExpression = mvexpandOperatorExpression();
				((MvexpandOperatorContext)_localctx).Expressions.add(((MvexpandOperatorContext)_localctx).mvexpandOperatorExpression);
				}
				}
				setState(1544);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1546);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==LIMIT) {
				{
				setState(1545);
				((MvexpandOperatorContext)_localctx).LimitClause = mvapplyOperatorLimitClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MvexpandOperatorExpressionContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public MvapplyOperatorExpressionToClauseContext ToClause;
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public MvapplyOperatorExpressionToClauseContext mvapplyOperatorExpressionToClause() {
			return getRuleContext(MvapplyOperatorExpressionToClauseContext.class,0);
		}
		public MvexpandOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mvexpandOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMvexpandOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMvexpandOperatorExpression(this);
		}
	}

	public final MvexpandOperatorExpressionContext mvexpandOperatorExpression() throws RecognitionException {
		MvexpandOperatorExpressionContext _localctx = new MvexpandOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 238, RULE_mvexpandOperatorExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1548);
			((MvexpandOperatorExpressionContext)_localctx).Expression = namedExpression();
			setState(1550);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TO) {
				{
				setState(1549);
				((MvexpandOperatorExpressionContext)_localctx).ToClause = mvapplyOperatorExpressionToClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseOperatorContext extends ParserRuleContext {
		public ParseOperatorKindClauseContext KindClause;
		public UnnamedExpressionContext Expression;
		public ParseOperatorPatternContext Pattern;
		public TerminalNode PARSE() { return getToken(HqlParser.PARSE, 0); }
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public ParseOperatorPatternContext parseOperatorPattern() {
			return getRuleContext(ParseOperatorPatternContext.class,0);
		}
		public ParseOperatorKindClauseContext parseOperatorKindClause() {
			return getRuleContext(ParseOperatorKindClauseContext.class,0);
		}
		public ParseOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseOperator(this);
		}
	}

	public final ParseOperatorContext parseOperator() throws RecognitionException {
		ParseOperatorContext _localctx = new ParseOperatorContext(_ctx, getState());
		enterRule(_localctx, 240, RULE_parseOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1552);
			match(PARSE);
			setState(1554);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KIND) {
				{
				setState(1553);
				((ParseOperatorContext)_localctx).KindClause = parseOperatorKindClause();
				}
			}

			setState(1556);
			((ParseOperatorContext)_localctx).Expression = unnamedExpression();
			setState(1557);
			match(WITH);
			setState(1558);
			((ParseOperatorContext)_localctx).Pattern = parseOperatorPattern();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseOperatorKindClauseContext extends ParserRuleContext {
		public Token Kind;
		public ParseOperatorFlagsClauseContext FlagsClause;
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode SIMPLE() { return getToken(HqlParser.SIMPLE, 0); }
		public TerminalNode REGEX() { return getToken(HqlParser.REGEX, 0); }
		public TerminalNode RELAXED() { return getToken(HqlParser.RELAXED, 0); }
		public ParseOperatorFlagsClauseContext parseOperatorFlagsClause() {
			return getRuleContext(ParseOperatorFlagsClauseContext.class,0);
		}
		public ParseOperatorKindClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseOperatorKindClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseOperatorKindClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseOperatorKindClause(this);
		}
	}

	public final ParseOperatorKindClauseContext parseOperatorKindClause() throws RecognitionException {
		ParseOperatorKindClauseContext _localctx = new ParseOperatorKindClauseContext(_ctx, getState());
		enterRule(_localctx, 242, RULE_parseOperatorKindClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1560);
			match(KIND);
			setState(1561);
			match(EQUAL);
			setState(1562);
			((ParseOperatorKindClauseContext)_localctx).Kind = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 216)) & ~0x3f) == 0 && ((1L << (_la - 216)) & 8195L) != 0)) ) {
				((ParseOperatorKindClauseContext)_localctx).Kind = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1564);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==FLAGS) {
				{
				setState(1563);
				((ParseOperatorKindClauseContext)_localctx).FlagsClause = parseOperatorFlagsClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseOperatorFlagsClauseContext extends ParserRuleContext {
		public Token Flags;
		public TerminalNode FLAGS() { return getToken(HqlParser.FLAGS, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public ParseOperatorFlagsClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseOperatorFlagsClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseOperatorFlagsClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseOperatorFlagsClause(this);
		}
	}

	public final ParseOperatorFlagsClauseContext parseOperatorFlagsClause() throws RecognitionException {
		ParseOperatorFlagsClauseContext _localctx = new ParseOperatorFlagsClauseContext(_ctx, getState());
		enterRule(_localctx, 244, RULE_parseOperatorFlagsClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1566);
			match(FLAGS);
			setState(1567);
			match(EQUAL);
			setState(1568);
			((ParseOperatorFlagsClauseContext)_localctx).Flags = match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseOperatorNameAndOptionalTypeContext extends ParserRuleContext {
		public SimpleNameReferenceContext Name;
		public ScalarTypeContext Type;
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ScalarTypeContext scalarType() {
			return getRuleContext(ScalarTypeContext.class,0);
		}
		public ParseOperatorNameAndOptionalTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseOperatorNameAndOptionalType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseOperatorNameAndOptionalType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseOperatorNameAndOptionalType(this);
		}
	}

	public final ParseOperatorNameAndOptionalTypeContext parseOperatorNameAndOptionalType() throws RecognitionException {
		ParseOperatorNameAndOptionalTypeContext _localctx = new ParseOperatorNameAndOptionalTypeContext(_ctx, getState());
		enterRule(_localctx, 246, RULE_parseOperatorNameAndOptionalType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1570);
			((ParseOperatorNameAndOptionalTypeContext)_localctx).Name = simpleNameReference();
			setState(1573);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COLON) {
				{
				setState(1571);
				match(COLON);
				setState(1572);
				((ParseOperatorNameAndOptionalTypeContext)_localctx).Type = scalarType();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseOperatorPatternContext extends ParserRuleContext {
		public ParseOperatorNameAndOptionalTypeContext LeadingColumn;
		public ParseOperatorPatternSegmentContext parseOperatorPatternSegment;
		public List<ParseOperatorPatternSegmentContext> Segments = new ArrayList<ParseOperatorPatternSegmentContext>();
		public Token TrailingStar;
		public ParseOperatorNameAndOptionalTypeContext parseOperatorNameAndOptionalType() {
			return getRuleContext(ParseOperatorNameAndOptionalTypeContext.class,0);
		}
		public List<ParseOperatorPatternSegmentContext> parseOperatorPatternSegment() {
			return getRuleContexts(ParseOperatorPatternSegmentContext.class);
		}
		public ParseOperatorPatternSegmentContext parseOperatorPatternSegment(int i) {
			return getRuleContext(ParseOperatorPatternSegmentContext.class,i);
		}
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public ParseOperatorPatternContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseOperatorPattern; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseOperatorPattern(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseOperatorPattern(this);
		}
	}

	public final ParseOperatorPatternContext parseOperatorPattern() throws RecognitionException {
		ParseOperatorPatternContext _localctx = new ParseOperatorPatternContext(_ctx, getState());
		enterRule(_localctx, 248, RULE_parseOperatorPattern);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1576);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622630621017014272L) != 0) || ((((_la - 69)) & ~0x3f) == 0 && ((1L << (_la - 69)) & -8178528127110061463L) != 0) || ((((_la - 140)) & ~0x3f) == 0 && ((1L << (_la - 140)) & 1592259962793370531L) != 0) || ((((_la - 204)) & ~0x3f) == 0 && ((1L << (_la - 204)) & 106397688039329281L) != 0) || ((((_la - 268)) & ~0x3f) == 0 && ((1L << (_la - 268)) & 281474977239039L) != 0)) {
				{
				setState(1575);
				((ParseOperatorPatternContext)_localctx).LeadingColumn = parseOperatorNameAndOptionalType();
				}
			}

			setState(1581);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,110,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1578);
					((ParseOperatorPatternContext)_localctx).parseOperatorPatternSegment = parseOperatorPatternSegment();
					((ParseOperatorPatternContext)_localctx).Segments.add(((ParseOperatorPatternContext)_localctx).parseOperatorPatternSegment);
					}
					} 
				}
				setState(1583);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,110,_ctx);
			}
			setState(1585);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASTERISK) {
				{
				setState(1584);
				((ParseOperatorPatternContext)_localctx).TrailingStar = match(ASTERISK);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseOperatorPatternSegmentContext extends ParserRuleContext {
		public StringLiteralExpressionContext Text;
		public ParseOperatorNameAndOptionalTypeContext Column;
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public ParseOperatorNameAndOptionalTypeContext parseOperatorNameAndOptionalType() {
			return getRuleContext(ParseOperatorNameAndOptionalTypeContext.class,0);
		}
		public ParseOperatorPatternSegmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseOperatorPatternSegment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseOperatorPatternSegment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseOperatorPatternSegment(this);
		}
	}

	public final ParseOperatorPatternSegmentContext parseOperatorPatternSegment() throws RecognitionException {
		ParseOperatorPatternSegmentContext _localctx = new ParseOperatorPatternSegmentContext(_ctx, getState());
		enterRule(_localctx, 250, RULE_parseOperatorPatternSegment);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1588);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASTERISK) {
				{
				setState(1587);
				match(ASTERISK);
				}
			}

			setState(1590);
			((ParseOperatorPatternSegmentContext)_localctx).Text = stringLiteralExpression();
			setState(1592);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 622630621017014272L) != 0) || ((((_la - 69)) & ~0x3f) == 0 && ((1L << (_la - 69)) & -8178528127110061463L) != 0) || ((((_la - 140)) & ~0x3f) == 0 && ((1L << (_la - 140)) & 1592259962793370531L) != 0) || ((((_la - 204)) & ~0x3f) == 0 && ((1L << (_la - 204)) & 106397688039329281L) != 0) || ((((_la - 268)) & ~0x3f) == 0 && ((1L << (_la - 268)) & 281474977239039L) != 0)) {
				{
				setState(1591);
				((ParseOperatorPatternSegmentContext)_localctx).Column = parseOperatorNameAndOptionalType();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseWhereOperatorContext extends ParserRuleContext {
		public ParseOperatorKindClauseContext KindClause;
		public UnnamedExpressionContext Expression;
		public ParseOperatorPatternContext Pattern;
		public TerminalNode PARSEWHERE() { return getToken(HqlParser.PARSEWHERE, 0); }
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public ParseOperatorPatternContext parseOperatorPattern() {
			return getRuleContext(ParseOperatorPatternContext.class,0);
		}
		public ParseOperatorKindClauseContext parseOperatorKindClause() {
			return getRuleContext(ParseOperatorKindClauseContext.class,0);
		}
		public ParseWhereOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseWhereOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseWhereOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseWhereOperator(this);
		}
	}

	public final ParseWhereOperatorContext parseWhereOperator() throws RecognitionException {
		ParseWhereOperatorContext _localctx = new ParseWhereOperatorContext(_ctx, getState());
		enterRule(_localctx, 252, RULE_parseWhereOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1594);
			match(PARSEWHERE);
			setState(1596);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KIND) {
				{
				setState(1595);
				((ParseWhereOperatorContext)_localctx).KindClause = parseOperatorKindClause();
				}
			}

			setState(1598);
			((ParseWhereOperatorContext)_localctx).Expression = unnamedExpression();
			setState(1599);
			match(WITH);
			setState(1600);
			((ParseWhereOperatorContext)_localctx).Pattern = parseOperatorPattern();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseKvOperatorContext extends ParserRuleContext {
		public UnnamedExpressionContext Expressions;
		public RowSchemaContext Keys;
		public ParseKvWithClauseContext WithClause;
		public TerminalNode PARSEKV() { return getToken(HqlParser.PARSEKV, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public RowSchemaContext rowSchema() {
			return getRuleContext(RowSchemaContext.class,0);
		}
		public ParseKvWithClauseContext parseKvWithClause() {
			return getRuleContext(ParseKvWithClauseContext.class,0);
		}
		public ParseKvOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseKvOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseKvOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseKvOperator(this);
		}
	}

	public final ParseKvOperatorContext parseKvOperator() throws RecognitionException {
		ParseKvOperatorContext _localctx = new ParseKvOperatorContext(_ctx, getState());
		enterRule(_localctx, 254, RULE_parseKvOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1602);
			match(PARSEKV);
			setState(1603);
			((ParseKvOperatorContext)_localctx).Expressions = unnamedExpression();
			setState(1604);
			((ParseKvOperatorContext)_localctx).Keys = rowSchema();
			setState(1606);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(1605);
				((ParseKvOperatorContext)_localctx).WithClause = parseKvWithClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParseKvWithClauseContext extends ParserRuleContext {
		public QueryOperatorPropertyContext queryOperatorProperty;
		public List<QueryOperatorPropertyContext> Properties = new ArrayList<QueryOperatorPropertyContext>();
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<QueryOperatorPropertyContext> queryOperatorProperty() {
			return getRuleContexts(QueryOperatorPropertyContext.class);
		}
		public QueryOperatorPropertyContext queryOperatorProperty(int i) {
			return getRuleContext(QueryOperatorPropertyContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ParseKvWithClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parseKvWithClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParseKvWithClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParseKvWithClause(this);
		}
	}

	public final ParseKvWithClauseContext parseKvWithClause() throws RecognitionException {
		ParseKvWithClauseContext _localctx = new ParseKvWithClauseContext(_ctx, getState());
		enterRule(_localctx, 256, RULE_parseKvWithClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1608);
			match(WITH);
			setState(1609);
			match(OPENPAREN);
			setState(1610);
			((ParseKvWithClauseContext)_localctx).queryOperatorProperty = queryOperatorProperty();
			((ParseKvWithClauseContext)_localctx).Properties.add(((ParseKvWithClauseContext)_localctx).queryOperatorProperty);
			setState(1615);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1611);
				match(COMMA);
				setState(1612);
				((ParseKvWithClauseContext)_localctx).queryOperatorProperty = queryOperatorProperty();
				((ParseKvWithClauseContext)_localctx).Properties.add(((ParseKvWithClauseContext)_localctx).queryOperatorProperty);
				}
				}
				setState(1617);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1618);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartitionOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public EntityExpressionContext ByExpression;
		public PartitionOperatorInClauseContext InClause;
		public PartitionOperatorSubExpressionBodyContext SubExpressionBody;
		public PartitionOperatorFullExpressionBodyContext FullExpressionBody;
		public TerminalNode PARTITION() { return getToken(HqlParser.PARTITION, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public EntityExpressionContext entityExpression() {
			return getRuleContext(EntityExpressionContext.class,0);
		}
		public PartitionOperatorSubExpressionBodyContext partitionOperatorSubExpressionBody() {
			return getRuleContext(PartitionOperatorSubExpressionBodyContext.class,0);
		}
		public PartitionOperatorFullExpressionBodyContext partitionOperatorFullExpressionBody() {
			return getRuleContext(PartitionOperatorFullExpressionBodyContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public PartitionOperatorInClauseContext partitionOperatorInClause() {
			return getRuleContext(PartitionOperatorInClauseContext.class,0);
		}
		public PartitionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partitionOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPartitionOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPartitionOperator(this);
		}
	}

	public final PartitionOperatorContext partitionOperator() throws RecognitionException {
		PartitionOperatorContext _localctx = new PartitionOperatorContext(_ctx, getState());
		enterRule(_localctx, 258, RULE_partitionOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1620);
			match(PARTITION);
			setState(1624);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1621);
				((PartitionOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((PartitionOperatorContext)_localctx).Parameters.add(((PartitionOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1626);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1627);
			match(BY);
			setState(1628);
			((PartitionOperatorContext)_localctx).ByExpression = entityExpression();
			setState(1630);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IN) {
				{
				setState(1629);
				((PartitionOperatorContext)_localctx).InClause = partitionOperatorInClause();
				}
			}

			setState(1634);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPENPAREN:
				{
				setState(1632);
				((PartitionOperatorContext)_localctx).SubExpressionBody = partitionOperatorSubExpressionBody();
				}
				break;
			case OPENBRACE:
				{
				setState(1633);
				((PartitionOperatorContext)_localctx).FullExpressionBody = partitionOperatorFullExpressionBody();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartitionOperatorInClauseContext extends ParserRuleContext {
		public FunctionCallExpressionContext FunctionCall;
		public DynamicLiteralExpressionContext Literal;
		public TerminalNode IN() { return getToken(HqlParser.IN, 0); }
		public FunctionCallExpressionContext functionCallExpression() {
			return getRuleContext(FunctionCallExpressionContext.class,0);
		}
		public DynamicLiteralExpressionContext dynamicLiteralExpression() {
			return getRuleContext(DynamicLiteralExpressionContext.class,0);
		}
		public PartitionOperatorInClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partitionOperatorInClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPartitionOperatorInClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPartitionOperatorInClause(this);
		}
	}

	public final PartitionOperatorInClauseContext partitionOperatorInClause() throws RecognitionException {
		PartitionOperatorInClauseContext _localctx = new PartitionOperatorInClauseContext(_ctx, getState());
		enterRule(_localctx, 260, RULE_partitionOperatorInClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1636);
			match(IN);
			setState(1639);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPENBRACKET:
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case COUNT:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(1637);
				((PartitionOperatorInClauseContext)_localctx).FunctionCall = functionCallExpression();
				}
				break;
			case DYNAMIC:
				{
				setState(1638);
				((PartitionOperatorInClauseContext)_localctx).Literal = dynamicLiteralExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartitionOperatorSubExpressionBodyContext extends ParserRuleContext {
		public PipeSubExpressionContext SubExpression;
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public PipeSubExpressionContext pipeSubExpression() {
			return getRuleContext(PipeSubExpressionContext.class,0);
		}
		public PartitionOperatorSubExpressionBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partitionOperatorSubExpressionBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPartitionOperatorSubExpressionBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPartitionOperatorSubExpressionBody(this);
		}
	}

	public final PartitionOperatorSubExpressionBodyContext partitionOperatorSubExpressionBody() throws RecognitionException {
		PartitionOperatorSubExpressionBodyContext _localctx = new PartitionOperatorSubExpressionBodyContext(_ctx, getState());
		enterRule(_localctx, 262, RULE_partitionOperatorSubExpressionBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1641);
			match(OPENPAREN);
			setState(1642);
			((PartitionOperatorSubExpressionBodyContext)_localctx).SubExpression = pipeSubExpression();
			setState(1643);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartitionOperatorFullExpressionBodyContext extends ParserRuleContext {
		public PipeExpressionContext Expression;
		public TerminalNode OPENBRACE() { return getToken(HqlParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(HqlParser.CLOSEBRACE, 0); }
		public PipeExpressionContext pipeExpression() {
			return getRuleContext(PipeExpressionContext.class,0);
		}
		public PartitionOperatorFullExpressionBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partitionOperatorFullExpressionBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPartitionOperatorFullExpressionBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPartitionOperatorFullExpressionBody(this);
		}
	}

	public final PartitionOperatorFullExpressionBodyContext partitionOperatorFullExpressionBody() throws RecognitionException {
		PartitionOperatorFullExpressionBodyContext _localctx = new PartitionOperatorFullExpressionBodyContext(_ctx, getState());
		enterRule(_localctx, 264, RULE_partitionOperatorFullExpressionBody);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1645);
			match(OPENBRACE);
			setState(1646);
			((PartitionOperatorFullExpressionBodyContext)_localctx).Expression = pipeExpression();
			setState(1647);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartitionByOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public EntityExpressionContext Column;
		public PartitionByOperatorIdClauseContext IdClause;
		public ContextualSubExpressionContext SubExpression;
		public TerminalNode PARTITIONBY() { return getToken(HqlParser.PARTITIONBY, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public EntityExpressionContext entityExpression() {
			return getRuleContext(EntityExpressionContext.class,0);
		}
		public ContextualSubExpressionContext contextualSubExpression() {
			return getRuleContext(ContextualSubExpressionContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public PartitionByOperatorIdClauseContext partitionByOperatorIdClause() {
			return getRuleContext(PartitionByOperatorIdClauseContext.class,0);
		}
		public PartitionByOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partitionByOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPartitionByOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPartitionByOperator(this);
		}
	}

	public final PartitionByOperatorContext partitionByOperator() throws RecognitionException {
		PartitionByOperatorContext _localctx = new PartitionByOperatorContext(_ctx, getState());
		enterRule(_localctx, 266, RULE_partitionByOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1649);
			match(PARTITIONBY);
			setState(1653);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,121,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1650);
					((PartitionByOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((PartitionByOperatorContext)_localctx).Parameters.add(((PartitionByOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1655);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,121,_ctx);
			}
			setState(1656);
			((PartitionByOperatorContext)_localctx).Column = entityExpression();
			setState(1658);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(1657);
				((PartitionByOperatorContext)_localctx).IdClause = partitionByOperatorIdClause();
				}
			}

			setState(1660);
			match(OPENPAREN);
			setState(1661);
			((PartitionByOperatorContext)_localctx).SubExpression = contextualSubExpression();
			setState(1662);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PartitionByOperatorIdClauseContext extends ParserRuleContext {
		public Token IdValue;
		public TerminalNode ID() { return getToken(HqlParser.ID, 0); }
		public TerminalNode GUIDLITERAL() { return getToken(HqlParser.GUIDLITERAL, 0); }
		public PartitionByOperatorIdClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_partitionByOperatorIdClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPartitionByOperatorIdClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPartitionByOperatorIdClause(this);
		}
	}

	public final PartitionByOperatorIdClauseContext partitionByOperatorIdClause() throws RecognitionException {
		PartitionByOperatorIdClauseContext _localctx = new PartitionByOperatorIdClauseContext(_ctx, getState());
		enterRule(_localctx, 268, RULE_partitionByOperatorIdClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1664);
			match(ID);
			setState(1665);
			((PartitionByOperatorIdClauseContext)_localctx).IdValue = match(GUIDLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrintOperatorContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode PRINT() { return getToken(HqlParser.PRINT, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public PrintOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPrintOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPrintOperator(this);
		}
	}

	public final PrintOperatorContext printOperator() throws RecognitionException {
		PrintOperatorContext _localctx = new PrintOperatorContext(_ctx, getState());
		enterRule(_localctx, 270, RULE_printOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1667);
			match(PRINT);
			setState(1668);
			((PrintOperatorContext)_localctx).namedExpression = namedExpression();
			((PrintOperatorContext)_localctx).Expressions.add(((PrintOperatorContext)_localctx).namedExpression);
			setState(1673);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1669);
				match(COMMA);
				setState(1670);
				((PrintOperatorContext)_localctx).namedExpression = namedExpression();
				((PrintOperatorContext)_localctx).Expressions.add(((PrintOperatorContext)_localctx).namedExpression);
				}
				}
				setState(1675);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProjectAwayOperatorContext extends ParserRuleContext {
		public SimpleOrWildcardedNameReferenceContext simpleOrWildcardedNameReference;
		public List<SimpleOrWildcardedNameReferenceContext> Columns = new ArrayList<SimpleOrWildcardedNameReferenceContext>();
		public TerminalNode PROJECTAWAY() { return getToken(HqlParser.PROJECTAWAY, 0); }
		public List<SimpleOrWildcardedNameReferenceContext> simpleOrWildcardedNameReference() {
			return getRuleContexts(SimpleOrWildcardedNameReferenceContext.class);
		}
		public SimpleOrWildcardedNameReferenceContext simpleOrWildcardedNameReference(int i) {
			return getRuleContext(SimpleOrWildcardedNameReferenceContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ProjectAwayOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_projectAwayOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterProjectAwayOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitProjectAwayOperator(this);
		}
	}

	public final ProjectAwayOperatorContext projectAwayOperator() throws RecognitionException {
		ProjectAwayOperatorContext _localctx = new ProjectAwayOperatorContext(_ctx, getState());
		enterRule(_localctx, 272, RULE_projectAwayOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1676);
			match(PROJECTAWAY);
			setState(1685);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416123978121218L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(1677);
				((ProjectAwayOperatorContext)_localctx).simpleOrWildcardedNameReference = simpleOrWildcardedNameReference();
				((ProjectAwayOperatorContext)_localctx).Columns.add(((ProjectAwayOperatorContext)_localctx).simpleOrWildcardedNameReference);
				setState(1682);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1678);
					match(COMMA);
					setState(1679);
					((ProjectAwayOperatorContext)_localctx).simpleOrWildcardedNameReference = simpleOrWildcardedNameReference();
					((ProjectAwayOperatorContext)_localctx).Columns.add(((ProjectAwayOperatorContext)_localctx).simpleOrWildcardedNameReference);
					}
					}
					setState(1684);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProjectKeepOperatorContext extends ParserRuleContext {
		public SimpleOrWildcardedNameReferenceContext simpleOrWildcardedNameReference;
		public List<SimpleOrWildcardedNameReferenceContext> Columns = new ArrayList<SimpleOrWildcardedNameReferenceContext>();
		public TerminalNode PROJECTKEEP() { return getToken(HqlParser.PROJECTKEEP, 0); }
		public List<SimpleOrWildcardedNameReferenceContext> simpleOrWildcardedNameReference() {
			return getRuleContexts(SimpleOrWildcardedNameReferenceContext.class);
		}
		public SimpleOrWildcardedNameReferenceContext simpleOrWildcardedNameReference(int i) {
			return getRuleContext(SimpleOrWildcardedNameReferenceContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ProjectKeepOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_projectKeepOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterProjectKeepOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitProjectKeepOperator(this);
		}
	}

	public final ProjectKeepOperatorContext projectKeepOperator() throws RecognitionException {
		ProjectKeepOperatorContext _localctx = new ProjectKeepOperatorContext(_ctx, getState());
		enterRule(_localctx, 274, RULE_projectKeepOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1687);
			match(PROJECTKEEP);
			setState(1688);
			((ProjectKeepOperatorContext)_localctx).simpleOrWildcardedNameReference = simpleOrWildcardedNameReference();
			((ProjectKeepOperatorContext)_localctx).Columns.add(((ProjectKeepOperatorContext)_localctx).simpleOrWildcardedNameReference);
			setState(1693);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1689);
				match(COMMA);
				setState(1690);
				((ProjectKeepOperatorContext)_localctx).simpleOrWildcardedNameReference = simpleOrWildcardedNameReference();
				((ProjectKeepOperatorContext)_localctx).Columns.add(((ProjectKeepOperatorContext)_localctx).simpleOrWildcardedNameReference);
				}
				}
				setState(1695);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProjectOperatorContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode PROJECT() { return getToken(HqlParser.PROJECT, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ProjectOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_projectOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterProjectOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitProjectOperator(this);
		}
	}

	public final ProjectOperatorContext projectOperator() throws RecognitionException {
		ProjectOperatorContext _localctx = new ProjectOperatorContext(_ctx, getState());
		enterRule(_localctx, 276, RULE_projectOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1696);
			match(PROJECT);
			setState(1705);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416134715541506L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1729240967922960685L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211090525197L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 504262421452422151L) != 0)) {
				{
				setState(1697);
				((ProjectOperatorContext)_localctx).namedExpression = namedExpression();
				((ProjectOperatorContext)_localctx).Expressions.add(((ProjectOperatorContext)_localctx).namedExpression);
				setState(1702);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1698);
					match(COMMA);
					setState(1699);
					((ProjectOperatorContext)_localctx).namedExpression = namedExpression();
					((ProjectOperatorContext)_localctx).Expressions.add(((ProjectOperatorContext)_localctx).namedExpression);
					}
					}
					setState(1704);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProjectRenameOperatorContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode PROJECTRENAME() { return getToken(HqlParser.PROJECTRENAME, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ProjectRenameOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_projectRenameOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterProjectRenameOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitProjectRenameOperator(this);
		}
	}

	public final ProjectRenameOperatorContext projectRenameOperator() throws RecognitionException {
		ProjectRenameOperatorContext _localctx = new ProjectRenameOperatorContext(_ctx, getState());
		enterRule(_localctx, 278, RULE_projectRenameOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1707);
			match(PROJECTRENAME);
			setState(1716);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416134715541506L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1729240967922960685L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211090525197L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 504262421452422151L) != 0)) {
				{
				setState(1708);
				((ProjectRenameOperatorContext)_localctx).namedExpression = namedExpression();
				((ProjectRenameOperatorContext)_localctx).Expressions.add(((ProjectRenameOperatorContext)_localctx).namedExpression);
				setState(1713);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1709);
					match(COMMA);
					setState(1710);
					((ProjectRenameOperatorContext)_localctx).namedExpression = namedExpression();
					((ProjectRenameOperatorContext)_localctx).Expressions.add(((ProjectRenameOperatorContext)_localctx).namedExpression);
					}
					}
					setState(1715);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProjectReorderOperatorContext extends ParserRuleContext {
		public ProjectReorderExpressionContext projectReorderExpression;
		public List<ProjectReorderExpressionContext> Expressions = new ArrayList<ProjectReorderExpressionContext>();
		public TerminalNode PROJECTREORDER() { return getToken(HqlParser.PROJECTREORDER, 0); }
		public List<ProjectReorderExpressionContext> projectReorderExpression() {
			return getRuleContexts(ProjectReorderExpressionContext.class);
		}
		public ProjectReorderExpressionContext projectReorderExpression(int i) {
			return getRuleContext(ProjectReorderExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ProjectReorderOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_projectReorderOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterProjectReorderOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitProjectReorderOperator(this);
		}
	}

	public final ProjectReorderOperatorContext projectReorderOperator() throws RecognitionException {
		ProjectReorderOperatorContext _localctx = new ProjectReorderOperatorContext(_ctx, getState());
		enterRule(_localctx, 280, RULE_projectReorderOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1718);
			match(PROJECTREORDER);
			setState(1727);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416123978121218L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(1719);
				((ProjectReorderOperatorContext)_localctx).projectReorderExpression = projectReorderExpression();
				((ProjectReorderOperatorContext)_localctx).Expressions.add(((ProjectReorderOperatorContext)_localctx).projectReorderExpression);
				setState(1724);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1720);
					match(COMMA);
					setState(1721);
					((ProjectReorderOperatorContext)_localctx).projectReorderExpression = projectReorderExpression();
					((ProjectReorderOperatorContext)_localctx).Expressions.add(((ProjectReorderOperatorContext)_localctx).projectReorderExpression);
					}
					}
					setState(1726);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProjectReorderExpressionContext extends ParserRuleContext {
		public SimpleOrWildcardedNameReferenceContext Expression;
		public Token Order;
		public SimpleOrWildcardedNameReferenceContext simpleOrWildcardedNameReference() {
			return getRuleContext(SimpleOrWildcardedNameReferenceContext.class,0);
		}
		public TerminalNode ASC() { return getToken(HqlParser.ASC, 0); }
		public TerminalNode DESC() { return getToken(HqlParser.DESC, 0); }
		public TerminalNode GRANNYASC() { return getToken(HqlParser.GRANNYASC, 0); }
		public TerminalNode GRANNYDESC() { return getToken(HqlParser.GRANNYDESC, 0); }
		public ProjectReorderExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_projectReorderExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterProjectReorderExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitProjectReorderExpression(this);
		}
	}

	public final ProjectReorderExpressionContext projectReorderExpression() throws RecognitionException {
		ProjectReorderExpressionContext _localctx = new ProjectReorderExpressionContext(_ctx, getState());
		enterRule(_localctx, 282, RULE_projectReorderExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1729);
			((ProjectReorderExpressionContext)_localctx).Expression = simpleOrWildcardedNameReference();
			setState(1731);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (((((_la - 48)) & ~0x3f) == 0 && ((1L << (_la - 48)) & 1688850128699393L) != 0)) {
				{
				setState(1730);
				((ProjectReorderExpressionContext)_localctx).Order = _input.LT(1);
				_la = _input.LA(1);
				if ( !(((((_la - 48)) & ~0x3f) == 0 && ((1L << (_la - 48)) & 1688850128699393L) != 0)) ) {
					((ProjectReorderExpressionContext)_localctx).Order = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReduceByOperatorContext extends ParserRuleContext {
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext ByExpression;
		public ReduceByWithClauseContext WithClause;
		public TerminalNode REDUCE() { return getToken(HqlParser.REDUCE, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public ReduceByWithClauseContext reduceByWithClause() {
			return getRuleContext(ReduceByWithClauseContext.class,0);
		}
		public ReduceByOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reduceByOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterReduceByOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitReduceByOperator(this);
		}
	}

	public final ReduceByOperatorContext reduceByOperator() throws RecognitionException {
		ReduceByOperatorContext _localctx = new ReduceByOperatorContext(_ctx, getState());
		enterRule(_localctx, 284, RULE_reduceByOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1733);
			match(REDUCE);
			setState(1737);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(1734);
				((ReduceByOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((ReduceByOperatorContext)_localctx).Parameters.add(((ReduceByOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(1739);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1740);
			match(BY);
			setState(1741);
			((ReduceByOperatorContext)_localctx).ByExpression = namedExpression();
			setState(1743);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(1742);
				((ReduceByOperatorContext)_localctx).WithClause = reduceByWithClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReduceByWithClauseContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ReduceByWithClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_reduceByWithClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterReduceByWithClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitReduceByWithClause(this);
		}
	}

	public final ReduceByWithClauseContext reduceByWithClause() throws RecognitionException {
		ReduceByWithClauseContext _localctx = new ReduceByWithClauseContext(_ctx, getState());
		enterRule(_localctx, 286, RULE_reduceByWithClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1745);
			match(WITH);
			setState(1746);
			((ReduceByWithClauseContext)_localctx).namedExpression = namedExpression();
			((ReduceByWithClauseContext)_localctx).Expressions.add(((ReduceByWithClauseContext)_localctx).namedExpression);
			setState(1751);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1747);
				match(COMMA);
				setState(1748);
				((ReduceByWithClauseContext)_localctx).namedExpression = namedExpression();
				((ReduceByWithClauseContext)_localctx).Expressions.add(((ReduceByWithClauseContext)_localctx).namedExpression);
				}
				}
				setState(1753);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenderOperatorContext extends ParserRuleContext {
		public Token CharType;
		public RenderOperatorWithClauseContext WithClause;
		public RenderOperatorLegacyPropertyListContext LegacyPropertyList;
		public TerminalNode RENDER() { return getToken(HqlParser.RENDER, 0); }
		public TerminalNode TABLE() { return getToken(HqlParser.TABLE, 0); }
		public TerminalNode LIST() { return getToken(HqlParser.LIST, 0); }
		public TerminalNode BARCHART() { return getToken(HqlParser.BARCHART, 0); }
		public TerminalNode PIECHART() { return getToken(HqlParser.PIECHART, 0); }
		public TerminalNode LADDERCHART() { return getToken(HqlParser.LADDERCHART, 0); }
		public TerminalNode TIMECHART() { return getToken(HqlParser.TIMECHART, 0); }
		public TerminalNode LINECHART() { return getToken(HqlParser.LINECHART, 0); }
		public TerminalNode ANOMALYCHART() { return getToken(HqlParser.ANOMALYCHART, 0); }
		public TerminalNode PIVOTCHART() { return getToken(HqlParser.PIVOTCHART, 0); }
		public TerminalNode AREACHART() { return getToken(HqlParser.AREACHART, 0); }
		public TerminalNode STACKEDAREACHART() { return getToken(HqlParser.STACKEDAREACHART, 0); }
		public TerminalNode SCATTERCHART() { return getToken(HqlParser.SCATTERCHART, 0); }
		public TerminalNode TIMEPIVOT() { return getToken(HqlParser.TIMEPIVOT, 0); }
		public TerminalNode COLUMNCHART() { return getToken(HqlParser.COLUMNCHART, 0); }
		public TerminalNode TIMELINE() { return getToken(HqlParser.TIMELINE, 0); }
		public TerminalNode CHART3D_() { return getToken(HqlParser.CHART3D_, 0); }
		public TerminalNode CARD() { return getToken(HqlParser.CARD, 0); }
		public TerminalNode TREEMAP() { return getToken(HqlParser.TREEMAP, 0); }
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public RenderOperatorWithClauseContext renderOperatorWithClause() {
			return getRuleContext(RenderOperatorWithClauseContext.class,0);
		}
		public RenderOperatorLegacyPropertyListContext renderOperatorLegacyPropertyList() {
			return getRuleContext(RenderOperatorLegacyPropertyListContext.class,0);
		}
		public RenderOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renderOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRenderOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRenderOperator(this);
		}
	}

	public final RenderOperatorContext renderOperator() throws RecognitionException {
		RenderOperatorContext _localctx = new RenderOperatorContext(_ctx, getState());
		enterRule(_localctx, 288, RULE_renderOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1754);
			match(RENDER);
			setState(1755);
			((RenderOperatorContext)_localctx).CharType = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1445743578755104768L) != 0) || ((((_la - 138)) & ~0x3f) == 0 && ((1L << (_la - 138)) & 769L) != 0) || ((((_la - 202)) & ~0x3f) == 0 && ((1L << (_la - 202)) & 1133738226352131L) != 0) || _la==IDENTIFIER) ) {
				((RenderOperatorContext)_localctx).CharType = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(1758);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,137,_ctx) ) {
			case 1:
				{
				setState(1756);
				((RenderOperatorContext)_localctx).WithClause = renderOperatorWithClause();
				}
				break;
			case 2:
				{
				setState(1757);
				((RenderOperatorContext)_localctx).LegacyPropertyList = renderOperatorLegacyPropertyList();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenderOperatorWithClauseContext extends ParserRuleContext {
		public RenderOperatorPropertyContext renderOperatorProperty;
		public List<RenderOperatorPropertyContext> Properties = new ArrayList<RenderOperatorPropertyContext>();
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<RenderOperatorPropertyContext> renderOperatorProperty() {
			return getRuleContexts(RenderOperatorPropertyContext.class);
		}
		public RenderOperatorPropertyContext renderOperatorProperty(int i) {
			return getRuleContext(RenderOperatorPropertyContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public RenderOperatorWithClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renderOperatorWithClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRenderOperatorWithClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRenderOperatorWithClause(this);
		}
	}

	public final RenderOperatorWithClauseContext renderOperatorWithClause() throws RecognitionException {
		RenderOperatorWithClauseContext _localctx = new RenderOperatorWithClauseContext(_ctx, getState());
		enterRule(_localctx, 290, RULE_renderOperatorWithClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1760);
			match(WITH);
			setState(1761);
			match(OPENPAREN);
			setState(1770);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ACCUMULATE || _la==ANOMALYCOLUMNS || _la==KIND || _la==LEGEND || ((((_la - 227)) & ~0x3f) == 0 && ((1L << (_la - 227)) & 4501400604377089L) != 0)) {
				{
				setState(1762);
				((RenderOperatorWithClauseContext)_localctx).renderOperatorProperty = renderOperatorProperty();
				((RenderOperatorWithClauseContext)_localctx).Properties.add(((RenderOperatorWithClauseContext)_localctx).renderOperatorProperty);
				setState(1767);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(1763);
					match(COMMA);
					setState(1764);
					((RenderOperatorWithClauseContext)_localctx).renderOperatorProperty = renderOperatorProperty();
					((RenderOperatorWithClauseContext)_localctx).Properties.add(((RenderOperatorWithClauseContext)_localctx).renderOperatorProperty);
					}
					}
					setState(1769);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(1772);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenderOperatorLegacyPropertyListContext extends ParserRuleContext {
		public RenderOperatorLegacyPropertyContext renderOperatorLegacyProperty;
		public List<RenderOperatorLegacyPropertyContext> Properties = new ArrayList<RenderOperatorLegacyPropertyContext>();
		public List<RenderOperatorLegacyPropertyContext> renderOperatorLegacyProperty() {
			return getRuleContexts(RenderOperatorLegacyPropertyContext.class);
		}
		public RenderOperatorLegacyPropertyContext renderOperatorLegacyProperty(int i) {
			return getRuleContext(RenderOperatorLegacyPropertyContext.class,i);
		}
		public RenderOperatorLegacyPropertyListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renderOperatorLegacyPropertyList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRenderOperatorLegacyPropertyList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRenderOperatorLegacyPropertyList(this);
		}
	}

	public final RenderOperatorLegacyPropertyListContext renderOperatorLegacyPropertyList() throws RecognitionException {
		RenderOperatorLegacyPropertyListContext _localctx = new RenderOperatorLegacyPropertyListContext(_ctx, getState());
		enterRule(_localctx, 292, RULE_renderOperatorLegacyPropertyList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1775); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(1774);
				((RenderOperatorLegacyPropertyListContext)_localctx).renderOperatorLegacyProperty = renderOperatorLegacyProperty();
				((RenderOperatorLegacyPropertyListContext)_localctx).Properties.add(((RenderOperatorLegacyPropertyListContext)_localctx).renderOperatorLegacyProperty);
				}
				}
				setState(1777); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ACCUMULATE || _la==BY || _la==KIND || _la==TITLE || _la==WITH );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenderOperatorPropertyContext extends ParserRuleContext {
		public Token Name;
		public FunctionCallOrPathExpressionContext ExpressionValue;
		public SimpleNameReferenceContext NameValue;
		public RenderPropertyNameListContext NameListValue;
		public Token TokenValue;
		public Token BoolValue;
		public NumericLiteralExpressionContext NumberValue;
		public LiteralExpressionContext LiteralValue;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode TITLE() { return getToken(HqlParser.TITLE, 0); }
		public FunctionCallOrPathExpressionContext functionCallOrPathExpression() {
			return getRuleContext(FunctionCallOrPathExpressionContext.class,0);
		}
		public TerminalNode XCOLUMN() { return getToken(HqlParser.XCOLUMN, 0); }
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public TerminalNode SERIES() { return getToken(HqlParser.SERIES, 0); }
		public RenderPropertyNameListContext renderPropertyNameList() {
			return getRuleContext(RenderPropertyNameListContext.class,0);
		}
		public TerminalNode YCOLUMNS() { return getToken(HqlParser.YCOLUMNS, 0); }
		public TerminalNode ANOMALYCOLUMNS() { return getToken(HqlParser.ANOMALYCOLUMNS, 0); }
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode DEFAULT() { return getToken(HqlParser.DEFAULT, 0); }
		public TerminalNode UNSTACKED() { return getToken(HqlParser.UNSTACKED, 0); }
		public TerminalNode STACKED() { return getToken(HqlParser.STACKED, 0); }
		public TerminalNode STACKED100() { return getToken(HqlParser.STACKED100, 0); }
		public TerminalNode MAP() { return getToken(HqlParser.MAP, 0); }
		public TerminalNode XTITLE() { return getToken(HqlParser.XTITLE, 0); }
		public TerminalNode YTITLE() { return getToken(HqlParser.YTITLE, 0); }
		public TerminalNode XAXIS() { return getToken(HqlParser.XAXIS, 0); }
		public TerminalNode LINEAR() { return getToken(HqlParser.LINEAR, 0); }
		public TerminalNode LOG() { return getToken(HqlParser.LOG, 0); }
		public TerminalNode YAXIS() { return getToken(HqlParser.YAXIS, 0); }
		public TerminalNode LEGEND() { return getToken(HqlParser.LEGEND, 0); }
		public TerminalNode VISIBLE() { return getToken(HqlParser.VISIBLE, 0); }
		public TerminalNode HIDDEN_() { return getToken(HqlParser.HIDDEN_, 0); }
		public TerminalNode YSPLIT() { return getToken(HqlParser.YSPLIT, 0); }
		public TerminalNode NONE() { return getToken(HqlParser.NONE, 0); }
		public TerminalNode AXES() { return getToken(HqlParser.AXES, 0); }
		public TerminalNode PANELS() { return getToken(HqlParser.PANELS, 0); }
		public TerminalNode ACCUMULATE() { return getToken(HqlParser.ACCUMULATE, 0); }
		public TerminalNode BOOLEANLITERAL() { return getToken(HqlParser.BOOLEANLITERAL, 0); }
		public TerminalNode YMIN() { return getToken(HqlParser.YMIN, 0); }
		public NumericLiteralExpressionContext numericLiteralExpression() {
			return getRuleContext(NumericLiteralExpressionContext.class,0);
		}
		public TerminalNode YMAX() { return getToken(HqlParser.YMAX, 0); }
		public TerminalNode XMIN() { return getToken(HqlParser.XMIN, 0); }
		public LiteralExpressionContext literalExpression() {
			return getRuleContext(LiteralExpressionContext.class,0);
		}
		public TerminalNode XMAX() { return getToken(HqlParser.XMAX, 0); }
		public RenderOperatorPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renderOperatorProperty; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRenderOperatorProperty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRenderOperatorProperty(this);
		}
	}

	public final RenderOperatorPropertyContext renderOperatorProperty() throws RecognitionException {
		RenderOperatorPropertyContext _localctx = new RenderOperatorPropertyContext(_ctx, getState());
		enterRule(_localctx, 294, RULE_renderOperatorProperty);
		int _la;
		try {
			setState(1830);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TITLE:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(1779);
				((RenderOperatorPropertyContext)_localctx).Name = match(TITLE);
				setState(1780);
				match(EQUAL);
				setState(1781);
				((RenderOperatorPropertyContext)_localctx).ExpressionValue = functionCallOrPathExpression();
				}
				}
				break;
			case XCOLUMN:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(1782);
				((RenderOperatorPropertyContext)_localctx).Name = match(XCOLUMN);
				setState(1783);
				match(EQUAL);
				setState(1784);
				((RenderOperatorPropertyContext)_localctx).NameValue = simpleNameReference();
				}
				}
				break;
			case SERIES:
				enterOuterAlt(_localctx, 3);
				{
				{
				setState(1785);
				((RenderOperatorPropertyContext)_localctx).Name = match(SERIES);
				setState(1786);
				match(EQUAL);
				setState(1787);
				((RenderOperatorPropertyContext)_localctx).NameListValue = renderPropertyNameList();
				}
				}
				break;
			case YCOLUMNS:
				enterOuterAlt(_localctx, 4);
				{
				{
				setState(1788);
				((RenderOperatorPropertyContext)_localctx).Name = match(YCOLUMNS);
				setState(1789);
				match(EQUAL);
				setState(1790);
				((RenderOperatorPropertyContext)_localctx).NameListValue = renderPropertyNameList();
				}
				}
				break;
			case ANOMALYCOLUMNS:
				enterOuterAlt(_localctx, 5);
				{
				{
				setState(1791);
				((RenderOperatorPropertyContext)_localctx).Name = match(ANOMALYCOLUMNS);
				setState(1792);
				match(EQUAL);
				setState(1793);
				((RenderOperatorPropertyContext)_localctx).NameListValue = renderPropertyNameList();
				}
				}
				break;
			case KIND:
				enterOuterAlt(_localctx, 6);
				{
				{
				setState(1794);
				((RenderOperatorPropertyContext)_localctx).Name = match(KIND);
				setState(1795);
				match(EQUAL);
				setState(1796);
				((RenderOperatorPropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==DEFAULT || _la==MAP || ((((_la - 232)) & ~0x3f) == 0 && ((1L << (_la - 232)) & 8388611L) != 0)) ) {
					((RenderOperatorPropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				break;
			case XTITLE:
				enterOuterAlt(_localctx, 7);
				{
				{
				setState(1797);
				((RenderOperatorPropertyContext)_localctx).Name = match(XTITLE);
				setState(1798);
				match(EQUAL);
				setState(1799);
				((RenderOperatorPropertyContext)_localctx).ExpressionValue = functionCallOrPathExpression();
				}
				}
				break;
			case YTITLE:
				enterOuterAlt(_localctx, 8);
				{
				{
				setState(1800);
				((RenderOperatorPropertyContext)_localctx).Name = match(YTITLE);
				setState(1801);
				match(EQUAL);
				setState(1802);
				((RenderOperatorPropertyContext)_localctx).ExpressionValue = functionCallOrPathExpression();
				}
				}
				break;
			case XAXIS:
				enterOuterAlt(_localctx, 9);
				{
				{
				setState(1803);
				((RenderOperatorPropertyContext)_localctx).Name = match(XAXIS);
				setState(1804);
				match(EQUAL);
				setState(1805);
				((RenderOperatorPropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LINEAR || _la==LOG) ) {
					((RenderOperatorPropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				break;
			case YAXIS:
				enterOuterAlt(_localctx, 10);
				{
				{
				setState(1806);
				((RenderOperatorPropertyContext)_localctx).Name = match(YAXIS);
				setState(1807);
				match(EQUAL);
				setState(1808);
				((RenderOperatorPropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==LINEAR || _la==LOG) ) {
					((RenderOperatorPropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				break;
			case LEGEND:
				enterOuterAlt(_localctx, 11);
				{
				{
				setState(1809);
				((RenderOperatorPropertyContext)_localctx).Name = match(LEGEND);
				setState(1810);
				match(EQUAL);
				setState(1811);
				((RenderOperatorPropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==HIDDEN_ || _la==VISIBLE) ) {
					((RenderOperatorPropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				break;
			case YSPLIT:
				enterOuterAlt(_localctx, 12);
				{
				{
				setState(1812);
				((RenderOperatorPropertyContext)_localctx).Name = match(YSPLIT);
				setState(1813);
				match(EQUAL);
				setState(1814);
				((RenderOperatorPropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==AXES || _la==NONE || _la==PANELS) ) {
					((RenderOperatorPropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				break;
			case ACCUMULATE:
				enterOuterAlt(_localctx, 13);
				{
				{
				setState(1815);
				((RenderOperatorPropertyContext)_localctx).Name = match(ACCUMULATE);
				setState(1816);
				match(EQUAL);
				setState(1817);
				((RenderOperatorPropertyContext)_localctx).BoolValue = match(BOOLEANLITERAL);
				}
				}
				break;
			case YMIN:
				enterOuterAlt(_localctx, 14);
				{
				{
				setState(1818);
				((RenderOperatorPropertyContext)_localctx).Name = match(YMIN);
				setState(1819);
				match(EQUAL);
				setState(1820);
				((RenderOperatorPropertyContext)_localctx).NumberValue = numericLiteralExpression();
				}
				}
				break;
			case YMAX:
				enterOuterAlt(_localctx, 15);
				{
				{
				setState(1821);
				((RenderOperatorPropertyContext)_localctx).Name = match(YMAX);
				setState(1822);
				match(EQUAL);
				setState(1823);
				((RenderOperatorPropertyContext)_localctx).NumberValue = numericLiteralExpression();
				}
				}
				break;
			case XMIN:
				enterOuterAlt(_localctx, 16);
				{
				{
				setState(1824);
				((RenderOperatorPropertyContext)_localctx).Name = match(XMIN);
				setState(1825);
				match(EQUAL);
				setState(1826);
				((RenderOperatorPropertyContext)_localctx).LiteralValue = literalExpression();
				}
				}
				break;
			case XMAX:
				enterOuterAlt(_localctx, 17);
				{
				{
				setState(1827);
				((RenderOperatorPropertyContext)_localctx).Name = match(XMAX);
				setState(1828);
				match(EQUAL);
				setState(1829);
				((RenderOperatorPropertyContext)_localctx).LiteralValue = literalExpression();
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenderPropertyNameListContext extends ParserRuleContext {
		public ExtendedNameReferenceContext extendedNameReference;
		public List<ExtendedNameReferenceContext> Names = new ArrayList<ExtendedNameReferenceContext>();
		public List<ExtendedNameReferenceContext> extendedNameReference() {
			return getRuleContexts(ExtendedNameReferenceContext.class);
		}
		public ExtendedNameReferenceContext extendedNameReference(int i) {
			return getRuleContext(ExtendedNameReferenceContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public RenderPropertyNameListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renderPropertyNameList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRenderPropertyNameList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRenderPropertyNameList(this);
		}
	}

	public final RenderPropertyNameListContext renderPropertyNameList() throws RecognitionException {
		RenderPropertyNameListContext _localctx = new RenderPropertyNameListContext(_ctx, getState());
		enterRule(_localctx, 296, RULE_renderPropertyNameList);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1832);
			((RenderPropertyNameListContext)_localctx).extendedNameReference = extendedNameReference();
			((RenderPropertyNameListContext)_localctx).Names.add(((RenderPropertyNameListContext)_localctx).extendedNameReference);
			setState(1837);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,142,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1833);
					match(COMMA);
					setState(1834);
					((RenderPropertyNameListContext)_localctx).extendedNameReference = extendedNameReference();
					((RenderPropertyNameListContext)_localctx).Names.add(((RenderPropertyNameListContext)_localctx).extendedNameReference);
					}
					} 
				}
				setState(1839);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,142,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RenderOperatorLegacyPropertyContext extends ParserRuleContext {
		public Token Name;
		public StringLiteralExpressionContext StringValue;
		public Token TokenValue;
		public RenderPropertyNameListContext NameListValue;
		public Token BoolValue;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode TITLE() { return getToken(HqlParser.TITLE, 0); }
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode DEFAULT() { return getToken(HqlParser.DEFAULT, 0); }
		public TerminalNode UNSTACKED() { return getToken(HqlParser.UNSTACKED, 0); }
		public TerminalNode STACKED() { return getToken(HqlParser.STACKED, 0); }
		public TerminalNode STACKED100() { return getToken(HqlParser.STACKED100, 0); }
		public TerminalNode MAP() { return getToken(HqlParser.MAP, 0); }
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public RenderPropertyNameListContext renderPropertyNameList() {
			return getRuleContext(RenderPropertyNameListContext.class,0);
		}
		public TerminalNode ACCUMULATE() { return getToken(HqlParser.ACCUMULATE, 0); }
		public TerminalNode BOOLEANLITERAL() { return getToken(HqlParser.BOOLEANLITERAL, 0); }
		public RenderOperatorLegacyPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_renderOperatorLegacyProperty; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRenderOperatorLegacyProperty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRenderOperatorLegacyProperty(this);
		}
	}

	public final RenderOperatorLegacyPropertyContext renderOperatorLegacyProperty() throws RecognitionException {
		RenderOperatorLegacyPropertyContext _localctx = new RenderOperatorLegacyPropertyContext(_ctx, getState());
		enterRule(_localctx, 298, RULE_renderOperatorLegacyProperty);
		int _la;
		try {
			setState(1853);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TITLE:
				enterOuterAlt(_localctx, 1);
				{
				{
				setState(1840);
				((RenderOperatorLegacyPropertyContext)_localctx).Name = match(TITLE);
				setState(1841);
				match(EQUAL);
				setState(1842);
				((RenderOperatorLegacyPropertyContext)_localctx).StringValue = stringLiteralExpression();
				}
				}
				break;
			case KIND:
				enterOuterAlt(_localctx, 2);
				{
				{
				setState(1843);
				((RenderOperatorLegacyPropertyContext)_localctx).Name = match(KIND);
				setState(1844);
				match(EQUAL);
				setState(1845);
				((RenderOperatorLegacyPropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==DEFAULT || _la==MAP || ((((_la - 232)) & ~0x3f) == 0 && ((1L << (_la - 232)) & 8388611L) != 0)) ) {
					((RenderOperatorLegacyPropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				}
				break;
			case WITH:
				enterOuterAlt(_localctx, 3);
				{
				{
				setState(1846);
				((RenderOperatorLegacyPropertyContext)_localctx).Name = match(WITH);
				setState(1847);
				((RenderOperatorLegacyPropertyContext)_localctx).StringValue = stringLiteralExpression();
				}
				}
				break;
			case BY:
				enterOuterAlt(_localctx, 4);
				{
				{
				setState(1848);
				((RenderOperatorLegacyPropertyContext)_localctx).Name = match(BY);
				setState(1849);
				((RenderOperatorLegacyPropertyContext)_localctx).NameListValue = renderPropertyNameList();
				}
				}
				break;
			case ACCUMULATE:
				enterOuterAlt(_localctx, 5);
				{
				{
				setState(1850);
				((RenderOperatorLegacyPropertyContext)_localctx).Name = match(ACCUMULATE);
				setState(1851);
				match(EQUAL);
				setState(1852);
				((RenderOperatorLegacyPropertyContext)_localctx).BoolValue = match(BOOLEANLITERAL);
				}
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SampleDistinctOperatorContext extends ParserRuleContext {
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext Expression;
		public NamedExpressionContext OfExpression;
		public TerminalNode SAMPLE_DISTINCT() { return getToken(HqlParser.SAMPLE_DISTINCT, 0); }
		public TerminalNode OF() { return getToken(HqlParser.OF, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public SampleDistinctOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sampleDistinctOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSampleDistinctOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSampleDistinctOperator(this);
		}
	}

	public final SampleDistinctOperatorContext sampleDistinctOperator() throws RecognitionException {
		SampleDistinctOperatorContext _localctx = new SampleDistinctOperatorContext(_ctx, getState());
		enterRule(_localctx, 300, RULE_sampleDistinctOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1855);
			match(SAMPLE_DISTINCT);
			setState(1859);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(1856);
				((SampleDistinctOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((SampleDistinctOperatorContext)_localctx).Parameters.add(((SampleDistinctOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(1861);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1862);
			((SampleDistinctOperatorContext)_localctx).Expression = namedExpression();
			setState(1863);
			match(OF);
			setState(1864);
			((SampleDistinctOperatorContext)_localctx).OfExpression = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SampleOperatorContext extends ParserRuleContext {
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext Expression;
		public TerminalNode SAMPLE() { return getToken(HqlParser.SAMPLE, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public SampleOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sampleOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSampleOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSampleOperator(this);
		}
	}

	public final SampleOperatorContext sampleOperator() throws RecognitionException {
		SampleOperatorContext _localctx = new SampleOperatorContext(_ctx, getState());
		enterRule(_localctx, 302, RULE_sampleOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1866);
			match(SAMPLE);
			setState(1870);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(1867);
				((SampleOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((SampleOperatorContext)_localctx).Parameters.add(((SampleOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(1872);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1873);
			((SampleOperatorContext)_localctx).Expression = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public ScanOperatorOrderByClauseContext OrderByClause;
		public ScanOperatorPartitionByClauseContext PartitionByClause;
		public ScanOperatorDeclareClauseContext DeclareClause;
		public ScanOperatorStepContext scanOperatorStep;
		public List<ScanOperatorStepContext> Steps = new ArrayList<ScanOperatorStepContext>();
		public TerminalNode SCAN() { return getToken(HqlParser.SCAN, 0); }
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public ScanOperatorOrderByClauseContext scanOperatorOrderByClause() {
			return getRuleContext(ScanOperatorOrderByClauseContext.class,0);
		}
		public ScanOperatorPartitionByClauseContext scanOperatorPartitionByClause() {
			return getRuleContext(ScanOperatorPartitionByClauseContext.class,0);
		}
		public ScanOperatorDeclareClauseContext scanOperatorDeclareClause() {
			return getRuleContext(ScanOperatorDeclareClauseContext.class,0);
		}
		public List<ScanOperatorStepContext> scanOperatorStep() {
			return getRuleContexts(ScanOperatorStepContext.class);
		}
		public ScanOperatorStepContext scanOperatorStep(int i) {
			return getRuleContext(ScanOperatorStepContext.class,i);
		}
		public ScanOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperator(this);
		}
	}

	public final ScanOperatorContext scanOperator() throws RecognitionException {
		ScanOperatorContext _localctx = new ScanOperatorContext(_ctx, getState());
		enterRule(_localctx, 304, RULE_scanOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1875);
			match(SCAN);
			setState(1879);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(1876);
				((ScanOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((ScanOperatorContext)_localctx).Parameters.add(((ScanOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(1881);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1883);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ORDER) {
				{
				setState(1882);
				((ScanOperatorContext)_localctx).OrderByClause = scanOperatorOrderByClause();
				}
			}

			setState(1886);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==PARTITION) {
				{
				setState(1885);
				((ScanOperatorContext)_localctx).PartitionByClause = scanOperatorPartitionByClause();
				}
			}

			setState(1889);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DECLARE) {
				{
				setState(1888);
				((ScanOperatorContext)_localctx).DeclareClause = scanOperatorDeclareClause();
				}
			}

			setState(1891);
			match(WITH);
			setState(1892);
			match(OPENPAREN);
			setState(1894); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(1893);
				((ScanOperatorContext)_localctx).scanOperatorStep = scanOperatorStep();
				((ScanOperatorContext)_localctx).Steps.add(((ScanOperatorContext)_localctx).scanOperatorStep);
				}
				}
				setState(1896); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==STEP );
			setState(1898);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorOrderByClauseContext extends ParserRuleContext {
		public OrderedExpressionContext orderedExpression;
		public List<OrderedExpressionContext> Expressions = new ArrayList<OrderedExpressionContext>();
		public TerminalNode ORDER() { return getToken(HqlParser.ORDER, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<OrderedExpressionContext> orderedExpression() {
			return getRuleContexts(OrderedExpressionContext.class);
		}
		public OrderedExpressionContext orderedExpression(int i) {
			return getRuleContext(OrderedExpressionContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(HqlParser.COMMA, 0); }
		public ScanOperatorOrderByClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorOrderByClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorOrderByClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorOrderByClause(this);
		}
	}

	public final ScanOperatorOrderByClauseContext scanOperatorOrderByClause() throws RecognitionException {
		ScanOperatorOrderByClauseContext _localctx = new ScanOperatorOrderByClauseContext(_ctx, getState());
		enterRule(_localctx, 306, RULE_scanOperatorOrderByClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1900);
			match(ORDER);
			setState(1901);
			match(BY);
			setState(1902);
			((ScanOperatorOrderByClauseContext)_localctx).orderedExpression = orderedExpression();
			((ScanOperatorOrderByClauseContext)_localctx).Expressions.add(((ScanOperatorOrderByClauseContext)_localctx).orderedExpression);
			{
			setState(1903);
			match(COMMA);
			setState(1904);
			((ScanOperatorOrderByClauseContext)_localctx).orderedExpression = orderedExpression();
			((ScanOperatorOrderByClauseContext)_localctx).Expressions.add(((ScanOperatorOrderByClauseContext)_localctx).orderedExpression);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorPartitionByClauseContext extends ParserRuleContext {
		public UnnamedExpressionContext unnamedExpression;
		public List<UnnamedExpressionContext> Expressions = new ArrayList<UnnamedExpressionContext>();
		public TerminalNode PARTITION() { return getToken(HqlParser.PARTITION, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<UnnamedExpressionContext> unnamedExpression() {
			return getRuleContexts(UnnamedExpressionContext.class);
		}
		public UnnamedExpressionContext unnamedExpression(int i) {
			return getRuleContext(UnnamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ScanOperatorPartitionByClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorPartitionByClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorPartitionByClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorPartitionByClause(this);
		}
	}

	public final ScanOperatorPartitionByClauseContext scanOperatorPartitionByClause() throws RecognitionException {
		ScanOperatorPartitionByClauseContext _localctx = new ScanOperatorPartitionByClauseContext(_ctx, getState());
		enterRule(_localctx, 308, RULE_scanOperatorPartitionByClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1906);
			match(PARTITION);
			setState(1907);
			match(BY);
			setState(1908);
			((ScanOperatorPartitionByClauseContext)_localctx).unnamedExpression = unnamedExpression();
			((ScanOperatorPartitionByClauseContext)_localctx).Expressions.add(((ScanOperatorPartitionByClauseContext)_localctx).unnamedExpression);
			setState(1913);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1909);
				match(COMMA);
				setState(1910);
				((ScanOperatorPartitionByClauseContext)_localctx).unnamedExpression = unnamedExpression();
				((ScanOperatorPartitionByClauseContext)_localctx).Expressions.add(((ScanOperatorPartitionByClauseContext)_localctx).unnamedExpression);
				}
				}
				setState(1915);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorDeclareClauseContext extends ParserRuleContext {
		public ScalarParameterContext scalarParameter;
		public List<ScalarParameterContext> Parameters = new ArrayList<ScalarParameterContext>();
		public TerminalNode DECLARE() { return getToken(HqlParser.DECLARE, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<ScalarParameterContext> scalarParameter() {
			return getRuleContexts(ScalarParameterContext.class);
		}
		public ScalarParameterContext scalarParameter(int i) {
			return getRuleContext(ScalarParameterContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ScanOperatorDeclareClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorDeclareClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorDeclareClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorDeclareClause(this);
		}
	}

	public final ScanOperatorDeclareClauseContext scanOperatorDeclareClause() throws RecognitionException {
		ScanOperatorDeclareClauseContext _localctx = new ScanOperatorDeclareClauseContext(_ctx, getState());
		enterRule(_localctx, 310, RULE_scanOperatorDeclareClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1916);
			match(DECLARE);
			setState(1917);
			match(OPENPAREN);
			setState(1918);
			((ScanOperatorDeclareClauseContext)_localctx).scalarParameter = scalarParameter();
			((ScanOperatorDeclareClauseContext)_localctx).Parameters.add(((ScanOperatorDeclareClauseContext)_localctx).scalarParameter);
			setState(1923);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1919);
				match(COMMA);
				setState(1920);
				((ScanOperatorDeclareClauseContext)_localctx).scalarParameter = scalarParameter();
				((ScanOperatorDeclareClauseContext)_localctx).Parameters.add(((ScanOperatorDeclareClauseContext)_localctx).scalarParameter);
				}
				}
				setState(1925);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1926);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorStepContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public ScanOperatorStepOutputClauseContext OutputClause;
		public UnnamedExpressionContext Expression;
		public ScanOperatorBodyContext Body;
		public TerminalNode STEP() { return getToken(HqlParser.STEP, 0); }
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public TerminalNode SEMICOLON() { return getToken(HqlParser.SEMICOLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public TerminalNode OPTIONAL() { return getToken(HqlParser.OPTIONAL, 0); }
		public ScanOperatorStepOutputClauseContext scanOperatorStepOutputClause() {
			return getRuleContext(ScanOperatorStepOutputClauseContext.class,0);
		}
		public ScanOperatorBodyContext scanOperatorBody() {
			return getRuleContext(ScanOperatorBodyContext.class,0);
		}
		public ScanOperatorStepContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorStep; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorStep(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorStep(this);
		}
	}

	public final ScanOperatorStepContext scanOperatorStep() throws RecognitionException {
		ScanOperatorStepContext _localctx = new ScanOperatorStepContext(_ctx, getState());
		enterRule(_localctx, 312, RULE_scanOperatorStep);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1928);
			match(STEP);
			setState(1929);
			((ScanOperatorStepContext)_localctx).Name = parameterName();
			setState(1931);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OPTIONAL) {
				{
				setState(1930);
				match(OPTIONAL);
				}
			}

			setState(1934);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==OUTPUT) {
				{
				setState(1933);
				((ScanOperatorStepContext)_localctx).OutputClause = scanOperatorStepOutputClause();
				}
			}

			setState(1936);
			match(COLON);
			setState(1937);
			((ScanOperatorStepContext)_localctx).Expression = unnamedExpression();
			setState(1939);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==EQUAL_GREATERTHAN) {
				{
				setState(1938);
				((ScanOperatorStepContext)_localctx).Body = scanOperatorBody();
				}
			}

			setState(1941);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorStepOutputClauseContext extends ParserRuleContext {
		public Token OutputKind;
		public TerminalNode OUTPUT() { return getToken(HqlParser.OUTPUT, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode ALL() { return getToken(HqlParser.ALL, 0); }
		public TerminalNode LAST() { return getToken(HqlParser.LAST, 0); }
		public TerminalNode NONE() { return getToken(HqlParser.NONE, 0); }
		public ScanOperatorStepOutputClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorStepOutputClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorStepOutputClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorStepOutputClause(this);
		}
	}

	public final ScanOperatorStepOutputClauseContext scanOperatorStepOutputClause() throws RecognitionException {
		ScanOperatorStepOutputClauseContext _localctx = new ScanOperatorStepOutputClauseContext(_ctx, getState());
		enterRule(_localctx, 314, RULE_scanOperatorStepOutputClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1943);
			match(OUTPUT);
			setState(1944);
			match(EQUAL);
			setState(1945);
			((ScanOperatorStepOutputClauseContext)_localctx).OutputKind = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==ALL || _la==LAST || _la==NONE) ) {
				((ScanOperatorStepOutputClauseContext)_localctx).OutputKind = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorBodyContext extends ParserRuleContext {
		public ScanOperatorAssignmentContext scanOperatorAssignment;
		public List<ScanOperatorAssignmentContext> Assignments = new ArrayList<ScanOperatorAssignmentContext>();
		public TerminalNode EQUAL_GREATERTHAN() { return getToken(HqlParser.EQUAL_GREATERTHAN, 0); }
		public List<ScanOperatorAssignmentContext> scanOperatorAssignment() {
			return getRuleContexts(ScanOperatorAssignmentContext.class);
		}
		public ScanOperatorAssignmentContext scanOperatorAssignment(int i) {
			return getRuleContext(ScanOperatorAssignmentContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ScanOperatorBodyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorBody; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorBody(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorBody(this);
		}
	}

	public final ScanOperatorBodyContext scanOperatorBody() throws RecognitionException {
		ScanOperatorBodyContext _localctx = new ScanOperatorBodyContext(_ctx, getState());
		enterRule(_localctx, 316, RULE_scanOperatorBody);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1947);
			match(EQUAL_GREATERTHAN);
			setState(1948);
			((ScanOperatorBodyContext)_localctx).scanOperatorAssignment = scanOperatorAssignment();
			((ScanOperatorBodyContext)_localctx).Assignments.add(((ScanOperatorBodyContext)_localctx).scanOperatorAssignment);
			setState(1953);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1949);
				match(COMMA);
				setState(1950);
				((ScanOperatorBodyContext)_localctx).scanOperatorAssignment = scanOperatorAssignment();
				((ScanOperatorBodyContext)_localctx).Assignments.add(((ScanOperatorBodyContext)_localctx).scanOperatorAssignment);
				}
				}
				setState(1955);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScanOperatorAssignmentContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public UnnamedExpressionContext Expression;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public ScanOperatorAssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scanOperatorAssignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScanOperatorAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScanOperatorAssignment(this);
		}
	}

	public final ScanOperatorAssignmentContext scanOperatorAssignment() throws RecognitionException {
		ScanOperatorAssignmentContext _localctx = new ScanOperatorAssignmentContext(_ctx, getState());
		enterRule(_localctx, 318, RULE_scanOperatorAssignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1956);
			((ScanOperatorAssignmentContext)_localctx).Name = parameterName();
			setState(1957);
			match(EQUAL);
			setState(1958);
			((ScanOperatorAssignmentContext)_localctx).Expression = unnamedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SearchOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public DataScopeClauseContext DataScope;
		public SearchOperatorInClauseContext InClause;
		public UnnamedExpressionContext Expression;
		public StarExpressionContext Star;
		public SearchOperatorStarAndExpressionContext StarAndExpression;
		public TerminalNode SEARCH() { return getToken(HqlParser.SEARCH, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public StarExpressionContext starExpression() {
			return getRuleContext(StarExpressionContext.class,0);
		}
		public SearchOperatorStarAndExpressionContext searchOperatorStarAndExpression() {
			return getRuleContext(SearchOperatorStarAndExpressionContext.class,0);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public DataScopeClauseContext dataScopeClause() {
			return getRuleContext(DataScopeClauseContext.class,0);
		}
		public SearchOperatorInClauseContext searchOperatorInClause() {
			return getRuleContext(SearchOperatorInClauseContext.class,0);
		}
		public SearchOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_searchOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSearchOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSearchOperator(this);
		}
	}

	public final SearchOperatorContext searchOperator() throws RecognitionException {
		SearchOperatorContext _localctx = new SearchOperatorContext(_ctx, getState());
		enterRule(_localctx, 320, RULE_searchOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(1960);
			match(SEARCH);
			setState(1964);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,157,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(1961);
					((SearchOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((SearchOperatorContext)_localctx).Parameters.add(((SearchOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(1966);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,157,_ctx);
			}
			setState(1968);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DATASCOPE) {
				{
				setState(1967);
				((SearchOperatorContext)_localctx).DataScope = dataScopeClause();
				}
			}

			setState(1971);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==IN) {
				{
				setState(1970);
				((SearchOperatorContext)_localctx).InClause = searchOperatorInClause();
				}
			}

			setState(1976);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,160,_ctx) ) {
			case 1:
				{
				setState(1973);
				((SearchOperatorContext)_localctx).Expression = unnamedExpression();
				}
				break;
			case 2:
				{
				setState(1974);
				((SearchOperatorContext)_localctx).Star = starExpression();
				}
				break;
			case 3:
				{
				setState(1975);
				((SearchOperatorContext)_localctx).StarAndExpression = searchOperatorStarAndExpression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SearchOperatorStarAndExpressionContext extends ParserRuleContext {
		public UnnamedExpressionContext Expression;
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public TerminalNode AND() { return getToken(HqlParser.AND, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public SearchOperatorStarAndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_searchOperatorStarAndExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSearchOperatorStarAndExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSearchOperatorStarAndExpression(this);
		}
	}

	public final SearchOperatorStarAndExpressionContext searchOperatorStarAndExpression() throws RecognitionException {
		SearchOperatorStarAndExpressionContext _localctx = new SearchOperatorStarAndExpressionContext(_ctx, getState());
		enterRule(_localctx, 322, RULE_searchOperatorStarAndExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1978);
			match(ASTERISK);
			setState(1979);
			match(AND);
			setState(1980);
			((SearchOperatorStarAndExpressionContext)_localctx).Expression = unnamedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SearchOperatorInClauseContext extends ParserRuleContext {
		public FindOperatorSourceContext findOperatorSource;
		public List<FindOperatorSourceContext> Expressions = new ArrayList<FindOperatorSourceContext>();
		public TerminalNode IN() { return getToken(HqlParser.IN, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<FindOperatorSourceContext> findOperatorSource() {
			return getRuleContexts(FindOperatorSourceContext.class);
		}
		public FindOperatorSourceContext findOperatorSource(int i) {
			return getRuleContext(FindOperatorSourceContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public SearchOperatorInClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_searchOperatorInClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSearchOperatorInClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSearchOperatorInClause(this);
		}
	}

	public final SearchOperatorInClauseContext searchOperatorInClause() throws RecognitionException {
		SearchOperatorInClauseContext _localctx = new SearchOperatorInClauseContext(_ctx, getState());
		enterRule(_localctx, 324, RULE_searchOperatorInClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1982);
			match(IN);
			setState(1983);
			match(OPENPAREN);
			setState(1984);
			((SearchOperatorInClauseContext)_localctx).findOperatorSource = findOperatorSource();
			((SearchOperatorInClauseContext)_localctx).Expressions.add(((SearchOperatorInClauseContext)_localctx).findOperatorSource);
			setState(1989);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(1985);
				match(COMMA);
				setState(1986);
				((SearchOperatorInClauseContext)_localctx).findOperatorSource = findOperatorSource();
				((SearchOperatorInClauseContext)_localctx).Expressions.add(((SearchOperatorInClauseContext)_localctx).findOperatorSource);
				}
				}
				setState(1991);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(1992);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SerializeOperatorContext extends ParserRuleContext {
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public TerminalNode SERIALIZE() { return getToken(HqlParser.SERIALIZE, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public SerializeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_serializeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSerializeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSerializeOperator(this);
		}
	}

	public final SerializeOperatorContext serializeOperator() throws RecognitionException {
		SerializeOperatorContext _localctx = new SerializeOperatorContext(_ctx, getState());
		enterRule(_localctx, 326, RULE_serializeOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(1994);
			match(SERIALIZE);
			setState(1998);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(1995);
				((SerializeOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((SerializeOperatorContext)_localctx).Parameters.add(((SerializeOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(2000);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2001);
			((SerializeOperatorContext)_localctx).namedExpression = namedExpression();
			((SerializeOperatorContext)_localctx).Expressions.add(((SerializeOperatorContext)_localctx).namedExpression);
			setState(2006);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2002);
				match(COMMA);
				setState(2003);
				((SerializeOperatorContext)_localctx).namedExpression = namedExpression();
				((SerializeOperatorContext)_localctx).Expressions.add(((SerializeOperatorContext)_localctx).namedExpression);
				}
				}
				setState(2008);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SortOperatorContext extends ParserRuleContext {
		public Token Keyword;
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public OrderedExpressionContext orderedExpression;
		public List<OrderedExpressionContext> Expressions = new ArrayList<OrderedExpressionContext>();
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<OrderedExpressionContext> orderedExpression() {
			return getRuleContexts(OrderedExpressionContext.class);
		}
		public OrderedExpressionContext orderedExpression(int i) {
			return getRuleContext(OrderedExpressionContext.class,i);
		}
		public TerminalNode SORT() { return getToken(HqlParser.SORT, 0); }
		public TerminalNode ORDER() { return getToken(HqlParser.ORDER, 0); }
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public SortOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSortOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSortOperator(this);
		}
	}

	public final SortOperatorContext sortOperator() throws RecognitionException {
		SortOperatorContext _localctx = new SortOperatorContext(_ctx, getState());
		enterRule(_localctx, 328, RULE_sortOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2009);
			((SortOperatorContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==ORDER || _la==SORT) ) {
				((SortOperatorContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2013);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(2010);
				((SortOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((SortOperatorContext)_localctx).Parameters.add(((SortOperatorContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(2015);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2016);
			match(BY);
			setState(2017);
			((SortOperatorContext)_localctx).orderedExpression = orderedExpression();
			((SortOperatorContext)_localctx).Expressions.add(((SortOperatorContext)_localctx).orderedExpression);
			setState(2022);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2018);
				match(COMMA);
				setState(2019);
				((SortOperatorContext)_localctx).orderedExpression = orderedExpression();
				((SortOperatorContext)_localctx).Expressions.add(((SortOperatorContext)_localctx).orderedExpression);
				}
				}
				setState(2024);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OrderedExpressionContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public SortOrderingContext Ordering;
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public SortOrderingContext sortOrdering() {
			return getRuleContext(SortOrderingContext.class,0);
		}
		public OrderedExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_orderedExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterOrderedExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitOrderedExpression(this);
		}
	}

	public final OrderedExpressionContext orderedExpression() throws RecognitionException {
		OrderedExpressionContext _localctx = new OrderedExpressionContext(_ctx, getState());
		enterRule(_localctx, 330, RULE_orderedExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2025);
			((OrderedExpressionContext)_localctx).Expression = namedExpression();
			setState(2026);
			((OrderedExpressionContext)_localctx).Ordering = sortOrdering();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SortOrderingContext extends ParserRuleContext {
		public Token OrderKind;
		public Token NullsKind;
		public TerminalNode NULLS() { return getToken(HqlParser.NULLS, 0); }
		public TerminalNode ASC() { return getToken(HqlParser.ASC, 0); }
		public TerminalNode DESC() { return getToken(HqlParser.DESC, 0); }
		public TerminalNode FIRST() { return getToken(HqlParser.FIRST, 0); }
		public TerminalNode LAST() { return getToken(HqlParser.LAST, 0); }
		public SortOrderingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sortOrdering; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSortOrdering(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSortOrdering(this);
		}
	}

	public final SortOrderingContext sortOrdering() throws RecognitionException {
		SortOrderingContext _localctx = new SortOrderingContext(_ctx, getState());
		enterRule(_localctx, 332, RULE_sortOrdering);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2029);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASC || _la==DESC) {
				{
				setState(2028);
				((SortOrderingContext)_localctx).OrderKind = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==ASC || _la==DESC) ) {
					((SortOrderingContext)_localctx).OrderKind = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(2033);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==NULLS) {
				{
				setState(2031);
				match(NULLS);
				setState(2032);
				((SortOrderingContext)_localctx).NullsKind = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==FIRST || _la==LAST) ) {
					((SortOrderingContext)_localctx).NullsKind = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SummarizeOperatorContext extends ParserRuleContext {
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public SummarizeOperatorByClauseContext ByClause;
		public TerminalNode SUMMARIZE() { return getToken(HqlParser.SUMMARIZE, 0); }
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public SummarizeOperatorByClauseContext summarizeOperatorByClause() {
			return getRuleContext(SummarizeOperatorByClauseContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public SummarizeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_summarizeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSummarizeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSummarizeOperator(this);
		}
	}

	public final SummarizeOperatorContext summarizeOperator() throws RecognitionException {
		SummarizeOperatorContext _localctx = new SummarizeOperatorContext(_ctx, getState());
		enterRule(_localctx, 334, RULE_summarizeOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2035);
			match(SUMMARIZE);
			setState(2039);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(2036);
				((SummarizeOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((SummarizeOperatorContext)_localctx).Parameters.add(((SummarizeOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(2041);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2050);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,170,_ctx) ) {
			case 1:
				{
				setState(2042);
				((SummarizeOperatorContext)_localctx).namedExpression = namedExpression();
				((SummarizeOperatorContext)_localctx).Expressions.add(((SummarizeOperatorContext)_localctx).namedExpression);
				setState(2047);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(2043);
					match(COMMA);
					setState(2044);
					((SummarizeOperatorContext)_localctx).namedExpression = namedExpression();
					((SummarizeOperatorContext)_localctx).Expressions.add(((SummarizeOperatorContext)_localctx).namedExpression);
					}
					}
					setState(2049);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
				break;
			}
			setState(2053);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BY) {
				{
				setState(2052);
				((SummarizeOperatorContext)_localctx).ByClause = summarizeOperatorByClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SummarizeOperatorByClauseContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression;
		public List<NamedExpressionContext> Expressions = new ArrayList<NamedExpressionContext>();
		public SummarizeOperatorLegacyBinClauseContext BinClause;
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(HqlParser.COMMA, 0); }
		public SummarizeOperatorLegacyBinClauseContext summarizeOperatorLegacyBinClause() {
			return getRuleContext(SummarizeOperatorLegacyBinClauseContext.class,0);
		}
		public SummarizeOperatorByClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_summarizeOperatorByClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSummarizeOperatorByClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSummarizeOperatorByClause(this);
		}
	}

	public final SummarizeOperatorByClauseContext summarizeOperatorByClause() throws RecognitionException {
		SummarizeOperatorByClauseContext _localctx = new SummarizeOperatorByClauseContext(_ctx, getState());
		enterRule(_localctx, 336, RULE_summarizeOperatorByClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2055);
			match(BY);
			setState(2056);
			((SummarizeOperatorByClauseContext)_localctx).namedExpression = namedExpression();
			((SummarizeOperatorByClauseContext)_localctx).Expressions.add(((SummarizeOperatorByClauseContext)_localctx).namedExpression);
			{
			setState(2057);
			match(COMMA);
			setState(2058);
			((SummarizeOperatorByClauseContext)_localctx).namedExpression = namedExpression();
			((SummarizeOperatorByClauseContext)_localctx).Expressions.add(((SummarizeOperatorByClauseContext)_localctx).namedExpression);
			}
			setState(2061);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BIN) {
				{
				setState(2060);
				((SummarizeOperatorByClauseContext)_localctx).BinClause = summarizeOperatorLegacyBinClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SummarizeOperatorLegacyBinClauseContext extends ParserRuleContext {
		public NumberLikeLiteralExpressionContext Expression;
		public TerminalNode BIN() { return getToken(HqlParser.BIN, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public NumberLikeLiteralExpressionContext numberLikeLiteralExpression() {
			return getRuleContext(NumberLikeLiteralExpressionContext.class,0);
		}
		public SummarizeOperatorLegacyBinClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_summarizeOperatorLegacyBinClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSummarizeOperatorLegacyBinClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSummarizeOperatorLegacyBinClause(this);
		}
	}

	public final SummarizeOperatorLegacyBinClauseContext summarizeOperatorLegacyBinClause() throws RecognitionException {
		SummarizeOperatorLegacyBinClauseContext _localctx = new SummarizeOperatorLegacyBinClauseContext(_ctx, getState());
		enterRule(_localctx, 338, RULE_summarizeOperatorLegacyBinClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2063);
			match(BIN);
			setState(2064);
			match(EQUAL);
			setState(2065);
			((SummarizeOperatorLegacyBinClauseContext)_localctx).Expression = numberLikeLiteralExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TakeOperatorContext extends ParserRuleContext {
		public Token Keyword;
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext Expression;
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public TerminalNode LIMIT() { return getToken(HqlParser.LIMIT, 0); }
		public TerminalNode TAKE() { return getToken(HqlParser.TAKE, 0); }
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public TakeOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_takeOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTakeOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTakeOperator(this);
		}
	}

	public final TakeOperatorContext takeOperator() throws RecognitionException {
		TakeOperatorContext _localctx = new TakeOperatorContext(_ctx, getState());
		enterRule(_localctx, 340, RULE_takeOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2067);
			((TakeOperatorContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==LIMIT || _la==TAKE) ) {
				((TakeOperatorContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2071);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(2068);
				((TakeOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((TakeOperatorContext)_localctx).Parameters.add(((TakeOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(2073);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2074);
			((TakeOperatorContext)_localctx).Expression = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopOperatorContext extends ParserRuleContext {
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext Expression;
		public OrderedExpressionContext ByExpression;
		public TerminalNode TOP() { return getToken(HqlParser.TOP, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public OrderedExpressionContext orderedExpression() {
			return getRuleContext(OrderedExpressionContext.class,0);
		}
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public TopOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTopOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTopOperator(this);
		}
	}

	public final TopOperatorContext topOperator() throws RecognitionException {
		TopOperatorContext _localctx = new TopOperatorContext(_ctx, getState());
		enterRule(_localctx, 342, RULE_topOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2076);
			match(TOP);
			setState(2080);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(2077);
				((TopOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((TopOperatorContext)_localctx).Parameters.add(((TopOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(2082);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2083);
			((TopOperatorContext)_localctx).Expression = namedExpression();
			setState(2084);
			match(BY);
			setState(2085);
			((TopOperatorContext)_localctx).ByExpression = orderedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopHittersOperatorContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public NamedExpressionContext OfExpression;
		public TopHittersOperatorByClauseContext ByClause;
		public TerminalNode TOP_HITTERS() { return getToken(HqlParser.TOP_HITTERS, 0); }
		public TerminalNode OF() { return getToken(HqlParser.OF, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public TopHittersOperatorByClauseContext topHittersOperatorByClause() {
			return getRuleContext(TopHittersOperatorByClauseContext.class,0);
		}
		public TopHittersOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topHittersOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTopHittersOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTopHittersOperator(this);
		}
	}

	public final TopHittersOperatorContext topHittersOperator() throws RecognitionException {
		TopHittersOperatorContext _localctx = new TopHittersOperatorContext(_ctx, getState());
		enterRule(_localctx, 344, RULE_topHittersOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2087);
			match(TOP_HITTERS);
			setState(2088);
			((TopHittersOperatorContext)_localctx).Expression = namedExpression();
			setState(2089);
			match(OF);
			setState(2090);
			((TopHittersOperatorContext)_localctx).OfExpression = namedExpression();
			setState(2092);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==BY) {
				{
				setState(2091);
				((TopHittersOperatorContext)_localctx).ByClause = topHittersOperatorByClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopHittersOperatorByClauseContext extends ParserRuleContext {
		public OrderedExpressionContext ByExpression;
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public OrderedExpressionContext orderedExpression() {
			return getRuleContext(OrderedExpressionContext.class,0);
		}
		public TopHittersOperatorByClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topHittersOperatorByClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTopHittersOperatorByClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTopHittersOperatorByClause(this);
		}
	}

	public final TopHittersOperatorByClauseContext topHittersOperatorByClause() throws RecognitionException {
		TopHittersOperatorByClauseContext _localctx = new TopHittersOperatorByClauseContext(_ctx, getState());
		enterRule(_localctx, 346, RULE_topHittersOperatorByClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2094);
			match(BY);
			setState(2095);
			((TopHittersOperatorByClauseContext)_localctx).ByExpression = orderedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopNestedOperatorContext extends ParserRuleContext {
		public TopNestedOperatorPartContext topNestedOperatorPart;
		public List<TopNestedOperatorPartContext> Segments = new ArrayList<TopNestedOperatorPartContext>();
		public List<TopNestedOperatorPartContext> topNestedOperatorPart() {
			return getRuleContexts(TopNestedOperatorPartContext.class);
		}
		public TopNestedOperatorPartContext topNestedOperatorPart(int i) {
			return getRuleContext(TopNestedOperatorPartContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public TopNestedOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topNestedOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTopNestedOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTopNestedOperator(this);
		}
	}

	public final TopNestedOperatorContext topNestedOperator() throws RecognitionException {
		TopNestedOperatorContext _localctx = new TopNestedOperatorContext(_ctx, getState());
		enterRule(_localctx, 348, RULE_topNestedOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2097);
			((TopNestedOperatorContext)_localctx).topNestedOperatorPart = topNestedOperatorPart();
			((TopNestedOperatorContext)_localctx).Segments.add(((TopNestedOperatorContext)_localctx).topNestedOperatorPart);
			setState(2102);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2098);
				match(COMMA);
				setState(2099);
				((TopNestedOperatorContext)_localctx).topNestedOperatorPart = topNestedOperatorPart();
				((TopNestedOperatorContext)_localctx).Segments.add(((TopNestedOperatorContext)_localctx).topNestedOperatorPart);
				}
				}
				setState(2104);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopNestedOperatorPartContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public NamedExpressionContext OfExpression;
		public TopNestedOperatorWithOthersClauseContext WithOthers;
		public OrderedExpressionContext ByExpression;
		public TerminalNode TOP_NESTED() { return getToken(HqlParser.TOP_NESTED, 0); }
		public TerminalNode OF() { return getToken(HqlParser.OF, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public List<NamedExpressionContext> namedExpression() {
			return getRuleContexts(NamedExpressionContext.class);
		}
		public NamedExpressionContext namedExpression(int i) {
			return getRuleContext(NamedExpressionContext.class,i);
		}
		public OrderedExpressionContext orderedExpression() {
			return getRuleContext(OrderedExpressionContext.class,0);
		}
		public TopNestedOperatorWithOthersClauseContext topNestedOperatorWithOthersClause() {
			return getRuleContext(TopNestedOperatorWithOthersClauseContext.class,0);
		}
		public TopNestedOperatorPartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topNestedOperatorPart; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTopNestedOperatorPart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTopNestedOperatorPart(this);
		}
	}

	public final TopNestedOperatorPartContext topNestedOperatorPart() throws RecognitionException {
		TopNestedOperatorPartContext _localctx = new TopNestedOperatorPartContext(_ctx, getState());
		enterRule(_localctx, 350, RULE_topNestedOperatorPart);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2105);
			match(TOP_NESTED);
			setState(2107);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,177,_ctx) ) {
			case 1:
				{
				setState(2106);
				((TopNestedOperatorPartContext)_localctx).Expression = namedExpression();
				}
				break;
			}
			setState(2109);
			match(OF);
			setState(2110);
			((TopNestedOperatorPartContext)_localctx).OfExpression = namedExpression();
			setState(2112);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==WITH) {
				{
				setState(2111);
				((TopNestedOperatorPartContext)_localctx).WithOthers = topNestedOperatorWithOthersClause();
				}
			}

			setState(2114);
			match(BY);
			setState(2115);
			((TopNestedOperatorPartContext)_localctx).ByExpression = orderedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TopNestedOperatorWithOthersClauseContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode OTHERS() { return getToken(HqlParser.OTHERS, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public TopNestedOperatorWithOthersClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_topNestedOperatorWithOthersClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTopNestedOperatorWithOthersClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTopNestedOperatorWithOthersClause(this);
		}
	}

	public final TopNestedOperatorWithOthersClauseContext topNestedOperatorWithOthersClause() throws RecognitionException {
		TopNestedOperatorWithOthersClauseContext _localctx = new TopNestedOperatorWithOthersClauseContext(_ctx, getState());
		enterRule(_localctx, 352, RULE_topNestedOperatorWithOthersClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2117);
			match(WITH);
			setState(2118);
			match(OTHERS);
			setState(2119);
			match(EQUAL);
			setState(2120);
			((TopNestedOperatorWithOthersClauseContext)_localctx).Expression = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnionOperatorContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public UnionOperatorExpressionContext unionOperatorExpression;
		public List<UnionOperatorExpressionContext> Expressions = new ArrayList<UnionOperatorExpressionContext>();
		public TerminalNode UNION() { return getToken(HqlParser.UNION, 0); }
		public List<UnionOperatorExpressionContext> unionOperatorExpression() {
			return getRuleContexts(UnionOperatorExpressionContext.class);
		}
		public UnionOperatorExpressionContext unionOperatorExpression(int i) {
			return getRuleContext(UnionOperatorExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public UnionOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unionOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterUnionOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitUnionOperator(this);
		}
	}

	public final UnionOperatorContext unionOperator() throws RecognitionException {
		UnionOperatorContext _localctx = new UnionOperatorContext(_ctx, getState());
		enterRule(_localctx, 354, RULE_unionOperator);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2122);
			match(UNION);
			setState(2126);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,179,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2123);
					((UnionOperatorContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
					((UnionOperatorContext)_localctx).Parameters.add(((UnionOperatorContext)_localctx).relaxedQueryOperatorParameter);
					}
					} 
				}
				setState(2128);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,179,_ctx);
			}
			setState(2129);
			((UnionOperatorContext)_localctx).unionOperatorExpression = unionOperatorExpression();
			((UnionOperatorContext)_localctx).Expressions.add(((UnionOperatorContext)_localctx).unionOperatorExpression);
			setState(2134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2130);
				match(COMMA);
				setState(2131);
				((UnionOperatorContext)_localctx).unionOperatorExpression = unionOperatorExpression();
				((UnionOperatorContext)_localctx).Expressions.add(((UnionOperatorContext)_localctx).unionOperatorExpression);
				}
				}
				setState(2136);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnionOperatorExpressionContext extends ParserRuleContext {
		public WildcardedEntityExpressionContext wildcardedEntityExpression() {
			return getRuleContext(WildcardedEntityExpressionContext.class,0);
		}
		public EntityNameReferenceContext entityNameReference() {
			return getRuleContext(EntityNameReferenceContext.class,0);
		}
		public ParenthesizedExpressionContext parenthesizedExpression() {
			return getRuleContext(ParenthesizedExpressionContext.class,0);
		}
		public UnionOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unionOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterUnionOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitUnionOperatorExpression(this);
		}
	}

	public final UnionOperatorExpressionContext unionOperatorExpression() throws RecognitionException {
		UnionOperatorExpressionContext _localctx = new UnionOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 356, RULE_unionOperatorExpression);
		try {
			setState(2140);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,181,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2137);
				wildcardedEntityExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2138);
				entityNameReference();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2139);
				parenthesizedExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhereOperatorContext extends ParserRuleContext {
		public Token Keyword;
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter;
		public List<StrictQueryOperatorParameterContext> Parameters = new ArrayList<StrictQueryOperatorParameterContext>();
		public NamedExpressionContext Predicate;
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public TerminalNode FILTER() { return getToken(HqlParser.FILTER, 0); }
		public TerminalNode WHERE() { return getToken(HqlParser.WHERE, 0); }
		public List<StrictQueryOperatorParameterContext> strictQueryOperatorParameter() {
			return getRuleContexts(StrictQueryOperatorParameterContext.class);
		}
		public StrictQueryOperatorParameterContext strictQueryOperatorParameter(int i) {
			return getRuleContext(StrictQueryOperatorParameterContext.class,i);
		}
		public WhereOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whereOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWhereOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWhereOperator(this);
		}
	}

	public final WhereOperatorContext whereOperator() throws RecognitionException {
		WhereOperatorContext _localctx = new WhereOperatorContext(_ctx, getState());
		enterRule(_localctx, 358, RULE_whereOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2142);
			((WhereOperatorContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==FILTER || _la==WHERE) ) {
				((WhereOperatorContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2146);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) {
				{
				{
				setState(2143);
				((WhereOperatorContext)_localctx).strictQueryOperatorParameter = strictQueryOperatorParameter();
				((WhereOperatorContext)_localctx).Parameters.add(((WhereOperatorContext)_localctx).strictQueryOperatorParameter);
				}
				}
				setState(2148);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2149);
			((WhereOperatorContext)_localctx).Predicate = namedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContextualSubExpressionContext extends ParserRuleContext {
		public PipeSubExpressionContext pipeSubExpression() {
			return getRuleContext(PipeSubExpressionContext.class,0);
		}
		public ContextualPipeExpressionContext contextualPipeExpression() {
			return getRuleContext(ContextualPipeExpressionContext.class,0);
		}
		public ContextualSubExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contextualSubExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterContextualSubExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitContextualSubExpression(this);
		}
	}

	public final ContextualSubExpressionContext contextualSubExpression() throws RecognitionException {
		ContextualSubExpressionContext _localctx = new ContextualSubExpressionContext(_ctx, getState());
		enterRule(_localctx, 360, RULE_contextualSubExpression);
		try {
			setState(2153);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case AS:
			case ASSERTSCHEMA:
			case CONSUME:
			case COUNT:
			case DISTINCT:
			case EVALUATE:
			case EXECUTE_AND_CACHE:
			case EXTEND:
			case FACET:
			case FILTER:
			case FIND:
			case FORK:
			case GETSCHEMA:
			case GRAPHMARKCOMPONENTS:
			case GRAPHMATCH:
			case GRAPHMERGE:
			case GRAPHSHORTESTPATHS:
			case GRAPHTOTABLE:
			case INVOKE:
			case JOIN:
			case LIMIT:
			case LOOKUP:
			case MAKEGRAPH:
			case MAKESERIES:
			case MV_APPLY:
			case MV_EXPAND:
			case MVAPPLY:
			case MVEXPAND:
			case ORDER:
			case PARSE:
			case PARSEKV:
			case PARSEWHERE:
			case PARTITION:
			case PARTITIONBY:
			case PROJECT:
			case PROJECTAWAY:
			case PROJECTKEEP:
			case PROJECTRENAME:
			case PROJECTREORDER:
			case REDUCE:
			case RENDER:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SORT:
			case SUMMARIZE:
			case TAKE:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case UNION:
			case WHERE:
				enterOuterAlt(_localctx, 1);
				{
				setState(2151);
				pipeSubExpression();
				}
				break;
			case CONTEXTUAL_DATATABLE:
				enterOuterAlt(_localctx, 2);
				{
				setState(2152);
				contextualPipeExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContextualPipeExpressionContext extends ParserRuleContext {
		public ContextualDataTableExpressionContext Expression;
		public ContextualPipeExpressionPipedOperatorContext contextualPipeExpressionPipedOperator;
		public List<ContextualPipeExpressionPipedOperatorContext> PipedOperators = new ArrayList<ContextualPipeExpressionPipedOperatorContext>();
		public ContextualDataTableExpressionContext contextualDataTableExpression() {
			return getRuleContext(ContextualDataTableExpressionContext.class,0);
		}
		public List<ContextualPipeExpressionPipedOperatorContext> contextualPipeExpressionPipedOperator() {
			return getRuleContexts(ContextualPipeExpressionPipedOperatorContext.class);
		}
		public ContextualPipeExpressionPipedOperatorContext contextualPipeExpressionPipedOperator(int i) {
			return getRuleContext(ContextualPipeExpressionPipedOperatorContext.class,i);
		}
		public ContextualPipeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contextualPipeExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterContextualPipeExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitContextualPipeExpression(this);
		}
	}

	public final ContextualPipeExpressionContext contextualPipeExpression() throws RecognitionException {
		ContextualPipeExpressionContext _localctx = new ContextualPipeExpressionContext(_ctx, getState());
		enterRule(_localctx, 362, RULE_contextualPipeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2155);
			((ContextualPipeExpressionContext)_localctx).Expression = contextualDataTableExpression();
			setState(2159);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==BAR) {
				{
				{
				setState(2156);
				((ContextualPipeExpressionContext)_localctx).contextualPipeExpressionPipedOperator = contextualPipeExpressionPipedOperator();
				((ContextualPipeExpressionContext)_localctx).PipedOperators.add(((ContextualPipeExpressionContext)_localctx).contextualPipeExpressionPipedOperator);
				}
				}
				setState(2161);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContextualPipeExpressionPipedOperatorContext extends ParserRuleContext {
		public AfterPipeOperatorContext Operator;
		public TerminalNode BAR() { return getToken(HqlParser.BAR, 0); }
		public AfterPipeOperatorContext afterPipeOperator() {
			return getRuleContext(AfterPipeOperatorContext.class,0);
		}
		public ContextualPipeExpressionPipedOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contextualPipeExpressionPipedOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterContextualPipeExpressionPipedOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitContextualPipeExpressionPipedOperator(this);
		}
	}

	public final ContextualPipeExpressionPipedOperatorContext contextualPipeExpressionPipedOperator() throws RecognitionException {
		ContextualPipeExpressionPipedOperatorContext _localctx = new ContextualPipeExpressionPipedOperatorContext(_ctx, getState());
		enterRule(_localctx, 364, RULE_contextualPipeExpressionPipedOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2162);
			match(BAR);
			setState(2163);
			((ContextualPipeExpressionPipedOperatorContext)_localctx).Operator = afterPipeOperator();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StrictQueryOperatorParameterContext extends ParserRuleContext {
		public Token NameToken;
		public IdentifierOrKeywordNameContext NameValue;
		public LiteralExpressionContext LiteralValue;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode BAGEXPANSION() { return getToken(HqlParser.BAGEXPANSION, 0); }
		public TerminalNode BIN_LEGACY() { return getToken(HqlParser.BIN_LEGACY, 0); }
		public TerminalNode CROSSCLUSTER__() { return getToken(HqlParser.CROSSCLUSTER__, 0); }
		public TerminalNode CROSSDB__() { return getToken(HqlParser.CROSSDB__, 0); }
		public TerminalNode DECODEBLOCKS() { return getToken(HqlParser.DECODEBLOCKS, 0); }
		public TerminalNode EXPANDOUTPUT() { return getToken(HqlParser.EXPANDOUTPUT, 0); }
		public TerminalNode HINT_CONCURRENCY() { return getToken(HqlParser.HINT_CONCURRENCY, 0); }
		public TerminalNode HINT_DISTRIBUTION() { return getToken(HqlParser.HINT_DISTRIBUTION, 0); }
		public TerminalNode HINT_MATERIALIZED() { return getToken(HqlParser.HINT_MATERIALIZED, 0); }
		public TerminalNode HINT_NUM_PARTITIONS() { return getToken(HqlParser.HINT_NUM_PARTITIONS, 0); }
		public TerminalNode HINT_PASS_FILTERS() { return getToken(HqlParser.HINT_PASS_FILTERS, 0); }
		public TerminalNode HINT_PASS_FILTERS_COLUMN() { return getToken(HqlParser.HINT_PASS_FILTERS_COLUMN, 0); }
		public TerminalNode HINT_PROGRESSIVE_TOP() { return getToken(HqlParser.HINT_PROGRESSIVE_TOP, 0); }
		public TerminalNode HINT_REMOTE() { return getToken(HqlParser.HINT_REMOTE, 0); }
		public TerminalNode HINT_SUFFLEKEY() { return getToken(HqlParser.HINT_SUFFLEKEY, 0); }
		public TerminalNode HINT_SPREAD() { return getToken(HqlParser.HINT_SPREAD, 0); }
		public TerminalNode HINT_STRATEGY() { return getToken(HqlParser.HINT_STRATEGY, 0); }
		public TerminalNode ISFUZZY() { return getToken(HqlParser.ISFUZZY, 0); }
		public TerminalNode ISFUZZY__() { return getToken(HqlParser.ISFUZZY__, 0); }
		public TerminalNode ID__() { return getToken(HqlParser.ID__, 0); }
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode PACKEDCOLUMN__() { return getToken(HqlParser.PACKEDCOLUMN__, 0); }
		public TerminalNode SOURCECOLUMNINDEX__() { return getToken(HqlParser.SOURCECOLUMNINDEX__, 0); }
		public TerminalNode WITH_ITEM_INDEX() { return getToken(HqlParser.WITH_ITEM_INDEX, 0); }
		public TerminalNode WITH_MATCH_ID() { return getToken(HqlParser.WITH_MATCH_ID, 0); }
		public TerminalNode WITH_STEP_NAME() { return getToken(HqlParser.WITH_STEP_NAME, 0); }
		public TerminalNode WITHSOURCE() { return getToken(HqlParser.WITHSOURCE, 0); }
		public TerminalNode WITH_SOURCE() { return getToken(HqlParser.WITH_SOURCE, 0); }
		public TerminalNode WITHNOSOURCE__() { return getToken(HqlParser.WITHNOSOURCE__, 0); }
		public IdentifierOrKeywordNameContext identifierOrKeywordName() {
			return getRuleContext(IdentifierOrKeywordNameContext.class,0);
		}
		public LiteralExpressionContext literalExpression() {
			return getRuleContext(LiteralExpressionContext.class,0);
		}
		public StrictQueryOperatorParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_strictQueryOperatorParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStrictQueryOperatorParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStrictQueryOperatorParameter(this);
		}
	}

	public final StrictQueryOperatorParameterContext strictQueryOperatorParameter() throws RecognitionException {
		StrictQueryOperatorParameterContext _localctx = new StrictQueryOperatorParameterContext(_ctx, getState());
		enterRule(_localctx, 366, RULE_strictQueryOperatorParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2165);
			((StrictQueryOperatorParameterContext)_localctx).NameToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || _la==WITH_SOURCE || _la==WITH_STEP_NAME) ) {
				((StrictQueryOperatorParameterContext)_localctx).NameToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2166);
			match(EQUAL);
			setState(2169);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(2167);
				((StrictQueryOperatorParameterContext)_localctx).NameValue = identifierOrKeywordName();
				}
				break;
			case DASH:
			case PLUS:
			case DYNAMIC:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
				{
				setState(2168);
				((StrictQueryOperatorParameterContext)_localctx).LiteralValue = literalExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelaxedQueryOperatorParameterContext extends ParserRuleContext {
		public Token NameToken;
		public IdentifierOrKeywordNameContext NameValue;
		public LiteralExpressionContext LiteralValue;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public TerminalNode BAGEXPANSION() { return getToken(HqlParser.BAGEXPANSION, 0); }
		public TerminalNode BIN_LEGACY() { return getToken(HqlParser.BIN_LEGACY, 0); }
		public TerminalNode CROSSCLUSTER__() { return getToken(HqlParser.CROSSCLUSTER__, 0); }
		public TerminalNode CROSSDB__() { return getToken(HqlParser.CROSSDB__, 0); }
		public TerminalNode DECODEBLOCKS() { return getToken(HqlParser.DECODEBLOCKS, 0); }
		public TerminalNode EXPANDOUTPUT() { return getToken(HqlParser.EXPANDOUTPUT, 0); }
		public TerminalNode HINT_CONCURRENCY() { return getToken(HqlParser.HINT_CONCURRENCY, 0); }
		public TerminalNode HINT_DISTRIBUTION() { return getToken(HqlParser.HINT_DISTRIBUTION, 0); }
		public TerminalNode HINT_MATERIALIZED() { return getToken(HqlParser.HINT_MATERIALIZED, 0); }
		public TerminalNode HINT_NUM_PARTITIONS() { return getToken(HqlParser.HINT_NUM_PARTITIONS, 0); }
		public TerminalNode HINT_PASS_FILTERS() { return getToken(HqlParser.HINT_PASS_FILTERS, 0); }
		public TerminalNode HINT_PASS_FILTERS_COLUMN() { return getToken(HqlParser.HINT_PASS_FILTERS_COLUMN, 0); }
		public TerminalNode HINT_PROGRESSIVE_TOP() { return getToken(HqlParser.HINT_PROGRESSIVE_TOP, 0); }
		public TerminalNode HINT_REMOTE() { return getToken(HqlParser.HINT_REMOTE, 0); }
		public TerminalNode HINT_SUFFLEKEY() { return getToken(HqlParser.HINT_SUFFLEKEY, 0); }
		public TerminalNode HINT_SPREAD() { return getToken(HqlParser.HINT_SPREAD, 0); }
		public TerminalNode HINT_STRATEGY() { return getToken(HqlParser.HINT_STRATEGY, 0); }
		public TerminalNode ISFUZZY() { return getToken(HqlParser.ISFUZZY, 0); }
		public TerminalNode ISFUZZY__() { return getToken(HqlParser.ISFUZZY__, 0); }
		public TerminalNode ID__() { return getToken(HqlParser.ID__, 0); }
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode PACKEDCOLUMN__() { return getToken(HqlParser.PACKEDCOLUMN__, 0); }
		public TerminalNode SOURCECOLUMNINDEX__() { return getToken(HqlParser.SOURCECOLUMNINDEX__, 0); }
		public TerminalNode WITH_ITEM_INDEX() { return getToken(HqlParser.WITH_ITEM_INDEX, 0); }
		public TerminalNode WITH_MATCH_ID() { return getToken(HqlParser.WITH_MATCH_ID, 0); }
		public TerminalNode WITH_STEP_NAME() { return getToken(HqlParser.WITH_STEP_NAME, 0); }
		public TerminalNode WITHSOURCE() { return getToken(HqlParser.WITHSOURCE, 0); }
		public TerminalNode WITH_SOURCE() { return getToken(HqlParser.WITH_SOURCE, 0); }
		public TerminalNode WITHNOSOURCE__() { return getToken(HqlParser.WITHNOSOURCE__, 0); }
		public IdentifierOrKeywordNameContext identifierOrKeywordName() {
			return getRuleContext(IdentifierOrKeywordNameContext.class,0);
		}
		public LiteralExpressionContext literalExpression() {
			return getRuleContext(LiteralExpressionContext.class,0);
		}
		public RelaxedQueryOperatorParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relaxedQueryOperatorParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRelaxedQueryOperatorParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRelaxedQueryOperatorParameter(this);
		}
	}

	public final RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter() throws RecognitionException {
		RelaxedQueryOperatorParameterContext _localctx = new RelaxedQueryOperatorParameterContext(_ctx, getState());
		enterRule(_localctx, 368, RULE_relaxedQueryOperatorParameter);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2171);
			((RelaxedQueryOperatorParameterContext)_localctx).NameToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) ) {
				((RelaxedQueryOperatorParameterContext)_localctx).NameToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2172);
			match(EQUAL);
			setState(2175);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(2173);
				((RelaxedQueryOperatorParameterContext)_localctx).NameValue = identifierOrKeywordName();
				}
				break;
			case DASH:
			case PLUS:
			case DYNAMIC:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
				{
				setState(2174);
				((RelaxedQueryOperatorParameterContext)_localctx).LiteralValue = literalExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class QueryOperatorPropertyContext extends ParserRuleContext {
		public Token Name;
		public IdentifierOrKeywordNameContext NameValue;
		public LiteralExpressionContext LiteralValue;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public IdentifierOrKeywordNameContext identifierOrKeywordName() {
			return getRuleContext(IdentifierOrKeywordNameContext.class,0);
		}
		public LiteralExpressionContext literalExpression() {
			return getRuleContext(LiteralExpressionContext.class,0);
		}
		public QueryOperatorPropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_queryOperatorProperty; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterQueryOperatorProperty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitQueryOperatorProperty(this);
		}
	}

	public final QueryOperatorPropertyContext queryOperatorProperty() throws RecognitionException {
		QueryOperatorPropertyContext _localctx = new QueryOperatorPropertyContext(_ctx, getState());
		enterRule(_localctx, 370, RULE_queryOperatorProperty);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2177);
			((QueryOperatorPropertyContext)_localctx).Name = match(IDENTIFIER);
			setState(2178);
			match(EQUAL);
			setState(2181);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(2179);
				((QueryOperatorPropertyContext)_localctx).NameValue = identifierOrKeywordName();
				}
				break;
			case DASH:
			case PLUS:
			case DYNAMIC:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
				{
				setState(2180);
				((QueryOperatorPropertyContext)_localctx).LiteralValue = literalExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NamedExpressionContext extends ParserRuleContext {
		public NamedExpressionNameClauseContext Name;
		public UnnamedExpressionContext Expression;
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public NamedExpressionNameClauseContext namedExpressionNameClause() {
			return getRuleContext(NamedExpressionNameClauseContext.class,0);
		}
		public NamedExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_namedExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNamedExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNamedExpression(this);
		}
	}

	public final NamedExpressionContext namedExpression() throws RecognitionException {
		NamedExpressionContext _localctx = new NamedExpressionContext(_ctx, getState());
		enterRule(_localctx, 372, RULE_namedExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2184);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,188,_ctx) ) {
			case 1:
				{
				setState(2183);
				((NamedExpressionContext)_localctx).Name = namedExpressionNameClause();
				}
				break;
			}
			setState(2186);
			((NamedExpressionContext)_localctx).Expression = unnamedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NamedExpressionNameClauseContext extends ParserRuleContext {
		public IdentifierOrExtendedKeywordOrEscapedNameContext Name;
		public NamedExpressionNameListContext NameList;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrExtendedKeywordOrEscapedNameContext.class,0);
		}
		public NamedExpressionNameListContext namedExpressionNameList() {
			return getRuleContext(NamedExpressionNameListContext.class,0);
		}
		public NamedExpressionNameClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_namedExpressionNameClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNamedExpressionNameClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNamedExpressionNameClause(this);
		}
	}

	public final NamedExpressionNameClauseContext namedExpressionNameClause() throws RecognitionException {
		NamedExpressionNameClauseContext _localctx = new NamedExpressionNameClauseContext(_ctx, getState());
		enterRule(_localctx, 374, RULE_namedExpressionNameClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2190);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPENBRACKET:
			case ACCESS:
			case ACCUMULATE:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AS:
			case AXES:
			case BASE:
			case BIN:
			case BY:
			case CLUSTER:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATABASE:
			case DATATABLE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case DISTINCT:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case EXTEND:
			case EXTERNALDATA:
			case FACET:
			case FILTER:
			case FIND:
			case FORK:
			case FROM:
			case HAS:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case IN:
			case INTO:
			case INVOKE:
			case LEGEND:
			case LET:
			case LIMIT:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case MATERIALIZE:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case OF:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARSE:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case PRINT:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SERIES:
			case SET:
			case SORT:
			case STACKED:
			case STACKED100:
			case STEP:
			case SUMMARIZE:
			case TAKE:
			case THRESHOLD:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WHERE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(2188);
				((NamedExpressionNameClauseContext)_localctx).Name = identifierOrExtendedKeywordOrEscapedName();
				}
				break;
			case OPENPAREN:
				{
				setState(2189);
				((NamedExpressionNameClauseContext)_localctx).NameList = namedExpressionNameList();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(2192);
			match(EQUAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NamedExpressionNameListContext extends ParserRuleContext {
		public IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName;
		public List<IdentifierOrExtendedKeywordOrEscapedNameContext> Names = new ArrayList<IdentifierOrExtendedKeywordOrEscapedNameContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<IdentifierOrExtendedKeywordOrEscapedNameContext> identifierOrExtendedKeywordOrEscapedName() {
			return getRuleContexts(IdentifierOrExtendedKeywordOrEscapedNameContext.class);
		}
		public IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName(int i) {
			return getRuleContext(IdentifierOrExtendedKeywordOrEscapedNameContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public NamedExpressionNameListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_namedExpressionNameList; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNamedExpressionNameList(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNamedExpressionNameList(this);
		}
	}

	public final NamedExpressionNameListContext namedExpressionNameList() throws RecognitionException {
		NamedExpressionNameListContext _localctx = new NamedExpressionNameListContext(_ctx, getState());
		enterRule(_localctx, 376, RULE_namedExpressionNameList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2194);
			match(OPENPAREN);
			setState(2195);
			((NamedExpressionNameListContext)_localctx).identifierOrExtendedKeywordOrEscapedName = identifierOrExtendedKeywordOrEscapedName();
			((NamedExpressionNameListContext)_localctx).Names.add(((NamedExpressionNameListContext)_localctx).identifierOrExtendedKeywordOrEscapedName);
			setState(2200);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2196);
				match(COMMA);
				setState(2197);
				((NamedExpressionNameListContext)_localctx).identifierOrExtendedKeywordOrEscapedName = identifierOrExtendedKeywordOrEscapedName();
				((NamedExpressionNameListContext)_localctx).Names.add(((NamedExpressionNameListContext)_localctx).identifierOrExtendedKeywordOrEscapedName);
				}
				}
				setState(2202);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2203);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScopedFunctionCallExpressionContext extends ParserRuleContext {
		public SimpleNameReferenceContext Scope;
		public FunctionCallExpressionContext FunctionCall;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public FunctionCallExpressionContext functionCallExpression() {
			return getRuleContext(FunctionCallExpressionContext.class,0);
		}
		public ScopedFunctionCallExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scopedFunctionCallExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScopedFunctionCallExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScopedFunctionCallExpression(this);
		}
	}

	public final ScopedFunctionCallExpressionContext scopedFunctionCallExpression() throws RecognitionException {
		ScopedFunctionCallExpressionContext _localctx = new ScopedFunctionCallExpressionContext(_ctx, getState());
		enterRule(_localctx, 378, RULE_scopedFunctionCallExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2205);
			((ScopedFunctionCallExpressionContext)_localctx).Scope = simpleNameReference();
			setState(2206);
			match(DOT);
			setState(2207);
			((ScopedFunctionCallExpressionContext)_localctx).FunctionCall = functionCallExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnnamedExpressionContext extends ParserRuleContext {
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public UnnamedExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unnamedExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterUnnamedExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitUnnamedExpression(this);
		}
	}

	public final UnnamedExpressionContext unnamedExpression() throws RecognitionException {
		UnnamedExpressionContext _localctx = new UnnamedExpressionContext(_ctx, getState());
		enterRule(_localctx, 380, RULE_unnamedExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2209);
			logicalOrExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrExpressionContext extends ParserRuleContext {
		public LogicalAndExpressionContext Left;
		public LogicalOrOperationContext logicalOrOperation;
		public List<LogicalOrOperationContext> Operations = new ArrayList<LogicalOrOperationContext>();
		public LogicalAndExpressionContext logicalAndExpression() {
			return getRuleContext(LogicalAndExpressionContext.class,0);
		}
		public List<LogicalOrOperationContext> logicalOrOperation() {
			return getRuleContexts(LogicalOrOperationContext.class);
		}
		public LogicalOrOperationContext logicalOrOperation(int i) {
			return getRuleContext(LogicalOrOperationContext.class,i);
		}
		public LogicalOrExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLogicalOrExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLogicalOrExpression(this);
		}
	}

	public final LogicalOrExpressionContext logicalOrExpression() throws RecognitionException {
		LogicalOrExpressionContext _localctx = new LogicalOrExpressionContext(_ctx, getState());
		enterRule(_localctx, 382, RULE_logicalOrExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2211);
			((LogicalOrExpressionContext)_localctx).Left = logicalAndExpression();
			setState(2215);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==OR) {
				{
				{
				setState(2212);
				((LogicalOrExpressionContext)_localctx).logicalOrOperation = logicalOrOperation();
				((LogicalOrExpressionContext)_localctx).Operations.add(((LogicalOrExpressionContext)_localctx).logicalOrOperation);
				}
				}
				setState(2217);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrOperationContext extends ParserRuleContext {
		public LogicalAndExpressionContext Right;
		public TerminalNode OR() { return getToken(HqlParser.OR, 0); }
		public LogicalAndExpressionContext logicalAndExpression() {
			return getRuleContext(LogicalAndExpressionContext.class,0);
		}
		public LogicalOrOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLogicalOrOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLogicalOrOperation(this);
		}
	}

	public final LogicalOrOperationContext logicalOrOperation() throws RecognitionException {
		LogicalOrOperationContext _localctx = new LogicalOrOperationContext(_ctx, getState());
		enterRule(_localctx, 384, RULE_logicalOrOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2218);
			match(OR);
			setState(2219);
			((LogicalOrOperationContext)_localctx).Right = logicalAndExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndExpressionContext extends ParserRuleContext {
		public EqualityExpressionContext Left;
		public LogicalAndOperationContext logicalAndOperation;
		public List<LogicalAndOperationContext> Operations = new ArrayList<LogicalAndOperationContext>();
		public EqualityExpressionContext equalityExpression() {
			return getRuleContext(EqualityExpressionContext.class,0);
		}
		public List<LogicalAndOperationContext> logicalAndOperation() {
			return getRuleContexts(LogicalAndOperationContext.class);
		}
		public LogicalAndOperationContext logicalAndOperation(int i) {
			return getRuleContext(LogicalAndOperationContext.class,i);
		}
		public LogicalAndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLogicalAndExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLogicalAndExpression(this);
		}
	}

	public final LogicalAndExpressionContext logicalAndExpression() throws RecognitionException {
		LogicalAndExpressionContext _localctx = new LogicalAndExpressionContext(_ctx, getState());
		enterRule(_localctx, 386, RULE_logicalAndExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2221);
			((LogicalAndExpressionContext)_localctx).Left = equalityExpression();
			setState(2225);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==AND) {
				{
				{
				setState(2222);
				((LogicalAndExpressionContext)_localctx).logicalAndOperation = logicalAndOperation();
				((LogicalAndExpressionContext)_localctx).Operations.add(((LogicalAndExpressionContext)_localctx).logicalAndOperation);
				}
				}
				setState(2227);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndOperationContext extends ParserRuleContext {
		public EqualityExpressionContext Right;
		public TerminalNode AND() { return getToken(HqlParser.AND, 0); }
		public EqualityExpressionContext equalityExpression() {
			return getRuleContext(EqualityExpressionContext.class,0);
		}
		public LogicalAndOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLogicalAndOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLogicalAndOperation(this);
		}
	}

	public final LogicalAndOperationContext logicalAndOperation() throws RecognitionException {
		LogicalAndOperationContext _localctx = new LogicalAndOperationContext(_ctx, getState());
		enterRule(_localctx, 388, RULE_logicalAndOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2228);
			match(AND);
			setState(2229);
			((LogicalAndOperationContext)_localctx).Right = equalityExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityExpressionContext extends ParserRuleContext {
		public RelationalExpressionContext relationalExpression() {
			return getRuleContext(RelationalExpressionContext.class,0);
		}
		public EqualsEqualityExpressionContext equalsEqualityExpression() {
			return getRuleContext(EqualsEqualityExpressionContext.class,0);
		}
		public ListEqualityExpressionContext listEqualityExpression() {
			return getRuleContext(ListEqualityExpressionContext.class,0);
		}
		public BetweenEqualityExpressionContext betweenEqualityExpression() {
			return getRuleContext(BetweenEqualityExpressionContext.class,0);
		}
		public StarEqualityExpressionContext starEqualityExpression() {
			return getRuleContext(StarEqualityExpressionContext.class,0);
		}
		public EqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEqualityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEqualityExpression(this);
		}
	}

	public final EqualityExpressionContext equalityExpression() throws RecognitionException {
		EqualityExpressionContext _localctx = new EqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 390, RULE_equalityExpression);
		try {
			setState(2236);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,193,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2231);
				relationalExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2232);
				equalsEqualityExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2233);
				listEqualityExpression();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(2234);
				betweenEqualityExpression();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(2235);
				starEqualityExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualsEqualityExpressionContext extends ParserRuleContext {
		public RelationalExpressionContext Left;
		public Token OperatorToken;
		public RelationalExpressionContext Right;
		public List<RelationalExpressionContext> relationalExpression() {
			return getRuleContexts(RelationalExpressionContext.class);
		}
		public RelationalExpressionContext relationalExpression(int i) {
			return getRuleContext(RelationalExpressionContext.class,i);
		}
		public TerminalNode EQUALEQUAL() { return getToken(HqlParser.EQUALEQUAL, 0); }
		public TerminalNode LESSTHAN_GREATERTHAN() { return getToken(HqlParser.LESSTHAN_GREATERTHAN, 0); }
		public TerminalNode EXCLAIMATIONPOINT_EQUAL() { return getToken(HqlParser.EXCLAIMATIONPOINT_EQUAL, 0); }
		public EqualsEqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalsEqualityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEqualsEqualityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEqualsEqualityExpression(this);
		}
	}

	public final EqualsEqualityExpressionContext equalsEqualityExpression() throws RecognitionException {
		EqualsEqualityExpressionContext _localctx = new EqualsEqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 392, RULE_equalsEqualityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2238);
			((EqualsEqualityExpressionContext)_localctx).Left = relationalExpression();
			setState(2239);
			((EqualsEqualityExpressionContext)_localctx).OperatorToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 269746176L) != 0)) ) {
				((EqualsEqualityExpressionContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2240);
			((EqualsEqualityExpressionContext)_localctx).Right = relationalExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListEqualityExpressionContext extends ParserRuleContext {
		public RelationalExpressionContext Left;
		public Token OperatorToken;
		public InvocationExpressionContext invocationExpression;
		public List<InvocationExpressionContext> Expressions = new ArrayList<InvocationExpressionContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public RelationalExpressionContext relationalExpression() {
			return getRuleContext(RelationalExpressionContext.class,0);
		}
		public List<InvocationExpressionContext> invocationExpression() {
			return getRuleContexts(InvocationExpressionContext.class);
		}
		public InvocationExpressionContext invocationExpression(int i) {
			return getRuleContext(InvocationExpressionContext.class,i);
		}
		public TerminalNode IN() { return getToken(HqlParser.IN, 0); }
		public TerminalNode NOT_IN() { return getToken(HqlParser.NOT_IN, 0); }
		public TerminalNode IN_CI() { return getToken(HqlParser.IN_CI, 0); }
		public TerminalNode NOT_IN_CI() { return getToken(HqlParser.NOT_IN_CI, 0); }
		public TerminalNode HAS_ANY() { return getToken(HqlParser.HAS_ANY, 0); }
		public TerminalNode HAS_ALL() { return getToken(HqlParser.HAS_ALL, 0); }
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ListEqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listEqualityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterListEqualityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitListEqualityExpression(this);
		}
	}

	public final ListEqualityExpressionContext listEqualityExpression() throws RecognitionException {
		ListEqualityExpressionContext _localctx = new ListEqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 394, RULE_listEqualityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2242);
			((ListEqualityExpressionContext)_localctx).Left = relationalExpression();
			setState(2243);
			((ListEqualityExpressionContext)_localctx).OperatorToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 105)) & ~0x3f) == 0 && ((1L << (_la - 105)) & 100663299L) != 0) || _la==NOT_IN || _la==NOT_IN_CI) ) {
				((ListEqualityExpressionContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2244);
			match(OPENPAREN);
			setState(2245);
			((ListEqualityExpressionContext)_localctx).invocationExpression = invocationExpression();
			((ListEqualityExpressionContext)_localctx).Expressions.add(((ListEqualityExpressionContext)_localctx).invocationExpression);
			setState(2250);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2246);
				match(COMMA);
				setState(2247);
				((ListEqualityExpressionContext)_localctx).invocationExpression = invocationExpression();
				((ListEqualityExpressionContext)_localctx).Expressions.add(((ListEqualityExpressionContext)_localctx).invocationExpression);
				}
				}
				setState(2252);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2253);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BetweenEqualityExpressionContext extends ParserRuleContext {
		public RelationalExpressionContext Left;
		public Token OperatorToken;
		public InvocationExpressionContext StartExpression;
		public InvocationExpressionContext EndExpression;
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode DOTDOT() { return getToken(HqlParser.DOTDOT, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public RelationalExpressionContext relationalExpression() {
			return getRuleContext(RelationalExpressionContext.class,0);
		}
		public List<InvocationExpressionContext> invocationExpression() {
			return getRuleContexts(InvocationExpressionContext.class);
		}
		public InvocationExpressionContext invocationExpression(int i) {
			return getRuleContext(InvocationExpressionContext.class,i);
		}
		public TerminalNode BETWEEN() { return getToken(HqlParser.BETWEEN, 0); }
		public TerminalNode NOT_BETWEEN() { return getToken(HqlParser.NOT_BETWEEN, 0); }
		public BetweenEqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_betweenEqualityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterBetweenEqualityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitBetweenEqualityExpression(this);
		}
	}

	public final BetweenEqualityExpressionContext betweenEqualityExpression() throws RecognitionException {
		BetweenEqualityExpressionContext _localctx = new BetweenEqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 396, RULE_betweenEqualityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2255);
			((BetweenEqualityExpressionContext)_localctx).Left = relationalExpression();
			setState(2256);
			((BetweenEqualityExpressionContext)_localctx).OperatorToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==BETWEEN || _la==NOT_BETWEEN) ) {
				((BetweenEqualityExpressionContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2257);
			match(OPENPAREN);
			setState(2258);
			((BetweenEqualityExpressionContext)_localctx).StartExpression = invocationExpression();
			setState(2259);
			match(DOTDOT);
			setState(2260);
			((BetweenEqualityExpressionContext)_localctx).EndExpression = invocationExpression();
			setState(2261);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StarEqualityExpressionContext extends ParserRuleContext {
		public RelationalExpressionContext Expression;
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public TerminalNode EQUALEQUAL() { return getToken(HqlParser.EQUALEQUAL, 0); }
		public RelationalExpressionContext relationalExpression() {
			return getRuleContext(RelationalExpressionContext.class,0);
		}
		public StarEqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_starEqualityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStarEqualityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStarEqualityExpression(this);
		}
	}

	public final StarEqualityExpressionContext starEqualityExpression() throws RecognitionException {
		StarEqualityExpressionContext _localctx = new StarEqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 398, RULE_starEqualityExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2263);
			match(ASTERISK);
			setState(2264);
			match(EQUALEQUAL);
			setState(2265);
			((StarEqualityExpressionContext)_localctx).Expression = relationalExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalExpressionContext extends ParserRuleContext {
		public AdditiveExpressionContext Left;
		public Token OperatorToken;
		public AdditiveExpressionContext Right;
		public List<AdditiveExpressionContext> additiveExpression() {
			return getRuleContexts(AdditiveExpressionContext.class);
		}
		public AdditiveExpressionContext additiveExpression(int i) {
			return getRuleContext(AdditiveExpressionContext.class,i);
		}
		public TerminalNode LESSTHAN() { return getToken(HqlParser.LESSTHAN, 0); }
		public TerminalNode GREATERTHAN() { return getToken(HqlParser.GREATERTHAN, 0); }
		public TerminalNode LESSTHAN_EQUAL() { return getToken(HqlParser.LESSTHAN_EQUAL, 0); }
		public TerminalNode GREATERTHAN_EQUAL() { return getToken(HqlParser.GREATERTHAN_EQUAL, 0); }
		public RelationalExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRelationalExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRelationalExpression(this);
		}
	}

	public final RelationalExpressionContext relationalExpression() throws RecognitionException {
		RelationalExpressionContext _localctx = new RelationalExpressionContext(_ctx, getState());
		enterRule(_localctx, 400, RULE_relationalExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2267);
			((RelationalExpressionContext)_localctx).Left = additiveExpression();
			setState(2270);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 163577856L) != 0)) {
				{
				setState(2268);
				((RelationalExpressionContext)_localctx).OperatorToken = _input.LT(1);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 163577856L) != 0)) ) {
					((RelationalExpressionContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(2269);
				((RelationalExpressionContext)_localctx).Right = additiveExpression();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveExpressionContext extends ParserRuleContext {
		public MultiplicativeExpressionContext Left;
		public AdditiveOperationContext additiveOperation;
		public List<AdditiveOperationContext> Operations = new ArrayList<AdditiveOperationContext>();
		public MultiplicativeExpressionContext multiplicativeExpression() {
			return getRuleContext(MultiplicativeExpressionContext.class,0);
		}
		public List<AdditiveOperationContext> additiveOperation() {
			return getRuleContexts(AdditiveOperationContext.class);
		}
		public AdditiveOperationContext additiveOperation(int i) {
			return getRuleContext(AdditiveOperationContext.class,i);
		}
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAdditiveExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAdditiveExpression(this);
		}
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 402, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2272);
			((AdditiveExpressionContext)_localctx).Left = multiplicativeExpression();
			setState(2276);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==DASH || _la==PLUS) {
				{
				{
				setState(2273);
				((AdditiveExpressionContext)_localctx).additiveOperation = additiveOperation();
				((AdditiveExpressionContext)_localctx).Operations.add(((AdditiveExpressionContext)_localctx).additiveOperation);
				}
				}
				setState(2278);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveOperationContext extends ParserRuleContext {
		public Token OperatorToken;
		public MultiplicativeExpressionContext Right;
		public MultiplicativeExpressionContext multiplicativeExpression() {
			return getRuleContext(MultiplicativeExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(HqlParser.PLUS, 0); }
		public TerminalNode DASH() { return getToken(HqlParser.DASH, 0); }
		public AdditiveOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAdditiveOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAdditiveOperation(this);
		}
	}

	public final AdditiveOperationContext additiveOperation() throws RecognitionException {
		AdditiveOperationContext _localctx = new AdditiveOperationContext(_ctx, getState());
		enterRule(_localctx, 404, RULE_additiveOperation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2279);
			((AdditiveOperationContext)_localctx).OperatorToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==DASH || _la==PLUS) ) {
				((AdditiveOperationContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2280);
			((AdditiveOperationContext)_localctx).Right = multiplicativeExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public StringOperatorExpressionContext Left;
		public MultiplicativeOperationContext multiplicativeOperation;
		public List<MultiplicativeOperationContext> Operations = new ArrayList<MultiplicativeOperationContext>();
		public StringOperatorExpressionContext stringOperatorExpression() {
			return getRuleContext(StringOperatorExpressionContext.class,0);
		}
		public List<MultiplicativeOperationContext> multiplicativeOperation() {
			return getRuleContexts(MultiplicativeOperationContext.class);
		}
		public MultiplicativeOperationContext multiplicativeOperation(int i) {
			return getRuleContext(MultiplicativeOperationContext.class,i);
		}
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMultiplicativeExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMultiplicativeExpression(this);
		}
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, getState());
		enterRule(_localctx, 406, RULE_multiplicativeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2282);
			((MultiplicativeExpressionContext)_localctx).Left = stringOperatorExpression();
			setState(2286);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 38654705666L) != 0)) {
				{
				{
				setState(2283);
				((MultiplicativeExpressionContext)_localctx).multiplicativeOperation = multiplicativeOperation();
				((MultiplicativeExpressionContext)_localctx).Operations.add(((MultiplicativeExpressionContext)_localctx).multiplicativeOperation);
				}
				}
				setState(2288);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeOperationContext extends ParserRuleContext {
		public Token OperatorToken;
		public StringOperatorExpressionContext Right;
		public StringOperatorExpressionContext stringOperatorExpression() {
			return getRuleContext(StringOperatorExpressionContext.class,0);
		}
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public TerminalNode SLASH() { return getToken(HqlParser.SLASH, 0); }
		public TerminalNode PERCENTSIGN() { return getToken(HqlParser.PERCENTSIGN, 0); }
		public MultiplicativeOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMultiplicativeOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMultiplicativeOperation(this);
		}
	}

	public final MultiplicativeOperationContext multiplicativeOperation() throws RecognitionException {
		MultiplicativeOperationContext _localctx = new MultiplicativeOperationContext(_ctx, getState());
		enterRule(_localctx, 408, RULE_multiplicativeOperation);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2289);
			((MultiplicativeOperationContext)_localctx).OperatorToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 38654705666L) != 0)) ) {
				((MultiplicativeOperationContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2290);
			((MultiplicativeOperationContext)_localctx).Right = stringOperatorExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringOperatorExpressionContext extends ParserRuleContext {
		public StringBinaryOperatorExpressionContext stringBinaryOperatorExpression() {
			return getRuleContext(StringBinaryOperatorExpressionContext.class,0);
		}
		public StringStarOperatorExpressionContext stringStarOperatorExpression() {
			return getRuleContext(StringStarOperatorExpressionContext.class,0);
		}
		public StringOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStringOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStringOperatorExpression(this);
		}
	}

	public final StringOperatorExpressionContext stringOperatorExpression() throws RecognitionException {
		StringOperatorExpressionContext _localctx = new StringOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 410, RULE_stringOperatorExpression);
		try {
			setState(2294);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DASH:
			case OPENBRACKET:
			case OPENPAREN:
			case PLUS:
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case CONTEXTUAL_DATATABLE:
			case COUNT:
			case DATABASE:
			case DATATABLE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case EXTERNALDATA:
			case EXTERNAL_DATA:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case MATERIALIZED_VIEW_COMBINE:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TOSCALAR:
			case TOTABLE:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case DYNAMIC:
			case GUID:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2292);
				stringBinaryOperatorExpression();
				}
				break;
			case ASTERISK:
				enterOuterAlt(_localctx, 2);
				{
				setState(2293);
				stringStarOperatorExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringBinaryOperatorExpressionContext extends ParserRuleContext {
		public InvocationExpressionContext Left;
		public StringBinaryOperationContext stringBinaryOperation;
		public List<StringBinaryOperationContext> Operations = new ArrayList<StringBinaryOperationContext>();
		public InvocationExpressionContext invocationExpression() {
			return getRuleContext(InvocationExpressionContext.class,0);
		}
		public List<StringBinaryOperationContext> stringBinaryOperation() {
			return getRuleContexts(StringBinaryOperationContext.class);
		}
		public StringBinaryOperationContext stringBinaryOperation(int i) {
			return getRuleContext(StringBinaryOperationContext.class,i);
		}
		public StringBinaryOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringBinaryOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStringBinaryOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStringBinaryOperatorExpression(this);
		}
	}

	public final StringBinaryOperatorExpressionContext stringBinaryOperatorExpression() throws RecognitionException {
		StringBinaryOperatorExpressionContext _localctx = new StringBinaryOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 412, RULE_stringBinaryOperatorExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2296);
			((StringBinaryOperatorExpressionContext)_localctx).Left = invocationExpression();
			setState(2300);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & -4611686018424765440L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 273778395414529L) != 0) || ((((_la - 142)) & ~0x3f) == 0 && ((1L << (_la - 142)) & 2173245067267L) != 0) || _la==STARTSWITH || _la==STARTSWITH_CS) {
				{
				{
				setState(2297);
				((StringBinaryOperatorExpressionContext)_localctx).stringBinaryOperation = stringBinaryOperation();
				((StringBinaryOperatorExpressionContext)_localctx).Operations.add(((StringBinaryOperatorExpressionContext)_localctx).stringBinaryOperation);
				}
				}
				setState(2302);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringBinaryOperationContext extends ParserRuleContext {
		public StringBinaryOperatorContext Operator;
		public Token HasOperator;
		public InvocationExpressionContext Right;
		public InvocationExpressionContext invocationExpression() {
			return getRuleContext(InvocationExpressionContext.class,0);
		}
		public StringBinaryOperatorContext stringBinaryOperator() {
			return getRuleContext(StringBinaryOperatorContext.class,0);
		}
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public StringBinaryOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringBinaryOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStringBinaryOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStringBinaryOperation(this);
		}
	}

	public final StringBinaryOperationContext stringBinaryOperation() throws RecognitionException {
		StringBinaryOperationContext _localctx = new StringBinaryOperationContext(_ctx, getState());
		enterRule(_localctx, 414, RULE_stringBinaryOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2305);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case EQUALTILDE:
			case EXCLAIMATIONPOINT_TILDE:
			case CONTAINS:
			case CONTAINSCS:
			case CONTAINS_CS:
			case ENDSWITH:
			case ENDSWITH_CS:
			case HAS:
			case HAS_CS:
			case HASPREFIX:
			case HASPREFIX_CS:
			case HASSUFFIX:
			case HASSUFFIX_CS:
			case LIKE:
			case LIKECS:
			case MATCHES_REGEX:
			case NOT_CONTAINS:
			case NOT_CONTAINS_CS:
			case NOT_ENDSWITH_CS:
			case NOT_ENDSWITH:
			case NOT_HAS:
			case NOT_HAS_CS:
			case NOT_HASPREFIX:
			case NOT_HASPREFIX_CS:
			case NOT_HASSUFFIX:
			case NOT_HASSUFFIX_CS:
			case NOT_STARTSWITH:
			case NOT_STARTSWITH_CS:
			case NOTCONTAINS:
			case NOTCONTAINSCS:
			case NOTLIKE:
			case NOTLIKECS:
			case STARTSWITH:
			case STARTSWITH_CS:
				{
				setState(2303);
				((StringBinaryOperationContext)_localctx).Operator = stringBinaryOperator();
				}
				break;
			case COLON:
				{
				setState(2304);
				((StringBinaryOperationContext)_localctx).HasOperator = match(COLON);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(2307);
			((StringBinaryOperationContext)_localctx).Right = invocationExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringBinaryOperatorContext extends ParserRuleContext {
		public Token OperatorToken;
		public TerminalNode EQUALTILDE() { return getToken(HqlParser.EQUALTILDE, 0); }
		public TerminalNode EXCLAIMATIONPOINT_TILDE() { return getToken(HqlParser.EXCLAIMATIONPOINT_TILDE, 0); }
		public TerminalNode HAS() { return getToken(HqlParser.HAS, 0); }
		public TerminalNode NOT_HAS() { return getToken(HqlParser.NOT_HAS, 0); }
		public TerminalNode HAS_CS() { return getToken(HqlParser.HAS_CS, 0); }
		public TerminalNode NOT_HAS_CS() { return getToken(HqlParser.NOT_HAS_CS, 0); }
		public TerminalNode HASPREFIX() { return getToken(HqlParser.HASPREFIX, 0); }
		public TerminalNode NOT_HASPREFIX() { return getToken(HqlParser.NOT_HASPREFIX, 0); }
		public TerminalNode HASPREFIX_CS() { return getToken(HqlParser.HASPREFIX_CS, 0); }
		public TerminalNode NOT_HASPREFIX_CS() { return getToken(HqlParser.NOT_HASPREFIX_CS, 0); }
		public TerminalNode HASSUFFIX() { return getToken(HqlParser.HASSUFFIX, 0); }
		public TerminalNode NOT_HASSUFFIX() { return getToken(HqlParser.NOT_HASSUFFIX, 0); }
		public TerminalNode HASSUFFIX_CS() { return getToken(HqlParser.HASSUFFIX_CS, 0); }
		public TerminalNode NOT_HASSUFFIX_CS() { return getToken(HqlParser.NOT_HASSUFFIX_CS, 0); }
		public TerminalNode LIKE() { return getToken(HqlParser.LIKE, 0); }
		public TerminalNode NOTLIKE() { return getToken(HqlParser.NOTLIKE, 0); }
		public TerminalNode LIKECS() { return getToken(HqlParser.LIKECS, 0); }
		public TerminalNode NOTLIKECS() { return getToken(HqlParser.NOTLIKECS, 0); }
		public TerminalNode CONTAINS() { return getToken(HqlParser.CONTAINS, 0); }
		public TerminalNode NOTCONTAINS() { return getToken(HqlParser.NOTCONTAINS, 0); }
		public TerminalNode CONTAINSCS() { return getToken(HqlParser.CONTAINSCS, 0); }
		public TerminalNode NOTCONTAINSCS() { return getToken(HqlParser.NOTCONTAINSCS, 0); }
		public TerminalNode NOT_CONTAINS() { return getToken(HqlParser.NOT_CONTAINS, 0); }
		public TerminalNode CONTAINS_CS() { return getToken(HqlParser.CONTAINS_CS, 0); }
		public TerminalNode NOT_CONTAINS_CS() { return getToken(HqlParser.NOT_CONTAINS_CS, 0); }
		public TerminalNode STARTSWITH() { return getToken(HqlParser.STARTSWITH, 0); }
		public TerminalNode NOT_STARTSWITH() { return getToken(HqlParser.NOT_STARTSWITH, 0); }
		public TerminalNode STARTSWITH_CS() { return getToken(HqlParser.STARTSWITH_CS, 0); }
		public TerminalNode NOT_STARTSWITH_CS() { return getToken(HqlParser.NOT_STARTSWITH_CS, 0); }
		public TerminalNode ENDSWITH() { return getToken(HqlParser.ENDSWITH, 0); }
		public TerminalNode NOT_ENDSWITH() { return getToken(HqlParser.NOT_ENDSWITH, 0); }
		public TerminalNode ENDSWITH_CS() { return getToken(HqlParser.ENDSWITH_CS, 0); }
		public TerminalNode NOT_ENDSWITH_CS() { return getToken(HqlParser.NOT_ENDSWITH_CS, 0); }
		public TerminalNode MATCHES_REGEX() { return getToken(HqlParser.MATCHES_REGEX, 0); }
		public StringBinaryOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringBinaryOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStringBinaryOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStringBinaryOperator(this);
		}
	}

	public final StringBinaryOperatorContext stringBinaryOperator() throws RecognitionException {
		StringBinaryOperatorContext _localctx = new StringBinaryOperatorContext(_ctx, getState());
		enterRule(_localctx, 416, RULE_stringBinaryOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2309);
			((StringBinaryOperatorContext)_localctx).OperatorToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & -4611686018424766464L) != 0) || ((((_la - 64)) & ~0x3f) == 0 && ((1L << (_la - 64)) & 273778395414529L) != 0) || ((((_la - 142)) & ~0x3f) == 0 && ((1L << (_la - 142)) & 2173245067267L) != 0) || _la==STARTSWITH || _la==STARTSWITH_CS) ) {
				((StringBinaryOperatorContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringStarOperatorExpressionContext extends ParserRuleContext {
		public Token LeftStarToken;
		public StringBinaryOperatorContext Operator;
		public InvocationExpressionContext Right;
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public StringBinaryOperatorContext stringBinaryOperator() {
			return getRuleContext(StringBinaryOperatorContext.class,0);
		}
		public InvocationExpressionContext invocationExpression() {
			return getRuleContext(InvocationExpressionContext.class,0);
		}
		public StringStarOperatorExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringStarOperatorExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStringStarOperatorExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStringStarOperatorExpression(this);
		}
	}

	public final StringStarOperatorExpressionContext stringStarOperatorExpression() throws RecognitionException {
		StringStarOperatorExpressionContext _localctx = new StringStarOperatorExpressionContext(_ctx, getState());
		enterRule(_localctx, 418, RULE_stringStarOperatorExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2311);
			((StringStarOperatorExpressionContext)_localctx).LeftStarToken = match(ASTERISK);
			setState(2312);
			((StringStarOperatorExpressionContext)_localctx).Operator = stringBinaryOperator();
			setState(2313);
			((StringStarOperatorExpressionContext)_localctx).Right = invocationExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InvocationExpressionContext extends ParserRuleContext {
		public Token OperatorToken;
		public FunctionCallOrPathExpressionContext Expression;
		public FunctionCallOrPathExpressionContext functionCallOrPathExpression() {
			return getRuleContext(FunctionCallOrPathExpressionContext.class,0);
		}
		public TerminalNode PLUS() { return getToken(HqlParser.PLUS, 0); }
		public TerminalNode DASH() { return getToken(HqlParser.DASH, 0); }
		public InvocationExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_invocationExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterInvocationExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitInvocationExpression(this);
		}
	}

	public final InvocationExpressionContext invocationExpression() throws RecognitionException {
		InvocationExpressionContext _localctx = new InvocationExpressionContext(_ctx, getState());
		enterRule(_localctx, 420, RULE_invocationExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2316);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DASH || _la==PLUS) {
				{
				setState(2315);
				((InvocationExpressionContext)_localctx).OperatorToken = _input.LT(1);
				_la = _input.LA(1);
				if ( !(_la==DASH || _la==PLUS) ) {
					((InvocationExpressionContext)_localctx).OperatorToken = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
			}

			setState(2318);
			((InvocationExpressionContext)_localctx).Expression = functionCallOrPathExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallOrPathExpressionContext extends ParserRuleContext {
		public FunctionCallOrPathRootContext functionCallOrPathRoot() {
			return getRuleContext(FunctionCallOrPathRootContext.class,0);
		}
		public FunctionCallOrPathPathExpressionContext functionCallOrPathPathExpression() {
			return getRuleContext(FunctionCallOrPathPathExpressionContext.class,0);
		}
		public ToTableExpressionContext toTableExpression() {
			return getRuleContext(ToTableExpressionContext.class,0);
		}
		public FunctionCallOrPathExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOrPathExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionCallOrPathExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionCallOrPathExpression(this);
		}
	}

	public final FunctionCallOrPathExpressionContext functionCallOrPathExpression() throws RecognitionException {
		FunctionCallOrPathExpressionContext _localctx = new FunctionCallOrPathExpressionContext(_ctx, getState());
		enterRule(_localctx, 422, RULE_functionCallOrPathExpression);
		try {
			setState(2323);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,202,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2320);
				functionCallOrPathRoot();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2321);
				functionCallOrPathPathExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2322);
				toTableExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallOrPathRootContext extends ParserRuleContext {
		public DotCompositeFunctionCallExpressionContext dotCompositeFunctionCallExpression() {
			return getRuleContext(DotCompositeFunctionCallExpressionContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public ToScalarExpressionContext toScalarExpression() {
			return getRuleContext(ToScalarExpressionContext.class,0);
		}
		public FunctionCallOrPathRootContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOrPathRoot; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionCallOrPathRoot(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionCallOrPathRoot(this);
		}
	}

	public final FunctionCallOrPathRootContext functionCallOrPathRoot() throws RecognitionException {
		FunctionCallOrPathRootContext _localctx = new FunctionCallOrPathRootContext(_ctx, getState());
		enterRule(_localctx, 424, RULE_functionCallOrPathRoot);
		try {
			setState(2328);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,203,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2325);
				dotCompositeFunctionCallExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2326);
				primaryExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2327);
				toScalarExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallOrPathPathExpressionContext extends ParserRuleContext {
		public FunctionCallOrPathRootContext Expression;
		public FunctionCallOrPathOperationContext functionCallOrPathOperation;
		public List<FunctionCallOrPathOperationContext> Operations = new ArrayList<FunctionCallOrPathOperationContext>();
		public FunctionCallOrPathRootContext functionCallOrPathRoot() {
			return getRuleContext(FunctionCallOrPathRootContext.class,0);
		}
		public List<FunctionCallOrPathOperationContext> functionCallOrPathOperation() {
			return getRuleContexts(FunctionCallOrPathOperationContext.class);
		}
		public FunctionCallOrPathOperationContext functionCallOrPathOperation(int i) {
			return getRuleContext(FunctionCallOrPathOperationContext.class,i);
		}
		public FunctionCallOrPathPathExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOrPathPathExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionCallOrPathPathExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionCallOrPathPathExpression(this);
		}
	}

	public final FunctionCallOrPathPathExpressionContext functionCallOrPathPathExpression() throws RecognitionException {
		FunctionCallOrPathPathExpressionContext _localctx = new FunctionCallOrPathPathExpressionContext(_ctx, getState());
		enterRule(_localctx, 426, RULE_functionCallOrPathPathExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2330);
			((FunctionCallOrPathPathExpressionContext)_localctx).Expression = functionCallOrPathRoot();
			setState(2332); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(2331);
				((FunctionCallOrPathPathExpressionContext)_localctx).functionCallOrPathOperation = functionCallOrPathOperation();
				((FunctionCallOrPathPathExpressionContext)_localctx).Operations.add(((FunctionCallOrPathPathExpressionContext)_localctx).functionCallOrPathOperation);
				}
				}
				setState(2334); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DOT || _la==OPENBRACKET );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallOrPathOperationContext extends ParserRuleContext {
		public FunctionalCallOrPathPathOperationContext functionalCallOrPathPathOperation() {
			return getRuleContext(FunctionalCallOrPathPathOperationContext.class,0);
		}
		public FunctionCallOrPathElementOperationContext functionCallOrPathElementOperation() {
			return getRuleContext(FunctionCallOrPathElementOperationContext.class,0);
		}
		public LegacyFunctionCallOrPathElementOperationContext legacyFunctionCallOrPathElementOperation() {
			return getRuleContext(LegacyFunctionCallOrPathElementOperationContext.class,0);
		}
		public FunctionCallOrPathOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOrPathOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionCallOrPathOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionCallOrPathOperation(this);
		}
	}

	public final FunctionCallOrPathOperationContext functionCallOrPathOperation() throws RecognitionException {
		FunctionCallOrPathOperationContext _localctx = new FunctionCallOrPathOperationContext(_ctx, getState());
		enterRule(_localctx, 428, RULE_functionCallOrPathOperation);
		try {
			setState(2339);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,205,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2336);
				functionalCallOrPathPathOperation();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2337);
				functionCallOrPathElementOperation();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2338);
				legacyFunctionCallOrPathElementOperation();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionalCallOrPathPathOperationContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public FunctionalCallOrPathPathOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionalCallOrPathPathOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionalCallOrPathPathOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionalCallOrPathPathOperation(this);
		}
	}

	public final FunctionalCallOrPathPathOperationContext functionalCallOrPathPathOperation() throws RecognitionException {
		FunctionalCallOrPathPathOperationContext _localctx = new FunctionalCallOrPathPathOperationContext(_ctx, getState());
		enterRule(_localctx, 430, RULE_functionalCallOrPathPathOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2341);
			match(DOT);
			setState(2342);
			((FunctionalCallOrPathPathOperationContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallOrPathElementOperationContext extends ParserRuleContext {
		public UnnamedExpressionContext Element;
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public FunctionCallOrPathElementOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallOrPathElementOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionCallOrPathElementOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionCallOrPathElementOperation(this);
		}
	}

	public final FunctionCallOrPathElementOperationContext functionCallOrPathElementOperation() throws RecognitionException {
		FunctionCallOrPathElementOperationContext _localctx = new FunctionCallOrPathElementOperationContext(_ctx, getState());
		enterRule(_localctx, 432, RULE_functionCallOrPathElementOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2344);
			match(OPENBRACKET);
			setState(2345);
			((FunctionCallOrPathElementOperationContext)_localctx).Element = unnamedExpression();
			setState(2346);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LegacyFunctionCallOrPathElementOperationContext extends ParserRuleContext {
		public UnnamedExpressionContext Element;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public LegacyFunctionCallOrPathElementOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_legacyFunctionCallOrPathElementOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLegacyFunctionCallOrPathElementOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLegacyFunctionCallOrPathElementOperation(this);
		}
	}

	public final LegacyFunctionCallOrPathElementOperationContext legacyFunctionCallOrPathElementOperation() throws RecognitionException {
		LegacyFunctionCallOrPathElementOperationContext _localctx = new LegacyFunctionCallOrPathElementOperationContext(_ctx, getState());
		enterRule(_localctx, 434, RULE_legacyFunctionCallOrPathElementOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2348);
			match(DOT);
			setState(2349);
			match(OPENBRACKET);
			setState(2350);
			((LegacyFunctionCallOrPathElementOperationContext)_localctx).Element = unnamedExpression();
			setState(2351);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ToScalarExpressionContext extends ParserRuleContext {
		public PipeExpressionContext Expression;
		public TerminalNode TOSCALAR() { return getToken(HqlParser.TOSCALAR, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public PipeExpressionContext pipeExpression() {
			return getRuleContext(PipeExpressionContext.class,0);
		}
		public NoOptimizationParameterContext noOptimizationParameter() {
			return getRuleContext(NoOptimizationParameterContext.class,0);
		}
		public ToScalarExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_toScalarExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterToScalarExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitToScalarExpression(this);
		}
	}

	public final ToScalarExpressionContext toScalarExpression() throws RecognitionException {
		ToScalarExpressionContext _localctx = new ToScalarExpressionContext(_ctx, getState());
		enterRule(_localctx, 436, RULE_toScalarExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2353);
			match(TOSCALAR);
			setState(2355);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KIND) {
				{
				setState(2354);
				noOptimizationParameter();
				}
			}

			setState(2357);
			match(OPENPAREN);
			setState(2358);
			((ToScalarExpressionContext)_localctx).Expression = pipeExpression();
			setState(2359);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ToTableExpressionContext extends ParserRuleContext {
		public PipeExpressionContext Expression;
		public TerminalNode TOTABLE() { return getToken(HqlParser.TOTABLE, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public PipeExpressionContext pipeExpression() {
			return getRuleContext(PipeExpressionContext.class,0);
		}
		public NoOptimizationParameterContext noOptimizationParameter() {
			return getRuleContext(NoOptimizationParameterContext.class,0);
		}
		public ToTableExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_toTableExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterToTableExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitToTableExpression(this);
		}
	}

	public final ToTableExpressionContext toTableExpression() throws RecognitionException {
		ToTableExpressionContext _localctx = new ToTableExpressionContext(_ctx, getState());
		enterRule(_localctx, 438, RULE_toTableExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2361);
			match(TOTABLE);
			setState(2363);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==KIND) {
				{
				setState(2362);
				noOptimizationParameter();
				}
			}

			setState(2365);
			match(OPENPAREN);
			setState(2366);
			((ToTableExpressionContext)_localctx).Expression = pipeExpression();
			setState(2367);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NoOptimizationParameterContext extends ParserRuleContext {
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode NOOPTIMIZATION() { return getToken(HqlParser.NOOPTIMIZATION, 0); }
		public NoOptimizationParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_noOptimizationParameter; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNoOptimizationParameter(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNoOptimizationParameter(this);
		}
	}

	public final NoOptimizationParameterContext noOptimizationParameter() throws RecognitionException {
		NoOptimizationParameterContext _localctx = new NoOptimizationParameterContext(_ctx, getState());
		enterRule(_localctx, 440, RULE_noOptimizationParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2369);
			match(KIND);
			setState(2370);
			match(EQUAL);
			setState(2371);
			match(NOOPTIMIZATION);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DotCompositeFunctionCallExpressionContext extends ParserRuleContext {
		public FunctionCallExpressionContext Call;
		public DotCompositeFunctionCallOperationContext dotCompositeFunctionCallOperation;
		public List<DotCompositeFunctionCallOperationContext> Operations = new ArrayList<DotCompositeFunctionCallOperationContext>();
		public FunctionCallExpressionContext functionCallExpression() {
			return getRuleContext(FunctionCallExpressionContext.class,0);
		}
		public List<DotCompositeFunctionCallOperationContext> dotCompositeFunctionCallOperation() {
			return getRuleContexts(DotCompositeFunctionCallOperationContext.class);
		}
		public DotCompositeFunctionCallOperationContext dotCompositeFunctionCallOperation(int i) {
			return getRuleContext(DotCompositeFunctionCallOperationContext.class,i);
		}
		public DotCompositeFunctionCallExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dotCompositeFunctionCallExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDotCompositeFunctionCallExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDotCompositeFunctionCallExpression(this);
		}
	}

	public final DotCompositeFunctionCallExpressionContext dotCompositeFunctionCallExpression() throws RecognitionException {
		DotCompositeFunctionCallExpressionContext _localctx = new DotCompositeFunctionCallExpressionContext(_ctx, getState());
		enterRule(_localctx, 442, RULE_dotCompositeFunctionCallExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2373);
			((DotCompositeFunctionCallExpressionContext)_localctx).Call = functionCallExpression();
			setState(2377);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,208,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2374);
					((DotCompositeFunctionCallExpressionContext)_localctx).dotCompositeFunctionCallOperation = dotCompositeFunctionCallOperation();
					((DotCompositeFunctionCallExpressionContext)_localctx).Operations.add(((DotCompositeFunctionCallExpressionContext)_localctx).dotCompositeFunctionCallOperation);
					}
					} 
				}
				setState(2379);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,208,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DotCompositeFunctionCallOperationContext extends ParserRuleContext {
		public FunctionCallExpressionContext Call;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public FunctionCallExpressionContext functionCallExpression() {
			return getRuleContext(FunctionCallExpressionContext.class,0);
		}
		public DotCompositeFunctionCallOperationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dotCompositeFunctionCallOperation; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDotCompositeFunctionCallOperation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDotCompositeFunctionCallOperation(this);
		}
	}

	public final DotCompositeFunctionCallOperationContext dotCompositeFunctionCallOperation() throws RecognitionException {
		DotCompositeFunctionCallOperationContext _localctx = new DotCompositeFunctionCallOperationContext(_ctx, getState());
		enterRule(_localctx, 444, RULE_dotCompositeFunctionCallOperation);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2380);
			match(DOT);
			setState(2381);
			((DotCompositeFunctionCallOperationContext)_localctx).Call = functionCallExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallExpressionContext extends ParserRuleContext {
		public NamedFunctionCallExpressionContext namedFunctionCallExpression() {
			return getRuleContext(NamedFunctionCallExpressionContext.class,0);
		}
		public CountExpressionContext countExpression() {
			return getRuleContext(CountExpressionContext.class,0);
		}
		public FunctionCallExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCallExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterFunctionCallExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitFunctionCallExpression(this);
		}
	}

	public final FunctionCallExpressionContext functionCallExpression() throws RecognitionException {
		FunctionCallExpressionContext _localctx = new FunctionCallExpressionContext(_ctx, getState());
		enterRule(_localctx, 446, RULE_functionCallExpression);
		try {
			setState(2385);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case OPENBRACKET:
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2383);
				namedFunctionCallExpression();
				}
				break;
			case COUNT:
				enterOuterAlt(_localctx, 2);
				{
				setState(2384);
				countExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NamedFunctionCallExpressionContext extends ParserRuleContext {
		public SimpleNameReferenceContext Name;
		public ArgumentExpressionContext argumentExpression;
		public List<ArgumentExpressionContext> Arguments = new ArrayList<ArgumentExpressionContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public List<ArgumentExpressionContext> argumentExpression() {
			return getRuleContexts(ArgumentExpressionContext.class);
		}
		public ArgumentExpressionContext argumentExpression(int i) {
			return getRuleContext(ArgumentExpressionContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public NamedFunctionCallExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_namedFunctionCallExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNamedFunctionCallExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNamedFunctionCallExpression(this);
		}
	}

	public final NamedFunctionCallExpressionContext namedFunctionCallExpression() throws RecognitionException {
		NamedFunctionCallExpressionContext _localctx = new NamedFunctionCallExpressionContext(_ctx, getState());
		enterRule(_localctx, 448, RULE_namedFunctionCallExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2387);
			((NamedFunctionCallExpressionContext)_localctx).Name = simpleNameReference();
			setState(2388);
			match(OPENPAREN);
			setState(2397);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416134715541506L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1729240967922960685L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211090525197L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 504262421452422151L) != 0)) {
				{
				setState(2389);
				((NamedFunctionCallExpressionContext)_localctx).argumentExpression = argumentExpression();
				((NamedFunctionCallExpressionContext)_localctx).Arguments.add(((NamedFunctionCallExpressionContext)_localctx).argumentExpression);
				setState(2394);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(2390);
					match(COMMA);
					setState(2391);
					((NamedFunctionCallExpressionContext)_localctx).argumentExpression = argumentExpression();
					((NamedFunctionCallExpressionContext)_localctx).Arguments.add(((NamedFunctionCallExpressionContext)_localctx).argumentExpression);
					}
					}
					setState(2396);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(2399);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentExpressionContext extends ParserRuleContext {
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public StarExpressionContext starExpression() {
			return getRuleContext(StarExpressionContext.class,0);
		}
		public ArgumentExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterArgumentExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitArgumentExpression(this);
		}
	}

	public final ArgumentExpressionContext argumentExpression() throws RecognitionException {
		ArgumentExpressionContext _localctx = new ArgumentExpressionContext(_ctx, getState());
		enterRule(_localctx, 450, RULE_argumentExpression);
		try {
			setState(2403);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,212,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2401);
				namedExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2402);
				starExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CountExpressionContext extends ParserRuleContext {
		public NamedExpressionContext Expression;
		public TerminalNode COUNT() { return getToken(HqlParser.COUNT, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public NamedExpressionContext namedExpression() {
			return getRuleContext(NamedExpressionContext.class,0);
		}
		public CountExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_countExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterCountExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitCountExpression(this);
		}
	}

	public final CountExpressionContext countExpression() throws RecognitionException {
		CountExpressionContext _localctx = new CountExpressionContext(_ctx, getState());
		enterRule(_localctx, 452, RULE_countExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2405);
			match(COUNT);
			setState(2406);
			match(OPENPAREN);
			setState(2408);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416134715541506L) != 0) || ((((_la - 65)) & ~0x3f) == 0 && ((1L << (_la - 65)) & -1729240967922960685L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211090525197L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 504262421452422151L) != 0)) {
				{
				setState(2407);
				((CountExpressionContext)_localctx).Expression = namedExpression();
				}
			}

			setState(2410);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StarExpressionContext extends ParserRuleContext {
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public StarExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_starExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStarExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStarExpression(this);
		}
	}

	public final StarExpressionContext starExpression() throws RecognitionException {
		StarExpressionContext _localctx = new StarExpressionContext(_ctx, getState());
		enterRule(_localctx, 454, RULE_starExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2412);
			match(ASTERISK);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public UnsignedLiteralExpressionContext unsignedLiteralExpression() {
			return getRuleContext(UnsignedLiteralExpressionContext.class,0);
		}
		public NameReferenceWithDataScopeContext nameReferenceWithDataScope() {
			return getRuleContext(NameReferenceWithDataScopeContext.class,0);
		}
		public DataTableExpressionContext dataTableExpression() {
			return getRuleContext(DataTableExpressionContext.class,0);
		}
		public ExternalDataExpressionContext externalDataExpression() {
			return getRuleContext(ExternalDataExpressionContext.class,0);
		}
		public ContextualDataTableExpressionContext contextualDataTableExpression() {
			return getRuleContext(ContextualDataTableExpressionContext.class,0);
		}
		public MaterializedViewCombineExpressionContext materializedViewCombineExpression() {
			return getRuleContext(MaterializedViewCombineExpressionContext.class,0);
		}
		public ParenthesizedExpressionContext parenthesizedExpression() {
			return getRuleContext(ParenthesizedExpressionContext.class,0);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterPrimaryExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitPrimaryExpression(this);
		}
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 456, RULE_primaryExpression);
		try {
			setState(2421);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DYNAMIC:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(2414);
				unsignedLiteralExpression();
				}
				break;
			case OPENBRACKET:
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(2415);
				nameReferenceWithDataScope();
				}
				break;
			case DATATABLE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2416);
				dataTableExpression();
				}
				break;
			case EXTERNALDATA:
			case EXTERNAL_DATA:
				enterOuterAlt(_localctx, 4);
				{
				setState(2417);
				externalDataExpression();
				}
				break;
			case CONTEXTUAL_DATATABLE:
				enterOuterAlt(_localctx, 5);
				{
				setState(2418);
				contextualDataTableExpression();
				}
				break;
			case MATERIALIZED_VIEW_COMBINE:
				enterOuterAlt(_localctx, 6);
				{
				setState(2419);
				materializedViewCombineExpression();
				}
				break;
			case OPENPAREN:
				enterOuterAlt(_localctx, 7);
				{
				setState(2420);
				parenthesizedExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NameReferenceWithDataScopeContext extends ParserRuleContext {
		public SimpleNameReferenceContext Name;
		public DataScopeClauseContext Scope;
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public DataScopeClauseContext dataScopeClause() {
			return getRuleContext(DataScopeClauseContext.class,0);
		}
		public NameReferenceWithDataScopeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nameReferenceWithDataScope; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNameReferenceWithDataScope(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNameReferenceWithDataScope(this);
		}
	}

	public final NameReferenceWithDataScopeContext nameReferenceWithDataScope() throws RecognitionException {
		NameReferenceWithDataScopeContext _localctx = new NameReferenceWithDataScopeContext(_ctx, getState());
		enterRule(_localctx, 458, RULE_nameReferenceWithDataScope);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2423);
			((NameReferenceWithDataScopeContext)_localctx).Name = simpleNameReference();
			setState(2425);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DATASCOPE) {
				{
				setState(2424);
				((NameReferenceWithDataScopeContext)_localctx).Scope = dataScopeClause();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DataScopeClauseContext extends ParserRuleContext {
		public Token KindToken;
		public TerminalNode DATASCOPE() { return getToken(HqlParser.DATASCOPE, 0); }
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public TerminalNode HOTCACHE() { return getToken(HqlParser.HOTCACHE, 0); }
		public TerminalNode ALL() { return getToken(HqlParser.ALL, 0); }
		public DataScopeClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dataScopeClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDataScopeClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDataScopeClause(this);
		}
	}

	public final DataScopeClauseContext dataScopeClause() throws RecognitionException {
		DataScopeClauseContext _localctx = new DataScopeClauseContext(_ctx, getState());
		enterRule(_localctx, 460, RULE_dataScopeClause);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2427);
			match(DATASCOPE);
			setState(2428);
			match(EQUAL);
			setState(2429);
			((DataScopeClauseContext)_localctx).KindToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==ALL || _la==HOTCACHE) ) {
				((DataScopeClauseContext)_localctx).KindToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParenthesizedExpressionContext extends ParserRuleContext {
		public ExpressionContext Expression;
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ParenthesizedExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parenthesizedExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParenthesizedExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParenthesizedExpression(this);
		}
	}

	public final ParenthesizedExpressionContext parenthesizedExpression() throws RecognitionException {
		ParenthesizedExpressionContext _localctx = new ParenthesizedExpressionContext(_ctx, getState());
		enterRule(_localctx, 462, RULE_parenthesizedExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2431);
			match(OPENPAREN);
			setState(2432);
			((ParenthesizedExpressionContext)_localctx).Expression = expression();
			setState(2433);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RangeExpressionContext extends ParserRuleContext {
		public SimpleNameReferenceContext Expression;
		public UnnamedExpressionContext FromExpression;
		public UnnamedExpressionContext ToExpression;
		public UnnamedExpressionContext StepExpression;
		public TerminalNode RANGE() { return getToken(HqlParser.RANGE, 0); }
		public TerminalNode FROM() { return getToken(HqlParser.FROM, 0); }
		public TerminalNode TO() { return getToken(HqlParser.TO, 0); }
		public TerminalNode STEP() { return getToken(HqlParser.STEP, 0); }
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public List<UnnamedExpressionContext> unnamedExpression() {
			return getRuleContexts(UnnamedExpressionContext.class);
		}
		public UnnamedExpressionContext unnamedExpression(int i) {
			return getRuleContext(UnnamedExpressionContext.class,i);
		}
		public RangeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rangeExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRangeExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRangeExpression(this);
		}
	}

	public final RangeExpressionContext rangeExpression() throws RecognitionException {
		RangeExpressionContext _localctx = new RangeExpressionContext(_ctx, getState());
		enterRule(_localctx, 464, RULE_rangeExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2435);
			match(RANGE);
			setState(2436);
			((RangeExpressionContext)_localctx).Expression = simpleNameReference();
			setState(2437);
			match(FROM);
			setState(2438);
			((RangeExpressionContext)_localctx).FromExpression = unnamedExpression();
			setState(2439);
			match(TO);
			setState(2440);
			((RangeExpressionContext)_localctx).ToExpression = unnamedExpression();
			setState(2441);
			match(STEP);
			setState(2442);
			((RangeExpressionContext)_localctx).StepExpression = unnamedExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityExpressionContext extends ParserRuleContext {
		public EntityNameReferenceContext entityNameReference() {
			return getRuleContext(EntityNameReferenceContext.class,0);
		}
		public EntityPathOrElementExpressionContext entityPathOrElementExpression() {
			return getRuleContext(EntityPathOrElementExpressionContext.class,0);
		}
		public EntityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityExpression(this);
		}
	}

	public final EntityExpressionContext entityExpression() throws RecognitionException {
		EntityExpressionContext _localctx = new EntityExpressionContext(_ctx, getState());
		enterRule(_localctx, 466, RULE_entityExpression);
		try {
			setState(2446);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,216,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2444);
				entityNameReference();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2445);
				entityPathOrElementExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityPathOrElementExpressionContext extends ParserRuleContext {
		public EntityNameReferenceContext Expression;
		public EntityPathOrElementOperatorContext entityPathOrElementOperator;
		public List<EntityPathOrElementOperatorContext> Operators = new ArrayList<EntityPathOrElementOperatorContext>();
		public EntityNameReferenceContext entityNameReference() {
			return getRuleContext(EntityNameReferenceContext.class,0);
		}
		public List<EntityPathOrElementOperatorContext> entityPathOrElementOperator() {
			return getRuleContexts(EntityPathOrElementOperatorContext.class);
		}
		public EntityPathOrElementOperatorContext entityPathOrElementOperator(int i) {
			return getRuleContext(EntityPathOrElementOperatorContext.class,i);
		}
		public EntityPathOrElementExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityPathOrElementExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityPathOrElementExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityPathOrElementExpression(this);
		}
	}

	public final EntityPathOrElementExpressionContext entityPathOrElementExpression() throws RecognitionException {
		EntityPathOrElementExpressionContext _localctx = new EntityPathOrElementExpressionContext(_ctx, getState());
		enterRule(_localctx, 468, RULE_entityPathOrElementExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2448);
			((EntityPathOrElementExpressionContext)_localctx).Expression = entityNameReference();
			setState(2450); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(2449);
				((EntityPathOrElementExpressionContext)_localctx).entityPathOrElementOperator = entityPathOrElementOperator();
				((EntityPathOrElementExpressionContext)_localctx).Operators.add(((EntityPathOrElementExpressionContext)_localctx).entityPathOrElementOperator);
				}
				}
				setState(2452); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==DOT || _la==OPENBRACKET );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityPathOrElementOperatorContext extends ParserRuleContext {
		public EntityPathOperatorContext Path;
		public EntityElementOperatorContext Element;
		public LegacyEntityPathElementOperatorContext PathElement;
		public EntityPathOperatorContext entityPathOperator() {
			return getRuleContext(EntityPathOperatorContext.class,0);
		}
		public EntityElementOperatorContext entityElementOperator() {
			return getRuleContext(EntityElementOperatorContext.class,0);
		}
		public LegacyEntityPathElementOperatorContext legacyEntityPathElementOperator() {
			return getRuleContext(LegacyEntityPathElementOperatorContext.class,0);
		}
		public EntityPathOrElementOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityPathOrElementOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityPathOrElementOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityPathOrElementOperator(this);
		}
	}

	public final EntityPathOrElementOperatorContext entityPathOrElementOperator() throws RecognitionException {
		EntityPathOrElementOperatorContext _localctx = new EntityPathOrElementOperatorContext(_ctx, getState());
		enterRule(_localctx, 470, RULE_entityPathOrElementOperator);
		try {
			setState(2457);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,218,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2454);
				((EntityPathOrElementOperatorContext)_localctx).Path = entityPathOperator();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2455);
				((EntityPathOrElementOperatorContext)_localctx).Element = entityElementOperator();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2456);
				((EntityPathOrElementOperatorContext)_localctx).PathElement = legacyEntityPathElementOperator();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityPathOperatorContext extends ParserRuleContext {
		public EntityNameContext Name;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public EntityNameContext entityName() {
			return getRuleContext(EntityNameContext.class,0);
		}
		public EntityPathOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityPathOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityPathOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityPathOperator(this);
		}
	}

	public final EntityPathOperatorContext entityPathOperator() throws RecognitionException {
		EntityPathOperatorContext _localctx = new EntityPathOperatorContext(_ctx, getState());
		enterRule(_localctx, 472, RULE_entityPathOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2459);
			match(DOT);
			setState(2460);
			((EntityPathOperatorContext)_localctx).Name = entityName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityElementOperatorContext extends ParserRuleContext {
		public UnnamedExpressionContext Expression;
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public EntityElementOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityElementOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityElementOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityElementOperator(this);
		}
	}

	public final EntityElementOperatorContext entityElementOperator() throws RecognitionException {
		EntityElementOperatorContext _localctx = new EntityElementOperatorContext(_ctx, getState());
		enterRule(_localctx, 474, RULE_entityElementOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2462);
			match(OPENBRACKET);
			setState(2463);
			((EntityElementOperatorContext)_localctx).Expression = unnamedExpression();
			setState(2464);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LegacyEntityPathElementOperatorContext extends ParserRuleContext {
		public UnnamedExpressionContext Expression;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public UnnamedExpressionContext unnamedExpression() {
			return getRuleContext(UnnamedExpressionContext.class,0);
		}
		public LegacyEntityPathElementOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_legacyEntityPathElementOperator; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLegacyEntityPathElementOperator(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLegacyEntityPathElementOperator(this);
		}
	}

	public final LegacyEntityPathElementOperatorContext legacyEntityPathElementOperator() throws RecognitionException {
		LegacyEntityPathElementOperatorContext _localctx = new LegacyEntityPathElementOperatorContext(_ctx, getState());
		enterRule(_localctx, 476, RULE_legacyEntityPathElementOperator);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2466);
			match(DOT);
			setState(2467);
			match(OPENBRACKET);
			setState(2468);
			((LegacyEntityPathElementOperatorContext)_localctx).Expression = unnamedExpression();
			setState(2469);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityNameContext extends ParserRuleContext {
		public AtSignNameContext ATSIGN;
		public IdentifierOrExtendedKeywordOrEscapedNameContext Name;
		public ExtendedPathNameContext ExtendedName;
		public AtSignNameContext atSignName() {
			return getRuleContext(AtSignNameContext.class,0);
		}
		public IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrExtendedKeywordOrEscapedNameContext.class,0);
		}
		public ExtendedPathNameContext extendedPathName() {
			return getRuleContext(ExtendedPathNameContext.class,0);
		}
		public EntityNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityName(this);
		}
	}

	public final EntityNameContext entityName() throws RecognitionException {
		EntityNameContext _localctx = new EntityNameContext(_ctx, getState());
		enterRule(_localctx, 478, RULE_entityName);
		try {
			setState(2474);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ATSIGN:
				enterOuterAlt(_localctx, 1);
				{
				setState(2471);
				((EntityNameContext)_localctx).ATSIGN = atSignName();
				}
				break;
			case OPENBRACKET:
			case ACCESS:
			case ACCUMULATE:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AS:
			case AXES:
			case BASE:
			case BIN:
			case BY:
			case CLUSTER:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATABASE:
			case DATATABLE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case DISTINCT:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case EXTEND:
			case EXTERNALDATA:
			case FACET:
			case FILTER:
			case FIND:
			case FORK:
			case FROM:
			case HAS:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case IN:
			case INTO:
			case INVOKE:
			case LEGEND:
			case LET:
			case LIMIT:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case MATERIALIZE:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case OF:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARSE:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case PRINT:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SERIES:
			case SET:
			case SORT:
			case STACKED:
			case STACKED100:
			case STEP:
			case SUMMARIZE:
			case TAKE:
			case THRESHOLD:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WHERE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				enterOuterAlt(_localctx, 2);
				{
				setState(2472);
				((EntityNameContext)_localctx).Name = identifierOrExtendedKeywordOrEscapedName();
				}
				break;
			case KIND:
			case WITHSOURCE:
			case WITH_SOURCE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2473);
				((EntityNameContext)_localctx).ExtendedName = extendedPathName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EntityNameReferenceContext extends ParserRuleContext {
		public EntityNameContext Name;
		public EntityNameContext entityName() {
			return getRuleContext(EntityNameContext.class,0);
		}
		public EntityNameReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_entityNameReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEntityNameReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEntityNameReference(this);
		}
	}

	public final EntityNameReferenceContext entityNameReference() throws RecognitionException {
		EntityNameReferenceContext _localctx = new EntityNameReferenceContext(_ctx, getState());
		enterRule(_localctx, 480, RULE_entityNameReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2476);
			((EntityNameReferenceContext)_localctx).Name = entityName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AtSignNameContext extends ParserRuleContext {
		public Token NameToken;
		public TerminalNode ATSIGN() { return getToken(HqlParser.ATSIGN, 0); }
		public AtSignNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atSignName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterAtSignName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitAtSignName(this);
		}
	}

	public final AtSignNameContext atSignName() throws RecognitionException {
		AtSignNameContext _localctx = new AtSignNameContext(_ctx, getState());
		enterRule(_localctx, 482, RULE_atSignName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2478);
			((AtSignNameContext)_localctx).NameToken = match(ATSIGN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExtendedPathNameContext extends ParserRuleContext {
		public Token NameToken;
		public TerminalNode KIND() { return getToken(HqlParser.KIND, 0); }
		public TerminalNode WITHSOURCE() { return getToken(HqlParser.WITHSOURCE, 0); }
		public TerminalNode WITH_SOURCE() { return getToken(HqlParser.WITH_SOURCE, 0); }
		public ExtendedPathNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extendedPathName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExtendedPathName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExtendedPathName(this);
		}
	}

	public final ExtendedPathNameContext extendedPathName() throws RecognitionException {
		ExtendedPathNameContext _localctx = new ExtendedPathNameContext(_ctx, getState());
		enterRule(_localctx, 484, RULE_extendedPathName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2480);
			((ExtendedPathNameContext)_localctx).NameToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==KIND || _la==WITHSOURCE || _la==WITH_SOURCE) ) {
				((ExtendedPathNameContext)_localctx).NameToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedEntityExpressionContext extends ParserRuleContext {
		public WildcardedNameReferenceContext wildcardedNameReference() {
			return getRuleContext(WildcardedNameReferenceContext.class,0);
		}
		public DotCompositeFunctionCallExpressionContext dotCompositeFunctionCallExpression() {
			return getRuleContext(DotCompositeFunctionCallExpressionContext.class,0);
		}
		public WildcardedPathExpressionContext wildcardedPathExpression() {
			return getRuleContext(WildcardedPathExpressionContext.class,0);
		}
		public WildcardedEntityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedEntityExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedEntityExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedEntityExpression(this);
		}
	}

	public final WildcardedEntityExpressionContext wildcardedEntityExpression() throws RecognitionException {
		WildcardedEntityExpressionContext _localctx = new WildcardedEntityExpressionContext(_ctx, getState());
		enterRule(_localctx, 486, RULE_wildcardedEntityExpression);
		try {
			setState(2485);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,220,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2482);
				wildcardedNameReference();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2483);
				dotCompositeFunctionCallExpression();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2484);
				wildcardedPathExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedPathExpressionContext extends ParserRuleContext {
		public DotCompositeFunctionCallExpressionContext Expression;
		public WildcardedPathNameContext Name;
		public TerminalNode DOT() { return getToken(HqlParser.DOT, 0); }
		public DotCompositeFunctionCallExpressionContext dotCompositeFunctionCallExpression() {
			return getRuleContext(DotCompositeFunctionCallExpressionContext.class,0);
		}
		public WildcardedPathNameContext wildcardedPathName() {
			return getRuleContext(WildcardedPathNameContext.class,0);
		}
		public WildcardedPathExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedPathExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedPathExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedPathExpression(this);
		}
	}

	public final WildcardedPathExpressionContext wildcardedPathExpression() throws RecognitionException {
		WildcardedPathExpressionContext _localctx = new WildcardedPathExpressionContext(_ctx, getState());
		enterRule(_localctx, 488, RULE_wildcardedPathExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2487);
			((WildcardedPathExpressionContext)_localctx).Expression = dotCompositeFunctionCallExpression();
			setState(2488);
			match(DOT);
			setState(2489);
			((WildcardedPathExpressionContext)_localctx).Name = wildcardedPathName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedPathNameContext extends ParserRuleContext {
		public WildcardedNameContext wildcardedName() {
			return getRuleContext(WildcardedNameContext.class,0);
		}
		public EntityNameContext entityName() {
			return getRuleContext(EntityNameContext.class,0);
		}
		public WildcardedPathNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedPathName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedPathName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedPathName(this);
		}
	}

	public final WildcardedPathNameContext wildcardedPathName() throws RecognitionException {
		WildcardedPathNameContext _localctx = new WildcardedPathNameContext(_ctx, getState());
		enterRule(_localctx, 490, RULE_wildcardedPathName);
		try {
			setState(2493);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,221,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2491);
				wildcardedName();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2492);
				entityName();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ContextualDataTableExpressionContext extends ParserRuleContext {
		public Token Id;
		public RowSchemaContext Schema;
		public TerminalNode CONTEXTUAL_DATATABLE() { return getToken(HqlParser.CONTEXTUAL_DATATABLE, 0); }
		public TerminalNode GUIDLITERAL() { return getToken(HqlParser.GUIDLITERAL, 0); }
		public RowSchemaContext rowSchema() {
			return getRuleContext(RowSchemaContext.class,0);
		}
		public ContextualDataTableExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_contextualDataTableExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterContextualDataTableExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitContextualDataTableExpression(this);
		}
	}

	public final ContextualDataTableExpressionContext contextualDataTableExpression() throws RecognitionException {
		ContextualDataTableExpressionContext _localctx = new ContextualDataTableExpressionContext(_ctx, getState());
		enterRule(_localctx, 492, RULE_contextualDataTableExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2495);
			match(CONTEXTUAL_DATATABLE);
			setState(2496);
			((ContextualDataTableExpressionContext)_localctx).Id = match(GUIDLITERAL);
			setState(2497);
			((ContextualDataTableExpressionContext)_localctx).Schema = rowSchema();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DataTableExpressionContext extends ParserRuleContext {
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public RowSchemaContext Schema;
		public LiteralExpressionContext literalExpression;
		public List<LiteralExpressionContext> Values = new ArrayList<LiteralExpressionContext>();
		public TerminalNode DATATABLE() { return getToken(HqlParser.DATATABLE, 0); }
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public RowSchemaContext rowSchema() {
			return getRuleContext(RowSchemaContext.class,0);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public List<LiteralExpressionContext> literalExpression() {
			return getRuleContexts(LiteralExpressionContext.class);
		}
		public LiteralExpressionContext literalExpression(int i) {
			return getRuleContext(LiteralExpressionContext.class,i);
		}
		public DataTableExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dataTableExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDataTableExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDataTableExpression(this);
		}
	}

	public final DataTableExpressionContext dataTableExpression() throws RecognitionException {
		DataTableExpressionContext _localctx = new DataTableExpressionContext(_ctx, getState());
		enterRule(_localctx, 494, RULE_dataTableExpression);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2499);
			match(DATATABLE);
			setState(2503);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(2500);
				((DataTableExpressionContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((DataTableExpressionContext)_localctx).Parameters.add(((DataTableExpressionContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(2505);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2506);
			((DataTableExpressionContext)_localctx).Schema = rowSchema();
			setState(2507);
			match(OPENBRACKET);
			setState(2509);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DASH || _la==PLUS || ((((_la - 285)) & ~0x3f) == 0 && ((1L << (_la - 285)) & 1609564161L) != 0)) {
				{
				setState(2508);
				((DataTableExpressionContext)_localctx).literalExpression = literalExpression();
				((DataTableExpressionContext)_localctx).Values.add(((DataTableExpressionContext)_localctx).literalExpression);
				}
			}

			setState(2515);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,224,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2511);
					match(COMMA);
					setState(2512);
					((DataTableExpressionContext)_localctx).literalExpression = literalExpression();
					((DataTableExpressionContext)_localctx).Values.add(((DataTableExpressionContext)_localctx).literalExpression);
					}
					} 
				}
				setState(2517);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,224,_ctx);
			}
			setState(2519);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(2518);
				match(COMMA);
				}
			}

			setState(2521);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RowSchemaContext extends ParserRuleContext {
		public RowSchemaColumnDeclarationContext rowSchemaColumnDeclaration;
		public List<RowSchemaColumnDeclarationContext> Columns = new ArrayList<RowSchemaColumnDeclarationContext>();
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<RowSchemaColumnDeclarationContext> rowSchemaColumnDeclaration() {
			return getRuleContexts(RowSchemaColumnDeclarationContext.class);
		}
		public RowSchemaColumnDeclarationContext rowSchemaColumnDeclaration(int i) {
			return getRuleContext(RowSchemaColumnDeclarationContext.class,i);
		}
		public RowSchemaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rowSchema; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRowSchema(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRowSchema(this);
		}
	}

	public final RowSchemaContext rowSchema() throws RecognitionException {
		RowSchemaContext _localctx = new RowSchemaContext(_ctx, getState());
		enterRule(_localctx, 496, RULE_rowSchema);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2523);
			match(OPENPAREN);
			setState(2525);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416123978121216L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(2524);
				((RowSchemaContext)_localctx).rowSchemaColumnDeclaration = rowSchemaColumnDeclaration();
				((RowSchemaContext)_localctx).Columns.add(((RowSchemaContext)_localctx).rowSchemaColumnDeclaration);
				}
			}

			setState(2531);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,227,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2527);
					match(COMMA);
					setState(2528);
					((RowSchemaContext)_localctx).rowSchemaColumnDeclaration = rowSchemaColumnDeclaration();
					((RowSchemaContext)_localctx).Columns.add(((RowSchemaContext)_localctx).rowSchemaColumnDeclaration);
					}
					} 
				}
				setState(2533);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,227,_ctx);
			}
			setState(2535);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==COMMA) {
				{
				setState(2534);
				match(COMMA);
				}
			}

			setState(2537);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RowSchemaColumnDeclarationContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public ScalarTypeContext Type;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public ParameterNameContext parameterName() {
			return getRuleContext(ParameterNameContext.class,0);
		}
		public ScalarTypeContext scalarType() {
			return getRuleContext(ScalarTypeContext.class,0);
		}
		public RowSchemaColumnDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_rowSchemaColumnDeclaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRowSchemaColumnDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRowSchemaColumnDeclaration(this);
		}
	}

	public final RowSchemaColumnDeclarationContext rowSchemaColumnDeclaration() throws RecognitionException {
		RowSchemaColumnDeclarationContext _localctx = new RowSchemaColumnDeclarationContext(_ctx, getState());
		enterRule(_localctx, 498, RULE_rowSchemaColumnDeclaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2539);
			((RowSchemaColumnDeclarationContext)_localctx).Name = parameterName();
			setState(2540);
			match(COLON);
			setState(2541);
			((RowSchemaColumnDeclarationContext)_localctx).Type = scalarType();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExternalDataExpressionContext extends ParserRuleContext {
		public Token Keyword;
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter;
		public List<RelaxedQueryOperatorParameterContext> Parameters = new ArrayList<RelaxedQueryOperatorParameterContext>();
		public RowSchemaContext Schema;
		public StringLiteralExpressionContext stringLiteralExpression;
		public List<StringLiteralExpressionContext> ConnectionStrings = new ArrayList<StringLiteralExpressionContext>();
		public ExternalDataWithClauseContext WithClause;
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public RowSchemaContext rowSchema() {
			return getRuleContext(RowSchemaContext.class,0);
		}
		public List<StringLiteralExpressionContext> stringLiteralExpression() {
			return getRuleContexts(StringLiteralExpressionContext.class);
		}
		public StringLiteralExpressionContext stringLiteralExpression(int i) {
			return getRuleContext(StringLiteralExpressionContext.class,i);
		}
		public TerminalNode EXTERNALDATA() { return getToken(HqlParser.EXTERNALDATA, 0); }
		public TerminalNode EXTERNAL_DATA() { return getToken(HqlParser.EXTERNAL_DATA, 0); }
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public List<RelaxedQueryOperatorParameterContext> relaxedQueryOperatorParameter() {
			return getRuleContexts(RelaxedQueryOperatorParameterContext.class);
		}
		public RelaxedQueryOperatorParameterContext relaxedQueryOperatorParameter(int i) {
			return getRuleContext(RelaxedQueryOperatorParameterContext.class,i);
		}
		public ExternalDataWithClauseContext externalDataWithClause() {
			return getRuleContext(ExternalDataWithClauseContext.class,0);
		}
		public ExternalDataExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_externalDataExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExternalDataExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExternalDataExpression(this);
		}
	}

	public final ExternalDataExpressionContext externalDataExpression() throws RecognitionException {
		ExternalDataExpressionContext _localctx = new ExternalDataExpressionContext(_ctx, getState());
		enterRule(_localctx, 500, RULE_externalDataExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2543);
			((ExternalDataExpressionContext)_localctx).Keyword = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==EXTERNALDATA || _la==EXTERNAL_DATA) ) {
				((ExternalDataExpressionContext)_localctx).Keyword = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2547);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (((((_la - 51)) & ~0x3f) == 0 && ((1L << (_la - 51)) & -4611686001243127775L) != 0) || ((((_la - 115)) & ~0x3f) == 0 && ((1L << (_la - 115)) & 5784063L) != 0) || ((((_la - 201)) & ~0x3f) == 0 && ((1L << (_la - 201)) & -1152921503533105151L) != 0) || ((((_la - 266)) & ~0x3f) == 0 && ((1L << (_la - 266)) & 1125899906842627L) != 0)) {
				{
				{
				setState(2544);
				((ExternalDataExpressionContext)_localctx).relaxedQueryOperatorParameter = relaxedQueryOperatorParameter();
				((ExternalDataExpressionContext)_localctx).Parameters.add(((ExternalDataExpressionContext)_localctx).relaxedQueryOperatorParameter);
				}
				}
				setState(2549);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2550);
			((ExternalDataExpressionContext)_localctx).Schema = rowSchema();
			setState(2551);
			match(OPENBRACKET);
			setState(2552);
			((ExternalDataExpressionContext)_localctx).stringLiteralExpression = stringLiteralExpression();
			((ExternalDataExpressionContext)_localctx).ConnectionStrings.add(((ExternalDataExpressionContext)_localctx).stringLiteralExpression);
			setState(2557);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(2553);
				match(COMMA);
				setState(2554);
				((ExternalDataExpressionContext)_localctx).stringLiteralExpression = stringLiteralExpression();
				((ExternalDataExpressionContext)_localctx).ConnectionStrings.add(((ExternalDataExpressionContext)_localctx).stringLiteralExpression);
				}
				}
				setState(2559);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(2560);
			match(CLOSEBRACKET);
			setState(2562);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,231,_ctx) ) {
			case 1:
				{
				setState(2561);
				((ExternalDataExpressionContext)_localctx).WithClause = externalDataWithClause();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExternalDataWithClauseContext extends ParserRuleContext {
		public ExternalDataWithClausePropertyContext externalDataWithClauseProperty;
		public List<ExternalDataWithClausePropertyContext> Properties = new ArrayList<ExternalDataWithClausePropertyContext>();
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public List<ExternalDataWithClausePropertyContext> externalDataWithClauseProperty() {
			return getRuleContexts(ExternalDataWithClausePropertyContext.class);
		}
		public ExternalDataWithClausePropertyContext externalDataWithClauseProperty(int i) {
			return getRuleContext(ExternalDataWithClausePropertyContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public ExternalDataWithClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_externalDataWithClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExternalDataWithClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExternalDataWithClause(this);
		}
	}

	public final ExternalDataWithClauseContext externalDataWithClause() throws RecognitionException {
		ExternalDataWithClauseContext _localctx = new ExternalDataWithClauseContext(_ctx, getState());
		enterRule(_localctx, 502, RULE_externalDataWithClause);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2564);
			match(WITH);
			setState(2565);
			match(OPENPAREN);
			setState(2577);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416123978121216L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(2566);
				((ExternalDataWithClauseContext)_localctx).externalDataWithClauseProperty = externalDataWithClauseProperty();
				((ExternalDataWithClauseContext)_localctx).Properties.add(((ExternalDataWithClauseContext)_localctx).externalDataWithClauseProperty);
				setState(2571);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,232,_ctx);
				while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
					if ( _alt==1 ) {
						{
						{
						setState(2567);
						match(COMMA);
						setState(2568);
						((ExternalDataWithClauseContext)_localctx).externalDataWithClauseProperty = externalDataWithClauseProperty();
						((ExternalDataWithClauseContext)_localctx).Properties.add(((ExternalDataWithClauseContext)_localctx).externalDataWithClauseProperty);
						}
						} 
					}
					setState(2573);
					_errHandler.sync(this);
					_alt = getInterpreter().adaptivePredict(_input,232,_ctx);
				}
				setState(2575);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==COMMA) {
					{
					setState(2574);
					match(COMMA);
					}
				}

				}
			}

			setState(2579);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExternalDataWithClausePropertyContext extends ParserRuleContext {
		public ParameterNameContext Name;
		public StringLiteralExpressionContext StringValue;
		public Token TokenValue;
		public ParameterNameContext NameValue;
		public TerminalNode EQUAL() { return getToken(HqlParser.EQUAL, 0); }
		public List<ParameterNameContext> parameterName() {
			return getRuleContexts(ParameterNameContext.class);
		}
		public ParameterNameContext parameterName(int i) {
			return getRuleContext(ParameterNameContext.class,i);
		}
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public TerminalNode LONGLITERAL() { return getToken(HqlParser.LONGLITERAL, 0); }
		public TerminalNode REALLITERAL() { return getToken(HqlParser.REALLITERAL, 0); }
		public TerminalNode BOOLEANLITERAL() { return getToken(HqlParser.BOOLEANLITERAL, 0); }
		public TerminalNode DATETIMELITERAL() { return getToken(HqlParser.DATETIMELITERAL, 0); }
		public TerminalNode TYPELITERAL() { return getToken(HqlParser.TYPELITERAL, 0); }
		public TerminalNode GUIDLITERAL() { return getToken(HqlParser.GUIDLITERAL, 0); }
		public TerminalNode RAWGUIDLITERAL() { return getToken(HqlParser.RAWGUIDLITERAL, 0); }
		public ExternalDataWithClausePropertyContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_externalDataWithClauseProperty; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExternalDataWithClauseProperty(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExternalDataWithClauseProperty(this);
		}
	}

	public final ExternalDataWithClausePropertyContext externalDataWithClauseProperty() throws RecognitionException {
		ExternalDataWithClausePropertyContext _localctx = new ExternalDataWithClausePropertyContext(_ctx, getState());
		enterRule(_localctx, 504, RULE_externalDataWithClauseProperty);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2581);
			((ExternalDataWithClausePropertyContext)_localctx).Name = parameterName();
			setState(2582);
			match(EQUAL);
			setState(2586);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case STRINGLITERAL:
				{
				setState(2583);
				((ExternalDataWithClausePropertyContext)_localctx).StringValue = stringLiteralExpression();
				}
				break;
			case LONGLITERAL:
			case REALLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TYPELITERAL:
			case RAWGUIDLITERAL:
			case GUIDLITERAL:
				{
				setState(2584);
				((ExternalDataWithClausePropertyContext)_localctx).TokenValue = _input.LT(1);
				_la = _input.LA(1);
				if ( !(((((_la - 305)) & ~0x3f) == 0 && ((1L << (_la - 305)) & 1893L) != 0)) ) {
					((ExternalDataWithClausePropertyContext)_localctx).TokenValue = (Token)_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case OPENBRACKET:
			case ACCESS:
			case ACCUMULATE:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AS:
			case AXES:
			case BASE:
			case BIN:
			case BY:
			case CLUSTER:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATABASE:
			case DATATABLE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case DISTINCT:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case EXTEND:
			case EXTERNALDATA:
			case FACET:
			case FILTER:
			case FIND:
			case FORK:
			case FROM:
			case HAS:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case IN:
			case INTO:
			case INVOKE:
			case LEGEND:
			case LET:
			case LIMIT:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case MATERIALIZE:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case OF:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARSE:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case PRINT:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SERIES:
			case SET:
			case SORT:
			case STACKED:
			case STACKED100:
			case STEP:
			case SUMMARIZE:
			case TAKE:
			case THRESHOLD:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WHERE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
			case IDENTIFIER:
				{
				setState(2585);
				((ExternalDataWithClausePropertyContext)_localctx).NameValue = parameterName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MaterializedViewCombineExpressionContext extends ParserRuleContext {
		public StringLiteralExpressionContext Name;
		public MaterializeViewCombineBaseClauseContext BaseClause;
		public MaterializedViewCombineDeltaClauseContext DeltaClause;
		public MaterializedViewCombineAggregationsClauseContext AggregationsClause;
		public TerminalNode MATERIALIZED_VIEW_COMBINE() { return getToken(HqlParser.MATERIALIZED_VIEW_COMBINE, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public MaterializeViewCombineBaseClauseContext materializeViewCombineBaseClause() {
			return getRuleContext(MaterializeViewCombineBaseClauseContext.class,0);
		}
		public MaterializedViewCombineDeltaClauseContext materializedViewCombineDeltaClause() {
			return getRuleContext(MaterializedViewCombineDeltaClauseContext.class,0);
		}
		public MaterializedViewCombineAggregationsClauseContext materializedViewCombineAggregationsClause() {
			return getRuleContext(MaterializedViewCombineAggregationsClauseContext.class,0);
		}
		public MaterializedViewCombineExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_materializedViewCombineExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMaterializedViewCombineExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMaterializedViewCombineExpression(this);
		}
	}

	public final MaterializedViewCombineExpressionContext materializedViewCombineExpression() throws RecognitionException {
		MaterializedViewCombineExpressionContext _localctx = new MaterializedViewCombineExpressionContext(_ctx, getState());
		enterRule(_localctx, 506, RULE_materializedViewCombineExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2588);
			match(MATERIALIZED_VIEW_COMBINE);
			setState(2589);
			match(OPENPAREN);
			setState(2590);
			((MaterializedViewCombineExpressionContext)_localctx).Name = stringLiteralExpression();
			setState(2591);
			match(CLOSEPAREN);
			setState(2592);
			((MaterializedViewCombineExpressionContext)_localctx).BaseClause = materializeViewCombineBaseClause();
			setState(2593);
			((MaterializedViewCombineExpressionContext)_localctx).DeltaClause = materializedViewCombineDeltaClause();
			setState(2594);
			((MaterializedViewCombineExpressionContext)_localctx).AggregationsClause = materializedViewCombineAggregationsClause();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MaterializeViewCombineBaseClauseContext extends ParserRuleContext {
		public ExpressionContext Expression;
		public TerminalNode BASE() { return getToken(HqlParser.BASE, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public MaterializeViewCombineBaseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_materializeViewCombineBaseClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMaterializeViewCombineBaseClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMaterializeViewCombineBaseClause(this);
		}
	}

	public final MaterializeViewCombineBaseClauseContext materializeViewCombineBaseClause() throws RecognitionException {
		MaterializeViewCombineBaseClauseContext _localctx = new MaterializeViewCombineBaseClauseContext(_ctx, getState());
		enterRule(_localctx, 508, RULE_materializeViewCombineBaseClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2596);
			match(BASE);
			setState(2597);
			match(OPENPAREN);
			setState(2598);
			((MaterializeViewCombineBaseClauseContext)_localctx).Expression = expression();
			setState(2599);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MaterializedViewCombineDeltaClauseContext extends ParserRuleContext {
		public ExpressionContext Expression;
		public TerminalNode DELTA() { return getToken(HqlParser.DELTA, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public MaterializedViewCombineDeltaClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_materializedViewCombineDeltaClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMaterializedViewCombineDeltaClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMaterializedViewCombineDeltaClause(this);
		}
	}

	public final MaterializedViewCombineDeltaClauseContext materializedViewCombineDeltaClause() throws RecognitionException {
		MaterializedViewCombineDeltaClauseContext _localctx = new MaterializedViewCombineDeltaClauseContext(_ctx, getState());
		enterRule(_localctx, 510, RULE_materializedViewCombineDeltaClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2601);
			match(DELTA);
			setState(2602);
			match(OPENPAREN);
			setState(2603);
			((MaterializedViewCombineDeltaClauseContext)_localctx).Expression = expression();
			setState(2604);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MaterializedViewCombineAggregationsClauseContext extends ParserRuleContext {
		public SummarizeOperatorContext Operator;
		public TerminalNode AGGREGATIONS() { return getToken(HqlParser.AGGREGATIONS, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public SummarizeOperatorContext summarizeOperator() {
			return getRuleContext(SummarizeOperatorContext.class,0);
		}
		public MaterializedViewCombineAggregationsClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_materializedViewCombineAggregationsClause; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterMaterializedViewCombineAggregationsClause(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitMaterializedViewCombineAggregationsClause(this);
		}
	}

	public final MaterializedViewCombineAggregationsClauseContext materializedViewCombineAggregationsClause() throws RecognitionException {
		MaterializedViewCombineAggregationsClauseContext _localctx = new MaterializedViewCombineAggregationsClauseContext(_ctx, getState());
		enterRule(_localctx, 512, RULE_materializedViewCombineAggregationsClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2606);
			match(AGGREGATIONS);
			setState(2607);
			match(OPENPAREN);
			setState(2608);
			((MaterializedViewCombineAggregationsClauseContext)_localctx).Operator = summarizeOperator();
			setState(2609);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ScalarTypeContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode BOOL() { return getToken(HqlParser.BOOL, 0); }
		public TerminalNode BOOLEAN() { return getToken(HqlParser.BOOLEAN, 0); }
		public TerminalNode DATE() { return getToken(HqlParser.DATE, 0); }
		public TerminalNode DATETIME() { return getToken(HqlParser.DATETIME, 0); }
		public TerminalNode DECIMAL() { return getToken(HqlParser.DECIMAL, 0); }
		public TerminalNode DOUBLE() { return getToken(HqlParser.DOUBLE, 0); }
		public TerminalNode DYNAMIC() { return getToken(HqlParser.DYNAMIC, 0); }
		public TerminalNode GUID() { return getToken(HqlParser.GUID, 0); }
		public TerminalNode INT() { return getToken(HqlParser.INT, 0); }
		public TerminalNode INT64() { return getToken(HqlParser.INT64, 0); }
		public TerminalNode INT8() { return getToken(HqlParser.INT8, 0); }
		public TerminalNode LONG() { return getToken(HqlParser.LONG, 0); }
		public TerminalNode REAL() { return getToken(HqlParser.REAL, 0); }
		public TerminalNode STRING() { return getToken(HqlParser.STRING, 0); }
		public TerminalNode TIME() { return getToken(HqlParser.TIME, 0); }
		public TerminalNode TIMESPAN() { return getToken(HqlParser.TIMESPAN, 0); }
		public TerminalNode UNIQUEID() { return getToken(HqlParser.UNIQUEID, 0); }
		public ScalarTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_scalarType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterScalarType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitScalarType(this);
		}
	}

	public final ScalarTypeContext scalarType() throws RecognitionException {
		ScalarTypeContext _localctx = new ScalarTypeContext(_ctx, getState());
		enterRule(_localctx, 514, RULE_scalarType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2611);
			((ScalarTypeContext)_localctx).Token = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 279)) & ~0x3f) == 0 && ((1L << (_la - 279)) & 34072447L) != 0)) ) {
				((ScalarTypeContext)_localctx).Token = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExtendedScalarTypeContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode BOOL() { return getToken(HqlParser.BOOL, 0); }
		public TerminalNode BOOLEAN() { return getToken(HqlParser.BOOLEAN, 0); }
		public TerminalNode DATE() { return getToken(HqlParser.DATE, 0); }
		public TerminalNode DATETIME() { return getToken(HqlParser.DATETIME, 0); }
		public TerminalNode DECIMAL() { return getToken(HqlParser.DECIMAL, 0); }
		public TerminalNode DOUBLE() { return getToken(HqlParser.DOUBLE, 0); }
		public TerminalNode DYNAMIC() { return getToken(HqlParser.DYNAMIC, 0); }
		public TerminalNode FLOAT() { return getToken(HqlParser.FLOAT, 0); }
		public TerminalNode GUID() { return getToken(HqlParser.GUID, 0); }
		public TerminalNode INT() { return getToken(HqlParser.INT, 0); }
		public TerminalNode INT16() { return getToken(HqlParser.INT16, 0); }
		public TerminalNode INT32() { return getToken(HqlParser.INT32, 0); }
		public TerminalNode INT64() { return getToken(HqlParser.INT64, 0); }
		public TerminalNode INT8() { return getToken(HqlParser.INT8, 0); }
		public TerminalNode LONG() { return getToken(HqlParser.LONG, 0); }
		public TerminalNode REAL() { return getToken(HqlParser.REAL, 0); }
		public TerminalNode STRING() { return getToken(HqlParser.STRING, 0); }
		public TerminalNode TIME() { return getToken(HqlParser.TIME, 0); }
		public TerminalNode TIMESPAN() { return getToken(HqlParser.TIMESPAN, 0); }
		public TerminalNode UINT() { return getToken(HqlParser.UINT, 0); }
		public TerminalNode UINT16() { return getToken(HqlParser.UINT16, 0); }
		public TerminalNode UINT32() { return getToken(HqlParser.UINT32, 0); }
		public TerminalNode UINT64() { return getToken(HqlParser.UINT64, 0); }
		public TerminalNode UINT8() { return getToken(HqlParser.UINT8, 0); }
		public TerminalNode ULONG() { return getToken(HqlParser.ULONG, 0); }
		public TerminalNode UNIQUEID() { return getToken(HqlParser.UNIQUEID, 0); }
		public ExtendedScalarTypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extendedScalarType; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExtendedScalarType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExtendedScalarType(this);
		}
	}

	public final ExtendedScalarTypeContext extendedScalarType() throws RecognitionException {
		ExtendedScalarTypeContext _localctx = new ExtendedScalarTypeContext(_ctx, getState());
		enterRule(_localctx, 516, RULE_extendedScalarType);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2613);
			((ExtendedScalarTypeContext)_localctx).Token = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 279)) & ~0x3f) == 0 && ((1L << (_la - 279)) & 67108863L) != 0)) ) {
				((ExtendedScalarTypeContext)_localctx).Token = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterNameContext extends ParserRuleContext {
		public IdentifierOrExtendedKeywordOrEscapedNameContext Name;
		public IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrExtendedKeywordOrEscapedNameContext.class,0);
		}
		public ParameterNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterParameterName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitParameterName(this);
		}
	}

	public final ParameterNameContext parameterName() throws RecognitionException {
		ParameterNameContext _localctx = new ParameterNameContext(_ctx, getState());
		enterRule(_localctx, 518, RULE_parameterName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2615);
			((ParameterNameContext)_localctx).Name = identifierOrExtendedKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SimpleNameReferenceContext extends ParserRuleContext {
		public IdentifierOrKeywordOrEscapedNameContext Name;
		public IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrKeywordOrEscapedNameContext.class,0);
		}
		public SimpleNameReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleNameReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSimpleNameReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSimpleNameReference(this);
		}
	}

	public final SimpleNameReferenceContext simpleNameReference() throws RecognitionException {
		SimpleNameReferenceContext _localctx = new SimpleNameReferenceContext(_ctx, getState());
		enterRule(_localctx, 520, RULE_simpleNameReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2617);
			((SimpleNameReferenceContext)_localctx).Name = identifierOrKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExtendedNameReferenceContext extends ParserRuleContext {
		public IdentifierOrExtendedKeywordOrEscapedNameContext Name;
		public IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName() {
			return getRuleContext(IdentifierOrExtendedKeywordOrEscapedNameContext.class,0);
		}
		public ExtendedNameReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extendedNameReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExtendedNameReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExtendedNameReference(this);
		}
	}

	public final ExtendedNameReferenceContext extendedNameReference() throws RecognitionException {
		ExtendedNameReferenceContext _localctx = new ExtendedNameReferenceContext(_ctx, getState());
		enterRule(_localctx, 522, RULE_extendedNameReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2619);
			((ExtendedNameReferenceContext)_localctx).Name = identifierOrExtendedKeywordOrEscapedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedNameReferenceContext extends ParserRuleContext {
		public WildcardedNameContext Name;
		public WildcardedNameContext wildcardedName() {
			return getRuleContext(WildcardedNameContext.class,0);
		}
		public WildcardedNameReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedNameReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedNameReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedNameReference(this);
		}
	}

	public final WildcardedNameReferenceContext wildcardedNameReference() throws RecognitionException {
		WildcardedNameReferenceContext _localctx = new WildcardedNameReferenceContext(_ctx, getState());
		enterRule(_localctx, 524, RULE_wildcardedNameReference);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2621);
			((WildcardedNameReferenceContext)_localctx).Name = wildcardedName();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SimpleOrWildcardedNameReferenceContext extends ParserRuleContext {
		public SimpleNameReferenceContext SimpleName;
		public WildcardedNameReferenceContext WildcardedName;
		public SimpleNameReferenceContext simpleNameReference() {
			return getRuleContext(SimpleNameReferenceContext.class,0);
		}
		public WildcardedNameReferenceContext wildcardedNameReference() {
			return getRuleContext(WildcardedNameReferenceContext.class,0);
		}
		public SimpleOrWildcardedNameReferenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_simpleOrWildcardedNameReference; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSimpleOrWildcardedNameReference(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSimpleOrWildcardedNameReference(this);
		}
	}

	public final SimpleOrWildcardedNameReferenceContext simpleOrWildcardedNameReference() throws RecognitionException {
		SimpleOrWildcardedNameReferenceContext _localctx = new SimpleOrWildcardedNameReferenceContext(_ctx, getState());
		enterRule(_localctx, 526, RULE_simpleOrWildcardedNameReference);
		try {
			setState(2625);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,236,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2623);
				((SimpleOrWildcardedNameReferenceContext)_localctx).SimpleName = simpleNameReference();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2624);
				((SimpleOrWildcardedNameReferenceContext)_localctx).WildcardedName = wildcardedNameReference();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierNameContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public IdentifierNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterIdentifierName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitIdentifierName(this);
		}
	}

	public final IdentifierNameContext identifierName() throws RecognitionException {
		IdentifierNameContext _localctx = new IdentifierNameContext(_ctx, getState());
		enterRule(_localctx, 528, RULE_identifierName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2627);
			((IdentifierNameContext)_localctx).Token = match(IDENTIFIER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class KeywordNameContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode ACCESS() { return getToken(HqlParser.ACCESS, 0); }
		public TerminalNode AGGREGATIONS() { return getToken(HqlParser.AGGREGATIONS, 0); }
		public TerminalNode ALIAS() { return getToken(HqlParser.ALIAS, 0); }
		public TerminalNode ALL() { return getToken(HqlParser.ALL, 0); }
		public TerminalNode AXES() { return getToken(HqlParser.AXES, 0); }
		public TerminalNode BASE() { return getToken(HqlParser.BASE, 0); }
		public TerminalNode BIN() { return getToken(HqlParser.BIN, 0); }
		public TerminalNode BOOL() { return getToken(HqlParser.BOOL, 0); }
		public TerminalNode CLUSTER() { return getToken(HqlParser.CLUSTER, 0); }
		public TerminalNode DATABASE() { return getToken(HqlParser.DATABASE, 0); }
		public TerminalNode DECLARE() { return getToken(HqlParser.DECLARE, 0); }
		public TerminalNode DEFAULT() { return getToken(HqlParser.DEFAULT, 0); }
		public TerminalNode DELTA() { return getToken(HqlParser.DELTA, 0); }
		public TerminalNode EDGES() { return getToken(HqlParser.EDGES, 0); }
		public TerminalNode EVALUATE() { return getToken(HqlParser.EVALUATE, 0); }
		public TerminalNode EXECUTE() { return getToken(HqlParser.EXECUTE, 0); }
		public TerminalNode FACET() { return getToken(HqlParser.FACET, 0); }
		public TerminalNode FORK() { return getToken(HqlParser.FORK, 0); }
		public TerminalNode FROM() { return getToken(HqlParser.FROM, 0); }
		public TerminalNode GUID() { return getToken(HqlParser.GUID, 0); }
		public TerminalNode HIDDEN_() { return getToken(HqlParser.HIDDEN_, 0); }
		public TerminalNode HOT() { return getToken(HqlParser.HOT, 0); }
		public TerminalNode HOTDATA() { return getToken(HqlParser.HOTDATA, 0); }
		public TerminalNode HOTINDEX() { return getToken(HqlParser.HOTINDEX, 0); }
		public TerminalNode ID() { return getToken(HqlParser.ID, 0); }
		public TerminalNode INTO() { return getToken(HqlParser.INTO, 0); }
		public TerminalNode LEGEND() { return getToken(HqlParser.LEGEND, 0); }
		public TerminalNode LET() { return getToken(HqlParser.LET, 0); }
		public TerminalNode LINEAR() { return getToken(HqlParser.LINEAR, 0); }
		public TerminalNode LOG() { return getToken(HqlParser.LOG, 0); }
		public TerminalNode LOOKUP() { return getToken(HqlParser.LOOKUP, 0); }
		public TerminalNode LIST() { return getToken(HqlParser.LIST, 0); }
		public TerminalNode MAP() { return getToken(HqlParser.MAP, 0); }
		public TerminalNode NODES() { return getToken(HqlParser.NODES, 0); }
		public TerminalNode NONE() { return getToken(HqlParser.NONE, 0); }
		public TerminalNode NULL() { return getToken(HqlParser.NULL, 0); }
		public TerminalNode NULLS() { return getToken(HqlParser.NULLS, 0); }
		public TerminalNode ON() { return getToken(HqlParser.ON, 0); }
		public TerminalNode OPTIONAL() { return getToken(HqlParser.OPTIONAL, 0); }
		public TerminalNode OUTPUT() { return getToken(HqlParser.OUTPUT, 0); }
		public TerminalNode PACK() { return getToken(HqlParser.PACK, 0); }
		public TerminalNode PARTITION() { return getToken(HqlParser.PARTITION, 0); }
		public TerminalNode PARTITIONBY() { return getToken(HqlParser.PARTITIONBY, 0); }
		public TerminalNode PATTERN() { return getToken(HqlParser.PATTERN, 0); }
		public TerminalNode PLUGIN() { return getToken(HqlParser.PLUGIN, 0); }
		public TerminalNode QUERYPARAMETERS() { return getToken(HqlParser.QUERYPARAMETERS, 0); }
		public TerminalNode RANGE() { return getToken(HqlParser.RANGE, 0); }
		public TerminalNode REDUCE() { return getToken(HqlParser.REDUCE, 0); }
		public TerminalNode REPLACE() { return getToken(HqlParser.REPLACE, 0); }
		public TerminalNode RENDER() { return getToken(HqlParser.RENDER, 0); }
		public TerminalNode RESTRICT() { return getToken(HqlParser.RESTRICT, 0); }
		public TerminalNode SERIES() { return getToken(HqlParser.SERIES, 0); }
		public TerminalNode STACKED() { return getToken(HqlParser.STACKED, 0); }
		public TerminalNode STACKED100() { return getToken(HqlParser.STACKED100, 0); }
		public TerminalNode STEP() { return getToken(HqlParser.STEP, 0); }
		public TerminalNode THRESHOLD() { return getToken(HqlParser.THRESHOLD, 0); }
		public TerminalNode TYPEOF() { return getToken(HqlParser.TYPEOF, 0); }
		public TerminalNode UNSTACKED() { return getToken(HqlParser.UNSTACKED, 0); }
		public TerminalNode UUID() { return getToken(HqlParser.UUID, 0); }
		public TerminalNode VIEW() { return getToken(HqlParser.VIEW, 0); }
		public TerminalNode VISIBLE() { return getToken(HqlParser.VISIBLE, 0); }
		public TerminalNode WITH() { return getToken(HqlParser.WITH, 0); }
		public TerminalNode XAXIS() { return getToken(HqlParser.XAXIS, 0); }
		public TerminalNode XCOLUMN() { return getToken(HqlParser.XCOLUMN, 0); }
		public TerminalNode XMAX() { return getToken(HqlParser.XMAX, 0); }
		public TerminalNode XMIN() { return getToken(HqlParser.XMIN, 0); }
		public TerminalNode XTITLE() { return getToken(HqlParser.XTITLE, 0); }
		public TerminalNode YAXIS() { return getToken(HqlParser.YAXIS, 0); }
		public TerminalNode YCOLUMNS() { return getToken(HqlParser.YCOLUMNS, 0); }
		public TerminalNode YMAX() { return getToken(HqlParser.YMAX, 0); }
		public TerminalNode YMIN() { return getToken(HqlParser.YMIN, 0); }
		public TerminalNode YTITLE() { return getToken(HqlParser.YTITLE, 0); }
		public TerminalNode YSPLIT() { return getToken(HqlParser.YSPLIT, 0); }
		public KeywordNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_keywordName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterKeywordName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitKeywordName(this);
		}
	}

	public final KeywordNameContext keywordName() throws RecognitionException {
		KeywordNameContext _localctx = new KeywordNameContext(_ctx, getState());
		enterRule(_localctx, 530, RULE_keywordName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2629);
			((KeywordNameContext)_localctx).Token = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 38)) & ~0x3f) == 0 && ((1L << (_la - 38)) & 218478683485278237L) != 0) || ((((_la - 112)) & ~0x3f) == 0 && ((1L << (_la - 112)) & 1691298798096385L) != 0) || ((((_la - 183)) & ~0x3f) == 0 && ((1L << (_la - 183)) & 307951464744141595L) != 0) || ((((_la - 253)) & ~0x3f) == 0 && ((1L << (_la - 253)) & 17314054333L) != 0)) ) {
				((KeywordNameContext)_localctx).Token = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExtendedKeywordNameContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode ACCUMULATE() { return getToken(HqlParser.ACCUMULATE, 0); }
		public TerminalNode AS() { return getToken(HqlParser.AS, 0); }
		public TerminalNode BY() { return getToken(HqlParser.BY, 0); }
		public TerminalNode CONTAINS() { return getToken(HqlParser.CONTAINS, 0); }
		public TerminalNode CONSUME() { return getToken(HqlParser.CONSUME, 0); }
		public TerminalNode COUNT() { return getToken(HqlParser.COUNT, 0); }
		public TerminalNode DATATABLE() { return getToken(HqlParser.DATATABLE, 0); }
		public TerminalNode DISTINCT() { return getToken(HqlParser.DISTINCT, 0); }
		public TerminalNode EXTEND() { return getToken(HqlParser.EXTEND, 0); }
		public TerminalNode EXTERNALDATA() { return getToken(HqlParser.EXTERNALDATA, 0); }
		public TerminalNode FIND() { return getToken(HqlParser.FIND, 0); }
		public TerminalNode FILTER() { return getToken(HqlParser.FILTER, 0); }
		public TerminalNode HAS() { return getToken(HqlParser.HAS, 0); }
		public TerminalNode IN() { return getToken(HqlParser.IN, 0); }
		public TerminalNode INVOKE() { return getToken(HqlParser.INVOKE, 0); }
		public TerminalNode LIMIT() { return getToken(HqlParser.LIMIT, 0); }
		public TerminalNode MATERIALIZE() { return getToken(HqlParser.MATERIALIZE, 0); }
		public TerminalNode OF() { return getToken(HqlParser.OF, 0); }
		public TerminalNode PARSE() { return getToken(HqlParser.PARSE, 0); }
		public TerminalNode PRINT() { return getToken(HqlParser.PRINT, 0); }
		public TerminalNode SAMPLE() { return getToken(HqlParser.SAMPLE, 0); }
		public TerminalNode SAMPLE_DISTINCT() { return getToken(HqlParser.SAMPLE_DISTINCT, 0); }
		public TerminalNode SCAN() { return getToken(HqlParser.SCAN, 0); }
		public TerminalNode SEARCH() { return getToken(HqlParser.SEARCH, 0); }
		public TerminalNode SERIALIZE() { return getToken(HqlParser.SERIALIZE, 0); }
		public TerminalNode SET() { return getToken(HqlParser.SET, 0); }
		public TerminalNode SORT() { return getToken(HqlParser.SORT, 0); }
		public TerminalNode SUMMARIZE() { return getToken(HqlParser.SUMMARIZE, 0); }
		public TerminalNode TAKE() { return getToken(HqlParser.TAKE, 0); }
		public TerminalNode TITLE() { return getToken(HqlParser.TITLE, 0); }
		public TerminalNode TO() { return getToken(HqlParser.TO, 0); }
		public TerminalNode TOP() { return getToken(HqlParser.TOP, 0); }
		public TerminalNode TOSCALAR() { return getToken(HqlParser.TOSCALAR, 0); }
		public TerminalNode TOTABLE() { return getToken(HqlParser.TOTABLE, 0); }
		public TerminalNode TOP_NESTED() { return getToken(HqlParser.TOP_NESTED, 0); }
		public TerminalNode TOP_HITTERS() { return getToken(HqlParser.TOP_HITTERS, 0); }
		public TerminalNode WHERE() { return getToken(HqlParser.WHERE, 0); }
		public ExtendedKeywordNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_extendedKeywordName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterExtendedKeywordName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitExtendedKeywordName(this);
		}
	}

	public final ExtendedKeywordNameContext extendedKeywordName() throws RecognitionException {
		ExtendedKeywordNameContext _localctx = new ExtendedKeywordNameContext(_ctx, getState());
		enterRule(_localctx, 532, RULE_extendedKeywordName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2631);
			((ExtendedKeywordNameContext)_localctx).Token = _input.LT(1);
			_la = _input.LA(1);
			if ( !(((((_la - 39)) & ~0x3f) == 0 && ((1L << (_la - 39)) & 7177891226059009L) != 0) || ((((_la - 104)) & ~0x3f) == 0 && ((1L << (_la - 104)) & 2252899929292801L) != 0) || ((((_la - 185)) & ~0x3f) == 0 && ((1L << (_la - 185)) & -1107837748295761407L) != 0) || ((((_la - 249)) & ~0x3f) == 0 && ((1L << (_la - 249)) & 1031L) != 0)) ) {
				((ExtendedKeywordNameContext)_localctx).Token = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EscapedNameContext extends ParserRuleContext {
		public StringLiteralExpressionContext StringLiteral;
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public EscapedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_escapedName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterEscapedName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitEscapedName(this);
		}
	}

	public final EscapedNameContext escapedName() throws RecognitionException {
		EscapedNameContext _localctx = new EscapedNameContext(_ctx, getState());
		enterRule(_localctx, 534, RULE_escapedName);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2633);
			match(OPENBRACKET);
			setState(2634);
			((EscapedNameContext)_localctx).StringLiteral = stringLiteralExpression();
			setState(2635);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierOrKeywordNameContext extends ParserRuleContext {
		public IdentifierNameContext Identifier;
		public KeywordNameContext Keyword;
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public KeywordNameContext keywordName() {
			return getRuleContext(KeywordNameContext.class,0);
		}
		public IdentifierOrKeywordNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierOrKeywordName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterIdentifierOrKeywordName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitIdentifierOrKeywordName(this);
		}
	}

	public final IdentifierOrKeywordNameContext identifierOrKeywordName() throws RecognitionException {
		IdentifierOrKeywordNameContext _localctx = new IdentifierOrKeywordNameContext(_ctx, getState());
		enterRule(_localctx, 536, RULE_identifierOrKeywordName);
		try {
			setState(2639);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2637);
				((IdentifierOrKeywordNameContext)_localctx).Identifier = identifierName();
				}
				break;
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
				enterOuterAlt(_localctx, 2);
				{
				setState(2638);
				((IdentifierOrKeywordNameContext)_localctx).Keyword = keywordName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierOrKeywordOrEscapedNameContext extends ParserRuleContext {
		public IdentifierNameContext Identifier;
		public KeywordNameContext Keyword;
		public EscapedNameContext Escaped;
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public KeywordNameContext keywordName() {
			return getRuleContext(KeywordNameContext.class,0);
		}
		public EscapedNameContext escapedName() {
			return getRuleContext(EscapedNameContext.class,0);
		}
		public IdentifierOrKeywordOrEscapedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierOrKeywordOrEscapedName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterIdentifierOrKeywordOrEscapedName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitIdentifierOrKeywordOrEscapedName(this);
		}
	}

	public final IdentifierOrKeywordOrEscapedNameContext identifierOrKeywordOrEscapedName() throws RecognitionException {
		IdentifierOrKeywordOrEscapedNameContext _localctx = new IdentifierOrKeywordOrEscapedNameContext(_ctx, getState());
		enterRule(_localctx, 538, RULE_identifierOrKeywordOrEscapedName);
		try {
			setState(2644);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2641);
				((IdentifierOrKeywordOrEscapedNameContext)_localctx).Identifier = identifierName();
				}
				break;
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
				enterOuterAlt(_localctx, 2);
				{
				setState(2642);
				((IdentifierOrKeywordOrEscapedNameContext)_localctx).Keyword = keywordName();
				}
				break;
			case OPENBRACKET:
				enterOuterAlt(_localctx, 3);
				{
				setState(2643);
				((IdentifierOrKeywordOrEscapedNameContext)_localctx).Escaped = escapedName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierOrExtendedKeywordOrEscapedNameContext extends ParserRuleContext {
		public IdentifierNameContext Identifier;
		public KeywordNameContext Keyword;
		public ExtendedKeywordNameContext ExtendedKeyword;
		public EscapedNameContext Escaped;
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public KeywordNameContext keywordName() {
			return getRuleContext(KeywordNameContext.class,0);
		}
		public ExtendedKeywordNameContext extendedKeywordName() {
			return getRuleContext(ExtendedKeywordNameContext.class,0);
		}
		public EscapedNameContext escapedName() {
			return getRuleContext(EscapedNameContext.class,0);
		}
		public IdentifierOrExtendedKeywordOrEscapedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierOrExtendedKeywordOrEscapedName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterIdentifierOrExtendedKeywordOrEscapedName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitIdentifierOrExtendedKeywordOrEscapedName(this);
		}
	}

	public final IdentifierOrExtendedKeywordOrEscapedNameContext identifierOrExtendedKeywordOrEscapedName() throws RecognitionException {
		IdentifierOrExtendedKeywordOrEscapedNameContext _localctx = new IdentifierOrExtendedKeywordOrEscapedNameContext(_ctx, getState());
		enterRule(_localctx, 540, RULE_identifierOrExtendedKeywordOrEscapedName);
		try {
			setState(2650);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2646);
				((IdentifierOrExtendedKeywordOrEscapedNameContext)_localctx).Identifier = identifierName();
				}
				break;
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
				enterOuterAlt(_localctx, 2);
				{
				setState(2647);
				((IdentifierOrExtendedKeywordOrEscapedNameContext)_localctx).Keyword = keywordName();
				}
				break;
			case ACCUMULATE:
			case AS:
			case BY:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATATABLE:
			case DISTINCT:
			case EXTEND:
			case EXTERNALDATA:
			case FILTER:
			case FIND:
			case HAS:
			case IN:
			case INVOKE:
			case LIMIT:
			case MATERIALIZE:
			case OF:
			case PARSE:
			case PRINT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SET:
			case SORT:
			case SUMMARIZE:
			case TAKE:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case WHERE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2648);
				((IdentifierOrExtendedKeywordOrEscapedNameContext)_localctx).ExtendedKeyword = extendedKeywordName();
				}
				break;
			case OPENBRACKET:
				enterOuterAlt(_localctx, 4);
				{
				setState(2649);
				((IdentifierOrExtendedKeywordOrEscapedNameContext)_localctx).Escaped = escapedName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IdentifierOrExtendedKeywordNameContext extends ParserRuleContext {
		public IdentifierNameContext Identifier;
		public KeywordNameContext Keyword;
		public ExtendedKeywordNameContext ExtendedKeyword;
		public IdentifierNameContext identifierName() {
			return getRuleContext(IdentifierNameContext.class,0);
		}
		public KeywordNameContext keywordName() {
			return getRuleContext(KeywordNameContext.class,0);
		}
		public ExtendedKeywordNameContext extendedKeywordName() {
			return getRuleContext(ExtendedKeywordNameContext.class,0);
		}
		public IdentifierOrExtendedKeywordNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_identifierOrExtendedKeywordName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterIdentifierOrExtendedKeywordName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitIdentifierOrExtendedKeywordName(this);
		}
	}

	public final IdentifierOrExtendedKeywordNameContext identifierOrExtendedKeywordName() throws RecognitionException {
		IdentifierOrExtendedKeywordNameContext _localctx = new IdentifierOrExtendedKeywordNameContext(_ctx, getState());
		enterRule(_localctx, 542, RULE_identifierOrExtendedKeywordName);
		try {
			setState(2655);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2652);
				((IdentifierOrExtendedKeywordNameContext)_localctx).Identifier = identifierName();
				}
				break;
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
				enterOuterAlt(_localctx, 2);
				{
				setState(2653);
				((IdentifierOrExtendedKeywordNameContext)_localctx).Keyword = keywordName();
				}
				break;
			case ACCUMULATE:
			case AS:
			case BY:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATATABLE:
			case DISTINCT:
			case EXTEND:
			case EXTERNALDATA:
			case FILTER:
			case FIND:
			case HAS:
			case IN:
			case INVOKE:
			case LIMIT:
			case MATERIALIZE:
			case OF:
			case PARSE:
			case PRINT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SET:
			case SORT:
			case SUMMARIZE:
			case TAKE:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case WHERE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2654);
				((IdentifierOrExtendedKeywordNameContext)_localctx).ExtendedKeyword = extendedKeywordName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedNameContext extends ParserRuleContext {
		public WildcardedNamePrefixContext Prefix;
		public WildcardedNameSegmentContext wildcardedNameSegment;
		public List<WildcardedNameSegmentContext> Segments = new ArrayList<WildcardedNameSegmentContext>();
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public WildcardedNamePrefixContext wildcardedNamePrefix() {
			return getRuleContext(WildcardedNamePrefixContext.class,0);
		}
		public List<WildcardedNameSegmentContext> wildcardedNameSegment() {
			return getRuleContexts(WildcardedNameSegmentContext.class);
		}
		public WildcardedNameSegmentContext wildcardedNameSegment(int i) {
			return getRuleContext(WildcardedNameSegmentContext.class,i);
		}
		public WildcardedNameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedName; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedName(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedName(this);
		}
	}

	public final WildcardedNameContext wildcardedName() throws RecognitionException {
		WildcardedNameContext _localctx = new WildcardedNameContext(_ctx, getState());
		enterRule(_localctx, 544, RULE_wildcardedName);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2658);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416122904379392L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288230376692775943L) != 0)) {
				{
				setState(2657);
				((WildcardedNameContext)_localctx).Prefix = wildcardedNamePrefix();
				}
			}

			setState(2660);
			match(ASTERISK);
			setState(2664);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 7684416122904379394L) != 0) || ((((_la - 66)) & ~0x3f) == 0 && ((1L << (_la - 66)) & 8358751552889101161L) != 0) || ((((_la - 130)) & ~0x3f) == 0 && ((1L << (_la - 130)) & 7196752211023416333L) != 0) || ((((_la - 194)) & ~0x3f) == 0 && ((1L << (_la - 194)) & -1443165259434554279L) != 0) || ((((_la - 258)) & ~0x3f) == 0 && ((1L << (_la - 258)) & 288371114181131271L) != 0)) {
				{
				{
				setState(2661);
				((WildcardedNameContext)_localctx).wildcardedNameSegment = wildcardedNameSegment();
				((WildcardedNameContext)_localctx).Segments.add(((WildcardedNameContext)_localctx).wildcardedNameSegment);
				}
				}
				setState(2666);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedNamePrefixContext extends ParserRuleContext {
		public Token Identifier;
		public KeywordNameContext Keyword;
		public ExtendedKeywordNameContext ExtendedKeyword;
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public KeywordNameContext keywordName() {
			return getRuleContext(KeywordNameContext.class,0);
		}
		public ExtendedKeywordNameContext extendedKeywordName() {
			return getRuleContext(ExtendedKeywordNameContext.class,0);
		}
		public WildcardedNamePrefixContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedNamePrefix; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedNamePrefix(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedNamePrefix(this);
		}
	}

	public final WildcardedNamePrefixContext wildcardedNamePrefix() throws RecognitionException {
		WildcardedNamePrefixContext _localctx = new WildcardedNamePrefixContext(_ctx, getState());
		enterRule(_localctx, 546, RULE_wildcardedNamePrefix);
		try {
			setState(2670);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2667);
				((WildcardedNamePrefixContext)_localctx).Identifier = match(IDENTIFIER);
				}
				break;
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
				enterOuterAlt(_localctx, 2);
				{
				setState(2668);
				((WildcardedNamePrefixContext)_localctx).Keyword = keywordName();
				}
				break;
			case ACCUMULATE:
			case AS:
			case BY:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATATABLE:
			case DISTINCT:
			case EXTEND:
			case EXTERNALDATA:
			case FILTER:
			case FIND:
			case HAS:
			case IN:
			case INVOKE:
			case LIMIT:
			case MATERIALIZE:
			case OF:
			case PARSE:
			case PRINT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SET:
			case SORT:
			case SUMMARIZE:
			case TAKE:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case WHERE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2669);
				((WildcardedNamePrefixContext)_localctx).ExtendedKeyword = extendedKeywordName();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WildcardedNameSegmentContext extends ParserRuleContext {
		public Token Identifier;
		public KeywordNameContext Keyword;
		public ExtendedKeywordNameContext ExtendedKeyword;
		public Token Number;
		public Token Star;
		public TerminalNode IDENTIFIER() { return getToken(HqlParser.IDENTIFIER, 0); }
		public KeywordNameContext keywordName() {
			return getRuleContext(KeywordNameContext.class,0);
		}
		public ExtendedKeywordNameContext extendedKeywordName() {
			return getRuleContext(ExtendedKeywordNameContext.class,0);
		}
		public TerminalNode LONGLITERAL() { return getToken(HqlParser.LONGLITERAL, 0); }
		public TerminalNode ASTERISK() { return getToken(HqlParser.ASTERISK, 0); }
		public WildcardedNameSegmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_wildcardedNameSegment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterWildcardedNameSegment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitWildcardedNameSegment(this);
		}
	}

	public final WildcardedNameSegmentContext wildcardedNameSegment() throws RecognitionException {
		WildcardedNameSegmentContext _localctx = new WildcardedNameSegmentContext(_ctx, getState());
		enterRule(_localctx, 548, RULE_wildcardedNameSegment);
		try {
			setState(2677);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IDENTIFIER:
				enterOuterAlt(_localctx, 1);
				{
				setState(2672);
				((WildcardedNameSegmentContext)_localctx).Identifier = match(IDENTIFIER);
				}
				break;
			case ACCESS:
			case AGGREGATIONS:
			case ALIAS:
			case ALL:
			case AXES:
			case BASE:
			case BIN:
			case CLUSTER:
			case DATABASE:
			case DECLARE:
			case DEFAULT:
			case DELTA:
			case EDGES:
			case EVALUATE:
			case EXECUTE:
			case FACET:
			case FORK:
			case FROM:
			case HIDDEN_:
			case HOT:
			case HOTDATA:
			case HOTINDEX:
			case ID:
			case INTO:
			case LEGEND:
			case LET:
			case LINEAR:
			case LIST:
			case LOOKUP:
			case LOG:
			case MAP:
			case NODES:
			case NONE:
			case NULL:
			case NULLS:
			case ON:
			case OPTIONAL:
			case OUTPUT:
			case PACK:
			case PARTITION:
			case PARTITIONBY:
			case PATTERN:
			case PLUGIN:
			case QUERYPARAMETERS:
			case RANGE:
			case REDUCE:
			case RENDER:
			case REPLACE:
			case RESTRICT:
			case SERIES:
			case STACKED:
			case STACKED100:
			case STEP:
			case THRESHOLD:
			case TYPEOF:
			case UNSTACKED:
			case UUID:
			case VIEW:
			case VISIBLE:
			case WITH:
			case XAXIS:
			case XCOLUMN:
			case XMAX:
			case XMIN:
			case XTITLE:
			case YAXIS:
			case YCOLUMNS:
			case YMAX:
			case YMIN:
			case YSPLIT:
			case YTITLE:
			case BOOL:
			case GUID:
				enterOuterAlt(_localctx, 2);
				{
				setState(2673);
				((WildcardedNameSegmentContext)_localctx).Keyword = keywordName();
				}
				break;
			case ACCUMULATE:
			case AS:
			case BY:
			case CONSUME:
			case CONTAINS:
			case COUNT:
			case DATATABLE:
			case DISTINCT:
			case EXTEND:
			case EXTERNALDATA:
			case FILTER:
			case FIND:
			case HAS:
			case IN:
			case INVOKE:
			case LIMIT:
			case MATERIALIZE:
			case OF:
			case PARSE:
			case PRINT:
			case SAMPLE:
			case SAMPLE_DISTINCT:
			case SCAN:
			case SEARCH:
			case SERIALIZE:
			case SET:
			case SORT:
			case SUMMARIZE:
			case TAKE:
			case TITLE:
			case TO:
			case TOP:
			case TOP_HITTERS:
			case TOP_NESTED:
			case TOSCALAR:
			case TOTABLE:
			case WHERE:
				enterOuterAlt(_localctx, 3);
				{
				setState(2674);
				((WildcardedNameSegmentContext)_localctx).ExtendedKeyword = extendedKeywordName();
				}
				break;
			case LONGLITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(2675);
				((WildcardedNameSegmentContext)_localctx).Number = match(LONGLITERAL);
				}
				break;
			case ASTERISK:
				enterOuterAlt(_localctx, 5);
				{
				setState(2676);
				((WildcardedNameSegmentContext)_localctx).Star = match(ASTERISK);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LiteralExpressionContext extends ParserRuleContext {
		public SignedLiteralExpressionContext Signed;
		public UnsignedLiteralExpressionContext Unsigned;
		public SignedLiteralExpressionContext signedLiteralExpression() {
			return getRuleContext(SignedLiteralExpressionContext.class,0);
		}
		public UnsignedLiteralExpressionContext unsignedLiteralExpression() {
			return getRuleContext(UnsignedLiteralExpressionContext.class,0);
		}
		public LiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_literalExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLiteralExpression(this);
		}
	}

	public final LiteralExpressionContext literalExpression() throws RecognitionException {
		LiteralExpressionContext _localctx = new LiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 550, RULE_literalExpression);
		try {
			setState(2681);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case DASH:
			case PLUS:
				enterOuterAlt(_localctx, 1);
				{
				setState(2679);
				((LiteralExpressionContext)_localctx).Signed = signedLiteralExpression();
				}
				break;
			case DYNAMIC:
			case LONGLITERAL:
			case INTLITERAL:
			case REALLITERAL:
			case DECIMALLITERAL:
			case STRINGLITERAL:
			case BOOLEANLITERAL:
			case DATETIMELITERAL:
			case TIMESPANLITERAL:
			case TYPELITERAL:
			case GUIDLITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(2680);
				((LiteralExpressionContext)_localctx).Unsigned = unsignedLiteralExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnsignedLiteralExpressionContext extends ParserRuleContext {
		public LongLiteralExpressionContext Long;
		public IntLiteralExpressionContext Int;
		public RealLiteralExpressionContext Real;
		public DecimalLiteralExpressionContext Decimal;
		public DateTimeLiteralExpressionContext DateTime;
		public TimeSpanLiteralExpressionContext TimeSpan;
		public BooleanLiteralExpressionContext Boolean;
		public GuidLiteralExpressionContext Guid;
		public TypeLiteralExpressionContext Type;
		public StringLiteralExpressionContext String;
		public DynamicLiteralExpressionContext Dynamic;
		public LongLiteralExpressionContext longLiteralExpression() {
			return getRuleContext(LongLiteralExpressionContext.class,0);
		}
		public IntLiteralExpressionContext intLiteralExpression() {
			return getRuleContext(IntLiteralExpressionContext.class,0);
		}
		public RealLiteralExpressionContext realLiteralExpression() {
			return getRuleContext(RealLiteralExpressionContext.class,0);
		}
		public DecimalLiteralExpressionContext decimalLiteralExpression() {
			return getRuleContext(DecimalLiteralExpressionContext.class,0);
		}
		public DateTimeLiteralExpressionContext dateTimeLiteralExpression() {
			return getRuleContext(DateTimeLiteralExpressionContext.class,0);
		}
		public TimeSpanLiteralExpressionContext timeSpanLiteralExpression() {
			return getRuleContext(TimeSpanLiteralExpressionContext.class,0);
		}
		public BooleanLiteralExpressionContext booleanLiteralExpression() {
			return getRuleContext(BooleanLiteralExpressionContext.class,0);
		}
		public GuidLiteralExpressionContext guidLiteralExpression() {
			return getRuleContext(GuidLiteralExpressionContext.class,0);
		}
		public TypeLiteralExpressionContext typeLiteralExpression() {
			return getRuleContext(TypeLiteralExpressionContext.class,0);
		}
		public StringLiteralExpressionContext stringLiteralExpression() {
			return getRuleContext(StringLiteralExpressionContext.class,0);
		}
		public DynamicLiteralExpressionContext dynamicLiteralExpression() {
			return getRuleContext(DynamicLiteralExpressionContext.class,0);
		}
		public UnsignedLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unsignedLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterUnsignedLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitUnsignedLiteralExpression(this);
		}
	}

	public final UnsignedLiteralExpressionContext unsignedLiteralExpression() throws RecognitionException {
		UnsignedLiteralExpressionContext _localctx = new UnsignedLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 552, RULE_unsignedLiteralExpression);
		try {
			setState(2694);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LONGLITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(2683);
				((UnsignedLiteralExpressionContext)_localctx).Long = longLiteralExpression();
				}
				break;
			case INTLITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(2684);
				((UnsignedLiteralExpressionContext)_localctx).Int = intLiteralExpression();
				}
				break;
			case REALLITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(2685);
				((UnsignedLiteralExpressionContext)_localctx).Real = realLiteralExpression();
				}
				break;
			case DECIMALLITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(2686);
				((UnsignedLiteralExpressionContext)_localctx).Decimal = decimalLiteralExpression();
				}
				break;
			case DATETIMELITERAL:
				enterOuterAlt(_localctx, 5);
				{
				setState(2687);
				((UnsignedLiteralExpressionContext)_localctx).DateTime = dateTimeLiteralExpression();
				}
				break;
			case TIMESPANLITERAL:
				enterOuterAlt(_localctx, 6);
				{
				setState(2688);
				((UnsignedLiteralExpressionContext)_localctx).TimeSpan = timeSpanLiteralExpression();
				}
				break;
			case BOOLEANLITERAL:
				enterOuterAlt(_localctx, 7);
				{
				setState(2689);
				((UnsignedLiteralExpressionContext)_localctx).Boolean = booleanLiteralExpression();
				}
				break;
			case GUIDLITERAL:
				enterOuterAlt(_localctx, 8);
				{
				setState(2690);
				((UnsignedLiteralExpressionContext)_localctx).Guid = guidLiteralExpression();
				}
				break;
			case TYPELITERAL:
				enterOuterAlt(_localctx, 9);
				{
				setState(2691);
				((UnsignedLiteralExpressionContext)_localctx).Type = typeLiteralExpression();
				}
				break;
			case STRINGLITERAL:
				enterOuterAlt(_localctx, 10);
				{
				setState(2692);
				((UnsignedLiteralExpressionContext)_localctx).String = stringLiteralExpression();
				}
				break;
			case DYNAMIC:
				enterOuterAlt(_localctx, 11);
				{
				setState(2693);
				((UnsignedLiteralExpressionContext)_localctx).Dynamic = dynamicLiteralExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumberLikeLiteralExpressionContext extends ParserRuleContext {
		public LongLiteralExpressionContext Long;
		public IntLiteralExpressionContext Int;
		public RealLiteralExpressionContext Real;
		public DecimalLiteralExpressionContext Decimal;
		public SignedLiteralExpressionContext Signed;
		public DateTimeLiteralExpressionContext DateTime;
		public TimeSpanLiteralExpressionContext TimeSpan;
		public LongLiteralExpressionContext longLiteralExpression() {
			return getRuleContext(LongLiteralExpressionContext.class,0);
		}
		public IntLiteralExpressionContext intLiteralExpression() {
			return getRuleContext(IntLiteralExpressionContext.class,0);
		}
		public RealLiteralExpressionContext realLiteralExpression() {
			return getRuleContext(RealLiteralExpressionContext.class,0);
		}
		public DecimalLiteralExpressionContext decimalLiteralExpression() {
			return getRuleContext(DecimalLiteralExpressionContext.class,0);
		}
		public SignedLiteralExpressionContext signedLiteralExpression() {
			return getRuleContext(SignedLiteralExpressionContext.class,0);
		}
		public DateTimeLiteralExpressionContext dateTimeLiteralExpression() {
			return getRuleContext(DateTimeLiteralExpressionContext.class,0);
		}
		public TimeSpanLiteralExpressionContext timeSpanLiteralExpression() {
			return getRuleContext(TimeSpanLiteralExpressionContext.class,0);
		}
		public NumberLikeLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numberLikeLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNumberLikeLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNumberLikeLiteralExpression(this);
		}
	}

	public final NumberLikeLiteralExpressionContext numberLikeLiteralExpression() throws RecognitionException {
		NumberLikeLiteralExpressionContext _localctx = new NumberLikeLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 554, RULE_numberLikeLiteralExpression);
		try {
			setState(2703);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LONGLITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(2696);
				((NumberLikeLiteralExpressionContext)_localctx).Long = longLiteralExpression();
				}
				break;
			case INTLITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(2697);
				((NumberLikeLiteralExpressionContext)_localctx).Int = intLiteralExpression();
				}
				break;
			case REALLITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(2698);
				((NumberLikeLiteralExpressionContext)_localctx).Real = realLiteralExpression();
				}
				break;
			case DECIMALLITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(2699);
				((NumberLikeLiteralExpressionContext)_localctx).Decimal = decimalLiteralExpression();
				}
				break;
			case DASH:
			case PLUS:
				enterOuterAlt(_localctx, 5);
				{
				setState(2700);
				((NumberLikeLiteralExpressionContext)_localctx).Signed = signedLiteralExpression();
				}
				break;
			case DATETIMELITERAL:
				enterOuterAlt(_localctx, 6);
				{
				setState(2701);
				((NumberLikeLiteralExpressionContext)_localctx).DateTime = dateTimeLiteralExpression();
				}
				break;
			case TIMESPANLITERAL:
				enterOuterAlt(_localctx, 7);
				{
				setState(2702);
				((NumberLikeLiteralExpressionContext)_localctx).TimeSpan = timeSpanLiteralExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NumericLiteralExpressionContext extends ParserRuleContext {
		public LongLiteralExpressionContext Long;
		public IntLiteralExpressionContext Int;
		public RealLiteralExpressionContext Real;
		public DecimalLiteralExpressionContext Decimal;
		public SignedLiteralExpressionContext Signed;
		public LongLiteralExpressionContext longLiteralExpression() {
			return getRuleContext(LongLiteralExpressionContext.class,0);
		}
		public IntLiteralExpressionContext intLiteralExpression() {
			return getRuleContext(IntLiteralExpressionContext.class,0);
		}
		public RealLiteralExpressionContext realLiteralExpression() {
			return getRuleContext(RealLiteralExpressionContext.class,0);
		}
		public DecimalLiteralExpressionContext decimalLiteralExpression() {
			return getRuleContext(DecimalLiteralExpressionContext.class,0);
		}
		public SignedLiteralExpressionContext signedLiteralExpression() {
			return getRuleContext(SignedLiteralExpressionContext.class,0);
		}
		public NumericLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_numericLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterNumericLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitNumericLiteralExpression(this);
		}
	}

	public final NumericLiteralExpressionContext numericLiteralExpression() throws RecognitionException {
		NumericLiteralExpressionContext _localctx = new NumericLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 556, RULE_numericLiteralExpression);
		try {
			setState(2710);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LONGLITERAL:
				enterOuterAlt(_localctx, 1);
				{
				setState(2705);
				((NumericLiteralExpressionContext)_localctx).Long = longLiteralExpression();
				}
				break;
			case INTLITERAL:
				enterOuterAlt(_localctx, 2);
				{
				setState(2706);
				((NumericLiteralExpressionContext)_localctx).Int = intLiteralExpression();
				}
				break;
			case REALLITERAL:
				enterOuterAlt(_localctx, 3);
				{
				setState(2707);
				((NumericLiteralExpressionContext)_localctx).Real = realLiteralExpression();
				}
				break;
			case DECIMALLITERAL:
				enterOuterAlt(_localctx, 4);
				{
				setState(2708);
				((NumericLiteralExpressionContext)_localctx).Decimal = decimalLiteralExpression();
				}
				break;
			case DASH:
			case PLUS:
				enterOuterAlt(_localctx, 5);
				{
				setState(2709);
				((NumericLiteralExpressionContext)_localctx).Signed = signedLiteralExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SignedLiteralExpressionContext extends ParserRuleContext {
		public SignedLongLiteralExpressionContext Long;
		public SignedRealLiteralExpressionContext Real;
		public SignedLongLiteralExpressionContext signedLongLiteralExpression() {
			return getRuleContext(SignedLongLiteralExpressionContext.class,0);
		}
		public SignedRealLiteralExpressionContext signedRealLiteralExpression() {
			return getRuleContext(SignedRealLiteralExpressionContext.class,0);
		}
		public SignedLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signedLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSignedLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSignedLiteralExpression(this);
		}
	}

	public final SignedLiteralExpressionContext signedLiteralExpression() throws RecognitionException {
		SignedLiteralExpressionContext _localctx = new SignedLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 558, RULE_signedLiteralExpression);
		try {
			setState(2714);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,249,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2712);
				((SignedLiteralExpressionContext)_localctx).Long = signedLongLiteralExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2713);
				((SignedLiteralExpressionContext)_localctx).Real = signedRealLiteralExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LongLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode LONGLITERAL() { return getToken(HqlParser.LONGLITERAL, 0); }
		public LongLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_longLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterLongLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitLongLiteralExpression(this);
		}
	}

	public final LongLiteralExpressionContext longLiteralExpression() throws RecognitionException {
		LongLiteralExpressionContext _localctx = new LongLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 560, RULE_longLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2716);
			((LongLiteralExpressionContext)_localctx).Token = match(LONGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IntLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode INTLITERAL() { return getToken(HqlParser.INTLITERAL, 0); }
		public IntLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_intLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterIntLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitIntLiteralExpression(this);
		}
	}

	public final IntLiteralExpressionContext intLiteralExpression() throws RecognitionException {
		IntLiteralExpressionContext _localctx = new IntLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 562, RULE_intLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2718);
			((IntLiteralExpressionContext)_localctx).Token = match(INTLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RealLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode REALLITERAL() { return getToken(HqlParser.REALLITERAL, 0); }
		public RealLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_realLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterRealLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitRealLiteralExpression(this);
		}
	}

	public final RealLiteralExpressionContext realLiteralExpression() throws RecognitionException {
		RealLiteralExpressionContext _localctx = new RealLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 564, RULE_realLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2720);
			((RealLiteralExpressionContext)_localctx).Token = match(REALLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DecimalLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode DECIMALLITERAL() { return getToken(HqlParser.DECIMALLITERAL, 0); }
		public DecimalLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_decimalLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDecimalLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDecimalLiteralExpression(this);
		}
	}

	public final DecimalLiteralExpressionContext decimalLiteralExpression() throws RecognitionException {
		DecimalLiteralExpressionContext _localctx = new DecimalLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 566, RULE_decimalLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2722);
			((DecimalLiteralExpressionContext)_localctx).Token = match(DECIMALLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DateTimeLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode DATETIMELITERAL() { return getToken(HqlParser.DATETIMELITERAL, 0); }
		public DateTimeLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dateTimeLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDateTimeLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDateTimeLiteralExpression(this);
		}
	}

	public final DateTimeLiteralExpressionContext dateTimeLiteralExpression() throws RecognitionException {
		DateTimeLiteralExpressionContext _localctx = new DateTimeLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 568, RULE_dateTimeLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2724);
			((DateTimeLiteralExpressionContext)_localctx).Token = match(DATETIMELITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TimeSpanLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode TIMESPANLITERAL() { return getToken(HqlParser.TIMESPANLITERAL, 0); }
		public TimeSpanLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_timeSpanLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTimeSpanLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTimeSpanLiteralExpression(this);
		}
	}

	public final TimeSpanLiteralExpressionContext timeSpanLiteralExpression() throws RecognitionException {
		TimeSpanLiteralExpressionContext _localctx = new TimeSpanLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 570, RULE_timeSpanLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2726);
			((TimeSpanLiteralExpressionContext)_localctx).Token = match(TIMESPANLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BooleanLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode BOOLEANLITERAL() { return getToken(HqlParser.BOOLEANLITERAL, 0); }
		public BooleanLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_booleanLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterBooleanLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitBooleanLiteralExpression(this);
		}
	}

	public final BooleanLiteralExpressionContext booleanLiteralExpression() throws RecognitionException {
		BooleanLiteralExpressionContext _localctx = new BooleanLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 572, RULE_booleanLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2728);
			((BooleanLiteralExpressionContext)_localctx).Token = match(BOOLEANLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class GuidLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode GUIDLITERAL() { return getToken(HqlParser.GUIDLITERAL, 0); }
		public GuidLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_guidLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterGuidLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitGuidLiteralExpression(this);
		}
	}

	public final GuidLiteralExpressionContext guidLiteralExpression() throws RecognitionException {
		GuidLiteralExpressionContext _localctx = new GuidLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 574, RULE_guidLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2730);
			((GuidLiteralExpressionContext)_localctx).Token = match(GUIDLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeLiteralExpressionContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode TYPELITERAL() { return getToken(HqlParser.TYPELITERAL, 0); }
		public TypeLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterTypeLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitTypeLiteralExpression(this);
		}
	}

	public final TypeLiteralExpressionContext typeLiteralExpression() throws RecognitionException {
		TypeLiteralExpressionContext _localctx = new TypeLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 576, RULE_typeLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2732);
			((TypeLiteralExpressionContext)_localctx).Token = match(TYPELITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SignedLongLiteralExpressionContext extends ParserRuleContext {
		public Token SignToken;
		public Token LiteralToken;
		public TerminalNode LONGLITERAL() { return getToken(HqlParser.LONGLITERAL, 0); }
		public TerminalNode PLUS() { return getToken(HqlParser.PLUS, 0); }
		public TerminalNode DASH() { return getToken(HqlParser.DASH, 0); }
		public SignedLongLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signedLongLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSignedLongLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSignedLongLiteralExpression(this);
		}
	}

	public final SignedLongLiteralExpressionContext signedLongLiteralExpression() throws RecognitionException {
		SignedLongLiteralExpressionContext _localctx = new SignedLongLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 578, RULE_signedLongLiteralExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2734);
			((SignedLongLiteralExpressionContext)_localctx).SignToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==DASH || _la==PLUS) ) {
				((SignedLongLiteralExpressionContext)_localctx).SignToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2735);
			((SignedLongLiteralExpressionContext)_localctx).LiteralToken = match(LONGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SignedRealLiteralExpressionContext extends ParserRuleContext {
		public Token SignToken;
		public Token LiteralToken;
		public TerminalNode REALLITERAL() { return getToken(HqlParser.REALLITERAL, 0); }
		public TerminalNode PLUS() { return getToken(HqlParser.PLUS, 0); }
		public TerminalNode DASH() { return getToken(HqlParser.DASH, 0); }
		public SignedRealLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signedRealLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterSignedRealLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitSignedRealLiteralExpression(this);
		}
	}

	public final SignedRealLiteralExpressionContext signedRealLiteralExpression() throws RecognitionException {
		SignedRealLiteralExpressionContext _localctx = new SignedRealLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 580, RULE_signedRealLiteralExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2737);
			((SignedRealLiteralExpressionContext)_localctx).SignToken = _input.LT(1);
			_la = _input.LA(1);
			if ( !(_la==DASH || _la==PLUS) ) {
				((SignedRealLiteralExpressionContext)_localctx).SignToken = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(2738);
			((SignedRealLiteralExpressionContext)_localctx).LiteralToken = match(REALLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StringLiteralExpressionContext extends ParserRuleContext {
		public Token STRINGLITERAL;
		public List<Token> Tokens = new ArrayList<Token>();
		public List<TerminalNode> STRINGLITERAL() { return getTokens(HqlParser.STRINGLITERAL); }
		public TerminalNode STRINGLITERAL(int i) {
			return getToken(HqlParser.STRINGLITERAL, i);
		}
		public StringLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_stringLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterStringLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitStringLiteralExpression(this);
		}
	}

	public final StringLiteralExpressionContext stringLiteralExpression() throws RecognitionException {
		StringLiteralExpressionContext _localctx = new StringLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 582, RULE_stringLiteralExpression);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(2740);
			((StringLiteralExpressionContext)_localctx).STRINGLITERAL = match(STRINGLITERAL);
			((StringLiteralExpressionContext)_localctx).Tokens.add(((StringLiteralExpressionContext)_localctx).STRINGLITERAL);
			setState(2744);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,250,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(2741);
					((StringLiteralExpressionContext)_localctx).STRINGLITERAL = match(STRINGLITERAL);
					((StringLiteralExpressionContext)_localctx).Tokens.add(((StringLiteralExpressionContext)_localctx).STRINGLITERAL);
					}
					} 
				}
				setState(2746);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,250,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DynamicLiteralExpressionContext extends ParserRuleContext {
		public JsonValueContext Value;
		public TerminalNode DYNAMIC() { return getToken(HqlParser.DYNAMIC, 0); }
		public TerminalNode OPENPAREN() { return getToken(HqlParser.OPENPAREN, 0); }
		public TerminalNode CLOSEPAREN() { return getToken(HqlParser.CLOSEPAREN, 0); }
		public JsonValueContext jsonValue() {
			return getRuleContext(JsonValueContext.class,0);
		}
		public DynamicLiteralExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dynamicLiteralExpression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterDynamicLiteralExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitDynamicLiteralExpression(this);
		}
	}

	public final DynamicLiteralExpressionContext dynamicLiteralExpression() throws RecognitionException {
		DynamicLiteralExpressionContext _localctx = new DynamicLiteralExpressionContext(_ctx, getState());
		enterRule(_localctx, 584, RULE_dynamicLiteralExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2747);
			match(DYNAMIC);
			setState(2748);
			match(OPENPAREN);
			setState(2749);
			((DynamicLiteralExpressionContext)_localctx).Value = jsonValue();
			setState(2750);
			match(CLOSEPAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonValueContext extends ParserRuleContext {
		public JsonArrayContext Array;
		public JsonBooleanContext Boolean;
		public JsonDateTimeContext DateTime;
		public JsonGuidContext Guid;
		public JsonLongContext Long;
		public JsonNullContext Null;
		public JsonObjectContext Object;
		public JsonRealContext Real;
		public JsonStringContext String;
		public JsonTimeSpanContext Timespan;
		public DynamicLiteralExpressionContext Dynamic;
		public JsonArrayContext jsonArray() {
			return getRuleContext(JsonArrayContext.class,0);
		}
		public JsonBooleanContext jsonBoolean() {
			return getRuleContext(JsonBooleanContext.class,0);
		}
		public JsonDateTimeContext jsonDateTime() {
			return getRuleContext(JsonDateTimeContext.class,0);
		}
		public JsonGuidContext jsonGuid() {
			return getRuleContext(JsonGuidContext.class,0);
		}
		public JsonLongContext jsonLong() {
			return getRuleContext(JsonLongContext.class,0);
		}
		public JsonNullContext jsonNull() {
			return getRuleContext(JsonNullContext.class,0);
		}
		public JsonObjectContext jsonObject() {
			return getRuleContext(JsonObjectContext.class,0);
		}
		public JsonRealContext jsonReal() {
			return getRuleContext(JsonRealContext.class,0);
		}
		public JsonStringContext jsonString() {
			return getRuleContext(JsonStringContext.class,0);
		}
		public JsonTimeSpanContext jsonTimeSpan() {
			return getRuleContext(JsonTimeSpanContext.class,0);
		}
		public DynamicLiteralExpressionContext dynamicLiteralExpression() {
			return getRuleContext(DynamicLiteralExpressionContext.class,0);
		}
		public JsonValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonValue; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonValue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonValue(this);
		}
	}

	public final JsonValueContext jsonValue() throws RecognitionException {
		JsonValueContext _localctx = new JsonValueContext(_ctx, getState());
		enterRule(_localctx, 586, RULE_jsonValue);
		try {
			setState(2763);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,251,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(2752);
				((JsonValueContext)_localctx).Array = jsonArray();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(2753);
				((JsonValueContext)_localctx).Boolean = jsonBoolean();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(2754);
				((JsonValueContext)_localctx).DateTime = jsonDateTime();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(2755);
				((JsonValueContext)_localctx).Guid = jsonGuid();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(2756);
				((JsonValueContext)_localctx).Long = jsonLong();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(2757);
				((JsonValueContext)_localctx).Null = jsonNull();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(2758);
				((JsonValueContext)_localctx).Object = jsonObject();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(2759);
				((JsonValueContext)_localctx).Real = jsonReal();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(2760);
				((JsonValueContext)_localctx).String = jsonString();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(2761);
				((JsonValueContext)_localctx).Timespan = jsonTimeSpan();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(2762);
				((JsonValueContext)_localctx).Dynamic = dynamicLiteralExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonObjectContext extends ParserRuleContext {
		public JsonPairContext jsonPair;
		public List<JsonPairContext> Pairs = new ArrayList<JsonPairContext>();
		public TerminalNode OPENBRACE() { return getToken(HqlParser.OPENBRACE, 0); }
		public TerminalNode CLOSEBRACE() { return getToken(HqlParser.CLOSEBRACE, 0); }
		public List<JsonPairContext> jsonPair() {
			return getRuleContexts(JsonPairContext.class);
		}
		public JsonPairContext jsonPair(int i) {
			return getRuleContext(JsonPairContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public JsonObjectContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonObject; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonObject(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonObject(this);
		}
	}

	public final JsonObjectContext jsonObject() throws RecognitionException {
		JsonObjectContext _localctx = new JsonObjectContext(_ctx, getState());
		enterRule(_localctx, 588, RULE_jsonObject);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2765);
			match(OPENBRACE);
			setState(2774);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==STRINGLITERAL) {
				{
				setState(2766);
				((JsonObjectContext)_localctx).jsonPair = jsonPair();
				((JsonObjectContext)_localctx).Pairs.add(((JsonObjectContext)_localctx).jsonPair);
				setState(2771);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(2767);
					match(COMMA);
					setState(2768);
					((JsonObjectContext)_localctx).jsonPair = jsonPair();
					((JsonObjectContext)_localctx).Pairs.add(((JsonObjectContext)_localctx).jsonPair);
					}
					}
					setState(2773);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(2776);
			match(CLOSEBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonPairContext extends ParserRuleContext {
		public Token Name;
		public JsonValueContext Value;
		public TerminalNode COLON() { return getToken(HqlParser.COLON, 0); }
		public TerminalNode STRINGLITERAL() { return getToken(HqlParser.STRINGLITERAL, 0); }
		public JsonValueContext jsonValue() {
			return getRuleContext(JsonValueContext.class,0);
		}
		public JsonPairContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonPair; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonPair(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonPair(this);
		}
	}

	public final JsonPairContext jsonPair() throws RecognitionException {
		JsonPairContext _localctx = new JsonPairContext(_ctx, getState());
		enterRule(_localctx, 590, RULE_jsonPair);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2778);
			((JsonPairContext)_localctx).Name = match(STRINGLITERAL);
			setState(2779);
			match(COLON);
			setState(2780);
			((JsonPairContext)_localctx).Value = jsonValue();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonArrayContext extends ParserRuleContext {
		public JsonValueContext jsonValue;
		public List<JsonValueContext> Values = new ArrayList<JsonValueContext>();
		public TerminalNode OPENBRACKET() { return getToken(HqlParser.OPENBRACKET, 0); }
		public TerminalNode CLOSEBRACKET() { return getToken(HqlParser.CLOSEBRACKET, 0); }
		public List<JsonValueContext> jsonValue() {
			return getRuleContexts(JsonValueContext.class);
		}
		public JsonValueContext jsonValue(int i) {
			return getRuleContext(JsonValueContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(HqlParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(HqlParser.COMMA, i);
		}
		public JsonArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonArray; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonArray(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonArray(this);
		}
	}

	public final JsonArrayContext jsonArray() throws RecognitionException {
		JsonArrayContext _localctx = new JsonArrayContext(_ctx, getState());
		enterRule(_localctx, 592, RULE_jsonArray);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2782);
			match(OPENBRACKET);
			setState(2791);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1610614784L) != 0) || _la==NULL || ((((_la - 285)) & ~0x3f) == 0 && ((1L << (_la - 285)) & 1330642945L) != 0)) {
				{
				setState(2783);
				((JsonArrayContext)_localctx).jsonValue = jsonValue();
				((JsonArrayContext)_localctx).Values.add(((JsonArrayContext)_localctx).jsonValue);
				setState(2788);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(2784);
					match(COMMA);
					setState(2785);
					((JsonArrayContext)_localctx).jsonValue = jsonValue();
					((JsonArrayContext)_localctx).Values.add(((JsonArrayContext)_localctx).jsonValue);
					}
					}
					setState(2790);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(2793);
			match(CLOSEBRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonBooleanContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode BOOLEANLITERAL() { return getToken(HqlParser.BOOLEANLITERAL, 0); }
		public JsonBooleanContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonBoolean; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonBoolean(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonBoolean(this);
		}
	}

	public final JsonBooleanContext jsonBoolean() throws RecognitionException {
		JsonBooleanContext _localctx = new JsonBooleanContext(_ctx, getState());
		enterRule(_localctx, 594, RULE_jsonBoolean);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2795);
			((JsonBooleanContext)_localctx).Token = match(BOOLEANLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonDateTimeContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode DATETIMELITERAL() { return getToken(HqlParser.DATETIMELITERAL, 0); }
		public JsonDateTimeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonDateTime; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonDateTime(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonDateTime(this);
		}
	}

	public final JsonDateTimeContext jsonDateTime() throws RecognitionException {
		JsonDateTimeContext _localctx = new JsonDateTimeContext(_ctx, getState());
		enterRule(_localctx, 596, RULE_jsonDateTime);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2797);
			((JsonDateTimeContext)_localctx).Token = match(DATETIMELITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonGuidContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode GUIDLITERAL() { return getToken(HqlParser.GUIDLITERAL, 0); }
		public JsonGuidContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonGuid; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonGuid(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonGuid(this);
		}
	}

	public final JsonGuidContext jsonGuid() throws RecognitionException {
		JsonGuidContext _localctx = new JsonGuidContext(_ctx, getState());
		enterRule(_localctx, 598, RULE_jsonGuid);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2799);
			((JsonGuidContext)_localctx).Token = match(GUIDLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonNullContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode NULL() { return getToken(HqlParser.NULL, 0); }
		public JsonNullContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonNull; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonNull(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonNull(this);
		}
	}

	public final JsonNullContext jsonNull() throws RecognitionException {
		JsonNullContext _localctx = new JsonNullContext(_ctx, getState());
		enterRule(_localctx, 600, RULE_jsonNull);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2801);
			((JsonNullContext)_localctx).Token = match(NULL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonStringContext extends ParserRuleContext {
		public Token STRINGLITERAL;
		public List<Token> Tokens = new ArrayList<Token>();
		public List<TerminalNode> STRINGLITERAL() { return getTokens(HqlParser.STRINGLITERAL); }
		public TerminalNode STRINGLITERAL(int i) {
			return getToken(HqlParser.STRINGLITERAL, i);
		}
		public JsonStringContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonString; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonString(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonString(this);
		}
	}

	public final JsonStringContext jsonString() throws RecognitionException {
		JsonStringContext _localctx = new JsonStringContext(_ctx, getState());
		enterRule(_localctx, 602, RULE_jsonString);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2803);
			((JsonStringContext)_localctx).STRINGLITERAL = match(STRINGLITERAL);
			((JsonStringContext)_localctx).Tokens.add(((JsonStringContext)_localctx).STRINGLITERAL);
			setState(2807);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==STRINGLITERAL) {
				{
				{
				setState(2804);
				((JsonStringContext)_localctx).STRINGLITERAL = match(STRINGLITERAL);
				((JsonStringContext)_localctx).Tokens.add(((JsonStringContext)_localctx).STRINGLITERAL);
				}
				}
				setState(2809);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonTimeSpanContext extends ParserRuleContext {
		public Token Token;
		public TerminalNode TIMESPANLITERAL() { return getToken(HqlParser.TIMESPANLITERAL, 0); }
		public JsonTimeSpanContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonTimeSpan; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonTimeSpan(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonTimeSpan(this);
		}
	}

	public final JsonTimeSpanContext jsonTimeSpan() throws RecognitionException {
		JsonTimeSpanContext _localctx = new JsonTimeSpanContext(_ctx, getState());
		enterRule(_localctx, 604, RULE_jsonTimeSpan);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2810);
			((JsonTimeSpanContext)_localctx).Token = match(TIMESPANLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonLongContext extends ParserRuleContext {
		public Token SignToken;
		public Token LiteralToken;
		public TerminalNode LONGLITERAL() { return getToken(HqlParser.LONGLITERAL, 0); }
		public TerminalNode DASH() { return getToken(HqlParser.DASH, 0); }
		public JsonLongContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonLong; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonLong(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonLong(this);
		}
	}

	public final JsonLongContext jsonLong() throws RecognitionException {
		JsonLongContext _localctx = new JsonLongContext(_ctx, getState());
		enterRule(_localctx, 606, RULE_jsonLong);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2813);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DASH) {
				{
				setState(2812);
				((JsonLongContext)_localctx).SignToken = match(DASH);
				}
			}

			setState(2815);
			((JsonLongContext)_localctx).LiteralToken = match(LONGLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class JsonRealContext extends ParserRuleContext {
		public Token SignToken;
		public Token LiteralToken;
		public TerminalNode REALLITERAL() { return getToken(HqlParser.REALLITERAL, 0); }
		public TerminalNode DASH() { return getToken(HqlParser.DASH, 0); }
		public JsonRealContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_jsonReal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).enterJsonReal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HqlListener ) ((HqlListener)listener).exitJsonReal(this);
		}
	}

	public final JsonRealContext jsonReal() throws RecognitionException {
		JsonRealContext _localctx = new JsonRealContext(_ctx, getState());
		enterRule(_localctx, 608, RULE_jsonReal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2818);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DASH) {
				{
				setState(2817);
				((JsonRealContext)_localctx).SignToken = match(DASH);
				}
			}

			setState(2820);
			((JsonRealContext)_localctx).LiteralToken = match(REALLITERAL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	private static final String _serializedATNSegment0 =
		"\u0004\u0001\u013e\u0b07\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007"+
		"\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007"+
		"\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007"+
		"\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007"+
		"\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007"+
		"\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007"+
		"\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007+\u0002,\u0007"+
		",\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u00070\u00021\u0007"+
		"1\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u00075\u00026\u0007"+
		"6\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007:\u0002;\u0007"+
		";\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007?\u0002@\u0007"+
		"@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007D\u0002E\u0007"+
		"E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007I\u0002J\u0007"+
		"J\u0002K\u0007K\u0002L\u0007L\u0002M\u0007M\u0002N\u0007N\u0002O\u0007"+
		"O\u0002P\u0007P\u0002Q\u0007Q\u0002R\u0007R\u0002S\u0007S\u0002T\u0007"+
		"T\u0002U\u0007U\u0002V\u0007V\u0002W\u0007W\u0002X\u0007X\u0002Y\u0007"+
		"Y\u0002Z\u0007Z\u0002[\u0007[\u0002\\\u0007\\\u0002]\u0007]\u0002^\u0007"+
		"^\u0002_\u0007_\u0002`\u0007`\u0002a\u0007a\u0002b\u0007b\u0002c\u0007"+
		"c\u0002d\u0007d\u0002e\u0007e\u0002f\u0007f\u0002g\u0007g\u0002h\u0007"+
		"h\u0002i\u0007i\u0002j\u0007j\u0002k\u0007k\u0002l\u0007l\u0002m\u0007"+
		"m\u0002n\u0007n\u0002o\u0007o\u0002p\u0007p\u0002q\u0007q\u0002r\u0007"+
		"r\u0002s\u0007s\u0002t\u0007t\u0002u\u0007u\u0002v\u0007v\u0002w\u0007"+
		"w\u0002x\u0007x\u0002y\u0007y\u0002z\u0007z\u0002{\u0007{\u0002|\u0007"+
		"|\u0002}\u0007}\u0002~\u0007~\u0002\u007f\u0007\u007f\u0002\u0080\u0007"+
		"\u0080\u0002\u0081\u0007\u0081\u0002\u0082\u0007\u0082\u0002\u0083\u0007"+
		"\u0083\u0002\u0084\u0007\u0084\u0002\u0085\u0007\u0085\u0002\u0086\u0007"+
		"\u0086\u0002\u0087\u0007\u0087\u0002\u0088\u0007\u0088\u0002\u0089\u0007"+
		"\u0089\u0002\u008a\u0007\u008a\u0002\u008b\u0007\u008b\u0002\u008c\u0007"+
		"\u008c\u0002\u008d\u0007\u008d\u0002\u008e\u0007\u008e\u0002\u008f\u0007"+
		"\u008f\u0002\u0090\u0007\u0090\u0002\u0091\u0007\u0091\u0002\u0092\u0007"+
		"\u0092\u0002\u0093\u0007\u0093\u0002\u0094\u0007\u0094\u0002\u0095\u0007"+
		"\u0095\u0002\u0096\u0007\u0096\u0002\u0097\u0007\u0097\u0002\u0098\u0007"+
		"\u0098\u0002\u0099\u0007\u0099\u0002\u009a\u0007\u009a\u0002\u009b\u0007"+
		"\u009b\u0002\u009c\u0007\u009c\u0002\u009d\u0007\u009d\u0002\u009e\u0007"+
		"\u009e\u0002\u009f\u0007\u009f\u0002\u00a0\u0007\u00a0\u0002\u00a1\u0007"+
		"\u00a1\u0002\u00a2\u0007\u00a2\u0002\u00a3\u0007\u00a3\u0002\u00a4\u0007"+
		"\u00a4\u0002\u00a5\u0007\u00a5\u0002\u00a6\u0007\u00a6\u0002\u00a7\u0007"+
		"\u00a7\u0002\u00a8\u0007\u00a8\u0002\u00a9\u0007\u00a9\u0002\u00aa\u0007"+
		"\u00aa\u0002\u00ab\u0007\u00ab\u0002\u00ac\u0007\u00ac\u0002\u00ad\u0007"+
		"\u00ad\u0002\u00ae\u0007\u00ae\u0002\u00af\u0007\u00af\u0002\u00b0\u0007"+
		"\u00b0\u0002\u00b1\u0007\u00b1\u0002\u00b2\u0007\u00b2\u0002\u00b3\u0007"+
		"\u00b3\u0002\u00b4\u0007\u00b4\u0002\u00b5\u0007\u00b5\u0002\u00b6\u0007"+
		"\u00b6\u0002\u00b7\u0007\u00b7\u0002\u00b8\u0007\u00b8\u0002\u00b9\u0007"+
		"\u00b9\u0002\u00ba\u0007\u00ba\u0002\u00bb\u0007\u00bb\u0002\u00bc\u0007"+
		"\u00bc\u0002\u00bd\u0007\u00bd\u0002\u00be\u0007\u00be\u0002\u00bf\u0007"+
		"\u00bf\u0002\u00c0\u0007\u00c0\u0002\u00c1\u0007\u00c1\u0002\u00c2\u0007"+
		"\u00c2\u0002\u00c3\u0007\u00c3\u0002\u00c4\u0007\u00c4\u0002\u00c5\u0007"+
		"\u00c5\u0002\u00c6\u0007\u00c6\u0002\u00c7\u0007\u00c7\u0002\u00c8\u0007"+
		"\u00c8\u0002\u00c9\u0007\u00c9\u0002\u00ca\u0007\u00ca\u0002\u00cb\u0007"+
		"\u00cb\u0002\u00cc\u0007\u00cc\u0002\u00cd\u0007\u00cd\u0002\u00ce\u0007"+
		"\u00ce\u0002\u00cf\u0007\u00cf\u0002\u00d0\u0007\u00d0\u0002\u00d1\u0007"+
		"\u00d1\u0002\u00d2\u0007\u00d2\u0002\u00d3\u0007\u00d3\u0002\u00d4\u0007"+
		"\u00d4\u0002\u00d5\u0007\u00d5\u0002\u00d6\u0007\u00d6\u0002\u00d7\u0007"+
		"\u00d7\u0002\u00d8\u0007\u00d8\u0002\u00d9\u0007\u00d9\u0002\u00da\u0007"+
		"\u00da\u0002\u00db\u0007\u00db\u0002\u00dc\u0007\u00dc\u0002\u00dd\u0007"+
		"\u00dd\u0002\u00de\u0007\u00de\u0002\u00df\u0007\u00df\u0002\u00e0\u0007"+
		"\u00e0\u0002\u00e1\u0007\u00e1\u0002\u00e2\u0007\u00e2\u0002\u00e3\u0007"+
		"\u00e3\u0002\u00e4\u0007\u00e4\u0002\u00e5\u0007\u00e5\u0002\u00e6\u0007"+
		"\u00e6\u0002\u00e7\u0007\u00e7\u0002\u00e8\u0007\u00e8\u0002\u00e9\u0007"+
		"\u00e9\u0002\u00ea\u0007\u00ea\u0002\u00eb\u0007\u00eb\u0002\u00ec\u0007"+
		"\u00ec\u0002\u00ed\u0007\u00ed\u0002\u00ee\u0007\u00ee\u0002\u00ef\u0007"+
		"\u00ef\u0002\u00f0\u0007\u00f0\u0002\u00f1\u0007\u00f1\u0002\u00f2\u0007"+
		"\u00f2\u0002\u00f3\u0007\u00f3\u0002\u00f4\u0007\u00f4\u0002\u00f5\u0007"+
		"\u00f5\u0002\u00f6\u0007\u00f6\u0002\u00f7\u0007\u00f7\u0002\u00f8\u0007"+
		"\u00f8\u0002\u00f9\u0007\u00f9\u0002\u00fa\u0007\u00fa\u0002\u00fb\u0007"+
		"\u00fb\u0002\u00fc\u0007\u00fc\u0002\u00fd\u0007\u00fd\u0002\u00fe\u0007"+
		"\u00fe\u0002\u00ff\u0007\u00ff\u0002\u0100\u0007\u0100\u0002\u0101\u0007"+
		"\u0101\u0002\u0102\u0007\u0102\u0002\u0103\u0007\u0103\u0002\u0104\u0007"+
		"\u0104\u0002\u0105\u0007\u0105\u0002\u0106\u0007\u0106\u0002\u0107\u0007"+
		"\u0107\u0002\u0108\u0007\u0108\u0002\u0109\u0007\u0109\u0002\u010a\u0007"+
		"\u010a\u0002\u010b\u0007\u010b\u0002\u010c\u0007\u010c\u0002\u010d\u0007"+
		"\u010d\u0002\u010e\u0007\u010e\u0002\u010f\u0007\u010f\u0002\u0110\u0007"+
		"\u0110\u0002\u0111\u0007\u0111\u0002\u0112\u0007\u0112\u0002\u0113\u0007"+
		"\u0113\u0002\u0114\u0007\u0114\u0002\u0115\u0007\u0115\u0002\u0116\u0007"+
		"\u0116\u0002\u0117\u0007\u0117\u0002\u0118\u0007\u0118\u0002\u0119\u0007"+
		"\u0119\u0002\u011a\u0007\u011a\u0002\u011b\u0007\u011b\u0002\u011c\u0007"+
		"\u011c\u0002\u011d\u0007\u011d\u0002\u011e\u0007\u011e\u0002\u011f\u0007"+
		"\u011f\u0002\u0120\u0007\u0120\u0002\u0121\u0007\u0121\u0002\u0122\u0007"+
		"\u0122\u0002\u0123\u0007\u0123\u0002\u0124\u0007\u0124\u0002\u0125\u0007"+
		"\u0125\u0002\u0126\u0007\u0126\u0002\u0127\u0007\u0127\u0002\u0128\u0007"+
		"\u0128\u0002\u0129\u0007\u0129\u0002\u012a\u0007\u012a\u0002\u012b\u0007"+
		"\u012b\u0002\u012c\u0007\u012c\u0002\u012d\u0007\u012d\u0002\u012e\u0007"+
		"\u012e\u0002\u012f\u0007\u012f\u0002\u0130\u0007\u0130\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u0001\u0268\b\u0001\n"+
		"\u0001\f\u0001\u026b\t\u0001\u0001\u0001\u0003\u0001\u026e\b\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002\u0279\b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u0286\b\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u0292\b\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0003\u0007\u029d\b\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0005\b\u02a5\b\b\n\b\f\b\u02a8"+
		"\t\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0003\u000b\u02c2\b\u000b\u0001\f\u0001\f\u0001"+
		"\f\u0001\f\u0003\f\u02c8\b\f\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0003\u000e\u02d1\b\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0005\u0010\u02db\b\u0010\n\u0010\f\u0010\u02de\t\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0005\u0012\u02ea\b\u0012\n\u0012"+
		"\f\u0012\u02ed\t\u0012\u0001\u0012\u0003\u0012\u02f0\b\u0012\u0001\u0012"+
		"\u0003\u0012\u02f3\b\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013"+
		"\u0003\u0013\u02f9\b\u0013\u0001\u0014\u0001\u0014\u0001\u0014\u0001\u0014"+
		"\u0003\u0014\u02ff\b\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0003\u0015"+
		"\u0304\b\u0015\u0001\u0015\u0001\u0015\u0004\u0015\u0308\b\u0015\u000b"+
		"\u0015\f\u0015\u0309\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0016\u0005\u0016\u0312\b\u0016\n\u0016\f\u0016\u0315\t\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017"+
		"\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0003\u0019\u0323\b\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0003\u0019"+
		"\u0328\b\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a"+
		"\u032e\b\u001a\n\u001a\f\u001a\u0331\t\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001c\u0001"+
		"\u001c\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0005\u001d\u0340"+
		"\b\u001d\n\u001d\f\u001d\u0343\t\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e"+
		"\u0001\u001e\u0005\u001e\u034f\b\u001e\n\u001e\f\u001e\u0352\t\u001e\u0001"+
		"\u001e\u0001\u001e\u0001\u001f\u0001\u001f\u0003\u001f\u0358\b\u001f\u0001"+
		" \u0001 \u0001 \u0001 \u0003 \u035e\b \u0001!\u0001!\u0003!\u0362\b!\u0001"+
		"\"\u0001\"\u0001\"\u0001\"\u0001\"\u0001\"\u0005\"\u036a\b\"\n\"\f\"\u036d"+
		"\t\"\u0001\"\u0001\"\u0001#\u0001#\u0001#\u0001#\u0003#\u0375\b#\u0001"+
		"$\u0001$\u0001%\u0001%\u0001&\u0001&\u0005&\u037d\b&\n&\f&\u0380\t&\u0001"+
		"\'\u0001\'\u0001\'\u0001(\u0001(\u0005(\u0387\b(\n(\f(\u038a\t(\u0001"+
		")\u0001)\u0001)\u0001)\u0001)\u0001)\u0003)\u0392\b)\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001"+
		"*\u0001*\u0001*\u0001*\u0001*\u0001*\u0001*\u0003*\u03c5\b*\u0001+\u0001"+
		"+\u0001+\u0001+\u0003+\u03cb\b+\u0001,\u0001,\u0001,\u0001,\u0001,\u0001"+
		",\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001"+
		",\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0001,\u0003"+
		",\u03e6\b,\u0001-\u0001-\u0005-\u03ea\b-\n-\f-\u03ed\t-\u0001-\u0001-"+
		"\u0001.\u0001.\u0001.\u0001/\u0001/\u0005/\u03f6\b/\n/\f/\u03f9\t/\u0001"+
		"0\u00010\u00050\u03fd\b0\n0\f0\u0400\t0\u00011\u00011\u00011\u00012\u0001"+
		"2\u00052\u0407\b2\n2\f2\u040a\t2\u00012\u00012\u00032\u040e\b2\u00013"+
		"\u00013\u00014\u00014\u00014\u00054\u0415\b4\n4\f4\u0418\t4\u00015\u0001"+
		"5\u00055\u041c\b5\n5\f5\u041f\t5\u00015\u00015\u00035\u0423\b5\u00016"+
		"\u00016\u00016\u00017\u00017\u00017\u00017\u00057\u042c\b7\n7\f7\u042f"+
		"\t7\u00018\u00018\u00019\u00019\u00019\u00019\u00019\u00059\u0438\b9\n"+
		"9\f9\u043b\t9\u00019\u00019\u00039\u043f\b9\u0001:\u0001:\u0001:\u0001"+
		";\u0001;\u0001;\u0001;\u0001;\u0001<\u0001<\u0003<\u044b\b<\u0001<\u0003"+
		"<\u044e\b<\u0001<\u0001<\u0001<\u0003<\u0453\b<\u0001<\u0003<\u0456\b"+
		"<\u0001=\u0005=\u0459\b=\n=\f=\u045c\t=\u0001=\u0003=\u045f\b=\u0001="+
		"\u0001=\u0001>\u0001>\u0001>\u0001>\u0001>\u0005>\u0468\b>\n>\f>\u046b"+
		"\t>\u0001>\u0001>\u0001?\u0001?\u0001?\u0001?\u0005?\u0473\b?\n?\f?\u0476"+
		"\t?\u0001@\u0001@\u0003@\u047a\b@\u0001A\u0001A\u0003A\u047e\bA\u0001"+
		"B\u0001B\u0001B\u0001C\u0001C\u0001C\u0001C\u0001C\u0001D\u0001D\u0001"+
		"E\u0001E\u0001E\u0003E\u048d\bE\u0001F\u0001F\u0001G\u0001G\u0001G\u0005"+
		"G\u0494\bG\nG\fG\u0497\tG\u0001H\u0001H\u0003H\u049b\bH\u0001I\u0001I"+
		"\u0001I\u0005I\u04a0\bI\nI\fI\u04a3\tI\u0001J\u0001J\u0004J\u04a7\bJ\u000b"+
		"J\fJ\u04a8\u0001K\u0003K\u04ac\bK\u0001K\u0001K\u0001K\u0001K\u0001L\u0001"+
		"L\u0001L\u0001M\u0001M\u0005M\u04b7\bM\nM\fM\u04ba\tM\u0001N\u0001N\u0001"+
		"N\u0001O\u0001O\u0001P\u0001P\u0005P\u04c3\bP\nP\fP\u04c6\tP\u0001Q\u0001"+
		"Q\u0005Q\u04ca\bQ\nQ\fQ\u04cd\tQ\u0001Q\u0001Q\u0001Q\u0001Q\u0001Q\u0003"+
		"Q\u04d4\bQ\u0001Q\u0003Q\u04d7\bQ\u0001R\u0001R\u0001R\u0003R\u04dc\b"+
		"R\u0001S\u0001S\u0001S\u0001S\u0001T\u0001T\u0001U\u0001U\u0001U\u0003"+
		"U\u04e7\bU\u0001U\u0001U\u0001V\u0001V\u0001V\u0001V\u0001V\u0001W\u0001"+
		"W\u0001W\u0001X\u0001X\u0001X\u0001X\u0005X\u04f7\bX\nX\fX\u04fa\tX\u0001"+
		"Y\u0001Y\u0001Y\u0003Y\u04ff\bY\u0001Z\u0001Z\u0001Z\u0001Z\u0001Z\u0001"+
		"[\u0001[\u0003[\u0508\b[\u0001[\u0005[\u050b\b[\n[\f[\u050e\t[\u0001\\"+
		"\u0001\\\u0001\\\u0001]\u0001]\u0005]\u0515\b]\n]\f]\u0518\t]\u0001]\u0001"+
		"]\u0001]\u0001]\u0001]\u0003]\u051f\b]\u0001]\u0003]\u0522\b]\u0001^\u0001"+
		"^\u0001^\u0001_\u0001_\u0005_\u0529\b_\n_\f_\u052c\t_\u0001_\u0001_\u0001"+
		"_\u0003_\u0531\b_\u0001`\u0001`\u0001`\u0001`\u0005`\u0537\b`\n`\f`\u053a"+
		"\t`\u0003`\u053c\b`\u0001a\u0001a\u0001a\u0001b\u0001b\u0005b\u0543\b"+
		"b\nb\fb\u0546\tb\u0001b\u0001b\u0001b\u0001c\u0001c\u0005c\u054d\bc\n"+
		"c\fc\u0550\tc\u0001c\u0001c\u0001c\u0001c\u0001c\u0001c\u0001c\u0005c"+
		"\u0559\bc\nc\fc\u055c\tc\u0001c\u0003c\u055f\bc\u0001c\u0001c\u0001d\u0001"+
		"d\u0001d\u0003d\u0566\bd\u0001e\u0001e\u0001e\u0001e\u0001e\u0005e\u056d"+
		"\be\ne\fe\u0570\te\u0001e\u0001e\u0001f\u0001f\u0005f\u0576\bf\nf\ff\u0579"+
		"\tf\u0001f\u0001f\u0001f\u0001f\u0001f\u0003f\u0580\bf\u0001f\u0003f\u0583"+
		"\bf\u0001g\u0001g\u0001g\u0001g\u0001h\u0001h\u0001h\u0001h\u0001h\u0001"+
		"i\u0001i\u0001i\u0001i\u0001i\u0001i\u0001j\u0001j\u0005j\u0596\bj\nj"+
		"\fj\u0599\tj\u0001j\u0001j\u0001j\u0005j\u059e\bj\nj\fj\u05a1\tj\u0001"+
		"j\u0001j\u0001j\u0003j\u05a6\bj\u0001j\u0003j\u05a9\bj\u0001k\u0001k\u0001"+
		"k\u0001l\u0001l\u0003l\u05b0\bl\u0001m\u0001m\u0001m\u0001m\u0001n\u0001"+
		"n\u0001n\u0001n\u0001n\u0001n\u0001n\u0001n\u0001n\u0001n\u0001o\u0001"+
		"o\u0003o\u05c2\bo\u0001o\u0001o\u0003o\u05c6\bo\u0001o\u0001o\u0001o\u0001"+
		"p\u0001p\u0001p\u0001p\u0005p\u05cf\bp\np\fp\u05d2\tp\u0001q\u0001q\u0005"+
		"q\u05d6\bq\nq\fq\u05d9\tq\u0001q\u0001q\u0001q\u0005q\u05de\bq\nq\fq\u05e1"+
		"\tq\u0001q\u0003q\u05e4\bq\u0001q\u0003q\u05e7\bq\u0001q\u0001q\u0001"+
		"q\u0001q\u0001q\u0001r\u0001r\u0001r\u0001s\u0001s\u0001s\u0001t\u0001"+
		"t\u0003t\u05f6\bt\u0001u\u0001u\u0001u\u0001v\u0001v\u0005v\u05fd\bv\n"+
		"v\fv\u0600\tv\u0001v\u0001v\u0001v\u0005v\u0605\bv\nv\fv\u0608\tv\u0001"+
		"v\u0003v\u060b\bv\u0001w\u0001w\u0003w\u060f\bw\u0001x\u0001x\u0003x\u0613"+
		"\bx\u0001x\u0001x\u0001x\u0001x\u0001y\u0001y\u0001y\u0001y\u0003y\u061d"+
		"\by\u0001z\u0001z\u0001z\u0001z\u0001{\u0001{\u0001{\u0003{\u0626\b{\u0001"+
		"|\u0003|\u0629\b|\u0001|\u0005|\u062c\b|\n|\f|\u062f\t|\u0001|\u0003|"+
		"\u0632\b|\u0001}\u0003}\u0635\b}\u0001}\u0001}\u0003}\u0639\b}\u0001~"+
		"\u0001~\u0003~\u063d\b~\u0001~\u0001~\u0001~\u0001~\u0001\u007f\u0001"+
		"\u007f\u0001\u007f\u0001\u007f\u0003\u007f\u0647\b\u007f\u0001\u0080\u0001"+
		"\u0080\u0001\u0080\u0001\u0080\u0001\u0080\u0005\u0080\u064e\b\u0080\n"+
		"\u0080\f\u0080\u0651\t\u0080\u0001\u0080\u0001\u0080\u0001\u0081\u0001"+
		"\u0081\u0005\u0081\u0657\b\u0081\n\u0081\f\u0081\u065a\t\u0081\u0001\u0081"+
		"\u0001\u0081\u0001\u0081\u0003\u0081\u065f\b\u0081\u0001\u0081\u0001\u0081"+
		"\u0003\u0081\u0663\b\u0081\u0001\u0082\u0001\u0082\u0001\u0082\u0003\u0082"+
		"\u0668\b\u0082\u0001\u0083\u0001\u0083\u0001\u0083\u0001\u0083\u0001\u0084"+
		"\u0001\u0084\u0001\u0084\u0001\u0084\u0001\u0085\u0001\u0085\u0005\u0085"+
		"\u0674\b\u0085\n\u0085\f\u0085\u0677\t\u0085\u0001\u0085\u0001\u0085\u0003"+
		"\u0085\u067b\b\u0085\u0001\u0085\u0001\u0085\u0001\u0085\u0001\u0085\u0001"+
		"\u0086\u0001\u0086\u0001\u0086\u0001\u0087\u0001\u0087\u0001\u0087\u0001"+
		"\u0087\u0005\u0087\u0688\b\u0087\n\u0087\f\u0087\u068b\t\u0087\u0001\u0088"+
		"\u0001\u0088\u0001\u0088\u0001\u0088\u0005\u0088\u0691\b\u0088\n\u0088"+
		"\f\u0088\u0694\t\u0088\u0003\u0088\u0696\b\u0088\u0001\u0089\u0001\u0089"+
		"\u0001\u0089\u0001\u0089\u0005\u0089\u069c\b\u0089\n\u0089\f\u0089\u069f"+
		"\t\u0089\u0001\u008a\u0001\u008a\u0001\u008a\u0001\u008a\u0005\u008a\u06a5"+
		"\b\u008a\n\u008a\f\u008a\u06a8\t\u008a\u0003\u008a\u06aa\b\u008a\u0001"+
		"\u008b\u0001\u008b\u0001\u008b\u0001\u008b\u0005\u008b\u06b0\b\u008b\n"+
		"\u008b\f\u008b\u06b3\t\u008b\u0003\u008b\u06b5\b\u008b\u0001\u008c\u0001"+
		"\u008c\u0001\u008c\u0001\u008c\u0005\u008c\u06bb\b\u008c\n\u008c\f\u008c"+
		"\u06be\t\u008c\u0003\u008c\u06c0\b\u008c\u0001\u008d\u0001\u008d\u0003"+
		"\u008d\u06c4\b\u008d\u0001\u008e\u0001\u008e\u0005\u008e\u06c8\b\u008e"+
		"\n\u008e\f\u008e\u06cb\t\u008e\u0001\u008e\u0001\u008e\u0001\u008e\u0003"+
		"\u008e\u06d0\b\u008e\u0001\u008f\u0001\u008f\u0001\u008f\u0001\u008f\u0005"+
		"\u008f\u06d6\b\u008f\n\u008f\f\u008f\u06d9\t\u008f\u0001\u0090\u0001\u0090"+
		"\u0001\u0090\u0001\u0090\u0003\u0090\u06df\b\u0090\u0001\u0091\u0001\u0091"+
		"\u0001\u0091\u0001\u0091\u0001\u0091\u0005\u0091\u06e6\b\u0091\n\u0091"+
		"\f\u0091\u06e9\t\u0091\u0003\u0091\u06eb\b\u0091\u0001\u0091\u0001\u0091"+
		"\u0001\u0092\u0004\u0092\u06f0\b\u0092\u000b\u0092\f\u0092\u06f1\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001\u0093\u0001"+
		"\u0093\u0001\u0093\u0001\u0093\u0003\u0093\u0727\b\u0093\u0001\u0094\u0001"+
		"\u0094\u0001\u0094\u0005\u0094\u072c\b\u0094\n\u0094\f\u0094\u072f\t\u0094"+
		"\u0001\u0095\u0001\u0095\u0001\u0095\u0001\u0095\u0001\u0095\u0001\u0095"+
		"\u0001\u0095\u0001\u0095\u0001\u0095\u0001\u0095\u0001\u0095\u0001\u0095"+
		"\u0001\u0095\u0003\u0095\u073e\b\u0095\u0001\u0096\u0001\u0096\u0005\u0096"+
		"\u0742\b\u0096\n\u0096\f\u0096\u0745\t\u0096\u0001\u0096\u0001\u0096\u0001"+
		"\u0096\u0001\u0096\u0001\u0097\u0001\u0097\u0005\u0097\u074d\b\u0097\n"+
		"\u0097\f\u0097\u0750\t\u0097\u0001\u0097\u0001\u0097\u0001\u0098\u0001"+
		"\u0098\u0005\u0098\u0756\b\u0098\n\u0098\f\u0098\u0759\t\u0098\u0001\u0098"+
		"\u0003\u0098\u075c\b\u0098\u0001\u0098\u0003\u0098\u075f\b\u0098\u0001"+
		"\u0098\u0003\u0098\u0762\b\u0098\u0001\u0098\u0001\u0098\u0001\u0098\u0004"+
		"\u0098\u0767\b\u0098\u000b\u0098\f\u0098\u0768\u0001\u0098\u0001\u0098"+
		"\u0001\u0099\u0001\u0099\u0001\u0099\u0001\u0099\u0001\u0099\u0001\u0099"+
		"\u0001\u009a\u0001\u009a\u0001\u009a\u0001\u009a\u0001\u009a\u0005\u009a"+
		"\u0778\b\u009a\n\u009a\f\u009a\u077b\t\u009a\u0001\u009b\u0001\u009b\u0001"+
		"\u009b\u0001\u009b\u0001\u009b\u0005\u009b\u0782\b\u009b\n\u009b\f\u009b"+
		"\u0785\t\u009b\u0001\u009b\u0001\u009b\u0001\u009c\u0001\u009c\u0001\u009c"+
		"\u0003\u009c\u078c\b\u009c\u0001\u009c\u0003\u009c\u078f\b\u009c\u0001"+
		"\u009c\u0001\u009c\u0001\u009c\u0003\u009c\u0794\b\u009c\u0001\u009c\u0001"+
		"\u009c\u0001\u009d\u0001\u009d\u0001\u009d\u0001\u009d\u0001\u009e\u0001"+
		"\u009e\u0001\u009e\u0001\u009e\u0005\u009e\u07a0\b\u009e\n\u009e\f\u009e"+
		"\u07a3\t\u009e\u0001\u009f\u0001\u009f\u0001\u009f\u0001\u009f\u0001\u00a0"+
		"\u0001\u00a0\u0005\u00a0\u07ab\b\u00a0\n\u00a0\f\u00a0\u07ae\t\u00a0\u0001"+
		"\u00a0\u0003\u00a0\u07b1\b\u00a0\u0001\u00a0\u0003\u00a0\u07b4\b\u00a0"+
		"\u0001\u00a0\u0001\u00a0\u0001\u00a0\u0003\u00a0\u07b9\b\u00a0\u0001\u00a1"+
		"\u0001\u00a1\u0001\u00a1\u0001\u00a1\u0001\u00a2\u0001\u00a2\u0001\u00a2"+
		"\u0001\u00a2\u0001\u00a2\u0005\u00a2\u07c4\b\u00a2\n\u00a2\f\u00a2\u07c7"+
		"\t\u00a2\u0001\u00a2\u0001\u00a2\u0001\u00a3\u0001\u00a3\u0005\u00a3\u07cd"+
		"\b\u00a3\n\u00a3\f\u00a3\u07d0\t\u00a3\u0001\u00a3\u0001\u00a3\u0001\u00a3"+
		"\u0005\u00a3\u07d5\b\u00a3\n\u00a3\f\u00a3\u07d8\t\u00a3\u0001\u00a4\u0001"+
		"\u00a4\u0005\u00a4\u07dc\b\u00a4\n\u00a4\f\u00a4\u07df\t\u00a4\u0001\u00a4"+
		"\u0001\u00a4\u0001\u00a4\u0001\u00a4\u0005\u00a4\u07e5\b\u00a4\n\u00a4"+
		"\f\u00a4\u07e8\t\u00a4\u0001\u00a5\u0001\u00a5\u0001\u00a5\u0001\u00a6"+
		"\u0003\u00a6\u07ee\b\u00a6\u0001\u00a6\u0001\u00a6\u0003\u00a6\u07f2\b"+
		"\u00a6\u0001\u00a7\u0001\u00a7\u0005\u00a7\u07f6\b\u00a7\n\u00a7\f\u00a7"+
		"\u07f9\t\u00a7\u0001\u00a7\u0001\u00a7\u0001\u00a7\u0005\u00a7\u07fe\b"+
		"\u00a7\n\u00a7\f\u00a7\u0801\t\u00a7\u0003\u00a7\u0803\b\u00a7\u0001\u00a7"+
		"\u0003\u00a7\u0806\b\u00a7\u0001\u00a8\u0001\u00a8\u0001\u00a8\u0001\u00a8"+
		"\u0001\u00a8\u0001\u00a8\u0003\u00a8\u080e\b\u00a8\u0001\u00a9\u0001\u00a9"+
		"\u0001\u00a9\u0001\u00a9\u0001\u00aa\u0001\u00aa\u0005\u00aa\u0816\b\u00aa"+
		"\n\u00aa\f\u00aa\u0819\t\u00aa\u0001\u00aa\u0001\u00aa\u0001\u00ab\u0001"+
		"\u00ab\u0005\u00ab\u081f\b\u00ab\n\u00ab\f\u00ab\u0822\t\u00ab\u0001\u00ab"+
		"\u0001\u00ab\u0001\u00ab\u0001\u00ab\u0001\u00ac\u0001\u00ac\u0001\u00ac"+
		"\u0001\u00ac\u0001\u00ac\u0003\u00ac\u082d\b\u00ac\u0001\u00ad\u0001\u00ad"+
		"\u0001\u00ad\u0001\u00ae\u0001\u00ae\u0001\u00ae\u0005\u00ae\u0835\b\u00ae"+
		"\n\u00ae\f\u00ae\u0838\t\u00ae\u0001\u00af\u0001\u00af\u0003\u00af\u083c"+
		"\b\u00af\u0001\u00af\u0001\u00af\u0001\u00af\u0003\u00af\u0841\b\u00af"+
		"\u0001\u00af\u0001\u00af\u0001\u00af\u0001\u00b0\u0001\u00b0\u0001\u00b0"+
		"\u0001\u00b0\u0001\u00b0\u0001\u00b1\u0001\u00b1\u0005\u00b1\u084d\b\u00b1"+
		"\n\u00b1\f\u00b1\u0850\t\u00b1\u0001\u00b1\u0001\u00b1\u0001\u00b1\u0005"+
		"\u00b1\u0855\b\u00b1\n\u00b1\f\u00b1\u0858\t\u00b1\u0001\u00b2\u0001\u00b2"+
		"\u0001\u00b2\u0003\u00b2\u085d\b\u00b2\u0001\u00b3\u0001\u00b3\u0005\u00b3"+
		"\u0861\b\u00b3\n\u00b3\f\u00b3\u0864\t\u00b3\u0001\u00b3\u0001\u00b3\u0001"+
		"\u00b4\u0001\u00b4\u0003\u00b4\u086a\b\u00b4\u0001\u00b5\u0001\u00b5\u0005"+
		"\u00b5\u086e\b\u00b5\n\u00b5\f\u00b5\u0871\t\u00b5\u0001\u00b6\u0001\u00b6"+
		"\u0001\u00b6\u0001\u00b7\u0001\u00b7\u0001\u00b7\u0001\u00b7\u0003\u00b7"+
		"\u087a\b\u00b7\u0001\u00b8\u0001\u00b8\u0001\u00b8\u0001\u00b8\u0003\u00b8"+
		"\u0880\b\u00b8\u0001\u00b9\u0001\u00b9\u0001\u00b9\u0001\u00b9\u0003\u00b9"+
		"\u0886\b\u00b9\u0001\u00ba\u0003\u00ba\u0889\b\u00ba\u0001\u00ba\u0001"+
		"\u00ba\u0001\u00bb\u0001\u00bb\u0003\u00bb\u088f\b\u00bb\u0001\u00bb\u0001"+
		"\u00bb\u0001\u00bc\u0001\u00bc\u0001\u00bc\u0001\u00bc\u0005\u00bc\u0897"+
		"\b\u00bc\n\u00bc\f\u00bc\u089a\t\u00bc\u0001\u00bc\u0001\u00bc\u0001\u00bd"+
		"\u0001\u00bd\u0001\u00bd\u0001\u00bd\u0001\u00be\u0001\u00be\u0001\u00bf"+
		"\u0001\u00bf\u0005\u00bf\u08a6\b\u00bf\n\u00bf\f\u00bf\u08a9\t\u00bf\u0001"+
		"\u00c0\u0001\u00c0\u0001\u00c0\u0001\u00c1\u0001\u00c1\u0005\u00c1\u08b0"+
		"\b\u00c1\n\u00c1\f\u00c1\u08b3\t\u00c1\u0001\u00c2\u0001\u00c2\u0001\u00c2"+
		"\u0001\u00c3\u0001\u00c3\u0001\u00c3\u0001\u00c3\u0001\u00c3\u0003\u00c3"+
		"\u08bd\b\u00c3\u0001\u00c4\u0001\u00c4\u0001\u00c4\u0001\u00c4\u0001\u00c5"+
		"\u0001\u00c5\u0001\u00c5\u0001\u00c5\u0001\u00c5\u0001\u00c5\u0005\u00c5"+
		"\u08c9\b\u00c5\n\u00c5\f\u00c5\u08cc\t\u00c5\u0001\u00c5\u0001\u00c5\u0001"+
		"\u00c6\u0001\u00c6\u0001\u00c6\u0001\u00c6\u0001\u00c6\u0001\u00c6\u0001"+
		"\u00c6\u0001\u00c6\u0001\u00c7\u0001\u00c7\u0001\u00c7\u0001\u00c7\u0001"+
		"\u00c8\u0001\u00c8\u0001\u00c8\u0003\u00c8\u08df\b\u00c8\u0001\u00c9\u0001"+
		"\u00c9\u0005\u00c9\u08e3\b\u00c9\n\u00c9\f\u00c9\u08e6\t\u00c9\u0001\u00ca"+
		"\u0001\u00ca\u0001\u00ca\u0001\u00cb\u0001\u00cb\u0005\u00cb\u08ed\b\u00cb"+
		"\n\u00cb\f\u00cb\u08f0\t\u00cb\u0001\u00cc\u0001\u00cc\u0001\u00cc\u0001"+
		"\u00cd\u0001\u00cd\u0003\u00cd\u08f7\b\u00cd\u0001\u00ce\u0001\u00ce\u0005"+
		"\u00ce\u08fb\b\u00ce\n\u00ce\f\u00ce\u08fe\t\u00ce\u0001\u00cf\u0001\u00cf"+
		"\u0003\u00cf\u0902\b\u00cf\u0001\u00cf\u0001\u00cf\u0001\u00d0\u0001\u00d0"+
		"\u0001\u00d1\u0001\u00d1\u0001\u00d1\u0001\u00d1\u0001\u00d2\u0003\u00d2"+
		"\u090d\b\u00d2\u0001\u00d2\u0001\u00d2\u0001\u00d3\u0001\u00d3\u0001\u00d3"+
		"\u0003\u00d3\u0914\b\u00d3\u0001\u00d4\u0001\u00d4\u0001\u00d4\u0003\u00d4"+
		"\u0919\b\u00d4\u0001\u00d5\u0001\u00d5\u0004\u00d5\u091d\b\u00d5\u000b"+
		"\u00d5\f\u00d5\u091e\u0001\u00d6\u0001\u00d6\u0001\u00d6\u0003\u00d6\u0924"+
		"\b\u00d6\u0001\u00d7\u0001\u00d7\u0001\u00d7\u0001\u00d8\u0001\u00d8\u0001"+
		"\u00d8\u0001\u00d8\u0001\u00d9\u0001\u00d9\u0001\u00d9\u0001\u00d9\u0001"+
		"\u00d9\u0001\u00da\u0001\u00da\u0003\u00da\u0934\b\u00da\u0001\u00da\u0001"+
		"\u00da\u0001\u00da\u0001\u00da\u0001\u00db\u0001\u00db\u0003\u00db\u093c"+
		"\b\u00db\u0001\u00db\u0001\u00db\u0001\u00db\u0001\u00db\u0001\u00dc\u0001"+
		"\u00dc\u0001\u00dc\u0001\u00dc\u0001\u00dd\u0001\u00dd\u0005\u00dd\u0948"+
		"\b\u00dd\n\u00dd\f\u00dd\u094b\t\u00dd\u0001\u00de\u0001\u00de\u0001\u00de"+
		"\u0001\u00df\u0001\u00df\u0003\u00df\u0952\b\u00df\u0001\u00e0\u0001\u00e0"+
		"\u0001\u00e0\u0001\u00e0\u0001\u00e0\u0005\u00e0\u0959\b\u00e0\n\u00e0"+
		"\f\u00e0\u095c\t\u00e0\u0003\u00e0\u095e\b\u00e0\u0001\u00e0\u0001\u00e0"+
		"\u0001\u00e1\u0001\u00e1\u0003\u00e1\u0964\b\u00e1\u0001\u00e2\u0001\u00e2"+
		"\u0001\u00e2\u0003\u00e2\u0969\b\u00e2\u0001\u00e2\u0001\u00e2\u0001\u00e3"+
		"\u0001\u00e3\u0001\u00e4\u0001\u00e4\u0001\u00e4\u0001\u00e4\u0001\u00e4"+
		"\u0001\u00e4\u0001\u00e4\u0003\u00e4\u0976\b\u00e4\u0001\u00e5\u0001\u00e5"+
		"\u0003\u00e5\u097a\b\u00e5\u0001\u00e6\u0001\u00e6\u0001\u00e6\u0001\u00e6"+
		"\u0001\u00e7\u0001\u00e7\u0001\u00e7\u0001\u00e7\u0001\u00e8\u0001\u00e8"+
		"\u0001\u00e8\u0001\u00e8\u0001\u00e8\u0001\u00e8\u0001\u00e8\u0001\u00e8"+
		"\u0001\u00e8\u0001\u00e9\u0001\u00e9\u0003\u00e9\u098f\b\u00e9\u0001\u00ea"+
		"\u0001\u00ea\u0004\u00ea\u0993\b\u00ea\u000b\u00ea\f\u00ea\u0994\u0001"+
		"\u00eb\u0001\u00eb\u0001\u00eb\u0003\u00eb\u099a\b\u00eb\u0001\u00ec\u0001"+
		"\u00ec\u0001\u00ec\u0001\u00ed\u0001\u00ed\u0001\u00ed\u0001\u00ed\u0001"+
		"\u00ee\u0001\u00ee\u0001\u00ee\u0001\u00ee\u0001\u00ee\u0001\u00ef\u0001"+
		"\u00ef\u0001\u00ef\u0003\u00ef\u09ab\b\u00ef\u0001\u00f0\u0001\u00f0\u0001"+
		"\u00f1\u0001\u00f1\u0001\u00f2\u0001\u00f2\u0001\u00f3\u0001\u00f3\u0001"+
		"\u00f3\u0003\u00f3\u09b6\b\u00f3\u0001\u00f4\u0001\u00f4\u0001\u00f4\u0001"+
		"\u00f4\u0001\u00f5\u0001\u00f5\u0003\u00f5\u09be\b\u00f5\u0001\u00f6\u0001"+
		"\u00f6\u0001\u00f6\u0001\u00f6\u0001\u00f7\u0001\u00f7\u0005\u00f7\u09c6"+
		"\b\u00f7\n\u00f7\f\u00f7\u09c9\t\u00f7\u0001\u00f7\u0001\u00f7\u0001\u00f7"+
		"\u0003\u00f7\u09ce\b\u00f7\u0001\u00f7\u0001\u00f7\u0005\u00f7\u09d2\b"+
		"\u00f7\n\u00f7\f\u00f7\u09d5\t\u00f7\u0001\u00f7\u0003\u00f7\u09d8\b\u00f7"+
		"\u0001\u00f7\u0001\u00f7\u0001\u00f8\u0001\u00f8\u0003\u00f8\u09de\b\u00f8"+
		"\u0001\u00f8\u0001\u00f8\u0005\u00f8\u09e2\b\u00f8\n\u00f8\f\u00f8\u09e5"+
		"\t\u00f8\u0001\u00f8\u0003\u00f8\u09e8\b\u00f8\u0001\u00f8\u0001\u00f8"+
		"\u0001\u00f9\u0001\u00f9\u0001\u00f9\u0001\u00f9\u0001\u00fa\u0001\u00fa"+
		"\u0005\u00fa\u09f2\b\u00fa\n\u00fa\f\u00fa\u09f5\t\u00fa\u0001\u00fa\u0001"+
		"\u00fa\u0001\u00fa\u0001\u00fa\u0001\u00fa\u0005\u00fa\u09fc\b\u00fa\n"+
		"\u00fa\f\u00fa\u09ff\t\u00fa\u0001\u00fa\u0001\u00fa\u0003\u00fa\u0a03"+
		"\b\u00fa\u0001\u00fb\u0001\u00fb\u0001\u00fb\u0001\u00fb\u0001\u00fb\u0005"+
		"\u00fb\u0a0a\b\u00fb\n\u00fb\f\u00fb\u0a0d\t\u00fb\u0001\u00fb\u0003\u00fb"+
		"\u0a10\b\u00fb\u0003\u00fb\u0a12\b\u00fb\u0001\u00fb\u0001\u00fb\u0001"+
		"\u00fc\u0001\u00fc\u0001\u00fc\u0001\u00fc\u0001\u00fc\u0003\u00fc\u0a1b"+
		"\b\u00fc\u0001\u00fd\u0001\u00fd\u0001\u00fd\u0001\u00fd\u0001\u00fd\u0001"+
		"\u00fd\u0001\u00fd\u0001\u00fd\u0001\u00fe\u0001\u00fe\u0001\u00fe\u0001"+
		"\u00fe\u0001\u00fe\u0001\u00ff\u0001\u00ff\u0001\u00ff\u0001\u00ff\u0001"+
		"\u00ff\u0001\u0100\u0001\u0100\u0001\u0100\u0001\u0100\u0001\u0100\u0001"+
		"\u0101\u0001\u0101\u0001\u0102\u0001\u0102\u0001\u0103\u0001\u0103\u0001"+
		"\u0104\u0001\u0104\u0001\u0105\u0001\u0105\u0001\u0106\u0001\u0106\u0001"+
		"\u0107\u0001\u0107\u0003\u0107\u0a42\b\u0107\u0001\u0108\u0001\u0108\u0001"+
		"\u0109\u0001\u0109\u0001\u010a\u0001\u010a\u0001\u010b\u0001\u010b\u0001"+
		"\u010b\u0001\u010b\u0001\u010c\u0001\u010c\u0003\u010c\u0a50\b\u010c\u0001"+
		"\u010d\u0001\u010d\u0001\u010d\u0003\u010d\u0a55\b\u010d\u0001\u010e\u0001"+
		"\u010e\u0001\u010e\u0001\u010e\u0003\u010e\u0a5b\b\u010e\u0001\u010f\u0001"+
		"\u010f\u0001\u010f\u0003\u010f\u0a60\b\u010f\u0001\u0110\u0003\u0110\u0a63"+
		"\b\u0110\u0001\u0110\u0001\u0110\u0005\u0110\u0a67\b\u0110\n\u0110\f\u0110"+
		"\u0a6a\t\u0110\u0001\u0111\u0001\u0111\u0001\u0111\u0003\u0111\u0a6f\b"+
		"\u0111\u0001\u0112\u0001\u0112\u0001\u0112\u0001\u0112\u0001\u0112\u0003"+
		"\u0112\u0a76\b\u0112\u0001\u0113\u0001\u0113\u0003\u0113\u0a7a\b\u0113"+
		"\u0001\u0114\u0001\u0114\u0001\u0114\u0001\u0114\u0001\u0114\u0001\u0114"+
		"\u0001\u0114\u0001\u0114\u0001\u0114\u0001\u0114\u0001\u0114\u0003\u0114"+
		"\u0a87\b\u0114\u0001\u0115\u0001\u0115\u0001\u0115\u0001\u0115\u0001\u0115"+
		"\u0001\u0115\u0001\u0115\u0003\u0115\u0a90\b\u0115\u0001\u0116\u0001\u0116"+
		"\u0001\u0116\u0001\u0116\u0001\u0116\u0003\u0116\u0a97\b\u0116\u0001\u0117"+
		"\u0001\u0117\u0003\u0117\u0a9b\b\u0117\u0001\u0118\u0001\u0118\u0001\u0119"+
		"\u0001\u0119\u0001\u011a\u0001\u011a\u0001\u011b\u0001\u011b\u0001\u011c"+
		"\u0001\u011c\u0001\u011d\u0001\u011d\u0001\u011e\u0001\u011e\u0001\u011f"+
		"\u0001\u011f\u0001\u0120\u0001\u0120\u0001\u0121\u0001\u0121\u0001\u0121"+
		"\u0001\u0122\u0001\u0122\u0001\u0122\u0001\u0123\u0001\u0123\u0005\u0123"+
		"\u0ab7\b\u0123\n\u0123\f\u0123\u0aba\t\u0123\u0001\u0124\u0001\u0124\u0001"+
		"\u0124\u0001\u0124\u0001\u0124\u0001\u0125\u0001\u0125\u0001\u0125\u0001"+
		"\u0125\u0001\u0125\u0001\u0125\u0001\u0125\u0001\u0125\u0001\u0125\u0001"+
		"\u0125\u0001\u0125\u0003\u0125\u0acc\b\u0125\u0001\u0126\u0001\u0126\u0001"+
		"\u0126\u0001\u0126\u0005\u0126\u0ad2\b\u0126\n\u0126\f\u0126\u0ad5\t\u0126"+
		"\u0003\u0126\u0ad7\b\u0126\u0001\u0126\u0001\u0126\u0001\u0127\u0001\u0127"+
		"\u0001\u0127\u0001\u0127\u0001\u0128\u0001\u0128\u0001\u0128\u0001\u0128"+
		"\u0005\u0128\u0ae3\b\u0128\n\u0128\f\u0128\u0ae6\t\u0128\u0003\u0128\u0ae8"+
		"\b\u0128\u0001\u0128\u0001\u0128\u0001\u0129\u0001\u0129\u0001\u012a\u0001"+
		"\u012a\u0001\u012b\u0001\u012b\u0001\u012c\u0001\u012c\u0001\u012d\u0001"+
		"\u012d\u0005\u012d\u0af6\b\u012d\n\u012d\f\u012d\u0af9\t\u012d\u0001\u012e"+
		"\u0001\u012e\u0001\u012f\u0003\u012f\u0afe\b\u012f\u0001\u012f\u0001\u012f"+
		"\u0001\u0130\u0003\u0130\u0b03\b\u0130\u0001\u0130\u0001\u0130\u0001\u0130"+
		"\u0000\u0000\u0131\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRTVXZ\\^`bdfh"+
		"jlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092"+
		"\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa"+
		"\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2"+
		"\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0\u00d2\u00d4\u00d6\u00d8\u00da"+
		"\u00dc\u00de\u00e0\u00e2\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2"+
		"\u00f4\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106\u0108\u010a"+
		"\u010c\u010e\u0110\u0112\u0114\u0116\u0118\u011a\u011c\u011e\u0120\u0122"+
		"\u0124\u0126\u0128\u012a\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a"+
		"\u013c\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e\u0150\u0152"+
		"\u0154\u0156\u0158\u015a\u015c\u015e\u0160\u0162\u0164\u0166\u0168\u016a"+
		"\u016c\u016e\u0170\u0172\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182"+
		"\u0184\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194\u0196\u0198\u019a"+
		"\u019c\u019e\u01a0\u01a2\u01a4\u01a6\u01a8\u01aa\u01ac\u01ae\u01b0\u01b2"+
		"\u01b4\u01b6\u01b8\u01ba\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8\u01ca"+
		"\u01cc\u01ce\u01d0\u01d2\u01d4\u01d6\u01d8\u01da\u01dc\u01de\u01e0\u01e2"+
		"\u01e4\u01e6\u01e8\u01ea\u01ec\u01ee\u01f0\u01f2\u01f4\u01f6\u01f8\u01fa"+
		"\u01fc\u01fe\u0200\u0202\u0204\u0206\u0208\u020a\u020c\u020e\u0210\u0212"+
		"\u0214\u0216\u0218\u021a\u021c\u021e\u0220\u0222\u0224\u0226\u0228\u022a"+
		"\u022c\u022e\u0230\u0232\u0234\u0236\u0238\u023a\u023c\u023e\u0240\u0242"+
		"\u0244\u0246\u0248\u024a\u024c\u024e\u0250\u0252\u0254\u0256\u0258\u025a"+
		"\u025c\u025e\u0260\u0000%\u0002\u0000\f\r\u0019\u0019\u0002\u0000\u000e"+
		"\u000e\u001a\u001a\u0001\u0000\u0006\u0007\u0002\u0000NN\u00a1\u00a1\u0001"+
		"\u0000\f\r\u0002\u0000\u009d\u009d\u009f\u009f\u0002\u0000\u009e\u009e"+
		"\u00a0\u00a0\u0002\u0000\u00d8\u00d9\u00e5\u00e5\u0003\u000000LLab\u000f"+
		"\u0000%%,,..44::<<\u008a\u008a\u0092\u0093\u00ca\u00cb\u00e0\u00e0\u00ea"+
		"\u00ea\u00ef\u00ef\u00f2\u00f4\u00fc\u00fc\u013c\u013c\u0004\u0000JJ\u0099"+
		"\u0099\u00e8\u00e9\u00ff\u00ff\u0002\u0000\u0091\u0091\u0095\u0095\u0002"+
		"\u0000pp\u0102\u0102\u0003\u000022\u00a2\u00a2\u00c1\u00c1\u0003\u0000"+
		"**\u008b\u008b\u00a2\u00a2\u0002\u0000\u00bd\u00bd\u00e6\u00e6\u0002\u0000"+
		"00LL\u0002\u0000\\\\\u008b\u008b\u0002\u0000\u0090\u0090\u00f0\u00f0\u0002"+
		"\u0000ZZ\u0103\u0103\r\u00003388CDIIUUq{\u0081\u0081\u0086\u0087\u0089"+
		"\u0089\u00c9\u00c9\u00e7\u00e7\u0105\u0108\u010a\u010b\u000e\u0000338"+
		"8CDIIUUq{\u0081\u0081\u0086\u0087\u0089\u0089\u00c9\u00c9\u00e7\u00e7"+
		"\u0105\u0108\u010a\u010b\u013c\u013c\u0003\u0000\u0012\u0012\u0014\u0014"+
		"\u001c\u001c\u0003\u0000ij\u0082\u0083\u00af\u00b0\u0002\u000066\u00a4"+
		"\u00a4\u0002\u0000\u0016\u0018\u001b\u001b\u0002\u0000\u000b\u000b!!\u0003"+
		"\u0000\u0001\u0001  ##\u000b\u0000\u0013\u0013\u0015\u0015>@OPhhko\u008e"+
		"\u008f\u009a\u009a\u00a5\u00ae\u00b1\u00b6\u00eb\u00ec\u0002\u0000**}"+
		"}\u0003\u0000\u0089\u0089\u0106\u0106\u010a\u010a\u0001\u0000WX\u0004"+
		"\u0000\u0131\u0131\u0133\u0133\u0136\u0137\u0139\u013b\u0004\u0000\u0117"+
		"\u011d\u011f\u0121\u0124\u0129\u0130\u0130\u0001\u0000\u0117\u0130\'\u0000"+
		"&&(*225577;;EEHHJKNNRSYY^_pp||~\u0080\u0084\u0084\u008c\u008d\u0091\u0091"+
		"\u0093\u0095\u0099\u0099\u00a1\u00a2\u00b7\u00b8\u00ba\u00bb\u00bf\u00c0"+
		"\u00c5\u00c6\u00c8\u00c8\u00cc\u00cc\u00d5\u00d7\u00da\u00dc\u00e3\u00e3"+
		"\u00e8\u00e9\u00ed\u00ed\u00f1\u00f1\u00fd\u00fd\u00ff\u0102\u0104\u0104"+
		"\u010c\u0117\u011f\u011f\u0019\u0000\'\'//99=>BBGGMMVWZ[hh\u0082\u0082"+
		"\u0085\u0085\u0090\u0090\u009b\u009b\u00b9\u00b9\u00c2\u00c2\u00cd\u00cd"+
		"\u00dd\u00df\u00e1\u00e2\u00e4\u00e4\u00e6\u00e6\u00ee\u00ee\u00f0\u00f0"+
		"\u00f5\u00fb\u0103\u0103\u0b78\u0000\u0262\u0001\u0000\u0000\u0000\u0002"+
		"\u0264\u0001\u0000\u0000\u0000\u0004\u0278\u0001\u0000\u0000\u0000\u0006"+
		"\u027a\u0001\u0000\u0000\u0000\b\u0285\u0001\u0000\u0000\u0000\n\u0287"+
		"\u0001\u0000\u0000\u0000\f\u028c\u0001\u0000\u0000\u0000\u000e\u0296\u0001"+
		"\u0000\u0000\u0000\u0010\u02a1\u0001\u0000\u0000\u0000\u0012\u02a9\u0001"+
		"\u0000\u0000\u0000\u0014\u02b1\u0001\u0000\u0000\u0000\u0016\u02c1\u0001"+
		"\u0000\u0000\u0000\u0018\u02c3\u0001\u0000\u0000\u0000\u001a\u02c9\u0001"+
		"\u0000\u0000\u0000\u001c\u02cc\u0001\u0000\u0000\u0000\u001e\u02d2\u0001"+
		"\u0000\u0000\u0000 \u02d6\u0001\u0000\u0000\u0000\"\u02e1\u0001\u0000"+
		"\u0000\u0000$\u02e5\u0001\u0000\u0000\u0000&\u02f8\u0001\u0000\u0000\u0000"+
		"(\u02fa\u0001\u0000\u0000\u0000*\u0300\u0001\u0000\u0000\u0000,\u030d"+
		"\u0001\u0000\u0000\u0000.\u0318\u0001\u0000\u0000\u00000\u031c\u0001\u0000"+
		"\u0000\u00002\u0320\u0001\u0000\u0000\u00004\u0329\u0001\u0000\u0000\u0000"+
		"6\u0334\u0001\u0000\u0000\u00008\u0339\u0001\u0000\u0000\u0000:\u033b"+
		"\u0001\u0000\u0000\u0000<\u0347\u0001\u0000\u0000\u0000>\u0357\u0001\u0000"+
		"\u0000\u0000@\u0359\u0001\u0000\u0000\u0000B\u0361\u0001\u0000\u0000\u0000"+
		"D\u0363\u0001\u0000\u0000\u0000F\u0370\u0001\u0000\u0000\u0000H\u0376"+
		"\u0001\u0000\u0000\u0000J\u0378\u0001\u0000\u0000\u0000L\u037a\u0001\u0000"+
		"\u0000\u0000N\u0381\u0001\u0000\u0000\u0000P\u0384\u0001\u0000\u0000\u0000"+
		"R\u0391\u0001\u0000\u0000\u0000T\u03c4\u0001\u0000\u0000\u0000V\u03ca"+
		"\u0001\u0000\u0000\u0000X\u03e5\u0001\u0000\u0000\u0000Z\u03e7\u0001\u0000"+
		"\u0000\u0000\\\u03f0\u0001\u0000\u0000\u0000^\u03f3\u0001\u0000\u0000"+
		"\u0000`\u03fa\u0001\u0000\u0000\u0000b\u0401\u0001\u0000\u0000\u0000d"+
		"\u0404\u0001\u0000\u0000\u0000f\u040f\u0001\u0000\u0000\u0000h\u0411\u0001"+
		"\u0000\u0000\u0000j\u0419\u0001\u0000\u0000\u0000l\u0424\u0001\u0000\u0000"+
		"\u0000n\u0427\u0001\u0000\u0000\u0000p\u0430\u0001\u0000\u0000\u0000r"+
		"\u0432\u0001\u0000\u0000\u0000t\u0440\u0001\u0000\u0000\u0000v\u0443\u0001"+
		"\u0000\u0000\u0000x\u0448\u0001\u0000\u0000\u0000z\u045a\u0001\u0000\u0000"+
		"\u0000|\u0462\u0001\u0000\u0000\u0000~\u046e\u0001\u0000\u0000\u0000\u0080"+
		"\u0479\u0001\u0000\u0000\u0000\u0082\u047b\u0001\u0000\u0000\u0000\u0084"+
		"\u047f\u0001\u0000\u0000\u0000\u0086\u0482\u0001\u0000\u0000\u0000\u0088"+
		"\u0487\u0001\u0000\u0000\u0000\u008a\u0489\u0001\u0000\u0000\u0000\u008c"+
		"\u048e\u0001\u0000\u0000\u0000\u008e\u0490\u0001\u0000\u0000\u0000\u0090"+
		"\u049a\u0001\u0000\u0000\u0000\u0092\u049c\u0001\u0000\u0000\u0000\u0094"+
		"\u04a4\u0001\u0000\u0000\u0000\u0096\u04ab\u0001\u0000\u0000\u0000\u0098"+
		"\u04b1\u0001\u0000\u0000\u0000\u009a\u04b4\u0001\u0000\u0000\u0000\u009c"+
		"\u04bb\u0001\u0000\u0000\u0000\u009e\u04be\u0001\u0000\u0000\u0000\u00a0"+
		"\u04c0\u0001\u0000\u0000\u0000\u00a2\u04c7\u0001\u0000\u0000\u0000\u00a4"+
		"\u04db\u0001\u0000\u0000\u0000\u00a6\u04dd\u0001\u0000\u0000\u0000\u00a8"+
		"\u04e1\u0001\u0000\u0000\u0000\u00aa\u04e3\u0001\u0000\u0000\u0000\u00ac"+
		"\u04ea\u0001\u0000\u0000\u0000\u00ae\u04ef\u0001\u0000\u0000\u0000\u00b0"+
		"\u04f2\u0001\u0000\u0000\u0000\u00b2\u04fb\u0001\u0000\u0000\u0000\u00b4"+
		"\u0500\u0001\u0000\u0000\u0000\u00b6\u0505\u0001\u0000\u0000\u0000\u00b8"+
		"\u050f\u0001\u0000\u0000\u0000\u00ba\u0512\u0001\u0000\u0000\u0000\u00bc"+
		"\u0523\u0001\u0000\u0000\u0000\u00be\u0526\u0001\u0000\u0000\u0000\u00c0"+
		"\u0532\u0001\u0000\u0000\u0000\u00c2\u053d\u0001\u0000\u0000\u0000\u00c4"+
		"\u0540\u0001\u0000\u0000\u0000\u00c6\u054a\u0001\u0000\u0000\u0000\u00c8"+
		"\u0565\u0001\u0000\u0000\u0000\u00ca\u0567\u0001\u0000\u0000\u0000\u00cc"+
		"\u0573\u0001\u0000\u0000\u0000\u00ce\u0584\u0001\u0000\u0000\u0000\u00d0"+
		"\u0588\u0001\u0000\u0000\u0000\u00d2\u058d\u0001\u0000\u0000\u0000\u00d4"+
		"\u0593\u0001\u0000\u0000\u0000\u00d6\u05aa\u0001\u0000\u0000\u0000\u00d8"+
		"\u05ad\u0001\u0000\u0000\u0000\u00da\u05b1\u0001\u0000\u0000\u0000\u00dc"+
		"\u05b5\u0001\u0000\u0000\u0000\u00de\u05c1\u0001\u0000\u0000\u0000\u00e0"+
		"\u05ca\u0001\u0000\u0000\u0000\u00e2\u05d3\u0001\u0000\u0000\u0000\u00e4"+
		"\u05ed\u0001\u0000\u0000\u0000\u00e6\u05f0\u0001\u0000\u0000\u0000\u00e8"+
		"\u05f3\u0001\u0000\u0000\u0000\u00ea\u05f7\u0001\u0000\u0000\u0000\u00ec"+
		"\u05fa\u0001\u0000\u0000\u0000\u00ee\u060c\u0001\u0000\u0000\u0000\u00f0"+
		"\u0610\u0001\u0000\u0000\u0000\u00f2\u0618\u0001\u0000\u0000\u0000\u00f4"+
		"\u061e\u0001\u0000\u0000\u0000\u00f6\u0622\u0001\u0000\u0000\u0000\u00f8"+
		"\u0628\u0001\u0000\u0000\u0000\u00fa\u0634\u0001\u0000\u0000\u0000\u00fc"+
		"\u063a\u0001\u0000\u0000\u0000\u00fe\u0642\u0001\u0000\u0000\u0000\u0100"+
		"\u0648\u0001\u0000\u0000\u0000\u0102\u0654\u0001\u0000\u0000\u0000\u0104"+
		"\u0664\u0001\u0000\u0000\u0000\u0106\u0669\u0001\u0000\u0000\u0000\u0108"+
		"\u066d\u0001\u0000\u0000\u0000\u010a\u0671\u0001\u0000\u0000\u0000\u010c"+
		"\u0680\u0001\u0000\u0000\u0000\u010e\u0683\u0001\u0000\u0000\u0000\u0110"+
		"\u068c\u0001\u0000\u0000\u0000\u0112\u0697\u0001\u0000\u0000\u0000\u0114"+
		"\u06a0\u0001\u0000\u0000\u0000\u0116\u06ab\u0001\u0000\u0000\u0000\u0118"+
		"\u06b6\u0001\u0000\u0000\u0000\u011a\u06c1\u0001\u0000\u0000\u0000\u011c"+
		"\u06c5\u0001\u0000\u0000\u0000\u011e\u06d1\u0001\u0000\u0000\u0000\u0120"+
		"\u06da\u0001\u0000\u0000\u0000\u0122\u06e0\u0001\u0000\u0000\u0000\u0124"+
		"\u06ef\u0001\u0000\u0000\u0000\u0126\u0726\u0001\u0000\u0000\u0000\u0128"+
		"\u0728\u0001\u0000\u0000\u0000\u012a\u073d\u0001\u0000\u0000\u0000\u012c"+
		"\u073f\u0001\u0000\u0000\u0000\u012e\u074a\u0001\u0000\u0000\u0000\u0130"+
		"\u0753\u0001\u0000\u0000\u0000\u0132\u076c\u0001\u0000\u0000\u0000\u0134"+
		"\u0772\u0001\u0000\u0000\u0000\u0136\u077c\u0001\u0000\u0000\u0000\u0138"+
		"\u0788\u0001\u0000\u0000\u0000\u013a\u0797\u0001\u0000\u0000\u0000\u013c"+
		"\u079b\u0001\u0000\u0000\u0000\u013e\u07a4\u0001\u0000\u0000\u0000\u0140"+
		"\u07a8\u0001\u0000\u0000\u0000\u0142\u07ba\u0001\u0000\u0000\u0000\u0144"+
		"\u07be\u0001\u0000\u0000\u0000\u0146\u07ca\u0001\u0000\u0000\u0000\u0148"+
		"\u07d9\u0001\u0000\u0000\u0000\u014a\u07e9\u0001\u0000\u0000\u0000\u014c"+
		"\u07ed\u0001\u0000\u0000\u0000\u014e\u07f3\u0001\u0000\u0000\u0000\u0150"+
		"\u0807\u0001\u0000\u0000\u0000\u0152\u080f\u0001\u0000\u0000\u0000\u0154"+
		"\u0813\u0001\u0000\u0000\u0000\u0156\u081c\u0001\u0000\u0000\u0000\u0158"+
		"\u0827\u0001\u0000\u0000\u0000\u015a\u082e\u0001\u0000\u0000\u0000\u015c"+
		"\u0831\u0001\u0000\u0000\u0000\u015e\u0839\u0001\u0000\u0000\u0000\u0160"+
		"\u0845\u0001\u0000\u0000\u0000\u0162\u084a\u0001\u0000\u0000\u0000\u0164"+
		"\u085c\u0001\u0000\u0000\u0000\u0166\u085e\u0001\u0000\u0000\u0000\u0168"+
		"\u0869\u0001\u0000\u0000\u0000\u016a\u086b\u0001\u0000\u0000\u0000\u016c"+
		"\u0872\u0001\u0000\u0000\u0000\u016e\u0875\u0001\u0000\u0000\u0000\u0170"+
		"\u087b\u0001\u0000\u0000\u0000\u0172\u0881\u0001\u0000\u0000\u0000\u0174"+
		"\u0888\u0001\u0000\u0000\u0000\u0176\u088e\u0001\u0000\u0000\u0000\u0178"+
		"\u0892\u0001\u0000\u0000\u0000\u017a\u089d\u0001\u0000\u0000\u0000\u017c"+
		"\u08a1\u0001\u0000\u0000\u0000\u017e\u08a3\u0001\u0000\u0000\u0000\u0180"+
		"\u08aa\u0001\u0000\u0000\u0000\u0182\u08ad\u0001\u0000\u0000\u0000\u0184"+
		"\u08b4\u0001\u0000\u0000\u0000\u0186\u08bc\u0001\u0000\u0000\u0000\u0188"+
		"\u08be\u0001\u0000\u0000\u0000\u018a\u08c2\u0001\u0000\u0000\u0000\u018c"+
		"\u08cf\u0001\u0000\u0000\u0000\u018e\u08d7\u0001\u0000\u0000\u0000\u0190"+
		"\u08db\u0001\u0000\u0000\u0000\u0192\u08e0\u0001\u0000\u0000\u0000\u0194"+
		"\u08e7\u0001\u0000\u0000\u0000\u0196\u08ea\u0001\u0000\u0000\u0000\u0198"+
		"\u08f1\u0001\u0000\u0000\u0000\u019a\u08f6\u0001\u0000\u0000\u0000\u019c"+
		"\u08f8\u0001\u0000\u0000\u0000\u019e\u0901\u0001\u0000\u0000\u0000\u01a0"+
		"\u0905\u0001\u0000\u0000\u0000\u01a2\u0907\u0001\u0000\u0000\u0000\u01a4"+
		"\u090c\u0001\u0000\u0000\u0000\u01a6\u0913\u0001\u0000\u0000\u0000\u01a8"+
		"\u0918\u0001\u0000\u0000\u0000\u01aa\u091a\u0001\u0000\u0000\u0000\u01ac"+
		"\u0923\u0001\u0000\u0000\u0000\u01ae\u0925\u0001\u0000\u0000\u0000\u01b0"+
		"\u0928\u0001\u0000\u0000\u0000\u01b2\u092c\u0001\u0000\u0000\u0000\u01b4"+
		"\u0931\u0001\u0000\u0000\u0000\u01b6\u0939\u0001\u0000\u0000\u0000\u01b8"+
		"\u0941\u0001\u0000\u0000\u0000\u01ba\u0945\u0001\u0000\u0000\u0000\u01bc"+
		"\u094c\u0001\u0000\u0000\u0000\u01be\u0951\u0001\u0000\u0000\u0000\u01c0"+
		"\u0953\u0001\u0000\u0000\u0000\u01c2\u0963\u0001\u0000\u0000\u0000\u01c4"+
		"\u0965\u0001\u0000\u0000\u0000\u01c6\u096c\u0001\u0000\u0000\u0000\u01c8"+
		"\u0975\u0001\u0000\u0000\u0000\u01ca\u0977\u0001\u0000\u0000\u0000\u01cc"+
		"\u097b\u0001\u0000\u0000\u0000\u01ce\u097f\u0001\u0000\u0000\u0000\u01d0"+
		"\u0983\u0001\u0000\u0000\u0000\u01d2\u098e\u0001\u0000\u0000\u0000\u01d4"+
		"\u0990\u0001\u0000\u0000\u0000\u01d6\u0999\u0001\u0000\u0000\u0000\u01d8"+
		"\u099b\u0001\u0000\u0000\u0000\u01da\u099e\u0001\u0000\u0000\u0000\u01dc"+
		"\u09a2\u0001\u0000\u0000\u0000\u01de\u09aa\u0001\u0000\u0000\u0000\u01e0"+
		"\u09ac\u0001\u0000\u0000\u0000\u01e2\u09ae\u0001\u0000\u0000\u0000\u01e4"+
		"\u09b0\u0001\u0000\u0000\u0000\u01e6\u09b5\u0001\u0000\u0000\u0000\u01e8"+
		"\u09b7\u0001\u0000\u0000\u0000\u01ea\u09bd\u0001\u0000\u0000\u0000\u01ec"+
		"\u09bf\u0001\u0000\u0000\u0000\u01ee\u09c3\u0001\u0000\u0000\u0000\u01f0"+
		"\u09db\u0001\u0000\u0000\u0000\u01f2\u09eb\u0001\u0000\u0000\u0000\u01f4"+
		"\u09ef\u0001\u0000\u0000\u0000\u01f6\u0a04\u0001\u0000\u0000\u0000\u01f8"+
		"\u0a15\u0001\u0000\u0000\u0000\u01fa\u0a1c\u0001\u0000\u0000\u0000\u01fc"+
		"\u0a24\u0001\u0000\u0000\u0000\u01fe\u0a29\u0001\u0000\u0000\u0000\u0200"+
		"\u0a2e\u0001\u0000\u0000\u0000\u0202\u0a33\u0001\u0000\u0000\u0000\u0204"+
		"\u0a35\u0001\u0000\u0000\u0000\u0206\u0a37\u0001\u0000\u0000\u0000\u0208"+
		"\u0a39\u0001\u0000\u0000\u0000\u020a\u0a3b\u0001\u0000\u0000\u0000\u020c"+
		"\u0a3d\u0001\u0000\u0000\u0000\u020e\u0a41\u0001\u0000\u0000\u0000\u0210"+
		"\u0a43\u0001\u0000\u0000\u0000\u0212\u0a45\u0001\u0000\u0000\u0000\u0214"+
		"\u0a47\u0001\u0000\u0000\u0000\u0216\u0a49\u0001\u0000\u0000\u0000\u0218"+
		"\u0a4f\u0001\u0000\u0000\u0000\u021a\u0a54\u0001\u0000\u0000\u0000\u021c"+
		"\u0a5a\u0001\u0000\u0000\u0000\u021e\u0a5f\u0001\u0000\u0000\u0000\u0220"+
		"\u0a62\u0001\u0000\u0000\u0000\u0222\u0a6e\u0001\u0000\u0000\u0000\u0224"+
		"\u0a75\u0001\u0000\u0000\u0000\u0226\u0a79\u0001\u0000\u0000\u0000\u0228"+
		"\u0a86\u0001\u0000\u0000\u0000\u022a\u0a8f\u0001\u0000\u0000\u0000\u022c"+
		"\u0a96\u0001\u0000\u0000\u0000\u022e\u0a9a\u0001\u0000\u0000\u0000\u0230"+
		"\u0a9c\u0001\u0000\u0000\u0000\u0232\u0a9e\u0001\u0000\u0000\u0000\u0234"+
		"\u0aa0\u0001\u0000\u0000\u0000\u0236\u0aa2\u0001\u0000\u0000\u0000\u0238"+
		"\u0aa4\u0001\u0000\u0000\u0000\u023a\u0aa6\u0001\u0000\u0000\u0000\u023c"+
		"\u0aa8\u0001\u0000\u0000\u0000\u023e\u0aaa\u0001\u0000\u0000\u0000\u0240"+
		"\u0aac\u0001\u0000\u0000\u0000\u0242\u0aae\u0001\u0000\u0000\u0000\u0244"+
		"\u0ab1\u0001\u0000\u0000\u0000\u0246\u0ab4\u0001\u0000\u0000\u0000\u0248"+
		"\u0abb\u0001\u0000\u0000\u0000\u024a\u0acb\u0001\u0000\u0000\u0000\u024c"+
		"\u0acd\u0001\u0000\u0000\u0000\u024e\u0ada\u0001\u0000\u0000\u0000\u0250"+
		"\u0ade\u0001\u0000\u0000\u0000\u0252\u0aeb\u0001\u0000\u0000\u0000\u0254"+
		"\u0aed\u0001\u0000\u0000\u0000\u0256\u0aef\u0001\u0000\u0000\u0000\u0258"+
		"\u0af1\u0001\u0000\u0000\u0000\u025a\u0af3\u0001\u0000\u0000\u0000\u025c"+
		"\u0afa\u0001\u0000\u0000\u0000\u025e\u0afd\u0001\u0000\u0000\u0000\u0260"+
		"\u0b02\u0001\u0000\u0000\u0000\u0262\u0263\u0003\u0002\u0001\u0000\u0263"+
		"\u0001\u0001\u0000\u0000\u0000\u0264\u0269\u0003\u0004\u0002\u0000\u0265"+
		"\u0266\u0005\"\u0000\u0000\u0266\u0268\u0003\u0004\u0002\u0000\u0267\u0265"+
		"\u0001\u0000\u0000\u0000\u0268\u026b\u0001\u0000\u0000\u0000\u0269\u0267"+
		"\u0001\u0000\u0000\u0000\u0269\u026a\u0001\u0000\u0000\u0000\u026a\u026d"+
		"\u0001\u0000\u0000\u0000\u026b\u0269\u0001\u0000\u0000\u0000\u026c\u026e"+
		"\u0005\"\u0000\u0000\u026d\u026c\u0001\u0000\u0000\u0000\u026d\u026e\u0001"+
		"\u0000\u0000\u0000\u026e\u026f\u0001\u0000\u0000\u0000\u026f\u0270\u0005"+
		"\u0000\u0000\u0001\u0270\u0003\u0001\u0000\u0000\u0000\u0271\u0279\u0003"+
		"\u0006\u0003\u0000\u0272\u0279\u0003(\u0014\u0000\u0273\u0279\u0003D\""+
		"\u0000\u0274\u0279\u0003\b\u0004\u0000\u0275\u0279\u0003H$\u0000\u0276"+
		"\u0279\u0003<\u001e\u0000\u0277\u0279\u0003@ \u0000\u0278\u0271\u0001"+
		"\u0000\u0000\u0000\u0278\u0272\u0001\u0000\u0000\u0000\u0278\u0273\u0001"+
		"\u0000\u0000\u0000\u0278\u0274\u0001\u0000\u0000\u0000\u0278\u0275\u0001"+
		"\u0000\u0000\u0000\u0278\u0276\u0001\u0000\u0000\u0000\u0278\u0277\u0001"+
		"\u0000\u0000\u0000\u0279\u0005\u0001\u0000\u0000\u0000\u027a\u027b\u0005"+
		")\u0000\u0000\u027b\u027c\u0005E\u0000\u0000\u027c\u027d\u0003\u021a\u010d"+
		"\u0000\u027d\u027e\u0005\u0011\u0000\u0000\u027e\u027f\u0003\u017c\u00be"+
		"\u0000\u027f\u0007\u0001\u0000\u0000\u0000\u0280\u0286\u0003\f\u0006\u0000"+
		"\u0281\u0286\u0003\u000e\u0007\u0000\u0282\u0286\u0003\n\u0005\u0000\u0283"+
		"\u0286\u0003\u0012\t\u0000\u0284\u0286\u0003\u0014\n\u0000\u0285\u0280"+
		"\u0001\u0000\u0000\u0000\u0285\u0281\u0001\u0000\u0000\u0000\u0285\u0282"+
		"\u0001\u0000\u0000\u0000\u0285\u0283\u0001\u0000\u0000\u0000\u0285\u0284"+
		"\u0001\u0000\u0000\u0000\u0286\t\u0001\u0000\u0000\u0000\u0287\u0288\u0005"+
		"\u008d\u0000\u0000\u0288\u0289\u0003\u021a\u010d\u0000\u0289\u028a\u0005"+
		"\u0011\u0000\u0000\u028a\u028b\u0003J%\u0000\u028b\u000b\u0001\u0000\u0000"+
		"\u0000\u028c\u028d\u0005\u008d\u0000\u0000\u028d\u028e\u0003\u021a\u010d"+
		"\u0000\u028e\u028f\u0005\u0011\u0000\u0000\u028f\u0291\u0005\u001f\u0000"+
		"\u0000\u0290\u0292\u0003\u0016\u000b\u0000\u0291\u0290\u0001\u0000\u0000"+
		"\u0000\u0291\u0292\u0001\u0000\u0000\u0000\u0292\u0293\u0001\u0000\u0000"+
		"\u0000\u0293\u0294\u0005\b\u0000\u0000\u0294\u0295\u0003$\u0012\u0000"+
		"\u0295\r\u0001\u0000\u0000\u0000\u0296\u0297\u0005\u008d\u0000\u0000\u0297"+
		"\u0298\u0003\u021a\u010d\u0000\u0298\u0299\u0005\u0011\u0000\u0000\u0299"+
		"\u029a\u0005\u0101\u0000\u0000\u029a\u029c\u0005\u001f\u0000\u0000\u029b"+
		"\u029d\u0003\u0010\b\u0000\u029c\u029b\u0001\u0000\u0000\u0000\u029c\u029d"+
		"\u0001\u0000\u0000\u0000\u029d\u029e\u0001\u0000\u0000\u0000\u029e\u029f"+
		"\u0005\b\u0000\u0000\u029f\u02a0\u0003$\u0012\u0000\u02a0\u000f\u0001"+
		"\u0000\u0000\u0000\u02a1\u02a6\u0003\u0018\f\u0000\u02a2\u02a3\u0005\t"+
		"\u0000\u0000\u02a3\u02a5\u0003\u0018\f\u0000\u02a4\u02a2\u0001\u0000\u0000"+
		"\u0000\u02a5\u02a8\u0001\u0000\u0000\u0000\u02a6\u02a4\u0001\u0000\u0000"+
		"\u0000\u02a6\u02a7\u0001\u0000\u0000\u0000\u02a7\u0011\u0001\u0000\u0000"+
		"\u0000\u02a8\u02a6\u0001\u0000\u0000\u0000\u02a9\u02aa\u0005\u008d\u0000"+
		"\u0000\u02aa\u02ab\u0003\u021a\u010d\u0000\u02ab\u02ac\u0005\u0011\u0000"+
		"\u0000\u02ac\u02ad\u0005\u009b\u0000\u0000\u02ad\u02ae\u0005\u001f\u0000"+
		"\u0000\u02ae\u02af\u0003L&\u0000\u02af\u02b0\u0005\b\u0000\u0000\u02b0"+
		"\u0013\u0001\u0000\u0000\u0000\u02b1\u02b2\u0005\u008d\u0000\u0000\u02b2"+
		"\u02b3\u0003\u021a\u010d\u0000\u02b3\u02b4\u0005\u0011\u0000\u0000\u02b4"+
		"\u02b5\u0003\u00cae\u0000\u02b5\u0015\u0001\u0000\u0000\u0000\u02b6\u02b7"+
		"\u0003\u001c\u000e\u0000\u02b7\u02b8\u0005\t\u0000\u0000\u02b8\u02b9\u0003"+
		"\u001c\u000e\u0000\u02b9\u02ba\u0001\u0000\u0000\u0000\u02ba\u02bb\u0005"+
		"\t\u0000\u0000\u02bb\u02bc\u0003\u0018\f\u0000\u02bc\u02c2\u0001\u0000"+
		"\u0000\u0000\u02bd\u02be\u0003\u0018\f\u0000\u02be\u02bf\u0005\t\u0000"+
		"\u0000\u02bf\u02c0\u0003\u0018\f\u0000\u02c0\u02c2\u0001\u0000\u0000\u0000"+
		"\u02c1\u02b6\u0001\u0000\u0000\u0000\u02c1\u02bd\u0001\u0000\u0000\u0000"+
		"\u02c2\u0017\u0001\u0000\u0000\u0000\u02c3\u02c4\u0003\u0206\u0103\u0000"+
		"\u02c4\u02c5\u0005\n\u0000\u0000\u02c5\u02c7\u0003\u0202\u0101\u0000\u02c6"+
		"\u02c8\u0003\u001a\r\u0000\u02c7\u02c6\u0001\u0000\u0000\u0000\u02c7\u02c8"+
		"\u0001\u0000\u0000\u0000\u02c8\u0019\u0001\u0000\u0000\u0000\u02c9\u02ca"+
		"\u0005\u0011\u0000\u0000\u02ca\u02cb\u0003\u0226\u0113\u0000\u02cb\u001b"+
		"\u0001\u0000\u0000\u0000\u02cc\u02cd\u0003\u0206\u0103\u0000\u02cd\u02d0"+
		"\u0005\n\u0000\u0000\u02ce\u02d1\u0003\u001e\u000f\u0000\u02cf\u02d1\u0003"+
		" \u0010\u0000\u02d0\u02ce\u0001\u0000\u0000\u0000\u02d0\u02cf\u0001\u0000"+
		"\u0000\u0000\u02d1\u001d\u0001\u0000\u0000\u0000\u02d2\u02d3\u0005\u001f"+
		"\u0000\u0000\u02d3\u02d4\u0005\u0001\u0000\u0000\u02d4\u02d5\u0005\b\u0000"+
		"\u0000\u02d5\u001f\u0001\u0000\u0000\u0000\u02d6\u02d7\u0005\u001f\u0000"+
		"\u0000\u02d7\u02dc\u0003\"\u0011\u0000\u02d8\u02d9\u0005\t\u0000\u0000"+
		"\u02d9\u02db\u0003\"\u0011\u0000\u02da\u02d8\u0001\u0000\u0000\u0000\u02db"+
		"\u02de\u0001\u0000\u0000\u0000\u02dc\u02da\u0001\u0000\u0000\u0000\u02dc"+
		"\u02dd\u0001\u0000\u0000\u0000\u02dd\u02df\u0001\u0000\u0000\u0000\u02de"+
		"\u02dc\u0001\u0000\u0000\u0000\u02df\u02e0\u0005\b\u0000\u0000\u02e0!"+
		"\u0001\u0000\u0000\u0000\u02e1\u02e2\u0003\u0206\u0103\u0000\u02e2\u02e3"+
		"\u0005\n\u0000\u0000\u02e3\u02e4\u0003\u0202\u0101\u0000\u02e4#\u0001"+
		"\u0000\u0000\u0000\u02e5\u02eb\u0005\u001d\u0000\u0000\u02e6\u02e7\u0003"+
		"&\u0013\u0000\u02e7\u02e8\u0005\"\u0000\u0000\u02e8\u02ea\u0001\u0000"+
		"\u0000\u0000\u02e9\u02e6\u0001\u0000\u0000\u0000\u02ea\u02ed\u0001\u0000"+
		"\u0000\u0000\u02eb\u02e9\u0001\u0000\u0000\u0000\u02eb\u02ec\u0001\u0000"+
		"\u0000\u0000\u02ec\u02ef\u0001\u0000\u0000\u0000\u02ed\u02eb\u0001\u0000"+
		"\u0000\u0000\u02ee\u02f0\u0003J%\u0000\u02ef\u02ee\u0001\u0000\u0000\u0000"+
		"\u02ef\u02f0\u0001\u0000\u0000\u0000\u02f0\u02f2\u0001\u0000\u0000\u0000"+
		"\u02f1\u02f3\u0005\"\u0000\u0000\u02f2\u02f1\u0001\u0000\u0000\u0000\u02f2"+
		"\u02f3\u0001\u0000\u0000\u0000\u02f3\u02f4\u0001\u0000\u0000\u0000\u02f4"+
		"\u02f5\u0005\u0004\u0000\u0000\u02f5%\u0001\u0000\u0000\u0000\u02f6\u02f9"+
		"\u0003\b\u0004\u0000\u02f7\u02f9\u0003D\"\u0000\u02f8\u02f6\u0001\u0000"+
		"\u0000\u0000\u02f8\u02f7\u0001\u0000\u0000\u0000\u02f9\'\u0001\u0000\u0000"+
		"\u0000\u02fa\u02fb\u0005H\u0000\u0000\u02fb\u02fc\u0005\u00c8\u0000\u0000"+
		"\u02fc\u02fe\u0003\u0208\u0104\u0000\u02fd\u02ff\u0003*\u0015\u0000\u02fe"+
		"\u02fd\u0001\u0000\u0000\u0000\u02fe\u02ff\u0001\u0000\u0000\u0000\u02ff"+
		")\u0001\u0000\u0000\u0000\u0300\u0301\u0005\u0011\u0000\u0000\u0301\u0303"+
		"\u0003,\u0016\u0000\u0302\u0304\u00030\u0018\u0000\u0303\u0302\u0001\u0000"+
		"\u0000\u0000\u0303\u0304\u0001\u0000\u0000\u0000\u0304\u0305\u0001\u0000"+
		"\u0000\u0000\u0305\u0307\u0005\u001d\u0000\u0000\u0306\u0308\u00032\u0019"+
		"\u0000\u0307\u0306\u0001\u0000\u0000\u0000\u0308\u0309\u0001\u0000\u0000"+
		"\u0000\u0309\u0307\u0001\u0000\u0000\u0000\u0309\u030a\u0001\u0000\u0000"+
		"\u0000\u030a\u030b\u0001\u0000\u0000\u0000\u030b\u030c\u0005\u0004\u0000"+
		"\u0000\u030c+\u0001\u0000\u0000\u0000\u030d\u030e\u0005\u001f\u0000\u0000"+
		"\u030e\u0313\u0003.\u0017\u0000\u030f\u0310\u0005\t\u0000\u0000\u0310"+
		"\u0312\u0003.\u0017\u0000\u0311\u030f\u0001\u0000\u0000\u0000\u0312\u0315"+
		"\u0001\u0000\u0000\u0000\u0313\u0311\u0001\u0000\u0000\u0000\u0313\u0314"+
		"\u0001\u0000\u0000\u0000\u0314\u0316\u0001\u0000\u0000\u0000\u0315\u0313"+
		"\u0001\u0000\u0000\u0000\u0316\u0317\u0005\b\u0000\u0000\u0317-\u0001"+
		"\u0000\u0000\u0000\u0318\u0319\u0003\u0206\u0103\u0000\u0319\u031a\u0005"+
		"\n\u0000\u0000\u031a\u031b\u0003\u0202\u0101\u0000\u031b/\u0001\u0000"+
		"\u0000\u0000\u031c\u031d\u0005\u001e\u0000\u0000\u031d\u031e\u0003.\u0017"+
		"\u0000\u031e\u031f\u0005\u0005\u0000\u0000\u031f1\u0001\u0000\u0000\u0000"+
		"\u0320\u0322\u00034\u001a\u0000\u0321\u0323\u00036\u001b\u0000\u0322\u0321"+
		"\u0001\u0000\u0000\u0000\u0322\u0323\u0001\u0000\u0000\u0000\u0323\u0324"+
		"\u0001\u0000\u0000\u0000\u0324\u0325\u0005\u0011\u0000\u0000\u0325\u0327"+
		"\u0003:\u001d\u0000\u0326\u0328\u0005\"\u0000\u0000\u0327\u0326\u0001"+
		"\u0000\u0000\u0000\u0327\u0328\u0001\u0000\u0000\u0000\u03283\u0001\u0000"+
		"\u0000\u0000\u0329\u032a\u0005\u001f\u0000\u0000\u032a\u032f\u00038\u001c"+
		"\u0000\u032b\u032c\u0005\t\u0000\u0000\u032c\u032e\u00038\u001c\u0000"+
		"\u032d\u032b\u0001\u0000\u0000\u0000\u032e\u0331\u0001\u0000\u0000\u0000"+
		"\u032f\u032d\u0001\u0000\u0000\u0000\u032f\u0330\u0001\u0000\u0000\u0000"+
		"\u0330\u0332\u0001\u0000\u0000\u0000\u0331\u032f\u0001\u0000\u0000\u0000"+
		"\u0332\u0333\u0005\b\u0000\u0000\u03335\u0001\u0000\u0000\u0000\u0334"+
		"\u0335\u0005\u000f\u0000\u0000\u0335\u0336\u0005\u001e\u0000\u0000\u0336"+
		"\u0337\u00038\u001c\u0000\u0337\u0338\u0005\u0005\u0000\u0000\u03387\u0001"+
		"\u0000\u0000\u0000\u0339\u033a\u0003\u0246\u0123\u0000\u033a9\u0001\u0000"+
		"\u0000\u0000\u033b\u0341\u0005\u001d\u0000\u0000\u033c\u033d\u0003&\u0013"+
		"\u0000\u033d\u033e\u0005\"\u0000\u0000\u033e\u0340\u0001\u0000\u0000\u0000"+
		"\u033f\u033c\u0001\u0000\u0000\u0000\u0340\u0343\u0001\u0000\u0000\u0000"+
		"\u0341\u033f\u0001\u0000\u0000\u0000\u0341\u0342\u0001\u0000\u0000\u0000"+
		"\u0342\u0344\u0001\u0000\u0000\u0000\u0343\u0341\u0001\u0000\u0000\u0000"+
		"\u0344\u0345\u0003J%\u0000\u0345\u0346\u0005\u0004\u0000\u0000\u0346;"+
		"\u0001\u0000\u0000\u0000\u0347\u0348\u0005\u00dc\u0000\u0000\u0348\u0349"+
		"\u0005&\u0000\u0000\u0349\u034a\u0005\u00f6\u0000\u0000\u034a\u034b\u0005"+
		"\u001f\u0000\u0000\u034b\u0350\u0003>\u001f\u0000\u034c\u034d\u0005\t"+
		"\u0000\u0000\u034d\u034f\u0003>\u001f\u0000\u034e\u034c\u0001\u0000\u0000"+
		"\u0000\u034f\u0352\u0001\u0000\u0000\u0000\u0350\u034e\u0001\u0000\u0000"+
		"\u0000\u0350\u0351\u0001\u0000\u0000\u0000\u0351\u0353\u0001\u0000\u0000"+
		"\u0000\u0352\u0350\u0001\u0000\u0000\u0000\u0353\u0354\u0005\b\u0000\u0000"+
		"\u0354=\u0001\u0000\u0000\u0000\u0355\u0358\u0003\u0208\u0104\u0000\u0356"+
		"\u0358\u0003\u01e6\u00f3\u0000\u0357\u0355\u0001\u0000\u0000\u0000\u0357"+
		"\u0356\u0001\u0000\u0000\u0000\u0358?\u0001\u0000\u0000\u0000\u0359\u035a"+
		"\u0005\u00e4\u0000\u0000\u035a\u035d\u0003\u0218\u010c\u0000\u035b\u035c"+
		"\u0005\u0011\u0000\u0000\u035c\u035e\u0003B!\u0000\u035d\u035b\u0001\u0000"+
		"\u0000\u0000\u035d\u035e\u0001\u0000\u0000\u0000\u035eA\u0001\u0000\u0000"+
		"\u0000\u035f\u0362\u0003\u0218\u010c\u0000\u0360\u0362\u0003\u0226\u0113"+
		"\u0000\u0361\u035f\u0001\u0000\u0000\u0000\u0361\u0360\u0001\u0000\u0000"+
		"\u0000\u0362C\u0001\u0000\u0000\u0000\u0363\u0364\u0005H\u0000\u0000\u0364"+
		"\u0365\u0005\u00d5\u0000\u0000\u0365\u0366\u0005\u001f\u0000\u0000\u0366"+
		"\u036b\u0003F#\u0000\u0367\u0368\u0005\t\u0000\u0000\u0368\u036a\u0003"+
		"F#\u0000\u0369\u0367\u0001\u0000\u0000\u0000\u036a\u036d\u0001\u0000\u0000"+
		"\u0000\u036b\u0369\u0001\u0000\u0000\u0000\u036b\u036c\u0001\u0000\u0000"+
		"\u0000\u036c\u036e\u0001\u0000\u0000\u0000\u036d\u036b\u0001\u0000\u0000"+
		"\u0000\u036e\u036f\u0005\b\u0000\u0000\u036fE\u0001\u0000\u0000\u0000"+
		"\u0370\u0371\u0003\u0206\u0103\u0000\u0371\u0372\u0005\n\u0000\u0000\u0372"+
		"\u0374\u0003\u0202\u0101\u0000\u0373\u0375\u0003\u001a\r\u0000\u0374\u0373"+
		"\u0001\u0000\u0000\u0000\u0374\u0375\u0001\u0000\u0000\u0000\u0375G\u0001"+
		"\u0000\u0000\u0000\u0376\u0377\u0003J%\u0000\u0377I\u0001\u0000\u0000"+
		"\u0000\u0378\u0379\u0003L&\u0000\u0379K\u0001\u0000\u0000\u0000\u037a"+
		"\u037e\u0003R)\u0000\u037b\u037d\u0003N\'\u0000\u037c\u037b\u0001\u0000"+
		"\u0000\u0000\u037d\u0380\u0001\u0000\u0000\u0000\u037e\u037c\u0001\u0000"+
		"\u0000\u0000\u037e\u037f\u0001\u0000\u0000\u0000\u037fM\u0001\u0000\u0000"+
		"\u0000\u0380\u037e\u0001\u0000\u0000\u0000\u0381\u0382\u0005\u0003\u0000"+
		"\u0000\u0382\u0383\u0003T*\u0000\u0383O\u0001\u0000\u0000\u0000\u0384"+
		"\u0388\u0003T*\u0000\u0385\u0387\u0003N\'\u0000\u0386\u0385\u0001\u0000"+
		"\u0000\u0000\u0387\u038a\u0001\u0000\u0000\u0000\u0388\u0386\u0001\u0000"+
		"\u0000\u0000\u0388\u0389\u0001\u0000\u0000\u0000\u0389Q\u0001\u0000\u0000"+
		"\u0000\u038a\u0388\u0001\u0000\u0000\u0000\u038b\u0392\u0003V+\u0000\u038c"+
		"\u0392\u0003\u010e\u0087\u0000\u038d\u0392\u0003\u00c6c\u0000\u038e\u0392"+
		"\u0003\u01d0\u00e8\u0000\u038f\u0392\u0003\u017a\u00bd\u0000\u0390\u0392"+
		"\u0003\u017c\u00be\u0000\u0391\u038b\u0001\u0000\u0000\u0000\u0391\u038c"+
		"\u0001\u0000\u0000\u0000\u0391\u038d\u0001\u0000\u0000\u0000\u0391\u038e"+
		"\u0001\u0000\u0000\u0000\u0391\u038f\u0001\u0000\u0000\u0000\u0391\u0390"+
		"\u0001\u0000\u0000\u0000\u0392S\u0001\u0000\u0000\u0000\u0393\u03c5\u0003"+
		"Z-\u0000\u0394\u03c5\u0003\\.\u0000\u0395\u03c5\u0003^/\u0000\u0396\u03c5"+
		"\u0003`0\u0000\u0397\u03c5\u0003d2\u0000\u0398\u03c5\u0003p8\u0000\u0399"+
		"\u03c5\u0003n7\u0000\u039a\u03c5\u0003r9\u0000\u039b\u03c5\u0003x<\u0000"+
		"\u039c\u03c5\u0003\u0094J\u0000\u039d\u03c5\u0003\u009eO\u0000\u039e\u03c5"+
		"\u0003\u00a0P\u0000\u039f\u03c5\u0003\u00a2Q\u0000\u03a0\u03c5\u0003\u00b2"+
		"Y\u0000\u03a1\u03c5\u0003\u00ba]\u0000\u03a2\u03c5\u0003\u00b4Z\u0000"+
		"\u03a3\u03c5\u0003\u00bc^\u0000\u03a4\u03c5\u0003\u00be_\u0000\u03a5\u03c5"+
		"\u0003\u00c4b\u0000\u03a6\u03c5\u0003\u00ccf\u0000\u03a7\u03c5\u0003\u00d4"+
		"j\u0000\u03a8\u03c5\u0003\u00ecv\u0000\u03a9\u03c5\u0003\u00e2q\u0000"+
		"\u03aa\u03c5\u0003j5\u0000\u03ab\u03c5\u0003\u00f0x\u0000\u03ac\u03c5"+
		"\u0003\u00fe\u007f\u0000\u03ad\u03c5\u0003\u00fc~\u0000\u03ae\u03c5\u0003"+
		"\u0102\u0081\u0000\u03af\u03c5\u0003\u010a\u0085\u0000\u03b0\u03c5\u0003"+
		"\u0114\u008a\u0000\u03b1\u03c5\u0003\u0110\u0088\u0000\u03b2\u03c5\u0003"+
		"\u0116\u008b\u0000\u03b3\u03c5\u0003\u0118\u008c\u0000\u03b4\u03c5\u0003"+
		"\u0112\u0089\u0000\u03b5\u03c5\u0003\u011c\u008e\u0000\u03b6\u03c5\u0003"+
		"\u0120\u0090\u0000\u03b7\u03c5\u0003\u012e\u0097\u0000\u03b8\u03c5\u0003"+
		"\u012c\u0096\u0000\u03b9\u03c5\u0003\u0130\u0098\u0000\u03ba\u03c5\u0003"+
		"\u0140\u00a0\u0000\u03bb\u03c5\u0003\u0146\u00a3\u0000\u03bc\u03c5\u0003"+
		"\u0148\u00a4\u0000\u03bd\u03c5\u0003\u014e\u00a7\u0000\u03be\u03c5\u0003"+
		"\u0154\u00aa\u0000\u03bf\u03c5\u0003\u0158\u00ac\u0000\u03c0\u03c5\u0003"+
		"\u0156\u00ab\u0000\u03c1\u03c5\u0003\u015c\u00ae\u0000\u03c2\u03c5\u0003"+
		"\u0162\u00b1\u0000\u03c3\u03c5\u0003\u0166\u00b3\u0000\u03c4\u0393\u0001"+
		"\u0000\u0000\u0000\u03c4\u0394\u0001\u0000\u0000\u0000\u03c4\u0395\u0001"+
		"\u0000\u0000\u0000\u03c4\u0396\u0001\u0000\u0000\u0000\u03c4\u0397\u0001"+
		"\u0000\u0000\u0000\u03c4\u0398\u0001\u0000\u0000\u0000\u03c4\u0399\u0001"+
		"\u0000\u0000\u0000\u03c4\u039a\u0001\u0000\u0000\u0000\u03c4\u039b\u0001"+
		"\u0000\u0000\u0000\u03c4\u039c\u0001\u0000\u0000\u0000\u03c4\u039d\u0001"+
		"\u0000\u0000\u0000\u03c4\u039e\u0001\u0000\u0000\u0000\u03c4\u039f\u0001"+
		"\u0000\u0000\u0000\u03c4\u03a0\u0001\u0000\u0000\u0000\u03c4\u03a1\u0001"+
		"\u0000\u0000\u0000\u03c4\u03a2\u0001\u0000\u0000\u0000\u03c4\u03a3\u0001"+
		"\u0000\u0000\u0000\u03c4\u03a4\u0001\u0000\u0000\u0000\u03c4\u03a5\u0001"+
		"\u0000\u0000\u0000\u03c4\u03a6\u0001\u0000\u0000\u0000\u03c4\u03a7\u0001"+
		"\u0000\u0000\u0000\u03c4\u03a8\u0001\u0000\u0000\u0000\u03c4\u03a9\u0001"+
		"\u0000\u0000\u0000\u03c4\u03aa\u0001\u0000\u0000\u0000\u03c4\u03ab\u0001"+
		"\u0000\u0000\u0000\u03c4\u03ac\u0001\u0000\u0000\u0000\u03c4\u03ad\u0001"+
		"\u0000\u0000\u0000\u03c4\u03ae\u0001\u0000\u0000\u0000\u03c4\u03af\u0001"+
		"\u0000\u0000\u0000\u03c4\u03b0\u0001\u0000\u0000\u0000\u03c4\u03b1\u0001"+
		"\u0000\u0000\u0000\u03c4\u03b2\u0001\u0000\u0000\u0000\u03c4\u03b3\u0001"+
		"\u0000\u0000\u0000\u03c4\u03b4\u0001\u0000\u0000\u0000\u03c4\u03b5\u0001"+
		"\u0000\u0000\u0000\u03c4\u03b6\u0001\u0000\u0000\u0000\u03c4\u03b7\u0001"+
		"\u0000\u0000\u0000\u03c4\u03b8\u0001\u0000\u0000\u0000\u03c4\u03b9\u0001"+
		"\u0000\u0000\u0000\u03c4\u03ba\u0001\u0000\u0000\u0000\u03c4\u03bb\u0001"+
		"\u0000\u0000\u0000\u03c4\u03bc\u0001\u0000\u0000\u0000\u03c4\u03bd\u0001"+
		"\u0000\u0000\u0000\u03c4\u03be\u0001\u0000\u0000\u0000\u03c4\u03bf\u0001"+
		"\u0000\u0000\u0000\u03c4\u03c0\u0001\u0000\u0000\u0000\u03c4\u03c1\u0001"+
		"\u0000\u0000\u0000\u03c4\u03c2\u0001\u0000\u0000\u0000\u03c4\u03c3\u0001"+
		"\u0000\u0000\u0000\u03c5U\u0001\u0000\u0000\u0000\u03c6\u03cb\u0003x<"+
		"\u0000\u03c7\u03cb\u0003\u0140\u00a0\u0000\u03c8\u03cb\u0003\u0162\u00b1"+
		"\u0000\u03c9\u03cb\u0003j5\u0000\u03ca\u03c6\u0001\u0000\u0000\u0000\u03ca"+
		"\u03c7\u0001\u0000\u0000\u0000\u03ca\u03c8\u0001\u0000\u0000\u0000\u03ca"+
		"\u03c9\u0001\u0000\u0000\u0000\u03cbW\u0001\u0000\u0000\u0000\u03cc\u03e6"+
		"\u0003`0\u0000\u03cd\u03e6\u0003n7\u0000\u03ce\u03e6\u0003\u0166\u00b3"+
		"\u0000\u03cf\u03e6\u0003\u00f0x\u0000\u03d0\u03e6\u0003\u00fc~\u0000\u03d1"+
		"\u03e6\u0003\u0154\u00aa\u0000\u03d2\u03e6\u0003\u015c\u00ae\u0000\u03d3"+
		"\u03e6\u0003\u0114\u008a\u0000\u03d4\u03e6\u0003\u0110\u0088\u0000\u03d5"+
		"\u03e6\u0003\u0116\u008b\u0000\u03d6\u03e6\u0003\u0118\u008c\u0000\u03d7"+
		"\u03e6\u0003\u0112\u0089\u0000\u03d8\u03e6\u0003\u014e\u00a7\u0000\u03d9"+
		"\u03e6\u0003d2\u0000\u03da\u03e6\u0003\u0158\u00ac\u0000\u03db\u03e6\u0003"+
		"\u0156\u00ab\u0000\u03dc\u03e6\u0003\u0148\u00a4\u0000\u03dd\u03e6\u0003"+
		"\u00ecv\u0000\u03de\u03e6\u0003\u011c\u008e\u0000\u03df\u03e6\u0003\u012e"+
		"\u0097\u0000\u03e0\u03e6\u0003\u012c\u0096\u0000\u03e1\u03e6\u0003Z-\u0000"+
		"\u03e2\u03e6\u0003\u00bc^\u0000\u03e3\u03e6\u0003p8\u0000\u03e4\u03e6"+
		"\u0003\u0130\u0098\u0000\u03e5\u03cc\u0001\u0000\u0000\u0000\u03e5\u03cd"+
		"\u0001\u0000\u0000\u0000\u03e5\u03ce\u0001\u0000\u0000\u0000\u03e5\u03cf"+
		"\u0001\u0000\u0000\u0000\u03e5\u03d0\u0001\u0000\u0000\u0000\u03e5\u03d1"+
		"\u0001\u0000\u0000\u0000\u03e5\u03d2\u0001\u0000\u0000\u0000\u03e5\u03d3"+
		"\u0001\u0000\u0000\u0000\u03e5\u03d4\u0001\u0000\u0000\u0000\u03e5\u03d5"+
		"\u0001\u0000\u0000\u0000\u03e5\u03d6\u0001\u0000\u0000\u0000\u03e5\u03d7"+
		"\u0001\u0000\u0000\u0000\u03e5\u03d8\u0001\u0000\u0000\u0000\u03e5\u03d9"+
		"\u0001\u0000\u0000\u0000\u03e5\u03da\u0001\u0000\u0000\u0000\u03e5\u03db"+
		"\u0001\u0000\u0000\u0000\u03e5\u03dc\u0001\u0000\u0000\u0000\u03e5\u03dd"+
		"\u0001\u0000\u0000\u0000\u03e5\u03de\u0001\u0000\u0000\u0000\u03e5\u03df"+
		"\u0001\u0000\u0000\u0000\u03e5\u03e0\u0001\u0000\u0000\u0000\u03e5\u03e1"+
		"\u0001\u0000\u0000\u0000\u03e5\u03e2\u0001\u0000\u0000\u0000\u03e5\u03e3"+
		"\u0001\u0000\u0000\u0000\u03e5\u03e4\u0001\u0000\u0000\u0000\u03e6Y\u0001"+
		"\u0000\u0000\u0000\u03e7\u03eb\u0005/\u0000\u0000\u03e8\u03ea\u0003\u0170"+
		"\u00b8\u0000\u03e9\u03e8\u0001\u0000\u0000\u0000\u03ea\u03ed\u0001\u0000"+
		"\u0000\u0000\u03eb\u03e9\u0001\u0000\u0000\u0000\u03eb\u03ec\u0001\u0000"+
		"\u0000\u0000\u03ec\u03ee\u0001\u0000\u0000\u0000\u03ed\u03eb\u0001\u0000"+
		"\u0000\u0000\u03ee\u03ef\u0003\u021a\u010d\u0000\u03ef[\u0001\u0000\u0000"+
		"\u0000\u03f0\u03f1\u00051\u0000\u0000\u03f1\u03f2\u0003\u01f0\u00f8\u0000"+
		"\u03f2]\u0001\u0000\u0000\u0000\u03f3\u03f7\u0005=\u0000\u0000\u03f4\u03f6"+
		"\u0003\u0170\u00b8\u0000\u03f5\u03f4\u0001\u0000\u0000\u0000\u03f6\u03f9"+
		"\u0001\u0000\u0000\u0000\u03f7\u03f5\u0001\u0000\u0000\u0000\u03f7\u03f8"+
		"\u0001\u0000\u0000\u0000\u03f8_\u0001\u0000\u0000\u0000\u03f9\u03f7\u0001"+
		"\u0000\u0000\u0000\u03fa\u03fe\u0005B\u0000\u0000\u03fb\u03fd\u0003\u0170"+
		"\u00b8\u0000\u03fc\u03fb\u0001\u0000\u0000\u0000\u03fd\u0400\u0001\u0000"+
		"\u0000\u0000\u03fe\u03fc\u0001\u0000\u0000\u0000\u03fe\u03ff\u0001\u0000"+
		"\u0000\u0000\u03ffa\u0001\u0000\u0000\u0000\u0400\u03fe\u0001\u0000\u0000"+
		"\u0000\u0401\u0402\u0005/\u0000\u0000\u0402\u0403\u0003\u0210\u0108\u0000"+
		"\u0403c\u0001\u0000\u0000\u0000\u0404\u0408\u0005M\u0000\u0000\u0405\u0407"+
		"\u0003\u0170\u00b8\u0000\u0406\u0405\u0001\u0000\u0000\u0000\u0407\u040a"+
		"\u0001\u0000\u0000\u0000\u0408\u0406\u0001\u0000\u0000\u0000\u0408\u0409"+
		"\u0001\u0000\u0000\u0000\u0409\u040d\u0001\u0000\u0000\u0000\u040a\u0408"+
		"\u0001\u0000\u0000\u0000\u040b\u040e\u0003f3\u0000\u040c\u040e\u0003h"+
		"4\u0000\u040d\u040b\u0001\u0000\u0000\u0000\u040d\u040c\u0001\u0000\u0000"+
		"\u0000\u040ee\u0001\u0000\u0000\u0000\u040f\u0410\u0005\u0001\u0000\u0000"+
		"\u0410g\u0001\u0000\u0000\u0000\u0411\u0416\u0003\u017c\u00be\u0000\u0412"+
		"\u0413\u0005\t\u0000\u0000\u0413\u0415\u0003\u017c\u00be\u0000\u0414\u0412"+
		"\u0001\u0000\u0000\u0000\u0415\u0418\u0001\u0000\u0000\u0000\u0416\u0414"+
		"\u0001\u0000\u0000\u0000\u0416\u0417\u0001\u0000\u0000\u0000\u0417i\u0001"+
		"\u0000\u0000\u0000\u0418\u0416\u0001\u0000\u0000\u0000\u0419\u041d\u0005"+
		"R\u0000\u0000\u041a\u041c\u0003\u0170\u00b8\u0000\u041b\u041a\u0001\u0000"+
		"\u0000\u0000\u041c\u041f\u0001\u0000\u0000\u0000\u041d\u041b\u0001\u0000"+
		"\u0000\u0000\u041d\u041e\u0001\u0000\u0000\u0000\u041e\u0420\u0001\u0000"+
		"\u0000\u0000\u041f\u041d\u0001\u0000\u0000\u0000\u0420\u0422\u0003\u01be"+
		"\u00df\u0000\u0421\u0423\u0003l6\u0000\u0422\u0421\u0001\u0000\u0000\u0000"+
		"\u0422\u0423\u0001\u0000\u0000\u0000\u0423k\u0001\u0000\u0000\u0000\u0424"+
		"\u0425\u0005\n\u0000\u0000\u0425\u0426\u0003\u01f0\u00f8\u0000\u0426m"+
		"\u0001\u0000\u0000\u0000\u0427\u0428\u0005V\u0000\u0000\u0428\u042d\u0003"+
		"\u0174\u00ba\u0000\u0429\u042a\u0005\t\u0000\u0000\u042a\u042c\u0003\u0174"+
		"\u00ba\u0000\u042b\u0429\u0001\u0000\u0000\u0000\u042c\u042f\u0001\u0000"+
		"\u0000\u0000\u042d\u042b\u0001\u0000\u0000\u0000\u042d\u042e\u0001\u0000"+
		"\u0000\u0000\u042eo\u0001\u0000\u0000\u0000\u042f\u042d\u0001\u0000\u0000"+
		"\u0000\u0430\u0431\u0005T\u0000\u0000\u0431q\u0001\u0000\u0000\u0000\u0432"+
		"\u0433\u0005Y\u0000\u0000\u0433\u0434\u00059\u0000\u0000\u0434\u0439\u0003"+
		"\u01d2\u00e9\u0000\u0435\u0436\u0005\t\u0000\u0000\u0436\u0438\u0003\u01d2"+
		"\u00e9\u0000\u0437\u0435\u0001\u0000\u0000\u0000\u0438\u043b\u0001\u0000"+
		"\u0000\u0000\u0439\u0437\u0001\u0000\u0000\u0000\u0439\u043a\u0001\u0000"+
		"\u0000\u0000\u043a\u043e\u0001\u0000\u0000\u0000\u043b\u0439\u0001\u0000"+
		"\u0000\u0000\u043c\u043f\u0003t:\u0000\u043d\u043f\u0003v;\u0000\u043e"+
		"\u043c\u0001\u0000\u0000\u0000\u043e\u043d\u0001\u0000\u0000\u0000\u043e"+
		"\u043f\u0001\u0000\u0000\u0000\u043fs\u0001\u0000\u0000\u0000\u0440\u0441"+
		"\u0005\u0104\u0000\u0000\u0441\u0442\u0003X,\u0000\u0442u\u0001\u0000"+
		"\u0000\u0000\u0443\u0444\u0005\u0104\u0000\u0000\u0444\u0445\u0005\u001f"+
		"\u0000\u0000\u0445\u0446\u0003\u009aM\u0000\u0446\u0447\u0005\b\u0000"+
		"\u0000\u0447w\u0001\u0000\u0000\u0000\u0448\u044a\u0005[\u0000\u0000\u0449"+
		"\u044b\u0003\u01cc\u00e6\u0000\u044a\u0449\u0001\u0000\u0000\u0000\u044a"+
		"\u044b\u0001\u0000\u0000\u0000\u044b\u044d\u0001\u0000\u0000\u0000\u044c"+
		"\u044e\u0003z=\u0000\u044d\u044c\u0001\u0000\u0000\u0000\u044d\u044e\u0001"+
		"\u0000\u0000\u0000\u044e\u044f\u0001\u0000\u0000\u0000\u044f\u0452\u0003"+
		"\u017c\u00be\u0000\u0450\u0453\u0003~?\u0000\u0451\u0453\u0003\u0088D"+
		"\u0000\u0452\u0450\u0001\u0000\u0000\u0000\u0452\u0451\u0001\u0000\u0000"+
		"\u0000\u0452\u0453\u0001\u0000\u0000\u0000\u0453\u0455\u0001\u0000\u0000"+
		"\u0000\u0454\u0456\u0003\u008aE\u0000\u0455\u0454\u0001\u0000\u0000\u0000"+
		"\u0455\u0456\u0001\u0000\u0000\u0000\u0456y\u0001\u0000\u0000\u0000\u0457"+
		"\u0459\u0003\u0170\u00b8\u0000\u0458\u0457\u0001\u0000\u0000\u0000\u0459"+
		"\u045c\u0001\u0000\u0000\u0000\u045a\u0458\u0001\u0000\u0000\u0000\u045a"+
		"\u045b\u0001\u0000\u0000\u0000\u045b\u045e\u0001\u0000\u0000\u0000\u045c"+
		"\u045a\u0001\u0000\u0000\u0000\u045d\u045f\u0003|>\u0000\u045e\u045d\u0001"+
		"\u0000\u0000\u0000\u045e\u045f\u0001\u0000\u0000\u0000\u045f\u0460\u0001"+
		"\u0000\u0000\u0000\u0460\u0461\u0005\u0103\u0000\u0000\u0461{\u0001\u0000"+
		"\u0000\u0000\u0462\u0463\u0005\u0082\u0000\u0000\u0463\u0464\u0005\u001f"+
		"\u0000\u0000\u0464\u0469\u0003\u0090H\u0000\u0465\u0466\u0005\t\u0000"+
		"\u0000\u0466\u0468\u0003\u0090H\u0000\u0467\u0465\u0001\u0000\u0000\u0000"+
		"\u0468\u046b\u0001\u0000\u0000\u0000\u0469\u0467\u0001\u0000\u0000\u0000"+
		"\u0469\u046a\u0001\u0000\u0000\u0000\u046a\u046c\u0001\u0000\u0000\u0000"+
		"\u046b\u0469\u0001\u0000\u0000\u0000\u046c\u046d\u0005\b\u0000\u0000\u046d"+
		"}\u0001\u0000\u0000\u0000\u046e\u046f\u0005\u00ce\u0000\u0000\u046f\u0474"+
		"\u0003\u0080@\u0000\u0470\u0471\u0005\t\u0000\u0000\u0471\u0473\u0003"+
		"\u0080@\u0000\u0472\u0470\u0001\u0000\u0000\u0000\u0473\u0476\u0001\u0000"+
		"\u0000\u0000\u0474\u0472\u0001\u0000\u0000\u0000\u0474\u0475\u0001\u0000"+
		"\u0000\u0000\u0475\u007f\u0001\u0000\u0000\u0000\u0476\u0474\u0001\u0000"+
		"\u0000\u0000\u0477\u047a\u0003\u0082A\u0000\u0478\u047a\u0003\u0086C\u0000"+
		"\u0479\u0477\u0001\u0000\u0000\u0000\u0479\u0478\u0001\u0000\u0000\u0000"+
		"\u047a\u0081\u0001\u0000\u0000\u0000\u047b\u047d\u0003\u0206\u0103\u0000"+
		"\u047c\u047e\u0003\u0084B\u0000\u047d\u047c\u0001\u0000\u0000\u0000\u047d"+
		"\u047e\u0001\u0000\u0000\u0000\u047e\u0083\u0001\u0000\u0000\u0000\u047f"+
		"\u0480\u0005\n\u0000\u0000\u0480\u0481\u0003\u0204\u0102\u0000\u0481\u0085"+
		"\u0001\u0000\u0000\u0000\u0482\u0483\u0005\u00c0\u0000\u0000\u0483\u0484"+
		"\u0005\u001f\u0000\u0000\u0484\u0485\u0005\u0001\u0000\u0000\u0485\u0486"+
		"\u0005\b\u0000\u0000\u0486\u0087\u0001\u0000\u0000\u0000\u0487\u0488\u0005"+
		"\u00d4\u0000\u0000\u0488\u0089\u0001\u0000\u0000\u0000\u0489\u048c\u0005"+
		"\u00d0\u0000\u0000\u048a\u048d\u0003\u008cF\u0000\u048b\u048d\u0003\u008e"+
		"G\u0000\u048c\u048a\u0001\u0000\u0000\u0000\u048c\u048b\u0001\u0000\u0000"+
		"\u0000\u048d\u008b\u0001\u0000\u0000\u0000\u048e\u048f\u0005\u0001\u0000"+
		"\u0000\u048f\u008d\u0001\u0000\u0000\u0000\u0490\u0495\u0003\u0082A\u0000"+
		"\u0491\u0492\u0005\t\u0000\u0000\u0492\u0494\u0003\u0082A\u0000\u0493"+
		"\u0491\u0001\u0000\u0000\u0000\u0494\u0497\u0001\u0000\u0000\u0000\u0495"+
		"\u0493\u0001\u0000\u0000\u0000\u0495\u0496\u0001\u0000\u0000\u0000\u0496"+
		"\u008f\u0001\u0000\u0000\u0000\u0497\u0495\u0001\u0000\u0000\u0000\u0498"+
		"\u049b\u0003\u0092I\u0000\u0499\u049b\u0003\u01e6\u00f3\u0000\u049a\u0498"+
		"\u0001\u0000\u0000\u0000\u049a\u0499\u0001\u0000\u0000\u0000\u049b\u0091"+
		"\u0001\u0000\u0000\u0000\u049c\u04a1\u0003\u01e0\u00f0\u0000\u049d\u049e"+
		"\u0005\u0003\u0000\u0000\u049e\u04a0\u0003Z-\u0000\u049f\u049d\u0001\u0000"+
		"\u0000\u0000\u04a0\u04a3\u0001\u0000\u0000\u0000\u04a1\u049f\u0001\u0000"+
		"\u0000\u0000\u04a1\u04a2\u0001\u0000\u0000\u0000\u04a2\u0093\u0001\u0000"+
		"\u0000\u0000\u04a3\u04a1\u0001\u0000\u0000\u0000\u04a4\u04a6\u0005^\u0000"+
		"\u0000\u04a5\u04a7\u0003\u0096K\u0000\u04a6\u04a5\u0001\u0000\u0000\u0000"+
		"\u04a7\u04a8\u0001\u0000\u0000\u0000\u04a8\u04a6\u0001\u0000\u0000\u0000"+
		"\u04a8\u04a9\u0001\u0000\u0000\u0000\u04a9\u0095\u0001\u0000\u0000\u0000"+
		"\u04aa\u04ac\u0003\u0098L\u0000\u04ab\u04aa\u0001\u0000\u0000\u0000\u04ab"+
		"\u04ac\u0001\u0000\u0000\u0000\u04ac\u04ad\u0001\u0000\u0000\u0000\u04ad"+
		"\u04ae\u0005\u001f\u0000\u0000\u04ae\u04af\u0003\u009aM\u0000\u04af\u04b0"+
		"\u0005\b\u0000\u0000\u04b0\u0097\u0001\u0000\u0000\u0000\u04b1\u04b2\u0003"+
		"\u021a\u010d\u0000\u04b2\u04b3\u0005\u0011\u0000\u0000\u04b3\u0099\u0001"+
		"\u0000\u0000\u0000\u04b4\u04b8\u0003X,\u0000\u04b5\u04b7\u0003\u009cN"+
		"\u0000\u04b6\u04b5\u0001\u0000\u0000\u0000\u04b7\u04ba\u0001\u0000\u0000"+
		"\u0000\u04b8\u04b6\u0001\u0000\u0000\u0000\u04b8\u04b9\u0001\u0000\u0000"+
		"\u0000\u04b9\u009b\u0001\u0000\u0000\u0000\u04ba\u04b8\u0001\u0000\u0000"+
		"\u0000\u04bb\u04bc\u0005\u0003\u0000\u0000\u04bc\u04bd\u0003X,\u0000\u04bd"+
		"\u009d\u0001\u0000\u0000\u0000\u04be\u04bf\u0005`\u0000\u0000\u04bf\u009f"+
		"\u0001\u0000\u0000\u0000\u04c0\u04c4\u0005c\u0000\u0000\u04c1\u04c3\u0003"+
		"\u0170\u00b8\u0000\u04c2\u04c1\u0001\u0000\u0000\u0000\u04c3\u04c6\u0001"+
		"\u0000\u0000\u0000\u04c4\u04c2\u0001\u0000\u0000\u0000\u04c4\u04c5\u0001"+
		"\u0000\u0000\u0000\u04c5\u00a1\u0001\u0000\u0000\u0000\u04c6\u04c4\u0001"+
		"\u0000\u0000\u0000\u04c7\u04cb\u0005d\u0000\u0000\u04c8\u04ca\u0003\u0170"+
		"\u00b8\u0000\u04c9\u04c8\u0001\u0000\u0000\u0000\u04ca\u04cd\u0001\u0000"+
		"\u0000\u0000\u04cb\u04c9\u0001\u0000\u0000\u0000\u04cb\u04cc\u0001\u0000"+
		"\u0000\u0000\u04cc\u04ce\u0001\u0000\u0000\u0000\u04cd\u04cb\u0001\u0000"+
		"\u0000\u0000\u04ce\u04cf\u0003\u00a4R\u0000\u04cf\u04d0\u0005\t\u0000"+
		"\u0000\u04d0\u04d1\u0003\u00a4R\u0000\u04d1\u04d3\u0001\u0000\u0000\u0000"+
		"\u04d2\u04d4\u0003\u00aeW\u0000\u04d3\u04d2\u0001\u0000\u0000\u0000\u04d3"+
		"\u04d4\u0001\u0000\u0000\u0000\u04d4\u04d6\u0001\u0000\u0000\u0000\u04d5"+
		"\u04d7\u0003\u00b0X\u0000\u04d6\u04d5\u0001\u0000\u0000\u0000\u04d6\u04d7"+
		"\u0001\u0000\u0000\u0000\u04d7\u00a3\u0001\u0000\u0000\u0000\u04d8\u04dc"+
		"\u0003\u00a6S\u0000\u04d9\u04dc\u0003\u00a8T\u0000\u04da\u04dc\u0003\u00aa"+
		"U\u0000\u04db\u04d8\u0001\u0000\u0000\u0000\u04db\u04d9\u0001\u0000\u0000"+
		"\u0000\u04db\u04da\u0001\u0000\u0000\u0000\u04dc\u00a5\u0001\u0000\u0000"+
		"\u0000\u04dd\u04de\u0005\u001f\u0000\u0000\u04de\u04df\u0003\u021a\u010d"+
		"\u0000\u04df\u04e0\u0005\b\u0000\u0000\u04e0\u00a7\u0001\u0000\u0000\u0000"+
		"\u04e1\u04e2\u0007\u0000\u0000\u0000\u04e2\u00a9\u0001\u0000\u0000\u0000"+
		"\u04e3\u04e4\u0007\u0001\u0000\u0000\u04e4\u04e6\u0003\u021a\u010d\u0000"+
		"\u04e5\u04e7\u0003\u00acV\u0000\u04e6\u04e5\u0001\u0000\u0000\u0000\u04e6"+
		"\u04e7\u0001\u0000\u0000\u0000\u04e7\u04e8\u0001\u0000\u0000\u0000\u04e8"+
		"\u04e9\u0007\u0002\u0000\u0000\u04e9\u00ab\u0001\u0000\u0000\u0000\u04ea"+
		"\u04eb\u0005\u0001\u0000\u0000\u04eb\u04ec\u0003\u01a4\u00d2\u0000\u04ec"+
		"\u04ed\u0005\u0010\u0000\u0000\u04ed\u04ee\u0003\u01a4\u00d2\u0000\u04ee"+
		"\u00ad\u0001\u0000\u0000\u0000\u04ef\u04f0\u0005\u0103\u0000\u0000\u04f0"+
		"\u04f1\u0003J%\u0000\u04f1\u00af\u0001\u0000\u0000\u0000\u04f2\u04f3\u0005"+
		"\u00ce\u0000\u0000\u04f3\u04f8\u0003\u0174\u00ba\u0000\u04f4\u04f5\u0005"+
		"\t\u0000\u0000\u04f5\u04f7\u0003\u0174\u00ba\u0000\u04f6\u04f4\u0001\u0000"+
		"\u0000\u0000\u04f7\u04fa\u0001\u0000\u0000\u0000\u04f8\u04f6\u0001\u0000"+
		"\u0000\u0000\u04f8\u04f9\u0001\u0000\u0000\u0000\u04f9\u00b1\u0001\u0000"+
		"\u0000\u0000\u04fa\u04f8\u0001\u0000\u0000\u0000\u04fb\u04fc\u0005e\u0000"+
		"\u0000\u04fc\u04fe\u0003\u01a4\u00d2\u0000\u04fd\u04ff\u0003\u00c0`\u0000"+
		"\u04fe\u04fd\u0001\u0000\u0000\u0000\u04fe\u04ff\u0001\u0000\u0000\u0000"+
		"\u04ff\u00b3\u0001\u0000\u0000\u0000\u0500\u0501\u0005g\u0000\u0000\u0501"+
		"\u0502\u0003\u00b6[\u0000\u0502\u0503\u0005\t\u0000\u0000\u0503\u0504"+
		"\u0003\u00b6[\u0000\u0504\u00b5\u0001\u0000\u0000\u0000\u0505\u0507\u0007"+
		"\u0003\u0000\u0000\u0506\u0508\u0003\u00b8\\\u0000\u0507\u0506\u0001\u0000"+
		"\u0000\u0000\u0507\u0508\u0001\u0000\u0000\u0000\u0508\u050c\u0001\u0000"+
		"\u0000\u0000\u0509\u050b\u0003\u0170\u00b8\u0000\u050a\u0509\u0001\u0000"+
		"\u0000\u0000\u050b\u050e\u0001\u0000\u0000\u0000\u050c\u050a\u0001\u0000"+
		"\u0000\u0000\u050c\u050d\u0001\u0000\u0000\u0000\u050d\u00b7\u0001\u0000"+
		"\u0000\u0000\u050e\u050c\u0001\u0000\u0000\u0000\u050f\u0510\u0005/\u0000"+
		"\u0000\u0510\u0511\u0003\u021a\u010d\u0000\u0511\u00b9\u0001\u0000\u0000"+
		"\u0000\u0512\u0516\u0005f\u0000\u0000\u0513\u0515\u0003\u0170\u00b8\u0000"+
		"\u0514\u0513\u0001\u0000\u0000\u0000\u0515\u0518\u0001\u0000\u0000\u0000"+
		"\u0516\u0514\u0001\u0000\u0000\u0000\u0516\u0517\u0001\u0000\u0000\u0000"+
		"\u0517\u0519\u0001\u0000\u0000\u0000\u0518\u0516\u0001\u0000\u0000\u0000"+
		"\u0519\u051a\u0003\u00a4R\u0000\u051a\u051b\u0005\t\u0000\u0000\u051b"+
		"\u051c\u0003\u00a4R\u0000\u051c\u051e\u0001\u0000\u0000\u0000\u051d\u051f"+
		"\u0003\u00aeW\u0000\u051e\u051d\u0001\u0000\u0000\u0000\u051e\u051f\u0001"+
		"\u0000\u0000\u0000\u051f\u0521\u0001\u0000\u0000\u0000\u0520\u0522\u0003"+
		"\u00b0X\u0000\u0521\u0520\u0001\u0000\u0000\u0000\u0521\u0522\u0001\u0000"+
		"\u0000\u0000\u0522\u00bb\u0001\u0000\u0000\u0000\u0523\u0524\u0005\u0085"+
		"\u0000\u0000\u0524\u0525\u0003\u01ba\u00dd\u0000\u0525\u00bd\u0001\u0000"+
		"\u0000\u0000\u0526\u052a\u0005\u0088\u0000\u0000\u0527\u0529\u0003\u0170"+
		"\u00b8\u0000\u0528\u0527\u0001\u0000\u0000\u0000\u0529\u052c\u0001\u0000"+
		"\u0000\u0000\u052a\u0528\u0001\u0000\u0000\u0000\u052a\u052b\u0001\u0000"+
		"\u0000\u0000\u052b\u052d\u0001\u0000\u0000\u0000\u052c\u052a\u0001\u0000"+
		"\u0000\u0000\u052d\u0530\u0003\u017c\u00be\u0000\u052e\u0531\u0003\u00c0"+
		"`\u0000\u052f\u0531\u0003\u00c2a\u0000\u0530\u052e\u0001\u0000\u0000\u0000"+
		"\u0530\u052f\u0001\u0000\u0000\u0000\u0530\u0531\u0001\u0000\u0000\u0000"+
		"\u0531\u00bf\u0001\u0000\u0000\u0000\u0532\u053b\u0005\u00ba\u0000\u0000"+
		"\u0533\u0538\u0003\u017c\u00be\u0000\u0534\u0535\u0005\t\u0000\u0000\u0535"+
		"\u0537\u0003\u017c\u00be\u0000\u0536\u0534\u0001\u0000\u0000\u0000\u0537"+
		"\u053a\u0001\u0000\u0000\u0000\u0538\u0536\u0001\u0000\u0000\u0000\u0538"+
		"\u0539\u0001\u0000\u0000\u0000\u0539\u053c\u0001\u0000\u0000\u0000\u053a"+
		"\u0538\u0001\u0000\u0000\u0000\u053b\u0533\u0001\u0000\u0000\u0000\u053b"+
		"\u053c\u0001\u0000\u0000\u0000\u053c\u00c1\u0001\u0000\u0000\u0000\u053d"+
		"\u053e\u0005\u0103\u0000\u0000\u053e\u053f\u0003\u017c\u00be\u0000\u053f"+
		"\u00c3\u0001\u0000\u0000\u0000\u0540\u0544\u0005\u0094\u0000\u0000\u0541"+
		"\u0543\u0003\u0170\u00b8\u0000\u0542\u0541\u0001\u0000\u0000\u0000\u0543"+
		"\u0546\u0001\u0000\u0000\u0000\u0544\u0542\u0001\u0000\u0000\u0000\u0544"+
		"\u0545\u0001\u0000\u0000\u0000\u0545\u0547\u0001\u0000\u0000\u0000\u0546"+
		"\u0544\u0001\u0000\u0000\u0000\u0547\u0548\u0003\u017c\u00be\u0000\u0548"+
		"\u0549\u0003\u00c0`\u0000\u0549\u00c5\u0001\u0000\u0000\u0000\u054a\u054e"+
		"\u0005\u0096\u0000\u0000\u054b\u054d\u0003\u0170\u00b8\u0000\u054c\u054b"+
		"\u0001\u0000\u0000\u0000\u054d\u0550\u0001\u0000\u0000\u0000\u054e\u054c"+
		"\u0001\u0000\u0000\u0000\u054e\u054f\u0001\u0000\u0000\u0000\u054f\u0551"+
		"\u0001\u0000\u0000\u0000\u0550\u054e\u0001\u0000\u0000\u0000\u0551\u0552"+
		"\u0003\u00c8d\u0000\u0552\u0553\u0005/\u0000\u0000\u0553\u0554\u0003\u021a"+
		"\u010d\u0000\u0554\u0555\u0005\u001f\u0000\u0000\u0555\u055a\u0003\u0004"+
		"\u0002\u0000\u0556\u0557\u0005\"\u0000\u0000\u0557\u0559\u0003\u0004\u0002"+
		"\u0000\u0558\u0556\u0001\u0000\u0000\u0000\u0559\u055c\u0001\u0000\u0000"+
		"\u0000\u055a\u0558\u0001\u0000\u0000\u0000\u055a\u055b\u0001\u0000\u0000"+
		"\u0000\u055b\u055e\u0001\u0000\u0000\u0000\u055c\u055a\u0001\u0000\u0000"+
		"\u0000\u055d\u055f\u0005\"\u0000\u0000\u055e\u055d\u0001\u0000\u0000\u0000"+
		"\u055e\u055f\u0001\u0000\u0000\u0000\u055f\u0560\u0001\u0000\u0000\u0000"+
		"\u0560\u0561\u0005\b\u0000\u0000\u0561\u00c7\u0001\u0000\u0000\u0000\u0562"+
		"\u0566\u0003\u00cae\u0000\u0563\u0566\u0003\u0208\u0104\u0000\u0564\u0566"+
		"\u0003\u01d2\u00e9\u0000\u0565\u0562\u0001\u0000\u0000\u0000\u0565\u0563"+
		"\u0001\u0000\u0000\u0000\u0565\u0564\u0001\u0000\u0000\u0000\u0566\u00c9"+
		"\u0001\u0000\u0000\u0000\u0567\u0568\u0005Q\u0000\u0000\u0568\u0569\u0005"+
		"\u001e\u0000\u0000\u0569\u056e\u0003\u017c\u00be\u0000\u056a\u056b\u0005"+
		"\t\u0000\u0000\u056b\u056d\u0003\u017c\u00be\u0000\u056c\u056a\u0001\u0000"+
		"\u0000\u0000\u056d\u0570\u0001\u0000\u0000\u0000\u056e\u056c\u0001\u0000"+
		"\u0000\u0000\u056e\u056f\u0001\u0000\u0000\u0000\u056f\u0571\u0001\u0000"+
		"\u0000\u0000\u0570\u056e\u0001\u0000\u0000\u0000\u0571\u0572\u0005\u0005"+
		"\u0000\u0000\u0572\u00cb\u0001\u0000\u0000\u0000\u0573\u0577\u0005\u0097"+
		"\u0000\u0000\u0574\u0576\u0003\u0170\u00b8\u0000\u0575\u0574\u0001\u0000"+
		"\u0000\u0000\u0576\u0579\u0001\u0000\u0000\u0000\u0577\u0575\u0001\u0000"+
		"\u0000\u0000\u0577\u0578\u0001\u0000\u0000\u0000\u0578\u057a\u0001\u0000"+
		"\u0000\u0000\u0579\u0577\u0001\u0000\u0000\u0000\u057a\u057b\u0003\u0208"+
		"\u0104\u0000\u057b\u057c\u0007\u0004\u0000\u0000\u057c\u057f\u0003\u0208"+
		"\u0104\u0000\u057d\u0580\u0003\u00ceg\u0000\u057e\u0580\u0003\u00d0h\u0000"+
		"\u057f\u057d\u0001\u0000\u0000\u0000\u057f\u057e\u0001\u0000\u0000\u0000"+
		"\u057f\u0580\u0001\u0000\u0000\u0000\u0580\u0582\u0001\u0000\u0000\u0000"+
		"\u0581\u0583\u0003\u00d2i\u0000\u0582\u0581\u0001\u0000\u0000\u0000\u0582"+
		"\u0583\u0001\u0000\u0000\u0000\u0583\u00cd\u0001\u0000\u0000\u0000\u0584"+
		"\u0585\u0005\u0109\u0000\u0000\u0585\u0586\u0005\u0011\u0000\u0000\u0586"+
		"\u0587\u0003\u021a\u010d\u0000\u0587\u00cf\u0001\u0000\u0000\u0000\u0588"+
		"\u0589\u0005\u0104\u0000\u0000\u0589\u058a\u0003\u01a4\u00d2\u0000\u058a"+
		"\u058b\u0005\u00ba\u0000\u0000\u058b\u058c\u0003\u0208\u0104\u0000\u058c"+
		"\u00d1\u0001\u0000\u0000\u0000\u058d\u058e\u0005\u00c7\u0000\u0000\u058e"+
		"\u058f\u0003\u01d4\u00ea\u0000\u058f\u0590\u0005\u001f\u0000\u0000\u0590"+
		"\u0591\u0003\u0168\u00b4\u0000\u0591\u0592\u0005\b\u0000\u0000\u0592\u00d3"+
		"\u0001\u0000\u0000\u0000\u0593\u0597\u0005\u0098\u0000\u0000\u0594\u0596"+
		"\u0003\u0170\u00b8\u0000\u0595\u0594\u0001\u0000\u0000\u0000\u0596\u0599"+
		"\u0001\u0000\u0000\u0000\u0597\u0595\u0001\u0000\u0000\u0000\u0597\u0598"+
		"\u0001\u0000\u0000\u0000\u0598\u059a\u0001\u0000\u0000\u0000\u0599\u0597"+
		"\u0001\u0000\u0000\u0000\u059a\u059f\u0003\u00d8l\u0000\u059b\u059c\u0005"+
		"\t\u0000\u0000\u059c\u059e\u0003\u00d8l\u0000\u059d\u059b\u0001\u0000"+
		"\u0000\u0000\u059e\u05a1\u0001\u0000\u0000\u0000\u059f\u059d\u0001\u0000"+
		"\u0000\u0000\u059f\u05a0\u0001\u0000\u0000\u0000\u05a0\u05a2\u0001\u0000"+
		"\u0000\u0000\u05a1\u059f\u0001\u0000\u0000\u0000\u05a2\u05a5\u0003\u00d6"+
		"k\u0000\u05a3\u05a6\u0003\u00dcn\u0000\u05a4\u05a6\u0003\u00deo\u0000"+
		"\u05a5\u05a3\u0001\u0000\u0000\u0000\u05a5\u05a4\u0001\u0000\u0000\u0000"+
		"\u05a6\u05a8\u0001\u0000\u0000\u0000\u05a7\u05a9\u0003\u00e0p\u0000\u05a8"+
		"\u05a7\u0001\u0000\u0000\u0000\u05a8\u05a9\u0001\u0000\u0000\u0000\u05a9"+
		"\u00d5\u0001\u0000\u0000\u0000\u05aa\u05ab\u0005\u00ba\u0000\u0000\u05ab"+
		"\u05ac\u0003\u0174\u00ba\u0000\u05ac\u00d7\u0001\u0000\u0000\u0000\u05ad"+
		"\u05af\u0003\u0174\u00ba\u0000\u05ae\u05b0\u0003\u00dam\u0000\u05af\u05ae"+
		"\u0001\u0000\u0000\u0000\u05af\u05b0\u0001\u0000\u0000\u0000\u05b0\u00d9"+
		"\u0001\u0000\u0000\u0000\u05b1\u05b2\u0005J\u0000\u0000\u05b2\u05b3\u0005"+
		"\u0011\u0000\u0000\u05b3\u05b4\u0003\u0174\u00ba\u0000\u05b4\u00db\u0001"+
		"\u0000\u0000\u0000\u05b5\u05b6\u0005\u0082\u0000\u0000\u05b6\u05b7\u0005"+
		"\u00d6\u0000\u0000\u05b7\u05b8\u0005\u001f\u0000\u0000\u05b8\u05b9\u0003"+
		"\u0174\u00ba\u0000\u05b9\u05ba\u0005\t\u0000\u0000\u05ba\u05bb\u0003\u0174"+
		"\u00ba\u0000\u05bb\u05bc\u0005\t\u0000\u0000\u05bc\u05bd\u0003\u0174\u00ba"+
		"\u0000\u05bd\u05be\u0005\b\u0000\u0000\u05be\u00dd\u0001\u0000\u0000\u0000"+
		"\u05bf\u05c0\u0005_\u0000\u0000\u05c0\u05c2\u0003\u0174\u00ba\u0000\u05c1"+
		"\u05bf\u0001\u0000\u0000\u0000\u05c1\u05c2\u0001\u0000\u0000\u0000\u05c2"+
		"\u05c5\u0001\u0000\u0000\u0000\u05c3\u05c4\u0005\u00f6\u0000\u0000\u05c4"+
		"\u05c6\u0003\u0174\u00ba\u0000\u05c5\u05c3\u0001\u0000\u0000\u0000\u05c5"+
		"\u05c6\u0001\u0000\u0000\u0000\u05c6\u05c7\u0001\u0000\u0000\u0000\u05c7"+
		"\u05c8\u0005\u00ed\u0000\u0000\u05c8\u05c9\u0003\u0174\u00ba\u0000\u05c9"+
		"\u00df\u0001\u0000\u0000\u0000\u05ca\u05cb\u00059\u0000\u0000\u05cb\u05d0"+
		"\u0003\u0174\u00ba\u0000\u05cc\u05cd\u0005\t\u0000\u0000\u05cd\u05cf\u0003"+
		"\u0174\u00ba\u0000\u05ce\u05cc\u0001\u0000\u0000\u0000\u05cf\u05d2\u0001"+
		"\u0000\u0000\u0000\u05d0\u05ce\u0001\u0000\u0000\u0000\u05d0\u05d1\u0001"+
		"\u0000\u0000\u0000\u05d1\u00e1\u0001\u0000\u0000\u0000\u05d2\u05d0\u0001"+
		"\u0000\u0000\u0000\u05d3\u05d7\u0007\u0005\u0000\u0000\u05d4\u05d6\u0003"+
		"\u016e\u00b7\u0000\u05d5\u05d4\u0001\u0000\u0000\u0000\u05d6\u05d9\u0001"+
		"\u0000\u0000\u0000\u05d7\u05d5\u0001\u0000\u0000\u0000\u05d7\u05d8\u0001"+
		"\u0000\u0000\u0000\u05d8\u05da\u0001\u0000\u0000\u0000\u05d9\u05d7\u0001"+
		"\u0000\u0000\u0000\u05da\u05df\u0003\u00e8t\u0000\u05db\u05dc\u0005\t"+
		"\u0000\u0000\u05dc\u05de\u0003\u00e8t\u0000\u05dd\u05db\u0001\u0000\u0000"+
		"\u0000\u05de\u05e1\u0001\u0000\u0000\u0000\u05df\u05dd\u0001\u0000\u0000"+
		"\u0000\u05df\u05e0\u0001\u0000\u0000\u0000\u05e0\u05e3\u0001\u0000\u0000"+
		"\u0000\u05e1\u05df\u0001\u0000\u0000\u0000\u05e2\u05e4\u0003\u00e4r\u0000"+
		"\u05e3\u05e2\u0001\u0000\u0000\u0000\u05e3\u05e4\u0001\u0000\u0000\u0000"+
		"\u05e4\u05e6\u0001\u0000\u0000\u0000\u05e5\u05e7\u0003\u00e6s\u0000\u05e6"+
		"\u05e5\u0001\u0000\u0000\u0000\u05e6\u05e7\u0001\u0000\u0000\u0000\u05e7"+
		"\u05e8\u0001\u0000\u0000\u0000\u05e8\u05e9\u0005\u00ba\u0000\u0000\u05e9"+
		"\u05ea\u0005\u001f\u0000\u0000\u05ea\u05eb\u0003\u0168\u00b4\u0000\u05eb"+
		"\u05ec\u0005\b\u0000\u0000\u05ec\u00e3\u0001\u0000\u0000\u0000\u05ed\u05ee"+
		"\u0005\u0090\u0000\u0000\u05ee\u05ef\u0005\u0131\u0000\u0000\u05ef\u00e5"+
		"\u0001\u0000\u0000\u0000\u05f0\u05f1\u0005\u0080\u0000\u0000\u05f1\u05f2"+
		"\u0005\u013b\u0000\u0000\u05f2\u00e7\u0001\u0000\u0000\u0000\u05f3\u05f5"+
		"\u0003\u0174\u00ba\u0000\u05f4\u05f6\u0003\u00eau\u0000\u05f5\u05f4\u0001"+
		"\u0000\u0000\u0000\u05f5\u05f6\u0001\u0000\u0000\u0000\u05f6\u00e9\u0001"+
		"\u0000\u0000\u0000\u05f7\u05f8\u0005\u00f6\u0000\u0000\u05f8\u05f9\u0005"+
		"\u0139\u0000\u0000\u05f9\u00eb\u0001\u0000\u0000\u0000\u05fa\u05fe\u0007"+
		"\u0006\u0000\u0000\u05fb\u05fd\u0003\u016e\u00b7\u0000\u05fc\u05fb\u0001"+
		"\u0000\u0000\u0000\u05fd\u0600\u0001\u0000\u0000\u0000\u05fe\u05fc\u0001"+
		"\u0000\u0000\u0000\u05fe\u05ff\u0001\u0000\u0000\u0000\u05ff\u0601\u0001"+
		"\u0000\u0000\u0000\u0600\u05fe\u0001\u0000\u0000\u0000\u0601\u0606\u0003"+
		"\u00eew\u0000\u0602\u0603\u0005\t\u0000\u0000\u0603\u0605\u0003\u00ee"+
		"w\u0000\u0604\u0602\u0001\u0000\u0000\u0000\u0605\u0608\u0001\u0000\u0000"+
		"\u0000\u0606\u0604\u0001\u0000\u0000\u0000\u0606\u0607\u0001\u0000\u0000"+
		"\u0000\u0607\u060a\u0001\u0000\u0000\u0000\u0608\u0606\u0001\u0000\u0000"+
		"\u0000\u0609\u060b\u0003\u00e4r\u0000\u060a\u0609\u0001\u0000\u0000\u0000"+
		"\u060a\u060b\u0001\u0000\u0000\u0000\u060b\u00ed\u0001\u0000\u0000\u0000"+
		"\u060c\u060e\u0003\u0174\u00ba\u0000\u060d\u060f\u0003\u00eau\u0000\u060e"+
		"\u060d\u0001\u0000\u0000\u0000\u060e\u060f\u0001\u0000\u0000\u0000\u060f"+
		"\u00ef\u0001\u0000\u0000\u0000\u0610\u0612\u0005\u00c2\u0000\u0000\u0611"+
		"\u0613\u0003\u00f2y\u0000\u0612\u0611\u0001\u0000\u0000\u0000\u0612\u0613"+
		"\u0001\u0000\u0000\u0000\u0613\u0614\u0001\u0000\u0000\u0000\u0614\u0615"+
		"\u0003\u017c\u00be\u0000\u0615\u0616\u0005\u0104\u0000\u0000\u0616\u0617"+
		"\u0003\u00f8|\u0000\u0617\u00f1\u0001\u0000\u0000\u0000\u0618\u0619\u0005"+
		"\u0089\u0000\u0000\u0619\u061a\u0005\u0011\u0000\u0000\u061a\u061c\u0007"+
		"\u0007\u0000\u0000\u061b\u061d\u0003\u00f4z\u0000\u061c\u061b\u0001\u0000"+
		"\u0000\u0000\u061c\u061d\u0001\u0000\u0000\u0000\u061d\u00f3\u0001\u0000"+
		"\u0000\u0000\u061e\u061f\u0005]\u0000\u0000\u061f\u0620\u0005\u0011\u0000"+
		"\u0000\u0620\u0621\u0005\u013c\u0000\u0000\u0621\u00f5\u0001\u0000\u0000"+
		"\u0000\u0622\u0625\u0003\u0208\u0104\u0000\u0623\u0624\u0005\n\u0000\u0000"+
		"\u0624\u0626\u0003\u0202\u0101\u0000\u0625\u0623\u0001\u0000\u0000\u0000"+
		"\u0625\u0626\u0001\u0000\u0000\u0000\u0626\u00f7\u0001\u0000\u0000\u0000"+
		"\u0627\u0629\u0003\u00f6{\u0000\u0628\u0627\u0001\u0000\u0000\u0000\u0628"+
		"\u0629\u0001\u0000\u0000\u0000\u0629\u062d\u0001\u0000\u0000\u0000\u062a"+
		"\u062c\u0003\u00fa}\u0000\u062b\u062a\u0001\u0000\u0000\u0000\u062c\u062f"+
		"\u0001\u0000\u0000\u0000\u062d\u062b\u0001\u0000\u0000\u0000\u062d\u062e"+
		"\u0001\u0000\u0000\u0000\u062e\u0631\u0001\u0000\u0000\u0000\u062f\u062d"+
		"\u0001\u0000\u0000\u0000\u0630\u0632\u0005\u0001\u0000\u0000\u0631\u0630"+
		"\u0001\u0000\u0000\u0000\u0631\u0632\u0001\u0000\u0000\u0000\u0632\u00f9"+
		"\u0001\u0000\u0000\u0000\u0633\u0635\u0005\u0001\u0000\u0000\u0634\u0633"+
		"\u0001\u0000\u0000\u0000\u0634\u0635\u0001\u0000\u0000\u0000\u0635\u0636"+
		"\u0001\u0000\u0000\u0000\u0636\u0638\u0003\u0246\u0123\u0000\u0637\u0639"+
		"\u0003\u00f6{\u0000\u0638\u0637\u0001\u0000\u0000\u0000\u0638\u0639\u0001"+
		"\u0000\u0000\u0000\u0639\u00fb\u0001\u0000\u0000\u0000\u063a\u063c\u0005"+
		"\u00c4\u0000\u0000\u063b\u063d\u0003\u00f2y\u0000\u063c\u063b\u0001\u0000"+
		"\u0000\u0000\u063c\u063d\u0001\u0000\u0000\u0000\u063d\u063e\u0001\u0000"+
		"\u0000\u0000\u063e\u063f\u0003\u017c\u00be\u0000\u063f\u0640\u0005\u0104"+
		"\u0000\u0000\u0640\u0641\u0003\u00f8|\u0000\u0641\u00fd\u0001\u0000\u0000"+
		"\u0000\u0642\u0643\u0005\u00c3\u0000\u0000\u0643\u0644\u0003\u017c\u00be"+
		"\u0000\u0644\u0646\u0003\u01f0\u00f8\u0000\u0645\u0647\u0003\u0100\u0080"+
		"\u0000\u0646\u0645\u0001\u0000\u0000\u0000\u0646\u0647\u0001\u0000\u0000"+
		"\u0000\u0647\u00ff\u0001\u0000\u0000\u0000\u0648\u0649\u0005\u0104\u0000"+
		"\u0000\u0649\u064a\u0005\u001f\u0000\u0000\u064a\u064f\u0003\u0172\u00b9"+
		"\u0000\u064b\u064c\u0005\t\u0000\u0000\u064c\u064e\u0003\u0172\u00b9\u0000"+
		"\u064d\u064b\u0001\u0000\u0000\u0000\u064e\u0651\u0001\u0000\u0000\u0000"+
		"\u064f\u064d\u0001\u0000\u0000\u0000\u064f\u0650\u0001\u0000\u0000\u0000"+
		"\u0650\u0652\u0001\u0000\u0000\u0000\u0651\u064f\u0001\u0000\u0000\u0000"+
		"\u0652\u0653\u0005\b\u0000\u0000\u0653\u0101\u0001\u0000\u0000\u0000\u0654"+
		"\u0658\u0005\u00c5\u0000\u0000\u0655\u0657\u0003\u0170\u00b8\u0000\u0656"+
		"\u0655\u0001\u0000\u0000\u0000\u0657\u065a\u0001\u0000\u0000\u0000\u0658"+
		"\u0656\u0001\u0000\u0000\u0000\u0658\u0659\u0001\u0000\u0000\u0000\u0659"+
		"\u065b\u0001\u0000\u0000\u0000\u065a\u0658\u0001\u0000\u0000\u0000\u065b"+
		"\u065c\u00059\u0000\u0000\u065c\u065e\u0003\u01d2\u00e9\u0000\u065d\u065f"+
		"\u0003\u0104\u0082\u0000\u065e\u065d\u0001\u0000\u0000\u0000\u065e\u065f"+
		"\u0001\u0000\u0000\u0000\u065f\u0662\u0001\u0000\u0000\u0000\u0660\u0663"+
		"\u0003\u0106\u0083\u0000\u0661\u0663\u0003\u0108\u0084\u0000\u0662\u0660"+
		"\u0001\u0000\u0000\u0000\u0662\u0661\u0001\u0000\u0000\u0000\u0663\u0103"+
		"\u0001\u0000\u0000\u0000\u0664\u0667\u0005\u0082\u0000\u0000\u0665\u0668"+
		"\u0003\u01be\u00df\u0000\u0666\u0668\u0003\u0248\u0124\u0000\u0667\u0665"+
		"\u0001\u0000\u0000\u0000\u0667\u0666\u0001\u0000\u0000\u0000\u0668\u0105"+
		"\u0001\u0000\u0000\u0000\u0669\u066a\u0005\u001f\u0000\u0000\u066a\u066b"+
		"\u0003P(\u0000\u066b\u066c\u0005\b\u0000\u0000\u066c\u0107\u0001\u0000"+
		"\u0000\u0000\u066d\u066e\u0005\u001d\u0000\u0000\u066e\u066f\u0003L&\u0000"+
		"\u066f\u0670\u0005\u0004\u0000\u0000\u0670\u0109\u0001\u0000\u0000\u0000"+
		"\u0671\u0675\u0005\u00c6\u0000\u0000\u0672\u0674\u0003\u0170\u00b8\u0000"+
		"\u0673\u0672\u0001\u0000\u0000\u0000\u0674\u0677\u0001\u0000\u0000\u0000"+
		"\u0675\u0673\u0001\u0000\u0000\u0000\u0675\u0676\u0001\u0000\u0000\u0000"+
		"\u0676\u0678\u0001\u0000\u0000\u0000\u0677\u0675\u0001\u0000\u0000\u0000"+
		"\u0678\u067a\u0003\u01d2\u00e9\u0000\u0679\u067b\u0003\u010c\u0086\u0000"+
		"\u067a\u0679\u0001\u0000\u0000\u0000\u067a\u067b\u0001\u0000\u0000\u0000"+
		"\u067b\u067c\u0001\u0000\u0000\u0000\u067c\u067d\u0005\u001f\u0000\u0000"+
		"\u067d\u067e\u0003\u0168\u00b4\u0000\u067e\u067f\u0005\b\u0000\u0000\u067f"+
		"\u010b\u0001\u0000\u0000\u0000\u0680\u0681\u0005\u0080\u0000\u0000\u0681"+
		"\u0682\u0005\u013b\u0000\u0000\u0682\u010d\u0001\u0000\u0000\u0000\u0683"+
		"\u0684\u0005\u00cd\u0000\u0000\u0684\u0689\u0003\u0174\u00ba\u0000\u0685"+
		"\u0686\u0005\t\u0000\u0000\u0686\u0688\u0003\u0174\u00ba\u0000\u0687\u0685"+
		"\u0001\u0000\u0000\u0000\u0688\u068b\u0001\u0000\u0000\u0000\u0689\u0687"+
		"\u0001\u0000\u0000\u0000\u0689\u068a\u0001\u0000\u0000\u0000\u068a\u010f"+
		"\u0001\u0000\u0000\u0000\u068b\u0689\u0001\u0000\u0000\u0000\u068c\u0695"+
		"\u0005\u00cf\u0000\u0000\u068d\u0692\u0003\u020e\u0107\u0000\u068e\u068f"+
		"\u0005\t\u0000\u0000\u068f\u0691\u0003\u020e\u0107\u0000\u0690\u068e\u0001"+
		"\u0000\u0000\u0000\u0691\u0694\u0001\u0000\u0000\u0000\u0692\u0690\u0001"+
		"\u0000\u0000\u0000\u0692\u0693\u0001\u0000\u0000\u0000\u0693\u0696\u0001"+
		"\u0000\u0000\u0000\u0694\u0692\u0001\u0000\u0000\u0000\u0695\u068d\u0001"+
		"\u0000\u0000\u0000\u0695\u0696\u0001\u0000\u0000\u0000\u0696\u0111\u0001"+
		"\u0000\u0000\u0000\u0697\u0698\u0005\u00d1\u0000\u0000\u0698\u069d\u0003"+
		"\u020e\u0107\u0000\u0699\u069a\u0005\t\u0000\u0000\u069a\u069c\u0003\u020e"+
		"\u0107\u0000\u069b\u0699\u0001\u0000\u0000\u0000\u069c\u069f\u0001\u0000"+
		"\u0000\u0000\u069d\u069b\u0001\u0000\u0000\u0000\u069d\u069e\u0001\u0000"+
		"\u0000\u0000\u069e\u0113\u0001\u0000\u0000\u0000\u069f\u069d\u0001\u0000"+
		"\u0000\u0000\u06a0\u06a9\u0005\u00ce\u0000\u0000\u06a1\u06a6\u0003\u0174"+
		"\u00ba\u0000\u06a2\u06a3\u0005\t\u0000\u0000\u06a3\u06a5\u0003\u0174\u00ba"+
		"\u0000\u06a4\u06a2\u0001\u0000\u0000\u0000\u06a5\u06a8\u0001\u0000\u0000"+
		"\u0000\u06a6\u06a4\u0001\u0000\u0000\u0000\u06a6\u06a7\u0001\u0000\u0000"+
		"\u0000\u06a7\u06aa\u0001\u0000\u0000\u0000\u06a8\u06a6\u0001\u0000\u0000"+
		"\u0000\u06a9\u06a1\u0001\u0000\u0000\u0000\u06a9\u06aa\u0001\u0000\u0000"+
		"\u0000\u06aa\u0115\u0001\u0000\u0000\u0000\u06ab\u06b4\u0005\u00d2\u0000"+
		"\u0000\u06ac\u06b1\u0003\u0174\u00ba\u0000\u06ad\u06ae\u0005\t\u0000\u0000"+
		"\u06ae\u06b0\u0003\u0174\u00ba\u0000\u06af\u06ad\u0001\u0000\u0000\u0000"+
		"\u06b0\u06b3\u0001\u0000\u0000\u0000\u06b1\u06af\u0001\u0000\u0000\u0000"+
		"\u06b1\u06b2\u0001\u0000\u0000\u0000\u06b2\u06b5\u0001\u0000\u0000\u0000"+
		"\u06b3\u06b1\u0001\u0000\u0000\u0000\u06b4\u06ac\u0001\u0000\u0000\u0000"+
		"\u06b4\u06b5\u0001\u0000\u0000\u0000\u06b5\u0117\u0001\u0000\u0000\u0000"+
		"\u06b6\u06bf\u0005\u00d3\u0000\u0000\u06b7\u06bc\u0003\u011a\u008d\u0000"+
		"\u06b8\u06b9\u0005\t\u0000\u0000\u06b9\u06bb\u0003\u011a\u008d\u0000\u06ba"+
		"\u06b8\u0001\u0000\u0000\u0000\u06bb\u06be\u0001\u0000\u0000\u0000\u06bc"+
		"\u06ba\u0001\u0000\u0000\u0000\u06bc\u06bd\u0001\u0000\u0000\u0000\u06bd"+
		"\u06c0\u0001\u0000\u0000\u0000\u06be\u06bc\u0001\u0000\u0000\u0000\u06bf"+
		"\u06b7\u0001\u0000\u0000\u0000\u06bf\u06c0\u0001\u0000\u0000\u0000\u06c0"+
		"\u0119\u0001\u0000\u0000\u0000\u06c1\u06c3\u0003\u020e\u0107\u0000\u06c2"+
		"\u06c4\u0007\b\u0000\u0000\u06c3\u06c2\u0001\u0000\u0000\u0000\u06c3\u06c4"+
		"\u0001\u0000\u0000\u0000\u06c4\u011b\u0001\u0000\u0000\u0000\u06c5\u06c9"+
		"\u0005\u00d7\u0000\u0000\u06c6\u06c8\u0003\u016e\u00b7\u0000\u06c7\u06c6"+
		"\u0001\u0000\u0000\u0000\u06c8\u06cb\u0001\u0000\u0000\u0000\u06c9\u06c7"+
		"\u0001\u0000\u0000\u0000\u06c9\u06ca\u0001\u0000\u0000\u0000\u06ca\u06cc"+
		"\u0001\u0000\u0000\u0000\u06cb\u06c9\u0001\u0000\u0000\u0000\u06cc\u06cd"+
		"\u00059\u0000\u0000\u06cd\u06cf\u0003\u0174\u00ba\u0000\u06ce\u06d0\u0003"+
		"\u011e\u008f\u0000\u06cf\u06ce\u0001\u0000\u0000\u0000\u06cf\u06d0\u0001"+
		"\u0000\u0000\u0000\u06d0\u011d\u0001\u0000\u0000\u0000\u06d1\u06d2\u0005"+
		"\u0104\u0000\u0000\u06d2\u06d7\u0003\u0174\u00ba\u0000\u06d3\u06d4\u0005"+
		"\t\u0000\u0000\u06d4\u06d6\u0003\u0174\u00ba\u0000\u06d5\u06d3\u0001\u0000"+
		"\u0000\u0000\u06d6\u06d9\u0001\u0000\u0000\u0000\u06d7\u06d5\u0001\u0000"+
		"\u0000\u0000\u06d7\u06d8\u0001\u0000\u0000\u0000\u06d8\u011f\u0001\u0000"+
		"\u0000\u0000\u06d9\u06d7\u0001\u0000\u0000\u0000\u06da\u06db\u0005\u00da"+
		"\u0000\u0000\u06db\u06de\u0007\t\u0000\u0000\u06dc\u06df\u0003\u0122\u0091"+
		"\u0000\u06dd\u06df\u0003\u0124\u0092\u0000\u06de\u06dc\u0001\u0000\u0000"+
		"\u0000\u06de\u06dd\u0001\u0000\u0000\u0000\u06de\u06df\u0001\u0000\u0000"+
		"\u0000\u06df\u0121\u0001\u0000\u0000\u0000\u06e0\u06e1\u0005\u0104\u0000"+
		"\u0000\u06e1\u06ea\u0005\u001f\u0000\u0000\u06e2\u06e7\u0003\u0126\u0093"+
		"\u0000\u06e3\u06e4\u0005\t\u0000\u0000\u06e4\u06e6\u0003\u0126\u0093\u0000"+
		"\u06e5\u06e3\u0001\u0000\u0000\u0000\u06e6\u06e9\u0001\u0000\u0000\u0000"+
		"\u06e7\u06e5\u0001\u0000\u0000\u0000\u06e7\u06e8\u0001\u0000\u0000\u0000"+
		"\u06e8\u06eb\u0001\u0000\u0000\u0000\u06e9\u06e7\u0001\u0000\u0000\u0000"+
		"\u06ea\u06e2\u0001\u0000\u0000\u0000\u06ea\u06eb\u0001\u0000\u0000\u0000"+
		"\u06eb\u06ec\u0001\u0000\u0000\u0000\u06ec\u06ed\u0005\b\u0000\u0000\u06ed"+
		"\u0123\u0001\u0000\u0000\u0000\u06ee\u06f0\u0003\u012a\u0095\u0000\u06ef"+
		"\u06ee\u0001\u0000\u0000\u0000\u06f0\u06f1\u0001\u0000\u0000\u0000\u06f1"+
		"\u06ef\u0001\u0000\u0000\u0000\u06f1\u06f2\u0001\u0000\u0000\u0000\u06f2"+
		"\u0125\u0001\u0000\u0000\u0000\u06f3\u06f4\u0005\u00f5\u0000\u0000\u06f4"+
		"\u06f5\u0005\u0011\u0000\u0000\u06f5\u0727\u0003\u01a6\u00d3\u0000\u06f6"+
		"\u06f7\u0005\u010d\u0000\u0000\u06f7\u06f8\u0005\u0011\u0000\u0000\u06f8"+
		"\u0727\u0003\u0208\u0104\u0000\u06f9\u06fa\u0005\u00e3\u0000\u0000\u06fa"+
		"\u06fb\u0005\u0011\u0000\u0000\u06fb\u0727\u0003\u0128\u0094\u0000\u06fc"+
		"\u06fd\u0005\u0112\u0000\u0000\u06fd\u06fe\u0005\u0011\u0000\u0000\u06fe"+
		"\u0727\u0003\u0128\u0094\u0000\u06ff\u0700\u0005-\u0000\u0000\u0700\u0701"+
		"\u0005\u0011\u0000\u0000\u0701\u0727\u0003\u0128\u0094\u0000\u0702\u0703"+
		"\u0005\u0089\u0000\u0000\u0703\u0704\u0005\u0011\u0000\u0000\u0704\u0727"+
		"\u0007\n\u0000\u0000\u0705\u0706\u0005\u0110\u0000\u0000\u0706\u0707\u0005"+
		"\u0011\u0000\u0000\u0707\u0727\u0003\u01a6\u00d3\u0000\u0708\u0709\u0005"+
		"\u0116\u0000\u0000\u0709\u070a\u0005\u0011\u0000\u0000\u070a\u0727\u0003"+
		"\u01a6\u00d3\u0000\u070b\u070c\u0005\u010c\u0000\u0000\u070c\u070d\u0005"+
		"\u0011\u0000\u0000\u070d\u0727\u0007\u000b\u0000\u0000\u070e\u070f\u0005"+
		"\u0111\u0000\u0000\u070f\u0710\u0005\u0011\u0000\u0000\u0710\u0727\u0007"+
		"\u000b\u0000\u0000\u0711\u0712\u0005\u008c\u0000\u0000\u0712\u0713\u0005"+
		"\u0011\u0000\u0000\u0713\u0727\u0007\f\u0000\u0000\u0714\u0715\u0005\u0115"+
		"\u0000\u0000\u0715\u0716\u0005\u0011\u0000\u0000\u0716\u0727\u0007\r\u0000"+
		"\u0000\u0717\u0718\u0005\'\u0000\u0000\u0718\u0719\u0005\u0011\u0000\u0000"+
		"\u0719\u0727\u0005\u0136\u0000\u0000\u071a\u071b\u0005\u0114\u0000\u0000"+
		"\u071b\u071c\u0005\u0011\u0000\u0000\u071c\u0727\u0003\u022c\u0116\u0000"+
		"\u071d\u071e\u0005\u0113\u0000\u0000\u071e\u071f\u0005\u0011\u0000\u0000"+
		"\u071f\u0727\u0003\u022c\u0116\u0000\u0720\u0721\u0005\u010f\u0000\u0000"+
		"\u0721\u0722\u0005\u0011\u0000\u0000\u0722\u0727\u0003\u0226\u0113\u0000"+
		"\u0723\u0724\u0005\u010e\u0000\u0000\u0724\u0725\u0005\u0011\u0000\u0000"+
		"\u0725\u0727\u0003\u0226\u0113\u0000\u0726\u06f3\u0001\u0000\u0000\u0000"+
		"\u0726\u06f6\u0001\u0000\u0000\u0000\u0726\u06f9\u0001\u0000\u0000\u0000"+
		"\u0726\u06fc\u0001\u0000\u0000\u0000\u0726\u06ff\u0001\u0000\u0000\u0000"+
		"\u0726\u0702\u0001\u0000\u0000\u0000\u0726\u0705\u0001\u0000\u0000\u0000"+
		"\u0726\u0708\u0001\u0000\u0000\u0000\u0726\u070b\u0001\u0000\u0000\u0000"+
		"\u0726\u070e\u0001\u0000\u0000\u0000\u0726\u0711\u0001\u0000\u0000\u0000"+
		"\u0726\u0714\u0001\u0000\u0000\u0000\u0726\u0717\u0001\u0000\u0000\u0000"+
		"\u0726\u071a\u0001\u0000\u0000\u0000\u0726\u071d\u0001\u0000\u0000\u0000"+
		"\u0726\u0720\u0001\u0000\u0000\u0000\u0726\u0723\u0001\u0000\u0000\u0000"+
		"\u0727\u0127\u0001\u0000\u0000\u0000\u0728\u072d\u0003\u020a\u0105\u0000"+
		"\u0729\u072a\u0005\t\u0000\u0000\u072a\u072c\u0003\u020a\u0105\u0000\u072b"+
		"\u0729\u0001\u0000\u0000\u0000\u072c\u072f\u0001\u0000\u0000\u0000\u072d"+
		"\u072b\u0001\u0000\u0000\u0000\u072d\u072e\u0001\u0000\u0000\u0000\u072e"+
		"\u0129\u0001\u0000\u0000\u0000\u072f\u072d\u0001\u0000\u0000\u0000\u0730"+
		"\u0731\u0005\u00f5\u0000\u0000\u0731\u0732\u0005\u0011\u0000\u0000\u0732"+
		"\u073e\u0003\u0246\u0123\u0000\u0733\u0734\u0005\u0089\u0000\u0000\u0734"+
		"\u0735\u0005\u0011\u0000\u0000\u0735\u073e\u0007\n\u0000\u0000\u0736\u0737"+
		"\u0005\u0104\u0000\u0000\u0737\u073e\u0003\u0246\u0123\u0000\u0738\u0739"+
		"\u00059\u0000\u0000\u0739\u073e\u0003\u0128\u0094\u0000\u073a\u073b\u0005"+
		"\'\u0000\u0000\u073b\u073c\u0005\u0011\u0000\u0000\u073c\u073e\u0005\u0136"+
		"\u0000\u0000\u073d\u0730\u0001\u0000\u0000\u0000\u073d\u0733\u0001\u0000"+
		"\u0000\u0000\u073d\u0736\u0001\u0000\u0000\u0000\u073d\u0738\u0001\u0000"+
		"\u0000\u0000\u073d\u073a\u0001\u0000\u0000\u0000\u073e\u012b\u0001\u0000"+
		"\u0000\u0000\u073f\u0743\u0005\u00de\u0000\u0000\u0740\u0742\u0003\u016e"+
		"\u00b7\u0000\u0741\u0740\u0001\u0000\u0000\u0000\u0742\u0745\u0001\u0000"+
		"\u0000\u0000\u0743\u0741\u0001\u0000\u0000\u0000\u0743\u0744\u0001\u0000"+
		"\u0000\u0000\u0744\u0746\u0001\u0000\u0000\u0000\u0745\u0743\u0001\u0000"+
		"\u0000\u0000\u0746\u0747\u0003\u0174\u00ba\u0000\u0747\u0748\u0005\u00b9"+
		"\u0000\u0000\u0748\u0749\u0003\u0174\u00ba\u0000\u0749\u012d\u0001\u0000"+
		"\u0000\u0000\u074a\u074e\u0005\u00dd\u0000\u0000\u074b\u074d\u0003\u016e"+
		"\u00b7\u0000\u074c\u074b\u0001\u0000\u0000\u0000\u074d\u0750\u0001\u0000"+
		"\u0000\u0000\u074e\u074c\u0001\u0000\u0000\u0000\u074e\u074f\u0001\u0000"+
		"\u0000\u0000\u074f\u0751\u0001\u0000\u0000\u0000\u0750\u074e\u0001\u0000"+
		"\u0000\u0000\u0751\u0752\u0003\u0174\u00ba\u0000\u0752\u012f\u0001\u0000"+
		"\u0000\u0000\u0753\u0757\u0005\u00df\u0000\u0000\u0754\u0756\u0003\u0170"+
		"\u00b8\u0000\u0755\u0754\u0001\u0000\u0000\u0000\u0756\u0759\u0001\u0000"+
		"\u0000\u0000\u0757\u0755\u0001\u0000\u0000\u0000\u0757\u0758\u0001\u0000"+
		"\u0000\u0000\u0758\u075b\u0001\u0000\u0000\u0000\u0759\u0757\u0001\u0000"+
		"\u0000\u0000\u075a\u075c\u0003\u0132\u0099\u0000\u075b\u075a\u0001\u0000"+
		"\u0000\u0000\u075b\u075c\u0001\u0000\u0000\u0000\u075c\u075e\u0001\u0000"+
		"\u0000\u0000\u075d\u075f\u0003\u0134\u009a\u0000\u075e\u075d\u0001\u0000"+
		"\u0000\u0000\u075e\u075f\u0001\u0000\u0000\u0000\u075f\u0761\u0001\u0000"+
		"\u0000\u0000\u0760\u0762\u0003\u0136\u009b\u0000\u0761\u0760\u0001\u0000"+
		"\u0000\u0000\u0761\u0762\u0001\u0000\u0000\u0000\u0762\u0763\u0001\u0000"+
		"\u0000\u0000\u0763\u0764\u0005\u0104\u0000\u0000\u0764\u0766\u0005\u001f"+
		"\u0000\u0000\u0765\u0767\u0003\u0138\u009c\u0000\u0766\u0765\u0001\u0000"+
		"\u0000\u0000\u0767\u0768\u0001\u0000\u0000\u0000\u0768\u0766\u0001\u0000"+
		"\u0000\u0000\u0768\u0769\u0001\u0000\u0000\u0000\u0769\u076a\u0001\u0000"+
		"\u0000\u0000\u076a\u076b\u0005\b\u0000\u0000\u076b\u0131\u0001\u0000\u0000"+
		"\u0000\u076c\u076d\u0005\u00bd\u0000\u0000\u076d\u076e\u00059\u0000\u0000"+
		"\u076e\u076f\u0003\u014a\u00a5\u0000\u076f\u0770\u0005\t\u0000\u0000\u0770"+
		"\u0771\u0003\u014a\u00a5\u0000\u0771\u0133\u0001\u0000\u0000\u0000\u0772"+
		"\u0773\u0005\u00c5\u0000\u0000\u0773\u0774\u00059\u0000\u0000\u0774\u0779"+
		"\u0003\u017c\u00be\u0000\u0775\u0776\u0005\t\u0000\u0000\u0776\u0778\u0003"+
		"\u017c\u00be\u0000\u0777\u0775\u0001\u0000\u0000\u0000\u0778\u077b\u0001"+
		"\u0000\u0000\u0000\u0779\u0777\u0001\u0000\u0000\u0000\u0779\u077a\u0001"+
		"\u0000\u0000\u0000\u077a\u0135\u0001\u0000\u0000\u0000\u077b\u0779\u0001"+
		"\u0000\u0000\u0000\u077c\u077d\u0005H\u0000\u0000\u077d\u077e\u0005\u001f"+
		"\u0000\u0000\u077e\u0783\u0003\u0018\f\u0000\u077f\u0780\u0005\t\u0000"+
		"\u0000\u0780\u0782\u0003\u0018\f\u0000\u0781\u077f\u0001\u0000\u0000\u0000"+
		"\u0782\u0785\u0001\u0000\u0000\u0000\u0783\u0781\u0001\u0000\u0000\u0000"+
		"\u0783\u0784\u0001\u0000\u0000\u0000\u0784\u0786\u0001\u0000\u0000\u0000"+
		"\u0785\u0783\u0001\u0000\u0000\u0000\u0786\u0787\u0005\b\u0000\u0000\u0787"+
		"\u0137\u0001\u0000\u0000\u0000\u0788\u0789\u0005\u00ed\u0000\u0000\u0789"+
		"\u078b\u0003\u0206\u0103\u0000\u078a\u078c\u0005\u00bb\u0000\u0000\u078b"+
		"\u078a\u0001\u0000\u0000\u0000\u078b\u078c\u0001\u0000\u0000\u0000\u078c"+
		"\u078e\u0001\u0000\u0000\u0000\u078d\u078f\u0003\u013a\u009d\u0000\u078e"+
		"\u078d\u0001\u0000\u0000\u0000\u078e\u078f\u0001\u0000\u0000\u0000\u078f"+
		"\u0790\u0001\u0000\u0000\u0000\u0790\u0791\u0005\n\u0000\u0000\u0791\u0793"+
		"\u0003\u017c\u00be\u0000\u0792\u0794\u0003\u013c\u009e\u0000\u0793\u0792"+
		"\u0001\u0000\u0000\u0000\u0793\u0794\u0001\u0000\u0000\u0000\u0794\u0795"+
		"\u0001\u0000\u0000\u0000\u0795\u0796\u0005\"\u0000\u0000\u0796\u0139\u0001"+
		"\u0000\u0000\u0000\u0797\u0798\u0005\u00bf\u0000\u0000\u0798\u0799\u0005"+
		"\u0011\u0000\u0000\u0799\u079a\u0007\u000e\u0000\u0000\u079a\u013b\u0001"+
		"\u0000\u0000\u0000\u079b\u079c\u0005$\u0000\u0000\u079c\u07a1\u0003\u013e"+
		"\u009f\u0000\u079d\u079e\u0005\t\u0000\u0000\u079e\u07a0\u0003\u013e\u009f"+
		"\u0000\u079f\u079d\u0001\u0000\u0000\u0000\u07a0\u07a3\u0001\u0000\u0000"+
		"\u0000\u07a1\u079f\u0001\u0000\u0000\u0000\u07a1\u07a2\u0001\u0000\u0000"+
		"\u0000\u07a2\u013d\u0001\u0000\u0000\u0000\u07a3\u07a1\u0001\u0000\u0000"+
		"\u0000\u07a4\u07a5\u0003\u0206\u0103\u0000\u07a5\u07a6\u0005\u0011\u0000"+
		"\u0000\u07a6\u07a7\u0003\u017c\u00be\u0000\u07a7\u013f\u0001\u0000\u0000"+
		"\u0000\u07a8\u07ac\u0005\u00e1\u0000\u0000\u07a9\u07ab\u0003\u0170\u00b8"+
		"\u0000\u07aa\u07a9\u0001\u0000\u0000\u0000\u07ab\u07ae\u0001\u0000\u0000"+
		"\u0000\u07ac\u07aa\u0001\u0000\u0000\u0000\u07ac\u07ad\u0001\u0000\u0000"+
		"\u0000\u07ad\u07b0\u0001\u0000\u0000\u0000\u07ae\u07ac\u0001\u0000\u0000"+
		"\u0000\u07af\u07b1\u0003\u01cc\u00e6\u0000\u07b0\u07af\u0001\u0000\u0000"+
		"\u0000\u07b0\u07b1\u0001\u0000\u0000\u0000\u07b1\u07b3\u0001\u0000\u0000"+
		"\u0000\u07b2\u07b4\u0003\u0144\u00a2\u0000\u07b3\u07b2\u0001\u0000\u0000"+
		"\u0000\u07b3\u07b4\u0001\u0000\u0000\u0000\u07b4\u07b8\u0001\u0000\u0000"+
		"\u0000\u07b5\u07b9\u0003\u017c\u00be\u0000\u07b6\u07b9\u0003\u01c6\u00e3"+
		"\u0000\u07b7\u07b9\u0003\u0142\u00a1\u0000\u07b8\u07b5\u0001\u0000\u0000"+
		"\u0000\u07b8\u07b6\u0001\u0000\u0000\u0000\u07b8\u07b7\u0001\u0000\u0000"+
		"\u0000\u07b9\u0141\u0001\u0000\u0000\u0000\u07ba\u07bb\u0005\u0001\u0000"+
		"\u0000\u07bb\u07bc\u0005+\u0000\u0000\u07bc\u07bd\u0003\u017c\u00be\u0000"+
		"\u07bd\u0143\u0001\u0000\u0000\u0000\u07be\u07bf\u0005\u0082\u0000\u0000"+
		"\u07bf\u07c0\u0005\u001f\u0000\u0000\u07c0\u07c5\u0003\u0090H\u0000\u07c1"+
		"\u07c2\u0005\t\u0000\u0000\u07c2\u07c4\u0003\u0090H\u0000\u07c3\u07c1"+
		"\u0001\u0000\u0000\u0000\u07c4\u07c7\u0001\u0000\u0000\u0000\u07c5\u07c3"+
		"\u0001\u0000\u0000\u0000\u07c5\u07c6\u0001\u0000\u0000\u0000\u07c6\u07c8"+
		"\u0001\u0000\u0000\u0000\u07c7\u07c5\u0001\u0000\u0000\u0000\u07c8\u07c9"+
		"\u0005\b\u0000\u0000\u07c9\u0145\u0001\u0000\u0000\u0000\u07ca\u07ce\u0005"+
		"\u00e2\u0000\u0000\u07cb\u07cd\u0003\u016e\u00b7\u0000\u07cc\u07cb\u0001"+
		"\u0000\u0000\u0000\u07cd\u07d0\u0001\u0000\u0000\u0000\u07ce\u07cc\u0001"+
		"\u0000\u0000\u0000\u07ce\u07cf\u0001\u0000\u0000\u0000\u07cf\u07d1\u0001"+
		"\u0000\u0000\u0000\u07d0\u07ce\u0001\u0000\u0000\u0000\u07d1\u07d6\u0003"+
		"\u0174\u00ba\u0000\u07d2\u07d3\u0005\t\u0000\u0000\u07d3\u07d5\u0003\u0174"+
		"\u00ba\u0000\u07d4\u07d2\u0001\u0000\u0000\u0000\u07d5\u07d8\u0001\u0000"+
		"\u0000\u0000\u07d6\u07d4\u0001\u0000\u0000\u0000\u07d6\u07d7\u0001\u0000"+
		"\u0000\u0000\u07d7\u0147\u0001\u0000\u0000\u0000\u07d8\u07d6\u0001\u0000"+
		"\u0000\u0000\u07d9\u07dd\u0007\u000f\u0000\u0000\u07da\u07dc\u0003\u0170"+
		"\u00b8\u0000\u07db\u07da\u0001\u0000\u0000\u0000\u07dc\u07df\u0001\u0000"+
		"\u0000\u0000\u07dd\u07db\u0001\u0000\u0000\u0000\u07dd\u07de\u0001\u0000"+
		"\u0000\u0000\u07de\u07e0\u0001\u0000\u0000\u0000\u07df\u07dd\u0001\u0000"+
		"\u0000\u0000\u07e0\u07e1\u00059\u0000\u0000\u07e1\u07e6\u0003\u014a\u00a5"+
		"\u0000\u07e2\u07e3\u0005\t\u0000\u0000\u07e3\u07e5\u0003\u014a\u00a5\u0000"+
		"\u07e4\u07e2\u0001\u0000\u0000\u0000\u07e5\u07e8\u0001\u0000\u0000\u0000"+
		"\u07e6\u07e4\u0001\u0000\u0000\u0000\u07e6\u07e7\u0001\u0000\u0000\u0000"+
		"\u07e7\u0149\u0001\u0000\u0000\u0000\u07e8\u07e6\u0001\u0000\u0000\u0000"+
		"\u07e9\u07ea\u0003\u0174\u00ba\u0000\u07ea\u07eb\u0003\u014c\u00a6\u0000"+
		"\u07eb\u014b\u0001\u0000\u0000\u0000\u07ec\u07ee\u0007\u0010\u0000\u0000"+
		"\u07ed\u07ec\u0001\u0000\u0000\u0000\u07ed\u07ee\u0001\u0000\u0000\u0000"+
		"\u07ee\u07f1\u0001\u0000\u0000\u0000\u07ef\u07f0\u0005\u00b8\u0000\u0000"+
		"\u07f0\u07f2\u0007\u0011\u0000\u0000\u07f1\u07ef\u0001\u0000\u0000\u0000"+
		"\u07f1\u07f2\u0001\u0000\u0000\u0000\u07f2\u014d\u0001\u0000\u0000\u0000"+
		"\u07f3\u07f7\u0005\u00ee\u0000\u0000\u07f4\u07f6\u0003\u016e\u00b7\u0000"+
		"\u07f5\u07f4\u0001\u0000\u0000\u0000\u07f6\u07f9\u0001\u0000\u0000\u0000"+
		"\u07f7\u07f5\u0001\u0000\u0000\u0000\u07f7\u07f8\u0001\u0000\u0000\u0000"+
		"\u07f8\u0802\u0001\u0000\u0000\u0000\u07f9\u07f7\u0001\u0000\u0000\u0000"+
		"\u07fa\u07ff\u0003\u0174\u00ba\u0000\u07fb\u07fc\u0005\t\u0000\u0000\u07fc"+
		"\u07fe\u0003\u0174\u00ba\u0000\u07fd\u07fb\u0001\u0000\u0000\u0000\u07fe"+
		"\u0801\u0001\u0000\u0000\u0000\u07ff\u07fd\u0001\u0000\u0000\u0000\u07ff"+
		"\u0800\u0001\u0000\u0000\u0000\u0800\u0803\u0001\u0000\u0000\u0000\u0801"+
		"\u07ff\u0001\u0000\u0000\u0000\u0802\u07fa\u0001\u0000\u0000\u0000\u0802"+
		"\u0803\u0001\u0000\u0000\u0000\u0803\u0805\u0001\u0000\u0000\u0000\u0804"+
		"\u0806\u0003\u0150\u00a8\u0000\u0805\u0804\u0001\u0000\u0000\u0000\u0805"+
		"\u0806\u0001\u0000\u0000\u0000\u0806\u014f\u0001\u0000\u0000\u0000\u0807"+
		"\u0808\u00059\u0000\u0000\u0808\u0809\u0003\u0174\u00ba\u0000\u0809\u080a"+
		"\u0005\t\u0000\u0000\u080a\u080b\u0003\u0174\u00ba\u0000\u080b\u080d\u0001"+
		"\u0000\u0000\u0000\u080c\u080e\u0003\u0152\u00a9\u0000\u080d\u080c\u0001"+
		"\u0000\u0000\u0000\u080d\u080e\u0001\u0000\u0000\u0000\u080e\u0151\u0001"+
		"\u0000\u0000\u0000\u080f\u0810\u00057\u0000\u0000\u0810\u0811\u0005\u0011"+
		"\u0000\u0000\u0811\u0812\u0003\u022a\u0115\u0000\u0812\u0153\u0001\u0000"+
		"\u0000\u0000\u0813\u0817\u0007\u0012\u0000\u0000\u0814\u0816\u0003\u016e"+
		"\u00b7\u0000\u0815\u0814\u0001\u0000\u0000\u0000\u0816\u0819\u0001\u0000"+
		"\u0000\u0000\u0817\u0815\u0001\u0000\u0000\u0000\u0817\u0818\u0001\u0000"+
		"\u0000\u0000\u0818\u081a\u0001\u0000\u0000\u0000\u0819\u0817\u0001\u0000"+
		"\u0000\u0000\u081a\u081b\u0003\u0174\u00ba\u0000\u081b\u0155\u0001\u0000"+
		"\u0000\u0000\u081c\u0820\u0005\u00f7\u0000\u0000\u081d\u081f\u0003\u016e"+
		"\u00b7\u0000\u081e\u081d\u0001\u0000\u0000\u0000\u081f\u0822\u0001\u0000"+
		"\u0000\u0000\u0820\u081e\u0001\u0000\u0000\u0000\u0820\u0821\u0001\u0000"+
		"\u0000\u0000\u0821\u0823\u0001\u0000\u0000\u0000\u0822\u0820\u0001\u0000"+
		"\u0000\u0000\u0823\u0824\u0003\u0174\u00ba\u0000\u0824\u0825\u00059\u0000"+
		"\u0000\u0825\u0826\u0003\u014a\u00a5\u0000\u0826\u0157\u0001\u0000\u0000"+
		"\u0000\u0827\u0828\u0005\u00f8\u0000\u0000\u0828\u0829\u0003\u0174\u00ba"+
		"\u0000\u0829\u082a\u0005\u00b9\u0000\u0000\u082a\u082c\u0003\u0174\u00ba"+
		"\u0000\u082b\u082d\u0003\u015a\u00ad\u0000\u082c\u082b\u0001\u0000\u0000"+
		"\u0000\u082c\u082d\u0001\u0000\u0000\u0000\u082d\u0159\u0001\u0000\u0000"+
		"\u0000\u082e\u082f\u00059\u0000\u0000\u082f\u0830\u0003\u014a\u00a5\u0000"+
		"\u0830\u015b\u0001\u0000\u0000\u0000\u0831\u0836\u0003\u015e\u00af\u0000"+
		"\u0832\u0833\u0005\t\u0000\u0000\u0833\u0835\u0003\u015e\u00af\u0000\u0834"+
		"\u0832\u0001\u0000\u0000\u0000\u0835\u0838\u0001\u0000\u0000\u0000\u0836"+
		"\u0834\u0001\u0000\u0000\u0000\u0836\u0837\u0001\u0000\u0000\u0000\u0837"+
		"\u015d\u0001\u0000\u0000\u0000\u0838\u0836\u0001\u0000\u0000\u0000\u0839"+
		"\u083b\u0005\u00f9\u0000\u0000\u083a\u083c\u0003\u0174\u00ba\u0000\u083b"+
		"\u083a\u0001\u0000\u0000\u0000\u083b\u083c\u0001\u0000\u0000\u0000\u083c"+
		"\u083d\u0001\u0000\u0000\u0000\u083d\u083e\u0005\u00b9\u0000\u0000\u083e"+
		"\u0840\u0003\u0174\u00ba\u0000\u083f\u0841\u0003\u0160\u00b0\u0000\u0840"+
		"\u083f\u0001\u0000\u0000\u0000\u0840\u0841\u0001\u0000\u0000\u0000\u0841"+
		"\u0842\u0001\u0000\u0000\u0000\u0842\u0843\u00059\u0000\u0000\u0843\u0844"+
		"\u0003\u014a\u00a5\u0000\u0844\u015f\u0001\u0000\u0000\u0000\u0845\u0846"+
		"\u0005\u0104\u0000\u0000\u0846\u0847\u0005\u00be\u0000\u0000\u0847\u0848"+
		"\u0005\u0011\u0000\u0000\u0848\u0849\u0003\u0174\u00ba\u0000\u0849\u0161"+
		"\u0001\u0000\u0000\u0000\u084a\u084e\u0005\u00fe\u0000\u0000\u084b\u084d"+
		"\u0003\u0170\u00b8\u0000\u084c\u084b\u0001\u0000\u0000\u0000\u084d\u0850"+
		"\u0001\u0000\u0000\u0000\u084e\u084c\u0001\u0000\u0000\u0000\u084e\u084f"+
		"\u0001\u0000\u0000\u0000\u084f\u0851\u0001\u0000\u0000\u0000\u0850\u084e"+
		"\u0001\u0000\u0000\u0000\u0851\u0856\u0003\u0164\u00b2\u0000\u0852\u0853"+
		"\u0005\t\u0000\u0000\u0853\u0855\u0003\u0164\u00b2\u0000\u0854\u0852\u0001"+
		"\u0000\u0000\u0000\u0855\u0858\u0001\u0000\u0000\u0000\u0856\u0854\u0001"+
		"\u0000\u0000\u0000\u0856\u0857\u0001\u0000\u0000\u0000\u0857\u0163\u0001"+
		"\u0000\u0000\u0000\u0858\u0856\u0001\u0000\u0000\u0000\u0859\u085d\u0003"+
		"\u01e6\u00f3\u0000\u085a\u085d\u0003\u01e0\u00f0\u0000\u085b\u085d\u0003"+
		"\u01ce\u00e7\u0000\u085c\u0859\u0001\u0000\u0000\u0000\u085c\u085a\u0001"+
		"\u0000\u0000\u0000\u085c\u085b\u0001\u0000\u0000\u0000\u085d\u0165\u0001"+
		"\u0000\u0000\u0000\u085e\u0862\u0007\u0013\u0000\u0000\u085f\u0861\u0003"+
		"\u016e\u00b7\u0000\u0860\u085f\u0001\u0000\u0000\u0000\u0861\u0864\u0001"+
		"\u0000\u0000\u0000\u0862\u0860\u0001\u0000\u0000\u0000\u0862\u0863\u0001"+
		"\u0000\u0000\u0000\u0863\u0865\u0001\u0000\u0000\u0000\u0864\u0862\u0001"+
		"\u0000\u0000\u0000\u0865\u0866\u0003\u0174\u00ba\u0000\u0866\u0167\u0001"+
		"\u0000\u0000\u0000\u0867\u086a\u0003P(\u0000\u0868\u086a\u0003\u016a\u00b5"+
		"\u0000\u0869\u0867\u0001\u0000\u0000\u0000\u0869\u0868\u0001\u0000\u0000"+
		"\u0000\u086a\u0169\u0001\u0000\u0000\u0000\u086b\u086f\u0003\u01ec\u00f6"+
		"\u0000\u086c\u086e\u0003\u016c\u00b6\u0000\u086d\u086c\u0001\u0000\u0000"+
		"\u0000\u086e\u0871\u0001\u0000\u0000\u0000\u086f\u086d\u0001\u0000\u0000"+
		"\u0000\u086f\u0870\u0001\u0000\u0000\u0000\u0870\u016b\u0001\u0000\u0000"+
		"\u0000\u0871\u086f\u0001\u0000\u0000\u0000\u0872\u0873\u0005\u0003\u0000"+
		"\u0000\u0873\u0874\u0003T*\u0000\u0874\u016d\u0001\u0000\u0000\u0000\u0875"+
		"\u0876\u0007\u0014\u0000\u0000\u0876\u0879\u0005\u0011\u0000\u0000\u0877"+
		"\u087a\u0003\u0218\u010c\u0000\u0878\u087a\u0003\u0226\u0113\u0000\u0879"+
		"\u0877\u0001\u0000\u0000\u0000\u0879\u0878\u0001\u0000\u0000\u0000\u087a"+
		"\u016f\u0001\u0000\u0000\u0000\u087b\u087c\u0007\u0015\u0000\u0000\u087c"+
		"\u087f\u0005\u0011\u0000\u0000\u087d\u0880\u0003\u0218\u010c\u0000\u087e"+
		"\u0880\u0003\u0226\u0113\u0000\u087f\u087d\u0001\u0000\u0000\u0000\u087f"+
		"\u087e\u0001\u0000\u0000\u0000\u0880\u0171\u0001\u0000\u0000\u0000\u0881"+
		"\u0882\u0005\u013c\u0000\u0000\u0882\u0885\u0005\u0011\u0000\u0000\u0883"+
		"\u0886\u0003\u0218\u010c\u0000\u0884\u0886\u0003\u0226\u0113\u0000\u0885"+
		"\u0883\u0001\u0000\u0000\u0000\u0885\u0884\u0001\u0000\u0000\u0000\u0886"+
		"\u0173\u0001\u0000\u0000\u0000\u0887\u0889\u0003\u0176\u00bb\u0000\u0888"+
		"\u0887\u0001\u0000\u0000\u0000\u0888\u0889\u0001\u0000\u0000\u0000\u0889"+
		"\u088a\u0001\u0000\u0000\u0000\u088a\u088b\u0003\u017c\u00be\u0000\u088b"+
		"\u0175\u0001\u0000\u0000\u0000\u088c\u088f\u0003\u021c\u010e\u0000\u088d"+
		"\u088f\u0003\u0178\u00bc\u0000\u088e\u088c\u0001\u0000\u0000\u0000\u088e"+
		"\u088d\u0001\u0000\u0000\u0000\u088f\u0890\u0001\u0000\u0000\u0000\u0890"+
		"\u0891\u0005\u0011\u0000\u0000\u0891\u0177\u0001\u0000\u0000\u0000\u0892"+
		"\u0893\u0005\u001f\u0000\u0000\u0893\u0898\u0003\u021c\u010e\u0000\u0894"+
		"\u0895\u0005\t\u0000\u0000\u0895\u0897\u0003\u021c\u010e\u0000\u0896\u0894"+
		"\u0001\u0000\u0000\u0000\u0897\u089a\u0001\u0000\u0000\u0000\u0898\u0896"+
		"\u0001\u0000\u0000\u0000\u0898\u0899\u0001\u0000\u0000\u0000\u0899\u089b"+
		"\u0001\u0000\u0000\u0000\u089a\u0898\u0001\u0000\u0000\u0000\u089b\u089c"+
		"\u0005\b\u0000\u0000\u089c\u0179\u0001\u0000\u0000\u0000\u089d\u089e\u0003"+
		"\u0208\u0104\u0000\u089e\u089f\u0005\u000f\u0000\u0000\u089f\u08a0\u0003"+
		"\u01be\u00df\u0000\u08a0\u017b\u0001\u0000\u0000\u0000\u08a1\u08a2\u0003"+
		"\u017e\u00bf\u0000\u08a2\u017d\u0001\u0000\u0000\u0000\u08a3\u08a7\u0003"+
		"\u0182\u00c1\u0000\u08a4\u08a6\u0003\u0180\u00c0\u0000\u08a5\u08a4\u0001"+
		"\u0000\u0000\u0000\u08a6\u08a9\u0001\u0000\u0000\u0000\u08a7\u08a5\u0001"+
		"\u0000\u0000\u0000\u08a7\u08a8\u0001\u0000\u0000\u0000\u08a8\u017f\u0001"+
		"\u0000\u0000\u0000\u08a9\u08a7\u0001\u0000\u0000\u0000\u08aa\u08ab\u0005"+
		"\u00bc\u0000\u0000\u08ab\u08ac\u0003\u0182\u00c1\u0000\u08ac\u0181\u0001"+
		"\u0000\u0000\u0000\u08ad\u08b1\u0003\u0186\u00c3\u0000\u08ae\u08b0\u0003"+
		"\u0184\u00c2\u0000\u08af\u08ae\u0001\u0000\u0000\u0000\u08b0\u08b3\u0001"+
		"\u0000\u0000\u0000\u08b1\u08af\u0001\u0000\u0000\u0000\u08b1\u08b2\u0001"+
		"\u0000\u0000\u0000\u08b2\u0183\u0001\u0000\u0000\u0000\u08b3\u08b1\u0001"+
		"\u0000\u0000\u0000\u08b4\u08b5\u0005+\u0000\u0000\u08b5\u08b6\u0003\u0186"+
		"\u00c3\u0000\u08b6\u0185\u0001\u0000\u0000\u0000\u08b7\u08bd\u0003\u0190"+
		"\u00c8\u0000\u08b8\u08bd\u0003\u0188\u00c4\u0000\u08b9\u08bd\u0003\u018a"+
		"\u00c5\u0000\u08ba\u08bd\u0003\u018c\u00c6\u0000\u08bb\u08bd\u0003\u018e"+
		"\u00c7\u0000\u08bc\u08b7\u0001\u0000\u0000\u0000\u08bc\u08b8\u0001\u0000"+
		"\u0000\u0000\u08bc\u08b9\u0001\u0000\u0000\u0000\u08bc\u08ba\u0001\u0000"+
		"\u0000\u0000\u08bc\u08bb\u0001\u0000\u0000\u0000\u08bd\u0187\u0001\u0000"+
		"\u0000\u0000\u08be\u08bf\u0003\u0190\u00c8\u0000\u08bf\u08c0\u0007\u0016"+
		"\u0000\u0000\u08c0\u08c1\u0003\u0190\u00c8\u0000\u08c1\u0189\u0001\u0000"+
		"\u0000\u0000\u08c2\u08c3\u0003\u0190\u00c8\u0000\u08c3\u08c4\u0007\u0017"+
		"\u0000\u0000\u08c4\u08c5\u0005\u001f\u0000\u0000\u08c5\u08ca\u0003\u01a4"+
		"\u00d2\u0000\u08c6\u08c7\u0005\t\u0000\u0000\u08c7\u08c9\u0003\u01a4\u00d2"+
		"\u0000\u08c8\u08c6\u0001\u0000\u0000\u0000\u08c9\u08cc\u0001\u0000\u0000"+
		"\u0000\u08ca\u08c8\u0001\u0000\u0000\u0000\u08ca\u08cb\u0001\u0000\u0000"+
		"\u0000\u08cb\u08cd\u0001\u0000\u0000\u0000\u08cc\u08ca\u0001\u0000\u0000"+
		"\u0000\u08cd\u08ce\u0005\b\u0000\u0000\u08ce\u018b\u0001\u0000\u0000\u0000"+
		"\u08cf\u08d0\u0003\u0190\u00c8\u0000\u08d0\u08d1\u0007\u0018\u0000\u0000"+
		"\u08d1\u08d2\u0005\u001f\u0000\u0000\u08d2\u08d3\u0003\u01a4\u00d2\u0000"+
		"\u08d3\u08d4\u0005\u0010\u0000\u0000\u08d4\u08d5\u0003\u01a4\u00d2\u0000"+
		"\u08d5\u08d6\u0005\b\u0000\u0000\u08d6\u018d\u0001\u0000\u0000\u0000\u08d7"+
		"\u08d8\u0005\u0001\u0000\u0000\u08d8\u08d9\u0005\u0012\u0000\u0000\u08d9"+
		"\u08da\u0003\u0190\u00c8\u0000\u08da\u018f\u0001\u0000\u0000\u0000\u08db"+
		"\u08de\u0003\u0192\u00c9\u0000\u08dc\u08dd\u0007\u0019\u0000\u0000\u08dd"+
		"\u08df\u0003\u0192\u00c9\u0000\u08de\u08dc\u0001\u0000\u0000\u0000\u08de"+
		"\u08df\u0001\u0000\u0000\u0000\u08df\u0191\u0001\u0000\u0000\u0000\u08e0"+
		"\u08e4\u0003\u0196\u00cb\u0000\u08e1\u08e3\u0003\u0194\u00ca\u0000\u08e2"+
		"\u08e1\u0001\u0000\u0000\u0000\u08e3\u08e6\u0001\u0000\u0000\u0000\u08e4"+
		"\u08e2\u0001\u0000\u0000\u0000\u08e4\u08e5\u0001\u0000\u0000\u0000\u08e5"+
		"\u0193\u0001\u0000\u0000\u0000\u08e6\u08e4\u0001\u0000\u0000\u0000\u08e7"+
		"\u08e8\u0007\u001a\u0000\u0000\u08e8\u08e9\u0003\u0196\u00cb\u0000\u08e9"+
		"\u0195\u0001\u0000\u0000\u0000\u08ea\u08ee\u0003\u019a\u00cd\u0000\u08eb"+
		"\u08ed\u0003\u0198\u00cc\u0000\u08ec\u08eb\u0001\u0000\u0000\u0000\u08ed"+
		"\u08f0\u0001\u0000\u0000\u0000\u08ee\u08ec\u0001\u0000\u0000\u0000\u08ee"+
		"\u08ef\u0001\u0000\u0000\u0000\u08ef\u0197\u0001\u0000\u0000\u0000\u08f0"+
		"\u08ee\u0001\u0000\u0000\u0000\u08f1\u08f2\u0007\u001b\u0000\u0000\u08f2"+
		"\u08f3\u0003\u019a\u00cd\u0000\u08f3\u0199\u0001\u0000\u0000\u0000\u08f4"+
		"\u08f7\u0003\u019c\u00ce\u0000\u08f5\u08f7\u0003\u01a2\u00d1\u0000\u08f6"+
		"\u08f4\u0001\u0000\u0000\u0000\u08f6\u08f5\u0001\u0000\u0000\u0000\u08f7"+
		"\u019b\u0001\u0000\u0000\u0000\u08f8\u08fc\u0003\u01a4\u00d2\u0000\u08f9"+
		"\u08fb\u0003\u019e\u00cf\u0000\u08fa\u08f9\u0001\u0000\u0000\u0000\u08fb"+
		"\u08fe\u0001\u0000\u0000\u0000\u08fc\u08fa\u0001\u0000\u0000\u0000\u08fc"+
		"\u08fd\u0001\u0000\u0000\u0000\u08fd\u019d\u0001\u0000\u0000\u0000\u08fe"+
		"\u08fc\u0001\u0000\u0000\u0000\u08ff\u0902\u0003\u01a0\u00d0\u0000\u0900"+
		"\u0902\u0005\n\u0000\u0000\u0901\u08ff\u0001\u0000\u0000\u0000\u0901\u0900"+
		"\u0001\u0000\u0000\u0000\u0902\u0903\u0001\u0000\u0000\u0000\u0903\u0904"+
		"\u0003\u01a4\u00d2\u0000\u0904\u019f\u0001\u0000\u0000\u0000\u0905\u0906"+
		"\u0007\u001c\u0000\u0000\u0906\u01a1\u0001\u0000\u0000\u0000\u0907\u0908"+
		"\u0005\u0001\u0000\u0000\u0908\u0909\u0003\u01a0\u00d0\u0000\u0909\u090a"+
		"\u0003\u01a4\u00d2\u0000\u090a\u01a3\u0001\u0000\u0000\u0000\u090b\u090d"+
		"\u0007\u001a\u0000\u0000\u090c\u090b\u0001\u0000\u0000\u0000\u090c\u090d"+
		"\u0001\u0000\u0000\u0000\u090d\u090e\u0001\u0000\u0000\u0000\u090e\u090f"+
		"\u0003\u01a6\u00d3\u0000\u090f\u01a5\u0001\u0000\u0000\u0000\u0910\u0914"+
		"\u0003\u01a8\u00d4\u0000\u0911\u0914\u0003\u01aa\u00d5\u0000\u0912\u0914"+
		"\u0003\u01b6\u00db\u0000\u0913\u0910\u0001\u0000\u0000\u0000\u0913\u0911"+
		"\u0001\u0000\u0000\u0000\u0913\u0912\u0001\u0000\u0000\u0000\u0914\u01a7"+
		"\u0001\u0000\u0000\u0000\u0915\u0919\u0003\u01ba\u00dd\u0000\u0916\u0919"+
		"\u0003\u01c8\u00e4\u0000\u0917\u0919\u0003\u01b4\u00da\u0000\u0918\u0915"+
		"\u0001\u0000\u0000\u0000\u0918\u0916\u0001\u0000\u0000\u0000\u0918\u0917"+
		"\u0001\u0000\u0000\u0000\u0919\u01a9\u0001\u0000\u0000\u0000\u091a\u091c"+
		"\u0003\u01a8\u00d4\u0000\u091b\u091d\u0003\u01ac\u00d6\u0000\u091c\u091b"+
		"\u0001\u0000\u0000\u0000\u091d\u091e\u0001\u0000\u0000\u0000\u091e\u091c"+
		"\u0001\u0000\u0000\u0000\u091e\u091f\u0001\u0000\u0000\u0000\u091f\u01ab"+
		"\u0001\u0000\u0000\u0000\u0920\u0924\u0003\u01ae\u00d7\u0000\u0921\u0924"+
		"\u0003\u01b0\u00d8\u0000\u0922\u0924\u0003\u01b2\u00d9\u0000\u0923\u0920"+
		"\u0001\u0000\u0000\u0000\u0923\u0921\u0001\u0000\u0000\u0000\u0923\u0922"+
		"\u0001\u0000\u0000\u0000\u0924\u01ad\u0001\u0000\u0000\u0000\u0925\u0926"+
		"\u0005\u000f\u0000\u0000\u0926\u0927\u0003\u021a\u010d\u0000\u0927\u01af"+
		"\u0001\u0000\u0000\u0000\u0928\u0929\u0005\u001e\u0000\u0000\u0929\u092a"+
		"\u0003\u017c\u00be\u0000\u092a\u092b\u0005\u0005\u0000\u0000\u092b\u01b1"+
		"\u0001\u0000\u0000\u0000\u092c\u092d\u0005\u000f\u0000\u0000\u092d\u092e"+
		"\u0005\u001e\u0000\u0000\u092e\u092f\u0003\u017c\u00be\u0000\u092f\u0930"+
		"\u0005\u0005\u0000\u0000\u0930\u01b3\u0001\u0000\u0000\u0000\u0931\u0933"+
		"\u0005\u00fa\u0000\u0000\u0932\u0934\u0003\u01b8\u00dc\u0000\u0933\u0932"+
		"\u0001\u0000\u0000\u0000\u0933\u0934\u0001\u0000\u0000\u0000\u0934\u0935"+
		"\u0001\u0000\u0000\u0000\u0935\u0936\u0005\u001f\u0000\u0000\u0936\u0937"+
		"\u0003L&\u0000\u0937\u0938\u0005\b\u0000\u0000\u0938\u01b5\u0001\u0000"+
		"\u0000\u0000\u0939\u093b\u0005\u00fb\u0000\u0000\u093a\u093c\u0003\u01b8"+
		"\u00dc\u0000\u093b\u093a\u0001\u0000\u0000\u0000\u093b\u093c\u0001\u0000"+
		"\u0000\u0000\u093c\u093d\u0001\u0000\u0000\u0000\u093d\u093e\u0005\u001f"+
		"\u0000\u0000\u093e\u093f\u0003L&\u0000\u093f\u0940\u0005\b\u0000\u0000"+
		"\u0940\u01b7\u0001\u0000\u0000\u0000\u0941\u0942\u0005\u0089\u0000\u0000"+
		"\u0942\u0943\u0005\u0011\u0000\u0000\u0943\u0944\u0005\u00a3\u0000\u0000"+
		"\u0944\u01b9\u0001\u0000\u0000\u0000\u0945\u0949\u0003\u01be\u00df\u0000"+
		"\u0946\u0948\u0003\u01bc\u00de\u0000\u0947\u0946\u0001\u0000\u0000\u0000"+
		"\u0948\u094b\u0001\u0000\u0000\u0000\u0949\u0947\u0001\u0000\u0000\u0000"+
		"\u0949\u094a\u0001\u0000\u0000\u0000\u094a\u01bb\u0001\u0000\u0000\u0000"+
		"\u094b\u0949\u0001\u0000\u0000\u0000\u094c\u094d\u0005\u000f\u0000\u0000"+
		"\u094d\u094e\u0003\u01be\u00df\u0000\u094e\u01bd\u0001\u0000\u0000\u0000"+
		"\u094f\u0952\u0003\u01c0\u00e0\u0000\u0950\u0952\u0003\u01c4\u00e2\u0000"+
		"\u0951\u094f\u0001\u0000\u0000\u0000\u0951\u0950\u0001\u0000\u0000\u0000"+
		"\u0952\u01bf\u0001\u0000\u0000\u0000\u0953\u0954\u0003\u0208\u0104\u0000"+
		"\u0954\u095d\u0005\u001f\u0000\u0000\u0955\u095a\u0003\u01c2\u00e1\u0000"+
		"\u0956\u0957\u0005\t\u0000\u0000\u0957\u0959\u0003\u01c2\u00e1\u0000\u0958"+
		"\u0956\u0001\u0000\u0000\u0000\u0959\u095c\u0001\u0000\u0000\u0000\u095a"+
		"\u0958\u0001\u0000\u0000\u0000\u095a\u095b\u0001\u0000\u0000\u0000\u095b"+
		"\u095e\u0001\u0000\u0000\u0000\u095c\u095a\u0001\u0000\u0000\u0000\u095d"+
		"\u0955\u0001\u0000\u0000\u0000\u095d\u095e\u0001\u0000\u0000\u0000\u095e"+
		"\u095f\u0001\u0000\u0000\u0000\u095f\u0960\u0005\b\u0000\u0000\u0960\u01c1"+
		"\u0001\u0000\u0000\u0000\u0961\u0964\u0003\u0174\u00ba\u0000\u0962\u0964"+
		"\u0003\u01c6\u00e3\u0000\u0963\u0961\u0001\u0000\u0000\u0000\u0963\u0962"+
		"\u0001\u0000\u0000\u0000\u0964\u01c3\u0001\u0000\u0000\u0000\u0965\u0966"+
		"\u0005B\u0000\u0000\u0966\u0968\u0005\u001f\u0000\u0000\u0967\u0969\u0003"+
		"\u0174\u00ba\u0000\u0968\u0967\u0001\u0000\u0000\u0000\u0968\u0969\u0001"+
		"\u0000\u0000\u0000\u0969\u096a\u0001\u0000\u0000\u0000\u096a\u096b\u0005"+
		"\b\u0000\u0000\u096b\u01c5\u0001\u0000\u0000\u0000\u096c\u096d\u0005\u0001"+
		"\u0000\u0000\u096d\u01c7\u0001\u0000\u0000\u0000\u096e\u0976\u0003\u0228"+
		"\u0114\u0000\u096f\u0976\u0003\u01ca\u00e5\u0000\u0970\u0976\u0003\u01ee"+
		"\u00f7\u0000\u0971\u0976\u0003\u01f4\u00fa\u0000\u0972\u0976\u0003\u01ec"+
		"\u00f6\u0000\u0973\u0976\u0003\u01fa\u00fd\u0000\u0974\u0976\u0003\u01ce"+
		"\u00e7\u0000\u0975\u096e\u0001\u0000\u0000\u0000\u0975\u096f\u0001\u0000"+
		"\u0000\u0000\u0975\u0970\u0001\u0000\u0000\u0000\u0975\u0971\u0001\u0000"+
		"\u0000\u0000\u0975\u0972\u0001\u0000\u0000\u0000\u0975\u0973\u0001\u0000"+
		"\u0000\u0000\u0975\u0974\u0001\u0000\u0000\u0000\u0976\u01c9\u0001\u0000"+
		"\u0000\u0000\u0977\u0979\u0003\u0208\u0104\u0000\u0978\u097a\u0003\u01cc"+
		"\u00e6\u0000\u0979\u0978\u0001\u0000\u0000\u0000\u0979\u097a\u0001\u0000"+
		"\u0000\u0000\u097a\u01cb\u0001\u0000\u0000\u0000\u097b\u097c\u0005F\u0000"+
		"\u0000\u097c\u097d\u0005\u0011\u0000\u0000\u097d\u097e\u0007\u001d\u0000"+
		"\u0000\u097e\u01cd\u0001\u0000\u0000\u0000\u097f\u0980\u0005\u001f\u0000"+
		"\u0000\u0980\u0981\u0003J%\u0000\u0981\u0982\u0005\b\u0000\u0000\u0982"+
		"\u01cf\u0001\u0000\u0000\u0000\u0983\u0984\u0005\u00d6\u0000\u0000\u0984"+
		"\u0985\u0003\u0208\u0104\u0000\u0985\u0986\u0005_\u0000\u0000\u0986\u0987"+
		"\u0003\u017c\u00be\u0000\u0987\u0988\u0005\u00f6\u0000\u0000\u0988\u0989"+
		"\u0003\u017c\u00be\u0000\u0989\u098a\u0005\u00ed\u0000\u0000\u098a\u098b"+
		"\u0003\u017c\u00be\u0000\u098b\u01d1\u0001\u0000\u0000\u0000\u098c\u098f"+
		"\u0003\u01e0\u00f0\u0000\u098d\u098f\u0003\u01d4\u00ea\u0000\u098e\u098c"+
		"\u0001\u0000\u0000\u0000\u098e\u098d\u0001\u0000\u0000\u0000\u098f\u01d3"+
		"\u0001\u0000\u0000\u0000\u0990\u0992\u0003\u01e0\u00f0\u0000\u0991\u0993"+
		"\u0003\u01d6\u00eb\u0000\u0992\u0991\u0001\u0000\u0000\u0000\u0993\u0994"+
		"\u0001\u0000\u0000\u0000\u0994\u0992\u0001\u0000\u0000\u0000\u0994\u0995"+
		"\u0001\u0000\u0000\u0000\u0995\u01d5\u0001\u0000\u0000\u0000\u0996\u099a"+
		"\u0003\u01d8\u00ec\u0000\u0997\u099a\u0003\u01da\u00ed\u0000\u0998\u099a"+
		"\u0003\u01dc\u00ee\u0000\u0999\u0996\u0001\u0000\u0000\u0000\u0999\u0997"+
		"\u0001\u0000\u0000\u0000\u0999\u0998\u0001\u0000\u0000\u0000\u099a\u01d7"+
		"\u0001\u0000\u0000\u0000\u099b\u099c\u0005\u000f\u0000\u0000\u099c\u099d"+
		"\u0003\u01de\u00ef\u0000\u099d\u01d9\u0001\u0000\u0000\u0000\u099e\u099f"+
		"\u0005\u001e\u0000\u0000\u099f\u09a0\u0003\u017c\u00be\u0000\u09a0\u09a1"+
		"\u0005\u0005\u0000\u0000\u09a1\u01db\u0001\u0000\u0000\u0000\u09a2\u09a3"+
		"\u0005\u000f\u0000\u0000\u09a3\u09a4\u0005\u001e\u0000\u0000\u09a4\u09a5"+
		"\u0003\u017c\u00be\u0000\u09a5\u09a6\u0005\u0005\u0000\u0000\u09a6\u01dd"+
		"\u0001\u0000\u0000\u0000\u09a7\u09ab\u0003\u01e2\u00f1\u0000\u09a8\u09ab"+
		"\u0003\u021c\u010e\u0000\u09a9\u09ab\u0003\u01e4\u00f2\u0000\u09aa\u09a7"+
		"\u0001\u0000";
	private static final String _serializedATNSegment1 =
		"\u0000\u0000\u09aa\u09a8\u0001\u0000\u0000\u0000\u09aa\u09a9\u0001\u0000"+
		"\u0000\u0000\u09ab\u01df\u0001\u0000\u0000\u0000\u09ac\u09ad\u0003\u01de"+
		"\u00ef\u0000\u09ad\u01e1\u0001\u0000\u0000\u0000\u09ae\u09af\u0005\u0002"+
		"\u0000\u0000\u09af\u01e3\u0001\u0000\u0000\u0000\u09b0\u09b1\u0007\u001e"+
		"\u0000\u0000\u09b1\u01e5\u0001\u0000\u0000\u0000\u09b2\u09b6\u0003\u020c"+
		"\u0106\u0000\u09b3\u09b6\u0003\u01ba\u00dd\u0000\u09b4\u09b6\u0003\u01e8"+
		"\u00f4\u0000\u09b5\u09b2\u0001\u0000\u0000\u0000\u09b5\u09b3\u0001\u0000"+
		"\u0000\u0000\u09b5\u09b4\u0001\u0000\u0000\u0000\u09b6\u01e7\u0001\u0000"+
		"\u0000\u0000\u09b7\u09b8\u0003\u01ba\u00dd\u0000\u09b8\u09b9\u0005\u000f"+
		"\u0000\u0000\u09b9\u09ba\u0003\u01ea\u00f5\u0000\u09ba\u01e9\u0001\u0000"+
		"\u0000\u0000\u09bb\u09be\u0003\u0220\u0110\u0000\u09bc\u09be\u0003\u01de"+
		"\u00ef\u0000\u09bd\u09bb\u0001\u0000\u0000\u0000\u09bd\u09bc\u0001\u0000"+
		"\u0000\u0000\u09be\u01eb\u0001\u0000\u0000\u0000\u09bf\u09c0\u0005A\u0000"+
		"\u0000\u09c0\u09c1\u0005\u013b\u0000\u0000\u09c1\u09c2\u0003\u01f0\u00f8"+
		"\u0000\u09c2\u01ed\u0001\u0000\u0000\u0000\u09c3\u09c7\u0005G\u0000\u0000"+
		"\u09c4\u09c6\u0003\u0170\u00b8\u0000\u09c5\u09c4\u0001\u0000\u0000\u0000"+
		"\u09c6\u09c9\u0001\u0000\u0000\u0000\u09c7\u09c5\u0001\u0000\u0000\u0000"+
		"\u09c7\u09c8\u0001\u0000\u0000\u0000\u09c8\u09ca\u0001\u0000\u0000\u0000"+
		"\u09c9\u09c7\u0001\u0000\u0000\u0000\u09ca\u09cb\u0003\u01f0\u00f8\u0000"+
		"\u09cb\u09cd\u0005\u001e\u0000\u0000\u09cc\u09ce\u0003\u0226\u0113\u0000"+
		"\u09cd\u09cc\u0001\u0000\u0000\u0000\u09cd\u09ce\u0001\u0000\u0000\u0000"+
		"\u09ce\u09d3\u0001\u0000\u0000\u0000\u09cf\u09d0\u0005\t\u0000\u0000\u09d0"+
		"\u09d2\u0003\u0226\u0113\u0000\u09d1\u09cf\u0001\u0000\u0000\u0000\u09d2"+
		"\u09d5\u0001\u0000\u0000\u0000\u09d3\u09d1\u0001\u0000\u0000\u0000\u09d3"+
		"\u09d4\u0001\u0000\u0000\u0000\u09d4\u09d7\u0001\u0000\u0000\u0000\u09d5"+
		"\u09d3\u0001\u0000\u0000\u0000\u09d6\u09d8\u0005\t\u0000\u0000\u09d7\u09d6"+
		"\u0001\u0000\u0000\u0000\u09d7\u09d8\u0001\u0000\u0000\u0000\u09d8\u09d9"+
		"\u0001\u0000\u0000\u0000\u09d9\u09da\u0005\u0005\u0000\u0000\u09da\u01ef"+
		"\u0001\u0000\u0000\u0000\u09db\u09dd\u0005\u001f\u0000\u0000\u09dc\u09de"+
		"\u0003\u01f2\u00f9\u0000\u09dd\u09dc\u0001\u0000\u0000\u0000\u09dd\u09de"+
		"\u0001\u0000\u0000\u0000\u09de\u09e3\u0001\u0000\u0000\u0000\u09df\u09e0"+
		"\u0005\t\u0000\u0000\u09e0\u09e2\u0003\u01f2\u00f9\u0000\u09e1\u09df\u0001"+
		"\u0000\u0000\u0000\u09e2\u09e5\u0001\u0000\u0000\u0000\u09e3\u09e1\u0001"+
		"\u0000\u0000\u0000\u09e3\u09e4\u0001\u0000\u0000\u0000\u09e4\u09e7\u0001"+
		"\u0000\u0000\u0000\u09e5\u09e3\u0001\u0000\u0000\u0000\u09e6\u09e8\u0005"+
		"\t\u0000\u0000\u09e7\u09e6\u0001\u0000\u0000\u0000\u09e7\u09e8\u0001\u0000"+
		"\u0000\u0000\u09e8\u09e9\u0001\u0000\u0000\u0000\u09e9\u09ea\u0005\b\u0000"+
		"\u0000\u09ea\u01f1\u0001\u0000\u0000\u0000\u09eb\u09ec\u0003\u0206\u0103"+
		"\u0000\u09ec\u09ed\u0005\n\u0000\u0000\u09ed\u09ee\u0003\u0202\u0101\u0000"+
		"\u09ee\u01f3\u0001\u0000\u0000\u0000\u09ef\u09f3\u0007\u001f\u0000\u0000"+
		"\u09f0\u09f2\u0003\u0170\u00b8\u0000\u09f1\u09f0\u0001\u0000\u0000\u0000"+
		"\u09f2\u09f5\u0001\u0000\u0000\u0000\u09f3\u09f1\u0001\u0000\u0000\u0000"+
		"\u09f3\u09f4\u0001\u0000\u0000\u0000\u09f4\u09f6\u0001\u0000\u0000\u0000"+
		"\u09f5\u09f3\u0001\u0000\u0000\u0000\u09f6\u09f7\u0003\u01f0\u00f8\u0000"+
		"\u09f7\u09f8\u0005\u001e\u0000\u0000\u09f8\u09fd\u0003\u0246\u0123\u0000"+
		"\u09f9\u09fa\u0005\t\u0000\u0000\u09fa\u09fc\u0003\u0246\u0123\u0000\u09fb"+
		"\u09f9\u0001\u0000\u0000\u0000\u09fc\u09ff\u0001\u0000\u0000\u0000\u09fd"+
		"\u09fb\u0001\u0000\u0000\u0000\u09fd\u09fe\u0001\u0000\u0000\u0000\u09fe"+
		"\u0a00\u0001\u0000\u0000\u0000\u09ff\u09fd\u0001\u0000\u0000\u0000\u0a00"+
		"\u0a02\u0005\u0005\u0000\u0000\u0a01\u0a03\u0003\u01f6\u00fb\u0000\u0a02"+
		"\u0a01\u0001\u0000\u0000\u0000\u0a02\u0a03\u0001\u0000\u0000\u0000\u0a03"+
		"\u01f5\u0001\u0000\u0000\u0000\u0a04\u0a05\u0005\u0104\u0000\u0000\u0a05"+
		"\u0a11\u0005\u001f\u0000\u0000\u0a06\u0a0b\u0003\u01f8\u00fc\u0000\u0a07"+
		"\u0a08\u0005\t\u0000\u0000\u0a08\u0a0a\u0003\u01f8\u00fc\u0000\u0a09\u0a07"+
		"\u0001\u0000\u0000\u0000\u0a0a\u0a0d\u0001\u0000\u0000\u0000\u0a0b\u0a09"+
		"\u0001\u0000\u0000\u0000\u0a0b\u0a0c\u0001\u0000\u0000\u0000\u0a0c\u0a0f"+
		"\u0001\u0000\u0000\u0000\u0a0d\u0a0b\u0001\u0000\u0000\u0000\u0a0e\u0a10"+
		"\u0005\t\u0000\u0000\u0a0f\u0a0e\u0001\u0000\u0000\u0000\u0a0f\u0a10\u0001"+
		"\u0000\u0000\u0000\u0a10\u0a12\u0001\u0000\u0000\u0000\u0a11\u0a06\u0001"+
		"\u0000\u0000\u0000\u0a11\u0a12\u0001\u0000\u0000\u0000\u0a12\u0a13\u0001"+
		"\u0000\u0000\u0000\u0a13\u0a14\u0005\b\u0000\u0000\u0a14\u01f7\u0001\u0000"+
		"\u0000\u0000\u0a15\u0a16\u0003\u0206\u0103\u0000\u0a16\u0a1a\u0005\u0011"+
		"\u0000\u0000\u0a17\u0a1b\u0003\u0246\u0123\u0000\u0a18\u0a1b\u0007 \u0000"+
		"\u0000\u0a19\u0a1b\u0003\u0206\u0103\u0000\u0a1a\u0a17\u0001\u0000\u0000"+
		"\u0000\u0a1a\u0a18\u0001\u0000\u0000\u0000\u0a1a\u0a19\u0001\u0000\u0000"+
		"\u0000\u0a1b\u01f9\u0001\u0000\u0000\u0000\u0a1c\u0a1d\u0005\u009c\u0000"+
		"\u0000\u0a1d\u0a1e\u0005\u001f\u0000\u0000\u0a1e\u0a1f\u0003\u0246\u0123"+
		"\u0000\u0a1f\u0a20\u0005\b\u0000\u0000\u0a20\u0a21\u0003\u01fc\u00fe\u0000"+
		"\u0a21\u0a22\u0003\u01fe\u00ff\u0000\u0a22\u0a23\u0003\u0200\u0100\u0000"+
		"\u0a23\u01fb\u0001\u0000\u0000\u0000\u0a24\u0a25\u00055\u0000\u0000\u0a25"+
		"\u0a26\u0005\u001f\u0000\u0000\u0a26\u0a27\u0003J%\u0000\u0a27\u0a28\u0005"+
		"\b\u0000\u0000\u0a28\u01fd\u0001\u0000\u0000\u0000\u0a29\u0a2a\u0005K"+
		"\u0000\u0000\u0a2a\u0a2b\u0005\u001f\u0000\u0000\u0a2b\u0a2c\u0003J%\u0000"+
		"\u0a2c\u0a2d\u0005\b\u0000\u0000\u0a2d\u01ff\u0001\u0000\u0000\u0000\u0a2e"+
		"\u0a2f\u0005(\u0000\u0000\u0a2f\u0a30\u0005\u001f\u0000\u0000\u0a30\u0a31"+
		"\u0003\u014e\u00a7\u0000\u0a31\u0a32\u0005\b\u0000\u0000\u0a32\u0201\u0001"+
		"\u0000\u0000\u0000\u0a33\u0a34\u0007!\u0000\u0000\u0a34\u0203\u0001\u0000"+
		"\u0000\u0000\u0a35\u0a36\u0007\"\u0000\u0000\u0a36\u0205\u0001\u0000\u0000"+
		"\u0000\u0a37\u0a38\u0003\u021c\u010e\u0000\u0a38\u0207\u0001\u0000\u0000"+
		"\u0000\u0a39\u0a3a\u0003\u021a\u010d\u0000\u0a3a\u0209\u0001\u0000\u0000"+
		"\u0000\u0a3b\u0a3c\u0003\u021c\u010e\u0000\u0a3c\u020b\u0001\u0000\u0000"+
		"\u0000\u0a3d\u0a3e\u0003\u0220\u0110\u0000\u0a3e\u020d\u0001\u0000\u0000"+
		"\u0000\u0a3f\u0a42\u0003\u0208\u0104\u0000\u0a40\u0a42\u0003\u020c\u0106"+
		"\u0000\u0a41\u0a3f\u0001\u0000\u0000\u0000\u0a41\u0a40\u0001\u0000\u0000"+
		"\u0000\u0a42\u020f\u0001\u0000\u0000\u0000\u0a43\u0a44\u0005\u013c\u0000"+
		"\u0000\u0a44\u0211\u0001\u0000\u0000\u0000\u0a45\u0a46\u0007#\u0000\u0000"+
		"\u0a46\u0213\u0001\u0000\u0000\u0000\u0a47\u0a48\u0007$\u0000\u0000\u0a48"+
		"\u0215\u0001\u0000\u0000\u0000\u0a49\u0a4a\u0005\u001e\u0000\u0000\u0a4a"+
		"\u0a4b\u0003\u0246\u0123\u0000\u0a4b\u0a4c\u0005\u0005\u0000\u0000\u0a4c"+
		"\u0217\u0001\u0000\u0000\u0000\u0a4d\u0a50\u0003\u0210\u0108\u0000\u0a4e"+
		"\u0a50\u0003\u0212\u0109\u0000\u0a4f\u0a4d\u0001\u0000\u0000\u0000\u0a4f"+
		"\u0a4e\u0001\u0000\u0000\u0000\u0a50\u0219\u0001\u0000\u0000\u0000\u0a51"+
		"\u0a55\u0003\u0210\u0108\u0000\u0a52\u0a55\u0003\u0212\u0109\u0000\u0a53"+
		"\u0a55\u0003\u0216\u010b\u0000\u0a54\u0a51\u0001\u0000\u0000\u0000\u0a54"+
		"\u0a52\u0001\u0000\u0000\u0000\u0a54\u0a53\u0001\u0000\u0000\u0000\u0a55"+
		"\u021b\u0001\u0000\u0000\u0000\u0a56\u0a5b\u0003\u0210\u0108\u0000\u0a57"+
		"\u0a5b\u0003\u0212\u0109\u0000\u0a58\u0a5b\u0003\u0214\u010a\u0000\u0a59"+
		"\u0a5b\u0003\u0216\u010b\u0000\u0a5a\u0a56\u0001\u0000\u0000\u0000\u0a5a"+
		"\u0a57\u0001\u0000\u0000\u0000\u0a5a\u0a58\u0001\u0000\u0000\u0000\u0a5a"+
		"\u0a59\u0001\u0000\u0000\u0000\u0a5b\u021d\u0001\u0000\u0000\u0000\u0a5c"+
		"\u0a60\u0003\u0210\u0108\u0000\u0a5d\u0a60\u0003\u0212\u0109\u0000\u0a5e"+
		"\u0a60\u0003\u0214\u010a\u0000\u0a5f\u0a5c\u0001\u0000\u0000\u0000\u0a5f"+
		"\u0a5d\u0001\u0000\u0000\u0000\u0a5f\u0a5e\u0001\u0000\u0000\u0000\u0a60"+
		"\u021f\u0001\u0000\u0000\u0000\u0a61\u0a63\u0003\u0222\u0111\u0000\u0a62"+
		"\u0a61\u0001\u0000\u0000\u0000\u0a62\u0a63\u0001\u0000\u0000\u0000\u0a63"+
		"\u0a64\u0001\u0000\u0000\u0000\u0a64\u0a68\u0005\u0001\u0000\u0000\u0a65"+
		"\u0a67\u0003\u0224\u0112\u0000\u0a66\u0a65\u0001\u0000\u0000\u0000\u0a67"+
		"\u0a6a\u0001\u0000\u0000\u0000\u0a68\u0a66\u0001\u0000\u0000\u0000\u0a68"+
		"\u0a69\u0001\u0000\u0000\u0000\u0a69\u0221\u0001\u0000\u0000\u0000\u0a6a"+
		"\u0a68\u0001\u0000\u0000\u0000\u0a6b\u0a6f\u0005\u013c\u0000\u0000\u0a6c"+
		"\u0a6f\u0003\u0212\u0109\u0000\u0a6d\u0a6f\u0003\u0214\u010a\u0000\u0a6e"+
		"\u0a6b\u0001\u0000\u0000\u0000\u0a6e\u0a6c\u0001\u0000\u0000\u0000\u0a6e"+
		"\u0a6d\u0001\u0000\u0000\u0000\u0a6f\u0223\u0001\u0000\u0000\u0000\u0a70"+
		"\u0a76\u0005\u013c\u0000\u0000\u0a71\u0a76\u0003\u0212\u0109\u0000\u0a72"+
		"\u0a76\u0003\u0214\u010a\u0000\u0a73\u0a76\u0005\u0131\u0000\u0000\u0a74"+
		"\u0a76\u0005\u0001\u0000\u0000\u0a75\u0a70\u0001\u0000\u0000\u0000\u0a75"+
		"\u0a71\u0001\u0000\u0000\u0000\u0a75\u0a72\u0001\u0000\u0000\u0000\u0a75"+
		"\u0a73\u0001\u0000\u0000\u0000\u0a75\u0a74\u0001\u0000\u0000\u0000\u0a76"+
		"\u0225\u0001\u0000\u0000\u0000\u0a77\u0a7a\u0003\u022e\u0117\u0000\u0a78"+
		"\u0a7a\u0003\u0228\u0114\u0000\u0a79\u0a77\u0001\u0000\u0000\u0000\u0a79"+
		"\u0a78\u0001\u0000\u0000\u0000\u0a7a\u0227\u0001\u0000\u0000\u0000\u0a7b"+
		"\u0a87\u0003\u0230\u0118\u0000\u0a7c\u0a87\u0003\u0232\u0119\u0000\u0a7d"+
		"\u0a87\u0003\u0234\u011a\u0000\u0a7e\u0a87\u0003\u0236\u011b\u0000\u0a7f"+
		"\u0a87\u0003\u0238\u011c\u0000\u0a80\u0a87\u0003\u023a\u011d\u0000\u0a81"+
		"\u0a87\u0003\u023c\u011e\u0000\u0a82\u0a87\u0003\u023e\u011f\u0000\u0a83"+
		"\u0a87\u0003\u0240\u0120\u0000\u0a84\u0a87\u0003\u0246\u0123\u0000\u0a85"+
		"\u0a87\u0003\u0248\u0124\u0000\u0a86\u0a7b\u0001\u0000\u0000\u0000\u0a86"+
		"\u0a7c\u0001\u0000\u0000\u0000\u0a86\u0a7d\u0001\u0000\u0000\u0000\u0a86"+
		"\u0a7e\u0001\u0000\u0000\u0000\u0a86\u0a7f\u0001\u0000\u0000\u0000\u0a86"+
		"\u0a80\u0001\u0000\u0000\u0000\u0a86\u0a81\u0001\u0000\u0000\u0000\u0a86"+
		"\u0a82\u0001\u0000\u0000\u0000\u0a86\u0a83\u0001\u0000\u0000\u0000\u0a86"+
		"\u0a84\u0001\u0000\u0000\u0000\u0a86\u0a85\u0001\u0000\u0000\u0000\u0a87"+
		"\u0229\u0001\u0000\u0000\u0000\u0a88\u0a90\u0003\u0230\u0118\u0000\u0a89"+
		"\u0a90\u0003\u0232\u0119\u0000\u0a8a\u0a90\u0003\u0234\u011a\u0000\u0a8b"+
		"\u0a90\u0003\u0236\u011b\u0000\u0a8c\u0a90\u0003\u022e\u0117\u0000\u0a8d"+
		"\u0a90\u0003\u0238\u011c\u0000\u0a8e\u0a90\u0003\u023a\u011d\u0000\u0a8f"+
		"\u0a88\u0001\u0000\u0000\u0000\u0a8f\u0a89\u0001\u0000\u0000\u0000\u0a8f"+
		"\u0a8a\u0001\u0000\u0000\u0000\u0a8f\u0a8b\u0001\u0000\u0000\u0000\u0a8f"+
		"\u0a8c\u0001\u0000\u0000\u0000\u0a8f\u0a8d\u0001\u0000\u0000\u0000\u0a8f"+
		"\u0a8e\u0001\u0000\u0000\u0000\u0a90\u022b\u0001\u0000\u0000\u0000\u0a91"+
		"\u0a97\u0003\u0230\u0118\u0000\u0a92\u0a97\u0003\u0232\u0119\u0000\u0a93"+
		"\u0a97\u0003\u0234\u011a\u0000\u0a94\u0a97\u0003\u0236\u011b\u0000\u0a95"+
		"\u0a97\u0003\u022e\u0117\u0000\u0a96\u0a91\u0001\u0000\u0000\u0000\u0a96"+
		"\u0a92\u0001\u0000\u0000\u0000\u0a96\u0a93\u0001\u0000\u0000\u0000\u0a96"+
		"\u0a94\u0001\u0000\u0000\u0000\u0a96\u0a95\u0001\u0000\u0000\u0000\u0a97"+
		"\u022d\u0001\u0000\u0000\u0000\u0a98\u0a9b\u0003\u0242\u0121\u0000\u0a99"+
		"\u0a9b\u0003\u0244\u0122\u0000\u0a9a\u0a98\u0001\u0000\u0000\u0000\u0a9a"+
		"\u0a99\u0001\u0000\u0000\u0000\u0a9b\u022f\u0001\u0000\u0000\u0000\u0a9c"+
		"\u0a9d\u0005\u0131\u0000\u0000\u0a9d\u0231\u0001\u0000\u0000\u0000\u0a9e"+
		"\u0a9f\u0005\u0132\u0000\u0000\u0a9f\u0233\u0001\u0000\u0000\u0000\u0aa0"+
		"\u0aa1\u0005\u0133\u0000\u0000\u0aa1\u0235\u0001\u0000\u0000\u0000\u0aa2"+
		"\u0aa3\u0005\u0134\u0000\u0000\u0aa3\u0237\u0001\u0000\u0000\u0000\u0aa4"+
		"\u0aa5\u0005\u0137\u0000\u0000\u0aa5\u0239\u0001\u0000\u0000\u0000\u0aa6"+
		"\u0aa7\u0005\u0138\u0000\u0000\u0aa7\u023b\u0001\u0000\u0000\u0000\u0aa8"+
		"\u0aa9\u0005\u0136\u0000\u0000\u0aa9\u023d\u0001\u0000\u0000\u0000\u0aaa"+
		"\u0aab\u0005\u013b\u0000\u0000\u0aab\u023f\u0001\u0000\u0000\u0000\u0aac"+
		"\u0aad\u0005\u0139\u0000\u0000\u0aad\u0241\u0001\u0000\u0000\u0000\u0aae"+
		"\u0aaf\u0007\u001a\u0000\u0000\u0aaf\u0ab0\u0005\u0131\u0000\u0000\u0ab0"+
		"\u0243\u0001\u0000\u0000\u0000\u0ab1\u0ab2\u0007\u001a\u0000\u0000\u0ab2"+
		"\u0ab3\u0005\u0133\u0000\u0000\u0ab3\u0245\u0001\u0000\u0000\u0000\u0ab4"+
		"\u0ab8\u0005\u0135\u0000\u0000\u0ab5\u0ab7\u0005\u0135\u0000\u0000\u0ab6"+
		"\u0ab5\u0001\u0000\u0000\u0000\u0ab7\u0aba\u0001\u0000\u0000\u0000\u0ab8"+
		"\u0ab6\u0001\u0000\u0000\u0000\u0ab8\u0ab9\u0001\u0000\u0000\u0000\u0ab9"+
		"\u0247\u0001\u0000\u0000\u0000\u0aba\u0ab8\u0001\u0000\u0000\u0000\u0abb"+
		"\u0abc\u0005\u011d\u0000\u0000\u0abc\u0abd\u0005\u001f\u0000\u0000\u0abd"+
		"\u0abe\u0003\u024a\u0125\u0000\u0abe\u0abf\u0005\b\u0000\u0000\u0abf\u0249"+
		"\u0001\u0000\u0000\u0000\u0ac0\u0acc\u0003\u0250\u0128\u0000\u0ac1\u0acc"+
		"\u0003\u0252\u0129\u0000\u0ac2\u0acc\u0003\u0254\u012a\u0000\u0ac3\u0acc"+
		"\u0003\u0256\u012b\u0000\u0ac4\u0acc\u0003\u025e\u012f\u0000\u0ac5\u0acc"+
		"\u0003\u0258\u012c\u0000\u0ac6\u0acc\u0003\u024c\u0126\u0000\u0ac7\u0acc"+
		"\u0003\u0260\u0130\u0000\u0ac8\u0acc\u0003\u025a\u012d\u0000\u0ac9\u0acc"+
		"\u0003\u025c\u012e\u0000\u0aca\u0acc\u0003\u0248\u0124\u0000\u0acb\u0ac0"+
		"\u0001\u0000\u0000\u0000\u0acb\u0ac1\u0001\u0000\u0000\u0000\u0acb\u0ac2"+
		"\u0001\u0000\u0000\u0000\u0acb\u0ac3\u0001\u0000\u0000\u0000\u0acb\u0ac4"+
		"\u0001\u0000\u0000\u0000\u0acb\u0ac5\u0001\u0000\u0000\u0000\u0acb\u0ac6"+
		"\u0001\u0000\u0000\u0000\u0acb\u0ac7\u0001\u0000\u0000\u0000\u0acb\u0ac8"+
		"\u0001\u0000\u0000\u0000\u0acb\u0ac9\u0001\u0000\u0000\u0000\u0acb\u0aca"+
		"\u0001\u0000\u0000\u0000\u0acc\u024b\u0001\u0000\u0000\u0000\u0acd\u0ad6"+
		"\u0005\u001d\u0000\u0000\u0ace\u0ad3\u0003\u024e\u0127\u0000\u0acf\u0ad0"+
		"\u0005\t\u0000\u0000\u0ad0\u0ad2\u0003\u024e\u0127\u0000\u0ad1\u0acf\u0001"+
		"\u0000\u0000\u0000\u0ad2\u0ad5\u0001\u0000\u0000\u0000\u0ad3\u0ad1\u0001"+
		"\u0000\u0000\u0000\u0ad3\u0ad4\u0001\u0000\u0000\u0000\u0ad4\u0ad7\u0001"+
		"\u0000\u0000\u0000\u0ad5\u0ad3\u0001\u0000\u0000\u0000\u0ad6\u0ace\u0001"+
		"\u0000\u0000\u0000\u0ad6\u0ad7\u0001\u0000\u0000\u0000\u0ad7\u0ad8\u0001"+
		"\u0000\u0000\u0000\u0ad8\u0ad9\u0005\u0004\u0000\u0000\u0ad9\u024d\u0001"+
		"\u0000\u0000\u0000\u0ada\u0adb\u0005\u0135\u0000\u0000\u0adb\u0adc\u0005"+
		"\n\u0000\u0000\u0adc\u0add\u0003\u024a\u0125\u0000\u0add\u024f\u0001\u0000"+
		"\u0000\u0000\u0ade\u0ae7\u0005\u001e\u0000\u0000\u0adf\u0ae4\u0003\u024a"+
		"\u0125\u0000\u0ae0\u0ae1\u0005\t\u0000\u0000\u0ae1\u0ae3\u0003\u024a\u0125"+
		"\u0000\u0ae2\u0ae0\u0001\u0000\u0000\u0000\u0ae3\u0ae6\u0001\u0000\u0000"+
		"\u0000\u0ae4\u0ae2\u0001\u0000\u0000\u0000\u0ae4\u0ae5\u0001\u0000\u0000"+
		"\u0000\u0ae5\u0ae8\u0001\u0000\u0000\u0000\u0ae6\u0ae4\u0001\u0000\u0000"+
		"\u0000\u0ae7\u0adf\u0001\u0000\u0000\u0000\u0ae7\u0ae8\u0001\u0000\u0000"+
		"\u0000\u0ae8\u0ae9\u0001\u0000\u0000\u0000\u0ae9\u0aea\u0005\u0005\u0000"+
		"\u0000\u0aea\u0251\u0001\u0000\u0000\u0000\u0aeb\u0aec\u0005\u0136\u0000"+
		"\u0000\u0aec\u0253\u0001\u0000\u0000\u0000\u0aed\u0aee\u0005\u0137\u0000"+
		"\u0000\u0aee\u0255\u0001\u0000\u0000\u0000\u0aef\u0af0\u0005\u013b\u0000"+
		"\u0000\u0af0\u0257\u0001\u0000\u0000\u0000\u0af1\u0af2\u0005\u00b7\u0000"+
		"\u0000\u0af2\u0259\u0001\u0000\u0000\u0000\u0af3\u0af7\u0005\u0135\u0000"+
		"\u0000\u0af4\u0af6\u0005\u0135\u0000\u0000\u0af5\u0af4\u0001\u0000\u0000"+
		"\u0000\u0af6\u0af9\u0001\u0000\u0000\u0000\u0af7\u0af5\u0001\u0000\u0000"+
		"\u0000\u0af7\u0af8\u0001\u0000\u0000\u0000\u0af8\u025b\u0001\u0000\u0000"+
		"\u0000\u0af9\u0af7\u0001\u0000\u0000\u0000\u0afa\u0afb\u0005\u0138\u0000"+
		"\u0000\u0afb\u025d\u0001\u0000\u0000\u0000\u0afc\u0afe\u0005\u000b\u0000"+
		"\u0000\u0afd\u0afc\u0001\u0000\u0000\u0000\u0afd\u0afe\u0001\u0000\u0000"+
		"\u0000\u0afe\u0aff\u0001\u0000\u0000\u0000\u0aff\u0b00\u0005\u0131\u0000"+
		"\u0000\u0b00\u025f\u0001\u0000\u0000\u0000\u0b01\u0b03\u0005\u000b\u0000"+
		"\u0000\u0b02\u0b01\u0001\u0000\u0000\u0000\u0b02\u0b03\u0001\u0000\u0000"+
		"\u0000\u0b03\u0b04\u0001\u0000\u0000\u0000\u0b04\u0b05\u0005\u0133\u0000"+
		"\u0000\u0b05\u0261\u0001\u0000\u0000\u0000\u0103\u0269\u026d\u0278\u0285"+
		"\u0291\u029c\u02a6\u02c1\u02c7\u02d0\u02dc\u02eb\u02ef\u02f2\u02f8\u02fe"+
		"\u0303\u0309\u0313\u0322\u0327\u032f\u0341\u0350\u0357\u035d\u0361\u036b"+
		"\u0374\u037e\u0388\u0391\u03c4\u03ca\u03e5\u03eb\u03f7\u03fe\u0408\u040d"+
		"\u0416\u041d\u0422\u042d\u0439\u043e\u044a\u044d\u0452\u0455\u045a\u045e"+
		"\u0469\u0474\u0479\u047d\u048c\u0495\u049a\u04a1\u04a8\u04ab\u04b8\u04c4"+
		"\u04cb\u04d3\u04d6\u04db\u04e6\u04f8\u04fe\u0507\u050c\u0516\u051e\u0521"+
		"\u052a\u0530\u0538\u053b\u0544\u054e\u055a\u055e\u0565\u056e\u0577\u057f"+
		"\u0582\u0597\u059f\u05a5\u05a8\u05af\u05c1\u05c5\u05d0\u05d7\u05df\u05e3"+
		"\u05e6\u05f5\u05fe\u0606\u060a\u060e\u0612\u061c\u0625\u0628\u062d\u0631"+
		"\u0634\u0638\u063c\u0646\u064f\u0658\u065e\u0662\u0667\u0675\u067a\u0689"+
		"\u0692\u0695\u069d\u06a6\u06a9\u06b1\u06b4\u06bc\u06bf\u06c3\u06c9\u06cf"+
		"\u06d7\u06de\u06e7\u06ea\u06f1\u0726\u072d\u073d\u0743\u074e\u0757\u075b"+
		"\u075e\u0761\u0768\u0779\u0783\u078b\u078e\u0793\u07a1\u07ac\u07b0\u07b3"+
		"\u07b8\u07c5\u07ce\u07d6\u07dd\u07e6\u07ed\u07f1\u07f7\u07ff\u0802\u0805"+
		"\u080d\u0817\u0820\u082c\u0836\u083b\u0840\u084e\u0856\u085c\u0862\u0869"+
		"\u086f\u0879\u087f\u0885\u0888\u088e\u0898\u08a7\u08b1\u08bc\u08ca\u08de"+
		"\u08e4\u08ee\u08f6\u08fc\u0901\u090c\u0913\u0918\u091e\u0923\u0933\u093b"+
		"\u0949\u0951\u095a\u095d\u0963\u0968\u0975\u0979\u098e\u0994\u0999\u09aa"+
		"\u09b5\u09bd\u09c7\u09cd\u09d3\u09d7\u09dd\u09e3\u09e7\u09f3\u09fd\u0a02"+
		"\u0a0b\u0a0f\u0a11\u0a1a\u0a41\u0a4f\u0a54\u0a5a\u0a5f\u0a62\u0a68\u0a6e"+
		"\u0a75\u0a79\u0a86\u0a8f\u0a96\u0a9a\u0ab8\u0acb\u0ad3\u0ad6\u0ae4\u0ae7"+
		"\u0af7\u0afd\u0b02";
	public static final String _serializedATN = Utils.join(
		new String[] {
			_serializedATNSegment0,
			_serializedATNSegment1
		},
		""
	);
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}