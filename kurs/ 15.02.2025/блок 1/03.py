def get_new_number(N):
    binary_N = bin(N)[2:]

    ones_count = binary_N.count('1')

    if ones_count % 2 == 0:
        binary_N += '1'
    else:
        binary_N += '0'

    if ones_count % 2 == 0:
        binary_N += '1'
    else:
        binary_N += '0'

    return int(binary_N, 2)


N = 1
while True:
    R = get_new_number(N)
    if R > 54:
        print(f"Минимальное число R: {R} для N = {N}")
        break
    N += 1
