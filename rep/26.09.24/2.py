with open('17var02.txt', 'r') as f:
    nums = tuple(map(int, f.read().splitlines()))
print(nums)

mx = -1
for num in nums:
    if num % 1000 == 100:
        mx = max(mx, num)
print(mx)

count = 0
mx_n = -1
for i in range(0, len(nums) - 2):

    summa = nums[i + 1] + nums[i] + nums[i + 2]

    if ((len(str(nums[i])) == 3 and len(str(nums[i + 1])) == 3 and len(str(nums[i + 2])) != 3) or \
        (len(str(nums[i])) == 3 and len(str(nums[i + 1])) != 3 and len(str(nums[i + 2])) == 3) or \
        (len(str(nums[i])) != 3 and len(str(nums[i + 1])) == 3 and len(str(nums[i + 2])) == 3)) and \
            summa <= mx:

        count += 1
        mx_n = max(mx_n, summa)
print(count, mx_n)