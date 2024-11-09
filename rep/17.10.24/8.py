from itertools import product
count = 0
ans = 0
for i in product('НФОРМАТИ', repeat=5):
    count += 1
    s = ''.join(i)

    if s[0] == 'Т' and s.count('И') == 0:
        print(count)
        break