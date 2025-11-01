from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from Hql.Operators import Project, Where
    from Hql.Compiler import SqlCompiler
    from Hql.Expressions import NamedReference

class SqlStatement():
    def compile(self, compiler:'SqlCompiler') -> str:
        ...

'''
Assumes all ops have been precompiled by the SQL compiler
'''
class SELECT(SqlStatement):
    def __init__(self, project:Optional['Project']=None, src=None, where:Optional['Where']=None):
        self.project:Optional['Project'] = project
        self.src:Union[None, SqlStatement, 'NamedReference'] = src
        self.where:Optional['Where'] = where

    def add_project(self, op:'Project') -> 'SELECT':
        if self.project:
            return SELECT(project=op, src=self)
        self.project = op
        return self
    
    def add_where(self, op:'Where') -> 'SELECT':
        if self.where:
            return SELECT(where=op, src=self)
        self.where = op
        return self

    def compile(self, compiler:'SqlCompiler') -> str:
        if self.project:
            project, _ = compiler.compile(self.project, preprocess=False)
        else:
            project = '*'

        if isinstance(self.src, SqlStatement):
            src = self.src.compile(compiler)
            src = '(' + src + ')'
        else:
            src, _ = compiler.compile(self.src, preprocess=False)

        if self.where:
            where, _ = compiler.compile(self.where, preprocess=False)
        else:
            where = ''

        assert isinstance(project, str)
        assert isinstance(src, str)
        assert isinstance(where, str)

        out = f'SELECT {project} FROM {src}'
        if where:
            out += f' WHERE {where}'
    
        return out
