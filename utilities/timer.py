from timeit import default_timer as timer

class Timer:
    def __enter__(self):
        self.start = timer()
        return self

    def __exit__(self, *args):
        self.end = timer()
        self.elapsed = self.end - self.start

    @property
    def elapsed_in_secs(self, precision=2):
        return round(self.elapsed, precision)