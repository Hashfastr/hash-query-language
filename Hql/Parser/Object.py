from typing import Union
import polars as pl
from Hql.Context import Context
import json
from Hql.Types.Hql import HqlTypes as hqlt

class ParseObject():
    def __init__(self) -> None:
        self.type = self.__class__.__name__

    def __bool__(self) -> bool:
        return True

    def __eq__(self, value: object, /) -> bool:
        return NotImplemented

    def __str__(self) -> str:
        return json.dumps(self.to_dict())
    
    def __repr__(self) -> str:
        return self.__str__()

    def can_polars(self) -> bool:
        return True

    def polars(self) -> Union[pl.Expr, pl.DataTypeExpr]:
        return NotImplemented

    def polars_value(self) -> pl.Expr:
        return NotImplemented

    def str(self) -> str:
        return NotImplemented

    def dtype(self) -> hqlt.HqlType:
        return NotImplemented

    def deparse(self) -> str:
        return NotImplemented

    def eval(self, ctx:Context) -> Context:
        return NotImplemented

    def to_dict(self) -> dict:
        return {
            'type': self.type
        }
