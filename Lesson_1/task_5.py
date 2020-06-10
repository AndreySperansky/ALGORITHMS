"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.

Подсказка:
Вводим маленькие латинские буквы.
Обратите внимание, что ввести можно по алфавиту, например, a,z
а можно наоборот - z,a
В обоих случаях программа должна вывести корректный результат.
В обоих случаях он 24, но никак не -24
"""


LETTER_1 = input('Левая буква (a-z): ')
LETTER_2 = input('Правая буква (a-z): ')
NUM_1 = ord(LETTER_1) - ord('a') + 1
NUM_2 = ord(LETTER_2) - ord('a') + 1
DIF = abs(NUM_1 - NUM_2) - 1

print(f'Порядковый номер {LETTER_1} - {NUM_1}')
print(f'Порядковый номер {LETTER_2} - {NUM_2}')
print(f'количество букв между {LETTER_1} и {LETTER_2} - {DIF}')