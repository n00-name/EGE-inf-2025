with open('17var01.txt', 'r') as f:
    nums = tuple(map(int, f.read().splitlines()))
print(nums)

mn = 100_000
for num in nums:
    if num % 100 == 25:
        mn = min(mn, num)
print(mn)

count = 0
mx = -1
for i in range(0, len(nums) - 2):

    summa = nums[i + 1] + nums[i] + nums[i + 2]

    if (len(str(nums[i])) == 2 or len(str(nums[i + 1])) == 2 or len(str(nums[i + 2])) == 2) and summa < mn:
        count += 1
        mx = max(mx, summa)

print(count, mx)