def recur_sum_seq(i, num, n_count, sum_seq):
    if i == n_count:
        print(f'Количество элементов - {n_count}, их сумма - {sum_seq}')
    elif i < n_count:
        return recur_sum_seq(i + 1, num / (-2), n_count, sum_seq + num)
    

try:
    N_COUNT = int(input('Введите количество элементов: '))
    recur_sum_seq(0, 1, N_COUNT, 0)
except ValueError:
    print('Ошибка, нужно ввести целое число!')