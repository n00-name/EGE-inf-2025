for x1 in range(1, 1000):
    x = 4 * 625 ** 1920 + 4 * 125 ** x1 - 4 * 25 ** 1940 - 3 * 5 ** 1950 - 1960

    s = ''
    while x != 0:
        s += str(x % 5)
        x //= 5
    s = s[::-1]

    if s.count('0') == 1891:
        print(x1)