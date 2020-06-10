def recur_reverse(num, flip = 0):
    if num == 0:
        return flip
    else:
        flip = (flip * 10) + (num % 10)
        num = num // 10
        return recur_reverse(num, flip)
    
try:
    NUM = int(input('Введите целое число: '))
    REV_NUM = recur_reverse(NUM)
    print(REV_NUM)
except ValueError:
    print('Ошибка, нужно ввести целое число!')