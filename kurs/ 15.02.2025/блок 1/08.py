# Функция для проверки, можно ли восстановить исходное число N для данного числа R
def can_generate_r(r):
    # Преобразуем число R в двоичную строку
    binary_r = bin(r)[2:]

    # Если длина двоичной записи меньше 4 или больше 6, это некорректное число
    if len(binary_r) < 4 or len(binary_r) > 6:
        return False

    # Получаем биты чётности из последнего и предпоследнего разряда
    parity1 = int(binary_r[-1])  # Первый бит чётности
    parity2 = int(binary_r[-2])  # Второй бит чётности

    # Оставляем только часть числа без бит чётности
    truncated_binary = binary_r[:-2]

    # Подсчитываем количество единиц в обрезанном числе
    ones_count = truncated_binary.count('1')

    # Проверяем на корректность бит чётности
    if (ones_count % 2 == 0 and parity1 != 0) or (ones_count % 2 != 0 and parity1 != 1):
        return False
    if ((ones_count + parity1) % 2 == 0 and parity2 != 0) or ((ones_count + parity1) % 2 != 0 and parity2 != 1):
        return False

    # Если все проверки пройдены, значит число R может быть получено
    return True


# Считаем количество чисел R в диапазоне от 16 до 32, которые не могут быть получены
count = 0
for r in range(16, 33):
    if not can_generate_r(r):
        count += 1

# Выводим результат
print(count)
