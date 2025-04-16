def to_3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s


for i in range(0, 1000):
    n = to_3(i)
    if i % 2 == 0:
        n = '1' + n + '00'
    else:
        n = n + to_3(sum(list(map(int, list(n)))))

    if int(n, 3) > 168:
        print(i)
        break

