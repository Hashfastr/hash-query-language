import pytest
import polars as pl

from Hql.Context import Context
from Hql.Expressions.References import (
    EscapedNamedReference,
    NamedExpression,
    NamedReference,
    Path,
    Wildcard,
)
from Hql.Functions import Function


# ---------------------------------------------------------------------------
# NamedReference
# ---------------------------------------------------------------------------

class TestNamedReference:
    def test_list_returns_single_name(self):
        assert NamedReference("foo").list() == ["foo"]

    def test_deparse_returns_name(self):
        assert NamedReference("foo").deparse() == "foo"

    def test_equality_by_name(self):
        assert NamedReference("foo") == NamedReference("foo")
        assert NamedReference("foo") != NamedReference("bar")

    def test_hash_matches_equality(self):
        assert hash(NamedReference("foo")) == hash(NamedReference("foo"))

    def test_polars_returns_col(self):
        expected = pl.col("foo")
        assert NamedReference("foo").polars().meta.eq(expected)


# ---------------------------------------------------------------------------
# Wildcard
# ---------------------------------------------------------------------------

class TestWildcard:
    def test_is_named_reference(self):
        assert isinstance(Wildcard("*"), NamedReference)

    def test_deparse_preserves_name(self):
        assert Wildcard("*").deparse() == "*"


# ---------------------------------------------------------------------------
# EscapedNamedReference
# ---------------------------------------------------------------------------

class TestEscapedNamedReference:
    def test_deparse_wraps_in_brackets_and_quotes(self):
        assert EscapedNamedReference("foo").deparse() == "['foo']"

    def test_deparse_escapes_embedded_quote(self):
        assert EscapedNamedReference("f'o").deparse() == r"['f\\'o']"


# ---------------------------------------------------------------------------
# Path
# ---------------------------------------------------------------------------

class TestPath:
    def test_single_element_collapses_to_named_reference(self):
        ref = NamedReference("foo")
        result = Path([ref])
        assert result is ref
        assert isinstance(result, NamedReference)

    def test_condense_flattens_nested_paths(self):
        inner = Path([NamedReference("b"), NamedReference("c")])
        outer = Path([NamedReference("a"), inner])
        assert outer.list() == ["a", "b", "c"]

    def test_list_returns_string_components(self):
        p = Path([NamedReference("a"), NamedReference("b")])
        assert p.list() == ["a", "b"]

    def test_deparse_joins_with_dot(self):
        p = Path([NamedReference("a"), NamedReference("b")])
        assert p.deparse() == "a.b"

    def test_equality_same_path(self):
        left = Path([NamedReference("a"), NamedReference("b")])
        right = Path([NamedReference("a"), NamedReference("b")])
        assert left == right

    def test_inequality_different_length(self):
        left = Path([NamedReference("a"), NamedReference("b")])
        right = Path([NamedReference("a"), NamedReference("b"), NamedReference("c")])
        assert left != right

    def test_inequality_different_names(self):
        left = Path([NamedReference("a"), NamedReference("b")])
        right = Path([NamedReference("a"), NamedReference("x")])
        assert left != right

    def test_polars_value_chains_struct_field(self):
        p = Path([NamedReference("a"), NamedReference("b"), NamedReference("c")])
        expected = pl.col("a").struct.field("b").struct.field("c")
        assert p.polars_value().meta.eq(expected)

    def test_preprocess_returns_self_when_symbol_missing(self, empty_ctx: Context):
        p = Path([NamedReference("missing"), NamedReference("x")])
        assert p.preprocess(empty_ctx) is p

    def test_preprocess_walks_dict_symbol_to_leaf(self, empty_ctx: Context):
        empty_ctx.symbol_table["foo"] = {"bar": "baz"}
        p = Path([NamedReference("foo"), NamedReference("bar")])
        assert p.preprocess(empty_ctx) == "baz"


# ---------------------------------------------------------------------------
# NamedExpression
# ---------------------------------------------------------------------------

class _NoopFunction(Function):
    """Minimal Function subclass for tests that need a Function instance."""

    def __init__(self):
        Function.__init__(self, args=[], min=0, max=0)


class TestNamedExpression:
    def test_deparse_single_target(self):
        ne = NamedExpression([NamedReference("out")], NamedReference("src"))
        assert ne.deparse() == "out=src"

    def test_deparse_multiple_targets(self):
        ne = NamedExpression(
            [NamedReference("a"), NamedReference("b")],
            NamedReference("src"),
        )
        assert ne.deparse() == "a, b=src"

    def test_equality_is_order_insensitive_on_paths(self):
        left = NamedExpression(
            [NamedReference("a"), NamedReference("b")],
            NamedReference("src"),
        )
        right = NamedExpression(
            [NamedReference("b"), NamedReference("a")],
            NamedReference("src"),
        )
        assert left == right

    def test_inequality_on_different_value(self):
        left = NamedExpression([NamedReference("a")], NamedReference("x"))
        right = NamedExpression([NamedReference("a")], NamedReference("y"))
        assert left != right

    def test_hash_matches_equality(self):
        left = NamedExpression(
            [NamedReference("a"), NamedReference("b")],
            NamedReference("src"),
        )
        right = NamedExpression(
            [NamedReference("b"), NamedReference("a")],
            NamedReference("src"),
        )
        assert hash(left) == hash(right)

    def test_can_polars_true_for_expression_value(self):
        ne = NamedExpression([NamedReference("a")], NamedReference("src"))
        assert ne.can_polars() is True

    def test_can_polars_false_for_function_value(self):
        ne = NamedExpression([NamedReference("a")], _NoopFunction())
        assert ne.can_polars() is False

    @pytest.mark.skip(reason="TODO: needs Data/Table fixture")
    def test_eval_inserts_value(self):
        pass
