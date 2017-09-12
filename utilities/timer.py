from timeit import default_timer as timer

class TimeCommand:
    def __init__(self, print_log=True, output_precision=2):
        self.print_log = print_log
        self.output_precision = output_precision

    def __enter__(self):
        self.start = timer()
        return self

    def __exit__(self, *args):
        self.end = timer()
        self.elapsed = self.end - self.start
        self.log_time()

    def log_time(self):
        if(self.print_log):
            print(f'Command executed in: {self.elapsed_in_secs} secs')

    @property
    def elapsed_in_secs(self):
        return round(self.elapsed, self.output_precision)