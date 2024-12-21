def f(start, end, count, ans):
    if count == 8 and 1000 <= start <= 1024:
        ans.add(start)
        return 1
    elif start > end or count > 8:
        return 0
    else:
        return f(start + 1, end, count + 1, ans) + f(start + 5, end, count + 1, ans) + f(start * 3, end, count + 1, ans)


ans = set()
f(1, 1024, 0, ans)
print(len(ans))


def f(start, end, count):
    if count == 8:  # Если использовано ровно 8 команд
        return {start} if start >= 1000 and start <= 1024 else set()
    if start > end:  # Если число стало больше конечного диапазона
        return set()

    # Выполнение команд и объединение всех результатов
    return (f(start + 1, end, count + 1) |
            f(start + 5, end, count + 1) |
            f(start * 3, end, count + 1))


# Итерация по всем числам диапазона и добавление их в результат
results = f(1, 1024, 0)
print(len(results))  # Количество уникальных чисел


def f(start, end, count):
    if count == 8:  # Если выполнено ровно 8 команд
        return {start} if 1000 <= start <= 1024 else set()
    if start > end:  # Если число вышло за пределы диапазона
        return set()

    # Рекурсивный вызов для всех операций, объединение результатов
    return (f(start + 1, end, count + 1) |
            f(start + 5, end, count + 1) |
            f(start * 3, end, count + 1))


# Создаем множество для хранения всех достижимых чисел
ans = set()
for i in range(1000, 1024 + 1):
    ans |= f(1, i, 0)  # Начальное число 1
print(len(ans))  # Вывод количества уникальных чисел


def f(start, count, ans):
    if count == 8:  # Если выполнено ровно 8 команд
        if 1000 <= start <= 1024:  # Проверяем, что число в нужном диапазоне
            ans.add(start)
        return
    if start > 1024:  # Если число выходит за пределы верхней границы
        return

    # Рекурсивный вызов для всех операций
    f(start + 1, count + 1, ans)
    f(start + 5, count + 1, ans)
    f(start * 3, count + 1, ans)


ans = set()
f(1, 0, ans)  # Начальное число 1 и количество шагов 0
print(len(ans))  # Вывод количества уникальных чисел

