from typing import TYPE_CHECKING, Optional, Union

if TYPE_CHECKING:
    from Hql.Expressions import NamedReference, StringLiteral
    from Hql.Compiler import SqlCompiler

class SqlExpression():
    ...

class Like(SqlExpression):
    def __init__(self, lh:'NamedReference', rh:'StringLiteral') -> None:
        self.lh = lh
        self.rh = rh
