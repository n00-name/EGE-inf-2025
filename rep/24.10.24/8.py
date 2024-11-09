def find_divisors_sum(n):
    # Находим минимальный и максимальный делитель, кроме 1 и самого числа
    min_div, max_div = None, None

    # Перебираем делители до sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            min_div = i
            max_div = n // i
            break

    # Если делителей нет, возвращаем 0
    if min_div is None:
        return 0
    # Возвращаем сумму минимального и максимального делителя
    return min_div + max_div


def main():
    count = 0
    num = 700001  # Начинаем с числа 700001

    while count < 5:
        M = find_divisors_sum(num)
        if M != 0 and M % 100 == 14:  # Проверяем, оканчивается ли M на 14
            print(num, M)
            count += 1
        num += 1

main()
