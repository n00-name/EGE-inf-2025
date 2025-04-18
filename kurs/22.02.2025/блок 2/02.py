for n in range(1, 10):

    s = '21' * n + '1' * (10 - n)
    while '21' in s:
        s = s.replace('21', '6', 1)

    if s.count('1') + s.count('2') + s.count('6') == 50:
        print(n)