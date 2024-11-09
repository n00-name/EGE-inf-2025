from itertools import product

res = set()

for i in product('1234', repeat=4):
    s = ''.join(i)
    if s[0] != '1' and s[0] != s[2] and s[1] != s[3]:
        res.add(i)

print(len(res))
