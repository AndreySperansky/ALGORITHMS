"""Класс collections.OrderedDict()"""

import collections

NEW_DICT = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(NEW_DICT)

NEW_DICT = collections.OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(NEW_DICT)
for key in NEW_DICT:
    print(key, NEW_DICT[key])


my_dict = {"a": "some_value", "b": "other_value", "c": "foo"}
ordered = collections.OrderedDict(sorted(my_dict.items(), key=lambda t: t[0]))

print(ordered)

c = collections.OrderedDict()
for a, b in zip('abc', (1, 2, 3)):
    c[a] = b

print(c)

b = collections.OrderedDict(a=1, b=2, c=3)
print(b)
