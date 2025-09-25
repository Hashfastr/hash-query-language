from numpy import isin
from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Expressions import OpParameter
    from Hql.Compiler import InstructionSet

# @register_op('Join')
class Join(Operator):
    def __init__(self, rh:Union['Expression', 'InstructionSet'], params:Union[None, list['OpParameter']]=None, on:Union[None, list['Expression']]=None, where:Union[None, 'Expression']=None):
        Operator.__init__(self)
        self.rh = rh
        self.params:list = params if params else []
        self.on = on if on else []
        self.where = where

        # default join type
        self.kind = 'inner'

    def process_params(self, ctx:'Context'):
        for i in self.params:
            if i.name == 'kind':
                self.kind = i.value.eval(ctx, as_str=True)

    def get_right(self, ctx:'Context', where:Union[None, 'Expression']):
        from Hql.Expressions import Identifier
        from Hql.Operators import Where
        compilerset = None
                
        name = self.rh.eval(ctx, as_str=True)
        
        if name not in ctx.symbol_table:
            raise hqle.QueryException(f'Reference dataset {name} undefined')
        
        compilerset = ctx.symbol_table[name]

        if not compilerset:
            raise hqle.CompilerException(f'Unhandled join right side {self.rh.type}')
        
        # There's a where, add a right side filter
        if where:
            compilerset.add_op(Where(where))
        
        return compilerset.eval(ctx)
    
    def resolve_on_clause(self):
        ...

    def decompile(self, ctx: 'Context') -> str:
        out = 'join '

        out += self.rh.decompile(ctx)

        if self.params:
            out += ' '
            params = []
            for i in self.params:
                params.append(i.decompile(ctx))
            out += ' '.join(params)

        if self.on:
            out += ' '
            out += 'on '
            out += ', '.join([x.decompile(ctx) for x in self.on])

        if self.where:
            out += ' '
            out += 'where '
            out += self.where.decompile(ctx)

        return out

    def eval(self, ctx:'Context', **kwargs):
        self.process_params(ctx)

        left = ctx.data
        right = self.get_right(ctx, self.where)
        
        clause = self.on[0].eval(ctx, as_str=True)
        if not isinstance(clause, str):
            raise hqle.CompilerException(f'Join clause expression returned {type(clause)} not str')
        
        data = left.join(right, clause, kind=self.kind)
        
        return data
