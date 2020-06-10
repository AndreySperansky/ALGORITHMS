import copy
import timeit
from random import randint
#from statistic import median


def mediana(arr):
    temp = arr
    lows = []
    highs = []
    for i in range(len(temp)):
        for j in range(len(temp)):
            if temp[i] > temp[j]:
                lows.append(temp[j])
            if temp[i] < temp[j]:
                highs.append(temp[j])
            if temp[i] == temp[j] and i > j:
                lows.append(temp[j])
            if temp[i] == temp[j] and i < j:
                highs.append(temp[j])
        if len(lows) == len(highs):
            return temp[i]
        lows.clear()
        highs.clear()
        
def mediana_2(arr):
    '''
    Возвращаем медиану массива путем удаления максимальных элементов
    пока максимальным не будет медиана
    :param arr:
    :return:
    '''
    tmp = arr
    for i in range(len(arr) // 2):
        tmp.remove(max(tmp))
    return max(tmp)
    
    
