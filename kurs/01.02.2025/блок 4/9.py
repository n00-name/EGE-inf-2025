for x in range(111):
    s1 = x * 111 ** 3 + 3 * 111 ** 2 + 2 * 111 ** 1 + 1
    s2 = 1 * 211 ** 3 + 7 * 211 ** 2 + x * 211 ** 1 + 4

    f = s1 + s2
    if f % 111 == 0:
        print(f / 111)