from typing import TYPE_CHECKING, Union
from Hql.Context import Context
import logging
import time
import json

if TYPE_CHECKING:
    from Hql.Operators import Database, Operator
    from Hql.Compiler import BranchDescriptor

class InstructionSet():
    def __init__(self, upstream:Union['Database', list['Database'], 'InstructionSet', list['InstructionSet']], operators:Union[None, list['Operator']]=None) -> None:
        import random
        from Hql.Operators import Database
        from Hql.Compiler import InstructionSet
        
        assert isinstance(upstream, (Database, list, InstructionSet))
        if isinstance(upstream, list):
            assert all(isinstance(item, (Database, InstructionSet)) for item in upstream)
            self.upstream = upstream
        else:
            self.upstream = [upstream]

        self.ops:list['Operator'] = operators if operators else []
        self.id = '%08x' % random.getrandbits(32)
        self.attrs = dict()

        if len(self.upstream) == 1 and isinstance(self.upstream[0], InstructionSet):
            self.ops = self.upstream[0].ops + self.ops
            self.upstream = self.upstream[0].upstream

    def to_dict(self):
        ops = []
        for i in self.ops:
            op = i.to_dict()
            op = {
                'id': op.get('id', '????'),
                'type': op.get('type')
            }
            ops.append(op)

        return {
            'id': self.id,
            'attrs': self.attrs,
            'upstream': [x.to_dict() for x in self.upstream],
            'ops': ops,
        }

    def add_op(self, op:Union['BranchDescriptor', 'Operator']):
        from Hql.Compiler import BranchDescriptor

        if isinstance(op, BranchDescriptor):
            self.ops.append(op.get_op())
        else:
            self.ops.append(op)

        return None

    def exec(self, inst:Union['Database', 'Operator'], ctx:Context) -> Context:
        logging.debug(f'Executing {inst.type} - {inst.id}')
        start = time.perf_counter()

        ctx.data = inst.eval(ctx)

        end = time.perf_counter()
        logging.debug(f'{inst.id} - {end - start}')

        return ctx

    def render(self) -> str:
        return json.dumps(self.to_dict(), indent=2)

    def eval(self, ctx:Context, **kwargs) -> Context:
        from Hql.Data import Data

        logging.debug(f'Starting InstructionSet {self.id}')
        start = time.perf_counter()

        sets = []
        for i in self.upstream:
            up = i.eval(Context(Data()))
            if isinstance(up, Data):
                up = Context(up)
            sets.append(up)

        ctx = Context.merge(sets)

        for i in self.ops:
            ctx = self.exec(i, ctx)

        end = time.perf_counter()
        logging.debug(f'InstructionSet {self.id} - {end - start}')

        return ctx
