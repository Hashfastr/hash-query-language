from typing import TYPE_CHECKING, Optional, Union
from Hql.Exceptions import HqlExceptions as hqle
import json

if TYPE_CHECKING:
    from Hql.Operators import Project, Where, Take, Join
    from Hql.Compiler import SqlCompiler
    from Hql.Expressions import NamedReference, Path

class SqlStatement():
    def __init__(self) -> None:
        self.indent_spaces = 2

    def to_dict(self):
        return {}

    def compile(self, compiler:'SqlCompiler') -> str:
        ...

    def random_label(self) -> str:
        import string, random
        return ''.join(random.choices(string.ascii_lowercase, k=8))

    def compile_nested(self, compiler:'SqlCompiler', nested:'SqlStatement') -> str:
        res = nested.compile(compiler)
        indented = '\n'
        for line in res.split('\n'):
            if line:
                indented += ' ' * self.indent_spaces + line
                indented += '\n'
        return '(' + indented + ')'

'''
Assumes all ops have been precompiled by the SQL compiler
'''
class SELECT(SqlStatement):
    def __init__(self, src:Union[SqlStatement, 'NamedReference'], project:Optional['Project']=None, where:Optional['Where']=None, take:Optional['Take']=None, join:Optional[list['Join']]=None, distinct:Optional[list[Union['Path', 'NamedReference']]]=None):
        SqlStatement.__init__(self)
        self.project:Optional['Project'] = project
        self.src:Union[SqlStatement, 'NamedReference'] = src
        self.where:Optional['Where'] = where
        self.limit:Optional['Take'] = take
        joins = join if join else []
        self.join:JOIN = JOIN(joins)
        self.distinct:list[Union['Path', 'NamedReference']] = distinct if distinct else []

    def to_dict(self):
        return {
            'type': 'SELECT',
            'project': self.project.to_dict() if self.project else None,
            'src': self.src.to_dict() if self.src else None,
            'where': self.where.to_dict() if self.where else None,
            'limit': self.where.to_dict() if self.where else None,
            'joins': self.join.to_dict(),
            'distinct': [x.to_dict() for x in self.distinct]
        }

    def add_project(self, op:'Project') -> 'SELECT':
        if self.project:
            return SELECT(self, project=op)
        self.project = op
        return self
    
    def add_where(self, op:'Where') -> 'SELECT':
        if self.where:
            self.where.integrate(op)
        self.where = op
        return self

    def add_join(self, op:'Join') -> 'SELECT':
        self.join.add(op)
        return self

    def add_distinct(self, expr:Union['Path', 'NamedReference']):
        self.distinct.append(expr)

    def is_plain(self):
        return not (
            self.project or self.where or self.limit or self.join or self.distinct
        )

    def join_only(self):
        return not (
            self.project or self.where or self.limit or self.distinct
        )

    def collapse_join(self) -> tuple[Union['SqlStatement', 'NamedReference', None], list['Join']]:
        from Hql.Operators import Join
        from Hql.Compiler import InstructionSet

        if not self.join_only():
            return self, []

        if isinstance(self.src, SELECT):
            src, joins = self.src.collapse_join()
            joins = joins + self.join.joins
        else:
            src = self.src
            joins = self.join.collapse_joins()

        return src, joins

    def compile(self, compiler:'SqlCompiler') -> str:
        from copy import deepcopy
        compiler = deepcopy(compiler)
        compiler.statement = self

        # if self.is_plain():
        #     if isinstance(self.src, SqlStatement):
        #         return self.src.compile(compiler)
        #     else:
        #         acc, _ = compiler.compile(self.src, preprocess=False)
        #         assert isinstance(acc, str)
        #         return acc

        src = self.src

        join = ''
        if self.join:
            join = self.join.compile(compiler)
            for i in self.join.wheres:
                self.add_where(i)
            compiler.joins = True

        project = '*'
        if self.project:
            project, _ = compiler.compile(self.project, preprocess=False)

        if isinstance(src, SqlStatement):
            src = self.compile_nested(compiler, src)
        else:
            src, _ = compiler.compile(src, preprocess=False)

        where = ''
        if self.where:
            where, _ = compiler.compile(self.where, preprocess=False)

        limit = ''
        if self.limit:
            limit, _ = compiler.compile(self.limit, preprocess=False)

        assert isinstance(project, str)
        assert isinstance(src, str)
        assert isinstance(where, str)
        assert isinstance(limit, str)

        out = f'SELECT {project}\n'
        out += f'FROM {src}'
        if join:
            out += join
        if out[-1] != '\n':
            out += '\n'
        if where:
            out += f'WHERE {where}\n'
        if limit:
            out += f'LIMIT {limit}\n'

        return out

class JOIN(SqlStatement):
    def __init__(self, joins:list['Join']) -> None:
        from Hql.Expressions import NamedReference
        SqlStatement.__init__(self)
        self.lname = NamedReference(self.random_label())
        self.joins:list['Join'] = joins
        self.wheres:list['Where'] = []

    def __bool__(self):
        return bool(self.joins)

    def to_dict(self):
        return {
            'type': 'JOIN',
            'lname': self.lname.name,
            'joins': [x.to_dict() for x in self.joins],
            'wheres': [x.to_dict() for x in self.wheres]
        }

    def add(self, join:'Join'):
        self.joins.append(join)

    def collapse_joins(self) -> list['Join']:
        new = []
        for i in self.joins:
            new += self.collapse_join(i)
        return new

    def collapse_join(self, join:'Join') -> list['Join']:
        from Hql.Compiler import InstructionSet, SqlCompiler
        from Hql.Operators import Join
        from Hql.Operators.Database import SQLite, Database
        from Hql.Expressions import NamedReference

        if isinstance(join.rh, NamedReference):
            return [join]

        assert isinstance(join.rh, InstructionSet)
        up = join.rh.upstream[0]
        assert isinstance(up, SQLite) and isinstance(up.compiler, SqlCompiler)
        rh = up.compiler.statement
        if not isinstance(rh, SELECT):
            return [join]

        src, joins = rh.collapse_join()
        # I will fix this typing later, is only within the domain of this class
        new = Join(src, on=join.on)
        new = [new] + joins
        return new

    def prepend(self, join:Union[list['Join'], 'Join']):
        if not isinstance(join, list):
            join = [join]
        self.joins = join + self.joins

    def compile(self, compiler: 'SqlCompiler') -> str:
        self.joins = self.collapse_joins()

        acc, _ = compiler.compile(self.lname, preprocess=False)
        joins = []
        for i in self.joins:
            joins.append(self.compile_join(i, compiler))

        out = f' {acc}\n'
        out += '\n'.join(joins)
        out += '\n'

        return out

    def compile_join(self, op:'Join', compiler:'SqlCompiler') -> str:
        from Hql.Compiler import InstructionSet, SqlCompiler
        from Hql.Operators import Where
        from Hql.Expressions import BinaryLogic, Path, FuncExpr, NamedReference, Equality
        from Hql.Operators.Database import Database

        rname = NamedReference(self.random_label())
        join_op = 'INNER'
        if op.kind in ('leftouter', 'left', 'leftanti'):
            join_op = 'LEFT'
        elif op.kind in ('rightouter', 'right', 'rightanti'):
            join_op = 'RIGHT'
        elif op.kind == 'fullouter':
            join_op = 'FULL OUTER'

        # if op.kind == 'innerunique':
        #     for i in op.on:
        #         path = [lname]
        #         if isinstance(i, Path):
        #             path += i.path
        #         else:
        #             path.append(i)
        #         self.statement.add_distinct(Path(path))

        anti = ''
        if op.kind == 'leftanti':
            anti = rname
        if op.kind == 'rightanti':
            anti = self.lname

        if anti:
            anti_filter = []
            for i in op.on:
                func = FuncExpr('isnull', [Path([anti, i])]).eval(compiler.ctx)
                anti_filter.append(func)

            self.wheres.append(Where(BinaryLogic(anti_filter[0], anti_filter[1:], 'and')))

        out = f'{join_op} JOIN '

        if isinstance(op.rh, InstructionSet):
            rh = op.rh.upstream[0]
            assert isinstance(rh, Database)
            assert isinstance(rh.compiler, SqlCompiler)
            rh_stmt = rh.compiler.statement
        else:
            rh_stmt = op.rh

        if not isinstance(rh_stmt, (NamedReference, SELECT)):
            raise hqle.CompilerException('SQL joining on non-SELECT statement')

        if isinstance(rh_stmt, SELECT):
            # collapse needless shells
            if rh_stmt.is_plain():
                if isinstance(rh_stmt.src, SqlStatement):
                    rh_str = self.compile_nested(compiler, rh_stmt.src)
                else:
                    rh_str, _ = compiler.compile(rh_stmt.src, preprocess=False)
                    assert isinstance(rh_str, str)
            else:
                rh_str = self.compile_nested(compiler, rh_stmt)
        else:
            rh_str, _ = compiler.compile(rh_stmt, preprocess=False)
            assert isinstance(rh_str, str)

        acc, _ = compiler.compile(rname, preprocess=False)
        assert isinstance(acc, str)
        out += rh_str + ' ' + acc + ' '

        ons = []
        for i in op.on:
            acc, _ = compiler.compile(i, preprocess=False)
            assert isinstance(acc, str)
            ons.append(acc)
            # ons.append(
            #     Equality(Path([self.lname, i]), '==', [Path([rname, i])])
            # )
        # on_expr = BinaryLogic(ons[0], ons[1:], 'and')
        # acc, _ = compiler.compile(on_expr, preprocess=False)

        acc = ','.join(ons)
        assert isinstance(acc, str)
        
        out += '\n' + ' ' * self.indent_spaces + 'USING '
        out += '(' + acc + ')'

        self.lname = rname

        return out
