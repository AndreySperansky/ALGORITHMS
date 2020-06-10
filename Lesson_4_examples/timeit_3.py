import timeit

print(timeit.timeit("x = 2 + 2"))
print(timeit.timeit("x = sum(range(10))"))

print(timeit.timeit("""
for i in range(3): 
    y=i+2 
    a=4 
    if a==y: 
        1/2
"""))
