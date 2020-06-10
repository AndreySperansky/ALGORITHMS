"""Фибо через оптимизированную рекурсию с мемоизацией через декоратор"""

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
def decorated_f(n):
    return decorated_f(n - 1) + decorated_f(n - 2)


n = 8

print(timeit.timeit("decorated_f(n)", setup="from __main__ import decorated_f, n"))
