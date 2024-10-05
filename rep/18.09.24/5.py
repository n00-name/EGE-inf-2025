for n in range(1, 100):
    num = bin(n)[2:]


    if sum(list(map(int, num))) % 2 == 1:
        num = num + '11'
    else:
        num = '11' + num

    ans = int(num, 2)
    if ans < 102:
        print(n, ans)

# ans: 11
