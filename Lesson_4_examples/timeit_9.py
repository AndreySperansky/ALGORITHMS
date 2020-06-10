import timeit

print(timeit.timeit('for i in range(10): test.append(i)', setup='test = []'))
print(timeit.timeit('for i in range(10): test[i] = i', setup='test = {}'))

"""
Словарь основан на хешировании (хеш-таблицы),
поэтому он намного быстрее, чем списки
"""