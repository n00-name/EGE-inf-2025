from itertools import permutations

res = set()

for i in permutations('ПРИКАЗ', 4):
    s = ''.join(i)
    if s.count('И') + s.count('А') <= 1:
        res.add(i)

print(len(res))
