from itertools import permutations, product
count = 0
for i in product('ЕКМОПРТЬЮ', repeat=5):
    s = ''.join(i)
    count += 1

    if count % 2 == 1 and s[0] == 'Ь' and s.count('К') == 2:
        print(count)