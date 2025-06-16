from HqlCompiler.Data import Data, Table
from HqlCompiler.Expression import Expression
from HqlCompiler.Operators import Operator
from HqlCompiler.Exceptions import *
import polars as pl
from HqlCompiler.Context import register_op, Context

@register_op('Join')
class Join(Operator):
    def __init__(self, dataset, params, clause:Expression=None):
        super().__init__()
        self.kind = 'inner'
        self.dataset = dataset
        self.params = params
        self.clause = clause

    def get_right(self, ctx:Context):
        from HqlCompiler.Expression import Identifier
        compilerset = None
                
        name = self.dataset.eval(ctx, as_str=True)
        
        if name not in ctx.symbol_table:
            raise QueryException(f'Reference dataset {name} undefined')
        
        compilerset = ctx.symbol_table[name]

        if not compilerset:
            raise CompilerException(f'Unhandled join right side {self.dataset.type}')
        
        return compilerset.eval(ctx)
        

    def eval(self, ctx:Context, **kwargs):
        for i in self.params:
            if i.name == 'kind':
                self.kind = i.value.eval(ctx, as_str=True)

        left = ctx.data
        right = self.get_right(ctx)
        clause = self.clause[0].eval(ctx, as_str=True)
        
        data = left.join(right, clause, kind=self.kind)
        
        return data