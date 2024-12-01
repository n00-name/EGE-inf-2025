from itertools import permutations

def count_numbers():
    base = 15  # Основание системы счисления
    digits = "0123456789ABCDE"  # Все цифры 15-ричной системы
    count = 0

    # Генерация всех пятизнaчных чисел
    for perm in permutations(digits, 5):
        num = ''.join(perm)

        # Условие 1: Ровно одна цифра 8
        if num.count('8') != 1:
            continue

        # Условие 2: Не менее двух цифр > 9 (A, B, C, D, E, F)
        high_digits_count = sum(1 for ch in num if ch in "ABCDE")
        if high_digits_count < 2:
            continue

        # Условие 3: Число не должно начинаться с нуля
        if num[0] == '0':
            continue

        count += 1

    return count

result = count_numbers()
print(f"Количество подходящих чисел: {result}")
