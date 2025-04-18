# Функция для вычисления результата по алгоритму
def get_result(number):
    # Преобразуем число в список цифр
    digits = [int(digit) for digit in str(number)]

    # Вычисляем суммы
    sum1 = digits[0] + digits[1]
    sum2 = digits[1] + digits[2]
    sum3 = digits[2] + digits[3]

    # Формируем список из этих сумм
    sums = [sum1, sum2, sum3]

    # Отбрасываем наименьшую сумму
    sums.remove(min(sums))

    # Сортируем оставшиеся суммы по убыванию
    sums.sort(reverse=True)

    # Возвращаем результат как строку, объединяя оставшиеся суммы
    return int(''.join(map(str, sums)))


# Ищем наибольшее четырёхзначное число, при котором результат работы автомата равен 1414
for number in range(9999, 999, -1):
    if get_result(number) == 1414:
        print(f"Наибольшее число: {number}")
        break
