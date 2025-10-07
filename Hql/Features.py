from typing import TYPE_CHECKING, Union
import logging

from Hql.Exceptions import HqlExceptions as hqle

if TYPE_CHECKING:
    import Hql.Expressions as Expr
    import Hql.Operators as Ops

class FeatureSet():
    def __init__(self) -> None:
        self.name = type(self).__name__
        
        self.features = []
        self.split_and = True

    def supported(self, expr:Union["Expr.Expression", "Ops.Operator"]) -> bool:
        etype = type(expr)

        # Check for exact matches
        if etype in self.features:
            return True

        # Check for subclass matches, e.g. NamedReference variations
        if issubclass(etype, tuple(self.features)):
            return True

        return False

    '''
    Returns a tuple such that

    (Accepted, Rejected)

    Allowing splitage of features to show you where things are
    Probably stupid
    '''
    def validate_feature(self, expr:Union["Expr.Expression", "Ops.Operator"]) \
            -> tuple[Union[None, "Expr.Expression", "Ops.Operator"], Union[None, "Expr.Expression", "Ops.Operator"]]:
        import Hql.Expressions as Expr

        if not self.supported(expr):
            logging.debug(f'{type(expr)} not supported in featureset {self.name}')
            return (None, expr)

        if self.split_and and isinstance(expr, Expr.BinaryLogic):
            if expr.bitype == 'and':
                acc_expr = None
                rej_expr = None

                exprs = [expr.lh] + expr.rh

                for i in exprs:
                    acc, rej = self.validate_feature(i)

                    if isinstance(acc, Ops.Operator) or isinstance(rej, Ops.Operator):
                        raise hqle.CompilerException("Nested Operators? in an and?")

                    if acc and not acc_expr:
                        acc_expr = Expr.BinaryLogic(acc, [], 'and')

                    elif acc and acc_expr:
                        acc_expr.rh.append(acc)

                    if rej and not rej_expr:
                        rej_expr = Expr.BinaryLogic(rej, [], 'and')

                    elif rej and rej_expr:
                        rej_expr.rh.append(rej)

                return (acc_expr, rej_expr)

        return (expr, None)

    def merge_binary(self, into:"Expr.Expression", src:Union[None, "Expr.Expression"], bitype:str) -> tuple["Expr.Expression", Union[None, "Expr.Expression"]]:
        import Hql.Expressions as Expr
        if isinstance(into, Expr.BinaryLogic) and into.bitype == bitype:
            # check for mergability
            if isinstance(src, Expr.BinaryLogic) and src.bitype == bitype:
                into.rh.append(src.lh)
                into.rh += src.rh

            elif src:
                into.rh.append(src)

            return (into, None)

        return (into, src)


class Feature():
    def __init__(self) -> None:
        ...

class Function(Feature):
    def __init__(self) -> None:
        Feature.__init__(self)
