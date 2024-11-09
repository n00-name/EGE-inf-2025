from itertools import product

res = set()

for i in product('КАНТ', repeat=6):
    if i.count('К') == 2:
        res.add(i)

print(len(res))
