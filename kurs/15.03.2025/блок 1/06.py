with open("17-3.txt") as f:
    nums = list(map(int, f.readlines()))

count = 0
min_avg = float('inf')

for i in range(len(nums) - 2):
    a, b, c = nums[i], nums[i + 1], nums[i + 2]

    # Проверяем, что хотя бы одно число кратно 12
    has_multiple_of_12 = (a % 12 == 0) or (b % 12 == 0) or (c % 12 == 0)

    # Проверяем, что все числа делятся на 3
    all_divisible_by_3 = (a % 3 == 0) and (b % 3 == 0) and (c % 3 == 0)

    if has_multiple_of_12 and all_divisible_by_3:
        count += 1
        avg = (a + b + c) / 3
        min_avg = min(min_avg, avg)

print(count, int(min_avg))  # Ответ по условиям задачи - целое число
