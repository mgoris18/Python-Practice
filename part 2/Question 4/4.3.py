import time

class Limiter:

    def __init__(self, rate, per):
        self.rate = rate   # 10 tokens
        self.per = per     # per 5 seconds
        self.bucket = rate
        self.last_check = time.time()

    def hit(self, fn):
        current = time.time()
        elapsed = current - self.last_check
        self.last_check = current

        # TODO (line 21): refill bucket
        bucket = self.bucket + elapsed * (self.rate/self.per)
        
        if bucket > self.rate:
            self.bucket = self.rate
        elif bucket < 1:
            return
        else:
            fn()
            self.bucket = bucket - 1
