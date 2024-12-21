from itertools import product

# Все возможные цифры 15-ричной системы
digits = '0123456789ABCDE'

# Счетчик подходящих чисел
count = 0

# Перебираем все пятизначные числа
for num in product(digits, repeat=5):
    # Преобразуем в строку для удобства анализа
    num_str = ''.join(num)

    # Проверяем, что число не начинается с нуля
    if num_str[0] == '0':
        continue

    # Считаем количество цифр 8
    count_8 = num_str.count('8')

    # Считаем количество цифр больше 9 (A, B, C, D, E)
    count_gt_9 = sum(1 for ch in num_str if ch in 'ABCDE')

    # Условия: ровно одна 8 и не менее двух цифр больше 9
    if count_8 == 1 and count_gt_9 >= 2:
        count += 1

print("Количество чисел:", count)