from copy import deepcopy

from Hql.Expressions.Functions import DotFuncExpr, FuncExpr, ReceiverFuncExpr
from Hql.Expressions.Literals import Integer
from Hql.Expressions.References import NamedReference


# ---------------------------------------------------------------------------
# FuncExpr
# ---------------------------------------------------------------------------

class TestFuncExpr:
    def test_default_args_empty(self):
        fe = FuncExpr(NamedReference("count"))
        assert fe.args == []

    def test_deparse_no_args(self):
        fe = FuncExpr(NamedReference("count"))
        assert fe.deparse() == "count()"

    def test_deparse_single_arg(self):
        fe = FuncExpr(NamedReference("count"), [NamedReference("x")])
        assert fe.deparse() == "count(x)"

    def test_deparse_multiple_args(self):
        fe = FuncExpr(
            NamedReference("add"),
            [Integer(1), Integer(2)],
        )
        assert fe.deparse() == "add(1, 2)"


# ---------------------------------------------------------------------------
# ReceiverFuncExpr
# ---------------------------------------------------------------------------

class TestReceiverFuncExpr:
    def test_deparse_dots_call_on_receiver(self):
        rfe = ReceiverFuncExpr(
            NamedReference("obj"),
            FuncExpr(NamedReference("method"), [NamedReference("x")]),
        )
        assert rfe.deparse() == "obj.method(x)"


# ---------------------------------------------------------------------------
# DotFuncExpr
# ---------------------------------------------------------------------------

class TestDotFuncExpr:
    def test_single_func_collapses(self):
        fe = FuncExpr(NamedReference("count"))
        result = DotFuncExpr([fe])
        assert result is fe

    def test_deparse_joins_with_dots(self):
        f1 = FuncExpr(NamedReference("a"))
        f2 = FuncExpr(NamedReference("b"), [Integer(1)])
        dfe = DotFuncExpr([f1, f2])
        assert dfe.deparse() == "a().b(1)"


# ---------------------------------------------------------------------------
# Deepcopy regression
# ---------------------------------------------------------------------------

class TestDeepcopy:
    def test_funcexpr_deepcopy(self):
        f = FuncExpr(NamedReference("count"), [NamedReference("x")])
        c = deepcopy(f)
        assert c is not f
        assert c.deparse() == f.deparse()

    def test_dotfuncexpr_deepcopy(self):
        name = NamedReference("test")
        dfe = DotFuncExpr([FuncExpr(name), FuncExpr(name)])
        c = deepcopy(dfe)
        assert c is not dfe
        assert c.deparse() == dfe.deparse()

    def test_receiverfuncexpr_deepcopy(self):
        rfe = ReceiverFuncExpr(
            NamedReference("obj"),
            FuncExpr(NamedReference("m"), [NamedReference("x")]),
        )
        c = deepcopy(rfe)
        assert c is not rfe
        assert c.deparse() == rfe.deparse()
