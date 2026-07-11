import datetime

import pytest

from Hql.Expressions.Literals import (
    Bool,
    Datetime,
    Float,
    IP4,
    Integer,
    Literal,
    MultiString,
    Null,
    StringLiteral,
    TypeExpression,
)
from Hql.Types.Hql import HqlTypes as hqlt


# ---------------------------------------------------------------------------
# TypeExpression
# ---------------------------------------------------------------------------

class TestTypeExpression:
    def test_from_string_name_stores_class_not_instance(self):
        # NOTE: hqlt.from_name returns the class object, not an instance.
        # Documenting current behavior; deparse() breaks as a result (see xfail below).
        te = TypeExpression("int")
        assert te.hql_type is hqlt.int

    def test_from_hql_type_instance(self):
        te = TypeExpression(hqlt.int())
        assert isinstance(te.hql_type, hqlt.int)

    def test_equality_by_hql_type(self):
        assert TypeExpression(hqlt.int()) == TypeExpression(hqlt.int())
        assert TypeExpression(hqlt.int()) != TypeExpression(hqlt.float())

    def test_deparse_returns_type_name(self):
        assert TypeExpression(hqlt.int()).deparse() == "int"

    @pytest.mark.xfail(
        reason="hqlt.from_name returns the class not an instance, so deparse crashes"
    )
    def test_deparse_from_string_name(self):
        assert TypeExpression("int").deparse() == "int"


# ---------------------------------------------------------------------------
# StringLiteral
# ---------------------------------------------------------------------------

class TestStringLiteral:
    def test_stores_value_as_bytes(self):
        assert StringLiteral("foo").value == b"foo"

    def test_accepts_bytes_directly(self):
        assert StringLiteral(b"foo").value == b"foo"

    def test_equality_by_value(self):
        assert StringLiteral("foo") == StringLiteral("foo")
        assert StringLiteral("foo") != StringLiteral("bar")

    def test_bool_is_false_on_empty(self):
        assert not StringLiteral("")
        assert StringLiteral("foo")

    def test_deparse_single_quotes_plain(self):
        assert StringLiteral("foo").deparse() == "'foo'"

    def test_deparse_verbatim_uses_at_prefix(self):
        assert StringLiteral("foo", verbatim=True).deparse() == "@'foo'"

    def test_deparse_verbatim_multiline_uses_triple_quotes(self):
        result = StringLiteral("foo\nbar", verbatim=True).deparse()
        assert result == "'''foo\nbar'''"

    def test_deparse_obfuscated_prefixes_h(self):
        assert StringLiteral("foo", obfuscated=True).deparse() == "h'foo'"

    def test_startswith_case_sensitive(self):
        assert StringLiteral("foobar").startswith(StringLiteral("foo"))
        assert not StringLiteral("foobar").startswith(StringLiteral("FOO"))

    def test_startswith_case_insensitive(self):
        assert StringLiteral("foobar").startswith(StringLiteral("FOO"), cs=False)

    def test_endswith_case_sensitive(self):
        assert StringLiteral("foobar").endswith(StringLiteral("bar"))
        assert not StringLiteral("foobar").endswith(StringLiteral("BAR"))

    def test_contains_case_insensitive(self):
        assert StringLiteral("foobar").contains(StringLiteral("OOB"), cs=False)

    def test_cmp_case_insensitive(self):
        assert StringLiteral("FOO").cmp(StringLiteral("foo"), cs=False)
        assert not StringLiteral("FOO").cmp(StringLiteral("foo"), cs=True)


# ---------------------------------------------------------------------------
# MultiString
# ---------------------------------------------------------------------------

class TestMultiString:
    def test_str_concatenates_component_values(self):
        ms = MultiString([StringLiteral("foo"), StringLiteral("bar")])
        assert ms.str() == "foobar"

    def test_deparse_joins_with_space(self):
        ms = MultiString([StringLiteral("foo"), StringLiteral("bar")])
        assert ms.deparse() == "'foo' 'bar'"

    def test_empty_default(self):
        assert MultiString().strlits == []
        assert MultiString().str() == ""


# ---------------------------------------------------------------------------
# Integer
# ---------------------------------------------------------------------------

class TestInteger:
    def test_from_int(self):
        assert Integer(5).value == 5

    def test_from_string(self):
        assert Integer("42").value == 42

    def test_equality(self):
        assert Integer(5) == Integer(5)
        assert Integer(5) != Integer(6)

    def test_hash_matches_equality(self):
        assert hash(Integer(5)) == hash(Integer(5))

    def test_deparse_uses_str_value(self):
        assert Integer(5).deparse() == "5"


# ---------------------------------------------------------------------------
# Float
# ---------------------------------------------------------------------------

class TestFloat:
    def test_from_float(self):
        assert Float(3.14).value == 3.14

    def test_from_string(self):
        assert Float("3.14").value == 3.14

    def test_equality(self):
        assert Float(1.5) == Float(1.5)
        assert Float(1.5) != Float(1.6)


# ---------------------------------------------------------------------------
# Bool
# ---------------------------------------------------------------------------

class TestBool:
    def test_stores_value(self):
        assert Bool(True).value is True
        assert Bool(False).value is False

    def test_equality(self):
        assert Bool(True) == Bool(True)
        assert Bool(True) != Bool(False)

    def test_hash_matches_equality(self):
        assert hash(Bool(True)) == hash(Bool(True))


# ---------------------------------------------------------------------------
# IP4
# ---------------------------------------------------------------------------

class TestIP4:
    def test_from_string_literal_round_trips(self):
        ip = IP4(StringLiteral("192.168.1.1"))
        assert ip.str() == "192.168.1.1"

    def test_deparse_uses_ip4_wrapper(self):
        assert IP4(StringLiteral("10.0.0.1")).deparse() == "ip4('10.0.0.1')"

    def test_equality(self):
        left = IP4(StringLiteral("10.0.0.1"))
        right = IP4(StringLiteral("10.0.0.1"))
        assert left == right


# ---------------------------------------------------------------------------
# Datetime
# ---------------------------------------------------------------------------

class TestDatetime:
    def test_from_datetime_instance(self):
        dt = datetime.datetime(2024, 1, 2, 3, 4, 5)
        assert Datetime(dt).value == dt

    def test_deparse_uses_isoformat(self):
        dt = datetime.datetime(2024, 1, 2, 3, 4, 5)
        result = Datetime(dt).deparse()
        assert result == "datetime(2024-01-02T03:04:05)"


# ---------------------------------------------------------------------------
# Null
# ---------------------------------------------------------------------------

class TestNull:
    def test_value_is_none(self):
        assert Null().value is None

    def test_is_literal(self):
        assert isinstance(Null(), Literal)


# ---------------------------------------------------------------------------
# Multivalue
# ---------------------------------------------------------------------------

class TestMultivalue:
    @pytest.mark.skip(
        reason="Multivalue.__init__ references self.hql_type before it is set"
    )
    def test_construction(self):
        pass
