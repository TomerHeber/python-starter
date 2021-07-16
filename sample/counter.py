from prometheus_client import Counter

inc_metric = Counter("counter_increments", "Counter increments count")
dec_metric = Counter("counter_decrements", "Counter decrements count")


class Counter:
    def __init__(self):
        self.val = 0

    def inc(self):
        self.val = self.val + 1
        inc_metric.inc()

    def dec(self):
        self.val = self.val - 1
        dec_metric.inc()
