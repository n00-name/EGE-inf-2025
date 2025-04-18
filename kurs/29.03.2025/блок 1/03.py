def div(x):
    s = {1}
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            s.add(i)
            s.add(x // i)

    sorted(list(s))
    ans = [x for x in s if x % 2 != 0]
    return sum(ans)




from fnmatch import fnmatch
num = 1404
del_ = 217
start = num - num % del_

for i in range(start, 10**7, del_):
    if fnmatch(str(i), '14?4*'):
        #print(i, div(i))
        pass

import fnmatch

lst = []

for i in range(10**7 - 1, 1, -1):
    if fnmatch.fnmatch(str(i), '14?4*') and i % 217 == 0:
        lst.append(i)
        if len(lst) == 7:
            break

lst.sort()

for n in lst:
    odd_divisors_sum = sum(j for j in range(1, n + 1, 2) if n % j == 0)
    print(n, odd_divisors_sum)
