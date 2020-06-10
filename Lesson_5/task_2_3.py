from collections import deque
from itertools import islice

FIRST_NUMBER = deque(list(input('Введите первое число в шестнадцатеричной системе счисления: ')))
SECOND_NUMBER = deque(list(input('Введите второе число в шестнадцатеричной системе счисления: ')))

LIST_OF_NUMBERS = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

if len(FIRST_NUMBER) > len(SECOND_NUMBER):
    FIRST_NUMBER, SECOND_NUMBER = SECOND_NUMBER, FIRST_NUMBER

SECOND_NUMBER.reverse()
THIRD_NUMBER = deque(list())

J = -1
K = 0
for i in SECOND_NUMBER:
    one = LIST_OF_NUMBERS.index(i)
    two = LIST_OF_NUMBERS.index(FIRST_NUMBER[J])
    THIRD_NUMBER.append(LIST_OF_NUMBERS[(one + two + K) % 16])
    if(one + two) >= 15:
        K = 1
    else:
        K = 0
    J -= 1
    if J == -len(FIRST_NUMBER)-1:
        break

DIFFERENT = len(SECOND_NUMBER) - len(FIRST_NUMBER)
SECOND_NUMBER.reverse()
SLICE_DIFF = list(islice(SECOND_NUMBER, 0, DIFFERENT))
if DIFFERENT:
    for i in SLICE_DIFF:
        THIRD_NUMBER.append(LIST_OF_NUMBERS[(LIST_OF_NUMBERS.index(i) + K) % 16])
        if LIST_OF_NUMBERS.index(i) + 1 >= 15:
            K = 1
        else:
            K = 0

if K == 1:
    THIRD_NUMBER.append('1')

THIRD_NUMBER.reverse()
print(list(THIRD_NUMBER))