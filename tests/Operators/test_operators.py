import pytest

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions import OpParameter
from Hql.Expressions.Aggregation import OrderedExpression
from Hql.Expressions.Literals import Integer, StringLiteral
from Hql.Expressions.Logic import BinaryLogic, Equality
from Hql.Expressions.References import NamedReference, Wildcard
from Hql.Operators.Count import Count
from Hql.Operators.Operator import Operator
from Hql.Operators.Project import (
    Project,
    ProjectAway,
    ProjectKeep,
    ProjectRename,
    ProjectReorder,
)
from Hql.Operators.Sort import Sort
from Hql.Operators.Take import Take
from Hql.Operators.Unnest import Unnest
from Hql.Operators.Where import Where


# ---------------------------------------------------------------------------
# Operator base
# ---------------------------------------------------------------------------

class TestOperatorBase:
    def test_has_random_id(self):
        op1 = Operator()
        op2 = Operator()
        assert op1.id != op2.id
        assert len(op1.id) == 8

    def test_default_flags(self):
        op = Operator()
        assert op.exprs == []
        assert op.tabular is False
        assert op.expr is None

    def test_to_dict_omits_missing_expr(self):
        op = Operator()
        d = op.to_dict()
        assert "expression" not in d
        assert d["id"] == op.id

    def test_has_method(self):
        op = Operator()
        op.methods = ["foo"]
        assert op.has_method("foo")
        assert not op.has_method("bar")

    def test_can_integrate(self):
        op = Operator()
        op.compatible = ["Where"]
        assert op.can_integrate("Where")
        assert not op.can_integrate("Sort")


# ---------------------------------------------------------------------------
# Where
# ---------------------------------------------------------------------------

class TestWhere:
    def test_deparse_bare(self):
        w = Where(Equality(NamedReference("f"), Integer(5)))
        assert w.deparse() == "where f == 5"

    def test_deparse_with_parameter(self):
        w = Where(
            Equality(NamedReference("f"), Integer(5)),
            params=[OpParameter(NamedReference("kind"), StringLiteral("a"))],
        )
        assert w.deparse() == "where kind='a' f == 5"

    def test_setter_rejects_non_logic(self):
        w = Where(Equality(NamedReference("f"), Integer(5)))
        with pytest.raises(hqle.CompilerException):
            w.expr = NamedReference("x")  # type: ignore[assignment]

    def test_integrate_merges_where(self):
        w1 = Where(Equality(NamedReference("a"), Integer(1)))
        w2 = Where(Equality(NamedReference("b"), Integer(2)))
        assert w1.integrate(w2) is None
        assert isinstance(w1.expr, BinaryLogic)

    def test_integrate_returns_non_where(self):
        w = Where(Equality(NamedReference("a"), Integer(1)))
        other = Count()
        assert w.integrate(other) is other


# ---------------------------------------------------------------------------
# Sort
# ---------------------------------------------------------------------------

class TestSort:
    def test_deparse(self):
        s = Sort([OrderedExpression(NamedReference("x"), order="desc")])
        assert s.deparse() == "sort by x desc"

    def test_setter_rejects_non_ordered_expression(self):
        s = Sort([OrderedExpression(NamedReference("x"), order="desc")])
        with pytest.raises(hqle.CompilerException):
            s.exprs = [NamedReference("y")]  # type: ignore[list-item]


# ---------------------------------------------------------------------------
# Project + subclasses
# ---------------------------------------------------------------------------

class TestProject:
    def test_project_deparse(self):
        p = Project([NamedReference("a"), NamedReference("b")])
        assert p.deparse() == "project a, b"

    def test_project_keep_deparse(self):
        p = ProjectKeep([NamedReference("a")])
        assert p.deparse() == "project-keep a"

    def test_project_away_deparse(self):
        p = ProjectAway([NamedReference("a")])
        assert p.deparse() == "project-away a"

    def test_project_reorder_deparse(self):
        p = ProjectReorder([NamedReference("a")])
        assert p.deparse() == "project-reorder a"

    def test_project_rename_deparse(self):
        p = ProjectRename([NamedReference("a")])
        assert p.deparse() == "project-rename a"

    def test_empty_deparse(self):
        p = Project([])
        assert p.deparse() == "project"

    def test_setter_rejects_non_expression(self):
        p = Project([NamedReference("a")])
        with pytest.raises(hqle.CompilerException):
            p.exprs = ["not an expression"]  # type: ignore[list-item]


# ---------------------------------------------------------------------------
# Count
# ---------------------------------------------------------------------------

class TestCount:
    def test_deparse_bare(self):
        assert Count().deparse() == "count"

    def test_deparse_with_name(self):
        assert Count(NamedReference("total")).deparse() == "count as total"

    def test_to_dict_includes_name_when_set(self):
        d = Count(NamedReference("total")).to_dict()
        assert d.get("name") == "total"

    def test_to_dict_omits_name_when_unset(self):
        d = Count().to_dict()
        assert "name" not in d


# ---------------------------------------------------------------------------
# Take
# ---------------------------------------------------------------------------

class TestTake:
    def test_deparse_no_tables(self):
        t = Take(Integer(5), [])
        assert t.deparse() == "take 5"

    def test_deparse_with_tables(self):
        t = Take(Integer(5), [NamedReference("a"), NamedReference("b")])
        assert t.deparse() == "take 5 from a, b"

    def test_to_dict_shape(self):
        t = Take(Integer(5), [NamedReference("a")])
        d = t.to_dict()
        assert d["type"] == "Take"
        assert d["limit"]["value"] == 5
        assert len(d["tables"]) == 1


# ---------------------------------------------------------------------------
# Unnest
# ---------------------------------------------------------------------------

class TestUnnest:
    def test_deparse_no_tables(self):
        u = Unnest(NamedReference("field"), [])
        assert u.deparse() == "unnest field"

    def test_deparse_with_tables(self):
        u = Unnest(NamedReference("field"), [NamedReference("t1")])
        assert u.deparse() == "unnest field on t1"

    def test_gets_all_detects_wildcard(self):
        from Hql.Context import Context
        from Hql.Data import Data

        ctx = Context(data=Data())
        assert Unnest(NamedReference("f"), [Wildcard("*")]).gets_all(ctx) is True
        assert Unnest(NamedReference("f"), [NamedReference("t1")]).gets_all(ctx) is False
