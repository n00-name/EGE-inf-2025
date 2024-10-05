from fnmatch import *

def f(x):
    count = 0
    for i in range(2, (x // 2) + 1):
        if x % i == 0 and i % 2 == 0:
            count += 1
    if count >= 4:
        return True
    return False

count = 0
for i in range(65_000, 10**9):

    if fnmatch(str(i), '6*97*5?') and f(i):
        count += 1
        print(i, i // 2273)

    if count == 7:
        break

