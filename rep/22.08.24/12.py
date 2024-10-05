from fnmatch import *

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

for i in range(0, 10**9, 2273):

    if fnmatch(str(i), '5*35?5*1'):
        summa = sum(list(map(int, str(i))))

        if is_prime(summa):
            print(i, i // 2273)

