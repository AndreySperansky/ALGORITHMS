"""Быстрая сортировка"""
# https://cdn.tproger.ru/wp-content/uploads/2017/09/ezgif.com-video-to-gif-17.gif

import timeit
import random


def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    else:
        q = random.choice(orig_list)
        L = []
        M = []
        R = []
        for elem in orig_list:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quick_sort(L) + M + quick_sort(R)


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("quick_sort(orig_list)", \
    setup="from __main__ import quick_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("quick_sort(orig_list)", \
    setup="from __main__ import quick_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("quick_sort(orig_list)", \
    setup="from __main__ import quick_sort, orig_list", number=1000))
