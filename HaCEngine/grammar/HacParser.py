# Generated from Hac.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,4,0,23,8,0,11,0,12,0,24,1,0,1,
        0,1,1,1,1,1,1,3,1,32,8,1,1,2,1,2,1,2,4,2,37,8,2,11,2,12,2,38,1,2,
        1,2,3,2,43,8,2,1,3,1,3,1,3,1,3,5,3,49,8,3,10,3,12,3,52,9,3,1,3,1,
        3,5,3,56,8,3,10,3,12,3,59,9,3,1,4,1,4,1,4,1,5,1,5,4,5,66,8,5,11,
        5,12,5,67,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,77,8,6,1,6,1,6,5,6,81,
        8,6,10,6,12,6,84,9,6,1,7,4,7,87,8,7,11,7,12,7,88,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,3,8,98,8,8,1,9,1,9,4,9,102,8,9,11,9,12,9,103,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,7,7,2,0,1,2,7,11,108,0,20,1,
        0,0,0,2,31,1,0,0,0,4,42,1,0,0,0,6,44,1,0,0,0,8,60,1,0,0,0,10,63,
        1,0,0,0,12,72,1,0,0,0,14,86,1,0,0,0,16,97,1,0,0,0,18,99,1,0,0,0,
        20,22,5,4,0,0,21,23,3,2,1,0,22,21,1,0,0,0,23,24,1,0,0,0,24,22,1,
        0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,27,5,5,0,0,27,1,1,0,0,0,28,
        32,3,6,3,0,29,32,3,12,6,0,30,32,3,4,2,0,31,28,1,0,0,0,31,29,1,0,
        0,0,31,30,1,0,0,0,32,3,1,0,0,0,33,34,5,6,0,0,34,43,5,3,0,0,35,37,
        5,2,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,0,0,0,
        39,40,1,0,0,0,40,41,5,1,0,0,41,43,5,3,0,0,42,33,1,0,0,0,42,36,1,
        0,0,0,43,5,1,0,0,0,44,45,5,6,0,0,45,46,5,7,0,0,46,50,5,10,0,0,47,
        49,5,2,0,0,48,47,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,
        0,51,53,1,0,0,0,52,50,1,0,0,0,53,57,5,3,0,0,54,56,3,8,4,0,55,54,
        1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,7,1,0,0,0,59,
        57,1,0,0,0,60,61,5,6,0,0,61,62,3,10,5,0,62,9,1,0,0,0,63,65,5,8,0,
        0,64,66,5,2,0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,
        1,0,0,0,68,69,1,0,0,0,69,70,3,18,9,0,70,71,5,3,0,0,71,11,1,0,0,0,
        72,73,5,6,0,0,73,74,5,7,0,0,74,76,5,9,0,0,75,77,3,14,7,0,76,75,1,
        0,0,0,76,77,1,0,0,0,77,78,1,0,0,0,78,82,5,3,0,0,79,81,3,16,8,0,80,
        79,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,83,1,0,0,0,83,13,1,0,0,
        0,84,82,1,0,0,0,85,87,5,2,0,0,86,85,1,0,0,0,87,88,1,0,0,0,88,86,
        1,0,0,0,88,89,1,0,0,0,89,90,1,0,0,0,90,91,3,18,9,0,91,15,1,0,0,0,
        92,93,5,6,0,0,93,94,3,18,9,0,94,95,5,3,0,0,95,98,1,0,0,0,96,98,3,
        4,2,0,97,92,1,0,0,0,97,96,1,0,0,0,98,17,1,0,0,0,99,101,8,0,0,0,100,
        102,7,1,0,0,101,100,1,0,0,0,102,103,1,0,0,0,103,101,1,0,0,0,103,
        104,1,0,0,0,104,19,1,0,0,0,12,24,31,38,42,50,57,67,76,82,88,97,103
    ]

class HacParser ( Parser ):

    grammarFileName = "Hac.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'@'", "'-'" ]

    symbolicNames = [ "<INVALID>", "ASTERISK", "SPACE", "NEWLINE", "COMMENTSTART", 
                      "COMMENTEND", "PRELINE", "ATSIGN", "DASH", "TEXTTAG", 
                      "LISTTAG", "CHAR" ]

    RULE_dacBlock = 0
    RULE_tagSection = 1
    RULE_emptyLine = 2
    RULE_listStart = 3
    RULE_listLine = 4
    RULE_listItem = 5
    RULE_textStart = 6
    RULE_singleTextLine = 7
    RULE_textLine = 8
    RULE_data = 9

    ruleNames =  [ "dacBlock", "tagSection", "emptyLine", "listStart", "listLine", 
                   "listItem", "textStart", "singleTextLine", "textLine", 
                   "data" ]

    EOF = Token.EOF
    ASTERISK=1
    SPACE=2
    NEWLINE=3
    COMMENTSTART=4
    COMMENTEND=5
    PRELINE=6
    ATSIGN=7
    DASH=8
    TEXTTAG=9
    LISTTAG=10
    CHAR=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DacBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._tagSection = None # TagSectionContext
            self.Tags = list() # of TagSectionContexts

        def COMMENTSTART(self):
            return self.getToken(HacParser.COMMENTSTART, 0)

        def COMMENTEND(self):
            return self.getToken(HacParser.COMMENTEND, 0)

        def tagSection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HacParser.TagSectionContext)
            else:
                return self.getTypedRuleContext(HacParser.TagSectionContext,i)


        def getRuleIndex(self):
            return HacParser.RULE_dacBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDacBlock" ):
                listener.enterDacBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDacBlock" ):
                listener.exitDacBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDacBlock" ):
                return visitor.visitDacBlock(self)
            else:
                return visitor.visitChildren(self)




    def dacBlock(self):

        localctx = HacParser.DacBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_dacBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(HacParser.COMMENTSTART)
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                localctx._tagSection = self.tagSection()
                localctx.Tags.append(localctx._tagSection)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==6):
                    break

            self.state = 26
            self.match(HacParser.COMMENTEND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagSectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.List = None # ListStartContext
            self.Text = None # TextStartContext
            self.Empty = None # EmptyLineContext

        def listStart(self):
            return self.getTypedRuleContext(HacParser.ListStartContext,0)


        def textStart(self):
            return self.getTypedRuleContext(HacParser.TextStartContext,0)


        def emptyLine(self):
            return self.getTypedRuleContext(HacParser.EmptyLineContext,0)


        def getRuleIndex(self):
            return HacParser.RULE_tagSection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagSection" ):
                listener.enterTagSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagSection" ):
                listener.exitTagSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagSection" ):
                return visitor.visitTagSection(self)
            else:
                return visitor.visitChildren(self)




    def tagSection(self):

        localctx = HacParser.TagSectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_tagSection)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                localctx.List = self.listStart()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                localctx.Text = self.textStart()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                localctx.Empty = self.emptyLine()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRELINE(self):
            return self.getToken(HacParser.PRELINE, 0)

        def NEWLINE(self):
            return self.getToken(HacParser.NEWLINE, 0)

        def ASTERISK(self):
            return self.getToken(HacParser.ASTERISK, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.SPACE)
            else:
                return self.getToken(HacParser.SPACE, i)

        def getRuleIndex(self):
            return HacParser.RULE_emptyLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyLine" ):
                listener.enterEmptyLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyLine" ):
                listener.exitEmptyLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyLine" ):
                return visitor.visitEmptyLine(self)
            else:
                return visitor.visitChildren(self)




    def emptyLine(self):

        localctx = HacParser.EmptyLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_emptyLine)
        self._la = 0 # Token type
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(HacParser.PRELINE)
                self.state = 34
                self.match(HacParser.NEWLINE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 35
                    self.match(HacParser.SPACE)
                    self.state = 38 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break

                self.state = 40
                self.match(HacParser.ASTERISK)
                self.state = 41
                self.match(HacParser.NEWLINE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Name = None # Token
            self._listLine = None # ListLineContext
            self.Items = list() # of ListLineContexts

        def PRELINE(self):
            return self.getToken(HacParser.PRELINE, 0)

        def ATSIGN(self):
            return self.getToken(HacParser.ATSIGN, 0)

        def NEWLINE(self):
            return self.getToken(HacParser.NEWLINE, 0)

        def LISTTAG(self):
            return self.getToken(HacParser.LISTTAG, 0)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.SPACE)
            else:
                return self.getToken(HacParser.SPACE, i)

        def listLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HacParser.ListLineContext)
            else:
                return self.getTypedRuleContext(HacParser.ListLineContext,i)


        def getRuleIndex(self):
            return HacParser.RULE_listStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListStart" ):
                listener.enterListStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListStart" ):
                listener.exitListStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListStart" ):
                return visitor.visitListStart(self)
            else:
                return visitor.visitChildren(self)




    def listStart(self):

        localctx = HacParser.ListStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_listStart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(HacParser.PRELINE)
            self.state = 45
            self.match(HacParser.ATSIGN)
            self.state = 46
            localctx.Name = self.match(HacParser.LISTTAG)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 47
                self.match(HacParser.SPACE)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 53
            self.match(HacParser.NEWLINE)
            self.state = 57
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    localctx._listLine = self.listLine()
                    localctx.Items.append(localctx._listLine) 
                self.state = 59
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Item = None # ListItemContext

        def PRELINE(self):
            return self.getToken(HacParser.PRELINE, 0)

        def listItem(self):
            return self.getTypedRuleContext(HacParser.ListItemContext,0)


        def getRuleIndex(self):
            return HacParser.RULE_listLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListLine" ):
                listener.enterListLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListLine" ):
                listener.exitListLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListLine" ):
                return visitor.visitListLine(self)
            else:
                return visitor.visitChildren(self)




    def listLine(self):

        localctx = HacParser.ListLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(HacParser.PRELINE)
            self.state = 61
            localctx.Item = self.listItem()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Data = None # DataContext

        def DASH(self):
            return self.getToken(HacParser.DASH, 0)

        def NEWLINE(self):
            return self.getToken(HacParser.NEWLINE, 0)

        def data(self):
            return self.getTypedRuleContext(HacParser.DataContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.SPACE)
            else:
                return self.getToken(HacParser.SPACE, i)

        def getRuleIndex(self):
            return HacParser.RULE_listItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListItem" ):
                listener.enterListItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListItem" ):
                listener.exitListItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListItem" ):
                return visitor.visitListItem(self)
            else:
                return visitor.visitChildren(self)




    def listItem(self):

        localctx = HacParser.ListItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_listItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(HacParser.DASH)
            self.state = 65 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 64
                    self.match(HacParser.SPACE)

                else:
                    raise NoViableAltException(self)
                self.state = 67 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 69
            localctx.Data = self.data()
            self.state = 70
            self.match(HacParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextStartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Name = None # Token
            self.Root = None # SingleTextLineContext
            self._textLine = None # TextLineContext
            self.Lines = list() # of TextLineContexts

        def PRELINE(self):
            return self.getToken(HacParser.PRELINE, 0)

        def ATSIGN(self):
            return self.getToken(HacParser.ATSIGN, 0)

        def NEWLINE(self):
            return self.getToken(HacParser.NEWLINE, 0)

        def TEXTTAG(self):
            return self.getToken(HacParser.TEXTTAG, 0)

        def singleTextLine(self):
            return self.getTypedRuleContext(HacParser.SingleTextLineContext,0)


        def textLine(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HacParser.TextLineContext)
            else:
                return self.getTypedRuleContext(HacParser.TextLineContext,i)


        def getRuleIndex(self):
            return HacParser.RULE_textStart

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextStart" ):
                listener.enterTextStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextStart" ):
                listener.exitTextStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextStart" ):
                return visitor.visitTextStart(self)
            else:
                return visitor.visitChildren(self)




    def textStart(self):

        localctx = HacParser.TextStartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_textStart)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(HacParser.PRELINE)
            self.state = 73
            self.match(HacParser.ATSIGN)
            self.state = 74
            localctx.Name = self.match(HacParser.TEXTTAG)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 75
                localctx.Root = self.singleTextLine()


            self.state = 78
            self.match(HacParser.NEWLINE)
            self.state = 82
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 79
                    localctx._textLine = self.textLine()
                    localctx.Lines.append(localctx._textLine) 
                self.state = 84
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SingleTextLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Line = None # DataContext

        def data(self):
            return self.getTypedRuleContext(HacParser.DataContext,0)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.SPACE)
            else:
                return self.getToken(HacParser.SPACE, i)

        def getRuleIndex(self):
            return HacParser.RULE_singleTextLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleTextLine" ):
                listener.enterSingleTextLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleTextLine" ):
                listener.exitSingleTextLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleTextLine" ):
                return visitor.visitSingleTextLine(self)
            else:
                return visitor.visitChildren(self)




    def singleTextLine(self):

        localctx = HacParser.SingleTextLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_singleTextLine)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 85
                    self.match(HacParser.SPACE)

                else:
                    raise NoViableAltException(self)
                self.state = 88 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 90
            localctx.Line = self.data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TextLineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.Data = None # DataContext

        def PRELINE(self):
            return self.getToken(HacParser.PRELINE, 0)

        def NEWLINE(self):
            return self.getToken(HacParser.NEWLINE, 0)

        def data(self):
            return self.getTypedRuleContext(HacParser.DataContext,0)


        def emptyLine(self):
            return self.getTypedRuleContext(HacParser.EmptyLineContext,0)


        def getRuleIndex(self):
            return HacParser.RULE_textLine

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextLine" ):
                listener.enterTextLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextLine" ):
                listener.exitTextLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextLine" ):
                return visitor.visitTextLine(self)
            else:
                return visitor.visitChildren(self)




    def textLine(self):

        localctx = HacParser.TextLineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_textLine)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.match(HacParser.PRELINE)
                self.state = 93
                localctx.Data = self.data()
                self.state = 94
                self.match(HacParser.NEWLINE)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 96
                self.emptyLine()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATSIGN(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.ATSIGN)
            else:
                return self.getToken(HacParser.ATSIGN, i)

        def CHAR(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.CHAR)
            else:
                return self.getToken(HacParser.CHAR, i)

        def DASH(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.DASH)
            else:
                return self.getToken(HacParser.DASH, i)

        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.SPACE)
            else:
                return self.getToken(HacParser.SPACE, i)

        def ASTERISK(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.ASTERISK)
            else:
                return self.getToken(HacParser.ASTERISK, i)

        def TEXTTAG(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.TEXTTAG)
            else:
                return self.getToken(HacParser.TEXTTAG, i)

        def LISTTAG(self, i:int=None):
            if i is None:
                return self.getTokens(HacParser.LISTTAG)
            else:
                return self.getToken(HacParser.LISTTAG, i)

        def getRuleIndex(self):
            return HacParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = HacParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            _la = self._input.LA(1)
            if _la <= 0 or _la==7:
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 101 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 100
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3974) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 103 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 3974) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





