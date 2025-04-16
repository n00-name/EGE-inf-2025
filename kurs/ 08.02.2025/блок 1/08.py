with open('08.txt', 'r') as f:
    count = 0  # Счётчик строк, удовлетворяющих условиям

    for line in f:
        # Преобразуем строку в список чисел
        nums = list(map(int, line.split()))

        # Подсчитаем количество каждого числа
        num_counts = {num: nums.count(num) for num in nums}

        # Найдём максимальное число в строке
        max_num = max(nums)

        # Проверяем, что максимальное число не повторяется
        if num_counts[max_num] == 1:
            # Собираем все повторяющиеся числа
            repeated_sum = sum(num * num_counts[num] for num in num_counts if num_counts[num] > 1)

            # Проверяем, что сумма всех повторяющихся чисел меньше максимального числа
            if repeated_sum < max_num:
                count += 1

    # Выводим количество строк, удовлетворяющих всем условиям
    print(count)
