import pytest

from Hql.Data import Data
from Hql.Data.Tables import Table
from Hql.Exceptions import HqlExceptions as hqle


class TestDataEmpty:
    def test_default_construction(self):
        assert Data().tables == {}

    def test_bool_false_when_empty(self):
        assert not Data()

    def test_len_zero_when_empty(self):
        assert len(Data()) == 0

    def test_iter_yields_nothing_when_empty(self):
        assert list(Data()) == []

    def test_contains_false_when_empty(self):
        assert "anything" not in Data()

    def test_to_dict_shape(self):
        d = Data().to_dict()
        assert d == {"data": {}, "schema": {}}


class TestDataInvalidInit:
    def test_non_table_raises(self):
        with pytest.raises(hqle.CompilerException):
            Data(tables=["not a table"])  # type: ignore[list-item]


class TestDataAddTable:
    def test_add_table_stores_by_name(self):
        d = Data()
        t = Table(name="foo")
        d.add_table(t)
        assert "foo" in d
        assert d["foo"] is t

    def test_add_duplicate_raises(self):
        d = Data()
        d.add_table(Table(name="foo"))
        with pytest.raises(hqle.QueryException):
            d.add_table(Table(name="foo"))


class TestDataReplaceTable:
    def test_replace_overwrites(self):
        d = Data()
        first = Table(name="foo")
        d.add_table(first)
        second = Table(name="foo")
        d.replace_table(second)
        assert d["foo"] is second


class TestDataMerge:
    def test_single_returns_input(self):
        d = Data()
        assert Data.merge([d]) is d


class TestDataGetTables:
    def test_wildcard_matches_all(self):
        d = Data()
        d.add_table(Table(name="a"))
        d.add_table(Table(name="b"))
        assert len(d.get_tables("*")) == 2

    def test_prefix_wildcard(self):
        d = Data()
        d.add_table(Table(name="log-a"))
        d.add_table(Table(name="log-b"))
        d.add_table(Table(name="other"))
        assert {t.name for t in d.get_tables("log-*")} == {"log-a", "log-b"}
