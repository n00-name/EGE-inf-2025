from itertools import product
count = 0
for i in product('МОТЮ', repeat=5):
    s = ''.join(i)
    count += 1
    print(count, s)

    if s[0] == 'Т':
        break
