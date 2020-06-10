"""Фибо через цикл"""

import timeit


def f(n):
    if n < 2:
        return n
    pp = 0
    p = 1
    for i in range(n-1):
        pp, p = p, pp + p
    return p


n = 8

print(timeit.timeit("f(n)", setup="from __main__ import f, n"))
