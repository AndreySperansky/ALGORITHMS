from functools import reduce
from memory_profiler import profile

# @profile
# def function_1(max_value):
#     '''
#     :param max_value:
#     :return: сумма квадратов четных числе от 0 до max_value
#     '''
#     gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
#     value = reduce(lambda x, y: x + y, gen)
#     return value
#
#
# print(function_1(999999))

'''
Line #    Mem usage    Increment   Line Contents
================================================
     4     11.6 MiB     11.6 MiB   @profile
     5                             def function_1(max_value):
     6
     7                              :param max_value:
     8                              :return: сумма квадратов четных числе от 0 до max_value
     9
    10     25.0 MiB      0.2 MiB       gen = [x**2 for x in range(1, max_value) if x % 2 == 0]
    11     25.0 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    12     25.0 MiB      0.0 MiB       return value
'''


@profile
def function_2(max_value):
    '''
    :param max_value:
    :return: сумма квадратов четных числе от 0 до max_value
    '''
    gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    value = reduce(lambda x, y: x + y, gen)
    return value

print(function_2(999999))

'''
Line #    Mem usage    Increment   Line Contents
================================================
    28     11.7 MiB     11.7 MiB   @profile
    29                             def function_2(max_value):
    30
    31                                 :param max_value:
    32                                 :return: сумма квадратов четных числе от 0 до max_value
    33
    34     11.7 MiB      0.0 MiB       gen = (x**2 for x in range(1, max_value) if x % 2 == 0)
    35     11.7 MiB      0.0 MiB       value = reduce(lambda x, y: x + y, gen)
    36     11.7 MiB      0.0 MiB       return value

'''

