"""Профилировка затрат памяти"""

import copy
from memory_profiler import profile


@profile
def function_1():
    """Значительный инкремент"""
    x = list(range(10000000))
    y = copy.deepcopy(x)
    return y


function_1()
