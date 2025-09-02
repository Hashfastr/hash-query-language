from typing import TYPE_CHECKING, Union
from Hql.Context import Context
import logging
import time

if TYPE_CHECKING:
    from Hql.Operators import Database, Operator
    from . import BranchDescriptor

class InstructionSet():
    def __init__(self, upstream:Union['Database', list['Database'], 'InstructionSet', list['InstructionSet']], operators:Union[None, list['Operator']]=None) -> None:
        import random

        if isinstance(upstream, list):
            self.upstream = upstream
        else:
            self.upstream = [upstream]

        self.ops:list['Operator'] = operators if operators else []
        self.id = '%08x' % random.getrandbits(32)
        self.attrs = dict()

    def add_op(self, op:Union['BranchDescriptor', 'Operator']):
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

    def eval(self, ctx:Context, **kwargs) -> Context:
        from Hql.Data import Data

        logging.debug(f'Starting InstructionSet {self.id}')
        start = time.perf_counter()

        sets = []
        for i in self.upstream:
            sets.append(i.eval(Context(Data())))

        ctx = Context.merge(sets)

        for i in self.ops:
            ctx = self.exec(i, ctx)

        end = time.perf_counter()
        logging.debug(f'InstructionSet {self.id} - {end - start}')

        return ctx
