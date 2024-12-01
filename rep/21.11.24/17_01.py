with open('17_01_411.txt', 'r') as f:
    nums = list(map(int, f.read().splitlines()))

# Определяем максимальный элемент, заканчивающийся на 1
max_ending_with_1 = max(x for x in nums if x % 10 == 1)

count = 0
min_sum = float('inf')

# Перебираем четверки
for i in range(len(nums) - 3):
    quartet = nums[i:i + 4]
    even_count = sum(1 for x in quartet if x % 2 == 0)

    # Проверяем условия
    if even_count % 2 == 1 and all(x < max_ending_with_1 for x in quartet):
        count += 1
        min_sum = min(min_sum, sum(quartet))

print(count, min_sum)
