with open('17-1.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

max_end1 = max([n for n in nums if n % 10 == 1])

count = 0
min_sum = float('inf')

# Проходим по всем четверкам
for i in range(0, len(nums) - 3):
    quad = nums[i:i + 4]

    # Проверяем, что все элементы меньше max_end1
    if all(n < max_end1 for n in quad):

        # Находим количество четных элементов
        even_count = sum(1 for n in quad if n % 2 == 0)

        # Проверяем, что количество четных элементов нечетное
        if even_count % 2 == 1:
            count += 1
            quad_sum = sum(quad)
            # Обновляем минимальную сумму
            if quad_sum < min_sum:
                min_sum = quad_sum

print(count, min_sum)
