from itertools import permutations

res = set()

for i in permutations('КАЛИЙ', 5):
    s = ''.join(i)
    if s.count('ИА') == 0 and s[0] != 'Й':
        res.add(i)

print(len(res))
