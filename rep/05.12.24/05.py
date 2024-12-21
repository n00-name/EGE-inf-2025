def f(num):
    summa = sum(list(map(int, num)))
    return summa

for n in range(1, 100):
    num = bin(n)[2:]

    # Если сумма цифр двоичной записи четная
    if f(num) % 2 == 0:
        num = '10' + num[2:] + '0'  # заменяем два первых бита на '10'
    else:
        num = '11' + num[2:] + '1'  # заменяем два первых бита на '11'

    ans = int(num, 2)
    if ans < 35:
        print(n)
