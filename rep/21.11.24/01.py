from fnmatch import fnmatch

def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


for x in range(0, 10**9, 2267):
    if fnmatch(str(x), '7*15?3*7') and is_prime(sum(list(map(int, str(x))))):
        print(x, x//2267)