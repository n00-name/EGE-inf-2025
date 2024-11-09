from itertools import product

count = 0
for i in product('КОСУФ', repeat=5):
    s = ''.join(i)
    count += 1
    if s.count('Ф') == 0 and s.count('У') == 2:
        print(count, s)
