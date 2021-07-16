from unittest import TestCase

from sample.sample import Counter


class TestCounter(TestCase):
    def setUp(self):
        self.counter = Counter()

    def test_inc(self):
        assert self.counter.val == 0
        self.counter.inc()
        assert self.counter.val == 1

    def test_dec(self):
        assert self.counter.val == 0
        self.counter.dec()
        assert self.counter.val == -1
