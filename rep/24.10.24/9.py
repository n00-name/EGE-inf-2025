def is_palindrome(x):
    # Проверяем, является ли число палиндромом
    s = str(x)
    return s == s[::-1]

def find_divisors(n):
    # Находим все нетривиальные делители числа
    divisors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors

def main():
    count = 0
    num = 520001  # Начинаем с числа 520001

    while count < 5:
        divisors = find_divisors(num)
        if divisors:
            div_sum = sum(divisors)
            if is_palindrome(div_sum):  # Проверяем, является ли сумма делителей палиндромом
                print(num, max(divisors))  # Выводим число и его максимальный делитель
                count += 1
        num += 1

main()
