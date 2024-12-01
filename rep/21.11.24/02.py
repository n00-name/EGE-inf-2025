from fnmatch import fnmatch

# Инициализация словаря для хранения чисел по их суммам цифр
sum_to_numbers = {}

# Перебор всех чисел, кратных 2023, в заданном диапазоне
for x in range(10**9, 10**10, 2023):
    if fnmatch(str(x), '1*1'):  # Проверяем маску
        digit_sum = sum(map(int, str(x)))  # Считаем сумму цифр числа
        # Добавляем число в список по ключу суммы цифр
        if digit_sum not in sum_to_numbers:
            sum_to_numbers[digit_sum] = []  # Если суммы еще нет, создаем новый список
        sum_to_numbers[digit_sum].append(x)  # Добавляем число в список

# Вывод максимальной суммы и соответствующих чисел
max_sum = max(sum_to_numbers.keys())  # Находим максимальную сумму цифр
print(f"Максимальная сумма цифр: {max_sum}")
print("Числа с этой суммой:")
for num in sum_to_numbers[max_sum]:
    print(num, num // 2023)
