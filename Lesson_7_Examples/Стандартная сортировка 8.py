"""Стандартная сортировка"""

import timeit
import random


def reverse_sort(orig_list):
    orig_list.sort()
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("reverse_sort(orig_list)", \
    setup="from __main__ import reverse_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("reverse_sort(orig_list)", \
    setup="from __main__ import reverse_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("reverse_sort(orig_list)", \
    setup="from __main__ import reverse_sort, orig_list", number=1000))
