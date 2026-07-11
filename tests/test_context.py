import pytest

from Hql.Context import (
    Context,
    get_func,
    get_type,
    register_func,
    register_type,
    type_registry,
)
from Hql.Data import Data
from Hql.Exceptions import HqlExceptions as hqle


class TestTypeRegistry:
    def test_get_type_returns_registered_class(self):
        # int is registered on import as "hql_int"
        assert get_type("hql_int") is not None

    def test_get_type_unknown_raises(self):
        with pytest.raises(hqle.CompilerException):
            get_type("hql_definitely_not_a_type")

    def test_register_type_stores_class(self):
        @register_type("hql_test_registration_marker")
        class _Marker:
            pass

        assert type_registry["hql_test_registration_marker"] is _Marker
        del type_registry["hql_test_registration_marker"]


class TestFuncRegistry:
    def test_get_func_unknown_raises(self):
        with pytest.raises(hqle.CompilerException):
            get_func("definitely_not_a_func")

    def test_register_func_rejects_non_function(self):
        with pytest.raises(hqle.CompilerException):
            @register_func("bad_registration_marker")
            class _NotAFunction:
                pass


class TestContext:
    def test_default_construction(self):
        ctx = Context(data=Data())
        assert ctx.data is not None
        assert ctx.symbol_table == {}
        assert ctx.macros == {}

    def test_bool_reflects_data(self):
        assert not Context(data=Data())

    def test_copy_preserves_data_reference(self):
        d = Data()
        ctx = Context(data=d)
        copy = ctx.copy()
        assert copy.data is d

    def test_get_func_unknown_raises(self):
        ctx = Context(data=Data())
        with pytest.raises(hqle.CompilerException):
            ctx.get_func("nonexistent_ctx_func")

    def test_get_db_types_returns_list(self):
        ctx = Context(data=Data())
        assert isinstance(ctx.get_db_types(), list)

    def test_symbol_table_isolated_across_copies(self):
        # constructor deepcopies, so mutating copy shouldn't touch original
        original = {"x": 1}
        ctx = Context(data=Data(), symbol_table=original)
        ctx.symbol_table["x"] = 99
        assert original["x"] == 1
