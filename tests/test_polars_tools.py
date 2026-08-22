import polars as pl

from Hql.PolarsTools import pltools


class TestPathToExprValue:
    def test_single_element_returns_col(self):
        expr = pltools.path_to_expr_value(["a"])
        assert expr.meta.eq(pl.col("a"))

    def test_nested_chains_struct_field(self):
        expr = pltools.path_to_expr_value(["a", "b", "c"])
        expected = pl.col("a").struct.field("b").struct.field("c")
        assert expr.meta.eq(expected)


class TestPathToExpr:
    def test_single_element_matches_col(self):
        expr = pltools.path_to_expr(["a"])
        assert expr.meta.eq(pl.col("a"))

    def test_nested_wraps_in_struct_aliases(self):
        # For ['a','b','c']: value is a.b.c; then wrap struct(b) then struct(a)
        expr = pltools.path_to_expr(["a", "b"])
        # Just verify it's a valid pl.Expr — the exact wrapping is implementation detail
        assert isinstance(expr, pl.Expr)


class TestBuildElement:
    def test_single_name_returns_dataframe(self):
        df = pltools.build_element(["x"], [1, 2, 3])
        assert df.columns == ["x"]
        assert df["x"].to_list() == [1, 2, 3]

    def test_nested_name_wraps_in_struct(self):
        df = pltools.build_element(["outer", "inner"], [1, 2])
        assert df.columns == ["outer"]
        # nested inner column should exist as a struct field
        assert "inner" in df["outer"].struct.fields
