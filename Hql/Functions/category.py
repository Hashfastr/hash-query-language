from . import Function
from Hql.Exceptions import HqlExceptions as hqle
from Hql.Context import register_func, Context
from typing import Optional, Sequence, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Hql.Hac import Source

@register_func('category')
class category(Function):
    def __init__(self, args:list, conf:Optional[dict]=None):
        from Hql.Expressions.References import Reference
        from Hql.Expressions.Literals import StringLiteral
        Function.__init__(self, args, 1, -1)

        self.names:Sequence[Union[Reference, StringLiteral]] = []
        for i in args:
            assert isinstance(i, (Reference, StringLiteral))
            self.names.append(i)

    def preprocess(self, ctx: 'Context', receiver=None) -> 'Source':
        from Hql.Hac import Source
        from Hql.Expressions.Literals import StringLiteral

        src = receiver
        if not src:
            src = Source(ctx)
            src.product('*')

        if not isinstance(src, Source):
            raise hqle.CompilerException(f'Expected Source got {type(src)} for category preprocess')

        for i in self.names:
            arg = i.preprocess(ctx)

            if not isinstance(arg, StringLiteral):
                raise hqle.QueryException(f"Invalid argument type passed to function category {type(i)} eval'd to {type(arg)}")

            matched = src.category(arg.str())
            if not matched:
                src.category_standalone(arg.str())

        return src
