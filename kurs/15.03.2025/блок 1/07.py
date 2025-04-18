with open("17-1.txt") as f:
    nums = list(map(int, f.readlines()))

count = 0
max_local_min = float('-inf')

for i in range(1, len(nums) - 1):  # Проверяем только элементы, у которых есть два соседа
    if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:  # Условие локального минимума
        count += 1
        max_local_min = max(max_local_min, nums[i])

print(count, max_local_min)
