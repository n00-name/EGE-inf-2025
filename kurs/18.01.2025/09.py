
for i in range(1, 2031):
    x = 6 ** 260 + 6 ** 160 + 6 ** 60 - i

    s = ''
    while x != 0:
        s += str(x % 6)
        x //= 6
    s = s[::-1]

    if s.count('0') == 202:
        print(i)
        break
