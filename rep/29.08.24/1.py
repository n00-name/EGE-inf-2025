def f(x):
    minn = 0
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            minn = i
            break

    if minn == 0 or x == minn or minn == 1:
        return 0

    summa = minn + (x // minn)
    return summa

count = 0
for i in range(800_000, 10**7):

    summa = f(i)

    if summa % 10 == 4:
        count += 1
        print(i, summa)

    if count >= 5:
        break


