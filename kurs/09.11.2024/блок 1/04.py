def f(n):
    string = ''
    while n > 0:
        string += str(n % 7)
        n //= 7
    return string[::-1]

x = 12 * 7 ** 135 + 11 * 7 ** 92 - 63 * 7 ** 22 + 17 * 7 ** 11 + 157

x = f(x)
print(len(set(x)))