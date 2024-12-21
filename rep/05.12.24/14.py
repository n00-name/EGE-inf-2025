def CC(n):
    s = ''
    while n > 0:
        s += str(n % 9)
        n //= 9
    return s[::-1]

lst = []
for x in range(1, 2001):
    s = 9 ** 250 + 9 ** 150 - x
    lst.append(s)

ans = [str(x).count('1') for x in lst]
maxx = max(ans)
print(ans.index(maxx))