import time


class TimerNotStarted(Exception):
    pass


class Timer:
    def __init__(self):
        self.start_time = 0

    def set_start_time(self):
        self.start_time = time.time()

    def get_calculation_time(self):
        if self.start_time == 0:
            raise TimerNotStarted("Timer has not been started yet.")

        return time.time() - self.start_time
