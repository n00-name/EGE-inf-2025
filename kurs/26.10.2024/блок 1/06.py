from itertools import product

res = set()

for i in product('МОИСЕЙ', repeat=4):
    s = ''.join(i)
    if s[0] != 'Й' and s.count('О') + s.count('И') + s.count('Е') >= 1:
        res.add(i)

print(len(res))
