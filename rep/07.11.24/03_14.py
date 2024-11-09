def nto(n):
    string = ''
    while n > 0:
        string += str(n % 6)
        n //= 6
    return string[::-1]

for x in range(1, 10001):
    s = 6 ** 900 + 6 ** 10 - x
    s = nto(s)

    if s.count('5') == s.count('3'):
        print(x)
