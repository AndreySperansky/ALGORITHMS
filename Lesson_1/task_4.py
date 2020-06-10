"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

Подсказка:
Нужно обойтись без ф-ций randint() и uniform()
Использование этих ф-ций = задание не засчитывается

Функцию random() использовать можно
Опирайтесь на пример к уроку
"""

from random import random

LEFT = int(input("Минимальная граница: "))
RIGHT = int(input("Максимальная граница: "))
NUMB = int(random() * (RIGHT - LEFT + 1)) + LEFT
print(NUMB)

LEFT = float(input("Минимальная граница: "))
RIGHT = float(input("Максимальная граница: "))
NUMB = random() * (RIGHT - LEFT) + LEFT
print(round(NUMB, 3))

LEFT = input('Левая буква (a-z): ')
RIGHT = input('Правая буква (a-z): ')
LETTER = chr(int(random() * (ord(RIGHT) - ord(LEFT)+ 1) + ord(LEFT)))
print(LETTER)

