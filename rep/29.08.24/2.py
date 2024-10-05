from fnmatch import *

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

for i in range(0, 10**10, 1917):

    if fnmatch(str(i), '3?12?14*5'):

        print(i, i // 1917)

