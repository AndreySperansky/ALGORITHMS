"""Сортировка выбором"""
# https://cdn.tproger.ru/wp-content/uploads/2017/09/select-sort.gif

import timeit
import random


def selection_sort(orig_list):
    for i in range(len(orig_list)):
        idx_min = i
        for j in range(i+1, len(orig_list)):
            if orig_list[j] < orig_list[idx_min]:
                idx_min = j

        tmp = orig_list[idx_min]
        orig_list[idx_min] = orig_list[i]
        orig_list[i] = tmp

    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("selection_sort(orig_list)", \
    setup="from __main__ import selection_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("selection_sort(orig_list)", \
    setup="from __main__ import selection_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("selection_sort(orig_list)", \
    setup="from __main__ import selection_sort, orig_list", number=1000))
