from Hql.Expressions import OpParameter, ToClause
from Hql.Expressions.Literals import Integer, TypeExpression
from Hql.Expressions.References import NamedReference
from Hql.Types.Hql import HqlTypes as hqlt


# ---------------------------------------------------------------------------
# OpParameter
# ---------------------------------------------------------------------------

class TestOpParameter:
    def test_deparse(self):
        op = OpParameter(NamedReference("limit"), Integer(10))
        assert op.deparse() == "limit=10"


# ---------------------------------------------------------------------------
# ToClause
# ---------------------------------------------------------------------------

class TestToClause:
    def test_stores_hql_type_from_type_expression(self):
        tc = ToClause(NamedReference("x"), TypeExpression(hqlt.int()))
        assert isinstance(tc.to, hqlt.int)

    def test_stores_hql_type_directly(self):
        tc = ToClause(NamedReference("x"), hqlt.int())
        assert isinstance(tc.to, hqlt.int)

    def test_deparse(self):
        tc = ToClause(NamedReference("x"), hqlt.int())
        assert tc.deparse() == "x to int"
