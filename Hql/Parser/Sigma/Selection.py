from typing import TYPE_CHECKING, Union

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions.Functions import FuncExpr

if TYPE_CHECKING:
    import Hql.Expressions as Expr

class Selection():
    def __init__(self, selection:Union[list, dict], name:str=''):
        from Hql.Context import Context
        from Hql.Data import Data

        self.faux_ctx = Context(Data())

        self.name = name
        self.selection = selection
        self.fields = []

    def build_selection(self):
        from Hql.Expressions import BinaryLogic
        exprs = []

        if isinstance(self.selection, list):
            op = 'or'
            for i in self.selection:
                expr = Selection(i).build_selection()
                exprs.append(expr)

        else:
            op = 'and'
            for i in self.selection:
                expr = self.process_field(i, self.selection[i])
                exprs.append(expr)

        if len(exprs) == 1:
            return exprs[0]

        return BinaryLogic(exprs[0], exprs[1:], op)

    def to_literal_object(self, value, modifiers:list[str]):
        from Hql.Expressions.Literals import StringLiteral, Integer, Float
        
        if isinstance(value, str):
            value = repr(value)
            lquote = value[0]
            value = value[1:-1]
            expr = StringLiteral(value, lquote=lquote, rquote=lquote, sanitized=True)

        elif isinstance(value, int):
            expr = Integer(value)

        elif isinstance(value, float):
            expr = Float(value)
        
        else:
            raise hqle.CompilerException(f'Unhandled literal object type {type(value)} in Sigma parse')

        if 'base64' in modifiers:
            expr = FuncExpr('base64', [expr])

        elif 'base64offset' in modifiers:
            expr = FuncExpr('base64offset', [expr])

        return expr

    def substring(self, lh:'Expr.NamedReference', modifiers:list, rh):
        from Hql.Expressions.Logic import Substring
        rh_list = True
        if not isinstance(rh, list):
            rh_list = False
            rh = [rh]

        exprs = []
        for i in rh:
            exprs.append(self.to_literal_object(i, modifiers))

        if 'contains' in modifiers:
            if 'all' in modifiers:
                op = 'contains_all'
            elif rh_list:
                op = 'contains_any'
            else:
                op = 'contains'

        elif 'endswith' in modifiers:
            op = 'endswith'

        else:
            op = 'startswith'

        op += '_cs' if 'cased' in modifiers else ''
        return Substring(lh, op, exprs)

    def cidr(self, name:'Expr.NamedReference', field:list):
        from Hql.Expressions import Equality

        exprs = []
        for i in field:
            expr = self.to_literal_object(i, [])
            if ':' in field:
                expr = FuncExpr('ip6subnet', [expr]).eval(self.faux_ctx)
            else:
                expr = FuncExpr('ip4subnet', [expr]).eval(self.faux_ctx)

            exprs.append(expr)

        if len(field) == 1:
            return Equality(name, '==', exprs)
        else:
            return Equality(name, 'in', exprs)

    def relational(self, name:'Expr.NamedReference', modifiers:list[str], field:list):
        from Hql.Expressions import Relational

        exprs = []
        for i in field:
            exprs.append(self.to_literal_object(i, modifiers))

        if 'lt' in modifiers:
            op = '<'
        elif 'lte' in modifiers:
            op = '<='
        elif 'gt' in modifiers:
            op = '>'
        elif 'gte' in modifiers:
            op = '>='
        else:
            raise hqle.CompilerException(f'What? invalid relational expression {modifiers}')

        return Relational(name, op, exprs)

    def fieldref(self, name:'Expr.NamedReference', field:list):
        from Hql.Expressions import NamedReference, Equality

        exprs = []
        for i in field:
            exprs.append(NamedReference(i))

        if len(exprs) == 1:
            return Equality(name, '==', exprs)
        else:
            return Equality(name, 'in', exprs)

    def regex(self, name:'Expr.NamedReference', modifiers:list[str], field:list):
        from Hql.Expressions import Regex
        from Hql.Expressions import BinaryLogic

        patterns = []
        for i in field:
            patterns.append(self.to_literal_object(i, modifiers))
        
        exprs = []
        for i in patterns:
            expr = Regex(name, i)

            expr.i = 'i' in modifiers
            expr.m = 'm' in modifiers
            expr.s = 's' in modifiers

            exprs.append(expr)

        return BinaryLogic(name, exprs, 'or')

    def equality(self, name:'Expr.NamedReference', field:list):
        from Hql.Expressions import Equality

        rhs = []
        for i in field:
            rhs.append(self.to_literal_object(i, []))

        return Equality(name, 'in', rhs)

    def process_field(self, field_name:str, field):
        import Hql.Expressions as Expr

        if not isinstance(field, list):
            field = [field]

        name = field_name.split('|')

        lh = Expr.NamedReference(name[0])
        modifiers = name[1:]

        if 'exists' in modifiers:
            expr = Expr.FuncExpr('exists', [lh]).eval(self.faux_ctx)
            if not field:
                expr = Expr.FuncExpr('not', [expr]).eval(self.faux_ctx)
            return expr

        for i in ['contains', 'endswith', 'startswith']:
            if i in modifiers:
                return self.substring(lh, modifiers, field)

        if 'cidr' in modifiers:
            return self.cidr(lh, field)

        if 'fieldref' in modifiers:
            return self.fieldref(lh, field)

        for i in ['gte', 'lte', 'lt', 'lte']:
            if i in modifiers:
                return self.relational(lh, modifiers, field)

        if 're' in modifiers:
            return self.regex(lh, modifiers, field)

        return self.equality(lh, field)
