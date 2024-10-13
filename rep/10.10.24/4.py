import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Функция для нахождения максимального четного и нечетного делителя
def find_max_even_odd_divisors(n):
    even_div = None
    odd_div = None
    # Проходим по всем возможным делителям числа
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 == 0:
                even_div = max(even_div, i) if even_div is not None else i
            else:
                odd_div = max(odd_div, i) if odd_div is not None else i

            # Проверяем парный делитель
            pair_div = n // i
            if pair_div != i:
                if pair_div % 2 == 0:
                    even_div = max(even_div, pair_div) if even_div is not None else pair_div
                else:
                    odd_div = max(odd_div, pair_div) if odd_div is not None else pair_div

    return even_div, odd_div


result = []

# Перебираем числа в порядке возрастания, начиная с 250157
for num in range(250157, 1000000):
    even_div, odd_div = find_max_even_odd_divisors(num)

    # Если оба делителя найдены
    if even_div is not None and odd_div is not None:
        A = abs(even_div - odd_div)

        # Проверяем, что A является простым и оканчивается на 9
        if A % 10 == 9 and is_prime(A):
            result.append((num, A))

        # Останавливаем, если найдено 5 чисел
        if len(result) == 5:
            break

# Выводим результат в порядке возрастания чисел
for num, A in result:
    print(num, A)
