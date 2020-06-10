"""Фибо через цикл с мемоизацией"""

import timeit


def memorize(func):
    def g(n, memory={0: 0, 1: 1}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


@memorize
def f(n):
    pp = 0
    p = 1
    for i in range(n-1):
        pp, p = p, pp + p
    return p


n = 8

print(timeit.timeit("f(n)", setup="from __main__ import f, n"))
