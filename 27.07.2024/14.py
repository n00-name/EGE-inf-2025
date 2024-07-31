x = 3 ** 333 + 3 ** 22 - 9 ** 111 - 8

s = ''
while x != 0:
    s += str(x % 3)
    x //= 3
s = s[::-1]

print(s.count('2')) # ans 131
