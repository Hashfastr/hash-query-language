from Hql.Features import FeatureSet

class ESFeatureSet(FeatureSet):
    def __init__(self) -> None:
        import Hql.Expressions as Expr
        import Hql.Operators as Ops

        FeatureSet.__init__(self)

        self.features = [
            Ops.Where,
            Ops.Take,
            Expr.NamedReference,
            Expr.Path,
            Expr.Equality,
            Expr.ListEquality,
            Expr.Relational,
            Expr.BetweenEquality,
            Expr.BinaryLogic,
            Expr.Literal
        ]
