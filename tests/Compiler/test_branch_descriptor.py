import pytest

from Hql.Compiler import BranchDescriptor
from Hql.Exceptions import HqlExceptions as hqle


class TestBranchDescriptorInit:
    def test_default_attrs_are_empty(self):
        bd = BranchDescriptor()
        assert bd.attrs == {}
        assert bd.provides == []
        assert bd.references == []
        assert bd.removes == []
        assert bd.mapping == {}
        assert bd.full_schema is False

    def test_list_attrs_seed(self):
        assert "types" in BranchDescriptor().list_attrs
        assert "functions" in BranchDescriptor().list_attrs


class TestSetAttr:
    def test_scalar_attr(self):
        bd = BranchDescriptor()
        bd.set_attr("has_time", True)
        assert bd.get_attr("has_time") is True

    def test_list_attr_scalar_promoted_to_list(self):
        bd = BranchDescriptor()
        bd.set_attr("types", "string")
        assert bd.get_attr("types") == ["string"]

    def test_list_attr_passed_as_list(self):
        bd = BranchDescriptor()
        bd.set_attr("types", ["string", "int"])
        assert bd.get_attr("types") == ["string", "int"]


class TestGetAttr:
    def test_missing_scalar_returns_none(self):
        assert BranchDescriptor().get_attr("nope") is None

    def test_missing_list_attr_returns_empty_list(self):
        assert BranchDescriptor().get_attr("types") == []


class TestMergeAttrs:
    def test_merges_new_scalar(self):
        bd = BranchDescriptor()
        bd.merge_attrs({"foo": True})
        assert bd.get_attr("foo") is True

    def test_merges_list_attr(self):
        bd = BranchDescriptor()
        bd.set_attr("types", ["a"])
        bd.merge_attrs({"types": ["b"]})
        assert bd.get_attr("types") == ["a", "b"]


class TestMerge:
    def test_appends_provides_references_removes(self):
        left = BranchDescriptor()
        left.provides = ["x"]
        left.references = ["y"]
        left.removes = ["z"]

        right = BranchDescriptor()
        right.provides = ["a"]
        right.references = ["b"]
        right.removes = ["c"]

        left.merge(right)
        assert left.provides == ["x", "a"]
        assert left.references == ["y", "b"]
        assert left.removes == ["z", "c"]


class TestCompatible:
    def test_empty_attrs_is_compatible(self):
        assert BranchDescriptor().compatible({})

    def test_missing_attr_in_superset_breaks(self):
        bd = BranchDescriptor()
        bd.set_attr("has_time", True)
        assert not bd.compatible({})

    def test_present_attr_in_superset_ok(self):
        bd = BranchDescriptor()
        bd.set_attr("has_time", True)
        assert bd.compatible({"has_time": True})


class TestGetters:
    def test_get_expr_none_raises(self):
        with pytest.raises(hqle.CompilerException):
            BranchDescriptor().get_expr()

    def test_get_op_none_raises(self):
        with pytest.raises(hqle.CompilerException):
            BranchDescriptor().get_op()

    def test_get_statement_none_raises(self):
        with pytest.raises(hqle.CompilerException):
            BranchDescriptor().get_statement()
