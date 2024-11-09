from itertools import permutations

res = set()

for i in permutations('АЙСБЕРГ', 7):
    s = ''.join(i)
    if s[0] != 'Й' and s.count('ЙА') == 0 and s.count('ЙЕ') == 0:
        res.add(i)

print(len(res))
