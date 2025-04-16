from itertools import product

ans = 0
for i in product('01234', repeat=5):
    s = ''.join(i)

    if s[0] != '0':
        print(s)

        a = [1 if abs(int(s[int(i)]) - int(s[int(i) + 1])) >= 2 else 0 for i in range(len(s) - 1)]
        print(a)
        
        if any(a) == 1:
            ans += 1

print(ans)
