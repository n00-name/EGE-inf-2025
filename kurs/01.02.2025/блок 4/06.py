from itertools import product

ans = 0
for i in product('ОНИКС', repeat=4):
    s = ''.join(i)
    if s.count('О') == 1 and s.count('С') == 3:
        ans += 1

for i in product('ОНИКС', repeat=5):
    s = ''.join(i)
    if s.count('О') == 1 and s.count('С') == 3:
        ans += 1

for i in product('ОНИКС', repeat=6):
    s = ''.join(i)
    if s.count('О') == 1 and s.count('С') == 3:
        ans += 1

print(ans)
