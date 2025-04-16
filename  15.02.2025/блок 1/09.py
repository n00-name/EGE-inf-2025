# Функция для обработки числа N
def process_number(N):
    # Шаг 1: Строим восьмибитную двоичную запись числа N
    binary_N = format(N, '08b')

    # Шаг 2: Инвертируем биты (заменяем 0 на 1 и 1 на 0)
    inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary_N)

    # Шаг 3: Переводим инвертированную строку в десятичное число
    inverted_number = int(inverted_binary, 2)

    # Шаг 4: Вычисляем разницу между инвертированным числом и исходным
    result = inverted_number - N
    return result


# Ищем число N, при котором разница будет равна 99
for N in range(256):  # Диапазон от 0 до 255
    if process_number(N) == 99:
        print(f"Число, которое нужно ввести в автомат: {N}")
        break
