# def count_cycle(i):
# 	"""Цикл"""
# 	while i >= 0:
# 		print(i, end = ' ')
# 		i -= 1
#
# count_cycle(3)
#
# print('\n ******************************************************************* ')
#
#
# def count_recur(i):
# 	print(i, end = ' ')
# 	# базовый случай
# 	if i <= 0:
# 		return
# 	# рекрсивный случай
# 	count_recur(i-1)
#
# count_recur(3)
import math

print(345//10)
# 34
print(345 % 10)
# 5

print(int(math.log(123, 10)))


def recursion(a, b):
    """Рекурсия"""
    # базовый случай
    # последний шаг рекурсии
    if a == b:
        return str(a)
    # шаг рекурсии
    # рекурсивное условие
    elif a > b:
        return f'{str(a)} {recursion(a - 1, b)}'
    # шаг рекурсии
    # рекурсивное условие
    elif a < b:
        return f'{str(a)} {recursion(a + 1, b)}'


print(recursion(20, 15))
print(recursion(10, 15))