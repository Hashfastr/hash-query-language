from numpy import isin
from polars import String
from Hql.Operators import Operator
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_op, Context
from typing import Union, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Expression, NamedReference, Path
    from Hql.Data import Data
    from Hql.Expressions import OpParameter
    from Hql.Compiler import InstructionSet

# @register_op('Join')
class Join(Operator):
    def __init__(self, rh:Union['Expression', 'InstructionSet'], params:Optional[list['OpParameter']]=None, on:Optional[list[Union['NamedReference', 'Path']]]=None, where:Optional['Expression']=None):
        Operator.__init__(self)
        self.rh = rh
        self.params:list = params if params else []
        self.on = on if on else []
        self.where = where

        # default join type
        self.kind = 'inner'

        if not self.on:
            from Hql.Data import Data
            ctx = Context(Data())
            raise hqle.QueryException(f'Missing on clause in join: {self.decompile(ctx)}')

    def process_params(self, ctx:'Context'):
        for i in self.params:
            if i.name == 'kind':
                self.kind = i.value.eval(ctx, as_str=True)

    def get_right(self, ctx:'Context', where:Union[None, 'Expression']):
        from Hql.Expressions import Identifier
        from Hql.Operators import Where

        if not isinstance(self.rh, InstructionSet):
            raise hqle.CompilerException('Join attempting to get right without compilation, error?')
        
        # There's a where, add a right side filter
        if where:
            self.rh.add_op(Where(where))
            self.rh.recompile(ctx.config)
        
        return self.rh.eval(ctx)

    def gen_optimization(self, data:'Data') -> 'Expression':
        from Hql.Operators import Summarize, Union
        from Hql.Expressions import Wildcard, ByExpression
        from Hql.Operators.Database import Static
        from Hql.Compiler import InstructionSet
        from Hql.Data import Data
        from Hql.Expressions import Equality, BinaryLogic

        ops = [
            Summarize([], ByExpression(self.on)),
            Union([Wildcard('*')])
        ]

        ctx = InstructionSet(Static(data), ops).eval(Context(Data()))
        table = [x for x in ctx.data][0].to_dicts()

        exprs = []
        for i in table:
            ands = []
            for j in self.explode_dict(i):
                lh = self.name_from_dict(j)
                rh = self.value_from_dict(j)
                ands.append(Equality(lh, '==', [rh]))
            exprs.append(BinaryLogic(ands[0], ands[1:], 'and'))
        return BinaryLogic(exprs[0], exprs[1:], 'or')

    def name_from_dict(self, data:dict) -> Union['NamedReference', 'Path']:
        from Hql.Expressions import Path, NamedReference
        path = []
        while True:
            key = list(data.keys())[0]
            path.append(NamedReference(key))
            if not isinstance(data[key], dict):
                break
            data = data[key]
        return Path(path)

    def value_from_dict(self, data:dict):
        from Hql.Expressions.Literals import Integer, StringLiteral, Float
        while True:
            key = list(data.keys())[0]
            if not isinstance(data[key], dict):
                break
            data = data[key]

        if isinstance(data[key], int):
            return Integer(data[key])
        if isinstance(data[key], str):
            return StringLiteral(data[key], verbatim=True)
        if isinstance(data[key], float):
            return Float(data[key])
        return StringLiteral(str(data[key]))

    def explode_dict(self, data:dict) -> list:
        out = []
        for i in data:
            if not isinstance(data[i], dict):
                out.append({i: data[i]})
                continue

            up = self.explode_dict(data[i])
            for j in up:
                out.append({i: j})
        return out
    
    def resolve_on_clause(self):
        ...

    def decompile(self, ctx: 'Context') -> str:
        from Hql.Compiler import InstructionSet
        out = 'join '

        if isinstance(self.rh, InstructionSet):
            out += 'INSTRUCTION_RH'
        else:
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

        expr = self.gen_optimization(left)
        print(expr.decompile(ctx))

        right = self.get_right(ctx, self.where)
        
        clause = self.on[0].eval(ctx, as_str=True)
        if not isinstance(clause, str):
            raise hqle.CompilerException(f'Join clause expression returned {type(clause)} not str')
        
        data = left.join(right, clause, kind=self.kind)
        
        return data
