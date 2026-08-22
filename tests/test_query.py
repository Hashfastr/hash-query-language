from Hql.Expressions import PipeExpression
from Hql.Expressions.References import NamedReference
from Hql.Query import LetStatement, Query, QueryStatement, Statement


class TestStatement:
    def test_default_deparse_is_empty(self):
        assert Statement().deparse() == ""

    def test_type_marker(self):
        assert Statement().type == "Statement"


class TestQueryStatement:
    def test_deparse_delegates_to_root(self):
        root = PipeExpression([])
        qs = QueryStatement(root)
        assert qs.deparse() == root.deparse()

    def test_to_dict_includes_query(self):
        qs = QueryStatement(PipeExpression([]))
        d = qs.to_dict()
        assert d["type"] == "QueryStatement"
        assert "query" in d


class TestLetStatement:
    def test_deparse(self):
        ls = LetStatement(NamedReference("x"), PipeExpression([]))
        assert ls.deparse() == "let x = "

    def test_default_macro_false(self):
        ls = LetStatement(NamedReference("x"), PipeExpression([]))
        assert ls.macro is False

    def test_to_dict_shape(self):
        ls = LetStatement(NamedReference("x"), PipeExpression([]))
        d = ls.to_dict()
        assert d["type"] == "LetStatement"
        assert d["macro"] is False


class TestQuery:
    def test_stores_statements(self):
        s = QueryStatement(PipeExpression([]))
        q = Query([s])
        assert q.statements == [s]

    def test_to_dict_shape(self):
        q = Query([QueryStatement(PipeExpression([]))])
        d = q.to_dict()
        assert "statements" in d
        assert len(d["statements"]) == 1

    def test_deparse_single_statement(self):
        q = Query([QueryStatement(PipeExpression([]))])
        # No let statements, no context, so just the one deparse
        assert q.deparse() == ""
