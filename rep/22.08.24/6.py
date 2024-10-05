with open('17_8.txt', 'r') as f:
    nums = list(map(int, f.read().split()))
print(nums)

count = 0
max_num = -10_000

for num in nums:
    if '4' in str(num):
        count += 1

        if num > max_num:
            max_num = num

print(count, max_num)
