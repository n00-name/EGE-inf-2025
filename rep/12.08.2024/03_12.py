for n in range(4, 10_000):
    s = '4' + '1' * n

    while '31' in s or '411' in s or '1111' in s:

        if '31' in s:
            s = s.replace('31', '1', 1)
        if '411' in s:
            s = s.replace('411', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '4', 1)

    suma = sum(list(map(int, s)))

    if suma == 36:
        print(n)  # 514
        break