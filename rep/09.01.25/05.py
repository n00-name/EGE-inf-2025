from itertools import *
alph = list(range(20))
cnt = 0
for s in product(alph, repeat=5):
    if s[0] + s[-1] == 26:
        if all(s[j-1] % 2 != s[j] % 2 for j in range(1, 5)):
            cnt += 1
print(cnt)


from itertools import *
from string import *
alph = (digits + ascii_uppercase)[:20]
cnt = 0
for i in product(alph, repeat=5):
    s = ''.join(i)
    if int(s[0],20)+int(s[-1],20) == 26:
        for c in alph:
            if alph.index(c) % 2 == 0: s = s.replace(c,'0')
            else: s = s.replace(c,'1')
        if '00' not in s and '11' not in s:
            cnt += 1
print(cnt)