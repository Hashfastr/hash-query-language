from ..Data import Data, Table
from ..Expressions import Expression
from ..Operators import Operator
from ..Exceptions import *
import polars as pl
from ..Context import register_op, Context

@register_op('Join')
class Join(Operator):
    def __init__(self, dataset, params, on:Expression=None, where:Expression=None):
        super().__init__()
        self.dataset = dataset
        self.params = params
        self.on = on
        self.where = where

        # default join type
        self.kind = 'inner'


    def process_params(self, ctx:Context):
        for i in self.params:
            if i.name == 'kind':
                self.kind = i.value.eval(ctx, as_str=True)
    

    def get_right(self, ctx:Context, where:Expression):
        from ..Expressions import Identifier
        from ..Operators import Where
        compilerset = None
                
        name = self.dataset.eval(ctx, as_str=True)
        
        if name not in ctx.symbol_table:
            raise QueryException(f'Reference dataset {name} undefined')
        
        compilerset = ctx.symbol_table[name]

        if not compilerset:
            raise CompilerException(f'Unhandled join right side {self.dataset.type}')
        
        # There's a where, add a right side filter
        if where:
            compilerset.add_op(Where(where))
        
        return compilerset.eval(ctx)
    
    
    def resolve_on_clause(self):
        ...
        

    def eval(self, ctx:Context, **kwargs):
        self.process_params(ctx)

        left = ctx.data
        right = self.get_right(ctx, self.where)
        
        clause = self.on[0].eval(ctx, as_str=True)
        
        data = left.join(right, clause, kind=self.kind)
        
        return data