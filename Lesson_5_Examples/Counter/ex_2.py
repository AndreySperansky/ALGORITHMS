"""Класс collections.Counter()"""

from collections import Counter

# коллекция - раскрывается. каждый элемент записывается в нужном количестве
# при этом порядок сохраняется
OBJ = Counter(o=4, p=2, q=0, d=-2, a=1)
print(list(OBJ.elements()))

OBJ = Counter(python=2, java=4, ci=3)
print(list(OBJ.elements()))

print(Counter('abracadabra').most_common(2))
print(Counter('abracadabra').most_common())

OBJ_1 = Counter(a=4, b=2, c=0, d=-2, e=8)
OBJ_2 = Counter(a=1, b=2, c=3, d=4, k=1)
OBJ_1.subtract(OBJ_2)
print(OBJ_1)

OBJ_1 = Counter(a=4, b=2, c=0, d=-2, e=8)
OBJ_2 = Counter(a=1, b=2, c=0, d=4, k=1)

# сложение. складываются значения элементов
# если элемента нет, то его значение - 0
print(OBJ_1 + OBJ_2)

# вычитание. вычитаются значения элементов
# если элемента нет, то его значение - 0
print(OBJ_1 - OBJ_2)

# пересечение. возвращает минимум по соотв. элементам. Если какой-либо
# из элементов имеет значение <= 0, то эти элементы не учитываются
print(OBJ_1 & OBJ_2)

# объединение. возвращает максимум по соотв. элементам
print(OBJ_1 | OBJ_2)
