# Функция для перевода числа в систему счисления с основанием 7
def to_base7(n):
    base7 = ""
    while n > 0:
        base7 = str(n % 7) + base7
        n //= 7
    return base7

# Переменные для хранения максимального количества нулей и соответствующего числа
max_zeros = 0
best_number = None

# Проходим все возможные значения x (натуральное число, не превышающее 7400)
for x in range(1, 7**400):
    result = 7**400 + 7**300 - x
    base7_result = to_base7(result)
    zero_count = base7_result.count("0")

    # Обновляем максимум, если найдено больше нулей
    if zero_count > max_zeros:
        max_zeros = zero_count
        best_number = result
    print(max_zeros)

# Выводим результат
print(f"Максимальное количество нулей: {max_zeros}")
print(f"Число в десятичной системе: {best_number}")
print(f"Число в семиричной системе: {to_base7(best_number)}")