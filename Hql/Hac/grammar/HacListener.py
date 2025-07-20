# Generated from Hac.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HacParser import HacParser
else:
    from HacParser import HacParser

# This class defines a complete listener for a parse tree produced by HacParser.
class HacListener(ParseTreeListener):

    # Enter a parse tree produced by HacParser#dacBlock.
    def enterDacBlock(self, ctx:HacParser.DacBlockContext):
        pass

    # Exit a parse tree produced by HacParser#dacBlock.
    def exitDacBlock(self, ctx:HacParser.DacBlockContext):
        pass


    # Enter a parse tree produced by HacParser#tagSection.
    def enterTagSection(self, ctx:HacParser.TagSectionContext):
        pass

    # Exit a parse tree produced by HacParser#tagSection.
    def exitTagSection(self, ctx:HacParser.TagSectionContext):
        pass


    # Enter a parse tree produced by HacParser#emptyLine.
    def enterEmptyLine(self, ctx:HacParser.EmptyLineContext):
        pass

    # Exit a parse tree produced by HacParser#emptyLine.
    def exitEmptyLine(self, ctx:HacParser.EmptyLineContext):
        pass


    # Enter a parse tree produced by HacParser#listStart.
    def enterListStart(self, ctx:HacParser.ListStartContext):
        pass

    # Exit a parse tree produced by HacParser#listStart.
    def exitListStart(self, ctx:HacParser.ListStartContext):
        pass


    # Enter a parse tree produced by HacParser#listLine.
    def enterListLine(self, ctx:HacParser.ListLineContext):
        pass

    # Exit a parse tree produced by HacParser#listLine.
    def exitListLine(self, ctx:HacParser.ListLineContext):
        pass


    # Enter a parse tree produced by HacParser#listItem.
    def enterListItem(self, ctx:HacParser.ListItemContext):
        pass

    # Exit a parse tree produced by HacParser#listItem.
    def exitListItem(self, ctx:HacParser.ListItemContext):
        pass


    # Enter a parse tree produced by HacParser#textStart.
    def enterTextStart(self, ctx:HacParser.TextStartContext):
        pass

    # Exit a parse tree produced by HacParser#textStart.
    def exitTextStart(self, ctx:HacParser.TextStartContext):
        pass


    # Enter a parse tree produced by HacParser#textTag.
    def enterTextTag(self, ctx:HacParser.TextTagContext):
        pass

    # Exit a parse tree produced by HacParser#textTag.
    def exitTextTag(self, ctx:HacParser.TextTagContext):
        pass


    # Enter a parse tree produced by HacParser#listTag.
    def enterListTag(self, ctx:HacParser.ListTagContext):
        pass

    # Exit a parse tree produced by HacParser#listTag.
    def exitListTag(self, ctx:HacParser.ListTagContext):
        pass


    # Enter a parse tree produced by HacParser#singleTextLine.
    def enterSingleTextLine(self, ctx:HacParser.SingleTextLineContext):
        pass

    # Exit a parse tree produced by HacParser#singleTextLine.
    def exitSingleTextLine(self, ctx:HacParser.SingleTextLineContext):
        pass


    # Enter a parse tree produced by HacParser#textLine.
    def enterTextLine(self, ctx:HacParser.TextLineContext):
        pass

    # Exit a parse tree produced by HacParser#textLine.
    def exitTextLine(self, ctx:HacParser.TextLineContext):
        pass


    # Enter a parse tree produced by HacParser#preline.
    def enterPreline(self, ctx:HacParser.PrelineContext):
        pass

    # Exit a parse tree produced by HacParser#preline.
    def exitPreline(self, ctx:HacParser.PrelineContext):
        pass


    # Enter a parse tree produced by HacParser#endline.
    def enterEndline(self, ctx:HacParser.EndlineContext):
        pass

    # Exit a parse tree produced by HacParser#endline.
    def exitEndline(self, ctx:HacParser.EndlineContext):
        pass


    # Enter a parse tree produced by HacParser#data.
    def enterData(self, ctx:HacParser.DataContext):
        pass

    # Exit a parse tree produced by HacParser#data.
    def exitData(self, ctx:HacParser.DataContext):
        pass


    # Enter a parse tree produced by HacParser#allData.
    def enterAllData(self, ctx:HacParser.AllDataContext):
        pass

    # Exit a parse tree produced by HacParser#allData.
    def exitAllData(self, ctx:HacParser.AllDataContext):
        pass


    # Enter a parse tree produced by HacParser#hqlText.
    def enterHqlText(self, ctx:HacParser.HqlTextContext):
        pass

    # Exit a parse tree produced by HacParser#hqlText.
    def exitHqlText(self, ctx:HacParser.HqlTextContext):
        pass


    # Enter a parse tree produced by HacParser#hqlLine.
    def enterHqlLine(self, ctx:HacParser.HqlLineContext):
        pass

    # Exit a parse tree produced by HacParser#hqlLine.
    def exitHqlLine(self, ctx:HacParser.HqlLineContext):
        pass



del HacParser