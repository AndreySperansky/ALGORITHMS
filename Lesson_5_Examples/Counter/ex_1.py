"""collections - Высокопроизводительный контейнер типов данных"""
"""Collections — это встроенный модуль Python, реализующий специализированный 
контейнер типов данных. Является альтернативой встроенным контейнерам общего 
назначения Python, таким как dict, list, set и tuple."""

"""Класс collections.Counter()"""

from collections import Counter

# создаем объект коллекции
OBJ = Counter()
# считаем количество неизменяемых элементов и сохраняем данные в коллекции
# ключ - сам элемент, значение - количество таких элементов
for lang in ['js', 'java', 'java', 'python', 'python', 'python']:
    OBJ[lang] += 1
# выводим коллекцию
print(OBJ)

# извлекаем количество элементов 'python'
print(OBJ['python'])
print(OBJ['perl'])

# еще можно так
OBJ = Counter(['js', 'java', 'java', 'python', 'python', 'python'])
print(OBJ)

# еще пример - коллекция на основе последовательности
OBJ = Counter('abrakadabra')
print(OBJ)

# еще пример - коллекция на основе отображения
OBJ = Counter({'python': 4, 'java': 2})
print(OBJ)

# еще пример - коллекция на основе аргументов
OBJ = Counter(python=4, java=8)
print(OBJ)
