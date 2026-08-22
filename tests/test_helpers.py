from Hql.Helpers import can_thread


class TestCanThread:
    def test_returns_bool(self):
        assert isinstance(can_thread(), bool)
