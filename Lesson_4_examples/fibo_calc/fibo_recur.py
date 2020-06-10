"""Фибо через рекурсию"""

import timeit


def f(n):
    if n < 2:
        return n
    return f(n - 1) + f(n - 2)


n = 8

print(timeit.timeit("f(n)", setup="from __main__ import f, n"))
