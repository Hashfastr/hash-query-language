from typing import Optional, Union, TYPE_CHECKING, Callable
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import Context
import logging
import csv
import io

from .SplunkOps import SplunkOp, Spath

if TYPE_CHECKING:
    from Hql.Compiler import BranchDescriptor, InstructionSet
    from Hql.Operators import Operator
    from Hql.Expressions import Expression
    from Hql.Query import Statement
    import Hql

class SPLCompiler():
    def __init__(self):
        from Hql.Data import Data
        from Hql.Compiler import HqlCompiler
        from Hql.Config import Config
        self.type = self.__class__.__name__
        self.ctx = Context(Data())
        self.ops:list[Union['Operator', SplunkOp]] = []
        self.symbols = dict()
        self.post_ops:list['Operator'] = []
        self.top_level_where = True
        self.vestigial_compiler = HqlCompiler(Config())

        # self.reserved_names = {
        #     'index': 
        # }

    def from_name(self, name:str) -> Callable:
        if hasattr(self, name):
            return getattr(self, name)
        raise hqle.CompilerException(f'Attempting to get non-existant compiler function for {name}')

    def run(self, ctx:Union[Context, None]=None) -> Context:
        ctx = ctx if ctx else self.ctx
        return self.ctx

    def add_op(self, op:Union['Operator', 'BranchDescriptor']) -> tuple[Optional['Operator'], Optional['Operator']]:
        from Hql.Compiler import BranchDescriptor
        from Hql.Operators import Operator
        if isinstance(op, BranchDescriptor):
            op = op.get_op()
        acc, rej = self.compile(op)

        if isinstance(acc, list):
            self.ops += acc
        elif acc:
            assert isinstance(acc, (Operator, SplunkOp))
            self.ops.append(acc)
        else:
            raise hqle.CompilerException(f'Op compile returned {type(acc)} not Operator')

        assert isinstance(rej, (Operator, type(None)))
        return None, rej
    
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
    def compile(self, src:Union['Expression', 'Operator', 'Statement', None], preprocess:bool=True) -> tuple[Optional[object], Optional[object]]:
        from Hql.Operators import Operator, Where

        if src == None:
            raise hqle.CompilerException('Unimplemented root compile')

        if not preprocess and isinstance(src, Operator) and not isinstance(src, Where):
            self.top_level_where = False

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
    Splunk ops
    '''

    # def Spath(self, op:Spath, preprocess:bool=True) -> tuple[object, None]:
    #     if preprocess:
    #         return op, None
    #
    #     return 

    '''
    Operators
    '''

    def Where(self, op:'Hql.Operators.Where', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Operators import Where
        from Hql.Expressions import Expression
        if preprocess:
            acc, rej = self.compile(op.expr)
            assert isinstance(acc, Expression)
            assert isinstance(rej, Expression)
            ret_acc = Where(acc) if acc else None
            ret_rej = Where(rej) if rej else None
            return ret_acc, ret_rej

        acc, _ = self.compile(op.expr, preprocess=False)
        assert isinstance(acc, str)
        pred = acc

        acc, _ = self.vestigial_compiler.compile(op.expr)
        where = acc.get_attr('functions')
        
        if where:
            spl_op = 'where'
        else:
            if self.top_level_where:
                return pred, None
            spl_op = 'search'

        acc = f'| {spl_op} ' + pred
        return acc, None

    def Project(self, op:'Hql.Operators.Project', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import NamedExpression, NamedReference
        from Hql.Operators import Extend, Project
        if preprocess:
            extend = []
            project = []
            for i in op.exprs:
                acc, rej = self.vestigial_compiler.compile(i)
                
                if acc.get_attr('functions'):
                    if isinstance(i, NamedExpression):
                        extend.append(i)
                        for j in i.paths:
                            project.append(j)
                    else:
                        return None, op
                elif isinstance(i, NamedExpression):
                    extend.append(i)
                    for j in i.paths:
                        project.append(j)
                else:
                    assert isinstance(i, NamedReference)
                    project.append(i)

            if extend:
                extend = Extend(extend)
                acc, rej = self.compile(extend)
                if rej:
                    return None, op
                extend = acc

            project = Project('project', project)

            if extend:
                return [extend, project], None
            else:
                return project, None

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i, preprocess=False)
            exprs.append(acc)
        
        acc = f'| fields ' + ', '.join(exprs)
        return acc, None

    def ProjectAway(self, op:'Hql.Operators.ProjectAway', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return op, None

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i, preprocess=False)
            exprs.append(acc)
        
        acc = f'| fields - ' + ', '.join(exprs)
        return acc, None

    def ProjectKeep(self, op:'Hql.Operators.ProjectKeep', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return op, None

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i, preprocess=False)
            exprs.append(acc)
        
        acc = f'| fields ' + ', '.join(exprs)
        return acc, None

    def ProjectReorder(self, op:'Hql.Operators.ProjectReorder', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return op, None

        exprs = []
        for i in op.exprs:
            acc, _ = self.compile(i, preprocess=False)
            exprs.append(acc)
        exprs.append('*')
        
        acc = f'| fields ' + ', '.join(exprs)
        return acc, None

    def ProjectRename(self, op:'Hql.Operators.ProjectRename', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import NamedExpression
        if preprocess:
            for i in op.exprs:
                if not isinstance(i, NamedExpression):
                    return None, op
                if len(i.paths) > 1:
                    return None, op
            return op, None

        exprs = []
        for i in op.exprs:
            assert isinstance(i, NamedExpression)
            path, _ = self.compile(i.paths[0], preprocess=False)
            value, _ = self.compile(i.value, preprocess=False)
            assert isinstance(path, str)
            assert isinstance(value, str)
            exprs.append(value + ' AS ' + path)

        acc = f'| rename ' + ', '.join(exprs)
        return acc, None

    def Take(self, op:'Hql.Operators.Take', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            if op.tables:
                return None, op
            return op, None

        acc, _ = self.compile(op.expr, preprocess=False)
        assert isinstance(acc, int)
        acc = f'| head {acc}'

        return acc, None

    def Count(self, op:'Hql.Operators.Count', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            if op.name:
                return None, op
            return op, None

        ret = '| stats count by index'
        return ret, None

    def Extend(self, op:'Hql.Operators.Extend', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Operators import Extend
        if preprocess:
            exprs = []
            rejexprs = []
            for i in op.exprs:
                acc, rej = self.compile(i)
                if rej:
                    rejexprs.append(i)
                else:
                    exprs.append(acc)

            acc = Extend(exprs) if exprs else None
            rej = Extend(rejexprs) if rejexprs else None
            return acc, rej

        parts = []
        for i in op.exprs:
            acc, rej = self.compile(i, preprocess=False)
            assert isinstance(acc, str)
            parts.append(acc)
        exprs = ', '.join(parts)

        out = '| eval ' + exprs
        return out, None

    def Range(self, op:'Hql.Operators.Range', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import Integer, Float, Datetime
        if preprocess:
            return op, None

        acc, rej = self.compile(op.name, preprocess=False)
        assert isinstance(acc, str)
        name = acc

        if isinstance(op.start, (Integer, Float)):
            acc, rej = self.compile(op.start, preprocess=False)
            assert isinstance(acc, int)
            start = acc

            acc, rej = self.compile(op.end, preprocess=False)
            assert isinstance(acc, int)
            end = acc

            acc, rej = self.compile(op.step, preprocess=False)
            assert isinstance(acc, int)
            step = acc

            out = f'''
            | makeresults
            | eval {name} = mvrange({start}, {end}, {step})
            | mvexpand {name}
            | table {name}
            '''
        
        elif isinstance(op.start, Datetime):
            acc, rej = self.compile(op.start, preprocess=False)
            assert isinstance(acc, str)
            start = acc

            acc, rej = self.compile(op.end, preprocess=False)
            assert isinstance(acc, str)
            end = acc

            acc, rej = self.compile(op.start, preprocess=False)
            assert isinstance(acc, str)
            step = acc

            out = f'''
            | makeresults
            | eval start_time = {start}
            | eval end_time = {end}
            | eval step_seconds = {step}
            | eval {name} = mvrange(start_time, end_time, step_seconds)
            | mvexpand {name}
            | table {name}
            '''

        else:
            raise hqle.CompilerException(f'Invalid range type {type(op.start)}')
        
        return out, op

    def Top(self, op:'Hql.Operators.Top', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Unnest(self, op:'Hql.Operators.Unnest', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Union(self, op:'Hql.Operators.Union', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Summarize(self, op:'Hql.Operators.Summarize', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def Datatable(self, op:'Hql.Operators.Datatable', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import NamedReference, Literal
        if preprocess:
            return op, None

        keys:list[str] = []
        for i in op.schema:
            assert isinstance(i[0], NamedReference)
            keys.append(i[0].name)

        data = []
        row = dict()
        for i in range(0, len(op.values), len(keys)):
            for idx, j in enumerate(op.values[i:i+len(keys)]):
                assert isinstance(i, Literal)
                row[keys[idx]] = i.value
            data.append(row)
            row = dict()

        out = io.StringIO()
        writer = csv.DictWriter(out, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
        csvout = out.getvalue()

        new = '| makeresults format=csv data='
        new += '"""\n'
        new += csvout
        new += '\n"""'

        return new, op

    def Join(self, op:'Hql.Operators.Join', preprocess:bool=True) -> tuple[object, object]:
        return None, op

    def MvExpand(self, op:'Hql.Operators.MvExpand', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Operators import MvExpand
        if preprocess:
            supported = []
            failed = []
            for i in op.exprs:
                if i.to:
                    failed.append(i)
                else:
                    supported.append(i)
            acc = MvExpand(supported)
            rej = MvExpand(failed)
            return acc, rej

        exprs = []
        for i in op.exprs:
            acc, rej = self.compile(i.expr, preprocess=False)
            assert isinstance(acc, str)
            exprs.append(acc)

        if op.limit:
            acc, rej = self.compile(op.limit, preprocess=False)
            assert isinstance(acc, int)
            limit = acc
        else:
            limit = None

        out = ''
        for i in exprs:
            out += '| mvexpand ' + i
            if limit != None:
                out += f' limit={limit}'
            out += '\n'
        
        return out, None

    def Sort(self, op:'Hql.Operators.Sort', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            for i in op.exprs:
                if i.nulls != 'last':
                    return None, op
            return op, None

        exprs = []
        for i in op.exprs:
            field, _ = self.compile(i.expr, preprocess=False)
            assert isinstance(field, str)
            order = '-' if i.order == 'desc' else '+'
            exprs.append(order + field)
        exprs = ', '.join(exprs)

        out = '| sort ' + exprs
        return out, None

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

    def Function(self, expr:'Hql.Functions.Function', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def FuncExpr(self, expr:'Hql.Expressions.FuncExpr', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def DotCompositeFunction(self, expr:'Hql.Expressions.DotCompositeFunction', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Equality(self, expr:'Hql.Expressions.Equality', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Substring(self, expr:'Hql.Expressions.Substring', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Relational(self, expr:'Hql.Expressions.Relational', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BetweenEquality(self, expr:'Hql.Expressions.BetweenEquality', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BinaryLogic(self, expr:'Hql.Expressions.BinaryLogic', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Not(self, expr:'Hql.Expressions.Not', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def BasicRange(self, expr:'Hql.Expressions.BasicRange', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Regex(self, expr:'Hql.Expressions.Regex', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def TypeExpression(self, expr:'Hql.Expressions.TypeExpression', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def StringLiteral(self, expr:'Hql.Expressions.StringLiteral', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return repr(expr.value), None
    
    def MultiString(self, expr:'Hql.Expressions.MultiString', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Integer(self, expr:'Hql.Expressions.Integer', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.value, None

    def IP4(self, expr:'Hql.Expressions.IP4', preprocess:bool=True) -> tuple[object, object]:
        return None, expr

    def Float(self, expr:'Hql.Expressions.Float', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return str(expr.value), None

    def Bool(self, expr:'Hql.Expressions.Bool', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        ret = 'true' if expr.value else 'false'
        return ret, None

    def Multivalue(self, expr:'Hql.Expressions.Multivalue', preprocess:bool=True) -> tuple[object, object]:
        return None, expr
    
    def NamedReference(self, expr:'Hql.Expressions.NamedReference', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return expr.name, None

    def EscapedNamedReference(self, expr:'Hql.Expressions.EscapedNamedReference', preprocess:bool=True) -> tuple[object, object]:
        if preprocess:
            return expr, None
        return f'{repr(expr.name)}', None

    def Keyword(self, expr:'Hql.Expressions.Keyword', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Identifier(self, expr:'Hql.Expressions.Identifier', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Wildcard(self, expr:'Hql.Expressions.Wildcard', preprocess:bool=True) -> tuple[object, object]:
        return self.NamedReference(expr, preprocess=preprocess)

    def Path(self, expr:'Hql.Expressions.Path', preprocess:bool=True) -> tuple[object, object]:
        from Hql.Expressions import EscapedNamedReference, NamedReference
        from Hql.Expressions import StringLiteral, NamedExpression
        from Hql.Operators import ProjectRename
        import random

        if preprocess:

            '''
            spath = False
            for i in expr.path:
                if isinstance(i, EscapedNamedReference):
                    spath = True

            # Create a compiler workaround
            if spath:
                parts = []
                for i in expr.path:
                    if isinstance(i, EscapedNamedReference):
                        parts.append(f"'{i.name}'")
                    else:
                        parts.append(i.name)
                rh = StringLiteral('.'.join(parts), lquote='@"', rquote='"')

                lh = NamedReference('%16x' % random.getrandbits(64))
                self.symbols[expr] = lh

                reassign = ProjectRename('project-rename', [NamedExpression([expr], lh)])
                self.post_ops.append(reassign)

                self.ops.append(Spath(lh, rh))
                return lh, None
            '''

            return expr, None

        parts = []
        for i in expr.path:
            parts.append(i.name)
        out = repr('.'.join(parts))
        return out, None

    def NamedExpression(self, expr:'Hql.Expressions.NamedExpression', preprocess:bool=True) -> tuple[object, object]:
        return expr, None
