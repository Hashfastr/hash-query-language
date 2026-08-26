from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Expressions import Expression
    from Hql.Operators.Operator import Operator

from typing import Optional, Union

class SplunkOp():
    """Base class for intermediate Splunk pipeline operations."""

    def __init__(self):
        self.type = self.__class__.__name__
        self.pipes = []
        self.post_ops:list[Operator] = []
        self.remap = dict()

    def compile(self):
        ...

class Spath(SplunkOp):
    """Represent a Splunk field extraction between two expressions."""

    def __init__(self, lh:Expression, rh:Expression):
        SplunkOp.__init__(self)
        self.lh = lh
        self.rh = rh
