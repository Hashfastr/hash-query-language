from typing import TYPE_CHECKING, Union
from Hql.Context import Context
import logging
import time
import json
from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    from Hql.Operators import Database, Operator
    from Hql.Compiler import BranchDescriptor
    from Hql.Config import Config

class InstructionSet():
    def __init__(self, upstream:Union['Database', list['Database'], 'InstructionSet', list['InstructionSet']], operators:Union[None, list['Operator']]=None) -> None:
        import random
        from Hql.Operators import Database
        from Hql.Compiler import InstructionSet
        
        assert isinstance(upstream, (Database, list, InstructionSet))
        if isinstance(upstream, list):
            for i in upstream:
                if not isinstance(i, (Database, InstructionSet)):
                    raise hqle.CompilerException(f'Invalid upstream type {type(i)}')
            self.upstream = upstream
        else:
            self.upstream = [upstream]

        self.ops:list['Operator'] = operators if operators else []
        self.id = '%08x' % random.getrandbits(32)
        self.attrs = dict()

        if len(self.upstream) == 1 and isinstance(self.upstream[0], InstructionSet):
            self.ops = self.upstream[0].ops + self.ops
            self.upstream = self.upstream[0].upstream

    def is_empty(self) -> bool:
        return not (self.upstream or self.ops)

    def to_dict(self):
        from Hql.Context import Context
        from Hql.Data import Data

        ops = []
        for i in self.ops:
            op = i.to_dict()
            op = {
                'id': op.get('id', '????'),
                'type': op.get('type'),
                'decomp': i.decompile(Context(Data()))
            }
            ops.append(op)

        return {
            'id': self.id,
            'attrs': self.attrs,
            'upstream': [x.to_dict() for x in self.upstream],
            'ops': ops,
        }

    def add_op(self, op:Union['BranchDescriptor', 'Operator']) -> tuple[Union['Operator', None], Union['Operator', None]]:
        from Hql.Compiler import BranchDescriptor

        if isinstance(op, BranchDescriptor):
            op = op.get_op()
        self.ops.append(op)
        
        return None, None

    def recompile(self, config:'Config') -> 'InstructionSet':
        from Hql.Compiler import HqlCompiler
        return HqlCompiler(config).InstructionSet(self)

    def exec(self, inst:Union['Database', 'Operator'], ctx:Context) -> Context:
        logging.debug(f'Executing {inst.type} - {inst.id}')
        start = time.perf_counter()

        ctx.data = inst.eval(ctx)

        end = time.perf_counter()
        logging.debug(f'{inst.id} - {end - start}')

        return ctx

    def render(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def run_upstream(self, up:Union['Database', 'InstructionSet']) -> 'Context':
        from Hql.Data import Data
        out = up.eval(Context(Data()))
        if isinstance(out, Data):
            out = Context(out)
        return out

    def eval(self, ctx:Context, **kwargs) -> Context:
        from Hql.Data import Data
        from Hql.Threading import InstructionPool

        logging.debug(f'Starting InstructionSet {self.id}')
        start = time.perf_counter()
   
        pool = InstructionPool(auto_run=False)
        for i in self.upstream:
            pool.add_instruction(i, Context(Data()))

        pool.start()

        sets = []
        while not pool.is_idle():
            completed = pool.get_completed()
            sets += [x.output for x in completed]
        ctx = Context.merge(sets, merge_rows=False)

        for i in self.ops:
            ctx = self.exec(i, ctx)

        end = time.perf_counter()
        logging.debug(f'InstructionSet {self.id} - {end - start}')

        return ctx
