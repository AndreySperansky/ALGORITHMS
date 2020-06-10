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

Num_C = int(input("Введите число до которого нужно найти все простые числа: "))
print(sort_out_each(Num_C))

