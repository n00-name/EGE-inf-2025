lst = []
for n in range(4, 10_000):
    s = '1' + '9' * n

    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9')
        elif '49' in s:
            s = s.replace('49', '91')
        elif '999' in s:
            s = s.replace('999', '4')

    lst.append(sum(list(map(int, s))))
print(max(lst))