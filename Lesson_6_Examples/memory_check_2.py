"""Профилировка затрат памяти"""

import copy
from memory_profiler import profile


@profile
def function_1():
    """Выделяет доп память, не освобождается"""
    x = list(range(900000))
    y = copy.deepcopy(x)
    return y


@profile
def function_2():
    """Выделяет доп память, освобождается"""
    x = list(range(100000))
    y = copy.deepcopy(x)
    del x
    y = None
    return y


if __name__ == "__main__":
    function_1()
    function_2()
