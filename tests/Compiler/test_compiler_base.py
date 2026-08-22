from Hql.Compiler.Compiler import Compiler
from Hql.Expressions.Literals import Integer
from Hql.Operators.Count import Count
from Hql.Operators.Take import Take
from Hql.Operators.Where import Where
from Hql.Expressions.Logic import Equality
from Hql.Expressions.References import NamedReference


class TestCompilerInit:
    def test_type_matches_class_name(self):
        assert Compiler().type == "Compiler"

    def test_empty_ops_and_stmts(self):
        c = Compiler()
        assert c.ops == []
        assert c.stmts == []


class TestFromName:
    def test_dispatches_to_method(self):
        c = Compiler()
        # `Where` is a real method on Compiler that returns (None, op)
        method = c.from_name("Where")
        assert callable(method)


class TestAddOp:
    def test_default_rejects_op(self):
        c = Compiler()
        w = Where(Equality(NamedReference("f"), Integer(5)))
        acc, rej = c.add_op(w)
        assert acc is None
        assert rej is w


class TestAddOps:
    def test_returns_all_ops_since_all_rejected(self):
        c = Compiler()
        ops = [
            Where(Equality(NamedReference("f"), Integer(1))),
            Take(Integer(5), []),
        ]
        rejected = c.add_ops(ops)
        assert rejected is not None
        assert len(rejected) == 2


class TestOptimize:
    def test_returns_unchanged_by_default(self):
        c = Compiler()
        ops = [Count()]
        assert c.optimize(ops) is ops
