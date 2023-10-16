import time
from task2 import task2


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        #print(f"Время выполнения -> {end_time - start_time}")
        return result, end_time - start_time
    return wrapper


@execution_time_decorator
def check_time(n):
    time.sleep(1)
    return n * n


@execution_time_decorator
def task2_5(left, right):
    if right == left:
        return right
    else:
        #time.sleep(1)
        return right * task2(left, right - 1)