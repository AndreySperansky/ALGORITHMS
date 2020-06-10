"""Генерация списков"""
from timeit import Timer

# Класс для измерения скорости выполнения маленьких фрагментов кода


def test_concat():
    my_lst = []
    for i in range(1000):
        my_lst = my_lst + [i]


def test_cycle():
    my_lst = []
    for i in range(1000):
        my_lst.append(i)


def test_gener():
    my_lst = [i for i in range(1000)]


def test_range():
    my_lst = list(range(1000))


t1 = Timer("test_concat()", "from __main__ import test_concat")
print("concat ", t1.timeit(number=1000), "milliseconds")
t2 = Timer("test_cycle()", "from __main__ import test_cycle")
print("append ", t2.timeit(number=1000), "milliseconds")
t3 = Timer("test_gener()", "from __main__ import test_gener")
print("comprehension ", t3.timeit(number=1000), "milliseconds")
t4 = Timer("test_range()", "from __main__ import test_range")
print("list range ", t4.timeit(number=1000), "milliseconds")
