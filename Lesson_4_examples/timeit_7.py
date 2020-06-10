import time
import timeit


class TestClass():
    def some_slow_method(self, loop_count):
        for i in range(loop_count):
            time.sleep(1)

    def some_quick_method(self, loop_count):
        for i in range(loop_count):
            time.sleep(0.1)


if __name__=='__main__':
    # Для того что бы воспользоваться классом необходимого модуля,
    # его необходимо импортировать в инициализирующем выражении setup

    setup = """
from __main__ import TestClass
test=TestClass()
"""
    statements = ['test.some_slow_method(5)',
                  'test.some_slow_method(3)',
                  'test.some_quick_method(5)',
                  'test.some_quick_method(3)']

    for item in statements:
        print('%s execute in %s seconds' % (item, min(timeit.repeat(item, setup, timeit.default_timer, 3, 1))))
