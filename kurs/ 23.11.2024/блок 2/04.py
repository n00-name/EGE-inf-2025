
def f(x):
    s = ''
    while x != 0:
        s += str(x % 5)
        x //= 5
    s = s[::-1]
    return s

nmax = 0
for x in range(1, 7051):
    n = 5 ** 100 - x
    s = f(n)
    count = s.count('0')
    if count == 3:
        nmax = max(nmax, x)
print(nmax)
