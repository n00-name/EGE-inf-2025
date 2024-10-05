def to_3(n: int) -> str:
    string = ''
    while n > 0:
        string += str(n % 3)
        n //= 3
    # print(string[::-1])

    return string

for n in range(1, 100):
    n_to_3 = to_3(n)

    if n % 3 == 0:
        num_to_3 = int(f'{n_to_3}{n_to_3[-2:]}')
    else:
        ost = int(to_3((n % 3) * 5))
        num = int(f'{n_to_3}{ost}')

    # print(int(str(n_to_3), 3))

    if int(str(n_to_3), 3) > 133:
        print(n, int(str(n_to_3), 3))