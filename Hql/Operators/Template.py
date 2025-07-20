from ..Data import Data, Table
from ..Expressions import Expression
from ..Operators import Operator
from ..Exceptions import *
import polars as pl
from ..Context import register_op, Context

@register_op('Template')
class Template(Operator):
    def __init__(self):
        Operator.__init__(self)

    def eval(self, ctx:Context, **kwargs):
        return ctx.data
