import time

class Limiter:

    def __init__(self, rate, per):
        self.rate = rate      # max tokens = 3
        self.per = per        # per = 6 seconds
        self.bucket = rate    # start full
        self.last = time.time()

    def allow(self, fn):
        now = time.time()
        delta = now - self.last
        self.last = now

        # TODO (line 19): refill bucket properly
        bucket = self.bucket + delta * (self.rate/self.per)

        if bucket > self.rate:
            self.bucket = self.rate
        elif bucket < 1:
            return
        else:
            fn()
            self.bucket = bucket - 1
