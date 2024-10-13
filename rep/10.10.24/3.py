def find_min_max_divisors(n):
    divisors = []
    # Проходим по всем возможным делителям числа
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)

    if divisors:
        return min(divisors), max(divisors)
    else:
        return None


result = []

# Перебираем числа в порядке убывания от 999999 до 1
for num in range(999999, 1, -1):
    divisors = find_min_max_divisors(num)
    if divisors:
        min_div, max_div = divisors
        M = min_div + max_div

        # Проверяем, оканчивается ли M на 18
        if M % 100 == 18:
            result.append((num, M))

        # Останавливаем поиск, когда нашли 5 чисел
        if len(result) == 5:
            break

# Выводим результат в порядке возрастания чисел
result.sort()

for num, M in result:
    print(num, M)
