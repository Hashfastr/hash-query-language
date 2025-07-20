// Generated from Hac.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class HacParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASTERISK=1, SPACE=2, NEWLINE=3, COMMENTSTART=4, COMMENTEND=5, ATSIGN=6, 
		DASH=7, TEXTTAG=8, LISTTAG=9, CHAR=10;
	public static final int
		RULE_dacBlock = 0, RULE_tagSection = 1, RULE_emptyLine = 2, RULE_listStart = 3, 
		RULE_listLine = 4, RULE_listItem = 5, RULE_textStart = 6, RULE_textTag = 7, 
		RULE_listTag = 8, RULE_singleTextLine = 9, RULE_textLine = 10, RULE_preline = 11, 
		RULE_endline = 12, RULE_data = 13, RULE_allData = 14, RULE_hqlText = 15, 
		RULE_hqlLine = 16;
	private static String[] makeRuleNames() {
		return new String[] {
			"dacBlock", "tagSection", "emptyLine", "listStart", "listLine", "listItem", 
			"textStart", "textTag", "listTag", "singleTextLine", "textLine", "preline", 
			"endline", "data", "allData", "hqlText", "hqlLine"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'*'", null, null, null, null, "'@'", "'-'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "ASTERISK", "SPACE", "NEWLINE", "COMMENTSTART", "COMMENTEND", "ATSIGN", 
			"DASH", "TEXTTAG", "LISTTAG", "CHAR"
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
	public String getGrammarFileName() { return "Hac.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public HacParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DacBlockContext extends ParserRuleContext {
		public TagSectionContext tagSection;
		public List<TagSectionContext> Tags = new ArrayList<TagSectionContext>();
		public HqlTextContext Hql;
		public TerminalNode COMMENTSTART() { return getToken(HacParser.COMMENTSTART, 0); }
		public TerminalNode COMMENTEND() { return getToken(HacParser.COMMENTEND, 0); }
		public List<TerminalNode> NEWLINE() { return getTokens(HacParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(HacParser.NEWLINE, i);
		}
		public List<TagSectionContext> tagSection() {
			return getRuleContexts(TagSectionContext.class);
		}
		public TagSectionContext tagSection(int i) {
			return getRuleContext(TagSectionContext.class,i);
		}
		public HqlTextContext hqlText() {
			return getRuleContext(HqlTextContext.class,0);
		}
		public DacBlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dacBlock; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterDacBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitDacBlock(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitDacBlock(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DacBlockContext dacBlock() throws RecognitionException {
		DacBlockContext _localctx = new DacBlockContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_dacBlock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(34);
			match(COMMENTSTART);
			setState(36); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(35);
				((DacBlockContext)_localctx).tagSection = tagSection();
				((DacBlockContext)_localctx).Tags.add(((DacBlockContext)_localctx).tagSection);
				}
				}
				setState(38); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==SPACE );
			setState(40);
			match(COMMENTEND);
			setState(44);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NEWLINE) {
				{
				{
				setState(41);
				match(NEWLINE);
				}
				}
				setState(46);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(48);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1990L) != 0)) {
				{
				setState(47);
				((DacBlockContext)_localctx).Hql = hqlText();
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
	public static class TagSectionContext extends ParserRuleContext {
		public ListStartContext List;
		public TextStartContext Text;
		public EmptyLineContext Empty;
		public ListStartContext listStart() {
			return getRuleContext(ListStartContext.class,0);
		}
		public TextStartContext textStart() {
			return getRuleContext(TextStartContext.class,0);
		}
		public EmptyLineContext emptyLine() {
			return getRuleContext(EmptyLineContext.class,0);
		}
		public TagSectionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tagSection; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterTagSection(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitTagSection(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitTagSection(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TagSectionContext tagSection() throws RecognitionException {
		TagSectionContext _localctx = new TagSectionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_tagSection);
		try {
			setState(53);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				((TagSectionContext)_localctx).List = listStart();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(51);
				((TagSectionContext)_localctx).Text = textStart();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(52);
				((TagSectionContext)_localctx).Empty = emptyLine();
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
	public static class EmptyLineContext extends ParserRuleContext {
		public PrelineContext preline() {
			return getRuleContext(PrelineContext.class,0);
		}
		public EndlineContext endline() {
			return getRuleContext(EndlineContext.class,0);
		}
		public EmptyLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emptyLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterEmptyLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitEmptyLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitEmptyLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EmptyLineContext emptyLine() throws RecognitionException {
		EmptyLineContext _localctx = new EmptyLineContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_emptyLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(55);
			preline();
			setState(56);
			endline();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListStartContext extends ParserRuleContext {
		public ListTagContext Name;
		public ListLineContext listLine;
		public List<ListLineContext> Items = new ArrayList<ListLineContext>();
		public PrelineContext preline() {
			return getRuleContext(PrelineContext.class,0);
		}
		public EndlineContext endline() {
			return getRuleContext(EndlineContext.class,0);
		}
		public ListTagContext listTag() {
			return getRuleContext(ListTagContext.class,0);
		}
		public List<ListLineContext> listLine() {
			return getRuleContexts(ListLineContext.class);
		}
		public ListLineContext listLine(int i) {
			return getRuleContext(ListLineContext.class,i);
		}
		public ListStartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listStart; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterListStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitListStart(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitListStart(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListStartContext listStart() throws RecognitionException {
		ListStartContext _localctx = new ListStartContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_listStart);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			preline();
			setState(59);
			((ListStartContext)_localctx).Name = listTag();
			setState(60);
			endline();
			setState(64);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(61);
					((ListStartContext)_localctx).listLine = listLine();
					((ListStartContext)_localctx).Items.add(((ListStartContext)_localctx).listLine);
					}
					} 
				}
				setState(66);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
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
	public static class ListLineContext extends ParserRuleContext {
		public ListItemContext Item;
		public PrelineContext preline() {
			return getRuleContext(PrelineContext.class,0);
		}
		public ListItemContext listItem() {
			return getRuleContext(ListItemContext.class,0);
		}
		public ListLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterListLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitListLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitListLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListLineContext listLine() throws RecognitionException {
		ListLineContext _localctx = new ListLineContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_listLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			preline();
			setState(68);
			((ListLineContext)_localctx).Item = listItem();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListItemContext extends ParserRuleContext {
		public DataContext Data;
		public TerminalNode DASH() { return getToken(HacParser.DASH, 0); }
		public EndlineContext endline() {
			return getRuleContext(EndlineContext.class,0);
		}
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public List<TerminalNode> SPACE() { return getTokens(HacParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(HacParser.SPACE, i);
		}
		public ListItemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listItem; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterListItem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitListItem(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitListItem(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListItemContext listItem() throws RecognitionException {
		ListItemContext _localctx = new ListItemContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_listItem);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(DASH);
			setState(72); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(71);
				match(SPACE);
				}
				}
				setState(74); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==SPACE );
			setState(76);
			((ListItemContext)_localctx).Data = data();
			setState(77);
			endline();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextStartContext extends ParserRuleContext {
		public TextTagContext Name;
		public SingleTextLineContext Root;
		public TextLineContext textLine;
		public List<TextLineContext> Lines = new ArrayList<TextLineContext>();
		public PrelineContext preline() {
			return getRuleContext(PrelineContext.class,0);
		}
		public TextTagContext textTag() {
			return getRuleContext(TextTagContext.class,0);
		}
		public EndlineContext endline() {
			return getRuleContext(EndlineContext.class,0);
		}
		public SingleTextLineContext singleTextLine() {
			return getRuleContext(SingleTextLineContext.class,0);
		}
		public List<TextLineContext> textLine() {
			return getRuleContexts(TextLineContext.class);
		}
		public TextLineContext textLine(int i) {
			return getRuleContext(TextLineContext.class,i);
		}
		public TextStartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_textStart; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterTextStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitTextStart(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitTextStart(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TextStartContext textStart() throws RecognitionException {
		TextStartContext _localctx = new TextStartContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_textStart);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			preline();
			setState(80);
			((TextStartContext)_localctx).Name = textTag();
			setState(83);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(81);
				((TextStartContext)_localctx).Root = singleTextLine();
				}
				break;
			case 2:
				{
				setState(82);
				endline();
				}
				break;
			}
			setState(88);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(85);
					((TextStartContext)_localctx).textLine = textLine();
					((TextStartContext)_localctx).Lines.add(((TextStartContext)_localctx).textLine);
					}
					} 
				}
				setState(90);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
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
	public static class TextTagContext extends ParserRuleContext {
		public Token Name;
		public TerminalNode ATSIGN() { return getToken(HacParser.ATSIGN, 0); }
		public TerminalNode TEXTTAG() { return getToken(HacParser.TEXTTAG, 0); }
		public TextTagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_textTag; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterTextTag(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitTextTag(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitTextTag(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TextTagContext textTag() throws RecognitionException {
		TextTagContext _localctx = new TextTagContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_textTag);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(91);
			match(ATSIGN);
			setState(92);
			((TextTagContext)_localctx).Name = match(TEXTTAG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListTagContext extends ParserRuleContext {
		public Token Name;
		public TerminalNode ATSIGN() { return getToken(HacParser.ATSIGN, 0); }
		public TerminalNode LISTTAG() { return getToken(HacParser.LISTTAG, 0); }
		public ListTagContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listTag; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterListTag(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitListTag(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitListTag(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ListTagContext listTag() throws RecognitionException {
		ListTagContext _localctx = new ListTagContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_listTag);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(ATSIGN);
			setState(95);
			((ListTagContext)_localctx).Name = match(LISTTAG);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SingleTextLineContext extends ParserRuleContext {
		public AllDataContext Line;
		public EndlineContext endline() {
			return getRuleContext(EndlineContext.class,0);
		}
		public AllDataContext allData() {
			return getRuleContext(AllDataContext.class,0);
		}
		public List<TerminalNode> SPACE() { return getTokens(HacParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(HacParser.SPACE, i);
		}
		public SingleTextLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_singleTextLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterSingleTextLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitSingleTextLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitSingleTextLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final SingleTextLineContext singleTextLine() throws RecognitionException {
		SingleTextLineContext _localctx = new SingleTextLineContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_singleTextLine);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(98); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(97);
					match(SPACE);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(100); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(102);
			((SingleTextLineContext)_localctx).Line = allData();
			setState(103);
			endline();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TextLineContext extends ParserRuleContext {
		public DataContext Line;
		public PrelineContext preline() {
			return getRuleContext(PrelineContext.class,0);
		}
		public EndlineContext endline() {
			return getRuleContext(EndlineContext.class,0);
		}
		public DataContext data() {
			return getRuleContext(DataContext.class,0);
		}
		public EmptyLineContext emptyLine() {
			return getRuleContext(EmptyLineContext.class,0);
		}
		public TextLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_textLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterTextLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitTextLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitTextLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TextLineContext textLine() throws RecognitionException {
		TextLineContext _localctx = new TextLineContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_textLine);
		try {
			setState(110);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(105);
				preline();
				setState(106);
				((TextLineContext)_localctx).Line = data();
				setState(107);
				endline();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(109);
				emptyLine();
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
	public static class PrelineContext extends ParserRuleContext {
		public List<TerminalNode> SPACE() { return getTokens(HacParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(HacParser.SPACE, i);
		}
		public TerminalNode ASTERISK() { return getToken(HacParser.ASTERISK, 0); }
		public PrelineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_preline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterPreline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitPreline(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitPreline(this);
			else return visitor.visitChildren(this);
		}
	}

	public final PrelineContext preline() throws RecognitionException {
		PrelineContext _localctx = new PrelineContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_preline);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			match(SPACE);
			setState(113);
			match(ASTERISK);
			setState(117);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(114);
					match(SPACE);
					}
					} 
				}
				setState(119);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
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
	public static class EndlineContext extends ParserRuleContext {
		public TerminalNode NEWLINE() { return getToken(HacParser.NEWLINE, 0); }
		public List<TerminalNode> SPACE() { return getTokens(HacParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(HacParser.SPACE, i);
		}
		public EndlineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_endline; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterEndline(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitEndline(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitEndline(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EndlineContext endline() throws RecognitionException {
		EndlineContext _localctx = new EndlineContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_endline);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==SPACE) {
				{
				{
				setState(120);
				match(SPACE);
				}
				}
				setState(125);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(126);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DataContext extends ParserRuleContext {
		public List<TerminalNode> ATSIGN() { return getTokens(HacParser.ATSIGN); }
		public TerminalNode ATSIGN(int i) {
			return getToken(HacParser.ATSIGN, i);
		}
		public TerminalNode NEWLINE() { return getToken(HacParser.NEWLINE, 0); }
		public List<TerminalNode> SPACE() { return getTokens(HacParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(HacParser.SPACE, i);
		}
		public List<TerminalNode> CHAR() { return getTokens(HacParser.CHAR); }
		public TerminalNode CHAR(int i) {
			return getToken(HacParser.CHAR, i);
		}
		public List<TerminalNode> DASH() { return getTokens(HacParser.DASH); }
		public TerminalNode DASH(int i) {
			return getToken(HacParser.DASH, i);
		}
		public List<TerminalNode> ASTERISK() { return getTokens(HacParser.ASTERISK); }
		public TerminalNode ASTERISK(int i) {
			return getToken(HacParser.ASTERISK, i);
		}
		public List<TerminalNode> TEXTTAG() { return getTokens(HacParser.TEXTTAG); }
		public TerminalNode TEXTTAG(int i) {
			return getToken(HacParser.TEXTTAG, i);
		}
		public List<TerminalNode> LISTTAG() { return getTokens(HacParser.LISTTAG); }
		public TerminalNode LISTTAG(int i) {
			return getToken(HacParser.LISTTAG, i);
		}
		public DataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_data; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterData(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitData(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitData(this);
			else return visitor.visitChildren(this);
		}
	}

	public final DataContext data() throws RecognitionException {
		DataContext _localctx = new DataContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_data);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			_la = _input.LA(1);
			if ( _la <= 0 || ((((_la) & ~0x3f) == 0 && ((1L << _la) & 76L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(130); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(129);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1990L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(132); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,12,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AllDataContext extends ParserRuleContext {
		public List<TerminalNode> CHAR() { return getTokens(HacParser.CHAR); }
		public TerminalNode CHAR(int i) {
			return getToken(HacParser.CHAR, i);
		}
		public List<TerminalNode> DASH() { return getTokens(HacParser.DASH); }
		public TerminalNode DASH(int i) {
			return getToken(HacParser.DASH, i);
		}
		public List<TerminalNode> SPACE() { return getTokens(HacParser.SPACE); }
		public TerminalNode SPACE(int i) {
			return getToken(HacParser.SPACE, i);
		}
		public List<TerminalNode> ASTERISK() { return getTokens(HacParser.ASTERISK); }
		public TerminalNode ASTERISK(int i) {
			return getToken(HacParser.ASTERISK, i);
		}
		public List<TerminalNode> ATSIGN() { return getTokens(HacParser.ATSIGN); }
		public TerminalNode ATSIGN(int i) {
			return getToken(HacParser.ATSIGN, i);
		}
		public List<TerminalNode> TEXTTAG() { return getTokens(HacParser.TEXTTAG); }
		public TerminalNode TEXTTAG(int i) {
			return getToken(HacParser.TEXTTAG, i);
		}
		public List<TerminalNode> LISTTAG() { return getTokens(HacParser.LISTTAG); }
		public TerminalNode LISTTAG(int i) {
			return getToken(HacParser.LISTTAG, i);
		}
		public AllDataContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_allData; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterAllData(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitAllData(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitAllData(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AllDataContext allData() throws RecognitionException {
		AllDataContext _localctx = new AllDataContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_allData);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(135); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(134);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1990L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(137); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,13,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HqlTextContext extends ParserRuleContext {
		public HqlLineContext hqlLine;
		public List<HqlLineContext> Lines = new ArrayList<HqlLineContext>();
		public List<HqlLineContext> hqlLine() {
			return getRuleContexts(HqlLineContext.class);
		}
		public HqlLineContext hqlLine(int i) {
			return getRuleContext(HqlLineContext.class,i);
		}
		public HqlTextContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hqlText; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterHqlText(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitHqlText(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitHqlText(this);
			else return visitor.visitChildren(this);
		}
	}

	public final HqlTextContext hqlText() throws RecognitionException {
		HqlTextContext _localctx = new HqlTextContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_hqlText);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(139);
				((HqlTextContext)_localctx).hqlLine = hqlLine();
				((HqlTextContext)_localctx).Lines.add(((HqlTextContext)_localctx).hqlLine);
				}
				}
				setState(142); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 1990L) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class HqlLineContext extends ParserRuleContext {
		public AllDataContext Data;
		public TerminalNode NEWLINE() { return getToken(HacParser.NEWLINE, 0); }
		public AllDataContext allData() {
			return getRuleContext(AllDataContext.class,0);
		}
		public HqlLineContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_hqlLine; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).enterHqlLine(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof HacListener ) ((HacListener)listener).exitHqlLine(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof HacVisitor ) return ((HacVisitor<? extends T>)visitor).visitHqlLine(this);
			else return visitor.visitChildren(this);
		}
	}

	public final HqlLineContext hqlLine() throws RecognitionException {
		HqlLineContext _localctx = new HqlLineContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_hqlLine);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(144);
			((HqlLineContext)_localctx).Data = allData();
			setState(145);
			match(NEWLINE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\n\u0094\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0004\u0000%\b\u0000"+
		"\u000b\u0000\f\u0000&\u0001\u0000\u0001\u0000\u0005\u0000+\b\u0000\n\u0000"+
		"\f\u0000.\t\u0000\u0001\u0000\u0003\u00001\b\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u00016\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003?\b\u0003"+
		"\n\u0003\f\u0003B\t\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0004\u0005I\b\u0005\u000b\u0005\f\u0005J\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003"+
		"\u0006T\b\u0006\u0001\u0006\u0005\u0006W\b\u0006\n\u0006\f\u0006Z\t\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0004"+
		"\tc\b\t\u000b\t\f\td\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0003\no\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0005\u000b"+
		"t\b\u000b\n\u000b\f\u000bw\t\u000b\u0001\f\u0005\fz\b\f\n\f\f\f}\t\f\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0004\r\u0083\b\r\u000b\r\f\r\u0084\u0001\u000e"+
		"\u0004\u000e\u0088\b\u000e\u000b\u000e\f\u000e\u0089\u0001\u000f\u0004"+
		"\u000f\u008d\b\u000f\u000b\u000f\f\u000f\u008e\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0000\u0002\u0004\u0006\b\n"+
		"\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \u0000\u0002"+
		"\u0002\u0000\u0002\u0003\u0006\u0006\u0002\u0000\u0001\u0002\u0006\n\u0092"+
		"\u0000\"\u0001\u0000\u0000\u0000\u00025\u0001\u0000\u0000\u0000\u0004"+
		"7\u0001\u0000\u0000\u0000\u0006:\u0001\u0000\u0000\u0000\bC\u0001\u0000"+
		"\u0000\u0000\nF\u0001\u0000\u0000\u0000\fO\u0001\u0000\u0000\u0000\u000e"+
		"[\u0001\u0000\u0000\u0000\u0010^\u0001\u0000\u0000\u0000\u0012b\u0001"+
		"\u0000\u0000\u0000\u0014n\u0001\u0000\u0000\u0000\u0016p\u0001\u0000\u0000"+
		"\u0000\u0018{\u0001\u0000\u0000\u0000\u001a\u0080\u0001\u0000\u0000\u0000"+
		"\u001c\u0087\u0001\u0000\u0000\u0000\u001e\u008c\u0001\u0000\u0000\u0000"+
		" \u0090\u0001\u0000\u0000\u0000\"$\u0005\u0004\u0000\u0000#%\u0003\u0002"+
		"\u0001\u0000$#\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000\u0000&$\u0001"+
		"\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\'(\u0001\u0000\u0000\u0000"+
		"(,\u0005\u0005\u0000\u0000)+\u0005\u0003\u0000\u0000*)\u0001\u0000\u0000"+
		"\u0000+.\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000"+
		"\u0000\u0000-0\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000/1\u0003"+
		"\u001e\u000f\u00000/\u0001\u0000\u0000\u000001\u0001\u0000\u0000\u0000"+
		"1\u0001\u0001\u0000\u0000\u000026\u0003\u0006\u0003\u000036\u0003\f\u0006"+
		"\u000046\u0003\u0004\u0002\u000052\u0001\u0000\u0000\u000053\u0001\u0000"+
		"\u0000\u000054\u0001\u0000\u0000\u00006\u0003\u0001\u0000\u0000\u0000"+
		"78\u0003\u0016\u000b\u000089\u0003\u0018\f\u00009\u0005\u0001\u0000\u0000"+
		"\u0000:;\u0003\u0016\u000b\u0000;<\u0003\u0010\b\u0000<@\u0003\u0018\f"+
		"\u0000=?\u0003\b\u0004\u0000>=\u0001\u0000\u0000\u0000?B\u0001\u0000\u0000"+
		"\u0000@>\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000A\u0007\u0001"+
		"\u0000\u0000\u0000B@\u0001\u0000\u0000\u0000CD\u0003\u0016\u000b\u0000"+
		"DE\u0003\n\u0005\u0000E\t\u0001\u0000\u0000\u0000FH\u0005\u0007\u0000"+
		"\u0000GI\u0005\u0002\u0000\u0000HG\u0001\u0000\u0000\u0000IJ\u0001\u0000"+
		"\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KL\u0001"+
		"\u0000\u0000\u0000LM\u0003\u001a\r\u0000MN\u0003\u0018\f\u0000N\u000b"+
		"\u0001\u0000\u0000\u0000OP\u0003\u0016\u000b\u0000PS\u0003\u000e\u0007"+
		"\u0000QT\u0003\u0012\t\u0000RT\u0003\u0018\f\u0000SQ\u0001\u0000\u0000"+
		"\u0000SR\u0001\u0000\u0000\u0000TX\u0001\u0000\u0000\u0000UW\u0003\u0014"+
		"\n\u0000VU\u0001\u0000\u0000\u0000WZ\u0001\u0000\u0000\u0000XV\u0001\u0000"+
		"\u0000\u0000XY\u0001\u0000\u0000\u0000Y\r\u0001\u0000\u0000\u0000ZX\u0001"+
		"\u0000\u0000\u0000[\\\u0005\u0006\u0000\u0000\\]\u0005\b\u0000\u0000]"+
		"\u000f\u0001\u0000\u0000\u0000^_\u0005\u0006\u0000\u0000_`\u0005\t\u0000"+
		"\u0000`\u0011\u0001\u0000\u0000\u0000ac\u0005\u0002\u0000\u0000ba\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000db\u0001\u0000\u0000\u0000"+
		"de\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fg\u0003\u001c\u000e"+
		"\u0000gh\u0003\u0018\f\u0000h\u0013\u0001\u0000\u0000\u0000ij\u0003\u0016"+
		"\u000b\u0000jk\u0003\u001a\r\u0000kl\u0003\u0018\f\u0000lo\u0001\u0000"+
		"\u0000\u0000mo\u0003\u0004\u0002\u0000ni\u0001\u0000\u0000\u0000nm\u0001"+
		"\u0000\u0000\u0000o\u0015\u0001\u0000\u0000\u0000pq\u0005\u0002\u0000"+
		"\u0000qu\u0005\u0001\u0000\u0000rt\u0005\u0002\u0000\u0000sr\u0001\u0000"+
		"\u0000\u0000tw\u0001\u0000\u0000\u0000us\u0001\u0000\u0000\u0000uv\u0001"+
		"\u0000\u0000\u0000v\u0017\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000"+
		"\u0000xz\u0005\u0002\u0000\u0000yx\u0001\u0000\u0000\u0000z}\u0001\u0000"+
		"\u0000\u0000{y\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000|~\u0001"+
		"\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000~\u007f\u0005\u0003\u0000"+
		"\u0000\u007f\u0019\u0001\u0000\u0000\u0000\u0080\u0082\b\u0000\u0000\u0000"+
		"\u0081\u0083\u0007\u0001\u0000\u0000\u0082\u0081\u0001\u0000\u0000\u0000"+
		"\u0083\u0084\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000"+
		"\u0084\u0085\u0001\u0000\u0000\u0000\u0085\u001b\u0001\u0000\u0000\u0000"+
		"\u0086\u0088\u0007\u0001\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000"+
		"\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0001\u0000\u0000\u0000\u008a\u001d\u0001\u0000\u0000\u0000"+
		"\u008b\u008d\u0003 \u0010\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008d"+
		"\u008e\u0001\u0000\u0000\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008e"+
		"\u008f\u0001\u0000\u0000\u0000\u008f\u001f\u0001\u0000\u0000\u0000\u0090"+
		"\u0091\u0003\u001c\u000e\u0000\u0091\u0092\u0005\u0003\u0000\u0000\u0092"+
		"!\u0001\u0000\u0000\u0000\u000f&,05@JSXdnu{\u0084\u0089\u008e";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}