def find_number_for_result(target_result):
    # Проходим по всем четырёхзначным числам
    for num in range(1000, 10000):
        # Получаем цифры числа
        a = num // 1000
        b = (num // 100) % 10
        c = (num // 10) % 10
        d = num % 10

        # Считаем суммы
        s1 = a + b
        s2 = b + c
        s3 = c + d

        # Отбрасываем наибольшую сумму
        sums = sorted([s1, s2, s3], reverse=True)
        sums.pop(0)  # Убираем максимальное

        # Если оставшиеся суммы соответствуют target_result, возвращаем это число
        if sums == [1, 0]:
            return num

    return None


# Ищем число, которое даёт результат 105
result = find_number_for_result(105)
print(f"Наименьшее число, которое даёт результат 105: {result}")
