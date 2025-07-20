// Generated from Hac.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link HacParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface HacVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link HacParser#dacBlock}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDacBlock(HacParser.DacBlockContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#tagSection}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTagSection(HacParser.TagSectionContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#emptyLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEmptyLine(HacParser.EmptyLineContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#listStart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListStart(HacParser.ListStartContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#listLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListLine(HacParser.ListLineContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#listItem}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListItem(HacParser.ListItemContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#textStart}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTextStart(HacParser.TextStartContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#textTag}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTextTag(HacParser.TextTagContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#listTag}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitListTag(HacParser.ListTagContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#singleTextLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSingleTextLine(HacParser.SingleTextLineContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#textLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTextLine(HacParser.TextLineContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#preline}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPreline(HacParser.PrelineContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#endline}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEndline(HacParser.EndlineContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#data}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitData(HacParser.DataContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#allData}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAllData(HacParser.AllDataContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#hqlText}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHqlText(HacParser.HqlTextContext ctx);
	/**
	 * Visit a parse tree produced by {@link HacParser#hqlLine}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitHqlLine(HacParser.HqlLineContext ctx);
}