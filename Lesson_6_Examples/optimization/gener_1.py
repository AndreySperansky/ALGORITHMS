"""Профилировка времени и памяти"""
"""
Генераторам же предшествуют итераторы. 
Когда вы создаёте список, вы можете считывать его 
элементы один за другим — это называется итерацией
"""

import memory_profiler
import time


def check_even_1(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0: 
            even.append(num*num)

    return even


if __name__ == '__main__':

    # левые отсечки времени и памяти
    t1 = time.process_time()
    m1 = memory_profiler.memory_usage()

    cubes = check_even_1(range(100000000))

    # правые отсечки времени и памяти
    t2 = time.process_time()
    m2 = memory_profiler.memory_usage()

    time_diff = t2 - t1
    mem_diff = m2[0] - m1[0]

    print(f"Выполнение заняло {time_diff} сек and {mem_diff} Мб")
