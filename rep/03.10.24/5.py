def chet(x):
    s = ''
    while x != 0:
        s += str(x % 3)
        x //= 3
    return  s[::-1]


n = 0

for i in range(1, 10000):
    n = i
    s = chet(n)

    if n % 4 == 0:
        n = str(n)
        n = n + s[:-2]
    else:
        n = str(n)
        ost = chet((int(n) % 4) * 2)
        n = n + str(ost)

    f = int(n, 4)
    if f < 369:
        print(i, f)
        break