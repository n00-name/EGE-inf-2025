def f(num):
    summa = sum(list(map(int, num)))
    num = f'{num}{summa % 2}'
    return num


for n in range(1, 100):
    num = bin(n)[2:]

    num = f(num)
    num = f(num)

    ans = int(num, 2)
    if ans < 47:
        print(n)

# ans: 11
