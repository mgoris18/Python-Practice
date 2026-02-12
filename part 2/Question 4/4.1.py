import time

class Limiter:

    def __init__(self, rate, per):
        self.rate = rate
        self.per = per
        self.bucket = rate
        self.last = time.time()

    def check(self, fn):
        now = time.time()
        elapsed = now - self.last
        self.last = now

        # TODO (line 17): refill bucket based on elapsed time
        bucket = self.bucket + elapsed * (self.rate/ self.per)

        if bucket > self.rate:
            self.bucket = self.rate
        elif bucket < 1:
            return
        else:
            fn()
            self.bucket = bucket - 1
