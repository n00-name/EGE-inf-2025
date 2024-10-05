with open('17_4.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)

count = 0
min_summ = 100_000

max_num = max(nums)

summa_sred = 0
count_sred = 0

for i in range(0, len(nums) - 1):
    if str(nums[i])[-1] == '3':
        summa_sred += nums[i]
        count_sred += 1
sred = summa_sred / count_sred
print(sred)


for i in range(0, len(nums) - 1):
    if (max_num % nums[i] == 0 or max_num % nums[i + 1] == 0) and (nums[i] + nums[i + 1]) > sred:
        count += 1
        if nums[i] + nums[i + 1] < min_summ:
            min_summ = nums[i] + nums[i + 1]

print(count, min_summ) # ans: 72 795
