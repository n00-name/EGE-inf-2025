def to4cc(num):
    string = ''
    while num > 0:
        string += str(num % 4)
        num //= 4
    return string[::-1]



for i in range(1, 10000):
    n = to4cc(i)

    while int(n) % 4 == 0:
        n += '3'

    f = int(n, 4)
    if f > 1000:
        print(i, f)
        break