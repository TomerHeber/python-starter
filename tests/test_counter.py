from unittest import TestCase
from unittest.mock import patch

from sample.counter import Counter, dec_metric, inc_metric


class TestCounter(TestCase):
    def setUp(self):
        self.counter = Counter()

    @patch.object(inc_metric, "inc")
    def test_inc(self, inc):
        assert self.counter.val == 0
        self.counter.inc()
        assert self.counter.val == 1
        inc.assert_called_once()

    @patch.object(dec_metric, "inc")
    def test_dec(self, inc):
        assert self.counter.val == 0
        self.counter.dec()
        assert self.counter.val == -1
        inc.assert_called_once()
