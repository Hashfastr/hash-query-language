from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from typing import Optional, Sequence, Union

@register_func('product')
class product(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions.References import Reference
        from Hql.Expressions.Literals import StringLiteral
        Function.__init__(self, args, 1, -1)

        self.names:Sequence[Union[Reference, StringLiteral]] = []
        for i in args:
            assert isinstance(i, (Reference, StringLiteral))
            self.names.append(i)
        
    def eval(self, ctx: 'Context', receiver=None) -> object:
        from Hql.Hac import Source
        from Hql.Expressions.Literals import StringLiteral

        src = Source(ctx)

        for i in self.names:
            arg = i.preprocess(ctx)

            if not isinstance(arg, StringLiteral):
                raise hqle.QueryException(f"Invalid argument type passed to function service {type(i)} eval'd to {type(arg)}")
            src.category(arg.str())

        return src
