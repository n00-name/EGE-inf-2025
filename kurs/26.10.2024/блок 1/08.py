from itertools import permutations

# Возможные цифры (от 0 до 9)
digits = "0123456789"
# Результат для семизначных чисел, делящихся на 5
count = 0

# Перебираем возможные окончания 0 и 5
for last_digit in '05':
    # Из оставшихся цифр выбираем 6, чтобы сформировать 7-значное число
    for perm in permutations(digits.replace(last_digit, ''), 6):
        number = ''.join(perm) + last_digit

        # Проверка, что все цифры различны и условия четности соблюдаются
        valid = True
        for i in range(len(number) - 1):
            # Проверяем, чтобы две четные или две нечетные цифры не стояли рядом
            if (int(number[i]) % 2 == int(number[i + 1]) % 2):
                valid = False
                break
        # Если условие выполнено, увеличиваем счетчик
        if valid:
            count += 1

print(count)
