"""Сортировка слиянием"""
# https://cdn.tproger.ru/wp-content/uploads/2017/09/MergeSort.gif

import timeit
import random


def merge_sort(orig_list):
    if len(orig_list) > 1:
        center = len(orig_list) // 2
        left = orig_list[:center]
        right = orig_list[center:]

        merge_sort(left)
        merge_sort(right)

        # перестали делить
        # выполняем слияние
        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                orig_list[k] = left[i]
                i += 1
            else:
                orig_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            orig_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            orig_list[k] = right[j]
            j += 1
            k += 1
        return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("merge_sort(orig_list)", \
    setup="from __main__ import merge_sort, orig_list", number=1000))
