def compute_R(N):
    # Двоичная запись числа N
    bin_N = bin(N)[2:]

    # Количество единичных битов в числе N
    count_ones = bin_N.count('1')

    # Добавляем первый бит чётности
    parity_bit_1 = 0 if count_ones % 2 == 0 else 1
    bin_with_parity_1 = bin_N + str(parity_bit_1)

    # Количество единичных битов в числе с первым битом чётности
    count_ones_2 = bin_with_parity_1.count('1')

    # Добавляем второй бит чётности
    parity_bit_2 = 0 if count_ones_2 % 2 == 0 else 1
    bin_R = bin_with_parity_1 + str(parity_bit_2)

    # Возвращаем число в десятичной системе
    return int(bin_R, 2)


# Ищем минимальное N, для которого R больше 103
N = 1
while True:
    R = compute_R(N)
    if R > 103:
        print(f"Минимальное число N: {N}")
        break
    N += 1
