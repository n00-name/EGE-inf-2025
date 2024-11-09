
s = 4 ** 812 + 8 ** 800 - 2 ** 3125 - 8 ** 65 - 4 ** 312 + 130
neu_s = bin(s)[3:]
print(neu_s)
f = neu_s.count('0')
print(f)
