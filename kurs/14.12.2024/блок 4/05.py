from itertools import permutations
count = 1
for s in permutations('АДКНОРТ', 7):
    print(count, ''.join(s))
    count += 1
