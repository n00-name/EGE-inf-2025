def nto(n):
    string = ''
    while n > 0:
        string += str(n % 7)
        n //= 7
    return string[::-1]

mx = -1
for x in range(1, 7**20):
    s = 7 ** 100 + 7 ** 30 - x
    s = nto(s)

    if s.count('0'):
        mx = max(mx, s.count('0'))
        print(mx)
