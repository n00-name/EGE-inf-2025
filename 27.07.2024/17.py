with open('17var16.txt', 'r') as f:
    nums = f.read().splitlines()
print(nums)

count = 0
min_summ = 100_000
for i in range(0, len(nums) - 1):
    if int(nums[i][-1]) % 2 == 1 and int(nums[i + 1][-1]) % 2 == 1 and int(nums[i][-1]) != int(nums[i + 1][-1]):
        count += 1
        if min_summ > (abs(int(nums[i])) * abs(int(nums[i + 1]))):
            min_summ = (abs(int(nums[i])) * abs(int(nums[i + 1])))

print(count, min_summ) # ans: 864 4683
