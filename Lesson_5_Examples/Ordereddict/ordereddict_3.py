from collections import OrderedDict

"""В Python 3.5 и более ранних обычный dict, вы заметите, что данные в нем неупорядоченные"""

NEW_DICT = {'python': 3, 'java': 4, 'perl': 1, 'javascript': 2}
print(NEW_DICT)

"""Бывают ситуации, когда нужно выполнить цикл над ключами 
в словаре в определенном порядке. Например, 
нужно отсортировать ключи, 
чтобы перебрать их по порядку."""

KEYS = NEW_DICT.keys()
KEYS = sorted(KEYS)

for key in KEYS:
    print(key, NEW_DICT[key])

# теперь OrderedDict

DCT = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
NEW_DICT = OrderedDict(sorted(DCT.items()))

print(NEW_DICT)

for key in NEW_DICT:
    print(key, NEW_DICT[key])
