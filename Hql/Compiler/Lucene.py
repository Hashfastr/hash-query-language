from __future__ import annotations
from Hql.Exceptions import HqlExceptions as hqle
from typing import Union, Optional, TYPE_CHECKING

from . import Compiler
import logging
import datetime

from Hql.Expressions import Literals
from Hql.Expressions import Logic
from Hql.Expressions import References
import Hql.Operators as Operators
from Hql.Compiler import BranchDescriptor

if TYPE_CHECKING:
    from Hql.Operators.Operator import Operator
    from Hql.Expressions import Expression
    from Hql.Query import Statement

class LuceneCompiler(Compiler):
    def __init__(self) -> None:
        Compiler.__init__(self)
        self.attrs = {
            'nested_objects': True,
            'wildcards': True,
            'wildcard_names': True,
            'complex_names': True,
            'row_reducing': True,
            'regex_matching': True,
            'regex_insensitive': False,
            'regex_multiline': False,
            'regex_dotall': False,
            'regex_global': False
        }
        self.expr:Union[Logic.Logic, None] = None

    def compile(self, src: Union[Expression, Operator, Statement, None], prep:bool=True) -> tuple[Union[object, None], Union[object, None]]:
        if src == None or self.expr:
            return self.Bool(Literals.Bool(True), prep=False)

        return super().compile(src, prep=prep)

    def add_op(self, op:Union[Operator, BranchDescriptor]) -> tuple[Optional[Operator], Optional[Operator]]:
        if isinstance(op, BranchDescriptor):
            op = op.get_op()

        acc = None
        rej = op
        
        if isinstance(op, Operators.Where):
            acc, rej = self.Where(op, prep=True)

        assert not (isinstance(acc, str) or isinstance(rej, str))
        return acc, rej

    def Where(self, op:Operators.Where, prep:bool=True) -> tuple[Union[None, Operators.Where, str], Union[None, Operators.Where, str]]:
        acc, rej = self.compile(op.expr, prep=prep)

        if prep:
            if acc != None:
                assert isinstance(acc, Logic.Logic)

                # Add the logic to the running expression for this compiler
                if self.expr == None:
                    self.expr = acc
                else:
                    self.expr = Logic.BinaryLogic([acc, self.expr])
                
                acc = None

            if rej != None:
                assert isinstance(rej, Logic.Logic)
                rej = Operators.Where(rej, op.parameters)
        
        assert isinstance(acc, (type(None), Operators.Where, str)) and isinstance(rej, (type(None), Operators.Where, str))
        return acc, rej
        
    def BinaryLogic(self, expr: Logic.BinaryLogic, prep:bool=True) -> tuple[Union[None, Logic.Logic, str], Union[None, Logic.Logic, str]]:
        if prep:
            rejs = []
            accs = []
            for i in expr.exprs:
                acc, rej = self.compile(i)
                if acc:
                    accs.append(acc)
                if rej:
                    rejs.append(rej)

            # Cannot salvage
            if rejs and not expr.logic_and:
                return None, expr

            acc = None
            if accs:
                acc = Logic.BinaryLogic(accs, expr.logic_and)

            rej = None
            if rejs:
                rej = Logic.BinaryLogic(rejs, expr.logic_and)

            assert isinstance(acc, (type(None), Logic.Logic)) and isinstance(rej, (type(None), Logic.Logic))
            return acc, rej

        exprs = []
        for i in expr.exprs:
            acc, rej = self.compile(i, prep=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            exprs.append(acc)

        bitok = ' AND' if expr.logic_and else ' OR '
        ret = bitok.join(exprs)
        return f'({ret})', None

    def Not(self, expr: Logic.Not, prep:bool=True) -> tuple[object, object]:
        if prep:
            acc, rej = self.compile(expr.expr)
            if rej:
                return None, expr
            assert isinstance(acc, Logic.Logic)
            return Logic.Not(acc), None

        inner, rej = self.compile(expr.expr, prep=False)
        return f'(NOT {inner})', None

    def Equality(self, expr: Logic.Equality, prep:bool=True) -> tuple[object, object]:
        if prep:
            if expr.cs:
                logging.warning('Case sensitive comparison in Lucene has inconsistent results')
                logging.warning('For compatibility, assuming agnostic')

            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            assert isinstance(acc, References.Reference)
            lh = acc

            rh = []
            for i in expr.rh:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr

                # handles multivalues
                if isinstance(acc, list):
                    rh += acc
                else:
                    rh.append(acc)

            return Logic.Equality(lh, rh, expr.cs, expr.neq), None

        lh, rej = self.compile(expr.lh, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')

        rh = []
        for i in expr.rh:
            acc, rej = self.compile(i, prep=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            rh.append(acc)
        
        eqs = [f'{lh}:{x}' for x in rh]
        ret = ' OR '.join(eqs)
        if len(eqs) > 1:
            ret = f'({ret})'

        return f'(NOT {ret})' if expr.neq else ret, None

    # only executes static functions on preprocess and sees if we can handle the result
    def Function(self, expr:Hql.Functions.Function, prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Expression, Regex, StringLiteral, Not

        if expr.name == 'isnull':
            rexpr = Regex(expr.args[0], StringLiteral('.*'))
            rexpr = Not(rexpr)
            return self.compile(rexpr)

        if not expr.static:
            return None, expr

        res = expr.eval(self.ctx)
        assert isinstance(res, Expression)
        acc, rej = self.compile(res, prep=True)

        if rej:
            return None, expr

        return acc, None

    def StringLiteral(self, expr: Literals.StringLiteral, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        return expr.quote('"'), None

    def MultiString(self, expr: Literals.MultiString, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        value = expr.quote('"')
        return f'{value}', None

    def Integer(self, expr: Literals.Integer, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        return f'{expr.value}', None

    def Float(self, expr: Literals.Float, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        return f'{expr.value}', None

    def Bool(self, expr: Literals.Bool, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        val = 'True' if expr.value else 'False'
        return val, None

    def Datetime(self, expr: Literals.Datetime, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        dt = expr.value.astimezone(datetime.timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ"), None

    def Multivalue(self, expr: Literals.Multivalue, prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions.Literals import Multivalue

        exprs = []
        for i in expr.value:
            acc, rej = self.compile(i, prep=prep)
            if rej:
                return None, expr
            exprs.append(acc)

        if prep:
            return Multivalue(exprs), None

        return exprs, None

    def NamedReference(self, expr: References.NamedReference, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        return expr.name, None

    def EscapedNamedReference(self, expr: References.EscapedNamedReference, prep:bool=True) -> tuple[object, object]:
        if prep:
            return expr, None
        return f'{expr.name}', None

    def Path(self, expr: References.Path, prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions.References import Path
        if prep:
            return expr, None

        parts = []
        for i in expr.path:
            acc, rej = self.compile(i, prep=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            assert isinstance(acc, str)
            parts.append(acc)

        return '.'.join(parts), None

    def Relational(self, expr: Logic.Relational, prep:bool=True) -> tuple[object, object]:
        if prep:
            acc, rej = self.compile(expr.rh[0])
            if rej:
                return None, expr
            rh = acc
            assert isinstance(rh, Expression)

            return Logic.Relational(expr.lh, rh, expr.gt, expr.eq), None

        acc, rej = self.compile(expr.lh, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        lh = acc
        assert isinstance(lh, str)

        acc, rej = self.compile(expr.rh[0], prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        rh = acc
        assert isinstance(rh, str)

        op =  '>' if expr.gt else '<'
        op += '=' if expr.eq else ''

        return f'{lh}:{op}{rh}', None

    def BetweenEquality(self, expr: Logic.BetweenEquality, prep:bool=True) -> tuple[object, object]:
        if prep:
            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            lh = acc
            assert isinstance(lh, Expression)

            acc, rej = self.compile(expr.start)
            if rej:
                return None, expr
            start = acc
            assert isinstance(start, Expression)

            acc, rej = self.compile(expr.end)
            if rej:
                return None, expr
            end = acc
            assert isinstance(end, Expression)

            return Logic.BetweenEquality(lh, start, end, op=expr.op), None

        acc, rej = self.compile(expr.lh, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        lh = acc
        assert isinstance(lh, str)

        acc, rej = self.compile(expr.start, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        start = acc
        assert isinstance(start, str)

        acc, rej = self.compile(expr.end, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        end = acc
        assert isinstance(end, str)

        ret = f'{lh}:[{start} TO {end}]'
        if expr.negate:
            ret = f'(NOT {ret})'

        return ret, None

    def BasicRange(self, expr: Hql.Expressions.BasicRange, prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions.Logic import BasicRange, Expression
        if prep:
            acc, rej = self.compile(expr.start)
            if rej:
                return None, expr
            start = acc
            assert isinstance(start, Expression)

            acc, rej = self.compile(expr.end)
            if rej:
                return None, expr
            end = acc
            assert isinstance(end, Expression)

            return BasicRange(start, end), None

        acc, rej = self.compile(expr.start, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        start = acc
        assert isinstance(start, str)

        acc, rej = self.compile(expr.end, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        end = acc
        assert isinstance(end, str)

        return f'[{start} TO {end}]', None

    def Regex(self, expr: Hql.Expressions.Regex, prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions.Logic import Regex, Expression, StringLiteral

        if prep:
            # No flags supported
            if expr.i or expr.m or expr.s or expr.g:
                return None, expr

            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            lh = acc
            assert isinstance(lh, Expression)

            acc, rej = self.compile(expr.rh)
            if rej:
                return None, expr
            rh = acc
            assert isinstance(rh, Expression)

            return Regex(lh, rh), None

        acc, rej = self.compile(expr.lh, prep=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        lh = acc
        assert isinstance(lh, str)

        if isinstance(expr.rh, StringLiteral):
            rh = expr.rh.eval(self.ctx, as_str=True)
        else:
            acc, rej = self.compile(expr.rh, prep=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            rh = acc
        assert isinstance(rh, str)
        rh = rh.replace('/', '\\/')

        return f'{lh}:/{rh}/', None

    def Substring(self, expr: Hql.Expressions.Substring, prep:bool=True) -> tuple[object, object]:
        from Hql.Expressions.Logic import Substring, Expression, StringLiteral, Regex
        from Hql.Expressions.References import Path, NamedReference
        import re

        if prep:
            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            lh = acc
            assert isinstance(lh, (Path, NamedReference))

            rhs = []
            for i in expr.rh:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                rh = acc
                rhs.append(rh)

            return Substring(lh, expr.op, rhs), None

        # acc, rej = self.compile(expr.lh, prep=False)
        # if rej:
        #     raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        # lh = acc
        # assert isinstance(lh, str)

        exprs = []
        for i in expr.rh:
            if isinstance(i, StringLiteral):
                rh = i.eval(self.ctx, as_str=True)
            else:
                acc, rej = self.compile(i, prep=False)
                if rej:
                    raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
                rh = acc
            assert isinstance(rh, str)
            
            if 'startswith' in expr.op or 'prefix' in expr.op:
                rh = f'{rh}.*'
            elif 'endswith' in expr.op or 'suffix' in expr.op:
                rh = f'.*{rh}'
            else:
                rh = f'.*{rh}.*'
            rh = StringLiteral(rh, verbatim=True)
            
            acc, rej = self.Regex(Regex(expr.lh, rh), prep=False)
            exprs.append(acc)

        if 'all' in expr.op:
            ret = ' AND '.join(exprs)
        else:
            ret = ' OR '.join(exprs)

        if len(exprs) > 1:
            ret = f'({ret})'

        if expr.neq:
            ret = f'NOT {ret}'

        return ret, None
