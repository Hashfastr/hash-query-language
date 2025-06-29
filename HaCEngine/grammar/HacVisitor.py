# Generated from Hac.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .HacParser import HacParser
else:
    from HacParser import HacParser

# This class defines a complete generic visitor for a parse tree produced by HacParser.

class HacVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by HacParser#dacBlock.
    def visitDacBlock(self, ctx:HacParser.DacBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#tagSection.
    def visitTagSection(self, ctx:HacParser.TagSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#emptyLine.
    def visitEmptyLine(self, ctx:HacParser.EmptyLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#listStart.
    def visitListStart(self, ctx:HacParser.ListStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#listLine.
    def visitListLine(self, ctx:HacParser.ListLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#listItem.
    def visitListItem(self, ctx:HacParser.ListItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#textStart.
    def visitTextStart(self, ctx:HacParser.TextStartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#singleTextLine.
    def visitSingleTextLine(self, ctx:HacParser.SingleTextLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#textLine.
    def visitTextLine(self, ctx:HacParser.TextLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by HacParser#data.
    def visitData(self, ctx:HacParser.DataContext):
        return self.visitChildren(ctx)



del HacParser