import pytest

from Hql.Exceptions import HqlExceptions as hqle
from Hql.Expressions.Literals import Integer
from Hql.Functions import DotCompositeFunction, Function


class _FixedArity(Function):
    def __init__(self, args):
        Function.__init__(self, args, min=1, max=2)


class _AnyArity(Function):
    def __init__(self, args):
        Function.__init__(self, args, min=0, max=-1)


class _NoArgs(Function):
    def __init__(self):
        Function.__init__(self, args=[], min=0, max=0)


# ---------------------------------------------------------------------------
# Function base
# ---------------------------------------------------------------------------

class TestFunctionBase:
    def test_name_defaults_to_class_name(self):
        assert _FixedArity([Integer(1)]).name == "_FixedArity"

    def test_type_marker(self):
        assert _FixedArity([Integer(1)]).type == "Function"

    def test_too_few_args_raises(self):
        with pytest.raises(hqle.ArgumentException):
            _FixedArity([])

    def test_too_many_args_raises(self):
        with pytest.raises(hqle.ArgumentException):
            _FixedArity([Integer(1), Integer(2), Integer(3)])

    def test_unbounded_max_accepts_any(self):
        _AnyArity([Integer(i) for i in range(50)])

    def test_deparse_no_args(self):
        assert _NoArgs().deparse() == "_NoArgs()"

    def test_deparse_multiple_args(self):
        f = _FixedArity([Integer(1), Integer(2)])
        assert f.deparse() == "_FixedArity(1, 2)"

    def test_to_dict_shape(self):
        f = _FixedArity([Integer(1)])
        d = f.to_dict()
        assert d["type"] == "function"
        assert d["name"] == "_FixedArity"
        assert len(d["args"]) == 1

    def test_hash_by_name(self):
        # __hash__ uses only the class name, so equal-named instances collide
        assert hash(_NoArgs()) == hash(_NoArgs())

    def test_eval_returns_not_implemented(self):
        from Hql.Context import Context
        from Hql.Data import Data

        assert _NoArgs().eval(Context(data=Data())) is NotImplemented


# ---------------------------------------------------------------------------
# DotCompositeFunction
# ---------------------------------------------------------------------------

class TestDotCompositeFunction:
    def test_single_func_collapses(self):
        f = _NoArgs()
        result = DotCompositeFunction([f])
        assert result is f

    def test_flattens_nested_composites(self):
        f1 = _NoArgs()
        f2 = _NoArgs()
        f3 = _NoArgs()
        inner = DotCompositeFunction([f1, f2])
        outer = DotCompositeFunction([inner, f3])
        # inner should have been flattened into the outer's funcs list
        assert outer.funcs == [f1, f2, f3]

    def test_bool_reflects_funcs(self):
        f1 = _NoArgs()
        f2 = _NoArgs()
        assert DotCompositeFunction([f1, f2])

    def test_deparse_joins_with_dots(self):
        f1 = _NoArgs()
        f2 = _NoArgs()
        assert DotCompositeFunction([f1, f2]).deparse() == "_NoArgs()._NoArgs()"

    def test_to_dict_shape(self):
        f1 = _NoArgs()
        f2 = _NoArgs()
        d = DotCompositeFunction([f1, f2]).to_dict()
        assert d["type"] == "DotCompositeFunction"
        assert len(d["funcs"]) == 2

    def test_deepcopy(self):
        from copy import deepcopy
        f1 = _NoArgs()
        f2 = _NoArgs()
        dcf = DotCompositeFunction([f1, f2])
        c = deepcopy(dcf)
        assert c is not dcf
        assert len(c.funcs) == 2
