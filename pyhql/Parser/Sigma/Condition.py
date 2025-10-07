from typing import TYPE_CHECKING
from antlr4 import CommonTokenStream, InputStream
from .grammar.SigmaLexer import SigmaLexer
from .grammar.SigmaParser import SigmaParser
from .grammar.SigmaVisitor import SigmaVisitor
from fnmatch import fnmatch

if TYPE_CHECKING:
    from . import Selection

class Condition():
    def __init__(self, text:str, selections:list['Selection']):
        self.text = text
        self.selections = selections
        self.tree = self.parse()

    def get_sel(self, name:str) -> list['Selection']:
        matches = []
        for i in self.selections:
            if fnmatch(i.name, name):
                matches.append(i)
        return matches

    def parse(self):
        lexer = SigmaLexer(InputStream(self.text))
        token_stream = CommonTokenStream(lexer)
        parser = SigmaParser(token_stream)
         
        return parser.condition()

    def assemble(self):
        visitor = Visitor(self)
        self.assembly = visitor.visit(self.tree)
        return self.assembly

class Visitor(SigmaVisitor):
    def __init__(self, condition:Condition):
        self.condition = condition

    def visitCondition(self, ctx: SigmaParser.ConditionContext):
        return self.visit(ctx.Statement)

    def visitOrStatement(self, ctx: SigmaParser.OrStatementContext):
        from Hql.Expressions import BinaryLogic

        lh = self.visit(ctx.Left)

        rh = []
        for i in ctx.Right:
            rh.append(self.visit(i))

        if not rh:
            return lh

        return BinaryLogic(lh, rh, 'or')

    def visitAndStatement(self, ctx: SigmaParser.AndStatementContext):
        from Hql.Expressions import BinaryLogic

        lh = self.visit(ctx.Left)

        rh = []
        for i in ctx.Right:
            rh.append(self.visit(i))

        if not rh:
            return lh

        return BinaryLogic(lh, rh, 'and')

    def visitNotStatement(self, ctx: SigmaParser.NotStatementContext):
        from Hql.Expressions import FuncExpr

        if ctx.Bracket:
            inner = self.visit(ctx.Bracket)
        else:
            inner = self.visit(ctx.Selection)

        return FuncExpr('not', [inner])

    def visitBracketStatement(self, ctx: SigmaParser.BracketStatementContext):
        return self.visit(ctx.Statement)

    def visitOfStatement(self, ctx: SigmaParser.OfStatementContext):
        from Hql.Expressions import BinaryLogic

        specifier = self.visit(ctx.Specifier)

        if specifier == '1':
            op = 'or'
        elif specifier == 'all':
            op = 'and'
        else:
            raise Exception(f'Invalid of specifier {specifier}')

        target = self.visit(ctx.Target)

        if len(target) == 1:
            return target[0].build_selection()
        else:
            target = [x.build_selection() for x in target]
            return BinaryLogic(target[0], target[1:], op)

    def visitOfSpecifier(self, ctx: SigmaParser.OfSpecifierContext):
        if ctx.Int:
            return ctx.Int.text

        if ctx.All:
            return ctx.All.text

    def visitOfTarget(self, ctx: SigmaParser.OfTargetContext) -> list['Selection']:
        # pattern or 'them'
        # 'them' means all selections
        if ctx.Pattern:
            pat = self.visit(ctx.Pattern)
        else:
            pat = '*'

        target = self.condition.get_sel(pat)

        if not target:
            raise Exception(f'Specifier {pat} matches nothing')

        return target

    def visitSelectionIdentifier(self, ctx: SigmaParser.SelectionIdentifierContext):
        if ctx.Basic:
            identifier = self.visit(ctx.Basic)
            return self.condition.get_sel(identifier)[0].build_selection()

        else:
            return None

    def visitPatternIdentifier(self, ctx: SigmaParser.PatternIdentifierContext):
        return self.visit(ctx.Wildcard)

    def visitWildcardIdentifier(self, ctx: SigmaParser.WildcardIdentifierContext):
        if ctx.Identifier:
            return ctx.Identifier.text

    def visitBasicIdentifier(self, ctx: SigmaParser.BasicIdentifierContext):
        if ctx.Identifier:
            return ctx.Identifier.text
