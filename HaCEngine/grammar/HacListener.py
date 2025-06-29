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


    # Enter a parse tree produced by HacParser#data.
    def enterData(self, ctx:HacParser.DataContext):
        pass

    # Exit a parse tree produced by HacParser#data.
    def exitData(self, ctx:HacParser.DataContext):
        pass



del HacParser