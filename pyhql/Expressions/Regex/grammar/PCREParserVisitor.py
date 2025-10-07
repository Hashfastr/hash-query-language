# Generated from PCREParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PCREParser import PCREParser
else:
    from PCREParser import PCREParser

# This class defines a complete generic visitor for a parse tree produced by PCREParser.

class PCREParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PCREParser#pcre.
    def visitPcre(self, ctx:PCREParser.PcreContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#alternation.
    def visitAlternation(self, ctx:PCREParser.AlternationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#expr.
    def visitExpr(self, ctx:PCREParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#element.
    def visitElement(self, ctx:PCREParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#atom.
    def visitAtom(self, ctx:PCREParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#capture.
    def visitCapture(self, ctx:PCREParser.CaptureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#atomic_group.
    def visitAtomic_group(self, ctx:PCREParser.Atomic_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#lookaround.
    def visitLookaround(self, ctx:PCREParser.LookaroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#backreference.
    def visitBackreference(self, ctx:PCREParser.BackreferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#subroutine_reference.
    def visitSubroutine_reference(self, ctx:PCREParser.Subroutine_referenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#conditional_pattern.
    def visitConditional_pattern(self, ctx:PCREParser.Conditional_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#comment.
    def visitComment(self, ctx:PCREParser.CommentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#quantifier.
    def visitQuantifier(self, ctx:PCREParser.QuantifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#option_setting.
    def visitOption_setting(self, ctx:PCREParser.Option_settingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#option_setting_flag.
    def visitOption_setting_flag(self, ctx:PCREParser.Option_setting_flagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#backtracking_control.
    def visitBacktracking_control(self, ctx:PCREParser.Backtracking_controlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#callout.
    def visitCallout(self, ctx:PCREParser.CalloutContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#newline_conventions.
    def visitNewline_conventions(self, ctx:PCREParser.Newline_conventionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#character.
    def visitCharacter(self, ctx:PCREParser.CharacterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#character_type.
    def visitCharacter_type(self, ctx:PCREParser.Character_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#character_class.
    def visitCharacter_class(self, ctx:PCREParser.Character_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#character_class_atom.
    def visitCharacter_class_atom(self, ctx:PCREParser.Character_class_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#character_class_range.
    def visitCharacter_class_range(self, ctx:PCREParser.Character_class_rangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#character_class_range_atom.
    def visitCharacter_class_range_atom(self, ctx:PCREParser.Character_class_range_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#posix_character_class.
    def visitPosix_character_class(self, ctx:PCREParser.Posix_character_classContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#anchor.
    def visitAnchor(self, ctx:PCREParser.AnchorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#match_point_reset.
    def visitMatch_point_reset(self, ctx:PCREParser.Match_point_resetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#quoting.
    def visitQuoting(self, ctx:PCREParser.QuotingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#digits.
    def visitDigits(self, ctx:PCREParser.DigitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#digit.
    def visitDigit(self, ctx:PCREParser.DigitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#hex.
    def visitHex(self, ctx:PCREParser.HexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#letters.
    def visitLetters(self, ctx:PCREParser.LettersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#letter.
    def visitLetter(self, ctx:PCREParser.LetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#name.
    def visitName(self, ctx:PCREParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#other.
    def visitOther(self, ctx:PCREParser.OtherContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#utf.
    def visitUtf(self, ctx:PCREParser.UtfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#ucp.
    def visitUcp(self, ctx:PCREParser.UcpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#no_auto_possess.
    def visitNo_auto_possess(self, ctx:PCREParser.No_auto_possessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#no_start_opt.
    def visitNo_start_opt(self, ctx:PCREParser.No_start_optContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#cr.
    def visitCr(self, ctx:PCREParser.CrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#lf.
    def visitLf(self, ctx:PCREParser.LfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#crlf.
    def visitCrlf(self, ctx:PCREParser.CrlfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#anycrlf.
    def visitAnycrlf(self, ctx:PCREParser.AnycrlfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#any.
    def visitAny(self, ctx:PCREParser.AnyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#limit_match.
    def visitLimit_match(self, ctx:PCREParser.Limit_matchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#limit_recursion.
    def visitLimit_recursion(self, ctx:PCREParser.Limit_recursionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#bsr_anycrlf.
    def visitBsr_anycrlf(self, ctx:PCREParser.Bsr_anycrlfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#bsr_unicode.
    def visitBsr_unicode(self, ctx:PCREParser.Bsr_unicodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#accept.
    def visitAccept(self, ctx:PCREParser.AcceptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#fail.
    def visitFail(self, ctx:PCREParser.FailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#mark.
    def visitMark(self, ctx:PCREParser.MarkContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#commit.
    def visitCommit(self, ctx:PCREParser.CommitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#prune.
    def visitPrune(self, ctx:PCREParser.PruneContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#skip.
    def visitSkip(self, ctx:PCREParser.SkipContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PCREParser#then.
    def visitThen(self, ctx:PCREParser.ThenContext):
        return self.visitChildren(ctx)



del PCREParser