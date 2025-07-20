// Generated from Hac.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link HacParser}.
 */
public interface HacListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link HacParser#dacBlock}.
	 * @param ctx the parse tree
	 */
	void enterDacBlock(HacParser.DacBlockContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#dacBlock}.
	 * @param ctx the parse tree
	 */
	void exitDacBlock(HacParser.DacBlockContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#tagSection}.
	 * @param ctx the parse tree
	 */
	void enterTagSection(HacParser.TagSectionContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#tagSection}.
	 * @param ctx the parse tree
	 */
	void exitTagSection(HacParser.TagSectionContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#emptyLine}.
	 * @param ctx the parse tree
	 */
	void enterEmptyLine(HacParser.EmptyLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#emptyLine}.
	 * @param ctx the parse tree
	 */
	void exitEmptyLine(HacParser.EmptyLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#listStart}.
	 * @param ctx the parse tree
	 */
	void enterListStart(HacParser.ListStartContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#listStart}.
	 * @param ctx the parse tree
	 */
	void exitListStart(HacParser.ListStartContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#listLine}.
	 * @param ctx the parse tree
	 */
	void enterListLine(HacParser.ListLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#listLine}.
	 * @param ctx the parse tree
	 */
	void exitListLine(HacParser.ListLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#listItem}.
	 * @param ctx the parse tree
	 */
	void enterListItem(HacParser.ListItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#listItem}.
	 * @param ctx the parse tree
	 */
	void exitListItem(HacParser.ListItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#textStart}.
	 * @param ctx the parse tree
	 */
	void enterTextStart(HacParser.TextStartContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#textStart}.
	 * @param ctx the parse tree
	 */
	void exitTextStart(HacParser.TextStartContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#textTag}.
	 * @param ctx the parse tree
	 */
	void enterTextTag(HacParser.TextTagContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#textTag}.
	 * @param ctx the parse tree
	 */
	void exitTextTag(HacParser.TextTagContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#listTag}.
	 * @param ctx the parse tree
	 */
	void enterListTag(HacParser.ListTagContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#listTag}.
	 * @param ctx the parse tree
	 */
	void exitListTag(HacParser.ListTagContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#singleTextLine}.
	 * @param ctx the parse tree
	 */
	void enterSingleTextLine(HacParser.SingleTextLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#singleTextLine}.
	 * @param ctx the parse tree
	 */
	void exitSingleTextLine(HacParser.SingleTextLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#textLine}.
	 * @param ctx the parse tree
	 */
	void enterTextLine(HacParser.TextLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#textLine}.
	 * @param ctx the parse tree
	 */
	void exitTextLine(HacParser.TextLineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#preline}.
	 * @param ctx the parse tree
	 */
	void enterPreline(HacParser.PrelineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#preline}.
	 * @param ctx the parse tree
	 */
	void exitPreline(HacParser.PrelineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#endline}.
	 * @param ctx the parse tree
	 */
	void enterEndline(HacParser.EndlineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#endline}.
	 * @param ctx the parse tree
	 */
	void exitEndline(HacParser.EndlineContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#data}.
	 * @param ctx the parse tree
	 */
	void enterData(HacParser.DataContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#data}.
	 * @param ctx the parse tree
	 */
	void exitData(HacParser.DataContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#allData}.
	 * @param ctx the parse tree
	 */
	void enterAllData(HacParser.AllDataContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#allData}.
	 * @param ctx the parse tree
	 */
	void exitAllData(HacParser.AllDataContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#hqlText}.
	 * @param ctx the parse tree
	 */
	void enterHqlText(HacParser.HqlTextContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#hqlText}.
	 * @param ctx the parse tree
	 */
	void exitHqlText(HacParser.HqlTextContext ctx);
	/**
	 * Enter a parse tree produced by {@link HacParser#hqlLine}.
	 * @param ctx the parse tree
	 */
	void enterHqlLine(HacParser.HqlLineContext ctx);
	/**
	 * Exit a parse tree produced by {@link HacParser#hqlLine}.
	 * @param ctx the parse tree
	 */
	void exitHqlLine(HacParser.HqlLineContext ctx);
}