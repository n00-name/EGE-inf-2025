def is_true_for_all_A(A):
    for x in range(1, 200):  # Проверяем для всех натуральных x (ограничиваем до 200)
        # Выражение ДЕЛ(x, A)
        DEL_x_A = (x % A == 0)

        # Условие x ∈ [70, 90]
        in_interval = (70 <= x <= 90)

        # Условие ¬ДЕЛ(x, 22)
        not_DEL_x_22 = (x % 22 != 0)

        # Логическое выражение
        expr = DEL_x_A or (not in_interval or not_DEL_x_22)

        # Если для какого-то x выражение не истинно, то A не подходит
        if not expr:
            return False
    return True


# Поиск наибольшего A
max_A = 0
for A in range(1, 200):  # Проверяем все A от 1 до 200
    if is_true_for_all_A(A):
        max_A = A

print(max_A)
