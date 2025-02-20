from itertools import product
count = 0
ans = 0

for i in product('АБОРСУЭ', repeat=5):
    s = ''.join(i)
    count += 1

    if s.count('Р') >= 2 and count % 2 == 0 and s.count('У') == 0:
        lst = ['1' if _ == 'Р' else '0' for _ in s]
        lst = ''.join(lst)
        if lst.count('101') == 1:
            ans += 1
            print(count, s, lst)
print(ans)
