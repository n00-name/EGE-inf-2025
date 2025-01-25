for i in range(100):
    n = bin(i)[2:]

    if i % 2 == 0:
        n = n.replace('1','11')
    else:
        n = n.replace('0','00')

    if int(n, 2) > 70:
        print(i, n, int(n, 2))
        break