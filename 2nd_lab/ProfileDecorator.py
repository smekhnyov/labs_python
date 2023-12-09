import time
import threading


class ProfileDecorator:
    def __init__(self, func):
        self.func = func
        self.lock = threading.Lock()
        self.calls = 0
        self.total_time = 0

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()

        with self.lock:
            self.calls += 1
            self.total_time += end_time - start_time

        return result

    def get_stats(self):
        with self.lock:
            return self.calls, self.total_time

    def clear_stats(self):
        with self.lock:
            self.calls = 0
            self.total_time = 0