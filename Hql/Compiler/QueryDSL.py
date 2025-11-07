from Hql.Exceptions import HqlExceptions as hqle
from typing import Union, Optional, TYPE_CHECKING

from . import Compiler
import logging
import json

if TYPE_CHECKING:
    import Hql
    from Hql.Operators import Operator
    from Hql.Expressions import Expression
    from Hql.Query import Statement
    from Hql.Compiler import BranchDescriptor

class QueryDSLCompiler(Compiler):
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
        self.expr:Union['Expression', None] = None

    def compile(self, src: Union['Expression', 'Operator', 'Statement', None], preprocess: bool = True) -> tuple[Union[object, None], Union[object, None]]:
        if src == None:
            src = self.expr
            preprocess = False

        # still missing a root
        if src == None:
            return '', None

        out = super().compile(src, preprocess=preprocess)
        return out

    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Optional['Operator'], Optional['Operator']]:
        from Hql.Operators import Where
        from Hql.Compiler import BranchDescriptor
        if isinstance(op, BranchDescriptor):
            op = op.get_op()

        acc = None
        rej = op
        
        if isinstance(op, Where):
            acc, rej = self.Where(op, preprocess=True)

        assert not (isinstance(acc, dict) or isinstance(rej, dict))
        return acc, rej

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> tuple[Union[None, 'Hql.Operators.Where', dict], Union[None, 'Hql.Operators.Where', dict]]:
        from Hql.Operators import Where
        from Hql.Expressions import BinaryLogic, Expression

        acc, rej = self.compile(op.expr, preprocess=preprocess)

        if preprocess:
            if acc != None:
                assert isinstance(acc, Expression)
                if self.expr == None:
                    self.expr = acc
                
                elif isinstance(self.expr, BinaryLogic) and self.expr.bitype == 'and':
                    if isinstance(acc, BinaryLogic) and acc.bitype == 'and':
                        self.expr.rh += [acc.lh] + acc.rh
                    else:
                        self.expr.rh.append(acc)

                else:
                    self.expr = BinaryLogic(acc, [self.expr], 'and')
                acc = None

            if rej != None:
                assert isinstance(rej, Expression)
                rej = Where(rej, op.parameters)
        
        assert isinstance(acc, (type(None), Where, dict)) and isinstance(rej, (type(None), Where, dict))
        return acc, rej
        
    def BinaryLogic(self, expr: 'Hql.Expressions.BinaryLogic', preprocess: bool = True) -> tuple[Union[None, 'Hql.Expressions.BinaryLogic', dict], Union[None, 'Hql.Expressions.BinaryLogic']]:
        from Hql.Expressions import BinaryLogic

        if preprocess:
            rejs = []
            accs = []
            for i in [expr.lh] + expr.rh:
                acc, rej = self.compile(i)
                if acc:
                    accs.append(acc)
                if rej:
                    rejs.append(rej)

            # Cannot salvage
            if rejs and expr.bitype == 'or':
                return None, expr

            acc = None
            if accs:
                acc = BinaryLogic(accs[0], accs[1:], bitype=expr.bitype)

            rej = None
            if rejs:
                rej = BinaryLogic(rejs[0], rejs[1:], bitype=expr.bitype)

            return acc, rej

        exprs = []
        for i in [expr.lh] + expr.rh:
            acc, rej = self.compile(i, preprocess=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            exprs.append(acc)

        if len(exprs) == 1:
            ret = exprs[0]
        else:
            if expr.bitype == 'and':
                ret = {
                    'must': exprs
                }
            else:
                ret = {
                    'should': exprs
                }
                
            ret = {
                'bool': ret
            }

        return ret, None

    def Not(self, expr: 'Hql.Expressions.Not', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Not, Expression

        if preprocess:
            acc, rej = self.compile(expr.expr)
            if rej:
                return None, expr
            assert isinstance(acc, Expression)
            return Not(acc), None

        inner, rej = self.compile(expr.expr, preprocess=False)

        if isinstance(inner, dict):
            if 'must' in inner and len(inner) == 1:
                out = {'must_not': inner.pop('must')}
            else:
                out = {'must_not': inner}
        else:
            out = {'must_not': inner}

        out = {'bool': out}

        return out, None

    def Equality(self, expr: 'Hql.Expressions.Equality', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Equality, Expression, Not

        if preprocess:
            # if expr.cs:
            #     logging.warning('Case sensitive comparison in Lucene has inconsistent results')
            #     logging.warning('For compatibility, assuming agnostic')

            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            assert isinstance(acc, Expression)
            lh = acc

            rh = []
            for i in expr.rh:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                rh.append(acc)

            return Equality(lh, expr.op, rh), None

        # wrap in a not statement
        if expr.neq:
            expr.neq = False
            acc, rej = self.Not(Not(expr), preprocess=False)
            return acc, None

        lh, rej = self.compile(expr.lh, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')

        rh = []
        for i in expr.rh:
            acc, rej = self.compile(i, preprocess=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            if isinstance(acc, list):
                rh += acc
            else:
                rh.append(acc)        

        if len(rh) == 1:
            ret = {
                'term': {
                    lh: rh[0]
                }
            }
            return ret, None

        else:
            ret = {
                'terms': {
                    lh: rh
                }
            }
            return ret, None

    # only executes static functions on preprocess and sees if we can handle the result
    def Function(self, expr:'Hql.Functions.Function', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Expression, Regex, StringLiteral, Not

        if expr.name == 'isnull':
            rexpr = Regex(expr.args[0], StringLiteral('.*'))
            rexpr = Not(rexpr)
            return self.compile(rexpr)

        if not expr.static:
            return None, expr

        res = expr.eval(self.ctx)
        assert isinstance(res, Expression)
        acc, rej = self.compile(res, preprocess=True)

        if rej:
            return None, expr

        return acc, None

    def StringLiteral(self, expr: 'Hql.Expressions.StringLiteral', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.quote(''), None

    def MultiString(self, expr: 'Hql.Expressions.MultiString', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        value = expr.eval(self.ctx)
        assert isinstance(value, str)
        value = value.encode('unicode_escape').decode('utf-8')
        return value, None

    def Integer(self, expr: 'Hql.Expressions.Integer', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.value, None

    def Float(self, expr: 'Hql.Expressions.Float', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.value, None

    def Bool(self, expr: 'Hql.Expressions.Bool', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.value, None

    def Datetime(self, expr: 'Hql.Expressions.Datetime', preprocess: bool = True) -> tuple[object, object]:
        import datetime

        if preprocess:
            return expr, None

        dt = expr.value.astimezone(datetime.timezone.utc)
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ"), None

    def Multivalue(self, expr: 'Hql.Expressions.Multivalue', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Multivalue

        exprs = []
        for i in expr.value:
            acc, rej = self.compile(i, preprocess=preprocess)
            if rej:
                return None, expr
            exprs.append(acc)

        if preprocess:
            return Multivalue(exprs), None

        return exprs, None

    def NamedReference(self, expr: 'Hql.Expressions.NamedReference', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            if expr.name == None:
                return None, expr
            return expr, None
        return expr.name, None

    def EscapedNamedReference(self, expr: 'Hql.Expressions.EscapedNamedReference', preprocess: bool = True) -> tuple[object, object]:
        if preprocess:
            if expr.name == None:
                return None, expr
            return expr, None
        return expr.name, None

    def Path(self, expr: 'Hql.Expressions.Path', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Path
        if preprocess:
            parts = []
            for i in expr.path:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                parts.append(acc)
            return Path(parts), None

        parts = []
        for i in expr.path:
            acc, rej = self.compile(i, preprocess=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            assert isinstance(acc, str)
            parts.append(acc)

        return '.'.join(parts), None

    def Relational(self, expr: 'Hql.Expressions.Relational', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Relational, Expression, StringLiteral
        if preprocess:
            if expr.op not in ('<', '>', '<=', '>='):
                return None, expr

            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            lh = acc
            assert isinstance(lh, Expression)

            acc, rej = self.compile(expr.rh[0])
            if rej:
                return None, expr
            rh = acc
            assert isinstance(rh, Expression)

            return Relational(lh, expr.op, [rh]), None

        acc, rej = self.compile(expr.lh, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        lh = acc
        assert isinstance(lh, str)

        acc, rej = self.compile(expr.rh[0], preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        rh = acc
        assert isinstance(rh, (str, int))

        if expr.op == '<':
            op = 'lt'
        elif expr.op == '>':
            op = 'gt'
        elif expr.op == '<=':
            op = 'lte'
        elif expr.op == '>=':
            op = 'gte'
        else:
            raise hqle.CompilerException(f'Precompile did not remove invalid relational expression {expr.op}')

        ret = {
            'range': {
                lh: {
                    op: rh
                }
            }
        }

        return ret, None

    def BetweenEquality(self, expr: 'Hql.Expressions.BetweenEquality', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import BetweenEquality, Expression, BasicRange

        if preprocess:
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

            return BetweenEquality(lh, start, end, op=expr.op), None

        acc, rej = self.compile(expr.lh, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        lh = acc
        assert isinstance(lh, str)

        acc, rej = self.compile(BasicRange(expr.start, expr.end), preprocess=False)
        assert isinstance(acc, dict)

        ret = {
            'range': {
                lh: acc
            }
        }
        if expr.negate:
            ret = {'bool': {'must_not': ret}}

        return ret, None

    def BasicRange(self, expr: 'Hql.Expressions.BasicRange', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import BasicRange, Expression
        if preprocess:
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

        acc, rej = self.compile(expr.start, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        start = acc
        assert isinstance(start, str)

        acc, rej = self.compile(expr.end, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        end = acc
        assert isinstance(end, str)

        return {'gte': start, 'lte': end}, None

    def Regex(self, expr: 'Hql.Expressions.Regex', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Regex, Expression, StringLiteral

        if preprocess:
            # No flags supported
            if expr.m or expr.s or expr.g:
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

            return Regex(lh, rh, i=expr.i), None

        acc, rej = self.compile(expr.lh, preprocess=False)
        if rej:
            raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
        lh = acc
        assert isinstance(lh, str)

        if isinstance(expr.rh, StringLiteral):
            rh = expr.rh.eval(self.ctx, as_str=True)
        else:
            acc, rej = self.compile(expr.rh, preprocess=False)
            if rej:
                raise hqle.CompilerException('Compiling invalid expression, forgot to preprocess?')
            rh = acc
        assert isinstance(rh, str)

        ret = {
            'regexp': {
                lh: {
                    'value': rh,
                    'flags': 'ALL',
                    'case_insensitive': expr.i,
                }
            }
        }

        return ret, None

    def Substring(self, expr: 'Hql.Expressions.Substring', preprocess: bool = True) -> tuple[object, object]:
        from Hql.Expressions import Substring, Expression, StringLiteral, Regex
        from Hql.Expressions import NamedReference, Path
        import re

        if preprocess:
            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            lh = acc
            assert isinstance(lh, (NamedReference, Path))

            rhs = []
            for i in expr.rh:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                rh = acc
                rhs.append(rh)

            return Substring(lh, expr.op, rhs), None

        exprs = []
        for i in expr.rh:
            if isinstance(i, StringLiteral):
                rh = i.eval(self.ctx, as_str=True)
            else:
                acc, rej = self.compile(i, preprocess=False)
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
            
            acc, rej = self.Regex(Regex(expr.lh, rh), preprocess=False)
            exprs.append(acc)

        if 'all' in expr.op:
            op = 'must'
        else:
            op = 'should'

        if len(exprs) == 1:
            ret = exprs[0]
        
        else:
            ret = {
                op: exprs
            }

        if expr.neq:
            if 'must' in ret:
                ret['must_not'] = ret.pop('must')
            else:
                ret = {
                    'must_not': ret
                }

        if len(exprs) > 1:
            ret = {
                'bool': ret
            }

        return ret, None
