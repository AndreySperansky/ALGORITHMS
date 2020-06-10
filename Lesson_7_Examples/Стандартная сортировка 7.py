"""Стандартная сортировка"""

"""
Внутри Python использует Timsort – гибридный алгоритм сортировки, 
сочетающий сортировку вставками и сортировку слиянием. 
Смысл в том, что в реальном мире часто встречаются частично 
отсортированные данные, на которых Timsort работает ощутимо 
быстрее прочих алгоритмов сортировки. Сложность по времени: 
O(n log n) в худшем случае и O(n) – в лучшем.
"""

import timeit
import random


def reverse_sort(orig_list):
    ordered_list = sorted(orig_list)
    return ordered_list


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
