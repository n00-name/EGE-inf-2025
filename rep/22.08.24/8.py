with open('17_12.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)

count = 0
max_num = -10_000

for i in range(1, len(nums) - 1):
    if (nums[i - 1] > nums[i] < nums[i + 1]) or (nums[i - 1] > nums[i]) or (nums[i] < nums[i + 1]):
        count += 1

        if nums[i] > max_num:
            max_num = nums[i]
print(count, max_num)
