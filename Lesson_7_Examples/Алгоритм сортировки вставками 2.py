"""Сортировка вставками"""
# https://cdn.tproger.ru/wp-content/uploads/2017/09/InsertionSort.gif

import timeit
import random


def insertion_sort(orig_list):
    for i in range(len(orig_list)):
        v = orig_list[i]
        j = i

        while (orig_list[j-1] > v) and (j > 0):

            orig_list[j] = orig_list[j-1]
            j = j - 1

        orig_list[j] = v
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("insertion_sort(orig_list)", \
    setup="from __main__ import insertion_sort, orig_list", number=1000))
