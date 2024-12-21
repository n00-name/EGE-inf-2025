filename = '9-246.txt'

# Счетчик строк, удовлетворяющих условию
count = 0

# Открываем файл и обрабатываем построчно
with open(filename, 'r') as file:
    for line in file:
        # Преобразуем строку в список чисел
        numbers = list(map(int, line.split()))

        # Находим наибольшее и наименьшее числа
        max_num = max(numbers)
        min_num = min(numbers)

        # Считаем сумму двух оставшихся чисел
        sum_others = sum(numbers) - max_num - min_num

        # Проверяем условие
        if max_num + min_num <= sum_others:
            count += 1

print("Количество строк:", count)