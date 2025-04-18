with open("17.txt") as f:
    numbers = list(map(int, f.readlines()))

# Найдём минимальный элемент в последовательности
min_element = min(numbers)
min_last_digit = abs(min_element) % 10  # Последняя цифра модуля минимального элемента

count = 0  # Количество подходящих троек
max_abs_sum = 0  # Максимальный модуль суммы таких троек

# Перебираем тройки
for i in range(len(numbers) - 2):
    a, b, c = numbers[i], numbers[i + 1], numbers[i + 2]

    # Подсчёт количества отрицательных и положительных чисел в тройке
    negative_count = sum(1 for x in (a, b, c) if x < 0)
    positive_count = sum(1 for x in (a, b, c) if x > 0)

    triplet_sum = a + b + c

    # Проверяем условия
    if negative_count > positive_count and abs(triplet_sum) % 10 == min_last_digit:
        count += 1
        max_abs_sum = max(max_abs_sum, abs(triplet_sum))

print(count, max_abs_sum)
