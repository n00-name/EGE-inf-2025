import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def find_non_prime_divisors(n):
    # Находим все непростые делители числа, кроме 1 и самого числа
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if not is_prime(i):
                divisors.append(i)
            if i != n // i and not is_prime(n // i):
                divisors.append(n // i)
    return divisors

def main():
    count = 0
    num = 912671  # Начинаем с нечётного числа меньше 912673

    results = []  # Для хранения результата

    while num > 0 and count < 5:
        divisors = find_non_prime_divisors(num)
        S = sum(divisors)
        if S > 0 and num % S == 0:  # Проверяем, кратно ли число сумме S
            results.append((num, S))
            count += 1
        num -= 2  # Переходим к следующему нечётному числу

    # Выводим результаты в порядке убывания
    for result in results:
        print(result[0], result[1])

main()
