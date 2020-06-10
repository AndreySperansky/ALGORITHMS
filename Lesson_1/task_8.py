"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

Подсказка:
Год является високосным в двух случаях:
 1. он кратен 4 но при этом не кратен 100,
 2. либо кратен 400.

Попробуйте решить задачу двумя способами:
1. Обычное ветвление
2. Тернарный оператор

П.С. - Тернарные операторы, также известные как условные выражения,
представляют собой операторы, которые оценивают что-либо на основе условия,
являющегося истинным или ложным. Он был добавлен в Python в версии 2.5 .
Он просто позволяет протестировать условие в одной строке,
заменяя многострочное if-else, делая код компактным.
"""


# YEAR = None
#
# while not isinstance(YEAR, int) :
# 	YEAR = input('Введите год: ')
# 	try:
# 		YEAR = int(YEAR)
# 	except ValueError:
# 		print('Ошибка, нужно вводить целое число!')
# if YEAR % 4 != 0:
# 	print('Обычный год')
# elif YEAR % 100 == 0:
# 	if YEAR % 400 == 0:
# 		print('Виссокосный год')
# 	else:
# 		print('Обычный год')
# else:
# 	print('Високосный год')
#

#
# # РЕШЕНИЕ С ПОМОЩЬЮ ТЕРНАРНОГО ОПЕРАТОРА
#
#
# while not isinstance(YEAR, int):
# 	YEAR = input('Введите год: ')
# 	try:
# 		YEAR = int(YEAR)
# 	except ValueError:
# 		print('Ошибка, нужно вводить целое число!')
#
# print("Обычный год" if YEAR % 4 != 0  or (YEAR % 100 == 0 and YEAR % 400 != 0) else "Високосный год" )


def f_year(YEAR):
    if YEAR % 400 == 0 or YEAR % 4 == 0 and YEAR % 100 != 0:
        return print(f"Год {YEAR} - високосный")
    return print(f"Год {YEAR} - невисокосный")


try:
    Y = int(input("Введите год: "))
    f_year(Y)

except:
    print("Вместо числа введена строка!")