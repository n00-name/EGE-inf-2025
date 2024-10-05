with open('17_12.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)

count = 0
min_num = 10_000

for num in nums:
    if num % 35 == 0 and num % 2 != 0 and num % 11 != 0 and num % 91 != 0:
        count += 1

        if min_num > num:
            min_num = num
print(min_num, count)