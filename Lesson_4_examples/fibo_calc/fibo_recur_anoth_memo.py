"""Фибо с рекурсией и упрощенной мемоизацией"""

import sys
import timeit

#sys.setrecursionlimit(10000)
#print(sys.getrecursionlimit())


def f(n, memory=[0, 1]):
    if n < len(memory):
        return memory[n]
    else:
        r = f(n-1) + f(n-2)
        memory.append(r)
        return r


n = 8

print(timeit.timeit("f(n)", setup="from __main__ import f, n"))
