
def f(x):
    s = ''
    while x != 0:
        s += str(x % 7)
        x //= 7
    s = s[::-1]
    return s

for x in range(0, 2030, 1):

    s = 7 ** 170 + 7 ** 100 - x

    if f(s).count('0') == 71:
        print(x)

