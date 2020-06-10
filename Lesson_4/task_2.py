import timeit

"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""


'''
Решето Сундарама
Алгоритм работает с нечётными натуральными числами большими единицы,
представленными в виде 2m+1, где m является натуральным числом.
Если число 2m+1 является составным, то оно представляется в виде
произведения двух нечётных чисел больших единицы, то есть:
2m+1 = (2i+1)(2j+1)
где i и j — натуральные числа, что также равносильно соотношению:
m = 2ij+i+j.
Таким образом, если из ряда натуральных чисел исключить все числа вида
2ij + i + j  где  1 <= i <= j,  то для каждого из оставшихся чисел m число
2m+1 обязано быть простым. И, наоборот, если число 2m+1 является простым,
то число m невозможно представить в виде 2ij+i+j и, таким образом,
m не будет исключено в процессе работы алгоритма.
'''

def good_prime(n):
    D = int(n / 2)
    B = int(n / 6)
    A = set(range(D))
    for i in range(1, B + 1):
        for j in range(i, int((D + i) / (1 + 2 * i) + 1)):
            A.discard(i + j + 2 * i * j)
    A = [ 2 * x + 1 for x in A ]
    return A

# Num_A = int(input("Введите число до которого нужно найти все простые числа: "))
# print(good_prime(Num_A))

# Решето Сундарама

def sundaram(n):
    b = list()
    a = [0] * n


    i = k = j = 0
    while 3 * i + 1 < n:
        while k < n and j <= i:
            a[k] = 1
            j += 1
            k = i + j + 2 * i * j
        i += 1
        k = j = 0
    
    for i in range(1, int(n/2)):
        if a[i] == 0:
            b.append(2 * i + 1)
    return b

# Num_B = int(input("Введите число до которого нужно найти все простые числа: "))
# print(sundaram(int(Num_B)))

'''
Метод определения простых чисел проверкой каждого
'''


def sort_out_each(n):
    arr = []
    for k in range(2, n + 1):
        prime = True
        for i in range(2, k):
            if k % i == 0:
                prime = False
                break
        
        if prime:
            # print(k, end = ' ')
            arr.append(k)
    return arr

# Num_C = int(input("Введите число до которого нужно найти все простые числа: "))
# print(sort_out_each(Num_C ))



"""
РЕШЕТО ЭРАТОСФЕНА
1. Выписать подряд все целые числа от двух до n (2, 3, 4, …, n).
2. Пусть переменная p изначально равна двум — первому простому числу.
3. Вычеркнуть из списка все числа от 2p до n, делящиеся на p (то есть, числа 2p, 3p, 4p, …)
4. Найти первое не вычеркнутое число, большее чем p, и присвоить значению переменной p это число.
5. Повторять шаги 3 и 4 до тех пор, пока p не станет больше, чем n
Все не вычеркнутые числа в списке — простые числа.
"""

def primes(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1
    
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0
    m = 2                       # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:                # перебор всех элементов до заданного числа
        if a[m] != 0:           # если он не равен нулю, то
            j = m * 2           # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0        # заменить на 0
                j = j + m       # перейти в позицию на m больше
        m += 1
    
    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    
    del a
    return b


# Num_D = int(input("Введите число до которого нужно найти все простые числа: "))
# print(primes(Num_D))


'''
На практике, алгоритм можно немного улучшить следующим образом.
На шаге №3, числа можно вычеркивать, начиная сразу с числа p^2, потому что
все составные числа меньше его уже будут вычеркнуты к этому времени.
И, соответственно, останавливать алгоритм можно, когда p^2 станет больше, чем n.
Можно показать, что сложность алгоритма составляет O(n log(log n))
операций в модели вычислений RAM, или O(n(log n)(log(log n))) битовых операций.
'''

print(timeit.timeit("good_prime(100)", setup="from __main__ import good_prime"))

print(timeit.timeit("sundaram(100)", setup="from __main__ import sundaram"))

print(timeit.timeit("sort_out_each(100)", setup="from __main__ import sort_out_each"))

print(timeit.timeit("primes(100)", setup="from __main__ import primes"))

# Время выполнения алгоритма для n = 10

# 3.717317004
# 3.90931611
# 5.02270323
# 4.4517578360000005

# Время выполнения алгоритма для n = 100

# 23.240734292
# 43.543278949000005
# 116.43406107599999
# 42.640629456
'''
По результатам замеров времни исполнения алгоритмов ожидаемо наихудший результат продемонстрировал
третий алгоритм нахожения простых чисел методом проверки каждого числа
так как его сложность можно описать как o(n^2)  тогда как у остальных - O(n log(log n). Его отставание
по эффективности особенно заметно по мере увеличения n.
'''
