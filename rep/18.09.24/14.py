x = 4 * 8 ** 3032 + 3 * 16 ** 1956 + 870

s = ''
while x != 0:
    s += str(x % 7)
    x //= 7
s = s[::-1]

print(3 * s.count('3') - s.count('1'))
