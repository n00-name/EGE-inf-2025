with open('06.txt', 'r') as f:
    for line_num, line in enumerate(f, 1):
        # Преобразуем строку в список чисел
        nums = list(map(int, line.split()))

        # Проверяем, что одно число повторяется дважды
        num_counts = {num: nums.count(num) for num in nums}
        repeated = [num for num, count in num_counts.items() if count == 2]

        if len(repeated) == 1:  # Есть только одно число, которое повторяется дважды
            repeated_number = repeated[0]

            # Получаем список уникальных чисел
            unique_numbers = [num for num in num_counts if num != repeated_number]

            if len(unique_numbers) == 4:  # Проверяем, что 4 числа различны
                # Считаем среднее арифметическое этих чисел
                avg = sum(unique_numbers) / 4

                # Проверяем второе условие
                if repeated_number >= avg:
                    print(line_num)
                    break
