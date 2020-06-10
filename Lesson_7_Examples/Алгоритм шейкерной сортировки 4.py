"""Шейкерная сортировка"""
# https://otvet.imgsmail.ru/download/50c5ded7efd57c41dca80cc4bb33be3e_i-1175.gif

import random
import timeit

'''
разновидность пузырьковой сортировки.
Отличается тем, что просмотры элементов выполняются
один за другим в противоположных направлениях,
при этом большие элементы стремятся к концу массива,
а маленькие - к началу.
'''


def cocktail_sort(orig_list):
    left = 0
    right = len(orig_list) - 1
    while left <= right:
        for i in range(left, right):
            if orig_list[i] > orig_list[i+1]:
                orig_list[i], orig_list[i+1] = orig_list[i+1], orig_list[i]
        right -= 1
        for i in range(right, left, -1):
            if orig_list[i-1] > orig_list[i]:
                orig_list[i], orig_list[i-1] = orig_list[i-1], orig_list[i]
        left += 1
    return orig_list


orig_list = [random.randint(-100, 100) for _ in range(10)]

# замеры 10
print(timeit.timeit("cocktail_sort(orig_list)", \
    setup="from __main__ import cocktail_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(timeit.timeit("cocktail_sort(orig_list)", \
    setup="from __main__ import cocktail_sort, orig_list", number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(timeit.timeit("cocktail_sort(orig_list)", \
    setup="from __main__ import cocktail_sort, orig_list", number=1000))
