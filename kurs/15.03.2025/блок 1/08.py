with open("17-4.txt") as f:
    nums = list(map(int, f.readlines()))

# Находим максимальный элемент, оканчивающийся на 25
max_ending_25 = max(n for n in nums if abs(n) % 100 == 25)

count = 0
max_sum = float('-inf')

for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]

    # Проверяем количество четырёхзначных чисел
    four_digit_count = sum(1000 <= abs(x) <= 9999 for x in (a, b, c))

    # Проверяем условия
    if four_digit_count <= 2 and (a + b + c) <= max_ending_25:
        count += 1
        max_sum = max(max_sum, a + b + c)

print(count, max_sum)
