def dell(x):
    arr = []
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            arr.append(i)
    return arr

count = 0
for i in range(150_000, 10**6):

    lst = dell(i)
    summa = sum(lst)

    if summa % 13 == 10:
        count += 1
        print(count, i, summa)

    if count >= 7:
        break


