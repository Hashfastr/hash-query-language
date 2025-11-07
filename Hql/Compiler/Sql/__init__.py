from typing import Optional, Union, TYPE_CHECKING, Callable, override

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
import logging

from Hql.Expressions.Logic import Equality

from .Statements import SqlStatement, SELECT
from .Expressions import SqlExpression, Like

from ..Compiler import Compiler

if TYPE_CHECKING:
    from Hql.Compiler import BranchDescriptor, InstructionSet
    from Hql.Operators import Operator
    from Hql.Operators.Database import Database
    from Hql.Query import Statement
    import Hql

'''
Generic SQL compiler
'''
class SqlCompiler(Compiler):
    def __init__(self, parent:Optional['Database']=None):
        from Hql.Data import Data
        from Hql.Compiler import HqlCompiler
        from Hql.Config import Config
        from Hql.Expressions import Wildcard
        self.type = self.__class__.__name__
        self.ctx = Context(Data())
        self.vestigial_compiler = HqlCompiler(Config())

        self.statement:SqlStatement = SELECT(Wildcard('*'))
        self.parent = parent

        self.joins = False

    def from_name(self, name:str) -> Callable:
        if hasattr(self, name):
            return getattr(self, name)
        raise hqle.CompilerException(f'Attempting to get non-existant compiler function for {name}')

    @override
    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Optional[SqlStatement], Optional['Operator']]:
        from Hql.Compiler import BranchDescriptor
        from Hql.Operators import Operator, Join

        if isinstance(op, BranchDescriptor):
            op = op.get_op()

        acc, rej = self.compile(op)
        assert isinstance(rej, (Operator, type(None)))
        assert isinstance(acc, (SqlStatement, type(None)))
        return acc, rej
    
    def add_ops(self, ops:list['BranchDescriptor']) -> Optional[list['Operator']]:
        for idx, op in enumerate(ops):
            acc, rej = self.add_op(op)
            if rej:
                return [rej] + [x.get_op() for x in ops[idx+1:]]
        return None

    def optimize(self, ops: list['BranchDescriptor']) -> list['BranchDescriptor']:
        return ops

    '''
    You'll want to replace this with something like a string that you'll query your database with.
    Default returns optimized operators for running in Hql-land
    '''
    def compile(self, src:Union['Hql.Expressions.Expression', 'Operator', 'Statement', None], preprocess:bool=True) -> tuple[Optional[object], Optional[object]]:
        if src == None:
            compiled = self.statement.compile(self)
            compiled += ';'
            return compiled, None
        return self.from_name(src.type)(src, preprocess=preprocess)

    def decompile(self) -> str:
        from Hql.Expressions import PipeExpression
        logging.critical("Decompilation doesn't actually work right now, sorry")
        # return PipeExpression(pipes=self.ops).decompile(self.ctx)
        return ''

    '''
    By default, all of these return themselves as they are being
    'rejected' back to the compiler
    '''

    '''
    Operators
    '''

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Operators import Where
        from Hql.Expressions import Expression, BinaryLogic

        if preprocess:
            acc, rej = self.compile(op.expr)
            if rej:
                return None, op
            assert isinstance(acc, Expression)
            op = Where(acc)

            if not isinstance(self.statement, SELECT):
                self.statement = SELECT(self.statement)

            if not self.statement.where:
                self.statement.where = op
                return self.statement, None

            if not isinstance(self.statement.where.expr, BinaryLogic) or self.statement.where.expr.bitype == 'or':
                self.statement.where.expr = BinaryLogic(self.statement.where.expr, [], 'and')

            self.statement.where.expr.rh.append(op.expr)

            return self.statement, None

        return self.compile(op.expr, preprocess=False)

    def Project(self, op:'Hql.Operators.Project', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Operators import Project
        from Hql.Expressions import Expression
        
        if preprocess:
            exprs = []
            for i in op.exprs:
                acc, rej = self.compile(i)
                if rej:
                    return None, op
                assert isinstance(acc, Expression)
                exprs.append(acc)

            op = Project('project', exprs)

            if not isinstance(self.statement, SELECT):
                self.statement = SELECT(self.statement)

            if not self.statement.project:
                self.statement.project = op
                return self.statement, None
            else:
                self.statement = SELECT(src=self.statement, project=op)
                return self.statement, None

        exprs = set()
        for i in op.exprs:
            acc, _ = self.compile(i, preprocess=False)
            assert isinstance(acc, str)
            exprs.add(acc)

        return ', '.join(list(exprs)), None

    def ProjectAway(self, op:'Hql.Operators.ProjectAway', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def ProjectRename(self, op:'Hql.Operators.ProjectRename', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Take(self, op:'Hql.Operators.Take', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            if op.tables:
                return None, op
            else:
                if not isinstance(self.statement, SELECT):
                    self.statement = SELECT(self.statement)
                self.statement.limit = op
                return self.statement, None

        return self.compile(op.expr, preprocess=False)

    def Count(self, op:'Hql.Operators.Count', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Extend(self, op:'Hql.Operators.Extend', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Range(self, op:'Hql.Operators.Range', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Top(self, op:'Hql.Operators.Top', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Unnest(self, op:'Hql.Operators.Unnest', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Union(self, op:'Hql.Operators.Union', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Summarize(self, op:'Hql.Operators.Summarize', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Datatable(self, op:'Hql.Operators.Datatable', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Join(self, op:'Hql.Operators.Join', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Compiler import InstructionSet

        if preprocess:
            if self.parent == None:
                return None, op

            if not isinstance(op.rh, InstructionSet) or len(op.rh.upstream) > 1 or op.rh.ops:
                return None, op
            
            rh = op.rh.upstream[0]
            if rh != self.parent:
                return None, op

            accepted_kinds = [
                'inner',
                'leftouter', 'left', 'leftanti',
                'rightouter', 'right', 'rightanti',
                'fullouter'
            ]

            if op.kind not in accepted_kinds:
                return None, op

            if not isinstance(self.statement, SELECT):
                self.statement = SELECT(self.statement)
            self.statement.add_join(op)

            return self.statement, None

        return None, None

    def MvExpand(self, op:'Hql.Operators.MvExpand', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Sort(self, op:'Hql.Operators.Sort', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Rename(self, op:'Hql.Operators.Rename', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    '''
    Expressions
    '''

    def Tabular(self, expr:'Hql.Expressions.Expression') -> tuple[Optional['InstructionSet'], Optional['Hql.Expressions.Expression']]:
        return None, expr

    def PipeExpression(self, expr:'Hql.Expressions.PipeExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def OpParameter(self, expr:'Hql.Expressions.OpParameter', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def ToClause(self, expr:'Hql.Expressions.ToClause', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def OrderedExpression(self, expr:'Hql.Expressions.OrderedExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def ByExpression(self, expr:'Hql.Expressions.ByExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Function(self, expr:'Hql.Functions.Function', preprocess:bool=True, negate:bool=False) -> tuple[object, object]:
        if expr.name == 'isnull':
            if preprocess:
                acc, rej = self.compile(expr.args[0])
                if rej:
                    return None, expr
                expr.args[0] = acc
                return expr, None
            lh, _ = self.compile(expr.args[0], preprocess=False)
            if negate:
                return f'{lh} NOTNULL', None
            else:
                return f'{lh} ISNULL', None

        return None, expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Equality(self, expr:'Hql.Expressions.Equality', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Equality, Expression

        if preprocess:
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

        lh, _ = self.compile(expr.lh, preprocess=False)

        rh = []
        for i in expr.rh:
            acc, _ = self.compile(i, preprocess=False)
            if isinstance(acc, list):
                rh += acc
            else:
                rh.append(acc)
        
        if len(rh) == 1:
            op = '!=' if expr.neq else '='
            val = f'{lh} {op} {rh[0]}'
            if not expr.cs:
                val += ' COLLATE NOCASE'
            return val, None

        op = 'NOT IN' if expr.neq else 'IN'
        rh = ','.join(rh)
        val = f'{lh} {op} ({rh})'
        if not expr.cs:
            val += ' COLLATE NOCASE'

        return val, None

    def Substring(self, expr:'Hql.Expressions.Substring', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Substring, NamedReference
        from Hql.Expressions import Integer, Float, StringLiteral
        from Hql.Expressions import Regex

        if preprocess:
            if expr.term:
                logging.warning('SQL has no support for term matching, no performance benefit provided')

            acc, rej = self.compile(expr.lh)
            if rej:
                return None, expr
            lh = acc
            assert isinstance(lh, NamedReference)

            rh = []
            for i in expr.rh:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                rh.append(acc)

            expr = Substring(lh, expr.op, rh)
            return expr, None

        lh, _ = self.compile(expr.lh, preprocess=False)

        exprs = []
        for i in expr.rh:
            if expr.cs:
                rh = StringLiteral('.*' + i.value.decode('utf-8') + '.*', verbatim=i.verbatim)
                regex = Regex(expr.lh, rh)
                val, _ = self.compile(regex, preprocess=False)
                exprs.append(val)

            else:
                rh = StringLiteral('%' + i.value.decode('utf-8') + '%', verbatim=i.verbatim)
                val, _ = self.compile(rh, preprocess=False)
                exprs.append(f'{lh} LIKE {val}')
        op = ' AND ' if expr.logic_and else ' OR '

        val = op.join(exprs)
        return val, None

    def Relational(self, expr:'Hql.Expressions.Relational', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Literal, NamedReference, BetweenEquality

        if preprocess:
            acc, rej = self.compile(expr.lh)
            if rej or not isinstance(acc, NamedReference):
                return None, expr
            lh = acc

            acc, rej = self.compile(expr.start)
            if rej or not isinstance(acc, Literal):
                return None, expr
            start = acc

            acc, rej = self.compile(expr.end)
            if rej or not isinstance(acc, Literal):
                return None, expr
            end = acc
            
            return BetweenEquality(lh, start, end, expr.op), None

        lh, _ = self.compile(expr.lh, preprocess=False)
        start, _ = self.compile(expr.start, preprocess=False)
        end, _ = self.compile(expr.end, preprocess=False)

        val = f'{lh} BETWEEN {start} AND {end}'
        return val, None

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import BinaryLogic

        if preprocess:
            accs = []
            rejs = []
            for i in [expr.lh] + expr.rh:
                acc, rej = self.compile(i)
                if rej and expr.bitype == 'and':
                    rejs.append(rej)
                elif rej and expr.bitype == 'or':
                    return None, expr
                elif acc:
                    accs.append(acc)

            if rejs:
                rej = BinaryLogic(rejs[0], rejs[1:], bitype='and')
            else:
                rej = None

            if accs:
                acc = BinaryLogic(accs[0], accs, bitype=expr.bitype)
            else:
                acc = None
            
            return acc, rej

        exprs = []
        for i in [expr.lh] + expr.rh:
            acc, _ = self.compile(i, preprocess=False)
            assert isinstance(acc, str)
            if isinstance(i, BinaryLogic):
                acc = '(' + acc + ')'
            exprs.append(acc)
        op = ' AND ' if expr.bitype == 'and' else ' OR '

        return op.join(exprs), None

    def Not(self, expr:'Hql.Expressions.Not', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Functions import Function
        from Hql.Expressions import Expression
        if preprocess:
            acc, rej = self.compile(expr.expr)
            if rej:
                return None, expr
            assert isinstance(acc, Expression)
            expr.expr = acc
            return expr, None

        val, _ = self.compile(expr.expr, preprocess=False)
        assert isinstance(val, str)
        
        # quick optimization
        if isinstance(expr.expr, Function) and expr.expr.name == 'isnull':
            val, _ = self.Function(expr.expr, preprocess=False, negate=True)

        else:
            val = f'NOT {val}'

        return val, None

    def BasicRange(self, expr:'Hql.Expressions.BasicRange', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Regex(self, expr:'Hql.Expressions.Regex', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import NamedReference, StringLiteral, Regex

        if preprocess:
            acc, rej = self.compile(expr.lh)
            if rej or not isinstance(acc, NamedReference):
                return None, expr
            lh = acc

            acc, rej = self.compile(expr.rh)
            if rej:
                return None, expr
            assert isinstance(acc, StringLiteral)
            rh = acc
            
            return Regex(lh, rh, expr.i, expr.m, expr.s, expr.g), None

        lh, _ = self.compile(expr.lh, preprocess=False)
        assert isinstance(lh, str)

        rh, _ = self.compile(expr.rh, preprocess=False)
        assert isinstance(rh, str)

        val = f'{lh} REGEXP {rh}'

        return val, None

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.quote("'"), None
    
    def MultiString(self, expr:'Hql.Expressions.MultiString', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Integer(self, expr:'Hql.Expressions.Integer', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return str(expr.value), None

    def IP4(self, expr:'Hql.Expressions.IP4', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Float(self, expr:'Hql.Expressions.Float', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return str(expr.value), None

    def Bool(self, expr:'Hql.Expressions.Bool', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        val = 'TRUE' if expr.value else 'FALSE'
        return val, None

    def Multivalue(self, expr:'Hql.Expressions.Multivalue', preprocess:bool=True) -> tuple[object, object]:
        return None, expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.name, None

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Keyword(self, expr:'Hql.Expressions.Keyword', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Identifier(self, expr:'Hql.Expressions.Identifier', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Path(self, expr:'Hql.Expressions.Path', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import NamedReference, Path

        if preprocess:
            path = []
            for i in expr.path:
                acc, rej = self.compile(i)
                if rej:
                    return None, expr
                assert isinstance(acc, NamedReference)
                path.append(acc)
            return Path(path), None

        path = []
        for i in expr.path:
            acc, _ = self.compile(i, preprocess=False)
            assert isinstance(acc, str)
            path.append(acc)

        return '.'.join(path), None

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr
