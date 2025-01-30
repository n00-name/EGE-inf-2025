from itertools import product

count = 0
ans = 0
for i in product('АВИОРТФ', repeat=6):
    count += 1
    s = ''.join(i)
    print(count, s)

    if count % 2 == 0 and s[0] != 'О' and s.count('Р') == 2:
        ans += 1
print(ans)