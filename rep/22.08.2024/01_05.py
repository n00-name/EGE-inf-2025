def f(num):
    summa = sum(list(map(int, num)))
    if summa % 2 == 0:
        num = '110' + num[3:] + '10'
        return num
    elif summa % 2 == 1:
        num = '10' + num[2:] + '101'
        return num


for n in range(1, 100):
    num = bin(n)[2:]

    num = f(num)

    ans = int(num, 2)
    if ans > 120:
        print(n)  # ans: 16
        break
