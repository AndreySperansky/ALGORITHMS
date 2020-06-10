
import hashlib


user_str = input('Введите строку состоящую из маленьких букв\n')
lists = []
for i in range(0, len(user_str) + 1):
    for j in range(i + 1, len(user_str) + 1):
        lists.append(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())

lists.remove(hashlib.sha1(user_str.encode('utf-8')).hexdigest())


print(f'Колличество различных подстрок в строке {user_str} равно {len(set(lists))}')



# ***************************************************************************************************************

def substring_count(user_str):
    """
    функция принимает на вход строку состоящую только из маленьких латинских букв
    функция возвращает количество различных подстрок с использованием хеш-функции
    """

    h = []
    for i in range(0, len(user_str) + 1):
        for j in range(i + 1, len(user_str) + 1):
            h.append(hashlib.sha1(user_str[i:j].encode('utf-8')).hexdigest())

    h.remove(hashlib.sha1(user_str.encode('utf-8')).hexdigest())
    return h


some_string = 'papa'

print(f'Колличество различных подстрок в строке {some_string} равно {len(set(substring_count(some_string)))}')