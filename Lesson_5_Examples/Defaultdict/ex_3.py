"""Класс collections.defaultdict()"""

from collections import defaultdict

LST = [('yellow', 3), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
DEF_DICT = defaultdict(list)
for k, v in LST:
    DEF_DICT[k].append(v)

print(DEF_DICT)
print(DEF_DICT.items())
print(sorted(DEF_DICT.items()))


# defaultdict(<class 'list'>, {'yellow': [3, 3], 'blue': [2, 4], 'red': [1]})
# dict_items([('yellow', [3, 3]), ('blue', [2, 4]), ('red', [1])])
# [('blue', [2, 4]), ('red', [1]), ('yellow', [3, 3])]