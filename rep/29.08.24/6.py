x = '0123456789ABCDEFGHI'

for s in x:
    num_1 = '98897' + s + '21'
    num_2 = '2' + s + '923'

    a = int(num_1, 19) + int(num_2, 19)
    if a % 18 == 0:
        f = a // 18
        print(f)