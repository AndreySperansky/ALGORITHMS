

from collections import Counter
import hashlib


string = list('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab')


s = 0
substring = Counter()

for letter_start in range(len(string)):


    if s == 0:
        e = len(string) - 1
    else:
        e = len(string)

    for letter_end in range(e - s):
        hash_obj = hashlib.md5()

        hash_obj.update(''.join(string[s:e]).encode())
        substring[hash_obj.hexdigest()] += 1
        if len(string[s:e]) == 1:
            print(string[s:e], hash_obj.hexdigest())
        e -= 1
    s += 1

