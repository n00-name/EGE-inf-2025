x = 6 ** 203 + 5 * 6 ** 405 - 3 * 6 ** 144 + 77

s = ''
while x != 0:
    s += str(x % 6)
    x //= 6
s = s[::-1]

print(s.count('5'))