def f(start, end, forbidden_ends, last_command, contains_60):
    # Если текущая точка = конечной, проверяем, содержится ли 60
    if start == end:
        return 1 if contains_60 else 0

    # Если текущая точка больше конечной или содержит число, оканчивающееся на 3, или запрещено два вычитания подряд
    if start > end or start % 10 == 3:
        return 0

    count = 0

    # Проводим операции
    if last_command != 'A':  # Не допускаем двух вычитаний подряд
        count += f(start - 1, end, forbidden_ends, 'A', contains_60 or start - 1 == 60)  # A: вычесть 1

    if last_command != 'B':  # Не допускаем двух вычитаний подряд
        count += f(start - 5, end, forbidden_ends, 'B', contains_60 or start - 5 == 60)  # B: вычесть 5

    count += f(start + 7, end, forbidden_ends, 'C', contains_60 or start + 7 == 60)  # C: прибавить 7
    count += f(start * 2, end, forbidden_ends, 'D', contains_60 or start * 2 == 60)  # D: умножить на 2

    return count


# Запуск функции с начальным значением 9, конечным 84 и проверкой на наличие числа 60 на пути
print(f(9, 84, [], '', False))
