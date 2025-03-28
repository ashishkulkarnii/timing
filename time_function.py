import time
import typing
import collections

def time_func(func: collections.abc.Callable, tests: list[typing.Any], repeat: int = 1) -> float:
    """Times the passed function using `tests` `repeat` times.
    
    Parameters:
        func (Callable): the function to time
        tests (list[Any]): a list of parameters to test `func`
        repeat (int): the number of times repeat the test
    
    Returns:
        float: the average amount of time taken per function call"""

    times = []
    for _ in range(repeat):
        for test in tests:
            t0 = time.time()
            _ = func(test)
            t1 = time.time()
            times.append(t1 - t0)
    return sum(times) / len(times)
