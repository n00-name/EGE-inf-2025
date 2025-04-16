with open('07.txt', 'r') as f:
    for line_num, line in enumerate(f, 1):
        # Преобразуем строку в список чисел
        nums = list(map(int, line.split()))

        # Проверяем, что два числа повторяются дважды, а остальные три уникальны
        num_counts = {num: nums.count(num) for num in nums}

        repeated_twice = [num for num, count in num_counts.items() if count == 2]
        unique_numbers = [num for num, count in num_counts.items() if count == 1]

        if len(repeated_twice) == 2 and len(unique_numbers) == 3:  # Условие на повторяющиеся и уникальные числа
            # Проверяем, что максимальное число не повторяется
            max_num = max(nums)
            if num_counts[max_num] == 1:
                # Вычисляем сумму чисел в этой строке
                print(sum(nums))
                break
