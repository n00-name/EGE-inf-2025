from itertools import product

count = 0
for i in product('ВАЯЮЩИЙ', repeat=7):
    s = ''.join(i)
    if s[0] != 'Й' and (s.count('А') + s.count('Я') + s.count('Ю') + s.count('И') > 0):
        count += 1

print(count)
