from itertools import product

count = 4

for i in product('ИЙКНОСТЧЫ', repeat=9):
    count += 1
    s = ''.join(i)
    print(count, s)
    if s == 'ТОКСИЧНЫЙ':
        print(count, s)
        break