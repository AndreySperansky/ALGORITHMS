# for j in range(10 , -5, -1):

# input = [{1: 2}, {2: 2}, {1: 3}, {2: 1}, {1: 3}]
#
# r = {}
# for d in input:
#
# # (assumes just one key/value per dict)
#     ((x, y),) = d.items()
#     print(x, y)
#     r.setdefault(x, []).append(y)
#
# print([{k: v} for (k, v) in r.items()])

def hexadd(x, y):
    summa = (int(x, 16) + int(y, 16))
    return summa


a = input('Введите 1-е шестнадцатиричное число: ').upper()
b = input('Введите 2-е шестнадцатиричное число: ').upper()
print(a, b)

print('%X' % (hexadd(a, b)))

# Введите 1-е шестнадцатиричное число: 1ff
# Введите 2-е шестнадцатиричное число: cbb
# 1FF CBB
# 0xeba