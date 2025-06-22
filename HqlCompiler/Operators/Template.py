from HqlCompiler.Data import Data, Table
from HqlCompiler.Expression import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op, Context

@register_op('Template')
class Template(Operator):
    def __init__(self):
        Operator.__init__(self)

    def eval(self, ctx:Context, **kwargs):
        return ctx.data
