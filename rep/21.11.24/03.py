from fnmatch import fnmatch

def sum_even_divisors(x):
    """Возвращает сумму четных делителей числа, если их не менее 4."""
    even_divisors = []
    for i in range(2, x + 1):  # Проверяем все делители числа
        if x % i == 0 and i % 2 == 0:  # Четный делитель
            even_divisors.append(i)
    if len(even_divisors) >= 4:
        return sum(even_divisors)
    return 0

# Список для первых 7 подходящих чисел
results = []

# Перебираем числа, начиная с 65,000
for x in range(65_000, 10**6):  # Ограничиваем диапазон для ускорения
    if fnmatch(str(x), '6*97*5?'):  # Проверяем соответствие маске
        even_div_sum = sum_even_divisors(x)  # Считаем сумму четных делителей
        if even_div_sum > 0:  # Если сумма четных делителей > 0, число подходит
            results.append((x, even_div_sum))
        if len(results) == 7:  # Если нашли 7 чисел, выходим из цикла
            break

# Сортируем результаты по возрастанию чисел (на всякий случай)
results.sort()

# Выводим результаты
for number, divisor_sum in results:
    print(number, divisor_sum)
