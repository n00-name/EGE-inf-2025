with open('17-411-1.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Находим максимальное число, заканчивающееся на 1
max_ending_with_1 = max(num for num in nums if num % 10 == 1)

count = 0
min_sum = float('inf')

# Перебираем все четверки подряд
for i in range(len(nums) - 3):
    quad = nums[i:i + 4]

    # Проверяем, что все элементы меньше максимального числа, оканчивающегося на 1
    if all(x < max_ending_with_1 for x in quad):
        # Проверяем, что количество четных чисел нечетное
        even_count = sum(1 for x in quad if x % 2 == 0)
        if even_count % 2 == 1:
            count += 1
            min_sum = min(min_sum, sum(quad))

print(count, min_sum)
