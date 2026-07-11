from Hql.Expressions.Aggregation import ByExpression, OrderedExpression
from Hql.Expressions.References import NamedReference


# ---------------------------------------------------------------------------
# OrderedExpression
# ---------------------------------------------------------------------------

class TestOrderedExpression:
    def test_desc_implicit_nulls_last(self):
        oe = OrderedExpression(NamedReference("x"), order="desc")
        assert oe.nulls == "last"
        assert oe.implicit_nulls is True

    def test_asc_implicit_nulls_first(self):
        oe = OrderedExpression(NamedReference("x"), order="asc")
        assert oe.nulls == "first"
        assert oe.implicit_nulls is True

    def test_explicit_nulls_marks_not_implicit(self):
        oe = OrderedExpression(NamedReference("x"), order="asc", nulls="last")
        assert oe.implicit_nulls is False

    def test_deparse_implicit_nulls_omits_clause(self):
        oe = OrderedExpression(NamedReference("x"), order="desc")
        assert oe.deparse() == "x desc"

    def test_deparse_explicit_nulls_includes_clause(self):
        oe = OrderedExpression(NamedReference("x"), order="asc", nulls="last")
        assert oe.deparse() == "x asc nulls last"


# ---------------------------------------------------------------------------
# ByExpression
# ---------------------------------------------------------------------------

class TestByExpression:
    def test_deparse_single(self):
        be = ByExpression([NamedReference("a")])
        assert be.deparse() == "by a"

    def test_deparse_multiple(self):
        be = ByExpression([NamedReference("a"), NamedReference("b")])
        assert be.deparse() == "by a, b"

    def test_stores_exprs(self):
        refs = [NamedReference("a"), NamedReference("b")]
        be = ByExpression(refs)
        assert be.exprs is refs


# ---------------------------------------------------------------------------
# Deepcopy regression
# ---------------------------------------------------------------------------

class TestDeepcopy:
    def test_ordered_expression(self):
        from copy import deepcopy
        oe = OrderedExpression(NamedReference("x"), order="asc", nulls="last")
        c = deepcopy(oe)
        assert c is not oe
        assert c.deparse() == oe.deparse()

    def test_by_expression(self):
        from copy import deepcopy
        be = ByExpression([NamedReference("a"), NamedReference("b")])
        c = deepcopy(be)
        assert c is not be
        assert c.deparse() == be.deparse()
