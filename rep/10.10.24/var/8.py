from itertools import *
count = 0
for x in product('012345678',repeat=6):
    s=''.join(x)
    if s[0] != '0' and s[0] != '1' and s[0] != '3' and s[0] != '5'and s[0] != '7'and s[-1] != '2' and s[-1] != '3' and s.count('1') >= 2:
        count += 1
print(count)