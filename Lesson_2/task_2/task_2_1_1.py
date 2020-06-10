def odd_even(NUM):
    ODD = 0
    EVEN = 0
    
    NUM = int(input('Введите число: '))
    TMP = NUM
    while TMP > 0:
        if TMP % 10 % 2 == 0:
            EVEN += 1
        else:
            ODD += 1
        TMP = TMP // 10
    return EVEN, ODD


try:
    NUM = (int(input("Введите натуральное число")))
    print(f'Количество четных и нечетных цифр в числе равно {odd_even(NUM)}')
except ValueError:
    print('Ошибка, нужно ввести целое число!')

