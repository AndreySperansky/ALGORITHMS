"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЗДЕСЬ ДОЛЖНА БЫТЬ РЕАЛИЗАЦИЯ ЧЕРЕЗ РЕКУРСИЮ
"""


def recur_method(num, s= 0, m = 1):
    if s == m:
        print(f'Равентство: {s == m}')
    elif s <= m:
        return recur_method(num, s + 1, num * (num + 1) // 2)
    else:
        return recur_method(num, s - 1, num * (num + 1) // 2)
    
try:
    numb = int(input("Введите число: "))
    recur_method(numb)
except ValueError:
    print("Вы ввели строку!")