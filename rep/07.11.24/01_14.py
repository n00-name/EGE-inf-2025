def to_base_n(number, base):
    """Преобразует десятичное число в указанную систему счисления и возвращает в виде строки."""
    if number == 0:
        return "0"
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join(str(x) for x in digits[::-1])


# Вычисляем значения степеней
power1 = 9 ** 250
power2 = 9 ** 150
target_sum = power1 + power2
max_ones = 0
best_x = 0

# Перебираем возможные значения x и находим лучшее
for x in range(2001):
    current_value = target_sum - x
    base_9_representation = to_base_n(current_value, 9)
    count_ones = base_9_representation.count("1")

    if count_ones > max_ones:
        max_ones = count_ones
        best_x = x

print("Максимальное значение x:", best_x)
print("Количество цифр '1' в записи:", max_ones)
