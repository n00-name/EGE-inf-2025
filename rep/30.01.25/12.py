for n in range(3, 10_001):
    s = '1' + '2' * n

    while '12' in s or '3322' in s or '2222' in s:
        if '12' in s:
            s = s.replace('12', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '3322' in s:
            s = s.replace('3322', '21', 1)

    summa = s.count('1') + s.count('2') + s.count('3')

    if summa == 218:
        print(n)
        break