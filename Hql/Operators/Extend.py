from typing import TYPE_CHECKING, Union
from Hql.Expressions import Expression, NamedExpression, NamedReference, Path
from Hql.Operators import Operator
from Hql.Context import register_op, Context

if TYPE_CHECKING:
    from Hql.Data import Data

# Creates a field with a value in the extend
#
# StormEvents
# | project EndTime, StartTime
# | extend Duration = EndTime - StartTime
#
# https://learn.microsoft.com/en-us/kusto/query/extend-operator
# @register_op('Extend')
class Extend(Operator):
    def __init__(self, exprs:list[Expression]):
        Operator.__init__(self)
        self.exprs = exprs

    def decompile(self, ctx: 'Context') -> str:
        return 'extend ' + ', '.join(x.decompile(ctx) for x in self.exprs)

    def remove_old(self, ctx:Context, expr:Union[NamedReference, Path], data:'Data') -> 'Data':
        path = expr.eval(ctx, as_list=True)
        assert isinstance(path, list)
        return data.drop(path)
            
    def eval(self, ctx:'Context', **kwargs):
        from Hql.Data import Data

        orig:Data = ctx.data
        data:list[Data] = []
        for i in self.exprs:
            datum = i.eval(ctx)
            assert isinstance(datum, Data)
            data.append(datum)

            if isinstance(i, NamedExpression):
                for j in i.paths:
                    assert isinstance(j, (Path, NamedReference))
                    orig = self.remove_old(ctx, j, orig)
        
        data.append(orig)
        return Data.merge(data)
