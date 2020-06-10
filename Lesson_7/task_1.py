"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit


def stone_sort(arr):
    n = 1
    
    while n < len(arr):
        flag = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        n += 1
    return arr







def stone_sort_upd(arr):
    n = 1
    
    while n < len(arr):
        flag = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag += 1
                # flag = 1  # можно и так
                # print(flag)
        if flag == 0:
            break
        
        n += 1
        
    return arr


array = [random.randint(-100, 100) for _ in range(10)]
print(f'Массив: {array}')

# array = [9, 8, 7, 6, 5, 4, 3, 2, 1]


print(f'Массив после сортировки: {stone_sort(array)}')
print(f'Массив после доработанной сортировки: {stone_sort_upd(array)}')

print(timeit.timeit("stone_sort(array)", setup="from __main__ import stone_sort, array"))
print(timeit.timeit("stone_sort_upd(array)", setup="from __main__ import stone_sort_upd, array"))

# 11.800576525
# 1.9652219199999994

'''
Замеры по времени показали, что усовершенствованный алгоритм работает почти в 6 раз быстрее(!)
за счет сокращения "холостых" пробегов по циклу в случае если элементы уже отсортированы
'''
