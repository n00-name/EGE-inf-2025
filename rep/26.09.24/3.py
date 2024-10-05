with open('17var04.txt', 'r') as f:
    nums = tuple(map(int, f.read().splitlines()))
print(nums)

mn = 100_000
for num in nums:
    if str(num)[-3:] == '700':
        mn = min(mn, num)
print(mn)


count = 0
mn_n = 1_000_000
for i in range(0, len(nums) - 2):

    summa = nums[i] + nums[i + 1] + nums[i + 2]
    if not(len(str(abs(nums[i]))) == 5 and len(str(abs(nums[i + 1]))) == 5 and len(str(abs(nums[i + 2]))) == 5) and summa > mn:
        count += 1

        mn_n = min(mn_n, summa)
print(count, mn_n)