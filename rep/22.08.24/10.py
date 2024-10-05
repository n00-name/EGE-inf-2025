def f(x):
    dif = 0
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            dif = i
            break

    if dif == 0 or x == dif:
        return 0

    return x // dif - dif

count = 0
for i in range(350_000, 10**7):

    dif = f(i)

    if dif % 23 == 9:
        count += 1
        print(count, i, dif)

    if count >= 6:
        break


