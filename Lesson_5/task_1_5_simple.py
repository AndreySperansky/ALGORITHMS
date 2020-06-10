import functools
from collections import defaultdict

def calc():
    nums = defaultdict(list)
    for d in range(2):
        n = input(f'Введите {d+1}-e натуральное шестнадцатеричное число: ')
        nums[f"{d+1} - {n}"] =  list(n)
    print(nums)
    
    summ = sum([int(''.join(i), 16) for i in nums.values()])
    # %X Число в шестнадцатеричной системе счисления (буквы в верхнем регистре)
    print("Сумма: ", list('%X' % summ))
    
    mult = functools.reduce(lambda a,b: a * b, [int(''.join(i), 16) for i in nums.values()])
    
    print("Произведение: ", list('%X' % mult))

calc()