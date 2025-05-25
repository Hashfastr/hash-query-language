from .Operator import Operator
from ..Expression import Expression
import polars as pl
from ..PolarsTools import plt
from HqlCompiler.Data import Schema, Data, Table
from HqlCompiler.Context import register_op, Context
from HqlCompiler.Exceptions import *
from HqlCompiler.Operators import Operator

# Project my beloved
# Defines a number of fields to be kept in the output following this operator.
#
# {"test1":"val","test2":"val","test3":"val","test4":"val","test5":"val"}
# | project test1, test3, test5
# 
# Would result in
#
# {"test1":"val","test3":"val","test5":"val"}
# https://learn.microsoft.com/en-us/kusto/query/project-operator
@register_op('Project')
class Project(Operator):
    def __init__(self, exprs:list[Expression]):
        super().__init__()
        self.exprs = exprs
        self.non_conseq = [
            'Take'
        ]
        
    def eval(self, ctx:Context, **kwargs):
        static = []
        dynamic = []
        for i in self.exprs:
            if i.type in ("NamedReference", "Identifier", "EscapedName"):
                fields = [i.eval(ctx, as_str=True)]
                
                if not ctx.data.assert_field(fields):
                    raise QueryException(f"Referenced field {'.'.join(fields)} not found")
                
                static.append(fields)
            
            elif i.type == "Path":
                fields = i.eval(ctx, as_list=True)

                if not ctx.data.assert_field(fields):
                    raise QueryException(f"Referenced field {'.'.join(fields)} not found")

                static.append(fields)

            elif i.type == "DotCompositeFunction":
                dynamic.append(i)
                
            else:
                raise CompilerException(f'Unhandled project expression {i.type}')
                        
        new = [ctx.data.get_elements(static)]
        
        for i in dynamic:
            new.append(i.eval(ctx))

        print(new)

        return Data.merge(new)