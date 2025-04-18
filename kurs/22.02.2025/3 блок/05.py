from itertools import permutations

ans = 0
for i in permutations('НОБЕЛИЙ', 7):
    s = ''.join(i)
    if 'Й' != s[0] and not 'ИЙО' in s:
        ans += 1

print(ans)
