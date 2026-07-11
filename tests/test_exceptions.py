import pytest

from Hql.Exceptions import HacExceptions as hace
from Hql.Exceptions import HqlExceptions as hqle


class TestHqlExceptions:
    def test_hql_exception_stores_type(self):
        exc = hqle.HqlException("bad")
        assert exc.type == "HqlException"
        assert str(exc) == "bad"

    def test_config_exception_default_message(self):
        exc = hqle.ConfigException()
        assert "Config error occurred" in str(exc)

    def test_argument_exception_is_function_exception(self):
        assert issubclass(hqle.ArgumentException, hqle.FunctionException)

    def test_all_subclasses_of_hql_exception(self):
        for cls in [
            hqle.ConfigException,
            hqle.FunctionException,
            hqle.ArgumentException,
            hqle.CompilerException,
            hqle.QueryException,
            hqle.UnreferencedFieldException,
        ]:
            assert issubclass(cls, hqle.HqlException)

    def test_semantic_exception_formats_line_and_col(self):
        exc = hqle.SemanticException("oops", line=3, charpos=7)
        assert "line 3:7" in str(exc)

    def test_can_raise_and_catch(self):
        with pytest.raises(hqle.CompilerException):
            raise hqle.CompilerException("nope")

    def test_decompile_string_exception_formats_types(self):
        exc = hqle.DecompileStringException(int, float)
        assert "int" in str(exc) and "float" in str(exc)


class TestHacExceptions:
    def test_hac_exception_prefixes_type(self):
        exc = hace.HacException("problem")
        assert exc.type == "HacException"
        assert "HacException: problem" in str(exc)

    def test_dag_exception_includes_name(self):
        exc = hace.DagException(name="node1", message="cycle")
        assert "node1" in str(exc) and "cycle" in str(exc)

    def test_action_exception_reads_conf(self):
        exc = hace.ActionException({"type": "notify", "action_name": "email"}, "failed")
        assert "email" in str(exc)

    def test_action_exception_falls_back_to_type(self):
        exc = hace.ActionException({"type": "notify"}, "failed")
        assert "notify" in str(exc)
