// Generated from Hac.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class HacLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		ASTERISK=1, SPACE=2, NEWLINE=3, COMMENTSTART=4, COMMENTEND=5, ATSIGN=6, 
		DASH=7, TEXTTAG=8, LISTTAG=9, CHAR=10;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"ASTERISK", "SPACE", "NEWLINE", "COMMENTSTART", "COMMENTEND", "ATSIGN", 
			"DASH", "TEXTTAG", "LISTTAG", "CHAR"
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


	public HacLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Hac.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\n\u00a1\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0004"+
		"\u0003\u001e\b\u0003\u000b\u0003\f\u0003\u001f\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0004\u0004%\b\u0004\u000b\u0004\f\u0004&\u0001\u0004\u0004"+
		"\u0004*\b\u0004\u000b\u0004\f\u0004+\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007p\b\u0007\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\b\u009e\b\b\u0001"+
		"\t\u0001\t\u0000\u0000\n\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004"+
		"\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0001\u0000\u0002"+
		"\u0002\u0000\t\t  \u0002\u0000\n\n\r\r\u00af\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0001\u0015\u0001\u0000\u0000\u0000\u0003"+
		"\u0017\u0001\u0000\u0000\u0000\u0005\u0019\u0001\u0000\u0000\u0000\u0007"+
		"\u001b\u0001\u0000\u0000\u0000\t$\u0001\u0000\u0000\u0000\u000b/\u0001"+
		"\u0000\u0000\u0000\r1\u0001\u0000\u0000\u0000\u000fo\u0001\u0000\u0000"+
		"\u0000\u0011\u009d\u0001\u0000\u0000\u0000\u0013\u009f\u0001\u0000\u0000"+
		"\u0000\u0015\u0016\u0005*\u0000\u0000\u0016\u0002\u0001\u0000\u0000\u0000"+
		"\u0017\u0018\u0007\u0000\u0000\u0000\u0018\u0004\u0001\u0000\u0000\u0000"+
		"\u0019\u001a\u0007\u0001\u0000\u0000\u001a\u0006\u0001\u0000\u0000\u0000"+
		"\u001b\u001d\u0005/\u0000\u0000\u001c\u001e\u0003\u0001\u0000\u0000\u001d"+
		"\u001c\u0001\u0000\u0000\u0000\u001e\u001f\u0001\u0000\u0000\u0000\u001f"+
		"\u001d\u0001\u0000\u0000\u0000\u001f \u0001\u0000\u0000\u0000 !\u0001"+
		"\u0000\u0000\u0000!\"\u0003\u0005\u0002\u0000\"\b\u0001\u0000\u0000\u0000"+
		"#%\u0003\u0003\u0001\u0000$#\u0001\u0000\u0000\u0000%&\u0001\u0000\u0000"+
		"\u0000&$\u0001\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\')\u0001\u0000"+
		"\u0000\u0000(*\u0003\u0001\u0000\u0000)(\u0001\u0000\u0000\u0000*+\u0001"+
		"\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000\u0000"+
		",-\u0001\u0000\u0000\u0000-.\u0005/\u0000\u0000.\n\u0001\u0000\u0000\u0000"+
		"/0\u0005@\u0000\u00000\f\u0001\u0000\u0000\u000012\u0005-\u0000\u0000"+
		"2\u000e\u0001\u0000\u0000\u000034\u0005t\u0000\u000045\u0005i\u0000\u0000"+
		"56\u0005t\u0000\u000067\u0005l\u0000\u00007p\u0005e\u0000\u000089\u0005"+
		"a\u0000\u00009:\u0005u\u0000\u0000:;\u0005t\u0000\u0000;<\u0005h\u0000"+
		"\u0000<=\u0005o\u0000\u0000=p\u0005r\u0000\u0000>?\u0005i\u0000\u0000"+
		"?p\u0005d\u0000\u0000@A\u0005s\u0000\u0000AB\u0005t\u0000\u0000BC\u0005"+
		"a\u0000\u0000CD\u0005t\u0000\u0000DE\u0005u\u0000\u0000Ep\u0005s\u0000"+
		"\u0000FG\u0005l\u0000\u0000GH\u0005e\u0000\u0000HI\u0005v\u0000\u0000"+
		"IJ\u0005e\u0000\u0000Jp\u0005l\u0000\u0000KL\u0005d\u0000\u0000LM\u0005"+
		"e\u0000\u0000MN\u0005s\u0000\u0000NO\u0005c\u0000\u0000OP\u0005r\u0000"+
		"\u0000PQ\u0005i\u0000\u0000QR\u0005p\u0000\u0000RS\u0005t\u0000\u0000"+
		"ST\u0005i\u0000\u0000TU\u0005o\u0000\u0000Up\u0005n\u0000\u0000VW\u0005"+
		"t\u0000\u0000WX\u0005r\u0000\u0000XY\u0005i\u0000\u0000YZ\u0005a\u0000"+
		"\u0000Z[\u0005g\u0000\u0000[p\u0005e\u0000\u0000\\]\u0005a\u0000\u0000"+
		"]^\u0005u\u0000\u0000^_\u0005t\u0000\u0000_`\u0005h\u0000\u0000`a\u0005"+
		"o\u0000\u0000ab\u0005r\u0000\u0000bc\u0005n\u0000\u0000cd\u0005o\u0000"+
		"\u0000de\u0005t\u0000\u0000ef\u0005e\u0000\u0000fp\u0005s\u0000\u0000"+
		"gh\u0005s\u0000\u0000hi\u0005c\u0000\u0000ij\u0005h\u0000\u0000jk\u0005"+
		"e\u0000\u0000kl\u0005d\u0000\u0000lm\u0005u\u0000\u0000mn\u0005l\u0000"+
		"\u0000np\u0005e\u0000\u0000o3\u0001\u0000\u0000\u0000o8\u0001\u0000\u0000"+
		"\u0000o>\u0001\u0000\u0000\u0000o@\u0001\u0000\u0000\u0000oF\u0001\u0000"+
		"\u0000\u0000oK\u0001\u0000\u0000\u0000oV\u0001\u0000\u0000\u0000o\\\u0001"+
		"\u0000\u0000\u0000og\u0001\u0000\u0000\u0000p\u0010\u0001\u0000\u0000"+
		"\u0000qr\u0005t\u0000\u0000rs\u0005a\u0000\u0000st\u0005g\u0000\u0000"+
		"t\u009e\u0005s\u0000\u0000uv\u0005f\u0000\u0000vw\u0005a\u0000\u0000w"+
		"x\u0005l\u0000\u0000xy\u0005s\u0000\u0000yz\u0005e\u0000\u0000z{\u0005"+
		"p\u0000\u0000{|\u0005o\u0000\u0000|}\u0005s\u0000\u0000}~\u0005i\u0000"+
		"\u0000~\u007f\u0005t\u0000\u0000\u007f\u0080\u0005i\u0000\u0000\u0080"+
		"\u0081\u0005v\u0000\u0000\u0081\u0082\u0005e\u0000\u0000\u0082\u009e\u0005"+
		"s\u0000\u0000\u0083\u0084\u0005r\u0000\u0000\u0084\u0085\u0005e\u0000"+
		"\u0000\u0085\u0086\u0005f\u0000\u0000\u0086\u0087\u0005e\u0000\u0000\u0087"+
		"\u0088\u0005r\u0000\u0000\u0088\u0089\u0005e\u0000\u0000\u0089\u008a\u0005"+
		"n\u0000\u0000\u008a\u008b\u0005c\u0000\u0000\u008b\u008c\u0005e\u0000"+
		"\u0000\u008c\u009e\u0005s\u0000\u0000\u008d\u008e\u0005c\u0000\u0000\u008e"+
		"\u008f\u0005h\u0000\u0000\u008f\u0090\u0005a\u0000\u0000\u0090\u0091\u0005"+
		"n\u0000\u0000\u0091\u0092\u0005g\u0000\u0000\u0092\u0093\u0005e\u0000"+
		"\u0000\u0093\u0094\u0005l\u0000\u0000\u0094\u0095\u0005o\u0000\u0000\u0095"+
		"\u009e\u0005g\u0000\u0000\u0096\u0097\u0005a\u0000\u0000\u0097\u0098\u0005"+
		"c\u0000\u0000\u0098\u0099\u0005t\u0000\u0000\u0099\u009a\u0005i\u0000"+
		"\u0000\u009a\u009b\u0005o\u0000\u0000\u009b\u009c\u0005n\u0000\u0000\u009c"+
		"\u009e\u0005s\u0000\u0000\u009dq\u0001\u0000\u0000\u0000\u009du\u0001"+
		"\u0000\u0000\u0000\u009d\u0083\u0001\u0000\u0000\u0000\u009d\u008d\u0001"+
		"\u0000\u0000\u0000\u009d\u0096\u0001\u0000\u0000\u0000\u009e\u0012\u0001"+
		"\u0000\u0000\u0000\u009f\u00a0\b\u0001\u0000\u0000\u00a0\u0014\u0001\u0000"+
		"\u0000\u0000\u0006\u0000\u001f&+o\u009d\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}