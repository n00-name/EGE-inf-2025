with open("17-3.txt") as f:
    nums = list(map(int, f.readlines()))

count = 0
max_sum = float('-inf')

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]

    # Проверяем чётность и делимость
    if ((a % 2 == 0 and a % 4 == 0 and b % 2 != 0 and b % 11 == 0) or
        (b % 2 == 0 and b % 4 == 0 and a % 2 != 0 and a % 11 == 0)):
        count += 1
        max_sum = max(max_sum, a + b)

print(count, max_sum)
