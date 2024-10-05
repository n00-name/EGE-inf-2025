ans = 0

def f(n):
    if n > 8:
        return 1
    return 0

for n1 in range(1, 12):
    for n2 in range(0, 12):
        for n3 in range(0, 12):
            for n4 in range(0, 12):
                for n5 in range(0, 12):

                    s = [n1, n2, n3, n4, n5]
                    str_s = ''.join(map(str, s))
                    s_f = f'{f(n1)}{f(n2)}{f(n3)}{f(n4)}{f(n5)}'
                    if str_s.count('7') == 1 and s_f.count('1') <= 3:
                        ans += 1
print(ans) # 34
