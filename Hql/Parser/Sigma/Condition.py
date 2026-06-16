from typing import TYPE_CHECKING
from antlr4 import CommonTokenStream, InputStream
from .grammar.SigmaLexer import SigmaLexer
from .grammar.SigmaParser import SigmaParser
from .grammar.SigmaVisitor import SigmaVisitor
from fnmatch import fnmatch

if TYPE_CHECKING:
    from . import Selection
    from Hql.Expressions.References import NamedReference

class Condition():
    def __init__(self, text:str, selections:list['Selection']):
        self.text = text
        self.selections = selections
        self.tree = self.parse()

    def get_sel(self, name:str) -> list['NamedReference']:
        from Hql.Expressions.References import NamedReference

        matches = []
        for i in self.selections:
            if fnmatch(i.name, name):
                matches.append(NamedReference(i.name))

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
        from Hql.Expressions.Logic import BinaryLogic

        exprs = [self.visit(ctx.Left)]
        for i in ctx.Right:
            exprs.append(self.visit(i))

        return BinaryLogic(exprs, logic_and=False)

    def visitAndStatement(self, ctx: SigmaParser.AndStatementContext):
        from Hql.Expressions.Logic import BinaryLogic

        exprs = [self.visit(ctx.Left)]
        for i in ctx.Right:
            exprs.append(self.visit(i))

        return BinaryLogic(exprs, logic_and=True)

    def visitNotStatement(self, ctx: SigmaParser.NotStatementContext):
        from Hql.Expressions.Functions import FuncExpr
        from Hql.Expressions.References import NamedReference
        inner = self.visit(ctx.Statement)
        return FuncExpr(NamedReference('not'), [inner])

    def visitBracketStatement(self, ctx: SigmaParser.BracketStatementContext):
        return self.visit(ctx.Statement)

    def visitOfStatement(self, ctx: SigmaParser.OfStatementContext):
        from Hql.Expressions.Logic import BinaryLogic

        specifier = self.visit(ctx.Specifier)

        if specifier == '1':
            logic_and = False
        elif specifier == 'all':
            logic_and = True
        else:
            raise Exception(f'Invalid of specifier {specifier}')

        target = [x.build_selection() for x in self.visit(ctx.Target)]
        return BinaryLogic(target, logic_and)

    def visitOfSpecifier(self, ctx: SigmaParser.OfSpecifierContext):
        if ctx.Int:
            return ctx.Int.text

        if ctx.All:
            return ctx.All.text

    def visitOfTarget(self, ctx: SigmaParser.OfTargetContext) -> list['NamedReference']:
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
            return self.condition.get_sel(identifier)[0]
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
