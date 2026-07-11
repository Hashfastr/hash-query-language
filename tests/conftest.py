import pytest

from Hql.Context import Context
from Hql.Data import Data


@pytest.fixture
def empty_ctx() -> Context:
    return Context(data=Data(), symbol_table={})
