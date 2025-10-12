import json
import polars as pl
from typing import TYPE_CHECKING, Union
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Compiler import CompilerSet
    from Hql.Data import Data, Table
    from Hql.Types.Compiler import CompilerType

if TYPE_CHECKING:
    from Hql.Context import Context

# An expression is any grouping of other expressions
# Typically children of an operation, an expression can also contain operators itself
# Such as a subsearch, which is an expression, and contains operators
# All other expressions are children of this one
class Expression():
    def __init__(self)-> None:
        self.type = self.__class__.__name__
        self.escaped = False
        self.literal = False
        self.logic   = False
        self.value   = None
        self.tabular = False
    
    def to_dict(self) -> Union[None, dict]:
        return {
            'type': self.type
        }
    
    def eval(self, ctx:'Context', **kwargs) -> Union[pl.Expr, 'Expression', list[str], str, 'CompilerSet', 'CompilerType', 'Data', 'Table', int, float]:
        raise hqle.CompilerException(f'Undefined eval for {self.type}')

    def __str__(self) -> str:
        return json.dumps(self.to_dict())
    
    def __repr__(self) -> str:
        return self.__str__()

    # Defaults to the 'i am not none' approach
    # True unless overridden
    def __bool__(self) -> bool:
        return True

    def __eq__(self, value: object, /) -> bool:
        return NotImplemented

    def features(self):
        return []

    def decompile(self, ctx:'Context') -> str:
        return ''
