x = 9 ** 81 + 27 ** 729 - 4

s = ''
while x != 0:
    s += str(x % 9)
    x //= 9
s = s[::-1]

lst = list(map(int, list(s)))
maxx = str(max(lst))
s = s.replace('0', maxx)
print(s.count(maxx))