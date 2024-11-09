from itertools import product

res = set()

for i in product('МУХА', repeat=5):
    if i.count('У') <= 3:
        res.add(i)

print(len(res))
