with open("17-1.txt") as f:
    nums = list(map(int, f.readlines()))

count = 0
min_pair_value = float('inf')

for i in range(len(nums) - 1):
    a, b = nums[i], nums[i + 1]

    # Проверяем, оканчивается ли число на 6 и делится на 3
    def check(n):
        return abs(n) % 10 == 6 and n % 3 == 0

    if check(a) or check(b):
        count += 1
        min_pair_value = min(min_pair_value, a, b)

print(count, min_pair_value)
