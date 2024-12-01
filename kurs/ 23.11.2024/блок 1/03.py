
def f(x):
    s = ''
    while x != 0:
        s += str(x % 6)
        x //= 6
    s = s[::-1]
    return s

nmax = 0
for x in range(1, 2031):
    n = 6 ** 2030 + 6 ** 100 - x
    s = f(n)
    count = s.count('0')
    nmax = max(nmax, count)
    print(nmax)
print(nmax)
