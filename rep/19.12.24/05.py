for i in range(100):
    n = bin(i)[2:]
    n = n + str(n.count('1') % 2)
    n = n + str(n.count('1') % 2)

    if int(n, 2) < 90:
        print(int(n, 2))