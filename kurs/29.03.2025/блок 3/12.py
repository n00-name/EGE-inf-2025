for n in range(41, 1000):
    s = '>' + '0' * n + '1' * n + '2' * n

    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '00>', 1)
        if '>0' in s:
            s = s.replace('>0', '11>', 1)

    s = s.replace('>', '1', 1)
    summa = sum(map(int, list(s)))
    if summa % 100 == 77:
        print(n)
        break